---
title: "Artifact Registry and Infrastructure interface agreement"
owning-stage: "~devops::package"
description: "Interface agreement between the Artifact Registry and Infrastructure teams"
toc_hide: true
---

<!-- vale gitlab.FutureTense = NO -->

## Summary

The Artifact Registry (AR) is the first stateful [modular service](https://docs.google.com/document/d/1ipEhmAO67nKJXPm7vrWIfRyRRBCTVtoavvwhnmmJruQ/edit). This document defines AR's infrastructure requirements as an interface agreement, so both teams can align on what is needed and then work independently.

The goal is not to prescribe how the infrastructure is provisioned, but to clearly state what AR requires, what we recommend, and where the risks are. The infrastructure team decides the "how"; this document defines the "what".

## Version history

| Version | Date | Author | Approved by | Summary |
| --- | --- | --- | --- | --- |
| 0.1 | 2026-04-13 | @jdrpereira | @jdrpereira @glopezfernandez | Initial version, migrated from [Google Doc](https://docs.google.com/document/d/1GApsHWd3XaQ0Z40Dk7J_pM9sWqDDJlbD9tQuBiebHLI/edit) |

## Timeline

AR is targeting .com go-live before the end of Q2 FY27 (July 31, 2026). Infrastructure meeting the MUST requirements in this document for .com needs to be ready across environments by **June 15, 2026**, to allow ~6 weeks for integration testing, staging validation, and progressive rollout. It does not need to be final or polished; it needs to meet the MUST requirements, in whatever form or format.

## Requirement levels

This document uses [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) keywords: **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate requirement levels.

## Infrastructure requirements

### Cardinality

One AR application connects to exactly one of each:

| Component | Compatibility | Cardinality |
| --- | --- | --- |
| Relational database | PostgreSQL-compatible | 1:1 |
| Object storage | GCS or S3-compatible | 1:1 |
| Key-value store | Redis-compatible | 1:1 |

AR MUST NOT be required to shard across multiple databases, buckets, or key-value instances at the application level. If the infrastructure layer provides multiple physical backends behind a single logical endpoint (e.g., proxy, connection pooler), that is transparent to AR and MAY be done without coordination.

### Isolation levels

| Component | MUST | SHOULD |
| --- | --- | --- |
| Object storage | Separate bucket. MUST NOT share a bucket with other modules. | N/A |
| Relational database | Separate logical database with its own schema, migrations, and credentials. Other modules MUST NOT have cross-database access. | Separate physical instance. |
| Key-value store | Separate logical keyspace (own database index or ACL). Other modules MUST NOT access AR's keys. | Separate physical instance. |

Not in scope for the MVP, but AR will need access to read-only replicas for database load balancing (to improve availability, fault tolerance and performance). This SHOULD be considered when provisioning the database to avoid a later migration.

### Why bucket MUST NOT be shared

| Reason | Detail |
| --- | --- |
| Lifecycle policies | AR manages application-level retention (expiration, cleanup). The infrastructure team MUST be able to set platform-level bucket policies (e.g., cold tiering, storage class transitions) specific to AR without affecting other modules. Bucket-level policies cannot be scoped to a prefix. |
| CDN configuration | CDN-signed URLs require per-bucket origin, cache behavior, and signing keys. |
| IAM isolation | Access policies are bucket-level (GCS lacks prefix-level IAM). |

### Why separate physical database and KV store SHOULD be provisioned

The risks below apply to both the relational database and the key-value store when sharing physical backends with other modules:

| Risk | Detail |
| --- | --- |
| Resource contention | AR's background operations (GC, lifecycle enforcement, storage accounting self-healing) involve long-running transactions and table scans that compete for I/O, CPU, and memory. |
| Noisy neighbor | A long-running AR migration or GC sweep can degrade co-located modules, and vice versa. |
| Scaling independence | AR's data grows with artifact metadata volume, which scales differently from other modules. Shared backends make independent scaling harder. |
| Migration risk | Starting shared and extracting later requires data migration under load, which is significantly more expensive and risky than provisioning separately from the start. |
| Memory pressure (KV) | AR's cache scales with active namespaces and concurrent sessions. Shared instances lead to unpredictable evictions across modules. |

Regardless of the decision, AR MUST NOT be required to provide any replication, extraction, or migration logic to move its data from a shared server to a dedicated one. That is an infrastructure concern, not an application concern. The module connects to an endpoint; how data is moved behind that endpoint is transparent to AR.

### Compute

AR is a single Go binary (API server + background workers), scales horizontally.

| Requirement | Level | Detail |
| --- | --- | --- |
| Separate deployment | MUST | Own pods, own replica count. MUST NOT share pods with other modules. |
| Resource quotas | MUST | AR MUST NOT be starved by, or starve, co-located modules. |
| Network policies | MUST | Inbound HTTPS from monolith(s), topology service, load balancer. Outbound to database, object storage, KV store, CDN, remote registries. |

### CDN

CDN MAY not be available on all installation types, but is expected for .com. AR uses CDN-signed URLs pointing to the AR bucket as origin. If CDN is provided, the following requirements apply:

| Requirement | Level | Detail |
| --- | --- | --- |
| Per-module origin | MUST | Origin MUST be AR's dedicated bucket, not a shared origin. |
| Signing keys | MUST | AR needs the private key to generate signed URLs. |
| Cache invalidation | MAY | Blobs are content-addressable and immutable. TTL-based expiration is expected to be sufficient. |

**Recommendation for .com:** The engineering team strongly recommends the GCS + Cloud CDN combination for .com. This is the proven stack that has been running the GitLab container registry at scale for years with high success. GCS offers strong consistency guarantees and performance characteristics (e.g., strong read-after-write consistency, single-object compose operations), some of which are not available in S3.

### DNS and TLS

AR serves on a dedicated domain (e.g., `artifact-registry.gitlab.com`, TBD), separate from the main GitLab application. Infrastructure MUST provision DNS records, TLS certificates, and certificate rotation for this domain.

### Configuration and secrets

AR reads all settings (endpoints, credentials, feature flags) from a configuration file. Secret management MUST be transparent to AR: the infrastructure layer populates the configuration file with the correct values, including secrets. AR MUST NOT be required to integrate with a specific secrets backend (e.g., Vault, KMS). How secrets are injected into the configuration is an infrastructure concern.

### Database connection pooling

A connection pooler (e.g., PgBouncer) MAY be placed in front of the database. AR is designed to be compatible with transaction-mode poolers, following the same pattern as the GitLab container registry (which runs behind PgBouncer on .com). AR uses transaction-level advisory locks (`pg_advisory_xact_lock`) and disables prepared statements by default in favor of simple query protocol.

### Backup and disaster recovery

Database backups, object storage durability (e.g., versioning, cross-region replication), and KV store persistence are infrastructure concerns. AR MUST NOT be required to implement its own backup or recovery mechanisms nor infrastructure-level data protection. See [Observability](#observability) and [Replication and zone availability](#replication-and-zone-availability) sections for related details.

### Observability

AR emits metrics, logs, and traces via LabKit. AR MUST have per-module dashboards, alerting, and SLIs/SLOs tracked independently from co-located modules.

The infrastructure team owns the health, availability, and recoverability of all components. AR team owns application-level incidents and defines module SLIs/SLOs.

## Capacity planning

Current .com baseline metrics and workload projections are documented in the [infrastructure contract](https://docs.google.com/document/d/1GApsHWd3XaQ0Z40Dk7J_pM9sWqDDJlbD9tQuBiebHLI/edit?tab=t.0#bookmark=id.mhzpab1ab65l). Source data from the [internal capacity planning note](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/17524#note_3024864366).

**AR starts from zero: no data and no users.** Compute scales horizontally by adding replicas. Specific VM/node sizing, replica counts, and leader configuration are to be determined by the owning team. Post-MVP, AR will need database read replicas for load balancing (see [Isolation levels](#isolation-levels)).

## Routing and topology

AR MUST NOT be required to be aware of any network topology. Request routing MUST be dynamic, external, and transparent to the application. AR receives requests on its endpoint; how requests get there is an infrastructure concern.

| Function | Detail | Alignment needed |
| --- | --- | --- |
| Request routing | Topology service (or equivalent) routes inbound requests to the correct AR deployment based on the slug in the URL path. | Routing configuration and integration |
| Slug claiming | The one exception: AR claims globally unique slugs via ClaimService gRPC API. This is the only point where AR interacts with the routing layer. Flow still being discussed in [#594637](https://gitlab.com/gitlab-org/gitlab/-/work_items/594637). | Proto changes and integration timeline |

## Continuous delivery and release

AR MUST have an automated, consistent release and deployment process across all installation types (.com, Dedicated, Self-Managed). Runway was previously identified as a candidate, and a preliminary investigation indicates feasibility ([source](https://gitlab.com/gitlab-com/gl-infra/platform/runway/team/-/work_items/823)), but the specific tooling is not a concern for AR as long as the process meets these requirements:

| Requirement | Level | Detail |
| --- | --- | --- |
| Automated deployment | MUST | No manual steps for deploying to .com. |
| Progressive rollout | MUST | Ring-based or equivalent. Modules roll through stages independently. |
| Consistent across install types | MUST | Same binary, same release artifacts, deployed to .com, Dedicated, and Self-Managed. |
| Independent release cycle | MUST | AR MUST be deployable independently of the monolith release cycle. |

## Replication and zone availability

AR MUST NOT have any awareness of its physical location, zone topology, or replication mechanisms. AR connects to a single database and KV store endpoint and a single bucket. How data is replicated, distributed, or failed over behind those endpoints is transparent to AR.

Per-component details:

**Object storage:** AR writes content-addressable blobs (immutable, identified by digest) to a single bucket. Writes are idempotent. If cross-region replication ("free" with multi-region GCS buckets) or versioning is configured on the bucket, it is transparent to AR. AR MUST NOT be required to switch between buckets or initiate replication. Bidirectional replication at the bucket level is compatible (no conflict resolution needed for immutable blobs) but doing so is a platform concern.

**Database:** AR connects to one primary for writes. Post-MVP, AR will route reads to replicas internally. Provisioning and replicating those replicas is an infrastructure concern. AR needs the replica endpoints in its configuration.

**KV store:** AR connects to one endpoint. Persistence and replication are infrastructure concerns.

Geo-style replication has been [de-scoped from the initial release](https://gitlab.com/gitlab-org/gitlab/-/work_items/590300#note_3208287650). Geo has no multi-tenant model. The right replication model for modular features will be designed later based on production learnings.

## Related

- [AR architecture design document](/handbook/engineering/architecture/design-documents/artifact_registry/)
- [AR database schema (ADR-007)](/handbook/engineering/architecture/design-documents/artifact_registry/decisions/007_database_schema/)
- [IMR Blueprint](https://docs.google.com/document/d/1Wsgzx6Mk7aJgWN6fQYpprAAwgtMsns5pPXR-b8oeRGY/edit)
- [CTO Module Review](https://docs.google.com/document/d/1xZ4B1iW4srffOViwHYFqVumnlUuBcp7ivN_Jk_UKj9c/edit)
- [Database provisioning issue](https://gitlab.com/gitlab-com/gl-infra/data-access/dbo/dbo-issue-tracker/-/work_items/691)
- [Provision required infrastructure components (epic)](https://gitlab.com/groups/gitlab-com/gl-infra/-/work_items/1999)
