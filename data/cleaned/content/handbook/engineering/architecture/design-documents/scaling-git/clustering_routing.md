---
title: "Scaling Git: Clustering and Routing"
description: "Proposed design for clustering and routing in Gitaly"
status: proposed
creation-date: "2026-07-15"
authors: [ "@jamesliu-gitlab" ]
owning-stage: "~group::gitaly"
participating-stages: [ "~group::git" ]
toc_hide: false
---

This document describes a proposed MVP for clustering and routing in Gitaly,
and how the new cluster is expected to be configured by administrators.

## Scope

### MVP

The initial cut of the clustering and routing layer will implement a subset of
the total functionality. This aims to validate the overall approach to
horizontal scalability and provide immediate value to customers.

The goals are to:

1. Enable a fixed-size cluster of Gitaly nodes to be exposed as a single storage
   to Rails.
1. Allow for a fixed $k$ value to be configured. See [Rendezvous hashing](#rendezvous-hashing)
   for more information on $k$.
1. Maintain cache stickiness via the [routing](#routing) layer, using a
   weighted rendezvous hashing scheme with equal weights.
1. Perform routing through [redirects](#redirects) instead of proxying.

### Future work

As the MVP rolls out to customers and we gain a better understanding of how the
cluster operates in practice, we will start considering the following
enhancements:

1. Cluster auto-scaling. This will likely be limited to Kubernetes deployments.
1. Setting per-repository $k$ values. This requires a globally-consistent source
   of repository metadata that all nodes can query, or it can be provided by
   clients through gRPC metadata or headers.
1. Using health or resource usage metrics to influence routing by adjusting the
   node weights at runtime.
1. Cache-prewarming. With an adjustable $k$ value, the likelihood that a node is
   serving a repository for the very first time increases significantly.
   Pre-warming will be critical.
1. The use of Kubernetes-native constructs like a service mesh to perform
   routing and clustering, as described in
   [this Kubernetes-native routing proposal](https://gitlab.com/gitlab-org/gitaly/-/work_items/7259).
1. More sophisticated policies on cluster autoscaling and load distribution. The
   custom [HELP protocol](https://gitlab.com/gitlab-org/gitaly/-/work_items/7214)
   is a good example of what could be possible.
1. Policy-driven routing decisions. This allows Gitaly clients (like Rails) to
   influence routing behaviour by specifying business requirements. For example,
   a requirement might be that Gitaly nodes within Europe should handle a given
   request, or that requests for a given repository should be distributed across
   three nodes.

## Clustering

We will implement a gossip network-based, eventually-consistent cluster that can
be easily scaled elastically. This is in contrast to Praefect where it’s
difficult to scale up as configuration on existing Praefect nodes need to be
updated. Gossip networks are also simpler to implement compared to a consensus
network like Raft, and does not require durable storage of runtime cluster
state.

The [memberlist](https://github.com/hashicorp/memberlist) package is the gossip
network implementation we aim to use. It builds on top of the SWIM protocol and
makes some enhancements to reduce flapping. Flapping is when nodes in the
network are repeatedly marked as dead despite that they’re functioning properly.
This leads to a lot of unnecessary churn in the composition of the cluster. The
memberlist package also provides the ability for a node joining the network to
send arbitrary metadata up to 512 bytes in size. Metadata updates can also be
sent at any time. The size restriction is in place because SWIM piggy-backs
these payloads off UDP health probes. Memberlist will also periodically attempt
to reconcile node metadata through TCP.

The drawbacks of a gossip network are:

1. The inability to propagate heavyweight state.
1. Its eventual consistency model.
1. The risk of a split-brain scenario due to a network partition or other
   failure.

Some of the guarantees we can no longer make under this model (without
augmenting it with additional components) are:

1. Enforcing exactly one writer for a given repository.
1. Write serialisation for concurrent operations for a given repository.

This means that it can be possible, under some scenarios, for more than one
Gitaly node to be issuing concurrent writes to a given repository. Conflicts may
arise when writing the next generation object, which will be dealt with
separately.

Given that local Gitaly disks are no longer the source of truth for durable
storage, these are acceptable tradeoffs to make for the sake of an architecture
that is simpler to implement, simpler to debug, and simpler to operate.

Existing storage systems like
[CockroachDB](https://github.com/cockroachdb/cockroach/blob/master/pkg/gossip/gossip.go)
and [Apache Cassandra](https://cassandra.apache.org/doc/3.11/cassandra/architecture/dynamo.html)
already use this form of eventually-consistent clustering. The original
[DynamoDB paper](https://dl.acm.org/doi/10.1145/1323293.1294281) also describes
the use of a gossip network.

### Joining the cluster

The cluster should scale from a single node to an arbitrary number of nodes.

A cluster begins with the creation of a single node via `gitaly serve`.
Subsequent nodes are joined to the cluster by starting them with a special flag
containing the address of an existing node. For example:

```bash
# Start the first node, listens on http://gitaly-1.internal
$ gitaly serve

# Start another node and join it to the first
$ gitaly serve --join-addr http://gitaly-1.internal
```

Several things happen when a new node joins the cluster:

1. The gossip protocol propagates the event across existing members. The new
   joiner is also made aware of the composition of the cluster.
1. Each node updates their local runtime state to reflect the expanded cluster.
1. The local cache of the new joiner is proactively warmed according to the
   repositories it's meant to serve.

It is important that the cluster can be established correctly despite the
following constraints:

- Nodes are started concurrently.
- Nodes are started in any order.
- The node(s) specified in `--join-addr` are unreachable because they're
  still starting up.

### Leaving the cluster

A node either leaves the cluster voluntarily (because the cluster is being
scaled down), or does so because it has become unhealthy or dead. These
scenarios are handled differently:

1. When a node leaves voluntarily, it should perform a graceful shutdown and
   communicate that it’s leaving to the rest of the cluster. This allows a
   period of time where dispatched requests can still be served by the node, and
   peer nodes can update their internal state.
1. When a node is unhealthy or dies, the gossip network will mark it in a
   "suspected" state as the node will fail to respond to a health probe. The
   suspected timeout is configurable and is designed to prevent the flapping
   issue described earlier. If the node continues to be unresponsive, it will be
   marked as failed.

Once other nodes in the cluster become aware of this change, they update their
local state to reflect that the cluster has shrunk.

### Contacting the cluster

Gitaly clients must contact the cluster using a means of service discovery. For
example, the addresses of nodes within the cluster could be exposed as a DNS
record.

This is the [current recommended approach](https://docs.gitlab.com/administration/gitaly/praefect/configure/#service-discovery)
for a Praefect cluster, so should be well-supported by clients.

### Cluster state

The beauty of this approach to clustering is that we’re not required to persist
any kind of hard state to durable storage. The composition of the cluster is
exclusively defined and maintained at runtime, and all runtime state is
considered ephemeral.

The entire cluster can be destroyed and recreated without any kind of data loss.

## Routing

Routing is achieved across today’s standalone Gitaly nodes through Rails, as it
keeps a persistent mapping of repositories to the Gitaly storage responsible for
serving that repository. The same Gitaly node always serves the same repository.
Praefect introduced a level of indirection called "virtual storages", which
exposed a cluster of Gitaly nodes as a single storage.

In the new cluster, routing will be handled internally. There will be no
separate routing/coordination layer like we have with Praefect; every node has
the dual responsibility of routing and serving requests. A single storage
representing the entire cluster will be exposed to Rails.

We may add support for policy-based routing in the future, where clients have
more control over routing decisions. For example, a Rails configuration could
specify that requests to `repo-a` should be distributed across `x` replicas, or
requests to `repo-d` should be served from Europe. Gitaly would then attempt to
honour this on a best-effort basis.

Every node must strive to make the same routing decision for a given repository.
If a client asks for `repo-a`, the request should be ultimately served by the
same node (or subset of nodes) regardless of which one the client first
contacts. The number of nodes serving a given repository should be configurable.

The primary reason for this is to maintain cache stickiness. Since repository
data must first be downloaded from S3 onto a node’s local disk before a request
can be served, it is advantageous for the same nodes to own the same
repositories.

### Rendezvous hashing

Given the constraints of the gossip network explained above, routing decisions
cannot be made by consulting a large shared table of repositories. Instead, we
use a [weighted rendezvous hashing](https://en.wikipedia.org/wiki/Rendezvous_hashing)
mechanism so nodes can make routing decisions independently and without prior
knowledge of all repositories in existence. The algorithm takes an "object" as
an input, and hashes it to $1 \leq k \leq N$ "sites":

1. Our objects will be repository identifiers.
1. $k$ is the number of nodes we wish to distribute the repository across.
1. $N$ is the total number of nodes in the cluster.
1. A site is the address of the Gitaly node destined to serve the request.

Rendezvous hashing is a generic mechanism that can be implemented using a
variety of non-cryptographic hashing schemes. Configuring the hasher with the
same seed for every node in the cluster guarantees the same output for a given
input. We [explored several options](https://gitlab.com/gitlab-org/gitaly/-/work_items/7168)
and selected `xxh3`, which had the best key distribution for small and large
clusters.

At runtime, each node maintains a conceptual "hash ring". Sites are added and
removed from the ring as nodes join and leave the cluster.

The weighted aspect of weighted rendezvous hashing allows each site to have a
corresponding weight. Sites with higher weights are more likely to be routed to.
This provides the future ability to dynamically adjust the routing policy at
runtime, and could be useful for example to reduce traffic flowing to a node
under resource contention.

### Redirects

If the node contacted by the client is not the node that should serve the
request, there needs to be a mechanism in place to route the request to the
appropriate node. There are broadly two approaches to achieve this:

1. Client redirects, where the node tells the client to contact someone else.
1. Proxying, where the node transparently proxies the existing request to
   someone else.

Historically, Praefect nodes would proxy requests to the target Gitaly node,
which made them susceptible to performance issues. Namely, long-running requests
would hold precious resources of the Praefect node, and in some situations, the
Praefect node would become a bottleneck.

Redirects address these issues at the expense of extra client-side processing.
The biggest challenge is that unlike HTTP, gRPC does not support redirects at
the protocol level. Redirects must be implemented by the application, i.e.
Gitaly must include some indication in its response that a redirect is
necessary, and the client must understand this and contact the appropriate node.

Supporting redirects thus requires two changes:

1. Gitaly gRPC response messages need to be updated to include the ability to
   specify a redirect.
1. Gitaly clients need to be updated to direct the same request elsewhere, if
   asked to.

## Configuration

Standalone Gitaly nodes are not difficult to operate. Configuration is largely
limited to various runtime tunables, address bindings for the gRPC service and
Prometheus metrics, and the storage disk. Praefect introduces more complexity as
it has a separate routing and coordination layer, and the size of the cluster is
statically-defined in configuration.

The new cluster should be easy to operate. There should be minimal configuration
introduced and the composition of the cluster itself should not be
statically-defined in a file. The following new configuration keys are required
at a minimum:

1. Whether the new cluster functionality is active, since we need to continue
   supporting existing Gitaly deployments.
1. The port on which the gossip network should listen on.
1. $k$; the number of nodes that should serve a given repository.
