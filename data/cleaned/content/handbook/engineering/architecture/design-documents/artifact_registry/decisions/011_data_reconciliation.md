---
title: "Artifact Registry ADR 011: Data Reconciliation Feature Timing"
owning-stage: "~devops::package"
description: "Decision on data reconciliation feature timing and requirements"
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Context

Content-addressable storage ([ADR-008](008_content_addressable_storage.md)) creates a two-source-of-truth system: database metadata (references, upload sessions) and object storage (blobs, uploads). This is an inherent consequence of CAS (ADR-008 Negative Consequence #6). Several categories of operations can cause these two sources to diverge:

- **Crash between storage write and DB commit**: The blob exists in object storage but has no database record. This produces an orphaned storage object.
- **Failed delete-after-copy during move**: An upload completes the copy to the final blob path but fails to delete the temporary upload object. This produces an orphaned upload object.
- **External storage modification**: An operator or external process modifies or deletes an object in storage without going through the registry API. This produces a content mismatch or missing object.
- **Reference tracking bugs**: A bug in dereference logic can leave stale references (leaked storage, never GC'd) or remove references prematurely (data loss on next GC cycle).

Virtual registry caches follow the same divergence pattern: cache metadata in the database can diverge from cached blobs in storage. The same reconciliation features (GC, upload purging, data validation) address virtual cache divergence because CAS stores all blobs uniformly regardless of origin.

### Scope boundary with ADR-010

[ADR-010](010_data_retention.md) (Data Retention) defines *what* GC does: remove orphaned blobs, hard-delete soft-deleted artifacts. This ADR decides *when* each reconciliation feature ships and *what architectural constraints* it imposes on the database schema (ADR-007<!-- (007_database_schema.md) -->) and storage layout ([ADR-008](008_content_addressable_storage.md)). Soft-delete expiry is a retention mechanism (ADR-010's scope), not a reconciliation mechanism, because both sources agree on the data's state. Only the policy says it should be removed.

### Reconciliation features

Three reconciliation features address DB/storage divergence:

| Feature | Purpose | Timing |
|---|---|---|
| Garbage collection | Delete zero-reference blobs from storage | First release |
| Upload purging | Clean up abandoned upload sessions (storage + DB) | Deferred |
| Data validation | Detect and report DB/storage divergence | Deferred |

## Decision

**We ship garbage collection in the first release. We defer upload purging and data validation but capture their requirements now to prevent schema or storage layout regressions.**

### GC: First-Release Requirement

#### Why not defer GC

**Container registry lesson.** The container registry retrofitted online GC after years of operation. The complexity of adding GC to a system with billions of existing objects, established access patterns, and no pre-existing tracking infrastructure was the primary engineering challenge. Building GC into a fresh service avoids this entirely.

**Scale-from-zero advantage.** A new service starts with zero data. At low data volume, GC bugs affect fewer objects: less data at risk of premature deletion, lower storage I/O and database connection pressure from GC competing with API traffic, and a dataset small enough to inspect manually during diagnosis. The concurrency problems (race conditions between GC and API) exist at any scale, but the cost of getting them wrong is lowest when the service is new. This is a one-time window.

**Storage cost.** Without GC, orphaned blobs accumulate indefinitely. The container registry grew to billions of objects and tens of petabytes on GitLab.com ([ADR-003](003_system_requirements.md), [ADR-002](002_storage_deduplication_scope.md)). We do not yet have an orphan accumulation rate for the Artifact Registry. Without a self-correction mechanism, orphaned storage grows monotonically.

**Reference tracking correctness.** GC is the only consumer that exercises the full reference tracking lifecycle (create reference, dereference, verify zero references, delete). Shipping GC early validates that the reference tracking schema (ADR-007<!-- (007_database_schema.md) -->) is correct before the data volume makes bugs expensive.

#### Why database-tracked from day one

GC candidates must come from database queries, not from enumerating objects in storage. The container registry encountered memory scaling problems from storage enumeration (issue [#216](https://gitlab.com/gitlab-org/container-registry/-/issues/216)) and redundant sweep problems from per-instance execution (issue [#217](https://gitlab.com/gitlab-org/container-registry/-/issues/217)), and rebuilt its database schema from the ground up to support online garbage collection ([online GC spec](https://gitlab.com/gitlab-org/container-registry/-/blob/master/docs/spec/gitlab/online-garbage-collection.md)). ADR-007<!-- (007_database_schema.md) --> must account for GC from the initial design: reference tracking and candidate selection should be native to the schema, not retrofitted. GC operates per namespace ([ADR-022](022_namespace_decoupling.md)), the isolation and partitioning boundary for all data operations.

#### Backpropagation to ADR-008 (CAS)

No changes required to [ADR-008](008_content_addressable_storage.md).

### Upload Purging: Deferred

#### Why deferrable

Upload paths are temporary (minutes to hours) and isolated under `uploads/{upload_id}`. They do not affect read paths or blob integrity. [ADR-008](008_content_addressable_storage.md) already specifies best-effort inline cleanup: the upload handler deletes the temporary object after a successful move, and non-resumable uploads delete on failure. This handles the common case. The purger catches the remainder (crashed processes, abandoned resumable uploads).

Without the purger, abandoned uploads accumulate in object storage. Expired session records also accumulate in the database. This is a storage and database hygiene issue, not a correctness issue. No data loss or broken pulls result from orphaned uploads. At extreme scale, unbounded session records could affect query performance for active uploads. At launch scale, both storage cost and session record volume are bounded and manageable.

When the purger does ship, it can reconstruct the full cleanup state from existing data. Expired upload session records in the database identify which uploads were abandoned. The `uploads/{upload_id}` path structure in object storage makes orphaned uploads enumerable by prefix. No additional tracking infrastructure is needed beyond what ADR-007<!-- (007_database_schema.md) --> and [ADR-008](008_content_addressable_storage.md) already provide.

#### Requirements captured now

Upload session tracking must support expiry-based cleanup from the initial schema design (ADR-007<!-- (007_database_schema.md) -->). The purger must identify candidates from database records, not by listing objects in storage (same principle as GC). [ADR-008](008_content_addressable_storage.md)'s reversible path structure already supports this.

### Data Validation Service: Deferred

#### Why deferrable

The validation service detects divergence that has already occurred. It does not prevent divergence. GC and upload purging handle the known divergence causes (orphaned blobs, orphaned uploads). The validation service catches everything else: storage corruption, external modification, and bugs in GC or purging.

The container registry's proposal ([#690](https://gitlab.com/gitlab-org/container-registry/-/issues/690)) focused on visibility (logging, metrics, Sentry) for the first iteration, not automated repair. The Artifact Registry can follow the same phased approach. Building the validation service requires a mature understanding of what "correct" looks like in production. Running GC first provides that baseline.

When the validation service does ship, it can derive correct state from the existing database and storage layout. [ADR-008](008_content_addressable_storage.md)'s reversible path structure lets the validator map between storage objects and database records in both directions. Any divergence that accumulated during the deferral period is detectable and recoverable from these two sources without a separate tracking system.

#### Requirements captured now

The validation service compares database records against storage objects to find divergence. Two properties of the current design make this safe to defer without foreclosing the option:

1. [ADR-008](008_content_addressable_storage.md)'s reversible path structure allows the validator to derive the expected database record from a storage path (and vice versa) without maintaining a separate mapping. SHA256 content addressing means the validator can verify integrity by re-hashing, without storing a secondary checksum.
2. ADR-007<!-- (007_database_schema.md) --> must support efficient per-namespace blob queries. GC already requires namespace-scoped candidate selection, so this constraint is not unique to the validation service.

Neither property requires design changes to support validation later. If either property were absent, the validation service would need its own tracking infrastructure, and we would need to ship it earlier.

## Alternatives Considered

### Ship all three features in the first release

Bundling GC, upload purging, and the validation service into the first release would eliminate the deferred-feature gap (orphaned uploads accumulating, undetected divergence). However, upload purging and validation do not carry the same deferral risk as GC. GC has a one-time scale-from-zero window and validates the reference tracking schema. Upload purging addresses a bounded hygiene issue. The validation service requires a production baseline that only GC can provide. Shipping all three increases first-release scope without proportional risk reduction.

### Defer all three features

Deferring GC trades a one-time advantage (building GC into a fresh service with zero data) for permanent retrofit cost. The container registry spent years retrofitting online GC into a system with billions of objects and no pre-existing tracking infrastructure. Without GC from day one, the database schema (ADR-007<!-- (007_database_schema.md) -->) ships without validation that reference tracking works under real traffic, and orphaned blobs accumulate with no self-correction mechanism.

## Consequences

### Positive

1. GC validates reference tracking correctness under real traffic before data volume grows.
2. Shipping GC into a new service with low data volume reduces the cost of finding and fixing concurrency bugs.
3. Deferred features have captured requirements that prevent schema or storage layout regressions.
4. Upload purging and validation build on the same design foundations as GC (database-driven candidate selection, namespace-scoped execution).

### Negative

1. First-release scope increases: GC requires database schema support and a background worker.
2. Until upload purging ships, abandoned uploads accumulate in object storage (bounded cost, no correctness impact).
3. Until the validation service ships, DB/storage divergence from causes other than orphaned blobs/uploads goes undetected.
4. Until the validation service ships, a GC bug that prematurely deletes a referenced blob goes undetected until a client requests the affected artifact. The scale-from-zero window bounds the number of affected artifacts but not the detection latency.

## References

- [ADR-008: Content-Addressable Storage](008_content_addressable_storage.md): Storage layout and blob lifecycle
<!-- - [ADR-007: Database Schema](007_database_schema.md): Reference tracking and GC schema support -->
- [ADR-022: Namespace Decoupling](022_namespace_decoupling.md): Namespace as GC boundary
- [ADR-010: Data Retention](010_data_retention.md): Retention policies that feed into GC triggers
- [Container Registry Online GC Spec](https://gitlab.com/gitlab-org/container-registry/-/blob/master/docs/spec/gitlab/online-garbage-collection.md): Production-proven GC architecture
- [Container Registry Upload Purging Memory (#216)](https://gitlab.com/gitlab-org/container-registry/-/issues/216): Why database-tracked purging, not filesystem walks
- [Container Registry Upload Purging Scaling (#217)](https://gitlab.com/gitlab-org/container-registry/-/issues/217): Why coordinated execution, not per-instance sweeps
- [Container Registry Data Validation Service (#690)](https://gitlab.com/gitlab-org/container-registry/-/issues/690): Visibility-first approach to divergence detection
