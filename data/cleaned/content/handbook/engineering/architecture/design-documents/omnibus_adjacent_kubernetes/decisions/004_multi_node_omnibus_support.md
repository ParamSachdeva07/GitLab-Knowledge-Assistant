---
title: "ADR-004: Multi-node Omnibus support in OAK"
owning-stage: "~devops::gitlab delivery"
toc_hide: true
---

## Summary

OAK supports multi-node Omnibus deployments. Network configuration and
service exposure are the customer's responsibility. The automation
planned for the Beta phase, combined with existing Omnibus settings,
covers what customers need to get up and running. Anything beyond that
is out of scope — Omnibus only manages its own node and has no knowledge
of or control over other nodes in the deployment.

## Context

Multi-node Omnibus refers to deployments where Omnibus components are
distributed across separate virtual machines: Rails, Sidekiq, PostgreSQL,
Redis, and Gitaly on distinct nodes. This is common when components need
to be split for scaling.

A proof-of-concept validating a multi-node Omnibus deployment
with OpenBao on GKE established the following:

1. No Omnibus configuration changes are required beyond standard
   multi-node Omnibus settings.
2. Network configuration is customer-specific and depends on their
   infrastructure (VPC peering, firewall rules, security groups).
3. The Rails node is the authoritative source for generating Helm values
   and configuration details.
4. The three stateful Omnibus services — PostgreSQL, Redis, and Gitaly —
   follow the same exposure pattern: the customer configures network
   access, and Omnibus provides connection details.

## Decision

OAK supports multi-node Omnibus deployments. Advanced components require
access to PostgreSQL, Redis, and Gitaly. Omnibus provides planned OAK
configuration options and Helm values generation. Network configuration
and service exposure are the customer's responsibility.

### Data storage considerations

Advanced components may require access to three stateful GitLab services:
PostgreSQL, Redis, and Gitaly.

**PostgreSQL**

There are three cases depending on how PostgreSQL is deployed.

For single-node Omnibus PostgreSQL, advanced components connect through
firewall rules, CIDR allowlisting, and `postgresql['md5_auth_cidr_addresses']`.

For external PostgreSQL (PaaS or self-managed), standard network
configuration is sufficient.

For Omnibus PostgreSQL clusters using Patroni, advanced components can
provision their own databases within the Omnibus cluster alongside the
main GitLab application database, and failovers propagate to those
databases automatically, as long as the component database usage is designed
to support a PostgreSQL WAL-based replication. The registry metadata database is
an example of a database that does not support PostgreSQL WAL-based replication
because it does its own database replication via application logic. So
components desiring to take advantage of the Omnibus support for multiple
databases in HA mode, must be PostgreSQL Wall replication compliant.
The same network access pattern as single-node Omnibus
PostgreSQL applies — firewall rules, CIDR allowlisting, and
`postgresql['md5_auth_cidr_addresses']`.

**Gitaly**

Advanced components reach Omnibus Gitaly through firewall rules and CIDR
allowlisting. No additional Omnibus configuration is needed once network
access is in place.

**Redis**

Both Omnibus Redis and external Redis (PaaS or self-managed) are
accessible through standard network configuration.

## Rationale

The PoC confirmed that existing Omnibus configuration mechanisms are
sufficient for multi-node deployments. Network configuration is
environment-specific and outside Omnibus's scope — customers configure
firewall rules to allow Kubernetes pod network access to Omnibus services,
set those services to listen on the right network interfaces, and manage
whatever infrastructure-level networking their environment requires (VPC
peering, security groups, and so on).

Omnibus contributes three things to this setup:

- **PostgreSQL exposure.** Customers who already configure
  `postgresql['md5_auth_cidr_addresses']` for their Rails nodes can use
  planned OAK Beta automation or continue setting it directly.
- **Redis and Gitaly exposure.** Neither service has CIDR allowlisting
  settings in Omnibus. Once firewall rules are in place and pods have
  credentials (Redis password, Gitaly token), no further Omnibus
  configuration is needed.
- **Helm values generation.** The Rails node has full knowledge of
  all data service addresses and can generate Helm values files from existing
  configuration, regardless of whether services are co-located or spread
  across nodes.

Omnibus should not orchestrate configuration across multiple nodes,
manage resources outside itself, or assume knowledge of Kubernetes
cluster topology. This keeps the operational boundary clear: Omnibus
manages itself; customers manage network and orchestration.

## Deployment workflow

### For customers: multi-node Omnibus + OAK

**Step 1: Configure network access**

Identify the Kubernetes pod network CIDR, then configure firewall rules
to allow pods to reach PostgreSQL, Redis, and Gitaly. Configure Omnibus
services to listen on the appropriate interfaces, either through OAK
automation or directly:

- PostgreSQL: add the pod CIDR to `postgresql['md5_auth_cidr_addresses']`
- Redis and Gitaly: configure to listen on the pod network interface if
  required by advanced components

**Step 2: Generate Helm values**

Generates Helm values files containing PostgreSQL connection
details, Redis and Gitaly connection details (where applicable), and
GitLab integration endpoints.

**Step 3: Deploy Kubernetes components**

Deploy advanced component to the cluster using connection details from previous
step.

### For feature teams: documenting service requirements

When introducing a new advanced component that requires access to
Omnibus services, document which services are required, which Omnibus
nodes need configuration, network requirements (ports, protocols,
authentication), and any multi-node considerations (for example,
Sidekiq nodes that need configuration for async workers).

Track these requirements as part of
[PREP (Production Reference Environment and Patterns)](../../../../infrastructure-platforms/production/prep.md).

**Example:** OpenBao requires PostgreSQL access. Both Rails and Sidekiq
nodes need `gitlab_rails['openbao']` configuration because Sidekiq runs
async workers for secrets provisioning.

## Geo deployments

In Geo setups, Helm values must be generated from the primary site's
Rails node. Secondary sites run read-only databases, so any advanced
component configured against a secondary will be unable to write to
PostgreSQL.

## References

- [OAK design document](../_index.md)
- [Multi-node Omnibus PoC — work item #9691](https://gitlab.com/gitlab-org/omnibus-gitlab/-/work_items/9691)
- PoC: [demo (internal link)](https://drive.google.com/file/d/1ZriEHz1Sjg-9rJLSi0EpUurmaHVscPTP/view) and [implementation details](https://gitlab.com/-/snippets/5974860)
