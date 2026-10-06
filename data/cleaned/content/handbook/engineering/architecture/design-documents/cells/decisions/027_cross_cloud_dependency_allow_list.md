---
title: "Cross-Cloud Dependency Allow-List"
owning-stage: "~devops::tenant-scale"
group: cells-infrastructure
creation-date: "2026-06-30"
authors: ["@kerusu"]
coach:
approvers: []
toc_hide: true
---

{{< engineering/design-document-header >}}

## Summary

This ADR extends [ADR-016: Cross Cloud Dependencies](016_cross_cloud_dependecies.md). ADR-016 establishes that a Cell must not depend on another cloud provider. This ADR keeps that as the default and defines the narrow, governed exception: a short, explicitly-named allow-list of cross-cloud dependencies that are tolerated for a defined transitionary period, each with a named owner and a sunset condition. The operating principle is **contained by default, cross-cloud by exception**.

## Context

ADR-016 set single-cloud self-containment as the rule for Cells, for cost, resiliency, and clean separation. In practice, a small number of components are centrally GitLab-operated services that do not yet have a per-cloud equivalent, and Cells on the "other" cloud must reach across to consume them during the transition to a fully cellular, multi-cloud architecture.

The concrete, already-live example is the AI Gateway: Cells deployed to Dedicated on AWS today reach the GCP-hosted AI Gateway to serve Duo/AI features. This is a working, accepted dependency, not a defect. Treating ADR-016 as absolute would mis-describe the system we actually operate, and would give teams no sanctioned path for the genuinely-shared central services that have not yet been regionalised.

The risk to manage is not the existence of cross-cloud dependencies, but their uncontrolled growth. Without an explicit list and entry criteria, ad-hoc cross-cloud calls accumulate and the ADR-016 end state (two independent single-cloud stacks) becomes unreachable.

## Decision

A component on one cloud provider may depend on a component on the other cloud provider **only if that dependency is on the allow-list below**. Everything not on the list remains subject to ADR-016 and must be self-contained within a single cloud.

The allow-list is expected to **shrink over time, not grow**. Adding an entry is an architectural decision recorded by amending this ADR (a new revision or superseding ADR), not an implementation choice made ad hoc.

### Criteria for an allowed cross-cloud exception

An entry may be added to the allow-list only if all of the following hold:

1. **No per-cloud equivalent yet.** The component is centrally GitLab-operated and a per-cloud deployment is non-trivial or not yet funded.
2. **Named owner and sunset condition.** The dependency has a DRI and a documented condition that retires it (what makes it go away, and roughly when).
3. **Bounded, understood traffic.** Cross-cloud egress is modelled for cost and latency, not incidental.
4. **Graceful degradation where possible.** Failure of the link degrades the dependent feature gracefully rather than taking down the Cell, consistent with the resiliency rationale of ADR-016.

### The allow-list (transitionary)

| Dependency | Why it crosses clouds | Owner | Sunset condition |
|---|---|---|---|
| Any Cell &rarr; GCP AI Gateway | Centrally-hosted Duo/AI model brokering; no per-cloud equivalent. Already live for Dedicated-on-AWS. | AI / Cloud Connector | Regional / per-cloud AI Gateway hosting, or per-tenant self-hosted-model option |
| AWS Cell &rarr; GCP Topology Service | Org classify/claim, Cell discovery/health, SSH routing &mdash; single central instance today (see ADR-019) | Cells Infrastructure | Per-cloud replication of the Topology Service (decision pending) |
| GCP &rarr; AWS via Siphon+NATS (HA-VPN / Transit Gateway) | Org data migration from Legacy Cell to AWS Protocells | ODM / Cells migration tooling | Removed automatically once a cohort completes migration |
| AWS Cell &rarr; Artifact Registry | Only deployed in GCP | Artifact Registry | [Cellular Target](../../artifact_registry/decisions/024_infrastructure_delivery.md#phase-2--cellular-target) |
| AWS Cell &rarr; Secrets Manager | Only deployed in GCP | Secrets Manager | [Cellular Target](https://gitlab.com/groups/gitlab-org/-/work_items/17846) |
| AWS S3 &rarr; GCP Elastic Agent (OIDC workload identity) | Cells log ingestion to centrally-operated Elasticsearch | Security Logging | Per-cloud log sink, if/when justified |
| AWS Cell &rarr; GCP GitLab Observability Backend (GOB) | Single centrally-hosted backend behind a hardcoded `observe.gitlab.com` URL (`lib/gitlab/observability.rb`); telemetry is stored externally keyed by project/group, with OAuth scoped per root ancestor group, so it behaves like an external SaaS with no Cell or Org awareness | Observability | Per-cell Observability Backend, tracked in [gitlab#606874](https://gitlab.com/gitlab-org/gitlab/-/work_items/606874) |

Any dependency not in this table must be contained within a single cloud.

### Relationship to native cross-cloud replication

A component that keeps a single logical service across clouds via **native data replication** (for example, the GATE/Auth stack using YugabyteDB cross-cloud replication to maintain one GitLab.com realm) is **not** an allow-list entry. It makes no runtime cross-cloud call: each Cell talks only to its in-cloud replica. This is the preferred pattern for the genuinely-shared stateful case and remains compliant with ADR-016. The allow-list is reserved for **runtime cross-cloud dependencies** only.

## Consequences

### Positive

- **Honest model.** The documented architecture matches the system actually in production (AI Gateway from AWS Cells), rather than an idealised version of it.
- **Controlled surface.** Cross-cloud dependency becomes an enumerated, owned, time-bounded set instead of an emergent property nobody owns.
- **Clear path to the ADR-016 end state.** Each entry has a sunset condition, so progress toward two independent single-cloud stacks is measurable.

### Negative

- **Ongoing governance cost.** The list must be reviewed and entries actively driven to sunset, or it ossifies.
- **Residual cross-cloud cost and compliance exposure.** While entries remain (AI Gateway in particular), cross-cloud egress cost and data-egress compliance scrutiny persist.

### Mitigations

- Review the allow-list at each Cells architecture / CTO review; report movement of entries toward sunset.
- Require that every new entry arrive with its sunset condition already defined, not deferred.
- Prefer the native-replication pattern (GATE/Auth) over a new runtime cross-cloud dependency wherever the shared component is stateful.

## Alternatives

- **Keep ADR-016 absolute (no exceptions).** Rejected: it contradicts the live AI Gateway dependency and leaves shared central services with no sanctioned transitional path.
- **Allow cross-cloud dependencies case-by-case without a list.** Rejected: this is the status quo failure mode &mdash; dependencies accumulate with no owner, no sunset, and no aggregate view, making the single-cloud end state unreachable.
