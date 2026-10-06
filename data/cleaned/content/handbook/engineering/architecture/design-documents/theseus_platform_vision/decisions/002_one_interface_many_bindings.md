---
title: "Theseus ADR 002: One declarative interface, many Platform Bindings"
owning-stage: ""
description: "Decision to have components declare a single Fairway manifest and to translate it per target via a Platform Binding, rather than collapse all targets onto one deployment path or let each target reinvent its own contract."
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Status

**Proposed.**

## Context

GitLab ships to a set of targets with little in common operationally:
the developer workstation (Caproni),
GitLab.com,
Cells,
Dedicated,
Dedicated for Government,
the Enterprise binding (GitLab-Inc-operated services like `customers.gitlab.com`),
Self-Managed Advanced,
and Self-Managed Foundation (Omnibus, legacy).

Each target has its own orchestrator, storage layer, secrets backend, monitoring system, and release cadence.
The two end-points of the design space are clear and both are wrong:

- **Collapse the targets onto one deployment path.**
  Pick Kubernetes + Helm + ArgoCD and require every target to look like that.
  Impossible in practice — customer environments are non-uniform,
  Omnibus on a VM is non-negotiable for Self-Managed Foundation,
  and Dedicated's compliance posture differs from GitLab.com's.
- **Let each target reinvent its own contract.**
  The status quo.
  Component teams write target-specific deployment code, tooling fragments,
  and the developer journey is different for every destination.

The platform needs to sit between these.

## Decision

A component declares a single [`FairwayManifest`](../#42-the-single-declarative-interface) describing its abstract dependencies
(a Postgres database, a key-value store, object storage, and so on).
The manifest is the contract.

Each target has a **Platform Binding**
that resolves the manifest into target-native infrastructure:

- Enterprise binding → CloudSQL, GCS, Memorystore on Google Cloud.
- Cells / Dedicated binding → RDS, S3, ElastiCache on AWS, via Instrumentor.
- Caproni binding → in-cluster operators via [`gitlab-dev-stack`](https://gitlab.com/gitlab-org/cloud-native/charts/gitlab-dev-stack).
- Self-Managed binding → Helm values; the customer provides the infrastructure.

The same component runs on every binding that exists for it,
without source changes,
and a new target lands as a new binding rather than a new component.

## Consequences

### Positive

1. **Write once, deploy everywhere.**
   Component teams target the manifest, not the binding.
1. **Targets evolve independently.**
   A binding can change its dependency story
   without re-releasing every component.
1. **New targets are additive.**
   A new deployment model is a new binding implementation,
   not a fork of every chart in the catalogue.

### Negative

1. **Every binding is a sustained engineering commitment.**
   Bindings need owners, SLAs, and parity with the manifest contract.
1. **Target-native features don't appear automatically.**
   A new managed service on one cloud is invisible to components
   until the relevant binding exposes it through the manifest.
1. **Abstractions leak.**
   When a component needs something the manifest doesn't model,
   it must extend the schema rather than drop to target-specific code.
   The `infrastructure:` escape hatch exists for this
   ([Section 7.3](../#73-open-tensions)) but using it carries a cost.

## Alternatives Considered

### Alternative: One deployment path for every target

#### Approach

Mandate Kubernetes + Helm + ArgoCD (or similar) everywhere
and migrate any target that doesn't fit.

#### Why Not Chosen

Self-Managed Foundation is Omnibus on a VM
and will remain so as a deliberate product choice.
Dedicated for Government has FedRAMP requirements
that limit operational flexibility on the SAAS side.
Customer environments are not negotiable.
A single deployment path is not reachable from where we are.

### Alternative: Per-target bespoke implementations per service

#### Approach

Continue the status quo:
each component writes its own deployment plumbing for each target it cares about.

#### Why Not Chosen

The cost is paid per component per target,
and the result is fragmentation:
inconsistent tooling,
no shared developer journey,
no economies of scale on observability or release tooling.
The whole point of the platform is to amortise that work.

## References

- [Section 4 — One platform, many bindings](../#4--one-platform-many-bindings) —
  the position this ADR formalises.
- [Section 4.1 — The target matrix](../#41-the-target-matrix) —
  the canonical list of bindings and their roles.
- [Section 4.2 — The single declarative interface](../#42-the-single-declarative-interface) —
  the manifest at the centre of the contract.
- [Section 7.3 — Open tensions: the Runway "leaky abstraction" debate](../#73-open-tensions) —
  the known failure mode of this approach and how the `infrastructure:` escape hatch responds to it.
