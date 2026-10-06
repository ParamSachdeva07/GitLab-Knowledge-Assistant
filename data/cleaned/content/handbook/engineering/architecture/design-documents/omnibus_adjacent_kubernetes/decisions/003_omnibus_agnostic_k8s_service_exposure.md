---
title: "GitLab Omnibus-Adjacent Kubernetes ADR 003: Omnibus is agnostic to Kubernetes service exposure"
owning-stage: "~devops::gitlab delivery"
toc_hide: true
---

## Context

Omnibus NGINX acts as the entry point for all external traffic to advanced components running in the adjacent
Kubernetes cluster. To generate reverse proxy configuration, Omnibus needs to know where to forward that traffic.

During the Beta PoC, we validated that Omnibus NGINX can proxy to a Kubernetes service regardless of how that
service is exposed. We tested both a LoadBalancer pattern (proxying to an in-cluster load balancer's IP) and a
NodePort pattern, and both work without any change to Omnibus automation. In all cases, Omnibus only needed an
address to proxy to.

This confirmed a broader principle: the mechanism by which Kubernetes services are made reachable from Omnibus
is a user-controlled concern. Different users will arrive at different valid solutions:

- **Same-VM ClusterIP**: When the Kubernetes cluster runs on the same VM as Omnibus, the host can often reach
  ClusterIP services directly, without a NodePort or LoadBalancer.
- **NodePort**: The user exposes services via NodePort bound to `127.0.0.1` (same VM) or a specific interface
  (separate VM).
- **LoadBalancer**: The user provisions a load balancer — either through the Kubernetes distribution's built-in
  controller or an external one — and Omnibus proxies to that IP.

There is no single correct exposure mechanism. Each has valid trade-offs depending on the user's infrastructure,
chosen Kubernetes distribution, and intended migration path.

Furthermore, users may choose to expose all advanced components through a single shared ingress address, or
expose each component on its own individual address (e.g. separate NodePorts per service). The configuration
model must accommodate both.

## Decision

Omnibus must be agnostic to how Kubernetes services are exposed. The OAK cookbook accepts a user-provided
address — an IP, hostname, or `IP:port` — and uses it when generating NGINX reverse proxy configuration.
Omnibus does not impose any constraint on what that address represents internally in the Kubernetes cluster.

### Configuration model

Configuration lives in the `oak` cookbook namespace. A global address serves as the default for all
components. Per-component overrides allow users to specify individual addresses when components are exposed
separately (for example, each on its own NodePort):

```ruby
# Global address — used for all components unless overridden.
# May be a shared ingress/LB IP, a ClusterIP (same-VM), or any reachable address.
oak['address'] = "10.43.25.7"

# Per-component override — used when a component is exposed on its own address.
oak['components']['openbao']['address'] = "127.0.0.1:32080"
```

Resolution order for each component:

1. `oak['components']['<component>']['address']` — if set, this takes precedence.
2. `oak['address']` — used as the fallback for all components without an explicit address.

Omnibus requires that at least one of the two is resolvable for each component it needs to configure. If
neither is set for a given component, `gitlab-ctl reconfigure` should fail with a clear error message.

## Consequences

- **User flexibility**: Users can share a single ingress address across all components or use individual
  addresses per component. Both patterns are supported without any structural change to Omnibus automation.
- **Clear responsibility boundary**: How Kubernetes services are exposed is entirely the user's responsibility.
  Documentation should describe common patterns (ClusterIP, NodePort, LoadBalancer) and their trade-offs
  without mandating any one approach.
- **Simplified Omnibus logic**: Omnibus does not need to query or introspect the Kubernetes API to discover
  service addresses. Configuration is explicit and deterministic.
- **Migration path**: Users on a same-VM setup (ClusterIP) can move to a separate-VM setup (LoadBalancer or
  NodePort) by updating the address in `gitlab.rb` and running `gitlab-ctl reconfigure`. No structural change
  to Omnibus automation is required.
- **Consistency with ADR-001**: Keeping address configuration explicit reinforces that GitLab is not
  responsible for the Kubernetes platform or its internal networking topology.
