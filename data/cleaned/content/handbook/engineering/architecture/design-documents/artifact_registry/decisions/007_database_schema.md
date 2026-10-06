---
title: "Artifact Registry ADR 007: Database Schema"
owning-stage: "~devops::package"
description: "Data tables organization for the registry"
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Context

The Artifact Registry needs a database organization that takes into account:

- **Different access patterns**: Artifact management clients will use their own protocol which is highly different from one format to another.
- **Scalability**: Artifacts storage can quickly go into millions of rows stored.
- **Performance**: Given the two previous points, we still want to maintain fast execution times on read queries which will be the vast majority of the operations.
- **Previous pitfalls**: The current container and package registry data organization is showing some cracks ([example](https://gitlab.com/groups/gitlab-org/-/work_items/16000), [example](https://gitlab.com/groups/gitlab-org/-/epics/9415)) that we will avoid here.

Before diving into the decisions, a few notes on the following schemas. These are mainly for improving the readability given the amount of tables to present.

- This document describes the core tables of the feature. Additional tables will be required for sub-features and are not described here. For example, see [Cleanup tasks](#cleanup-tasks) for background on auxiliary tables needed for blob storage cleanup.
- Table names have been shortened for readability. They will share a common prefix that is not shown here (for example, `artifacts_registry_container_repositories`).
- The Artifact Registry is scoped to namespaces. See [ADR-001](001_organizations_as_anchor_point.md) for rationale.
- Several common columns, such as primary keys or timestamps, are omitted for clarity.
- All tables include a `namespace_id` column. The [Cells sharding key requirement](https://docs.gitlab.com/ee/development/database/multiple_databases/#guidelines-on-choosing-a-sharding-key) does not apply to satellite service databases; rows are attributed to organizations indirectly through the namespace's anchor tuple (`platform`, `entity_type`, `entity_id`). This column is shown explicitly in all table definitions below.
- All `jsonb` columns must be validated against a strict JSON schema before persistence to prevent unbounded payloads and enforce expected structure. This applies to every `jsonb` column in this document (for example, `rule_configuration` and `package_json`).
- A remote repository table's encrypted credential columns do not stand alone. Each row also carries the wrapped data-encryption key that opens them and the identity of the namespace key that wrapped it (`wrapped_dek`, `ns_key_id`, `ns_key_version`), so the ciphertext is unreadable without the trio. That trio and the table's ciphertext columns form one all-or-none unit, and a CHECK constraint must enforce that either every column in the unit is set or every one is `NULL`. Partial credentials (for example, username without password) are not accepted, and neither are the partial states the trio admits: a wrapped DEK with no ciphertext, or ciphertext with no wrapped DEK. The constraint is required even where a table stores a single credential attribute, as `npm_remote_repositories` does, because those partial states do not depend on how many attributes the record holds. See [Encryption keys](#encryption-keys) for the key table and the shared column shape.
- Encrypted credential columns on remote repository tables (`encrypted_username`, `encrypted_password`, `encrypted_auth_token`) cap the plaintext input at 2048 characters, enforced at the Go validation layer before encryption. The cap is on plaintext, which only exists at the application layer; the database sees only `bytea` ciphertext, so any DB-side CHECK (e.g., `octet_length(...) <= N`) could only bound plaintext indirectly via the encryption scheme's fixed overhead (IV, auth tag, key-id header), making it an approximation of the cap and redundant with the mandatory Go check. Omitting the CHECK also keeps the schema decoupled from the crypto framing: changes to the cipher, key-id layout, or envelope structure do not require a schema migration.
- All `id` columns must be unique within the scope of an Artifact Registry instance. `namespaces.id` uses UUIDv7 ([RFC 9562](https://datatracker.ietf.org/doc/rfc9562/)) to guarantee global uniqueness across every Artifact Registry deployment — see [Namespace ID type](#namespace-id-type) for the full rationale, including the available generation paths across PostgreSQL versions. Every other API-exposed table also uses UUIDv7 for its `id`, generated in the application layer (no column default and no sequence), keeping a single identifier type across every API-exposed entity and guaranteeing global uniqueness across deployments without coordination. Application-generated UUIDv7 remains logical-replication friendly ([source](https://gitlab.com/gitlab-com/gl-infra/data-access/dbo/dbo-issue-tracker/-/work_items/691#note_3309931104)): there is no server-side sequence or `GENERATED` column to reconcile across subscribers, and UUIDv7's time-ordering keeps B-tree insert locality close to a `BIGSERIAL`. The internal blob-storage tier (`blob_storage_attachments`, `blob_storage_blobs`, `upload_sessions`) is the deliberate exception: it is never exposed through the API and carries the highest-volume rows, so it keeps `bigint DEFAULT nextval('<table>_id_seq')` ids, whose uniqueness is enforced locally within a single Artifact Registry database — sufficient because these rows are always scoped below a namespace. Every `uuid` `id` column with no server-side default carries a CHECK constraint holding the value to version 7, so the version is enforced by the schema instead of trusted to the generator.

## Decisions

We have six areas of data:

- [Namespace table](#namespaces). Decouples the Artifact Registry from external identifiers by introducing an internal namespace entity with an immutable slug and a virtual anchor tuple. See [ADR-022](022_namespace_decoupling.md) for full rationale.
- [Repository collections table](#repository-collections). A logical grouping of repositories within a namespace. Present in the schema from day one but not yet surfaced to users — every namespace gets a "default" repository collection and all repositories are assigned to it automatically.
- Namespace-level tables. These handle [lifecycle policies settings and rules](#lifecycle-policies), [namespace-level storage statistics](#storage-usage-calculation), and the [encryption keys](#encryption-keys) that wrap this namespace's stored secrets, scoped directly to the namespace.
- [Repositories parent table](#repositories). A unified registry of all repositories (hosted, virtual, remote) across all formats, powering the landing page hybrid list and cross-format queries.
- Artifact format level tables. Here we have the dedicated tables for each format: hosted repositories ([Container](#container-repositories), [Maven](#maven-repositories), [NPM](#npm-repositories)), remote repositories ([Container](#container-remote-repositories), [Maven](#maven-remote-repositories), [NPM](#npm-remote-repositories)), and virtual repositories ([Container](#virtual-container-repositories), [Maven](#maven-virtual-repositories), [NPM](#npm-virtual-repositories)). Each references the parent `repositories` table via `repository_id`.
- [Blob storage level tables](#blob-storage). Handles the actual storage metadata and [in-progress upload session tracking](#upload-sessions).

### Namespaces

```mermaid
erDiagram
    namespaces {
        uuid id PK "UUIDv7, globally unique across Artifact Registry deployments"
        text slug "NOT NULL, UNIQUE, immutable, limit 255"
        text platform "NOT NULL, limit 255"
        text entity_type "NOT NULL, limit 255"
        text entity_id "NOT NULL, opaque string, limit 255"
        text billing_entity_type "NOT NULL, limit 255"
        text billing_entity_id "NOT NULL, opaque string, limit 255"
        smallint delivery_mode_override "NULLABLE, 0=redirect, 1=proxy; per-namespace override of the instance default"
        timestamptz deleted_at "NULLABLE; set on soft-delete, reclaimable until purge (ADR-015)"
        timestamptz purged_at "NULLABLE; set on hard-delete, slug retired, anchor preserved for audit (ADR-015)"
        timestamptz blocked_at "NULLABLE; set on security-block, slug reserved but not serving (ADR-015)"
        timestamptz disabled_at "NULLABLE; set while the owning organization has the registry turned off, cleared on re-enable"
        timestamptz suspended_at "NULLABLE; set while billing-suspended, read-only service, cleared when resolved"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }
```

- **namespaces**: The root entity that all other tables reference via `namespace_id`. Each namespace has an immutable, globally unique `slug` used in URLs and client configurations (see [ADR-022](022_namespace_decoupling.md) for slug design and global uniqueness enforcement). The `(platform, entity_type, entity_id)` tuple links the namespace to an external entity (Organizations by default) without interpreting its semantics. `entity_id` is stored as `TEXT` even when the underlying value is numeric, keeping the schema uniform across anchor types. For Organizations v1, every row has `('gitlab', 'organization', '<organizations.uuid>')`: the organization's
  UUIDv7, not the numeric `organizations.id`. IAM's Relationships API rejects a non-UUIDv7 object id for the
  whole request it appears in, so the numeric id could not name the organization ancestor. `billing_entity_type` and `billing_entity_id` identify the billing anchor for usage events. None of the externally-provided columns (`platform`, `entity_type`, `entity_id`, `billing_entity_type`, `billing_entity_id`) carry schema-level defaults; see [ADR-022](022_namespace_decoupling.md) for the rationale. The `delivery_mode_override` column carries the per-namespace artifact delivery override defined by [ADR-005](005_artifact_delivery_mode.md): `NULL` inherits the instance default (`StorageConfig.delivery_mode`), `0` (`redirect`) forces redirect for this namespace, `1` (`proxy`) forces proxy. The effective delivery pattern for a download request is `namespace.delivery_mode_override ?? instance.delivery_mode`; the column is read as part of the existing namespace lookup performed by request handlers for authorization and routing, so no separate query or index is required. The column type is `SMALLINT` with the integer-to-label mapping defined in the Go application (`0 = redirect`, `1 = proxy`); PostgreSQL `ENUM` types are avoided because they are difficult to modify safely. Any future column that stores an artifact-delivery selection (for example, a per-repository override would S17 ever introduce one) reuses the same integer mapping.
- **Lifecycle events** (`deleted_at`, `purged_at`): implement the slug lifecycle defined in [ADR-015 (internal)](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/artifact_registry/decisions/015_slug_policy/#slug-lifecycle). `deleted_at` marks a soft-deleted namespace, reclaimable within the [ADR-010](010_data_retention.md#subscription-expiration) soft-delete window. `purged_at` marks a hard-deleted namespace; the slug is permanently retired and the anchor and billing columns are preserved for audit and forensics. These two are one-way event records: once set, they stay set. A purged row has both populated.
- **Service conditions** (`blocked_at`, `disabled_at`, `suspended_at`): reversible restrictions on an otherwise-live namespace. The timestamp records when the condition was imposed; `NULL` means not in effect; repeat-cycle history lives in the audit event stream, not the row. `blocked_at` marks a security block (slug reserved, no requests served; the namespace remains subscribed). `disabled_at` marks that the owning organization turned the registry off; no requests are served and the data is retained; it is set and cleared through the internal API, driven by the organization-level setting on the Rails side. `suspended_at` marks a billing suspension imposed through the internal API. Service degrades to read-only: downloads are served, writes are rejected. A payment lapse therefore does not break production consumers. The columns are independent so conditions can coexist; lifting one never lifts another.
- **Serviceability predicates**: write-serving lookups (pushes, mutations) require all five columns `NULL`. Read-serving lookups (routing, auth, downloads) require `deleted_at`, `purged_at`, `blocked_at`, and `disabled_at` to be `NULL`; a suspended namespace still serves reads. Subscription-lifecycle queries (billing, retention, and any scheduled lookup that only reads subscription state) exclude only `deleted_at` and `purged_at`, because blocked, disabled, and suspended namespaces remain subscribed. The predicate follows what the lookup does, not what schedules it: a background job that completes a write a client already asked for is a write-serving lookup and requires all five columns `NULL`, the same as the request that accepted it. That covers the deferred half of an accepted client write and nothing else. A platform-driven write, such as reclamation, counter reconciliation, or a policy-driven deletion, is not classified by this bullet. The API exposes the derived status (precedence: purged, deleted, blocked, disabled, suspended, active), which Rails caches for display ([ADR-022](022_namespace_decoupling.md#slug-discovery)).

#### Slug immutability

PostgreSQL has no native immutable-column support. Slug immutability ([ADR-022](022_namespace_decoupling.md)) is enforced at the database level with a `BEFORE UPDATE OF slug` trigger that raises an exception if the value changes. This catches any code path that bypasses the application layer (direct database access, admin tooling, migrations). The trigger can be disabled for emergency operations that require a slug change (e.g. `ALTER TABLE namespaces DISABLE TRIGGER trg_namespaces_immutable_slug`).

#### Indexes

- **`namespaces`**: unique index on `(slug)` — look up a namespace by slug. Partial unique index on `(platform, entity_type, entity_id) WHERE purged_at IS NULL` to prevent duplicate anchors among non-purged rows. Active and soft-deleted rows participate; purged rows do not, so a previously-purged organization can re-onboard with a new namespace row while the purged row keeps its anchor data for audit. No index on `delivery_mode_override`, `deleted_at`, `purged_at`, `blocked_at`, `disabled_at`, or `suspended_at`: these columns are read as part of the existing namespace lookup keyed by `id` or `slug`, and the serviceability predicates filter on a single fetched row.

The reserved slug lists defined in [ADR-015 (internal)](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/artifact_registry/decisions/015_slug_policy/#reservation-taxonomy) are not stored in the database.

### Repository collections

A repository collection is a logical grouping of repositories within a namespace, organizing artifacts by team, security domain, or product line. Surfacing repository collections in the UI and API is out of scope for the MVP — the entity exists from day one purely for forward-compatibility. During the MVP, every namespace gets a single "default" repository collection on creation and all repositories are assigned to it. Once the repository collection concept is surfaced post-MVP, users can create additional repository collections and reassign repositories to them.

```mermaid
erDiagram
    namespaces ||--o{ repository_collections : "has many"

    repository_collections {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        text name "NOT NULL, limit 255"
        boolean is_default "NOT NULL, DEFAULT false"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }
```

- **repository_collections**: A logical grouping of repositories within a namespace. `name` is a human-readable label unique within the namespace. `is_default` marks the repository collection that is automatically created with every namespace and to which all repositories are assigned during the MVP. Partitioned by `HASH(namespace_id)` with 64 partitions.

Every namespace creation must atomically insert a default repository collection row:

```sql
INSERT INTO repository_collections (namespace_id, name, is_default)
VALUES (<new_namespace_id>, 'default', true)
ON CONFLICT (namespace_id, name) DO NOTHING;
```

#### Indexes

- **`repository_collections`**: Primary key on `(id, namespace_id)` — composite PK required by `HASH(namespace_id)` partitioning; also serves as the target for the composite foreign key from `repositories`. Unique index on `(namespace_id, name)` — look up a repository collection by name within a namespace. Partial unique index on `(namespace_id) WHERE is_default IS TRUE` — enforce at most one default repository collection per namespace.

#### Query examples

- Get the default repository collection for a namespace:

  ```sql
  SELECT *
  FROM repository_collections
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND is_default = true;
  ```

- List all repository collections for a namespace:

  ```sql
  SELECT id, name, is_default, created_at
  FROM repository_collections
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
  ORDER BY created_at;
  ```

- Create a new (non-default) repository collection:

  ```sql
  INSERT INTO repository_collections (namespace_id, name)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', 'team-backend');
  ```

### Repositories

The `repositories` table is a unified parent table that registers every repository in the system regardless of format or kind. It powers the landing page hybrid list — a single sortable, filterable, paginated view showing Hosted, Virtual, and Remote repositories across all formats. Each format-specific repository table (hosted, virtual, remote) references a single row here via `repository_id`.

This model (Hosted, Remote, Virtual as peer-level standalone types, composed by reference) is what JFrog Artifactory, Sonatype Nexus, and Google Cloud AR all use, though each names the types differently.

```mermaid
erDiagram
    namespaces ||--o{ repositories : "has many"
    repository_collections }o--o{ repositories : "linked via repository_collection_repositories"

    repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        text name "NOT NULL, limit 255"
        text description "nullable, limit 1024"
        smallint format "NOT NULL, 0=docker, 1=maven, 2=npm, 3=oci"
        smallint kind "NOT NULL, 0=hosted, 1=virtual, 2=remote"
        smallint visibility "NOT NULL, 0=public, 1=private, 2=internal"
        bigint artifacts_count "NOT NULL, DEFAULT 0, buffered counter"
        bigint downloads_count "NOT NULL, DEFAULT 0, buffered counter"
        bigint size_bytes "NOT NULL, DEFAULT 0, buffered counter"
        timestamptz last_updated_at "nullable"
        timestamptz last_reconciled_at "NOT NULL, DEFAULT 'epoch', reconciliation bookkeeping"
        text gitlab_last_updated_by_user_id "nullable, opaque string, limit 255"
        timestamptz soft_deleted_at "nullable"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
        text gitlab_created_by_user_id "nullable, opaque string, limit 255"
    }
```

- **repositories**: The parent entity for all repositories. `format` identifies the artifact format (Docker, Maven, npm, OCI). `kind` identifies the repository type (hosted, virtual, remote). Repositories are linked to repository collections via the [`repository_collection_repositories`](#repository-collection-repositories) join table, allowing a repository to belong to one or more repository collections within its namespace. During the MVP, every repository is linked to the namespace's default repository collection. The `name` must be unique within a namespace, matching all competitors. Counter columns (`artifacts_count`, `downloads_count`, `size_bytes`) are maintained via [buffered/async writes](#buffered-and-asynchronous-writes) to avoid hot-row contention. `last_updated_at` tracks content changes (artifact publish/modify/delete, cache events), not downloads. `last_reconciled_at` is the repository-level counterpart to the `namespace_statistics` column of the same name (see [Storage usage calculation](#storage-usage-calculation)): reconciliation bookkeeping, stamped by the repository's own write-back, never surfaced through the API and not a counter. It carries no index of its own, unlike its namespace-level counterpart — the staleness scan that needs one selects namespaces, and a repository is reached through the namespace already chosen rather than by its own recency. Its `'epoch'` default is what lets the column be `NOT NULL` on an already-populated table: every existing row becomes valid at the moment the column is added, with no backfill and no nullable interim state. `gitlab_created_by_user_id` and `gitlab_last_updated_by_user_id` record which GitLab user created and last modified the repository; both are nullable opaque references with no foreign key and no application-side validation, because the user record lives in the monolith — rendering the user handle and avatar is the consumer's responsibility, the AR schema only stores the ID. They are stored as `TEXT` for the same reason as `namespaces.entity_id`: a future change in the upstream user-ID format (for example to UUID) does not require a schema migration. `description` is on the parent because the UI shows descriptions for all repo types, not just virtual ones. The `soft_deleted_at` timestamp records when the repository was soft deleted, enabling restoration if needed. Soft deletion is on the parent table so that all repository types (hosted, virtual, remote) share the same deletion semantics without format-specific handling. Partitioned by `HASH(namespace_id)` with 64 partitions.

Hard-deleting a repository cascades to its structural children. The foreign keys involved carry these referential actions:

- The format child tables (`container_repositories`, `npm_repositories`, `maven_repositories`, and their virtual and remote variants), FK `(repository_id, namespace_id)` referencing `repositories`: `ON DELETE CASCADE`.
- `repository_collection_repositories` (the collection join table), FK `(repository_id, namespace_id)` referencing `repositories`: `ON DELETE CASCADE`.
- The artifact tables (`container_images`, `npm_packages`, `maven_packages`), FK `(<format>_repository_id, namespace_id)` referencing their format child table: `NO ACTION`.
- The virtual upstream junction tables (`container_virtual_repository_upstreams`, `maven_virtual_repository_upstreams`, `npm_virtual_repository_upstreams`), FK `(upstream_repository_id, namespace_id)` referencing `repositories`: `NO ACTION`.

A single `DELETE FROM repositories` therefore removes the format child row and every collection link. The `NO ACTION` keys can refuse it, and any one rejection aborts the whole statement. The artifact-to-child key refuses while the repository still holds artifacts. The junction key refuses while any virtual repository still lists it as an upstream, whatever format that virtual repository is.

The list above covers the keys whose action this document states, which is not every key it draws. Two more ERD entries declare a `repositories` foreign key and leave the action unstated: `artifact_type_repository_lifecycle_policy_settings` and `upload_sessions`. The shipped schema carries neither foreign key, so neither refuses a delete today. Either would once added as its ERD entry describes it, because an unstated action is `NO ACTION`.

Two tests decide an edge's action, and an edge has to pass both to cascade. Direction is the first: only a parent-to-child edge cascades, so the delete follows the structural chain down from `repositories` and never sideways. What the child holds is the second: among those downward edges, cascade where the child is pure structure (the format child row, the collection link) and reject where it is user data (artifacts). `upstream_repository_id` fails the first test rather than the second — it names a repository this one does not own — so no reading of what a junction row holds makes it cascade. Together these are the declarative counterpart to the soft-delete path above and the application-managed `blob_storage_attachments` cleanup.

Neither refusal reaches an operator through the referential action alone, and which way it fails depends on when the statement runs. Where the delete is synchronous, the rejection arrives as a failed statement that the API layer has to recognize and translate. Where the delete is asynchronous — a tombstone now, the `DELETE FROM repositories` in a later purge — the rejection shows as a stalled purge and reaches no caller at all. The refusal an operator can rely on therefore comes from the management API, at the delete request and ahead of either path: see [Repository Deletion](009_api_design.md#repository-deletion). These keys are the backstop under that check, not the signal.

#### Indexes

- **`repositories`**: unique index on `(namespace_id, name)` — enforce name uniqueness across both active and soft-deleted repositories, ensuring restoration never fails due to a name conflict. Name reuse requires hard-deletion first. Index on `(namespace_id, name) WHERE soft_deleted_at IS NULL` — optimized scan path for active-repository lookups and name-ordered listings. Index on `(namespace_id, format) WHERE soft_deleted_at IS NULL` — filter active repositories by format. Index on `(namespace_id, kind) WHERE soft_deleted_at IS NULL` — filter active repositories by kind. Index on `(namespace_id, visibility) WHERE soft_deleted_at IS NULL` for filtering repositories by visibility level (powers the visibility-audit query: "which repositories in this namespace are public right now?"). One index per sortable column for the landing page, all with `WHERE soft_deleted_at IS NULL` and a trailing `id DESC` keyset tiebreaker: `(namespace_id, artifacts_count DESC, id DESC)`, `(namespace_id, downloads_count DESC, id DESC)`, `(namespace_id, size_bytes DESC, id DESC)`, and the expression index `(namespace_id, COALESCE(last_updated_at, created_at) DESC, id DESC)`. The `id` half of a `ROW(<col>, id)` keyset bound must be index-resident. The counter columns (`artifacts_count`, `downloads_count`, `size_bytes`) default to `0` and are low-cardinality, so without the tiebreaker in the index the planner applies it as a post-scan sort/filter, degrading deep pages to O(offset) over the namespace. The expression index also carries `id DESC`, not for cardinality (`COALESCE(last_updated_at, created_at)` is high-cardinality, since `created_at` is unique per row) but to give the keyset a deterministic cursor. The recency sort orders by `COALESCE(last_updated_at, created_at)`, not raw `last_updated_at`: a never-updated repository (NULL `last_updated_at`, the common case for a fresh repo) then ranks by its creation time and sorts to the top of "recently updated" instead of sinking under `NULLS LAST`, and because the coalesced key is never NULL the keyset bound is a plain `ROW(<col>, id)` comparison that folds into the index range with no NULL-region special case. The serialized `last_updated_at` field stays nullable; only the sort key coalesces. The `name` sort needs no tiebreaker — its `(namespace_id, name)` unique index is already a deterministic keyset. Index on `(namespace_id, format, name) WHERE soft_deleted_at IS NULL` for the format-filtered name listing (the primary browse view: filter by format, sort by name): it seeks the `(format, name)` range directly and stays index-only, instead of driving off the `(namespace_id, name)` unique index with `format` as a post-index filter that scans past wrong-format rows. Only the format+name combination is indexed; the rarer counter/timestamp sorts keep `format`/`kind` as a post-index filter rather than fan out a composite index per sort-by-filter pair. Index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted repositories in this namespace ordered by deletion time (powers the trash-listing query: "what's in the trash and when was it deleted?"). The inverse partial predicate mirrors the active-row partials above: every other partial on this table excludes the trash, and the full `(namespace_id, name)` unique index does not key `soft_deleted_at`, so a trash listing would otherwise have to visit every row in the namespace to filter and sort. GC eligibility is derived from `soft_deleted_at + retention_window` per [ADR-010](010_data_retention.md); no separate column is needed.

During the MVP, all repositories are linked to a single default repository collection, so the `(namespace_id, ...)` sort indexes serve both namespace-wide and collection-filtered queries. Post-MVP, when namespaces have multiple repository collections, collection-filtered queries join through `repository_collection_repositories`; additional supporting indexes will be evaluated when repository collections are surfaced.

#### Query examples

- List all repositories for a namespace (all repository collections), ordered by last update:

  ```sql
  SELECT id, name, description, format, kind, artifacts_count,
         downloads_count, size_bytes, last_updated_at
  FROM repositories
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND soft_deleted_at IS NULL
  ORDER BY COALESCE(last_updated_at, created_at) DESC
  LIMIT 20;
  ```

- List repositories for a namespace filtered by repository collection, ordered by last update:

  ```sql
  SELECT r.id, r.name, r.description, r.format, r.kind, r.artifacts_count,
         r.downloads_count, r.size_bytes, r.last_updated_at
  FROM repositories r
  JOIN repository_collection_repositories rcr
    ON rcr.namespace_id = r.namespace_id AND rcr.repository_id = r.id
  WHERE r.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND rcr.repository_collection_id = '019a1b2c-0456-7abc-8def-000000000456' AND r.soft_deleted_at IS NULL
  ORDER BY COALESCE(r.last_updated_at, r.created_at) DESC
  LIMIT 20;
  ```

- List repositories filtered by repository collection and format:

  ```sql
  SELECT r.id, r.name, r.description, r.format, r.kind, r.artifacts_count,
         r.downloads_count, r.size_bytes, r.last_updated_at
  FROM repositories r
  JOIN repository_collection_repositories rcr
    ON rcr.namespace_id = r.namespace_id AND rcr.repository_id = r.id
  WHERE r.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND rcr.repository_collection_id = 456 AND r.format = 0
    AND r.soft_deleted_at IS NULL
  ORDER BY r.name
  LIMIT 20;
  ```

- Look up a single repository by name:

  ```sql
  SELECT *
  FROM repositories
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND name = 'my-repo' AND soft_deleted_at IS NULL;
  ```

- Visibility audit: list every public repository in a namespace (uses the partial index on `(namespace_id, visibility) WHERE soft_deleted_at IS NULL`):

  ```sql
  SELECT id, name, format, kind
  FROM repositories
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND visibility = 0 AND soft_deleted_at IS NULL
  ORDER BY name;
  ```

- Trash listing: list every soft-deleted repository in a namespace, most-recently-deleted first (uses the partial index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL`). The scope is namespace-wide so administrators can answer "what is recoverable right now?" in one query; per-parent trash views are a separate UI concern and can be served by adding a parent-keyed index later if needed.

  ```sql
  SELECT id, name, format, kind, soft_deleted_at
  FROM repositories
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND soft_deleted_at IS NOT NULL
  ORDER BY soft_deleted_at DESC
  LIMIT 50;
  ```

### Repository collection repositories

The `repository_collection_repositories` join table maps repositories to the repository collections they belong to. A repository can be a member of one or more repository collections within its namespace, enabling shared-access scenarios such as a common util repository surfaced through several teams' repository collections.

```mermaid
erDiagram
    repository_collections ||--o{ repository_collection_repositories : "has many"
    repositories ||--o{ repository_collection_repositories : "has many"

    repository_collection_repositories {
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id), part of composite PK (namespace_id, repository_collection_id, repository_id)"
        uuid repository_collection_id PK,FK "NOT NULL, (repository_collection_id, namespace_id) references repository_collections(id, namespace_id)"
        uuid repository_id PK,FK "NOT NULL, (repository_id, namespace_id) references repositories(id, namespace_id)"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }
```

- **repository_collection_repositories**: Links repositories to repository collections. During the MVP, every repository is linked to exactly one repository collection (the namespace's default), but the schema permits multiple links so a repository can be shared across repository collections post-MVP. The application enforces the invariant that every repository has at least one repository collection link — Postgres cannot express this declaratively. The composite FKs ensure a repository collection and repository can only be linked within the same namespace. Partitioned by `HASH(namespace_id)` with 64 partitions.

#### Indexes

- **`repository_collection_repositories`**: Primary key on `(namespace_id, repository_collection_id, repository_id)` — enforces uniqueness of a link and serves lookups by repository collection. Index on `(namespace_id, repository_id)` — look up every repository collection a given repository belongs to.

#### Query examples

- List every repository collection a repository belongs to:

  ```sql
  SELECT repository_collection_id
  FROM repository_collection_repositories
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND repository_id = '019a1b2c-0789-7abc-8def-000000000789';
  ```

- Link a repository to a repository collection:

  ```sql
  INSERT INTO repository_collection_repositories (namespace_id, repository_collection_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0456-7abc-8def-000000000456', '019a1b2c-0789-7abc-8def-000000000789')
  ON CONFLICT (namespace_id, repository_collection_id, repository_id) DO NOTHING;
  ```

### Lifecycle Policies

```mermaid
erDiagram
    lifecycle_policy_settings ||--o{ lifecycle_rules : "has many"

    lifecycle_policy_settings {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, UNIQUE, references namespaces(id)"
        boolean enabled "NOT NULL"
    }

    lifecycle_rules {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid lifecycle_policy_settings_id FK "NOT NULL, (lifecycle_policy_settings_id, namespace_id) references lifecycle_policy_settings(id, namespace_id)"
        smallint rule_type "NOT NULL, 0=keep_last_downloaded_at, 1=keep_last_n, 2=keep_regex"
        jsonb rule_configuration "NOT NULL"
    }
```

- **lifecycle_policy_settings**: Defines lifecycle management configuration at the namespace level, serving as the default policy for all repositories. When enabled, associated lifecycle rules are applied namespace-wide. These policies can be [overridden](#repository-level-overrides) by repository-level policies. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **lifecycle_rules**: Specifies individual retention and cleanup rules that govern specific artifacts lifecycle behavior at the namespace level. These rules apply to all repositories unless [overridden](#repository-level-overrides) at the repository level. The number of lifecycle rules per policy record will be limited to prevent performance degradation during rule evaluation. This is used for users to specify, for example, how long certain artifacts are kept around (for example, Maven snapshots files could be kept for 1 month only). Partitioned by `HASH(namespace_id)` with 64 partitions.

#### Indexes

- **`lifecycle_policy_settings`**: unique index on `(namespace_id)` — one policy settings record per namespace.
- **`lifecycle_rules`**: index on `(namespace_id, lifecycle_policy_settings_id)` — fetch all rules for a given policy.

Repository-level override tables follow the same pattern: unique index on `(namespace_id, repository_id)` for the settings table and index on `(namespace_id, <format>_repository_lifecycle_policy_settings_id)` for the rules table.

#### Query examples

- Getting the policy for a given namespace

  ```sql
  SELECT lp.*
  FROM lifecycle_policy_settings lp
  WHERE lp.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8';
  ```

- Getting the policy of a given artifact repository

  ```sql
  SELECT *
  FROM container_repository_lifecycle_policy_settings
  WHERE container_repository_lifecycle_policy_settings.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND container_repository_lifecycle_policy_settings.repository_id = '019a1b2c-0123-7abc-8def-000000000123';
  ```

- Creating a new lifecycle rule

  ```sql
  INSERT INTO lifecycle_rules (namespace_id, lifecycle_policy_settings_id, rule_type, rule_configuration)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0123-7abc-8def-000000000123', 1, '{"count": 10}'::jsonb);
  ```

- Updating a lifecycle rule

  ```sql
  UPDATE lifecycle_rules
  SET rule_configuration = '{"count": 20}'::jsonb
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND id = '019a1b2c-0123-7abc-8def-000000000123';
  ```

- Destroying a lifecycle rule

  ```sql
  DELETE FROM lifecycle_rules
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND id = '019a1b2c-0123-7abc-8def-000000000123';
  ```

#### Repository level overrides

Each repository type ([container](#container-repositories), [maven](#maven-repositories) and [npm](#npm-repositories)) will have similarly named tables to provide overrides to the namespace-level values. This creates a priority system: namespace (lowest) -> Repository (highest). Overrides reference the parent `repositories` table via `repository_id`.

```mermaid
erDiagram
    artifact_type_repository ||--|| artifact_type_repository_lifecycle_policy_settings : "has one"
    artifact_type_repository ||--o{ artifact_type_repository_lifecycle_rules : "has many"

    artifact_type_repository_lifecycle_policy_settings {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid repository_id FK "NOT NULL, (repository_id, namespace_id) references repositories(id, namespace_id)"
        boolean enabled "NOT NULL"
    }

    artifact_type_repository_lifecycle_rules {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid artifact_type_repository_lifecycle_policy_settings_id FK "NOT NULL, (artifact_type_repository_lifecycle_policy_settings_id, namespace_id) references artifact_type_repository_lifecycle_policy_settings(id, namespace_id)"
        smallint rule_type "NOT NULL, 0=keep_last_downloaded_at, 1=keep_last_n, 2=keep_regex"
        jsonb rule_configuration "NOT NULL"
    }
```

(`artifact_type` needs to be replaced by `container`, `maven` and `npm` since we have overrides table in each artifact format. These overrides apply to hosted, virtual, and remote repositories alike — the `repository_id` FK references the parent `repositories` table, and the format-specific table is determined by the repository's `format` column.)

These tables act in a way as [cascading settings](https://docs.gitlab.com/development/cascading_settings/). Their descriptions are exactly the same as the similarly named tables on the [namespace level](#lifecycle-policies), including partitioning: every override table is partitioned by `HASH(namespace_id)` with 64 partitions. The current two-tier priority system (namespace → repository) can be extended to three tiers (namespace → repository collection → repository) when repository collections are surfaced post-MVP. This requires adding repository-collection-level override tables following the same pattern; no changes to existing namespace-level or repository-level tables are needed.

### Encryption keys

```mermaid
erDiagram
    namespaces ||--o{ namespace_encryption_keys : "has many"

    namespace_encryption_keys {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        int version "NOT NULL, CHECK >= 1, UNIQUE (namespace_id, version)"
        bytea wrapped_key "NOT NULL, the namespace key wrapped by the deployment root key; emptied to zero length on crypto-shred"
        text root_key_uri "NOT NULL, limit 255, names the root key this row was wrapped under"
        boolean active "NOT NULL, DEFAULT true"
        timestamptz shredded_at "nullable, crypto-shred tombstone marker"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }
```

- **namespace_encryption_keys**: One row per key-encryption key a namespace has held, each wrapped by the deployment root key. A namespace has one active key at a time; superseded versions stay in the table deactivated rather than deleted, because rows wrapped under an earlier version still resolve their key through it. The `id` is the referential identity, which a credential row names in `ns_key_id`, while `version` is a per-namespace ordinal that orders a namespace's keys and drives the rotation sweep. The two are not interchangeable: `version` restarts at 1 when a shredded namespace is re-enabled, so it cannot identify a key across the namespace's lifetime, and reads resolve the wrapping key by `ns_key_id`. Crypto-shredding retains the rows as tombstones instead of deleting them: `wrapped_key` is overwritten with a zero-length `bytea`, `active` is cleared, and `shredded_at` is stamped, so the shredded state survives restarts and holds across every instance. Two per-row CHECK constraints hold that shape: one refuses to leave a tombstone marked active, and one ties key material to liveness in both directions, so key material is present exactly when `shredded_at` is `NULL`. The namespace-wide invariant, that any tombstone shreds the whole namespace, is enforced in the application layer, which is the limit of what a per-row CHECK reaches. Partitioned by `HASH(namespace_id)` with 64 partitions.

#### Indexes

- **`namespace_encryption_keys`**: unique index on `(namespace_id, version)`, which holds the per-namespace version ordinal; partial unique index on `(namespace_id) WHERE active = true`, which is both the one-active-key-per-namespace guarantee and the lookup a credential write makes to find the key to wrap under; partial index on `(namespace_id) WHERE shredded_at IS NOT NULL`, to detect a shredded namespace on the read path without scanning its key history; partial index on `(root_key_uri) WHERE shredded_at IS NULL`, to find the live rows still wrapped under a given root key, which is what a root key rotation walks and what its completion check counts. Shredded rows are excluded from that last index deliberately: a shredded namespace keeps its old `root_key_uri` forever and its `wrapped_key` is already emptied, so rotation must not pick those rows up. Of the four, only that one leads with a column other than `namespace_id`, because the query it serves names a root key and no namespace. Like every index on a partitioned table it is local to each partition, so that read fans out across all 64 instead of pruning to one. Root key rotation walks the rows in bounded batches as a background job, so the fan-out is acceptable there in a way it would not be on a request path.

#### Credential columns on remote repository tables

The three remote repository tables ([Container](#container-remote-repositories), [Maven](#maven-remote-repositories), [NPM](#npm-remote-repositories)) store upstream credentials as ciphertext under a per-row data-encryption key, and each carries the same three columns alongside its ciphertext:

- `wrapped_dek` (`bytea`): the row's data-encryption key, wrapped by the namespace key.
- `ns_key_id` (`uuid`): the `namespace_encryption_keys` row that wrapped it. Composite foreign key on `(ns_key_id, namespace_id)` referencing `namespace_encryption_keys(id, namespace_id)` with `ON DELETE RESTRICT`, so a key version cannot be deleted while a credential row still depends on it.
- `ns_key_version` (`int`): the namespace key version the row was wrapped under, denormalized from the key row so the namespace key rotation sweep can select the rows still on an older version without joining the key table. The sweep walks a namespace's rows in row-id order under a keyset cursor, so the plan that serves that order without a sort leads on the primary key `(id, namespace_id)` and applies both `namespace_id` and the version inside the scan; the `(namespace_id, ns_key_id)` index described below serves the foreign key, not this read. `namespace_id` still confines the sweep to one partition, because it is the hash partition key, not because an index leads with it. Confining the scan within that partition would need a `(namespace_id, id)` index, which these tables do not carry. No index leads with `ns_key_version`: the scan reads one partition rather than one namespace, and the sweep walks that partition in bounded batches from an operator-run rotation pass, so the rows it examines beyond the namespace's own are acceptable there in a way they would not be on a request path. These tables also change only on administrative writes. Reads resolve the wrapping key by `ns_key_id`, never by this column.

All three are nullable, because a remote repository that needs no upstream credential is legal, and the all-or-none CHECK described in [Context](#context) is what keeps a row from holding part of the unit. Each table also carries an index on `(namespace_id, ns_key_id)`. PostgreSQL indexes the referenced side of a foreign key, not the referencing side, so without it every attempt to delete a key row scans the whole credential table to enforce `ON DELETE RESTRICT`. The action is written `ON DELETE RESTRICT`, where this document writes `ON DELETE NO ACTION` for the other keys that refuse a delete. None of these keys is `DEFERRABLE`, so the two spellings behave identically; `RESTRICT` is chosen because it also rules out ever deferring the check, which keeps the refusal on the statement that deletes the key row instead of on the transaction's commit.

Two key tiers sit above the row: the deployment root key wraps the namespace key, and the namespace key wraps each row's DEK. Each tier rotates independently and neither one re-encrypts a credential ciphertext. Rotating the root key wraps `namespace_encryption_keys.wrapped_key` under the new root key and updates `root_key_uri`, touching no credential row at all. Rotating a namespace key wraps each credential row's `wrapped_dek` under the new namespace key and updates its `ns_key_id` and `ns_key_version`, leaving the ciphertext columns as they are. Only a credential write replaces the ciphertext, and it generates a fresh DEK each time.

### Container Repositories

The challenge in this part is to adhere to the [OCI Distribution Spec v1.1](https://github.com/opencontainers/distribution-spec/blob/main/spec.md).

<!--TODO This link will not live for long since it's an artifact output-->
The approach was heavily inspired by the [GitLab Container Registry schema](https://gitlab.com/gitlab-org/container-registry/-/jobs/12449560500/artifacts/file/db-DAG.png).

```mermaid
erDiagram
    repositories ||--|| container_repositories : "has one"
    container_repositories ||--o{ container_images : "has many"
    container_images ||--o{ container_blobs : "has many"
    container_images ||--o{ container_manifests : "has many"
    container_images ||--o{ container_manifest_relationships : "has many"
    container_images ||--o{ container_tags : "has many"
    container_tags ||--|| container_manifests : "has one"
    container_blobs ||--|| blob_storage_attachments : "has one"
    container_manifests ||--|| blob_storage_attachments : "has one"
    container_manifest_relationships ||--|| container_manifests : "has one (parent_id)"
    container_manifest_relationships ||--|| container_manifests : "has one (child_id)"

    container_repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid repository_id FK "NOT NULL, UNIQUE (namespace_id, repository_id), (repository_id, namespace_id) references repositories(id, namespace_id)"
    }

    container_images {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_repository_id FK "NOT NULL, (container_repository_id, namespace_id) references container_repositories(id, namespace_id)"
        text name "NOT NULL, limit 255"
        timestamptz last_downloaded_at "nullable, buffered"
        timestamptz soft_deleted_at "nullable"
    }

    container_blobs {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_image_id FK "NOT NULL, (container_image_id, namespace_id) references container_images(id, namespace_id)"
        bytea digest "NOT NULL, CHECK octet_length = 32"
        text media_type "NOT NULL, limit 255"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, CHECK octet_length = 32, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        timestamptz soft_deleted_at "nullable"
    }

    container_manifests {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_image_id FK "NOT NULL, (container_image_id, namespace_id) references container_images(id, namespace_id)"
        bytea digest "NOT NULL, CHECK octet_length = 32"
        text media_type "NOT NULL, limit 255"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, CHECK octet_length = 32, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        bigint size "NOT NULL, precomputed at push time"
        text gitlab_user_id "nullable, opaque string, limit 255"
        text gitlab_project_id "nullable, opaque string, limit 255"
        bytea gitlab_git_commit_sha "nullable"
        timestamptz soft_deleted_at "nullable"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }

    container_manifest_relationships {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_image_id FK "NOT NULL, (container_image_id, namespace_id) references container_images(id, namespace_id)"
        uuid parent_container_manifest_id FK "NOT NULL, (namespace_id, container_image_id, parent_container_manifest_id) references container_manifests(namespace_id, container_image_id, id)"
        uuid child_container_manifest_id FK "NOT NULL, (namespace_id, container_image_id, child_container_manifest_id) references container_manifests(namespace_id, container_image_id, id)"
    }

    container_tags {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_image_id FK "NOT NULL, (container_image_id, namespace_id) references container_images(id, namespace_id)"
        uuid container_manifest_id FK "NOT NULL, (container_manifest_id, namespace_id) references container_manifests(id, namespace_id)"
        text name "NOT NULL, limit 255"
    }
```

- **container_repositories**: The container of multiple images. Each repository can host multiple images with independent versioning. References the parent `repositories` table via `repository_id` for name, visibility, and cross-format queries. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_images**: Represents a named container image within a repository (for example, `myapp`, `backend`). `last_downloaded_at` records when the image was last pulled; maintained via [buffered/async writes](#buffered-and-asynchronous-writes). Used by `keep_last_downloaded_at` lifecycle rules to evaluate download-based retention ([ADR-010](010_data_retention.md)). The `soft_deleted_at` timestamp records when the image was soft deleted, enabling restoration if needed. Deleting an image is also the one container delete that cannot complete inside a request-bounded transaction: a tag delete removes one row, and a manifest delete is bounded by the 1,000-tag limit from [ADR-004](004_data_and_application_limits.md#entity-count-limits), while an image holds up to 25,000 manifests, each permitted 200 references. An image delete therefore marks the row and leaves the reap to a background pass, which is why this table carries an image-level tombstone-discovery index that the manifest-level tombstone index cannot serve (see the index list below). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_blobs**: Stores individual content-addressable layers and configuration objects that comprise container images. The relationship between a manifest and its constituent layers (blobs) is implicit — determined by parsing the manifest content at runtime — and is not modeled as a database foreign key. The `soft_deleted_at` timestamp records when the blob was soft deleted, enabling restoration if needed. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_manifests**: Represents the image manifest that describes the configuration and layers for a specific image version. The `size` column holds the total byte size of the manifest tree rooted here: this manifest's own payload plus every blob reachable from it, transitively through any child manifests for manifest lists and OCI indexes. `gitlab_user_id` records which GitLab user pushed this manifest; nullable opaque text reference with no foreign key, same rationale as the equivalent column on [repositories](#repositories) — the user record lives in the monolith, rendering the user handle and avatar is the consumer's responsibility, the AR schema stores only the ID, and `TEXT` insulates the schema from any future change to the upstream user-ID format. `gitlab_project_id` and `gitlab_git_commit_sha` extend that attribution with the rest of the publish context: `gitlab_project_id` is the GitLab project the push originated from (for example, `CI_PROJECT_ID`), stored as nullable opaque text for the same monolith-reference reasons as `gitlab_user_id`. `gitlab_git_commit_sha` is the publish-time Git commit (for example, `CI_COMMIT_SHA`), stored as nullable `bytea` per the schema convention for hash columns — variable-length, fits both SHA-1 (20 bytes) and SHA-256 (32 bytes); it is a publish-time fact rather than a monolith reference, so no foreign key is needed. Both are NULL when the push arrives without CI context (for example, a manual push from a developer workstation). The `soft_deleted_at` timestamp records when the manifest was soft deleted, enabling restoration if needed. `created_at` records when the manifest was first pushed; combined with the per-namespace time-ordered index it powers publication-history and time-range artifact-provenance queries (for example, "what was pushed to this namespace between 2am and 8am?"). Soft-deleted rows continue to appear in publication history because the publish event itself is not erased by deletion. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_manifest_relationships**: Handles Docker manifest lists and OCI indexes (such as for multi-architecture images) where a parent manifest can reference multiple other manifests. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_tags**: Provides human-readable names (for example, `latest`, `v1.2.3`) that point to specific manifests. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **blob_storage_attachments**: See [Blob storage](#blob-storage) section for details.

The `container_blobs` table does not directly store the container registry physical blobs as other container registry architectures might do. The difference here is that the blob storage is handled in the [blob storage](#blob-storage) tables (along with deduplication and garbage collection). Thus, at the `container_*` level, we simply need to store a reference to a `blob_storage_attachments` record and that's it.

#### Indexes

- **`container_repositories`**: unique index on `(namespace_id, repository_id)` — look up a container repository by its parent repository reference.
- **`container_images`**: unique index on `(namespace_id, container_repository_id, name) WHERE soft_deleted_at IS NULL` — an image name identifies a unique image within a repository; duplicates would break OCI name-based lookups. The partial condition allows recreating an image with the same name after soft deletion; index on `(namespace_id, container_repository_id, last_downloaded_at NULLS FIRST) WHERE soft_deleted_at IS NULL` — support `keep_last_downloaded_at` lifecycle rule evaluation; returns only aged-out images via a bounded range scan rather than scanning every image in the repository and filtering row-by-row. `NULLS FIRST` groups never-downloaded images with the oldest rows so both are returned by the same range scan; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted images ordered by deletion time, powering the image-granularity trash listing and the reaper's image-level scan. The `container_manifests` index of this shape cannot serve either: it is keyed on manifests, and a soft-deleted image's manifests carry no `soft_deleted_at` of their own, so neither a manifest scan nor a repository walk reaches a tombstoned image whose repository is still live.
- **`container_blobs`**: unique index on `(namespace_id, container_image_id, digest) WHERE soft_deleted_at IS NULL` — a blob digest is content-addressed; the same digest within the same image is the same blob by definition. The partial condition allows re-pushing the same digest after soft deletion; index on `(namespace_id, blob_storage_attachment_id)` — look up a blob by its storage attachment; index on `(namespace_id, digest)` — cross-image lookup by content digest, used for blob mount. A container blob is content-addressed, so its `digest` equals its stored `blob_sha256`; this index therefore also serves cross-format checksum search and the vulnerability-impact query "given this compromised digest, which images reference it?", which is a layer/config-digest lookup, without a separate `(namespace_id, blob_sha256)` index. Reverse-lookup indexes in this document are unconditional (no `soft_deleted_at` predicate) so a digest that was once referenced still appears in the audit trail; vulnerability impact, which only wants currently-affected artifacts, adds `soft_deleted_at IS NULL` at query time — a cheap post-filter on a small intermediate set. Maven and npm files are not content-addressed and have no equivalent digest column, which is why those tables keep a dedicated `(namespace_id, blob_sha256)` reverse-lookup index and the container tables do not. This equivalence holds while sha256 is the only digest algorithm: `digest` and `blob_sha256` are both 32-byte values under the `octet_length = 32` CHECK, and content is verified against its digest on write, so the `(namespace_id, digest)` index returns exactly the rows a `blob_sha256` index would. A future non-sha256 digest algorithm would separate the two columns and reopen this.
- **`container_manifests`**: unique index on `(namespace_id, container_image_id, digest) WHERE soft_deleted_at IS NULL` — a manifest digest is content-addressed; the same digest within the same image is the same manifest by definition. The partial condition allows re-pushing the same digest after soft deletion; index on `(namespace_id, blob_storage_attachment_id)` — look up a manifest by its storage attachment; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted manifests ordered by deletion time, powering the artifact-granularity trash-listing query for container images; index on `(namespace_id, created_at DESC)` — chronological scans across the namespace, powering publication-history pagination and time-range artifact-provenance queries. Unconditional (no `soft_deleted_at` predicate) so a publish event that was later soft-deleted still appears in the audit trail; unique index on `(namespace_id, container_image_id, id)` — the target of the two image-scoped manifest references from `container_manifest_relationships`. The primary key already makes the triple unique, so this index adds no uniqueness guarantee. It exists because PostgreSQL requires a declared unique constraint or index over the columns a foreign key references, and infers none from the primary key. Unlike `container_blobs`, `container_manifests` has no standalone `(namespace_id, digest)` index — its digest is indexed only within an image, by the unique `(namespace_id, container_image_id, digest)` — so a cross-image checksum search over manifest payloads (a manifest's `digest` equals its stored `blob_sha256`) scans the namespace-pruned partition. This is accepted: no MVP endpoint issues that query, and the vulnerability-impact lookup is a layer/config-digest query served by the `container_blobs` `(namespace_id, digest)` index.
- **`container_manifest_relationships`**: unique index on `(namespace_id, parent_container_manifest_id, child_container_manifest_id)` — prevent duplicate parent-child relationships and find all children of a given parent manifest; index on `(namespace_id, child_container_manifest_id, parent_container_manifest_id)` — find all parents of a given child manifest, in parent-id order off the index rather than through a sort; index on `(namespace_id, container_image_id)` — find all manifest relationships for a given image.
- **`container_tags`**: unique index on `(namespace_id, container_image_id, name)` — look up a tag by name within an image; index on `(namespace_id, container_manifest_id, name)` — find all tags pointing to a given manifest, in name order off the index rather than through a sort.

#### Query examples

- Get image by name

  ```sql
  SELECT *
  FROM container_images
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND container_repository_id = '019a1b2c-0123-7abc-8def-000000000123' AND name = 'myapp/backend'
    AND soft_deleted_at IS NULL;
  ```

- Get blob by digest for a repository id

  ```sql
  SELECT cb.*
  FROM container_blobs cb
  JOIN container_images ci
    ON cb.container_image_id = ci.id AND cb.namespace_id = ci.namespace_id
  WHERE ci.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND ci.container_repository_id = '019a1b2c-0123-7abc-8def-000000000123'
    AND cb.digest = 'sha256:abcd1234...'::bytea
    AND ci.soft_deleted_at IS NULL AND cb.soft_deleted_at IS NULL;
  ```

- Get manifest by digest for a repository id

  ```sql
  SELECT cm.*
  FROM container_manifests cm
  JOIN container_images ci
    ON cm.container_image_id = ci.id AND cm.namespace_id = ci.namespace_id
  WHERE ci.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND ci.container_repository_id = '019a1b2c-0123-7abc-8def-000000000123'
    AND cm.digest = 'sha256:efgh5678...'::bytea
    AND ci.soft_deleted_at IS NULL AND cm.soft_deleted_at IS NULL;
  ```

- Checksum search and vulnerability impact: given a stored blob `sha256`, find every artifact in the namespace that references it. The `namespace_id` equality prunes to a single partition per table. Maven and npm files use the `(namespace_id, blob_sha256)` index, which returns the matching rows directly instead of scanning the partition. The container tables are content-addressed — a blob's or manifest's `digest` equals its stored `blob_sha256` — so `container_blobs` answers this through its `(namespace_id, digest)` index; `container_manifests` has no standalone digest index, so a manifest-payload lookup scans the namespace-pruned partition. Checksum search returns all references; vulnerability impact ("which artifacts are currently affected by this compromised digest?") adds `soft_deleted_at IS NULL` to restrict the result to active artifacts.

  ```sql
  -- Single format: container layer/config blobs referencing the digest.
  -- container_blobs is content-addressed (digest = blob_sha256) and has a
  -- (namespace_id, digest) index, so this reverse lookup rides that index
  -- rather than a dedicated blob_sha256 one. container_manifests has no
  -- standalone digest index. See the cross-format query below.
  SELECT cb.id, cb.container_image_id, cb.digest
  FROM container_blobs cb
  WHERE cb.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND cb.digest = 'sha256:abcd1234...'::bytea;

  -- Cross-format: every artifact referencing the digest, active rows only (vulnerability impact)
  SELECT 'container_blob' AS artifact_kind, cb.id AS artifact_id, cb.container_image_id AS parent_id
  FROM container_blobs cb
  WHERE cb.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND cb.digest = 'sha256:abcd1234...'::bytea AND cb.soft_deleted_at IS NULL
  UNION ALL
  -- container_manifests has no standalone (namespace_id, digest) index, so this
  -- arm scans the namespace-pruned partition (accepted: no MVP endpoint issues
  -- a cross-image manifest-payload checksum search).
  SELECT 'container_manifest', cm.id, cm.container_image_id
  FROM container_manifests cm
  WHERE cm.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND cm.digest = 'sha256:abcd1234...'::bytea AND cm.soft_deleted_at IS NULL
  UNION ALL
  SELECT 'maven_file', mf.id, mf.maven_version_id
  FROM maven_files mf
  WHERE mf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND mf.blob_sha256 = 'sha256:abcd1234...'::bytea AND mf.soft_deleted_at IS NULL
  UNION ALL
  SELECT 'npm_file', nf.id, nf.npm_version_id
  FROM npm_files nf
  WHERE nf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND nf.blob_sha256 = 'sha256:abcd1234...'::bytea AND nf.soft_deleted_at IS NULL;
  ```

  The same `(namespace_id, blob_sha256)` access path applies to the cache-side tables (`container_remote_blobs`, `container_remote_manifests`, `maven_remote_files`, `npm_remote_files`) and to `npm_metadata_files` / `npm_remote_metadata_files`; extend the `UNION ALL` to those tables to also cover cached references.

### Container Remote Repositories

Remote repositories represent external container registries that can be proxied and cached. They are standalone entities with their own lifecycle, shareable across multiple virtual repositories. They are referenced by virtual repository upstreams via the parent `repositories` table.

```mermaid
erDiagram
    repositories ||--|| container_remote_repositories : "has one"
    container_remote_repositories ||--o{ container_remote_images : "has many"
    container_remote_images ||--o{ container_remote_blobs : "has many"
    container_remote_images ||--o{ container_remote_manifests : "has many"
    container_remote_images ||--o{ container_remote_manifest_relationships : "has many"
    container_remote_images ||--o{ container_remote_tags : "has many"
    container_remote_tags ||--|| container_remote_manifests : "has one"
    container_remote_blobs ||--|| blob_storage_attachments : "has one"
    container_remote_manifests ||--|| blob_storage_attachments : "has one"
    container_remote_manifest_relationships ||--|| container_remote_manifests : "has one (parent_id)"
    container_remote_manifest_relationships ||--|| container_remote_manifests : "has one (child_id)"

    container_remote_repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid repository_id FK "NOT NULL, UNIQUE (namespace_id, repository_id), (repository_id, namespace_id) references repositories(id, namespace_id)"
        text url "NOT NULL, limit 1024"
        text auth_url "nullable, limit 1024"
        bytea wrapped_dek "nullable, this row's data-encryption key, wrapped by the namespace key"
        uuid ns_key_id FK "nullable, (ns_key_id, namespace_id) references namespace_encryption_keys(id, namespace_id), ON DELETE RESTRICT"
        int ns_key_version "nullable, the namespace key version this row was wrapped under"
        bytea encrypted_username
        bytea encrypted_password
        smallint cache_validity_hours "NOT NULL, DEFAULT 24"
        smallint last_health_status "NOT NULL, DEFAULT 0, 0=unknown, 1=healthy, 2=unhealthy"
        timestamptz last_health_checked_at "nullable"
    }

    container_remote_images {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_remote_repository_id FK "NOT NULL, (container_remote_repository_id, namespace_id) references container_remote_repositories(id, namespace_id)"
        text name "NOT NULL, limit 255"
        timestamptz last_downloaded_at "nullable, buffered"
        timestamptz soft_deleted_at "nullable"
    }

    container_remote_blobs {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_remote_image_id FK "NOT NULL, (container_remote_image_id, namespace_id) references container_remote_images(id, namespace_id)"
        bytea digest "NOT NULL, CHECK octet_length = 32"
        text media_type "NOT NULL, limit 255"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, CHECK octet_length = 32, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        timestamptz soft_deleted_at "nullable"
    }

    container_remote_manifests {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_remote_image_id FK "NOT NULL, (container_remote_image_id, namespace_id) references container_remote_images(id, namespace_id)"
        bytea digest "NOT NULL, CHECK octet_length = 32"
        text media_type "NOT NULL, limit 255"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, CHECK octet_length = 32, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        bigint size "NOT NULL, updated as children are cached"
        timestamptz soft_deleted_at "nullable"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }

    container_remote_manifest_relationships {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_remote_image_id FK "NOT NULL, (container_remote_image_id, namespace_id) references container_remote_images(id, namespace_id)"
        uuid parent_container_remote_manifest_id FK "NOT NULL, (parent_container_remote_manifest_id, namespace_id) references container_remote_manifests(id, namespace_id)"
        uuid child_container_remote_manifest_id FK "NOT NULL, (child_container_remote_manifest_id, namespace_id) references container_remote_manifests(id, namespace_id)"
    }

    container_remote_tags {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid container_remote_image_id FK "NOT NULL, (container_remote_image_id, namespace_id) references container_remote_images(id, namespace_id)"
        uuid container_remote_manifest_id FK "NOT NULL, (container_remote_manifest_id, namespace_id) references container_remote_manifests(id, namespace_id)"
        text name "NOT NULL, limit 255"
        timestamptz upstream_checked_at "NOT NULL, DEFAULT NOW()"
        text upstream_etag "nullable, limit 255"
    }
```

- **container_remote_repositories**: Represents an external container registry. Includes URL, optional authentication URL (`auth_url`), credentials, and cache TTL (`cache_validity_hours`). Health check status is tracked for monitoring. References the parent `repositories` table via `repository_id`. Because remote repos are standalone, two virtual repositories using the same remote share one cache. Upstream credentials are stored as ciphertext alongside the wrapped data-encryption key that opens them; see [Encryption keys](#encryption-keys) for that column shape and its constraints. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_remote_images**: A cached container image within a remote repository. Mirrors `container_images`. `last_downloaded_at` records when the cached image was last pulled; maintained via buffered/async writes (same pattern as `repositories.downloads_count`) to avoid hot-row contention. Used by `keep_last_downloaded_at` lifecycle rules and cache retention evaluation ([ADR-010](010_data_retention.md)). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_remote_blobs**: A cached layer or config blob. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_remote_manifests**: A cached image manifest. The `size` column holds the byte footprint of the subtree this cache knows about: the manifest's own payload at cache time plus each child's `size` as children arrive. For image manifests the value is complete at cache time; for manifest lists and OCI indexes it converges to the full tree footprint progressively as children are fetched and may stay partial if some children are never pulled. This progressive semantic reflects lazy remote caching — eagerly fetching children purely to keep `size` complete would undermine the lazy design. `created_at` records when the manifest was first cached and powers the same publication-history and time-range provenance scans as the hosted equivalent ([`container_manifests`](#container-repositories)). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_remote_manifest_relationships**: Cached multi-architecture manifest list relationships. Same structure as the hosted equivalent. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_remote_tags**: Cached tag-to-manifest mappings. Tags are mutable pointers — on cache revalidation, a tag may be re-pointed to a new manifest. `upstream_checked_at` records when the tag was last validated against the upstream registry; compared with `cache_validity_hours` to decide if revalidation is needed. `upstream_etag` stores the ETag returned by the upstream, enabling conditional requests (`If-None-Match`) to avoid full manifest resolution when the tag still points to the same manifest. Manifests and blobs do not need freshness tracking because they are content-addressed by cryptographic hash — if the stored bytes match the digest, the content is guaranteed correct. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **blob_storage_attachments**: See [Blob storage](#blob-storage) section for details.

#### Indexes

- **`container_remote_repositories`**: unique index on `(namespace_id, repository_id)` — look up a remote repository by its parent reference; index on `(namespace_id, ns_key_id)`, which backs the [encryption key](#encryption-keys) foreign key so a key-row deletion can check its referencing rows without scanning the table.
- **`container_remote_images`**: unique index on `(namespace_id, container_remote_repository_id, name) WHERE soft_deleted_at IS NULL` — look up a cached image by name; the partial condition allows recreating an image with the same name after soft deletion.
- **`container_remote_blobs`**: unique index on `(namespace_id, container_remote_image_id, digest) WHERE soft_deleted_at IS NULL` — look up a cached blob by digest within an image; the partial condition allows re-caching the same digest after soft deletion; index on `(namespace_id, blob_storage_attachment_id)` — look up a blob by its storage attachment; index on `(namespace_id, blob_sha256)` — reverse lookup from a stored blob sha256 to every cached blob referencing it, so checksum search and vulnerability impact cover cache-side references. This index is specific to the remote cache: the hosted `container_blobs` table is content-addressed and answers the same lookup through its `(namespace_id, digest)` index, so it carries no `blob_sha256` index for this to mirror. The remote table has no standalone `(namespace_id, digest)` index to reuse for the reverse lookup either — it is pull-only, with no blob-mount path to justify one — so it indexes `blob_sha256` directly, the column its checksum-search and size-reconciliation queries join to `blob_storage_blobs(namespace_id, sha256)`.
- **`container_remote_manifests`**: unique index on `(namespace_id, container_remote_image_id, digest) WHERE soft_deleted_at IS NULL` — look up a cached manifest by digest within an image; the partial condition allows re-caching the same digest after soft deletion; index on `(namespace_id, blob_storage_attachment_id)` — look up a manifest by its storage attachment; index on `(namespace_id, blob_sha256)` — reverse lookup from the stored blob sha256 of the manifest payload to every cached manifest referencing it, so checksum search and vulnerability impact cover cache-side references. This index is specific to the remote cache; the hosted `container_manifests` table carries no equivalent index — and like the remote blob table, the remote manifest table has no standalone `(namespace_id, digest)` index to reuse, so it indexes `blob_sha256` directly for the reverse lookup; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted cached manifests ordered by deletion time, powering the artifact-granularity trash-listing query for cached container images; index on `(namespace_id, created_at DESC)` — chronological scans across the namespace, mirroring the hosted [`container_manifests`](#container-repositories) index to cover cache-side publication history and provenance. Unconditional (no `soft_deleted_at` predicate) for the same audit-trail reason as the hosted index.
- **`container_remote_manifest_relationships`**: unique index on `(namespace_id, parent_container_remote_manifest_id, child_container_remote_manifest_id)` — prevent duplicate parent-child relationships; index on `(namespace_id, child_container_remote_manifest_id)` — find all parents of a given child manifest. This twin stays on the two-column form while the hosted index widens, because the table has no writer: a lazily cached index records no child links, so every read answers empty until the cache-side relationship population lands ([artifact-registry#264](https://gitlab.com/gitlab-org/ops/artifact-registry/-/work_items/264)); index on `(namespace_id, container_remote_image_id)` — find all manifest relationships for a given image.
- **`container_remote_tags`**: unique index on `(namespace_id, container_remote_image_id, name)` — look up a tag by name within an image; index on `(namespace_id, container_remote_manifest_id)` — find all tags pointing to a given manifest. This twin stays on the two-column form while the hosted index widens, and not because the read is cheaper: it measures 110 to 144 ms against the same 100 ms budget with the cached names in arbitrary order. No write path caps this table, so the cached row count has no ceiling an index could be sized against, and the remedy is the fill-side cap question ([artifact-registry#669](https://gitlab.com/gitlab-org/ops/artifact-registry/-/work_items/669)).

#### Query examples

- Create a remote repository

  ```sql
  -- Resolve the default repository collection for the namespace
  SELECT id FROM repository_collections WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND is_default = true;
  -- Create the parent repository
  INSERT INTO repositories (namespace_id, name, format, kind, visibility)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', 'docker-hub', 0, 2, 1)
  RETURNING id;
  -- Link the repository to the repository collection
  INSERT INTO repository_collection_repositories (namespace_id, repository_collection_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', <repository_collection_id>, <returned_id>);
  -- Then create the format-specific record
  INSERT INTO container_remote_repositories (namespace_id, repository_id, url, wrapped_dek, ns_key_id, ns_key_version, encrypted_username, encrypted_password)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', <returned_id>, 'https://registry.hub.docker.com', $1, $2, $3, $4, $5);
  ```

- Check if a cached manifest is fresh

  ```sql
  SELECT crm.digest
  FROM container_remote_manifests crm
  JOIN container_remote_tags crt
    ON crt.container_remote_manifest_id = crm.id AND crt.namespace_id = crm.namespace_id
  JOIN container_remote_images cri
    ON crt.container_remote_image_id = cri.id AND crt.namespace_id = cri.namespace_id
  WHERE cri.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND cri.container_remote_repository_id = '019a1b2c-0789-7abc-8def-000000000789'
    AND cri.name = 'library/nginx'
    AND crt.name = 'latest'
    AND cri.soft_deleted_at IS NULL AND crm.soft_deleted_at IS NULL;
  ```

- Pull a cached blob by digest (read-path shortcut to blob storage)

  ```sql
  SELECT bsb.object_storage_key, bsb.size
  FROM container_remote_blobs crb
  JOIN blob_storage_blobs bsb
    ON bsb.namespace_id = crb.namespace_id AND bsb.sha256 = crb.blob_sha256
  WHERE crb.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND crb.container_remote_image_id = '019a1b2c-0456-7abc-8def-000000000456'
    AND crb.digest = 'sha256:abcd1234...'::bytea
    AND crb.soft_deleted_at IS NULL;
  ```

### Virtual Container Repositories

```mermaid
erDiagram
    repositories ||--|| container_virtual_repositories : "has one"
    container_virtual_repositories ||--o{ container_virtual_repository_upstreams : "has many"
    container_virtual_repository_upstreams ||--|| repositories : "references upstream"
    container_virtual_repository_upstreams ||--o{ container_virtual_upstream_rules : "has many"

    container_virtual_repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id) ON DELETE NO ACTION"
        uuid repository_id FK "NOT NULL, UNIQUE (namespace_id, repository_id), (repository_id, namespace_id) references repositories(id, namespace_id) ON DELETE CASCADE"
    }

    container_virtual_repository_upstreams {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id) ON DELETE NO ACTION"
        uuid container_virtual_repository_id FK "NOT NULL, (container_virtual_repository_id, namespace_id) references container_virtual_repositories(id, namespace_id) ON DELETE CASCADE"
        uuid upstream_repository_id FK "NOT NULL, (upstream_repository_id, namespace_id) references repositories(id, namespace_id) ON DELETE NO ACTION"
        int position "NOT NULL, CHECK position >= 1"
    }

    container_virtual_upstream_rules {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id) ON DELETE NO ACTION"
        uuid container_virtual_repository_upstream_id FK "NOT NULL, (container_virtual_repository_upstream_id, namespace_id) references container_virtual_repository_upstreams(id, namespace_id) ON DELETE CASCADE"
        smallint rule_type "NOT NULL, 0=allow, 1=deny, CHECK rule_type IN (0, 1)"
        text pattern "NOT NULL, CHECK char_length(pattern) <= 255"
        smallint target_field "NOT NULL, 0=image, 1=tag, CHECK target_field IN (0, 1)"
    }
```

- **container_virtual_repositories**: The virtual repository for container images. References the parent `repositories` table via `repository_id` for name, visibility, and cross-format queries. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_virtual_repository_upstreams**: The table that joins virtual repositories and their upstreams. Each virtual repository has an ordered list of upstreams. Each entry references an upstream repository via `upstream_repository_id`, which points to `repositories(id, namespace_id)`. The composite FK `(namespace_id, upstream_repository_id)` enforces that upstreams are within the same namespace — consistent with the registry being scoped to namespaces ([ADR-001](001_organizations_as_anchor_point.md)). `position` is 1-based and contiguous: `CHECK position >= 1` sets the floor, and the management surface renumbers the list inside the transaction that changes it, so the values carry no gaps. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **container_virtual_upstream_rules**: Defines allow/deny filter rules for an upstream. Each rule specifies a wildcard pattern and target field to control which artifacts are included or excluded when resolving through this upstream. Patterns are wildcards only for the MVP; regex support is deferred until customer feedback justifies it ([discussion](https://gitlab.com/gitlab-org/gitlab/-/work_items/597754#note_3291871207)). Rules stay per-upstream-reference (not per-remote-repo), matching the JFrog model where include/exclude patterns are set per virtual-upstream association. The database enforces the two enumerations and the pattern length: `CHECK rule_type IN (0, 1)`, `CHECK target_field IN (0, 1)`, and `CHECK char_length(pattern) <= 255`. These are boundary rejections, so an out-of-range discriminator is refused at write time instead of being left for the read path to cope with. Partitioned by `HASH(namespace_id)` with 64 partitions.

The foreign keys in these three tables carry these referential actions:

- `container_virtual_repositories`, FK `(repository_id, namespace_id)` referencing `repositories`: `ON DELETE CASCADE`, the action [the general rule for format child tables](#repositories) already gives it.
- `container_virtual_repositories`, FK `namespace_id` referencing `namespaces`: `NO ACTION`.
- `container_virtual_repository_upstreams`, FK `namespace_id` referencing `namespaces`: `NO ACTION`.
- `container_virtual_repository_upstreams`, FK `(container_virtual_repository_id, namespace_id)` referencing `container_virtual_repositories`: `ON DELETE CASCADE`.
- `container_virtual_repository_upstreams`, FK `(upstream_repository_id, namespace_id)` referencing `repositories`: `NO ACTION`.
- `container_virtual_upstream_rules`, FK `namespace_id` referencing `namespaces`: `NO ACTION`.
- `container_virtual_upstream_rules`, FK `(container_virtual_repository_upstream_id, namespace_id)` referencing `container_virtual_repository_upstreams`: `ON DELETE CASCADE`.

The two foreign keys on `container_virtual_repository_upstreams` take opposite actions, and the difference is deliberate. `container_virtual_repository_id` is the parent-to-child link, so deleting a virtual repository takes its upstream associations with it. `upstream_repository_id` is a sibling reference, so deleting a repository that is still listed as an upstream is refused: cascading there would shrink every virtual repository that listed it, possibly to an empty list, and no operator would see it happen. The key refuses that shrink without signaling the refusal, which [the `repositories` delete path](#repositories) covers. Removing an upstream has to be a deliberate management action, which is also why the reverse-lookup index below exists.

#### Indexes

- **`container_virtual_repositories`**: unique index on `(namespace_id, repository_id)` — look up a virtual repository by its parent reference.
- **`container_virtual_repository_upstreams`**: unique constraint on `(namespace_id, container_virtual_repository_id, position)`, `DEFERRABLE INITIALLY DEFERRED` — retrieve ordered upstreams for a virtual repository; deferrable to allow reordering within a transaction. Unique index on `(namespace_id, container_virtual_repository_id, upstream_repository_id)` — prevent the same upstream from being added to a virtual repository twice. Index on `(namespace_id, upstream_repository_id)` — find every virtual repository that lists a given repository as an upstream, which is what the `NO ACTION` guard above and the association surface read. Neither unique entry has this as a usable prefix, and PostgreSQL does not index foreign-key columns automatically.
- **`container_virtual_upstream_rules`**: index on `(namespace_id, container_virtual_repository_upstream_id)` — fetch all rules for a given upstream.

The ordered-upstream entry is a unique **constraint**, not a unique index. Deferral is a property of a constraint, so it is added with `ALTER TABLE ... ADD CONSTRAINT ... UNIQUE (...) DEFERRABLE INITIALLY DEFERRED`; `CREATE UNIQUE INDEX ... DEFERRABLE` is a syntax error in PostgreSQL. The npm virtual table already carries one, added the same way — `unique_nvru_ns_id_repository_id_position` on `npm_virtual_repository_upstreams` — so the container migration copies a sibling rather than establishing the pattern. It does not copy that table's `position` floor, which is `0` there and `1` here. A deferrable unique constraint also cannot arbitrate `ON CONFLICT`, so a `position` write is an `UPDATE` followed by an `INSERT`, never an upsert on this key.

#### Query examples

- Create a virtual repository

  ```sql
  -- First create the parent repository
  INSERT INTO repositories (namespace_id, name, format, kind, visibility)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', 'my-virtual-repo', 0, 1, 1)
  RETURNING id;
  -- Link the repository to a repository collection
  INSERT INTO repository_collection_repositories (namespace_id, repository_collection_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0456-7abc-8def-000000000456', <returned_id>);
  -- Then create the format-specific record
  INSERT INTO container_virtual_repositories (namespace_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', <returned_id>);
  ```

- Associate a virtual repository with an upstream

  ```sql
  INSERT INTO container_virtual_repository_upstreams (namespace_id, container_virtual_repository_id, upstream_repository_id, position)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0123-7abc-8def-000000000123', '019a1b2c-0789-7abc-8def-000000000789', 1);
  ```

### Maven Repositories

Maven packages represent a collection of files (`.jar`, `.pom`, `maven-metadata.xml`). Downloading a single Maven package can thus represent between 4 and 15 API requests.

```mermaid
erDiagram
    repositories ||--|| maven_repositories : "has one"
    maven_repositories ||--o{ maven_packages : "has many"
    maven_packages ||--o{ maven_versions : "has many"
    maven_packages ||--o{ maven_files : "has many"
    maven_versions ||--o{ maven_files : "has many"
    maven_files ||--|| blob_storage_attachments : "has one"

    maven_repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid repository_id FK "NOT NULL, UNIQUE (namespace_id, repository_id), (repository_id, namespace_id) references repositories(id, namespace_id)"
    }

    maven_packages {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid maven_repository_id FK "NOT NULL, (maven_repository_id, namespace_id) references maven_repositories(id, namespace_id)"
        text group_id "NOT NULL, limit 255"
        text artifact_id "NOT NULL, limit 255"
        timestamptz last_downloaded_at "nullable, buffered"
        timestamptz soft_deleted_at "nullable"
    }

    maven_versions {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid maven_package_id FK "NOT NULL, (maven_package_id, namespace_id) references maven_packages(id, namespace_id)"
        text version "NOT NULL, limit 255"
        bigint size_bytes "NOT NULL, DEFAULT 0, buffered counter"
        timestamptz last_downloaded_at "nullable, buffered"
        text gitlab_user_id "nullable, opaque string, limit 255"
        text gitlab_project_id "nullable, opaque string, limit 255"
        bytea gitlab_git_commit_sha "nullable"
        timestamptz soft_deleted_at "nullable"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }

    maven_files {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid maven_package_id FK "NOT NULL, (maven_package_id, namespace_id) references maven_packages(id, namespace_id)"
        uuid maven_version_id FK "nullable, (maven_version_id, namespace_id) references maven_versions(id, namespace_id)"
        text file_name "NOT NULL, limit 255"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        bytea sha1 "NOT NULL"
        bytea md5 "nullable"
        bytea sha512 "NOT NULL"
        timestamptz soft_deleted_at "nullable"
    }
```

- **maven_repositories**: The container of multiple packages. Each repository can host multiple packages identified by group ID and artifact ID. References the parent `repositories` table via `repository_id` for name, visibility, and cross-format queries. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **maven_packages**: Represents a Maven package identified by [its group ID and artifact ID](https://maven.apache.org/pom.html#Maven_Coordinates) (for example, `com.example:myapp`). `last_downloaded_at` records when any file of the package was last downloaded; maintained via [buffered/async writes](#buffered-and-asynchronous-writes). `NULL` means the package has never been downloaded and is treated as the oldest possible download time for `keep_last_downloaded_at` lifecycle rule evaluation (i.e., eligible for deletion under download-based retention). Used by `keep_last_downloaded_at` lifecycle rules to evaluate download-based retention ([ADR-010](010_data_retention.md)). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **maven_versions**: Stores individual [versions](https://maven.apache.org/pom.html#Maven_Coordinates) of a Maven package (for example, `1.0.0`, `2.1.3-SNAPSHOT`). `last_downloaded_at` records when any file of the version was last downloaded; maintained via [buffered/async writes](#buffered-and-asynchronous-writes). Used by `keep_last_downloaded_at` lifecycle rules. `gitlab_user_id`, `gitlab_project_id`, and `gitlab_git_commit_sha` record which GitLab user published this version and the CI context (project, commit) behind the publish, with the same shapes and rationale as the equivalent columns on [`container_manifests`](#container-repositories). `created_at` records when the version was first published and powers the same publication-history and time-range provenance scans as [`container_manifests`](#container-repositories). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **maven_files**: Represents individual files associated with a Maven package. Files can be either version-specific (JAR, POM, sources, Javadoc, checksums) with `maven_version_id` set, or package-level (such as `maven-metadata.xml` and its checksums) with `maven_version_id` as NULL. The `maven_package_id` is always set, providing a direct path from package to all its files. It can also be auxiliary files used by the registry to improve performance bottlenecks. The `sha1` and `md5` columns store the [checksums required by the Maven protocol](https://maven.apache.org/resolver/about-checksums.html) for integrity verification. Maven clients expect `.sha1` and `.md5` sidecar files alongside every artifact. These columns are on `maven_files` rather than `blob_storage_blobs` because they are a Maven protocol concern, not a universal blob property — other formats (OCI containers) use SHA256 exclusively. Keeping them here preserves `blob_storage_blobs` as a format-agnostic table with no format-specific columns or indexes. `sha1` is `NOT NULL` because the Maven protocol requires it. `md5` is nullable because Maven 3.9+ [deprecated MD5 checksums](https://maven.apache.org/resolver/about-checksums.html). `sha512` is `NOT NULL` because the Maven protocol exposes a `.sha512` sidecar that the registry must be able to serve, and the value is always computable during upload as the bytes flow through the handler before being persisted. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **blob_storage_attachments**: See [Blob storage](#blob-storage) section for details.

We are not storing the package name, in this case, the group ID and artifact ID, and the version in the same table. The reason is that the UI will access this data by package name. Imagine a tree-like UI where the package name is a folder and opening that one, you have one subfolder for each version. This first request will need to list the folders, package names. Opening a folder will trigger a request to list all subfolders, package versions. Thus, we have two dedicated tables (`maven_packages` and `maven_versions`) to ease this access pattern.

#### Indexes

- **`maven_repositories`**: unique index on `(namespace_id, repository_id)` — look up a Maven repository by its parent repository reference.
- **`maven_packages`**: unique index on `(namespace_id, maven_repository_id, group_id, artifact_id) WHERE soft_deleted_at IS NULL` — look up a package by its Maven coordinates within a repository. The partial condition allows recreating a package with the same coordinates after soft deletion; index on `(namespace_id, maven_repository_id, last_downloaded_at NULLS FIRST) WHERE soft_deleted_at IS NULL` — support `keep_last_downloaded_at` lifecycle rule evaluation; returns only aged-out packages via a bounded range scan rather than scanning every package in the repository and filtering row-by-row. `NULLS FIRST` groups never-downloaded packages with the oldest rows so both are returned by the same range scan; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted packages ordered by deletion time, powering the reaper's package-level scan. The `maven_versions` index of this shape cannot serve it: a package delete marks the package row and writes no child row, so the versions beneath a tombstoned package carry no `soft_deleted_at` of their own, and neither a version-level scan nor a repository walk reaches that package while its repository is still live. Without this index the reaper would have to sequential-scan `maven_packages` to find it.
- **`maven_versions`**: unique index on `(namespace_id, maven_package_id, version) WHERE soft_deleted_at IS NULL` — look up a specific version within a package. The partial condition allows recreating a version with the same identifier after soft deletion; index on `(namespace_id, maven_package_id, last_downloaded_at NULLS FIRST) WHERE soft_deleted_at IS NULL` — support `keep_last_downloaded_at` lifecycle rule evaluation scoped to a package's versions, using the same range-scan strategy as `maven_packages`; index on `(namespace_id, maven_package_id, size_bytes DESC) WHERE soft_deleted_at IS NULL` — sort a package's versions by size for the version-list display, mirroring the landing-page repository sort; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted versions ordered by deletion time, powering the artifact-granularity trash-listing query for Maven artifacts; index on `(namespace_id, created_at DESC)` — chronological scans across the namespace, powering publication-history pagination and time-range artifact-provenance queries. Unconditional so soft-deleted publish events still appear in the audit trail.
- **`maven_files`**: unique index on `(namespace_id, maven_version_id, file_name) WHERE soft_deleted_at IS NULL AND maven_version_id IS NOT NULL` — a version-specific file name must be unique within a version. The partial conditions exclude soft-deleted rows and package-level files; unique index on `(namespace_id, maven_package_id, file_name) WHERE soft_deleted_at IS NULL AND maven_version_id IS NULL` — a package-level file name (such as `maven-metadata.xml`) must be unique within a package; index on `(namespace_id, blob_storage_attachment_id)` — look up a file by its storage attachment; index on `(namespace_id, blob_sha256)` — reverse lookup from a stored blob sha256 to every Maven file referencing it, powering cross-format checksum search. The existing parent-keyed indexes are version- or package-keyed and cannot satisfy a digest-keyed scan directly; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL AND maven_version_id IS NULL AND file_name = 'maven-metadata.xml'` — list a namespace's package-level `maven-metadata.xml` tombstones oldest-first for the metadata purge's discovery scan. The metadata-only predicate keeps the index to the package-level metadata files the purge reads, and `DESC` lets an oldest-first reader scan the index backward at the same cost a newest-first reader scans it forward. A bare tombstone index on the same key would serve the scan but carry every file's tombstone, so the three-conjunct predicate is what keeps the index to the rows the purge reads; index on `(namespace_id, maven_package_id, blob_sha256)` — serve the `maven_package_id` foreign-key check and the repository-level size walk's join, which reads `blob_sha256` from the index. Non-partial, because the check carries no predicate and the walk reaches soft-deleted and version-routed rows alike.

#### Query examples

- Get package version for a given repository id and package name.

  ```sql
  SELECT mv.*
  FROM maven_versions mv
  JOIN maven_packages mp
    ON mv.maven_package_id = mp.id AND mv.namespace_id = mp.namespace_id
  WHERE mp.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND mp.maven_repository_id = '019a1b2c-0123-7abc-8def-000000000123' AND mp.group_id = 'com.example' AND mp.artifact_id = 'myapp'
    AND mv.version = '1.0.0'
    AND mp.soft_deleted_at IS NULL AND mv.soft_deleted_at IS NULL;
  ```

- Get a file given a version id and filename.

  ```sql
  SELECT mf.*
  FROM maven_files mf
  WHERE mf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND mf.maven_version_id = '019a1b2c-0456-7abc-8def-000000000456' AND mf.file_name = 'myapp-1.0.0.jar'
    AND mf.soft_deleted_at IS NULL;
  ```

- Get package-level files (for example, `maven-metadata.xml`) for a given package.

  ```sql
  SELECT mf.*
  FROM maven_files mf
  WHERE mf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND mf.maven_package_id = '019a1b2c-0123-7abc-8def-000000000123' AND mf.maven_version_id IS NULL
    AND mf.soft_deleted_at IS NULL;
  ```

- Trash listing: list every soft-deleted Maven version in a namespace, most-recently-deleted first (uses the partial index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL`). The compliance use case is namespace-wide ("what is in the trash right now?"); a parent-scoped view ("trashed versions of this package") would benefit from a separate `(namespace_id, maven_package_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` index, which can be added later if that UI is built. The same pattern applies to [`npm_versions`](#npm-repositories), [`container_manifests`](#container-repositories), and their remote equivalents.

  ```sql
  SELECT mv.id, mv.maven_package_id, mv.version, mv.soft_deleted_at
  FROM maven_versions mv
  WHERE mv.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND mv.soft_deleted_at IS NOT NULL
  ORDER BY mv.soft_deleted_at DESC
  LIMIT 50;
  ```

- Metadata purge discovery: list a namespace's package-level `maven-metadata.xml` tombstones oldest-first for the metadata purge's background scan (uses the partial index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL AND maven_version_id IS NULL AND file_name = 'maven-metadata.xml'`). The purge is a background job that reads one bounded page per pass. The index is stored newest-first, so the oldest-first reader scans it backward at the same cost a newest-first reader scans it forward.

  ```sql
  SELECT mf.id, mf.maven_package_id, mf.file_name, mf.soft_deleted_at
  FROM maven_files mf
  WHERE mf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND mf.soft_deleted_at IS NOT NULL AND mf.maven_version_id IS NULL AND mf.file_name = 'maven-metadata.xml'
  ORDER BY mf.soft_deleted_at ASC
  LIMIT 50;
  ```

### Maven Remote Repositories

```mermaid
erDiagram
    repositories ||--|| maven_remote_repositories : "has one"
    maven_remote_repositories ||--o{ maven_remote_packages : "has many"
    maven_remote_packages ||--o{ maven_remote_versions : "has many"
    maven_remote_packages ||--o{ maven_remote_files : "has many"
    maven_remote_versions ||--o{ maven_remote_files : "has many"
    maven_remote_files ||--|| blob_storage_attachments : "has one"

    maven_remote_repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid repository_id FK "NOT NULL, UNIQUE (namespace_id, repository_id), (repository_id, namespace_id) references repositories(id, namespace_id)"
        text url "NOT NULL, limit 1024"
        bytea wrapped_dek "nullable, this row's data-encryption key, wrapped by the namespace key"
        uuid ns_key_id FK "nullable, (ns_key_id, namespace_id) references namespace_encryption_keys(id, namespace_id), ON DELETE RESTRICT"
        int ns_key_version "nullable, the namespace key version this row was wrapped under"
        bytea encrypted_username
        bytea encrypted_password
        smallint cache_validity_hours "NOT NULL, DEFAULT 24"
        smallint metadata_cache_validity_hours "NOT NULL, DEFAULT 24"
        smallint last_health_status "NOT NULL, DEFAULT 0, 0=unknown, 1=healthy, 2=unhealthy"
        timestamptz last_health_checked_at "nullable"
    }

    maven_remote_packages {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid maven_remote_repository_id FK "NOT NULL, (maven_remote_repository_id, namespace_id) references maven_remote_repositories(id, namespace_id)"
        text group_id "NOT NULL, limit 255"
        text artifact_id "NOT NULL, limit 255"
        timestamptz last_downloaded_at "nullable, buffered"
        timestamptz soft_deleted_at "nullable"
    }

    maven_remote_versions {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid maven_remote_package_id FK "NOT NULL, (maven_remote_package_id, namespace_id) references maven_remote_packages(id, namespace_id)"
        text version "NOT NULL, limit 255"
        bigint size_bytes "NOT NULL, DEFAULT 0, buffered counter"
        timestamptz last_downloaded_at "nullable, buffered"
        timestamptz soft_deleted_at "nullable"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }

    maven_remote_files {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid maven_remote_package_id FK "NOT NULL, (maven_remote_package_id, namespace_id) references maven_remote_packages(id, namespace_id)"
        uuid maven_remote_version_id FK "nullable, (maven_remote_version_id, namespace_id) references maven_remote_versions(id, namespace_id)"
        text file_name "NOT NULL, limit 255"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        bytea sha1 "NOT NULL"
        bytea md5 "nullable"
        bytea sha512 "NOT NULL"
        timestamptz upstream_checked_at "NOT NULL, DEFAULT NOW()"
        text upstream_etag "nullable, limit 255"
        timestamptz soft_deleted_at "nullable"
    }
```

- **maven_remote_repositories**: Represents an external Maven repository. Includes URL, credentials, artifact cache TTL (`cache_validity_hours`), and a separate TTL for metadata responses such as `maven-metadata.xml` (`metadata_cache_validity_hours`). Health check status is tracked for monitoring. References the parent `repositories` table via `repository_id`. Upstream credentials are stored as ciphertext alongside the wrapped data-encryption key that opens them; see [Encryption keys](#encryption-keys) for that column shape and its constraints. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **maven_remote_packages**: A cached Maven package identified by group ID and artifact ID. Mirrors `maven_packages`. `last_downloaded_at` records when any cached file of the package was last downloaded; maintained via buffered/async writes to avoid hot-row contention. Used by `keep_last_downloaded_at` lifecycle rules and cache retention evaluation. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **maven_remote_versions**: A cached version of a Maven package. Mirrors `maven_versions`. `last_downloaded_at` records when any cached file of the version was last downloaded; maintained via buffered/async writes to avoid hot-row contention. Used by `keep_last_downloaded_at` lifecycle rules and cache retention evaluation. `created_at` records when the version was first cached and powers cache-side publication-history and provenance scans, mirroring [`maven_versions`](#maven-repositories). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **maven_remote_files**: A cached file (JAR, POM, checksums, `maven-metadata.xml`). The nullable `maven_remote_version_id` preserves the same pattern as hosted: version-specific files vs. package-level files (like `maven-metadata.xml`). `sha1` and `md5` are retained because the Maven protocol requires serving these checksums regardless of whether the content is hosted or cached. `sha512` is added on parity grounds so it mirrors the hosted `maven_files` column shape, letting the Maven Virtual spec (S30) serve `.sha512` sidecars from either backend with one query path. The value is computed from the cached bytes during the proxy-write step alongside the other checksums, so `NOT NULL` is achievable from day one. `upstream_checked_at` records when the file was last validated against the upstream repository; compared with `cache_validity_hours` for artifact files or `metadata_cache_validity_hours` for metadata files (e.g. `maven-metadata.xml`) to decide if revalidation is needed. `upstream_etag` stores the ETag returned by the upstream, enabling conditional requests (`If-None-Match`) to avoid re-downloading unchanged files. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **blob_storage_attachments**: See [Blob storage](#blob-storage) section for details.

#### Indexes

- **`maven_remote_repositories`**: unique index on `(namespace_id, repository_id)` — look up a remote repository by its parent reference; index on `(namespace_id, ns_key_id)`, which backs the [encryption key](#encryption-keys) foreign key so a key-row deletion can check its referencing rows without scanning the table.
- **`maven_remote_packages`**: unique index on `(namespace_id, maven_remote_repository_id, group_id, artifact_id) WHERE soft_deleted_at IS NULL` — look up a cached package by its Maven coordinates. The partial condition allows recreating a package with the same coordinates after soft deletion.
- **`maven_remote_versions`**: unique index on `(namespace_id, maven_remote_package_id, version) WHERE soft_deleted_at IS NULL` — look up a cached version within a package. The partial condition allows recreating a version with the same identifier after soft deletion; index on `(namespace_id, maven_remote_package_id, size_bytes DESC) WHERE soft_deleted_at IS NULL` — sort a cached package's versions by size for the version-list display; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted cached versions ordered by deletion time, powering the artifact-granularity trash-listing query for cached Maven artifacts; index on `(namespace_id, created_at DESC)` — chronological scans across the namespace, mirroring the local [`maven_versions`](#maven-repositories) index to cover cache-side publication history and provenance. Unconditional (no `soft_deleted_at` predicate) for the same audit-trail reason as the local index.
- **`maven_remote_files`**: unique index on `(namespace_id, maven_remote_version_id, file_name) WHERE soft_deleted_at IS NULL AND maven_remote_version_id IS NOT NULL` — a version-specific file name must be unique within a version; unique index on `(namespace_id, maven_remote_package_id, file_name) WHERE soft_deleted_at IS NULL AND maven_remote_version_id IS NULL` — a package-level file name must be unique within a package; index on `(namespace_id, blob_storage_attachment_id)` — look up a file by its storage attachment; index on `(namespace_id, blob_sha256)` — reverse lookup from a stored blob sha256 to every cached Maven file referencing it, mirroring the local [`maven_files`](#maven-repositories) index so checksum search covers cache-side references too.

#### Query examples

- Create a remote repository

  ```sql
  -- First create the parent repository
  INSERT INTO repositories (namespace_id, name, format, kind, visibility)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', 'central', 1, 2, 0)
  RETURNING id;
  -- Link the repository to a repository collection
  INSERT INTO repository_collection_repositories (namespace_id, repository_collection_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0456-7abc-8def-000000000456', <returned_id>);
  -- Then create the format-specific record
  INSERT INTO maven_remote_repositories (namespace_id, repository_id, url, wrapped_dek, ns_key_id, ns_key_version, encrypted_username, encrypted_password)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', <returned_id>, 'https://repo.maven.apache.org/maven2', $1, $2, $3, $4, $5);
  ```

- Look up a cached Maven file by coordinates

  ```sql
  SELECT mrf.*, bsb.object_storage_key
  FROM maven_remote_files mrf
  JOIN maven_remote_versions mrv
    ON mrf.maven_remote_version_id = mrv.id AND mrf.namespace_id = mrv.namespace_id
  JOIN maven_remote_packages mrp
    ON mrv.maven_remote_package_id = mrp.id AND mrv.namespace_id = mrp.namespace_id
  JOIN blob_storage_blobs bsb
    ON bsb.namespace_id = mrf.namespace_id AND bsb.sha256 = mrf.blob_sha256
  WHERE mrp.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND mrp.maven_remote_repository_id = '019a1b2c-0789-7abc-8def-000000000789'
    AND mrp.group_id = 'com.example'
    AND mrp.artifact_id = 'myapp'
    AND mrv.version = '1.0.0'
    AND mrf.file_name = 'myapp-1.0.0.jar'
    AND mrp.soft_deleted_at IS NULL AND mrv.soft_deleted_at IS NULL AND mrf.soft_deleted_at IS NULL;
  ```

- Look up cached `maven-metadata.xml` for a package

  ```sql
  SELECT mrf.*
  FROM maven_remote_files mrf
  JOIN maven_remote_packages mrp
    ON mrf.maven_remote_package_id = mrp.id AND mrf.namespace_id = mrp.namespace_id
  WHERE mrp.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND mrp.maven_remote_repository_id = '019a1b2c-0789-7abc-8def-000000000789'
    AND mrp.group_id = 'com.example'
    AND mrp.artifact_id = 'myapp'
    AND mrf.maven_remote_version_id IS NULL
    AND mrf.file_name = 'maven-metadata.xml'
    AND mrp.soft_deleted_at IS NULL AND mrf.soft_deleted_at IS NULL;
  ```

### Maven Virtual Repositories

```mermaid
erDiagram
    repositories ||--|| maven_virtual_repositories : "has one"
    maven_virtual_repositories ||--o{ maven_virtual_repository_upstreams : "has many"
    maven_virtual_repository_upstreams ||--|| repositories : "references upstream"
    maven_virtual_repository_upstreams ||--o{ maven_virtual_upstream_rules : "has many"

    maven_virtual_repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid repository_id FK "NOT NULL, UNIQUE (namespace_id, repository_id), (repository_id, namespace_id) references repositories(id, namespace_id)"
    }

    maven_virtual_repository_upstreams {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid maven_virtual_repository_id FK "NOT NULL, (maven_virtual_repository_id, namespace_id) references maven_virtual_repositories(id, namespace_id)"
        uuid upstream_repository_id FK "NOT NULL, (upstream_repository_id, namespace_id) references repositories(id, namespace_id) ON DELETE NO ACTION"
        int position "NOT NULL"
    }

    maven_virtual_upstream_rules {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid maven_virtual_repository_upstream_id FK "NOT NULL, (maven_virtual_repository_upstream_id, namespace_id) references maven_virtual_repository_upstreams(id, namespace_id)"
        smallint rule_type "NOT NULL, 0=allow, 1=deny"
        text pattern "NOT NULL, limit 255"
        smallint target_field "NOT NULL, 0=group_id, 1=artifact_id, 2=version"
    }
```

- **maven_virtual_repositories**: The virtual repository for Maven packages. References the parent `repositories` table via `repository_id` for name, visibility, and cross-format queries. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **maven_virtual_repository_upstreams**: The table that joins virtual repositories and their upstreams. Each virtual repository has an ordered list of upstreams. Each entry references an upstream repository via `upstream_repository_id`, which points to `repositories(id, namespace_id)`. The composite FK `(namespace_id, upstream_repository_id)` enforces that upstreams are within the same namespace — consistent with the registry being scoped to namespaces ([ADR-001](001_organizations_as_anchor_point.md)). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **maven_virtual_upstream_rules**: Defines allow/deny filter rules for an upstream. Each rule specifies a wildcard pattern and target field to control which artifacts are included or excluded when resolving through this upstream. Patterns are wildcards only for the MVP; regex support is deferred until customer feedback justifies it ([discussion](https://gitlab.com/gitlab-org/gitlab/-/work_items/597754#note_3291871207)). Partitioned by `HASH(namespace_id)` with 64 partitions.

#### Indexes

- **`maven_virtual_repositories`**: unique index on `(namespace_id, repository_id)` — look up a virtual repository by its parent reference.
- **`maven_virtual_repository_upstreams`**: unique constraint on `(namespace_id, maven_virtual_repository_id, position)`, `DEFERRABLE INITIALLY DEFERRED` — retrieve ordered upstreams for a virtual repository; deferrable to allow reordering within a transaction. Unique index on `(namespace_id, maven_virtual_repository_id, upstream_repository_id)` — prevent the same upstream from being added to a virtual repository twice. Index on `(namespace_id, upstream_repository_id)` — find every virtual repository that lists a given repository as an upstream, which is what the `NO ACTION` guard reads. Neither unique entry has this as a usable prefix, and PostgreSQL does not index foreign-key columns automatically.
- **`maven_virtual_upstream_rules`**: index on `(namespace_id, maven_virtual_repository_upstream_id)` — fetch all rules for a given upstream.

#### Query examples

- Create a virtual repository

  ```sql
  -- First create the parent repository
  INSERT INTO repositories (namespace_id, name, format, kind, visibility)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', 'my-virtual-repo', 1, 1, 1)
  RETURNING id;
  -- Link the repository to a repository collection
  INSERT INTO repository_collection_repositories (namespace_id, repository_collection_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0456-7abc-8def-000000000456', <returned_id>);
  -- Then create the format-specific record
  INSERT INTO maven_virtual_repositories (namespace_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', <returned_id>);
  ```

- Associate a virtual repository with an upstream

  ```sql
  INSERT INTO maven_virtual_repository_upstreams (namespace_id, maven_virtual_repository_id, upstream_repository_id, position)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0123-7abc-8def-000000000123', '019a1b2c-0789-7abc-8def-000000000789', 1);
  ```

### NPM Repositories

Node packages are basically `.tar.gz` files where each version is a single archive. However, node clients have a richer feature set, for example, the use of distribution tags that we need to handle.

```mermaid
erDiagram
    repositories ||--|| npm_repositories : "has one"
    npm_repositories ||--o{ npm_packages : "has many"
    npm_packages ||--o{ npm_versions : "has many"
    npm_packages ||--o{ npm_tags : "has many"
    npm_versions ||--o{ npm_files : "has many"
    npm_tags ||--|| npm_versions : "has one"
    npm_packages ||--o{ npm_metadata_files : "has many"
    npm_files ||--|| blob_storage_attachments : "has one"
    npm_metadata_files ||--|| blob_storage_attachments : "has one"

    npm_repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid repository_id FK "NOT NULL, UNIQUE (namespace_id, repository_id), (repository_id, namespace_id) references repositories(id, namespace_id)"
    }

    npm_packages {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_repository_id FK "NOT NULL, (npm_repository_id, namespace_id) references npm_repositories(id, namespace_id)"
        text name "NOT NULL, limit 255"
        text scope "nullable, limit 255"
        integer versions_count "NOT NULL, DEFAULT 0, buffered counter"
        integer tags_count "NOT NULL, DEFAULT 0, buffered counter"
        timestamptz last_downloaded_at "nullable, buffered"
        timestamptz soft_deleted_at "nullable"
    }

    npm_versions {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_package_id FK "NOT NULL, (npm_package_id, namespace_id) references npm_packages(id, namespace_id)"
        text version "NOT NULL, limit 255"
        jsonb package_json "NOT NULL"
        bigint size_bytes "NOT NULL, DEFAULT 0, buffered counter"
        timestamptz last_downloaded_at "nullable, buffered"
        text gitlab_user_id "nullable, opaque string, limit 255"
        text gitlab_project_id "nullable, opaque string, limit 255"
        bytea gitlab_git_commit_sha "nullable"
        timestamptz soft_deleted_at "nullable"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }

    npm_tags {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_package_id FK "NOT NULL, (npm_package_id, namespace_id) references npm_packages(id, namespace_id)"
        uuid npm_version_id FK "NOT NULL, (npm_version_id, namespace_id) references npm_versions(id, namespace_id)"
        text name "NOT NULL, limit 255"
    }

    npm_files {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_version_id FK "NOT NULL, (npm_version_id, namespace_id) references npm_versions(id, namespace_id)"
        text file_name "NOT NULL, limit 255"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        timestamptz soft_deleted_at "nullable"
    }

    npm_metadata_files {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_package_id FK "NOT NULL, (npm_package_id, namespace_id) references npm_packages(id, namespace_id)"
        smallint kind "NOT NULL, 0=full, 1=dist_tags, 2=abbreviated"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        timestamptz expires_at "NOT NULL"
    }
```

- **npm_repositories**: The container of multiple packages. Each repository can host multiple packages with optional scopes. References the parent `repositories` table via `repository_id` for name, visibility, and cross-format queries. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_packages**: Represents an npm package. The `name` column stores the full package name including scope (for example, `@myorg/mypackage` or `lodash`). `versions_count` counts the package's `npm_versions` rows including soft-deleted ones, decrementing only when garbage collection hard-deletes a row; `tags_count` counts its `npm_tags` rows (`npm_tags` has no soft-delete column, so the question does not arise). Both are buffered counters that enforce the per-package entity-count limits from [ADR-004](004_data_and_application_limits.md#entity-count-limits) (25,000 versions, 1,000 tags) and are maintained via [buffered/async writes](#buffered-and-asynchronous-writes). Including soft-deleted versions mirrors the treatment of `namespace_statistics.deduplicated_size_bytes` and closes a gaming vector: a customer who could exclude soft-deleted rows from the cap could repeatedly soft-delete and republish to stay under the 25,000-version limit indefinitely, even though every soft-deleted row still occupies storage and remains restorable. Typed `integer` (not `bigint`) because both caps sit well below the 32-bit ceiling; the unbounded counters elsewhere (`downloads_count`, `size_bytes`) need `bigint` because they grow without limit. `last_downloaded_at` records when any file of the package was last downloaded; maintained via [buffered/async writes](#buffered-and-asynchronous-writes). Used by `keep_last_downloaded_at` lifecycle rules. npm's single-version unpublish soft-deletes this row when the last active version goes, so a soft-deleted package can outlive every version beneath it; that asymmetry is why this table carries a tombstone index of its own rather than relying on the version-level one (see the index list below). [`maven_packages`](#maven-repositories) carries an index of the same shape and reaches the same state from the other direction: a Maven package delete marks the package row and leaves its versions live, so there the parent is tombstoned while the children never are. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_versions**: Stores individual versions of an npm package with embedded package.json metadata. `last_downloaded_at` records when any file of the version was last downloaded; maintained via [buffered/async writes](#buffered-and-asynchronous-writes). Used by `keep_last_downloaded_at` lifecycle rules. `gitlab_user_id`, `gitlab_project_id`, and `gitlab_git_commit_sha` record which GitLab user published this version and the CI context (project, commit) behind the publish, with the same shapes and rationale as the equivalent columns on [`container_manifests`](#container-repositories). `created_at` records when the version was first published and powers the same publication-history and time-range provenance scans as [`container_manifests`](#container-repositories). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_tags**: Provides [NPM distribution tags](https://docs.npmjs.com/cli/v11/commands/npm-dist-tag) (for example, `latest`, `next`, `beta`) that point to specific package versions. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_files**: Represents the files for an npm package version. These are mainly tarball archives. It can also be auxiliary files used by the registry to improve performance bottlenecks. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_metadata_files**: Stores pre-computed metadata files for an npm package, one per `kind`. The `kind` column distinguishes the metadata variant: `full` (0) contains the complete packument with all versions, `dist_tags` (1) contains only the distribution tags mapping, and `abbreviated` (2) is the install-only projection served when the request carries `Accept: application/vnd.npm.install-v1+json`. The appropriate file is served on the npm metadata endpoint based on the client request. Linked to `npm_packages` (not `npm_versions`) because the metadata spans all versions of a package. Metadata files are generated by a cache rebuild: a write enqueues one to run asynchronously, and a read that finds no fresh row runs the same rebuild on the request goroutine before answering. The `expires_at` column drives cache freshness: writers (publish, deprecate, unpublish, dist-tag mutations) force-expire the cache by setting `expires_at = NOW()` on every row for the affected package in the same transaction as the data write; a rebuild sets `expires_at = NOW() + npm.packument_cache_ttl` when it upserts a row with the freshly generated blob, and either the cache job or an on-read fill can be the one that runs it. Readers filter on `expires_at > NOW()` and fall through to an on-read fill on a miss, so expired rows are never served to clients; the column is the cache's freshness signal rather than a hard delete deadline. Force-expiring leaves the blob and attachment in place so any response already resolving against them completes normally until the rebuild swaps the attachment. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **blob_storage_attachments**: See [Blob storage](#blob-storage) section for details.

Similar to [Maven](#maven-repositories), package names and versions are stored in two different tables for the exact same reason.

#### Indexes

- **`npm_repositories`**: unique index on `(namespace_id, repository_id)` — look up an NPM repository by its parent repository reference.
- **`npm_packages`**: unique index on `(namespace_id, npm_repository_id, name) WHERE soft_deleted_at IS NULL` — look up a package by name within a repository. The partial condition allows recreating a package with the same name after soft deletion; index on `(namespace_id, npm_repository_id, last_downloaded_at NULLS FIRST) WHERE soft_deleted_at IS NULL` — support `keep_last_downloaded_at` lifecycle rule evaluation; returns only aged-out packages via a bounded range scan rather than scanning every package in the repository and filtering row-by-row. `NULLS FIRST` groups never-downloaded packages with the oldest rows so both are returned by the same range scan; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted packages ordered by deletion time. Unlike the version-level indexes of this shape it is not primarily a trash-listing index: a package soft-deleted when its last active version goes outlives those versions, so once they are purged neither a version-level scan nor a repository walk can reach the package row, and a reaper would otherwise have to sequential-scan the table to find it; index on `(namespace_id, npm_repository_id, name) WHERE soft_deleted_at IS NOT NULL` — sum the tombstoned rows' `versions_count` at a publish coordinate, backing the publish pre-check's version-cap enforcement across soft deletion. `versions_count` counts soft-deleted versions and decrements only at hard-delete (the anti-gaming rule above), and a whole-package unpublish carries the whole count onto a tombstoned row while the unique name index's partial condition lets a republish insert a fresh active row at zero — so the cap check must read the tombstoned rows by name or one unpublish-and-republish cycle resets the cap. The unique name index cannot serve this read: PostgreSQL uses a partial index only for a query whose predicate implies the index predicate, and this query's predicate is the complement of that index's.
- **`npm_versions`**: unique index on `(namespace_id, npm_package_id, version) WHERE soft_deleted_at IS NULL` — look up a specific version within a package. The partial condition allows recreating a version with the same identifier after soft deletion; index on `(namespace_id, npm_package_id, last_downloaded_at NULLS FIRST) WHERE soft_deleted_at IS NULL` — support `keep_last_downloaded_at` lifecycle rule evaluation scoped to a package's versions, using the same range-scan strategy as `npm_packages`; index on `(namespace_id, npm_package_id, size_bytes DESC) WHERE soft_deleted_at IS NULL` — sort a package's versions by size for the version-list display, mirroring the landing-page repository sort; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted versions ordered by deletion time, powering the artifact-granularity trash-listing query for npm artifacts; index on `(namespace_id, created_at DESC)` — chronological scans across the namespace, powering publication-history pagination and time-range artifact-provenance queries. Unconditional so soft-deleted publish events still appear in the audit trail.
- **`npm_tags`**: unique index on `(namespace_id, npm_package_id, name)` — look up a distribution tag by name within a package; index on `(namespace_id, npm_version_id)` — find all tags pointing to a given version.
- **`npm_files`**: unique index on `(namespace_id, npm_version_id, file_name) WHERE soft_deleted_at IS NULL` — a file name must be unique within a version. The partial condition allows recreating a file with the same name after soft deletion; index on `(namespace_id, blob_storage_attachment_id)` — look up a file by its storage attachment; index on `(namespace_id, blob_sha256)` — reverse lookup from a stored blob sha256 to every npm file referencing it, powering cross-format checksum search. The existing version-keyed index cannot satisfy a digest-keyed scan directly.
- **`npm_metadata_files`**: unique index on `(namespace_id, npm_package_id, kind)` — one metadata file per package per kind; index on `(namespace_id, blob_storage_attachment_id)` — look up a metadata file by its storage attachment; index on `(namespace_id, blob_sha256)` — reverse lookup from a stored blob sha256 to every metadata file referencing it, mirroring [`npm_files`](#npm-repositories) so a single sha256 lookup covers both the tarball and the packument-style metadata.

#### Query examples

- Get all versions given a repository id and package name

  ```sql
  SELECT nv.*
  FROM npm_versions nv
  JOIN npm_packages np
    ON nv.npm_package_id = np.id AND nv.namespace_id = np.namespace_id
  WHERE np.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND np.npm_repository_id = '019a1b2c-0123-7abc-8def-000000000123' AND np.name = '@myorg/mypackage'
    AND np.soft_deleted_at IS NULL AND nv.soft_deleted_at IS NULL;
  ```

- Read per-package entity-count counters for the publish-path limit pre-check (advisory; the partial unique indexes on `npm_versions` and `npm_tags` are the authoritative race-free guards):

  ```sql
  SELECT versions_count, tags_count
  FROM npm_packages
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND id = '019a1b2c-0456-7abc-8def-000000000456' AND soft_deleted_at IS NULL;
  ```

- Get a file given a version id and a filename

  ```sql
  SELECT nf.*
  FROM npm_files nf
  WHERE nf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND nf.npm_version_id = '019a1b2c-0456-7abc-8def-000000000456' AND nf.file_name = 'mypackage-1.0.0.tgz'
    AND nf.soft_deleted_at IS NULL;
  ```

- Get the pre-computed full metadata file for a package (served on the npm metadata endpoint)

  ```sql
  SELECT bsb.object_storage_key, bsb.size
  FROM npm_metadata_files nmf
  JOIN blob_storage_blobs bsb ON bsb.namespace_id = nmf.namespace_id AND bsb.sha256 = nmf.blob_sha256
  WHERE nmf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND nmf.npm_package_id = 456 AND nmf.kind = 0
    AND nmf.expires_at > NOW();
  ```

  Reads filter on `expires_at > NOW()`. A miss (no row, or `expires_at <= NOW()` because a writer
  force-expired it or the TTL elapsed) runs the cache rebuild below on the request goroutine, then
  serves the row that rebuild committed. A miss therefore ends in a cache write and a blob open
  rather than in a body rendered straight into the response.

- Force-expire the packument cache on a write

  Publish, deprecate, unpublish, and dist-tag mutations invalidate the cache by flipping
  `expires_at` to `NOW()` on every kind for the affected package in the same transaction as the
  data write. The blob and attachment are left untouched so any response already in flight keeps
  resolving against the existing blob until the rebuild swaps the attachment.

  ```sql
  UPDATE npm_metadata_files
  SET expires_at = NOW()
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND npm_package_id = '019a1b2c-0456-7abc-8def-000000000456';
  ```

  For first-time publications no rows exist yet, so the `UPDATE` affects zero rows; the first
  rebuild to run inserts the cache rows, whether that is the cache job or an on-read fill.

- Upsert a metadata file after a version publish or unpublish

  The cache rebuild runs this once per kind for the package, whether the cache job or an on-read
  fill is running it. The old attachment must be deleted in the same transaction to prevent
  orphaned attachments from blocking blob garbage collection (see [Cleanup tasks](#cleanup-tasks)).

  ```sql
  -- The new blob and attachment (id=789) are created earlier in the same transaction.
  -- The interval below mirrors the configured `npm.packument_cache_ttl` (default 7 days).
  WITH old AS (
    SELECT blob_storage_attachment_id, blob_sha256
    FROM npm_metadata_files
    WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND npm_package_id = '019a1b2c-0456-7abc-8def-000000000456' AND kind = 0
  ),
  upsert AS (
    INSERT INTO npm_metadata_files (namespace_id, npm_package_id, kind, blob_storage_attachment_id, blob_sha256, expires_at)
    VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0456-7abc-8def-000000000456', 0, 789, 'abcd1234...'::bytea, NOW() + interval '7 days')
    ON CONFLICT (namespace_id, npm_package_id, kind)
    DO UPDATE SET blob_storage_attachment_id = EXCLUDED.blob_storage_attachment_id,
                  blob_sha256 = EXCLUDED.blob_sha256,
                  expires_at = EXCLUDED.expires_at
  )
  DELETE FROM blob_storage_attachments bsa
  USING old
  WHERE bsa.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND bsa.id = old.blob_storage_attachment_id
    AND bsa.sha256 = old.blob_sha256;
  ```

  On first insert the `old` CTE returns no rows, so no attachment is deleted.
  On conflict (update), the previous attachment is deleted. The old blob will be
  garbage-collected if no other attachments reference it (deduplication-safe:
  each client holds its own attachment, so removing one does not affect others
  sharing the same blob).

### NPM Remote Repositories

```mermaid
erDiagram
    repositories ||--|| npm_remote_repositories : "has one"
    npm_remote_repositories ||--o{ npm_remote_packages : "has many"
    npm_remote_packages ||--o{ npm_remote_versions : "has many"
    npm_remote_packages ||--o{ npm_remote_tags : "has many"
    npm_remote_packages ||--o{ npm_remote_metadata_files : "has many"
    npm_remote_metadata_files ||--o{ npm_remote_tags : "has many"
    npm_remote_versions ||--o{ npm_remote_files : "has many"
    npm_remote_tags ||--|| npm_remote_versions : "has one"
    npm_remote_metadata_files ||--|| blob_storage_attachments : "has one"
    npm_remote_files ||--|| blob_storage_attachments : "has one"

    npm_remote_repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid repository_id FK "NOT NULL, UNIQUE (namespace_id, repository_id), (repository_id, namespace_id) references repositories(id, namespace_id)"
        text url "NOT NULL, limit 1024"
        bytea wrapped_dek "nullable, this row's data-encryption key, wrapped by the namespace key"
        uuid ns_key_id FK "nullable, (ns_key_id, namespace_id) references namespace_encryption_keys(id, namespace_id), ON DELETE RESTRICT"
        int ns_key_version "nullable, the namespace key version this row was wrapped under"
        bytea encrypted_auth_token
        smallint cache_validity_hours "NOT NULL, DEFAULT 24"
        smallint metadata_cache_validity_hours "NOT NULL, DEFAULT 24"
        smallint last_health_status "NOT NULL, DEFAULT 0, 0=unknown, 1=healthy, 2=unhealthy"
        timestamptz last_health_checked_at "nullable"
    }

    npm_remote_packages {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_remote_repository_id FK "NOT NULL, (npm_remote_repository_id, namespace_id) references npm_remote_repositories(id, namespace_id)"
        text name "NOT NULL, limit 255"
        text scope "nullable, limit 255"
        timestamptz last_downloaded_at "nullable, buffered"
        timestamptz soft_deleted_at "nullable"
    }

    npm_remote_versions {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_remote_package_id FK "NOT NULL, (npm_remote_package_id, namespace_id) references npm_remote_packages(id, namespace_id)"
        text version "NOT NULL, limit 255"
        jsonb package_json "NOT NULL"
        bigint size_bytes "NOT NULL, DEFAULT 0, buffered counter"
        timestamptz last_downloaded_at "nullable, buffered"
        timestamptz soft_deleted_at "nullable"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
    }

    npm_remote_tags {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_remote_package_id FK "NOT NULL, (npm_remote_package_id, namespace_id) references npm_remote_packages(id, namespace_id)"
        uuid npm_remote_version_id FK "NOT NULL, (npm_remote_version_id, namespace_id) references npm_remote_versions(id, namespace_id)"
        uuid npm_remote_metadata_file_id FK "NOT NULL, (npm_remote_metadata_file_id, namespace_id) references npm_remote_metadata_files(id, namespace_id)"
        text name "NOT NULL, limit 255"
    }

    npm_remote_metadata_files {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_remote_package_id FK "NOT NULL, (npm_remote_package_id, namespace_id) references npm_remote_packages(id, namespace_id)"
        smallint kind "NOT NULL, 0=full, 1=dist_tags"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        timestamptz upstream_checked_at "NOT NULL, DEFAULT NOW()"
        text upstream_etag "nullable, limit 255"
    }

    npm_remote_files {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid npm_remote_version_id FK "NOT NULL, (npm_remote_version_id, namespace_id) references npm_remote_versions(id, namespace_id)"
        text file_name "NOT NULL, limit 255"
        bigint blob_storage_attachment_id FK "NOT NULL, (namespace_id, blob_storage_attachment_id, blob_sha256) references blob_storage_attachments(id, namespace_id, sha256)"
        bytea blob_sha256 FK "NOT NULL, (namespace_id, blob_sha256) references blob_storage_blobs(namespace_id, sha256)"
        timestamptz upstream_checked_at "NOT NULL, DEFAULT NOW()"
        text upstream_etag "nullable, limit 255"
        timestamptz soft_deleted_at "nullable"
    }
```

- **npm_remote_repositories**: Represents an external npm registry. Includes URL, credentials, artifact cache TTL (`cache_validity_hours`), and a separate TTL for package metadata responses (`metadata_cache_validity_hours`). Health check status is tracked for monitoring. References the parent `repositories` table via `repository_id`. Upstream credentials are stored as ciphertext alongside the wrapped data-encryption key that opens them; see [Encryption keys](#encryption-keys) for that column shape and its constraints. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_remote_packages**: A cached npm package. `last_downloaded_at` records when any cached file of the package was last downloaded; maintained via buffered/async writes to avoid hot-row contention. Used by `keep_last_downloaded_at` lifecycle rules and cache retention evaluation. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_remote_versions**: A cached version with its `package_json` metadata. Populated when the packument is fetched (it contains all version metadata). `last_downloaded_at` records when any cached file of the version was last downloaded; maintained via buffered/async writes to avoid hot-row contention. Used by `keep_last_downloaded_at` lifecycle rules and cache retention evaluation. `created_at` records when the version was first cached and powers cache-side publication-history and provenance scans, mirroring [`npm_versions`](#npm-repositories). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_remote_tags**: Cached dist-tag-to-version mappings (e.g., `latest`, `next`). Populated from the packument. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_remote_metadata_files**: Stores pre-computed metadata files cached from the upstream registry, one per kind per package. `kind` distinguishes between the full packument (`0`) containing all versions and the dist-tags-only mapping (`1`). `upstream_checked_at` records when the metadata was last validated against the upstream registry; compared with `metadata_cache_validity_hours` to decide if revalidation is needed. `upstream_etag` stores the ETag returned by the upstream, enabling conditional requests (`If-None-Match`) to avoid re-downloading unchanged metadata. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_remote_files**: A cached tarball. `file_name` holds the name derived from the upstream's `dist.tarball`, so it carries path separators when the upstream repeats the scope inside the file name (see [ADR-009](009_api_design.md)); `limit 255` therefore bounds the whole relative path rather than a single name, and it is the only bound, since no rule caps the number of elements. The hosted `npm_files` equivalent is always a single segment. `upstream_checked_at` records when the file was last validated against the upstream registry; compared with `cache_validity_hours` to decide if revalidation is needed. `upstream_etag` stores the ETag returned by the upstream, enabling conditional requests (`If-None-Match`) to avoid re-downloading unchanged tarballs. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **blob_storage_attachments**: See [Blob storage](#blob-storage) section for details.

#### Indexes

- **`npm_remote_repositories`**: unique index on `(namespace_id, repository_id)` — look up a remote repository by its parent reference; index on `(namespace_id, ns_key_id)`, which backs the [encryption key](#encryption-keys) foreign key so a key-row deletion can check its referencing rows without scanning the table.
- **`npm_remote_packages`**: unique index on `(namespace_id, npm_remote_repository_id, name) WHERE soft_deleted_at IS NULL` — look up a cached package by name. The partial condition allows recreating a package with the same name after soft deletion.
- **`npm_remote_versions`**: unique index on `(namespace_id, npm_remote_package_id, version) WHERE soft_deleted_at IS NULL` — look up a cached version within a package. The partial condition allows recreating a version with the same identifier after soft deletion; index on `(namespace_id, npm_remote_package_id, size_bytes DESC) WHERE soft_deleted_at IS NULL` — sort a cached package's versions by size for the version-list display; index on `(namespace_id, soft_deleted_at DESC) WHERE soft_deleted_at IS NOT NULL` — list soft-deleted cached versions ordered by deletion time, powering the artifact-granularity trash-listing query for cached npm artifacts; index on `(namespace_id, created_at DESC)` — chronological scans across the namespace, mirroring the local [`npm_versions`](#npm-repositories) index to cover cache-side publication history and provenance. Unconditional (no `soft_deleted_at` predicate) for the same audit-trail reason as the local index.
- **`npm_remote_tags`**: unique index on `(namespace_id, npm_remote_package_id, name)` — look up a distribution tag by name; index on `(namespace_id, npm_remote_version_id)` — find all tags pointing to a given version.
- **`npm_remote_metadata_files`**: unique index on `(namespace_id, npm_remote_package_id, kind)` — enforces one metadata file per package per kind; index on `(namespace_id, blob_storage_attachment_id)` — look up a metadata file by its storage attachment; index on `(namespace_id, blob_sha256)` — reverse lookup from a stored blob sha256 to every cached metadata file referencing it, mirroring the hosted [`npm_metadata_files`](#npm-repositories) index.
- **`npm_remote_files`**: unique index on `(namespace_id, npm_remote_version_id, file_name) WHERE soft_deleted_at IS NULL` — a file name must be unique within a version. The partial condition allows recreating a file with the same name after soft deletion; index on `(namespace_id, blob_storage_attachment_id)` — look up a file by its storage attachment; index on `(namespace_id, blob_sha256)` — reverse lookup from a stored blob sha256 to every cached npm file referencing it, mirroring the hosted [`npm_files`](#npm-repositories) index so checksum search covers cache-side references too.

#### Query examples

- Create a remote repository

  ```sql
  -- First create the parent repository
  INSERT INTO repositories (namespace_id, name, format, kind, visibility)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', 'npm-registry', 2, 2, 0)
  RETURNING id;
  -- Link the repository to a repository collection
  INSERT INTO repository_collection_repositories (namespace_id, repository_collection_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0456-7abc-8def-000000000456', <returned_id>);
  -- Then create the format-specific record
  INSERT INTO npm_remote_repositories (namespace_id, repository_id, url, wrapped_dek, ns_key_id, ns_key_version, encrypted_auth_token)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', <returned_id>, 'https://registry.npmjs.org', $1, $2, $3, $4);
  ```

- Get all cached versions for a package (serving a packument response)

  ```sql
  SELECT nrv.version, nrv.package_json
  FROM npm_remote_versions nrv
  JOIN npm_remote_packages nrp
    ON nrv.npm_remote_package_id = nrp.id AND nrv.namespace_id = nrp.namespace_id
  WHERE nrp.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND nrp.npm_remote_repository_id = '019a1b2c-0789-7abc-8def-000000000789'
    AND nrp.name = '@myorg/mypackage'
    AND nrp.soft_deleted_at IS NULL AND nrv.soft_deleted_at IS NULL;
  ```

- Pull a cached tarball (read-path shortcut)

  ```sql
  SELECT bsb.object_storage_key, bsb.size
  FROM npm_remote_files nrf
  JOIN blob_storage_blobs bsb
    ON bsb.namespace_id = nrf.namespace_id AND bsb.sha256 = nrf.blob_sha256
  WHERE nrf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
    AND nrf.npm_remote_version_id = '019a1b2c-0456-7abc-8def-000000000456'
    AND nrf.file_name = 'mypackage-1.0.0.tgz'
    AND nrf.soft_deleted_at IS NULL;
  ```

### NPM Virtual Repositories

```mermaid
erDiagram
    repositories ||--|| npm_virtual_repositories : "has one"
    npm_virtual_repositories ||--o{ npm_virtual_repository_upstreams : "has many"
    npm_virtual_repository_upstreams ||--|| repositories : "references upstream"
    npm_virtual_repository_upstreams ||--o{ npm_virtual_upstream_rules : "has many"

    npm_virtual_repositories {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id) ON DELETE NO ACTION"
        uuid repository_id FK "NOT NULL, UNIQUE (namespace_id, repository_id), (repository_id, namespace_id) references repositories(id, namespace_id) ON DELETE CASCADE"
    }

    npm_virtual_repository_upstreams {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id) ON DELETE NO ACTION"
        uuid npm_virtual_repository_id FK "NOT NULL, (npm_virtual_repository_id, namespace_id) references npm_virtual_repositories(id, namespace_id) ON DELETE CASCADE"
        uuid upstream_repository_id FK "NOT NULL, (upstream_repository_id, namespace_id) references repositories(id, namespace_id) ON DELETE NO ACTION"
        int position "NOT NULL, CHECK position >= 0"
    }

    npm_virtual_upstream_rules {
        uuid id PK "UUIDv7, application-generated, part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id) ON DELETE NO ACTION"
        uuid npm_virtual_repository_upstream_id FK "NOT NULL, (npm_virtual_repository_upstream_id, namespace_id) references npm_virtual_repository_upstreams(id, namespace_id) ON DELETE CASCADE"
        smallint rule_type "NOT NULL, 0=allow, 1=deny, CHECK rule_type IN (0, 1)"
        text pattern "NOT NULL, CHECK char_length(pattern) <= 255"
        smallint target_field "NOT NULL, 0=full_package_name, 1=scope, 2=version, CHECK target_field IN (0, 1, 2)"
    }
```

- **npm_virtual_repositories**: The virtual repository for npm packages. References the parent `repositories` table via `repository_id` for name, visibility, and cross-format queries. Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_virtual_repository_upstreams**: The table that joins virtual repositories and their upstreams. Each virtual repository has an ordered list of upstreams. Each entry references an upstream repository via `upstream_repository_id`, which points to `repositories(id, namespace_id)`. The composite FK `(namespace_id, upstream_repository_id)` enforces that upstreams are within the same namespace — consistent with the registry being scoped to namespaces ([ADR-001](001_organizations_as_anchor_point.md)). Partitioned by `HASH(namespace_id)` with 64 partitions.
- **npm_virtual_upstream_rules**: Defines allow/deny filter rules for an upstream. Each rule specifies a wildcard pattern and target field to control which artifacts are included or excluded when resolving through this upstream. Patterns are wildcards only for the MVP; regex support is deferred until customer feedback justifies it ([discussion](https://gitlab.com/gitlab-org/gitlab/-/work_items/597754#note_3291871207)). The database enforces the two enumerations and the pattern length: `CHECK rule_type IN (0, 1)`, `CHECK target_field IN (0, 1, 2)`, and `CHECK char_length(pattern) <= 255`. These are boundary rejections, so an out-of-range discriminator is refused at write time instead of being left for the read path to cope with. The pattern bound counts characters rather than bytes, so a 255-character pattern is admitted whatever it weighs in UTF-8. Partitioned by `HASH(namespace_id)` with 64 partitions.

`position` is 0-based here: `CHECK position >= 0` sets the floor, and 0 is the highest-priority slot. That floor is npm's alone, and it departs from the reference implementation rather than agreeing with it. The monolith's virtual registries are 1-based and gap-closing in every format they ship, npm included: [`virtual_registries_packages_npm_registry_upstreams`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/db/structure.sql) declares `"position" smallint DEFAULT 1 NOT NULL` with `CHECK ((1 <= "position") AND ("position" <= 20))`, and the shared [`VirtualRegistries::RegistryUpstream`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/ee/app/models/virtual_registries/registry_upstream.rb) assigns `maximum(:position).to_i + 1` on create and decrements every higher position when an entry is removed, so gaps are closed rather than tolerated. The container tables take a floor of 1, which agrees with that precedent: [S32](https://gitlab.com/gitlab-org/ops/artifact-registry/-/blob/main/docs/specs/S32-container-virtual.md) grounds it in S17's 1-based contiguous renumbering and in the query examples in this document, which start `position` at `1`. npm's `>= 0`, and its tolerance of the gap a removal leaves, are a deliberate choice of [S31](https://gitlab.com/gitlab-org/ops/artifact-registry/-/blob/main/docs/specs/S31-npm-virtual.md) against that precedent.

The two floors are not reconciled with each other, and only one of them is in a database. npm's shipped with [artifact-registry!2066](https://gitlab.com/gitlab-org/ops/artifact-registry/-/merge_requests/2066); container's is specified by S32 and has no migration yet. S32 assigns the disagreement to S17's management API or to this document rather than settling it in either format slice, on the grounds that a `position` value reaches no layer below that write surface: resolution reads the list in ascending order and never treats a position as an index. So this paragraph records the split rather than ratifying it. Tracked in [#985](https://gitlab.com/gitlab-org/ops/artifact-registry/-/work_items/985).

The foreign keys in these three tables carry these referential actions:

- `npm_virtual_repositories`, FK `(repository_id, namespace_id)` referencing `repositories`: `ON DELETE CASCADE`, the action [the general rule for format child tables](#repositories) already gives it.
- `npm_virtual_repositories`, FK `namespace_id` referencing `namespaces`: `NO ACTION`.
- `npm_virtual_repository_upstreams`, FK `namespace_id` referencing `namespaces`: `NO ACTION`.
- `npm_virtual_repository_upstreams`, FK `(npm_virtual_repository_id, namespace_id)` referencing `npm_virtual_repositories`: `ON DELETE CASCADE`.
- `npm_virtual_repository_upstreams`, FK `(upstream_repository_id, namespace_id)` referencing `repositories`: `NO ACTION`.
- `npm_virtual_upstream_rules`, FK `namespace_id` referencing `namespaces`: `NO ACTION`.
- `npm_virtual_upstream_rules`, FK `(npm_virtual_repository_upstream_id, namespace_id)` referencing `npm_virtual_repository_upstreams`: `ON DELETE CASCADE`.

The two foreign keys on `npm_virtual_repository_upstreams` take opposite actions, and the difference is deliberate. `npm_virtual_repository_id` is the parent-to-child link, so deleting a virtual repository takes its upstream associations with it. `upstream_repository_id` is a sibling reference, so deleting a repository that is still listed as an upstream is refused: cascading there would shrink every virtual repository that listed it, possibly to an empty list, with no operator signal. Removing an upstream has to be a deliberate management action, which is also why the reverse-lookup index below exists.

The cascade chain runs three levels, so one delete of a `repositories` row reaches a rule through `npm_virtual_repositories` and then `npm_virtual_repository_upstreams`.

#### Indexes

- **`npm_virtual_repositories`**: unique index on `(namespace_id, repository_id)` — look up a virtual repository by its parent reference.
- **`npm_virtual_repository_upstreams`**: unique constraint on `(namespace_id, npm_virtual_repository_id, position)`, `DEFERRABLE INITIALLY DEFERRED` — retrieve ordered upstreams for a virtual repository; deferrable to allow reordering within a transaction. Unique index on `(namespace_id, npm_virtual_repository_id, upstream_repository_id)` — prevent the same upstream from being added to a virtual repository twice. Index on `(namespace_id, upstream_repository_id)` — find every virtual repository that lists a given repository as an upstream, which is what the `NO ACTION` guard above and the association surface read. Neither unique entry has this as a usable prefix, and PostgreSQL does not index foreign-key columns automatically.
- **`npm_virtual_upstream_rules`**: index on `(namespace_id, npm_virtual_repository_upstream_id)` — fetch all rules for a given upstream. It leads on `namespace_id`, so a read of it has to carry its own `namespace_id` equality; keyed on the foreign-key column alone the read matches no usable prefix and scans every partition.

The ordered-upstream entry is a unique **constraint**, not a unique index. Deferral is a property of a constraint, so it is added with `ALTER TABLE ... ADD CONSTRAINT ... UNIQUE (...) DEFERRABLE INITIALLY DEFERRED`; `CREATE UNIQUE INDEX ... DEFERRABLE` is a syntax error in PostgreSQL. A deferrable unique constraint also cannot arbitrate `ON CONFLICT`, so a `position` write is an `UPDATE` followed by an `INSERT`, never an upsert on this key.

#### Query examples

- Create a virtual repository

  ```sql
  -- First create the parent repository
  INSERT INTO repositories (namespace_id, name, format, kind, visibility)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', 'my-virtual-repo', 2, 1, 1)
  RETURNING id;
  -- Link the repository to a repository collection
  INSERT INTO repository_collection_repositories (namespace_id, repository_collection_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0456-7abc-8def-000000000456', <returned_id>);
  -- Then create the format-specific record
  INSERT INTO npm_virtual_repositories (namespace_id, repository_id)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', <returned_id>);
  ```

- Associate a virtual repository with an upstream

  ```sql
  INSERT INTO npm_virtual_repository_upstreams (namespace_id, npm_virtual_repository_id, upstream_repository_id, position)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0123-7abc-8def-000000000123', '019a1b2c-0789-7abc-8def-000000000789', 1);
  ```

### Blob storage

The blob storage data organization has been done under the following assumptions:

- We don't need to handle one-to-many associations to blobs. This is handled by the blob storage clients area. Thus, we only need one-to-one association.
- We need to track how many blob storage clients use a single blob (deduplication) for proper [cleanup handling](#cleanup-tasks).
- Additionally, we might want to track the different origins of each usage for a single blob.

The schema we're presenting here only takes into account the storage side of the data. There might be auxiliary tables required for additional aspects such as metrics or [cleanup](#cleanup-tasks) that are not described here as these parts are still under evaluation. Upload session tracking is described in [Upload sessions](#upload-sessions).

```mermaid
erDiagram
    blob_storage_attachments ||--|| blob_storage_blobs : "has one"

    blob_storage_attachments {
        bigint id PK "DEFAULT nextval('blob_storage_attachments_id_seq')"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        bytea sha256 PK,FK "NOT NULL, (namespace_id, sha256) references blob_storage_blobs(namespace_id, sha256)"
    }

    blob_storage_blobs {
        bigint id PK "DEFAULT nextval('blob_storage_blobs_id_seq')"
        uuid namespace_id PK "NOT NULL, UNIQUE with sha256, no namespaces(id) reference by design"
        bytea sha256 PK "NOT NULL, UNIQUE with namespace_id"
        text object_storage_key "NOT NULL, limit 1024"
        bigint size "NOT NULL"
        bytea metadata_sha1 "nullable, CHECK octet_length = 20"
    }
```

- **blob_storage_attachments**: Tracks the usage of a given blob. Each client (Container, NPM or Maven repositories tables) needs to create a record here every time they want to use (create or re-use) a blob record. Each usage _needs_ to have a single record here. Clients are responsible for deleting the attachment record when they delete the referencing artifact record (file, blob, cache entry). Both deletions must happen in the same transaction to prevent orphaned attachments from blocking blob cleanup. The foreign key from client tables to `blob_storage_attachments` enforces referential integrity (prevents dangling references) but does not use `ON DELETE CASCADE` — cleanup is application-managed. For example, two Maven packages having the exact same file should each reference a different attachment record which in turn references the same blob record. The `namespace_id` column is required for Cells sharding. The `sha256` column is propagated from the referenced `blob_storage_blobs` record to enable partition-pruned joins (see [partitioning strategy](#blob-storage-partitioning-strategy)). The primary key is `(id, namespace_id, sha256)` rather than the conventional `(id)`: `sha256` is required because PostgreSQL forces the partition key to be part of every unique constraint on a hash-partitioned table, and `namespace_id` is required to keep the PK globally unique across deployments. The local `bigint id` is unique only within a single Artifact Registry database (see [Namespace ID type](#namespace-id-type)), so on cross-deployment namespace migration ([ADR-022](022_namespace_decoupling.md)) the same `(id, sha256)` pair could already exist in the target database. Adding the UUIDv7 `namespace_id` to the PK rules out that collision by construction. Client tables reference this composite PK via `(namespace_id, blob_storage_attachment_id, blob_sha256)`.
- **blob_storage_blobs**: This table lists all file contents (as blobs) that are present on object storage. The object storage key is entirely stored on a dedicated column and not computed every time a blob is used. `sha256` is the fundamental content-addressable identifier and is always present (`NOT NULL`). The `namespace_id` column scopes deduplication to an Organization, and carries no `namespaces(id)` reference by design: this row owns `object_storage_key`, the only handle to the stored object, and [ADR-025](025_garbage_collection.md) has garbage collection delete that object before the row, so a cascade from `namespaces` would destroy the handle while the object was still live and leak it, while a blocking reference would stall every namespace deletion behind a deliberately deferred garbage-collection cycle. A namespace hard-delete therefore leaves blob rows behind until garbage collection reclaims them. Format-specific checksums (for example, Maven's SHA1 and MD5) are stored on the format-specific file tables rather than here, keeping this table format-agnostic. Content type is excluded for the same reason: it is a property of how a format interprets a blob, not of the blob itself, and belongs in format-specific tables. The `metadata_sha1` column is a deliberate, scoped exception to that format-agnostic rule: it mirrors the SHA-1 from the MVP user-metadata allowlist attached to a blob at commit time, and is `NULL` when no SHA-1 was supplied. It is present on `blob_storage_blobs` (rather than on format-specific tables) because the storage layer's blob-info lookup is contractually a single DB round-trip on the push and pull hot paths; surfacing user metadata without a DB mirror would force a per-digest object-storage HEAD fan-out or partial-API surfacing. The same value is attached to the storage object as a backend-native `x-amz-meta-checksum-sha1` / `x-goog-meta-checksum-sha1` header at commit time, and rows are immutable, so the DB and storage-object copies cannot drift. Future allowlist additions add their own nullable columns by amendment. The primary key is `(id, namespace_id, sha256)` for the same reasons as `blob_storage_attachments` above: `sha256` satisfies PostgreSQL's partition-key inclusion rule, the UUIDv7 `namespace_id` keeps the PK globally unique across deployments, and the surrogate `bigint id` keeps the row-identifier shape consistent across the blob-storage tier. Per-Organization deduplication is enforced by a separate `UNIQUE (namespace_id, sha256)` constraint, which also serves as the lookup-by-content-hash index and is the target of every foreign key into this table. No FK references the PK directly: `(namespace_id, sha256)` already uniquely identifies a row and is globally unique on its own via the UUIDv7 `namespace_id`, so callers join via the natural key without carrying the surrogate `id`.

The blob storage tables are designed to be reusable outside the Artifact Registry. This allows other features to leverage the same deduplication and storage infrastructure.

All hash columns (`digest` and `sha256`; `sha1`, `md5` and `sha512` — Maven specific) are stored as `bytea` holding raw hash bytes, with no text encoding or inline algorithm prefix. The container `digest` and `blob_sha256` columns hold the raw 32-byte SHA-256, enforced by `CHECK octet_length = 32`; the OCI wire form `sha256:<64 hex chars>` is converted to and from raw bytes at the service layer, so `blob_sha256` joins `blob_storage_blobs.sha256` as a direct byte comparison. The MVP supports only sha256 — a non-sha256 reference is rejected at the service layer before it reaches these tables — so no separate `digest_algorithm` column is stored. Because a container blob's `digest` and `blob_sha256` are then the same bytes, the `(namespace_id, digest)` index doubles as the content-hash reverse-lookup index and the hosted container tables carry no separate `blob_sha256` index (see [Container Repositories indexes](#container-repositories)). A future non-sha256 digest algorithm would separate the two columns and revisit this.

### Upload sessions

Upload sessions track in-progress blob uploads through the two-phase upload lifecycle described in [ADR-008](008_content_addressable_storage.md#two-phase-upload-strategy). Each session maps to a temporary storage object at `uploads/{upload_id}` within the namespace's storage partition. Sessions are database-tracked from the initial schema to support the upload API (resumable uploads, concurrent upload resolution) and to enable [upload purging](#cleanup-tasks) without object storage enumeration ([ADR-011](011_data_reconciliation.md)).

```mermaid
erDiagram
    namespaces ||--o{ upload_sessions : "has many"
    repositories ||--o{ upload_sessions : "has many"

    upload_sessions {
        bigint id PK "DEFAULT nextval('upload_sessions_id_seq'), part of composite PK (id, namespace_id)"
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id)"
        uuid repository_id FK "NOT NULL, (repository_id, namespace_id) references repositories(id, namespace_id)"
        uuid upload_id "NOT NULL"
        bigint size_bytes "NOT NULL, DEFAULT 0, bytes uploaded so far"
        bytea hash_state "nullable, serialized intermediate SHA-256 hash state"
        boolean dirty "NOT NULL, DEFAULT FALSE, concurrent-writer poison bit"
        timestamptz created_at "NOT NULL, DEFAULT NOW()"
        timestamptz expires_at "NOT NULL"
        timestamptz updated_at "NOT NULL, DEFAULT NOW(), chunk-append latency metrics"
    }
```

- **upload_sessions**: Tracks each blob upload while it is in progress. The table follows a binary existence model, mirroring the [container registry pattern](https://gitlab.com/gitlab-org/container-registry/-/blob/master/registry/storage/blobwriter.go): if the row exists, the upload is in progress or requires cleanup; if it does not, the upload completed or was purged. On completion, the storage layer moves the blob to the content-addressable store, then deletes the session row in the same transaction that creates the `blob_storage_blobs` record. Format-specific rows (`blob_storage_attachments` and format tables) are created by the calling format subsystem in a separate transaction afterward — this keeps the storage layer format-agnostic. The `upload_id` (UUID) is the storage-level identifier used in the temporary object path (`uploads/{upload_id}`). The `repository_id` records the repository that initiated the upload. On follow-up requests, the server verifies that the repository in the URL matches session.repository_id, preventing cross-repo reuse of an upload_id if one leaks. Authorization for each request is performed by the request middleware against the URL's repository and does not depend on this column. The composite FK `(namespace_id, repository_id)` enforces that uploads are within the same namespace as the target repository. `size_bytes` tracks the number of bytes written to temporary storage. For resumable uploads, it is updated as each chunk arrives and is used to produce the `Range` response header that tells clients where to resume ([OCI Distribution Spec](https://github.com/opencontainers/distribution-spec/blob/main/spec.md)); for monolithic uploads, it is set after the blob data is written. `created_at` records when the upload started; it enables upload duration metrics (correlating duration with blob size) and retroactive expiry if the application's TTL configuration is lowered (`WHERE created_at < NOW() - :new_ttl`), which `expires_at` alone cannot support since existing sessions retain their original expiry. `expires_at` is the session expiry timestamp, computed at creation as `NOW() + :configured_ttl` based on upload type (shorter for non-resumable, longer for resumable uploads). Expired sessions are candidates for upload purging: the purger deletes the temporary storage object and removes the row ([ADR-008](008_content_addressable_storage.md#temporary-object-cleanup)). Hash state for resumable uploads is stored in the `hash_state` column as serialized intermediate SHA-256 state; a single-row `UPDATE` is simpler than per-PATCH object-storage round-trips (see [ADR-008](008_content_addressable_storage.md#resumable-uploads-and-hash-state)). That `UPDATE` takes no row lock: concurrent writers for one `upload_id` are reconciled by a compare-and-swap on `size_bytes` plus the `dirty` poison bit rather than by `SELECT ... FOR UPDATE` locking (terminate-on-divergence). `dirty` is that poison bit, set by a CAS loser and cleared only by row deletion. `updated_at` records the last modification time of the session, supporting chunk-append latency metrics and last-activity observability. It is a stored column rather than derived from access logs because it backs synchronous resume-path decisions at request time; the write cost is negligible since it rides the existing `size_bytes`/`hash_state` `UPDATE`. Partitioned by `HASH(namespace_id)` with 64 partitions, consistent with every other `namespace_id`-scoped table in the schema; although sessions are short-lived, the upload purger is deferred ([ADR-011](011_data_reconciliation.md)) so expired rows accumulate until it ships, and partitioning from day one avoids a later migration, preserves partition-wise join eligibility with `repositories`, and costs nothing on empty partitions. The primary key is `(id, namespace_id)` rather than the conventional `(id)` — PostgreSQL requires the partition key in every unique constraint on a hash-partitioned table, and this PK's partition key is the UUIDv7 `namespace_id`, so it is already globally unique across deployments — unlike `blob_storage_attachments` and `blob_storage_blobs`, which partition by `sha256` and add `namespace_id` for the same guarantee.

#### Indexes

- **`upload_sessions`**: unique index on `(namespace_id, upload_id)` — look up a session by its upload UUID within a namespace. Index on `expires_at` — find expired sessions for upload purging. Index on `(namespace_id, repository_id)` — find all sessions for a given repository, used for authorization checks and cleanup on repository deletion.

#### Query examples

- Create an upload session

  ```sql
  INSERT INTO upload_sessions (namespace_id, repository_id, upload_id, expires_at)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', '019a1b2c-0456-7abc-8def-000000000456', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', NOW() + INTERVAL '1 hour')
  RETURNING id, upload_id;
  ```

- Look up a session during a chunked upload

  ```sql
  SELECT *
  FROM upload_sessions
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND upload_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11';
  ```

- Update session state after a chunk append (`hash_state` + `updated_at`, compare-and-swap on `size_bytes`)

  ```sql
  UPDATE upload_sessions
  SET size_bytes = 1048576, hash_state = 'a1b2c3...'::bytea, updated_at = NOW()
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND upload_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'
    AND size_bytes = 524288;  -- CAS: only persist if no concurrent writer advanced the row; a zero-rowcount result is a conflict
  ```

- Find expired sessions for upload purging

  ```sql
  SELECT id, namespace_id, upload_id
  FROM upload_sessions
  WHERE expires_at < NOW()
  ORDER BY expires_at
  LIMIT 100;
  ```

  This query is not partition-pruned — the predicate does not include `namespace_id`, so it scans all 64 partitions. That is acceptable here: the purger is a bounded background job (`LIMIT 100`, backed by the index on `expires_at`), not a hot-path query, so the fan-out is not performance-critical.

- Delete a session after cleanup

  ```sql
  DELETE FROM upload_sessions
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND id = 789;
  ```

### Partitioning invariant

**Every table that includes `namespace_id` is partitioned.** The default partition key is `HASH(namespace_id)` with 64 partitions; specific tables may use a different key when there is a documented reason (see [Blob storage partitioning strategy](#blob-storage-partitioning-strategy) for the `HASH(sha256)` exception). Tables that do not include `namespace_id` are not partitioned.

The rule is stated as a property of the row, not a per-table judgement: if `namespace_id` is part of the schema, the table is partitioned. There is no carve-out for "this table is small," "this table is 1:1 with its parent," or "we can add partitioning later." Small tables are partitioned the same as large ones; uniformity is the point. The cost of partitioning a low-volume table is negligible — sixty-four nearly-empty children, no measurable runtime overhead — while the cost of _adding_ partitioning later is dominated by table rewrite, primary-key reshape, and cascading foreign-key changes once production data is in place.

The [Exceptions](#exceptions) below are structural in the same way, and none of them is one of the judgements rejected here.

#### Mechanical consequences

PostgreSQL requires the partition key to be part of every unique constraint on a partitioned table. This shapes primary keys and foreign keys throughout the schema:

- **Primary keys.** Every partitioned table's primary key absorbs `namespace_id`: `(id)` becomes `(id, namespace_id)`. Unique indexes on partitioned tables include `namespace_id` as a leading column.
- **Foreign keys between partitioned tables.** Composite on `namespace_id`. A child references its parent via `(<parent>_id, namespace_id)` referencing the parent's `(id, namespace_id)`. This is the form across `repositories`, `workspaces`, format-specific repository tables, mid-tier tables, file tables, and remote cache tables, with one variation: the ancestor-id kind. A table that denormalizes an ancestor id alongside a parent reference widens that reference to carry it, so the key spans `namespace_id`, the ancestor id, and the parent id as a set, against a secondary unique index on the parent over the same three columns. The schema's other three-column family, the `blob_storage_attachments` references, is not this variation: each carries the parent's own `sha256` alongside the parent id rather than a denormalized ancestor id. The database then refuses a row whose parent belongs to a different ancestor than the row names, which the two-column form permits. `container_manifest_relationships` widens both of its `container_manifests` references on `container_image_id`, `maven_files` widens its `maven_versions` reference on `maven_package_id`, and `maven_remote_files` widens its `maven_remote_versions` reference on `maven_remote_package_id`. Column order follows each parent's unique index rather than one convention, so it is not uniform across the three. The widened reference replaces the two-column one rather than joining it, because a present three-column key implies a present `(<parent>_id, namespace_id)` pair. The widening belongs to the individual reference and does not follow from a `NOT NULL` ancestor column: `container_remote_manifest_relationships` keeps the two-column form toward `container_remote_manifests` while its hosted twin widens, because nothing writes a cache-side child link today ([artifact-registry#264](https://gitlab.com/gitlab-org/ops/artifact-registry/-/work_items/264)). A nullable ancestor column cannot carry the widening at all, because MATCH SIMPLE skips a key with any NULL column, leaving the widened reference to enforce nothing for those rows.
- **Foreign keys to `namespaces`.** Single-column. `namespace_id` references `namespaces(id)`. `namespaces` is the only table whose primary key stays `(id)` — it is unpartitioned and has no `namespace_id` of its own (it _defines_ one), so child tables reference it without composite-PK gymnastics.

The composite foreign-key shape encodes the namespace boundary at the schema level: a row in any partitioned table cannot reference a row in another partitioned table that belongs to a different namespace, because the foreign key forbids it. This is the same boundary the Cells sharding key (`namespace_id`) draws at the application level, made redundant in the database itself.

#### Exceptions

Two structural conditions leave a table unpartitioned, and nothing else does.

**A table that lacks `namespace_id`.** The principal example today is `namespaces` itself: the routing root resolved from `slug` before `namespace_id` is known, with no `namespace_id` column because it defines one. Future tables without `namespace_id` — for example, instance-wide configuration, global cron state, or deployment-scoped lifecycle metadata — inherit this default automatically and are not partitioned.

**A table whose entire primary key is `namespace_id`,** with no separate `id` column, so it holds one row per namespace and cannot represent a second, and which no foreign key references. `namespace_statistics` is the only table that qualifies today. Any future table claiming this condition states in its own description that its primary key is exactly `(namespace_id)` and that nothing references it, which is what makes the claim auditable rather than asserted.

This second condition is deliberately not the "this table is 1:1 with its parent" carve-out the invariant rejects. That one was a judgement about a relationship an implementer could argue either way; this is a property of the schema, settled by the key definition and by the catalog's list of constraints referencing the table. A table with its own `id` is outside it however small it is, and a table that acquires an `id` — or an inbound foreign key — leaves it at that moment. Neither argument behind the invariant reaches a table of this shape. Partitioning exists so a `namespace_id`-scoped read touches one partition instead of 64, but here the primary key _is_ `namespace_id`, so every read is already a single-row key lookup. And converting later is cheap for two reasons that both have to hold: the primary-key reshape the invariant is written to avoid — `(id)` becoming `(id, namespace_id)` — is already done, since a table keyed on `namespace_id` alone satisfies PostgreSQL's requirement that the partition key belong to every unique constraint; and PostgreSQL cannot `ALTER` an ordinary table into a partitioned one, so conversion means building a partitioned table and swapping this one in underneath it, which forces every inbound foreign key to be dropped and recreated against the new table, each recreation revalidating with a scan of the referencing table. A table nothing references has none to drop. That is why the absence of inbound foreign keys is part of the condition rather than an observation about today's schema: a table that later acquires a reference would otherwise keep the exception while the argument for it no longer held.

Both exception predicates are structural: presence or absence of `namespace_id` in the row, and whether that column is the whole primary key of a table nothing references. Neither depends on row count, write frequency, or current access patterns, all of which can change as the system evolves.

Single-tenant deployments (Dedicated, Self-Managed, single-Organization Cells) are not an exception either: they keep all 64 partitions, with one populated and 63 empty. Empty partitions are negligible at this scale (a few KB of catalog and index overhead each), partition pruning is unaffected, and schema uniformity across deployments is more valuable than carving out a single-tenant variant. The pathological "one partition holds everything" case applies only to `blob_storage_blobs` / `blob_storage_attachments` at full multi-tenant scale, which is why those two tables use `HASH(sha256)` instead — see [Blob storage partitioning strategy](#blob-storage-partitioning-strategy).

### Blob storage partitioning strategy

As noted in [Consequences](#negative), `blob_storage_blobs` and `blob_storage_attachments` will accumulate very high row counts as they serve all artifact formats across all Organizations. Without a deliberate partitioning strategy, this leads to:

- Index bloat and degrading query performance as the tables grow into billions of rows.
- Table-wide locks (for example, during index creation or schema migrations) that block all artifact types simultaneously.
- Autovacuum contention at high write rates.

A key constraint to keep in mind: PostgreSQL requires the partition key to be part of every unique constraint on a partitioned table. For `blob_storage_blobs`, the deduplication constraint is `UNIQUE (namespace_id, sha256)`. Any strategy whose partition key is not a subset of those columns would force additional columns into that constraint — which would no longer prevent the same blob from being stored twice within the same Organization across different partitions, undermining the deduplication model entirely.

Below are the candidate strategies.

#### Option A: Hash partitioning by `sha256`

Partition both tables using `PARTITION BY HASH (sha256)` with 64 partitions.

Since `sha256` is a content-addressable digest, its values are uniformly distributed by nature — no additional effort is needed for even data distribution. This solves the single-tenant problem: single-tenant deployments (Dedicated, Self-Managed, single-Organization Cells) would concentrate all rows in a single partition when using `namespace_id` alone. With `sha256` as the partition key, rows spread evenly across all 64 partitions regardless of how many Organizations exist.

The existing unique constraint on `[namespace_id, sha256]` already includes `sha256`, so it is compatible with this scheme — PostgreSQL can enforce uniqueness across hash partitions because the partition key is part of the constraint.

This approach requires `sha256` to be propagated to `blob_storage_attachments` and to format-specific tables (`*_files`, `container_blobs`, `container_manifests`, cache entries) so that joins to `blob_storage_blobs` can target a single partition. This means blob identifiers (`namespace_id` + `sha256`) are stored in both `*_files` and `blob_storage_attachments` rows, using more physical storage than a simple `bigint` foreign key (`sha256` is 32 bytes as `bytea` vs 8 bytes for a `bigint`). However, the trade-off is justified: the read path (artifact pull) — the hottest query in the system — can join directly from `*_files` to `blob_storage_blobs` via `(namespace_id, sha256)`, skipping `blob_storage_attachments` entirely and eliminating one join. Attachments remain necessary for the lifecycle path — answering "is this blob still used by anyone?" during [cleanup](#cleanup-tasks).

The five critical access patterns behave as follows:

| # | Operation | Frequency | Partitions hit |
| --- | --- | --- | --- |
| AP1 | Pull artifact (`*_files` → `blob_storage_blobs` via `namespace_id` + `sha256`) | Highest | 1 |
| AP2 | Orphan check (`WHERE namespace_id = ? AND sha256 = ?`) | High | 1 |
| AP3 | Dedup upsert (`ON CONFLICT (namespace_id, sha256) DO NOTHING`) | Medium-high | 1 |
| AP4 | Attachment CRUD (`namespace_id` + `sha256` propagated from blob) | Medium | 1 |
| AP5 | Storage accounting by Organization (`WHERE namespace_id = ?`, no `sha256`) | Low | All 64 (mitigated) |

**Positive**:

- Uniform distribution regardless of tenant concentration: single-tenant deployments spread data across all 64 partitions instead of concentrating in one.
- All high-frequency access patterns (pull, orphan check, dedup upsert, attachment CRUD) hit exactly one partition.
- The unique constraint `(namespace_id, sha256)` includes the partition key — dedup upserts target a single partition and resolve concurrent uploads via `ON CONFLICT DO NOTHING` without external locking.
- The read path (artifact pull) skips the `blob_storage_attachments` join entirely, going directly from `*_files` to `blob_storage_blobs` via `(namespace_id, sha256)`.

**Negative**:

- `sha256` must be propagated to more tables: `blob_storage_attachments` and format-specific tables (`*_files`, `container_blobs`, `container_manifests`, cache entries) carry `(namespace_id, sha256)` in addition to the `blob_storage_attachment_id` foreign key. This duplicates blob identifiers across rows, increasing per-row storage.
- Queries with only `namespace_id` (no `sha256`) cannot prune partitions and scan all 64. The main case is storage accounting (summing blob sizes per Organization). This is mitigated by dedicated rollup tables updated via delayed increments on blob insert/delete — a pattern already established at GitLab (for example, project statistics). Even without rollup tables, a parallel aggregate across 64 partitions completes in seconds.

#### Option B: Hash partitioning by `namespace_id`

Partition both tables using `PARTITION BY HASH (namespace_id)` with a fixed number of partitions.

All common access patterns already include `namespace_id` in their `WHERE` clause, so the query planner can target a single partition for every operation. The Cells sharding key (`namespace_id`) doubles as the partition key, which is consistent with the broader architecture.

The unique constraint on `[namespace_id, sha256]` already includes `namespace_id`, so it is compatible with this scheme without any modification — PostgreSQL enforces uniqueness globally across all hash partitions.

**Positive**:

- All Organization-scoped queries hit a single partition; the query planner prunes all others automatically.
- Partition pruning applies directly to the cleanup path: the orphan check on `blob_storage_attachments` (`WHERE namespace_id = ? AND sha256 = ?`) is guaranteed to target a single partition, keeping lookup cost bounded by partition size rather than total table volume.
- Schema changes and locks are scoped to a single partition, reducing the impact on other Organizations.
- Aligns with the Cells sharding key; no cross-partition work for common access patterns.
- Existing constraint on `[namespace_id, sha256]` works correctly without modification.

**Negative**:

- Organizations with very high blob counts can dominate their hash partition if Organization sizes vary significantly. In single-tenant deployments (Dedicated, Self-Managed, single-Organization Cells), all rows concentrate in a single partition — VACUUM takes hours and indexes reach hundreds of GB.
- Any query that omits `namespace_id` from the `WHERE` clause scans all partitions.

#### Option C: Range partitioning by `id` (primary key)

Partition both tables by ranges of the auto-incrementing primary key. This is the approach used by GitLab's existing [table partitioning framework](https://docs.gitlab.com/ee/development/database/table_partitioning.html) and is well supported by existing tooling.

**Positive**:

- Partition sizes grow predictably; new partitions are easy to add as data accumulates.
- Compatible with GitLab's existing partition management infrastructure.

**Negative**:

- Breaks deduplication uniqueness: PostgreSQL requires `id` to be part of every unique constraint on the partitioned table. Adding `id` to `[namespace_id, sha256]` means the same sha256 for the same Organization could appear in multiple partitions — the deduplication model breaks entirely.
- Queries are Organization-scoped but partitions are id-range-based, so every Organization-scoped query spans multiple partitions.
- Lock scope reduction does not align with Organization boundaries.

#### Option D: Range partitioning by `created_at`

Partition both tables by time ranges (for example, monthly or quarterly windows).

**Positive**:

- Easy to archive or drop old partitions once their blobs have been cleaned up.
- Partitions correspond to known time windows, which is a clear operational model.

**Negative**:

- Hot partition problem: all writes target the most recent partition, concentrating write contention.
- Blobs expire when they lose all attachments, not by age. Time-based partitioning does not align with the actual blob lifecycle.
- Same unique constraint issue as Option C: `created_at` would need to be added to the unique constraints, breaking cross-partition deduplication.
- Access patterns are Organization-scoped, not time-scoped, so queries span all partitions.

#### Option E: No partitioning

Rely on Cells-level sharding (`namespace_id`) and standard indexing as the primary scalability mechanism. Partitioning is deferred until metrics show it is needed.

**Positive**:

- Simple schema and operations: no partition management overhead; migrations and schema changes are straightforward.
- Sufficient at early scale: works well while row counts remain manageable within a single Cell.

**Negative**:

- Unbounded growth within a Cell: table-level locks affect all Organizations simultaneously as the tables grow.
- Even well-designed indexes face performance pressure at very high row counts.

#### Decision

**Hash partitioning by `sha256` (Option A) is chosen** for both `blob_storage_blobs` and `blob_storage_attachments`.

It is the only option that:

1. Keeps all high-frequency access patterns (artifact pull, orphan check, dedup upsert, attachment CRUD) within a single partition.
2. Distributes rows uniformly regardless of tenant concentration — critical for single-tenant deployments (Dedicated, Self-Managed, single-Organization Cells) where `namespace_id`-based partitioning would concentrate all rows in one partition.
3. Is compatible with the existing unique constraint on `[namespace_id, sha256]` without modification, and enables race-free dedup upserts via `ON CONFLICT (namespace_id, sha256) DO NOTHING`.

An initial value of 64 partitions is chosen for both tables. This provides sufficient distribution and lock isolation while keeping operational overhead manageable.

The trade-off is that `sha256` must be propagated to `blob_storage_attachments` and format-specific tables (`*_files`, `container_blobs`, `container_manifests`, cache entries). This duplicates blob identifiers (`namespace_id` + `sha256`) across rows, using more physical storage than a `bigint` foreign key alone. The benefit is that the read path — the hottest query in the system — joins directly from `*_files` to `blob_storage_blobs` via `(namespace_id, sha256)`, skipping `blob_storage_attachments` entirely and eliminating one join. Attachments remain for the [cleanup lifecycle path](#cleanup-tasks) only.

Queries with only `namespace_id` (no `sha256`), such as Organization-level storage accounting, cannot prune partitions and scan all 64. This is mitigated by dedicated rollup tables updated via delayed increments — a pattern already established at GitLab (for example, project statistics).

### Format-specific table partitioning strategy

Format-specific tables — hosted content tables and their remote counterparts — follow the `HASH(namespace_id)` default established by the [Partitioning invariant](#partitioning-invariant); each table's bullet records that explicitly. Hosted and remote share one strategy because they share the same access shape: every primary access pattern is `namespace_id`-scoped. Per-table differences (cache TTL, upstream metadata) are orthogonal to partitioning and live in the per-table descriptions.

Rationale specific to this group:

- All primary access patterns are `namespace_id`-scoped — lookup by repository and artifact coordinates, listing files for a package or image, listing cached entries for an upstream — so `HASH(namespace_id)` gives single-partition pruning for every operation. The read-path shortcut (`*_files` → `blob_storage_blobs` via `(namespace_id, sha256)`, skipping `blob_storage_attachments`) — the hottest query in the system — benefits directly from this partitioning.
- The single-tenant concentration concern that drives `blob_storage_blobs` to `HASH(sha256)` does not apply: each format-specific table is scoped to one format (and, for remotes, to one upstream), so its per-namespace footprint is structurally a fraction of the cross-format aggregate that `blob_storage_blobs` holds.
- Joins to `blob_storage_blobs` via `(namespace_id, blob_sha256)` prune the format-table partition on the `namespace_id` literal. The blob side prunes at plan time only when the query names the digest: a column-to-column predicate such as `blob_storage_blobs.sha256 = maven_files.blob_sha256` leaves `sha256` unknown to the planner, which builds an `Append` over all 64 blob partitions and prunes per outer row at execution instead. The scan is avoided at run time, not at plan time, and the cost lands in planning.

Measured on PostgreSQL 17.10, on a single-namespace fixture of 5,000 rows each in `blob_storage_blobs`, `blob_storage_attachments`, and `maven_files`. Both rows are the same read — one `maven_files` row and its blob's size — with the blob side pointed at each table in turn. The second is the [namespace-level reconciliation](#namespace-level-storage-accounting-reconciliation) shadow, `PARTITION BY HASH (namespace_id)` with `PRIMARY KEY (namespace_id, sha256) INCLUDE (size)`. Each figure is the range over five repeats in one session.

| Table joined for the blob's size | Plan for the blob side | Planning | Execution |
| --- | --- | --- | --- |
| `blob_storage_blobs` | `Append` over 64 partitions, 63 of them `never executed` | 3.85–4.70 ms | 0.45–0.72 ms |
| `blob_storage_blobs_by_namespace` | Single-partition `Index Only Scan`, `Heap Fetches: 0` | 0.26–0.37 ms | 0.11–0.17 ms |

A `namespace_id` literal prunes the shadow at plan time, and no digest literal exists to prune the base table. The first plan for the base table in a fresh backend costs 22.07 ms of planning and reads 5,738 planning buffers. The fan-out follows from `HASH(sha256)` over 64 partitions and from the absence of a digest, not from the fixture's row count. The unique constraint on `blob_storage_blobs [namespace_id, sha256]` does not change it: an index on a partitioned table is local to each partition, so it makes a partition cheaper to open without changing the size of the `Append`.

### Partition count rationale

All `HASH(namespace_id)` tables use 64 partitions, matching the 64 partitions chosen for `blob_storage_blobs` and `blob_storage_attachments` (`HASH(sha256)`). This count is informed by production data from the existing Container Registry and Package Registry databases.

The partition count is driven by the largest expected table (`container_blobs`), whose production analog already uses 64 partitions at comparable scale. Other format-specific tables are significantly smaller, making 64 partitions comfortable for all of them.

Key factors in this decision:

- **Skew tolerance**: `HASH(namespace_id)` does not guarantee uniform distribution. Namespace sizes are heavily skewed — a small number of large namespaces hold a disproportionate share of rows. With fewer partitions, large namespaces that hash to the same partition amplify the imbalance. At 64 partitions, even worst-case skew keeps partition sizes manageable.
- **Under-partitioning is expensive to fix**: Changing partition counts later requires a full table rebuild. Over-partitioning a small table has negligible overhead, while under-partitioning a large table creates real operational risk.
- **Partition-wise joins**: PostgreSQL can optimize JOINs between tables that share the same partition scheme (same key, same method, same count) by joining matching partitions directly. Since all `HASH(namespace_id)` tables use 64 partitions, this optimization is available. In practice, queries already include `namespace_id = ?` so the planner prunes to one partition per side, but partition-wise joins remain a free optimization.
- **Operational consistency**: A single partition count across all `namespace_id`-partitioned tables means all tables for a given `namespace_id` hash to the same partition number, simplifying maintenance scripts, monitoring, and bulk operations.

Which tables are partitioned is settled by the [Partitioning invariant](#partitioning-invariant), not enumerated here.

### Buffered and asynchronous writes

Several columns are updated on every download or upload request: the counter columns on `repositories` (`artifacts_count`, `downloads_count`, `size_bytes`), the per-package counters on `npm_packages` (`versions_count`, `tags_count`) used for entity-count limit checks, the `size_bytes` counter on the Maven and npm version tables (`maven_versions`, `maven_remote_versions`, `npm_versions`, `npm_remote_versions`), and the `last_downloaded_at` timestamps on `container_images`, `maven_packages`, `maven_versions`, `npm_packages`, and `npm_versions`. Writing these directly on the request path would serialize concurrent requests on the same row (hot-row contention on popular packages) and couple request latency to database write throughput.

To avoid this, these columns are maintained via buffered/async writes: request handlers record the update in a fast intermediate store (for example, Redis), and a background process periodically merges the buffered entries back into the row. This reuses the same pattern as GitLab's `ProjectStatistics`.

Columns maintained this way are flagged `buffered` in the schema diagrams.

#### Merge semantics

The merge strategy depends on the column type:

- **Counters** (`artifacts_count`, `downloads_count`, `size_bytes`, `versions_count`, `tags_count`): sum the buffered deltas into the existing value. Every increment must be preserved — losing an increment causes permanent under-counting. For the entity-count limit checks (`versions_count`, `tags_count`), a small over-cap at the boundary is acceptable: the limit is a product cap (not a data-integrity rule), drift is bounded by the buffer window, and the next flush re-syncs. Duplicate version names are blocked separately by the unique indexes on `npm_versions` and `npm_tags`, regardless of the counter.
- **Timestamps** (`last_downloaded_at`): take the maximum of the buffered values and the existing value (latest wins). Only the most recent download time matters; intermediate values can be discarded.

Both strategies share the same buffering infrastructure and differ only in how buffered entries are reduced before the write.

#### Trade-offs

- **Staleness**: buffered columns lag reality by up to one flush interval. This is acceptable for the current consumers — lifecycle rule evaluation (`keep_last_downloaded_at`) runs on schedules well above the flush interval, and landing page counters tolerate brief divergence. It is _not_ suitable for reads that must observe their own write synchronously, or for decisions that require exact ordering of download events.
- **Buffer loss**: if the buffer is lost before a flush, recent updates are dropped. For counters this is permanent under-counting; for timestamps the next download restores a correct (though slightly delayed) value.

### Namespace ID type

The decision below applies to the `id` of every table this ADR defines, not only to `namespaces.id`; the internal blob-storage tier is the one exception. The rationale is argued for `namespaces.id`, where the type choice has the widest consequences.

The type of the `namespaces.id` column cascades across the entire schema: every partitioned table carries `namespace_id` as its sharding key, and essentially every composite primary key, foreign key, and composite index on those tables includes this column. It leads the foreign keys and the composite indexes; in the composite primary keys it follows `id`, which [Mechanical consequences](#mechanical-consequences) states as `(id)` becoming `(id, namespace_id)`. Changing the type later would require a multi-phase migration across every partitioned table and every physical child relation — an irreversible decision in practice once the schema carries production data.

Three properties drive the choice:

1. **Global uniqueness across deployment models.** The Artifact Registry is designed to run as multiple independent deployments — GitLab.com, Dedicated, Self-Managed, per-Cell, and potentially as a standalone product independent of GitLab Rails (see [ADR-022](022_namespace_decoupling.md#consequences)). Sequential integer IDs drawn from a local sequence collide across deployments, foreclosing any scenario where namespace rows move between Artifact Registry instances (post-MVP migration tooling, Cell consolidation, cross-deployment references).
2. **Operational debuggability.** `namespace_id = 42` is ambiguous across deployments: the same integer can refer to unrelated namespaces on different Cells or installations. Support tickets, incident runbooks, and cross-deployment log correlation all benefit when the identifier is unique on sight.
3. **No coordination dependency for ID generation.** Allocating non-overlapping bigint ranges across deployments requires a central authority (the Topology service or equivalent). UUIDv7 generates locally on the database with no coordination.

#### Options

##### Option A: UUIDv7

`namespaces.id` is a `uuid` populated with a UUIDv7 value ([RFC 9562](https://datatracker.ietf.org/doc/rfc9562/)). Every `namespace_id` column throughout the schema is `uuid`. Generation can happen on the database side (PG18 native `uuidv7()`, or the [`pg_uuidv7`](https://pgxn.org/dist/pg_uuidv7/) extension on PG13–17) or on the application side with an RFC 9562–compliant library; the column type is the same in all cases and the path can change later without rewriting data — see the Decision section below for the full matrix.

**Positive**:

- Globally unique by construction across every Artifact Registry deployment — no coordination, no central allocator, no range management. Collisions are cryptographically improbable even across thousands of deployments generating simultaneously.
- Time-ordered: new IDs append to the right end of the B-tree within each partition. On a [PG18, 1M-row comparison by credativ](https://www.credativ.de/en/blog/postgresql-en/a-deeper-look-at-old-uuidv4-vs-new-uuidv7-in-postgresql-18/), UUIDv7 primary key indexes achieved ~90% leaf density (the default `fillfactor` that bigint sequences also achieve) with ~0% fragmentation, versus ~71% leaf density and ~50% fragmentation for UUIDv4 on the same workload.
- WAL volume is much closer to bigint than UUIDv4 is: UUIDv7's sequential-insert locality avoids the full-page-write amplification that random UUIDs suffer. Insert throughput matches bigint within a few percent on realistic multi-column schemas ([kkm-mako, PG18, 1M-row 13-column e-commerce table: bigint 76.5s vs UUIDv7 77.0s](https://kkm-mako.com/en/blog/articles/uuid-v4-v7-bigint-primary-key-design/); [Ardent Performance, PG17-dev, 20M-row table with 10 concurrent clients: bigint 3,480 tps vs UUIDv7 3,420 tps](https://ardentperf.com/2024/02/03/uuid-benchmark-war/)). On bare 2-column toy schemas the gap is more visible — [kkm-mako's minimal schema](https://kkm-mako.com/en/blog/articles/uuid-v4-v7-bigint-primary-key-design/) measured bigint 1.63s vs UUIDv7 2.16s (~32% slower) at the same row count, because the wider ID column is a larger fraction of the row. Absolute figures are workload-dependent.
- The embedded millisecond timestamp makes IDs BRIN-friendly and trivially extractable for diagnostics.
- Available on every PostgreSQL version the Artifact Registry might run against. PG18 ships `uuidv7()` natively (September 2025); on PG13–17 the [`pg_uuidv7` extension](https://pgxn.org/dist/pg_uuidv7/BENCHMARKS.html) provides `uuid_generate_v7()` with <2% overhead versus native per its published benchmarks; and any version supports application-side generation with an RFC 9562–compliant library.
- Structurally enables cross-deployment namespace portability. Post-MVP migration tools ([ADR-011](011_data_reconciliation.md)), Cell consolidation, and the standalone-product path from [ADR-022](022_namespace_decoupling.md) move a namespace row between Artifact Registry instances without rewriting `namespace_id` on every related row.

**Negative**:

- Storage: 16 bytes per value vs 8 bytes for bigint. `namespace_id` is the leading column of nearly every composite index on the partitioned tables, so the widening compounds across every physical child relation. [Jamauriceholt's 20M-row foreign-key index benchmark on PG 15.4](https://medium.com/@jamauriceholt.com/uuid-v7-vs-bigserial-i-ran-the-benchmarks-so-you-dont-have-to-44d97be6268c) measured 847 MB for UUIDv7 vs 423 MB for BIGSERIAL (~2×), and 1,847 buffer-write pages vs 847 (~2.2×) on a 10k-row bulk insert. The per-entry widening is ~8 bytes out of ~20 in the index tuple (~40%); observed total index size ranges from that per-entry floor to ~2× depending on how much of the index is the key vs. fixed overhead. At the Artifact Registry's multi-TB metadata scale this is a real but bounded cost, concentrated on `namespace_id`-leading indexes rather than on entire tables.
- Read latency on queries that materially depend on the key width can be measurably slower than with bigint. On a [synthetic 5M-user / 20M-order / 50M-audit_log schema (Jamauriceholt)](https://medium.com/@jamauriceholt.com/uuid-v7-vs-bigserial-i-ran-the-benchmarks-so-you-dont-have-to-44d97be6268c), 1-to-many JOINs ran ≈26× slower, single-row lookups ≈15× slower, and range/pagination ≈16× slower with UUIDv7 than with BIGSERIAL. Those numbers reflect worst-case synthetic queries and should not be extrapolated to this schema: every hot path is a single-partition `namespace_id = ?` indexed lookup on a composite key. Under those conditions the overhead is bounded by the per-page byte cost noted above and does not amplify into query-shape cost. If reviewers want a stronger empirical floor, a partition-local indexed-lookup benchmark on a representative row width on PG18 is the right thing to commission before merge.
- Time-ordering does not enable partition pruning on `HASH(namespace_id)` tables — hashing scatters values across partitions regardless of their timestamp component. Within-partition B-tree locality is preserved, which bigint sequences also provide at lower storage cost. UUIDv7's partition-pruning advantage only applies to `RANGE(uuid)` schemes, which are not used here.
- Client libraries, admin tooling, and API responses render 36-character strings instead of integers. Minor but pervasive; JSON response sizes grow for any endpoint carrying `namespace_id`.

##### Option B: Bigint with coordinated range allocation

`namespaces.id` stays `bigint DEFAULT nextval('namespaces_id_seq')`. Each Artifact Registry deployment is provisioned with a non-overlapping bigint range (for example, deployment X: 1 to 10^12, deployment Y: 10^12+1 to 2×10^12) by the Topology service, which the Artifact Registry already depends on for slug claiming (see [ADR-022](022_namespace_decoupling.md#cells-routing)).

**Positive**:

- Zero storage delta versus the current draft. No index, WAL, or JOIN cost to reason about.
- Reuses an existing dependency: the Topology service is already required for slug claiming.
- ID generation remains a sequence `nextval` — trivially fast, no extension required.
- Matches GitLab Rails' established pattern of coordinated bigint sequences across Cells ([Cells development guidelines](https://docs.gitlab.com/development/cells/)).

**Negative**:

- Cross-deployment namespace portability is not structurally supported. Moving a namespace from deployment X to deployment Y still requires rewriting every row's `namespace_id` if Y's allocated range does not contain the source ID.
- Range allocation adds a bootstrap step for every new Artifact Registry deployment and a governance model for range sizes and reclamation. A misallocation that lets ranges overlap is a global-uniqueness violation that is hard to detect early.
- A later decision to support cross-deployment portability would require the full bigint-to-UUID migration this ADR is trying to avoid.

##### Option C: Snowflake-packed bigint

Bit-pack 64 bits application-side: deployment ID (14 bits, 16K deployments) + timestamp (41 bits, 69 years from epoch) + per-backend sequence (9 bits, 512 IDs/ms/backend). Generated in the Go service with a small library.

**Positive**:

- Zero storage delta versus bigint. Same index, WAL, and JOIN profile.
- Self-identifying: deployment origin is extractable from any `namespace_id`.
- Time-ordered like UUIDv7, giving the same within-partition B-tree locality benefits.
- No extension dependency; ID generation is a handful of bit operations.

**Negative**:

- Custom generator maintained in the Go service instead of a PostgreSQL primitive. All writers must use the same library version and clock source.
- Clock-skew sensitive: per-deployment counters must survive clock rewinds and burst traffic. Requires monotonic-clock discipline and careful handling of the within-millisecond sequence counter.
- Widely used in industry (Twitter, Discord, Instagram 41+13+10 variant) but is not a PostgreSQL-native pattern — tooling, auditability, and cross-team familiarity are weaker than for UUIDs.
- The bit-field split is a one-time design decision. Too few deployment bits or too narrow a timestamp range would be hard to change later.
- Does not solve deployment-to-deployment migration: an ID generated on deployment X carries X's 14-bit prefix forever, so relocating a namespace to deployment Y still means either a rewrite or an ID that lies about its origin.

#### Decision

**Option A (UUIDv7) is chosen** for `namespaces.id` and, by consequence, for every `namespace_id` column across the schema and for the `id` of every API-exposed table (`repositories.id`, `container_images.id`, `maven_packages.id`, and so on). Those `id` columns are `uuid` with no server-side default: the application layer supplies the value on `INSERT`, so there is no sequence and no `GENERATED` column to reconcile under logical replication, and cross-deployment row re-insertion under namespace migration ([ADR-022](022_namespace_decoupling.md)) needs no sequence bookkeeping. The internal blob-storage tier (`blob_storage_attachments`, `blob_storage_blobs`, `upload_sessions`) keeps `bigint DEFAULT nextval('<table>_id_seq')`: those tables are never exposed through the API and carry the highest-volume rows, where the narrower key measurably reduces index size.

The decisive factors:

1. **The namespace is the unit of portability.** If any Artifact Registry identifier must survive movement between deployments, it is `namespace_id`. Everything below a namespace moves with it; everything above a namespace is expressed through the immutable slug and anchor tuple ([ADR-022](022_namespace_decoupling.md)).
2. **The cost is concentrated and bounded.** Widening `namespace_id` from 8 to 16 bytes hits the leading column of many indexes but does not double total storage — row widths on the large partitioned tables are dominated by other columns (repository/image/manifest IDs, timestamps, counters, and 32-byte `bytea` digests). Preliminary sizing puts the hit at tens of percent of total metadata storage, within the Artifact Registry's capacity envelope.
3. **The benefit is structural, not incremental.** Every post-MVP feature that touches cross-deployment movement (migration tooling in [ADR-011](011_data_reconciliation.md), Cell consolidation, standalone-product packaging per [ADR-022](022_namespace_decoupling.md)) becomes meaningfully simpler when `namespace_id` is globally unique by construction, and the absence of an allocator removes a coordination dependency.
4. **The storage cost is paid once, at insert time, on a schema that is still empty.** Option B would require an irreversible migration across every partitioned table if the deployment model later demands global uniqueness. We accept a known, bounded cost today to avoid an unbounded migration risk later.
5. **UUIDv7 preserves the hot-path performance profile.** Single-partition `namespace_id = ?` lookups remain single-partition. Within-partition B-tree locality that bigint provides is also provided by UUIDv7's time-ordered prefix. The only properties lost (partition pruning by UUID range, 8-byte index leading column) are either non-applicable to `HASH` partitioning or bounded in cost.

**Implementation notes**:

- Three viable generation paths exist; the choice depends on the PostgreSQL version available at deployment time and is independent of the column type:
  - **PG18+ native**: column default `DEFAULT uuidv7()`. No extension required.
  - **PG13–17 with the [`pg_uuidv7`](https://pgxn.org/dist/pg_uuidv7/) extension**: column default `DEFAULT uuid_generate_v7()`. Note the function-name difference from the native path; migrations and schema dumps must reference the right name for the target environment.
  - **Application-side generation**: any PostgreSQL version, no extension required. The Go service generates the value with an [RFC 9562](https://datatracker.ietf.org/doc/rfc9562/)–compliant library and supplies it on `INSERT`.
- Switching between these paths later is metadata-only (`ALTER COLUMN SET DEFAULT`) and does not rewrite data, provided every generator emits RFC 9562–compliant UUIDv7 values. This makes the initial path a runtime/operational choice rather than a schema commitment.
- That compliance is enforced by the database, not assumed of the generator. Every table whose `id` is a `uuid` with no server-side default carries a version check on that column, `CHECK ((get_byte(uuid_send(id), 6) >> 4) = 7)`. `uuid_send` returns the value's 16 raw bytes and byte 6's high nibble is the RFC 9562 version field; both functions are immutable, which is what lets the expression stand in a `CHECK`. A value from a path that emits anything other than UUIDv7 is refused on write instead of discovered later, and so are the all-zero UUID that an `INSERT` which never assigned the field would otherwise store and a version-4 value from a stray `uuid.New()`. Those last two would each read as a legitimate primary key while sorting outside the time-ordered range every other row occupies.
- The check has no `uuid` `id` to bound on the remaining tables, which therefore do not carry it: the blob-storage tier, the three Artifact Registry tables keyed without an `id` column (`repository_collection_repositories`, `namespace_statistics`, and the `blob_storage_blobs_by_namespace` shadow, keyed `(namespace_id, sha256)`), and the library-owned schema-migration and job-queue tables, `goose_db_version` and the `river_*` tables, whose key shapes this schema does not set.
- Adding the version check to a table that already holds rows is a different operation from adding it to an empty one: `ADD CONSTRAINT ... NOT VALID` first, then a separate `VALIDATE`, and one table per migration rather than every table in one transaction, because a `CHECK` on a partitioned parent takes `ACCESS EXCLUSIVE` on the parent and on all 64 of its partitions.
- **Open question (resolve closer to GA)**: which initial path to take depends on the PostgreSQL version available across `.com`, Dedicated, and Self-Managed at GA. If PG18 cannot be guaranteed across all install types, application-side generation is the safest interim choice; the column default can move to native `uuidv7()` once PG18 is the floor everywhere.
- All mermaid diagrams in this ADR show `uuid` for `namespace_id` columns and for the `id` of every API-exposed table. Only the blob-storage tier (`blob_storage_attachments`, `blob_storage_blobs`, `upload_sessions`) keeps a `bigint` `id`.
- Monotonicity of UUIDv7 is strict within a single backend (database side) or process (application side) within the same millisecond, not across backends or processes. This is sufficient for index locality and debuggability; no hot-path logic assumes strict global ordering across connections.
- The slug-to-`namespace_id` lookup cache (see [ADR-022](022_namespace_decoupling.md#request-flow)) is unaffected: it keys on the immutable slug.
- The composite primary key pattern used on partitioned tables (for example, `(id, namespace_id)` on `upload_sessions`, required by PostgreSQL's partitioned-table constraint rules) still holds. The `namespace_id` component is `uuid`; the `id` component is `uuid` on every table except the blob-storage tier, where it is `bigint` (for example, `upload_sessions`).

### Partition schema organization

With 64 HASH partitions per partitioned table and a partition set that grows as mid-tier tables are partitioned later, child relations outnumber logical tables by a wide margin. Where these children live — alongside their parents in `public`, or in a dedicated namespace — shapes schema legibility, tooling alignment, and the migration tooling we build around partitioned tables.

#### Option A: Dedicated schema for partition children

Parent tables live in `public` and all partition children live in a dedicated `partitions` schema. Partition DDL explicitly targets the partition schema on every `CREATE TABLE ... PARTITION OF` — PostgreSQL otherwise places the child in the parent's schema.

**Positive**:

- Catalog legibility: `\dt public.*`, `information_schema`, ER diagrams, and IDE schema views show only the logical tables instead of every partition child. Schema reviews, onboarding, and DB console work operate at the abstraction engineers actually reason about.
- Application layer is unaffected: applications query through parent tables in `public` and never reference the `partitions` schema. Only migration tooling targets child partitions, using explicit `partitions.<name>` qualification.
- Clean scoping for partition-lifecycle operations: permissions, `pg_dump -n`, logical replication publications, and monitoring exporters target a single namespace instead of table-name patterns.
- Discourages accidental partition-level queries: reaching a specific child requires `partitions.<name>`, making it harder to bypass the partition abstraction.

**Negative**:

- Postgres defaults work against the convention: `CREATE TABLE ... PARTITION OF parent` places the child in the parent's schema unless explicitly overridden, so enforcement lives in migration tooling, linters, or CI — not in the database itself.
- Partitioning helpers must route child creation to the partition schema, and service bootstrap must provision the schema and its grants before migrations run ([ADR-006](006_technology_stack.md)).
- No runtime benefit. Pruning, locking, VACUUM, and query performance are unchanged; the case is entirely organizational.

#### Option B: All tables in `public`

Parents and their child partitions live together in the default schema — PostgreSQL's out-of-the-box behavior with no extra configuration.

**Positive**:

- Simplest bootstrap: no extra schema, no grants split, no partition-routing helper in migration tooling. Local dev, CI, and migrations work with no setup.
- Matches Postgres defaults and third-party tool assumptions (introspection, ORMs, query analyzers), avoiding per-tool configuration.

**Negative**:

- Catalog clutter: every partition child shares the namespace with the logical tables and quickly dominates any `\dt`, `information_schema` query, or ER diagram. The problem compounds as new tables are partitioned.
- No schema-level scoping for partition-lifecycle tooling: `pg_dump`, logical replication, and monitoring must be expressed as table-name patterns (`blob_storage_blobs_*`, `*_files_*`, and so on).
- Partition-level queries (for example, `SELECT FROM blob_storage_blobs_37`) are indistinguishable from normal table references, making it easier to bypass the partition abstraction.

#### Decision

**Option A (dedicated `partitions` schema) is chosen.**

The decisive factor is the distinction between application-facing tables and partitioning internals. Logical tables are the surface area applications read and write through; partition children are internal to the partitioning mechanism and should only be touched by partition-lifecycle tooling. Keeping both in a single schema blurs that boundary — schema introspection, grants, and operational tooling all have to filter by name to tell them apart. A dedicated `partitions` schema makes the distinction structural in the database itself: partition-lifecycle operations scope to one namespace, and anything reading `public` sees only the surface area applications are meant to touch.

The legibility argument reinforces the choice: partition children outnumber logical tables by a wide margin from the first deployment and the gap widens as more tables are partitioned, so the single-schema layout would be awkward from the first deployment and worse over time. The bootstrap cost (partition-routing helper in migration tooling, schema creation at startup) is one-time and amortizes across all satellite services adopting the same migration abstraction ([ADR-006](006_technology_stack.md)).

The pattern is validated at scale: GitLab Rails organizes its partition children in dedicated [`gitlab_partitions_static` and `gitlab_partitions_dynamic`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/lib/gitlab/database.rb) schemas.

Only partition children move to the dedicated schema; parent tables and tables without explicit partitioning remain in `public`.

### Cleanup tasks

To understand the above approach, it is important to understand the challenges of the blob storage part when it comes to cleanup.

On one side, we can have one or many attachments that are deleted as part of parent objects being destroyed (a package being destroyed or a cleanup policy being executed and removing hundreds of files).

On the other side, we can't simply remove records from the blobs table as they reference a file on object storage. As such, we need a cleanup task that will take the blob record, remove it, and also remove the file on object storage. This can't be done by the database. We need a callback that will be implemented as a background process.

Before handling a blob for destruction, the backend needs to make sure that it's not used anymore by any part (due to deduplication). That's where the attachments table fills a crucial role: it records the usage of a given blob. The cleanup task can simply ask if a `(namespace_id, sha256)` pair is still present in the attachments table (see [orphan check query](#blob-storage-query-examples)). If that's a no, then the blob is clear to be removed.

This approach keeps the cleanup contract simple for engineers working on each blob storage client. When deleting artifact records (single file, bulk destruction, or cleanup policy execution), the application must also delete the corresponding `blob_storage_attachments` record(s) in the same transaction. This is the only cleanup responsibility at the client level — no object storage interaction is needed. From that point, the blob storage background process takes over: it identifies `blob_storage_blobs` rows with no remaining attachments (orphan check) and removes both the database record and the object storage file.

Upload session cleanup follows a similar pattern. The `upload_sessions` table uses a binary existence model — if the row exists, the upload is in progress or requires cleanup — so expired sessions (where `expires_at < NOW()`) are candidates for purging. The purger deletes the temporary storage object and removes the row. The table provides all information needed to identify candidates and derive the storage path (`uploads/{upload_id}` under the namespace partition), without enumerating objects in storage. See [ADR-011](011_data_reconciliation.md) for the shipping timeline of upload purging.

This blueprint establishes the high-level database primitives (attachment tracking, blob storage organization, upload session tracking) that can enable cleanup processes, but the specific implementation details (triggers, background job logic, performance analysis) are left for later detailed specification work.

### Storage usage calculation

Storage usage is tracked at three scopes: namespace, repository, and artifact. Each scope has a pre-computed counter that serves the display path with sub-millisecond reads, and a reconciliation path that computes the exact value from source data when drift is suspected or on-demand verification is needed. The blob storage schema is designed to make these calculations and attribution both accurate and efficient:

- Blobs and attachments are scoped to an Organization, and deduplication happens **within** an Organization only (see [ADR-002](002_storage_deduplication_scope.md)).
- `blob_storage_blobs` has **one row per unique stored blob per Organization**: each physical object in object storage is represented once per Organization.
- Physical blobs and `blob_storage_blobs` records are cleaned up asynchronously when they lose all attachments (through the [cleanup process](#cleanup-tasks)), so `blob_storage_blobs` only references blobs that are still in use (or pending async deletion). As a result, storage usage queries do not need to filter by attachment counts.

Thus, calculating storage usage for a given Organization is a matter of summing the size of its blobs listed in `blob_storage_blobs`. This is distinct from the per-manifest `container_manifests.size` (see [Container Repositories](#container-repositories)): the latter answers "how big is this manifest tree" and may double-count blobs shared across manifests or across children of a manifest list, so it is not a substitute for Organization-level usage.

A separate ADR will describe storage usage calculation and attribution in more detail. This ADR defines the database primitives that facilitate those calculations.

```mermaid
erDiagram
    namespaces ||--|| namespace_statistics : "has one"

    namespace_statistics {
        uuid namespace_id PK,FK "NOT NULL, references namespaces(id) ON DELETE CASCADE"
        bigint deduplicated_size_bytes "NOT NULL, DEFAULT 0, buffered counter"
        bigint components_count "NOT NULL, DEFAULT 0, buffered counter"
        timestamptz last_reconciled_at "NOT NULL, DEFAULT 'epoch', reconciliation bookkeeping"
    }
```

- **namespace_statistics**: Stores pre-computed namespace-level counters, maintained via buffered counters (async flusher). This is the table that the display path and billing system read from, delivering sub-millisecond responses (see [benchmark table](#namespace-level-storage-accounting-reconciliation)). The [reconciliation mechanisms](#namespace-level-storage-accounting-reconciliation) exist to verify and correct these counters when drift is suspected. One row exists per namespace by construction: a seed covers every namespace present when the table is created, and an `AFTER INSERT` trigger on `namespaces` creates one for every namespace inserted afterwards, so no read path has to distinguish a missing row from zeroed counters. The `namespace_id` foreign key is one of the two `references namespaces(id)` in this schema carrying `ON DELETE CASCADE` — the other is the [`blob_storage_blobs_by_namespace`](#namespace-level-storage-accounting-reconciliation) shadow table's, on the same side of the same rule — and here it is the referential action the trigger forces: the trigger guarantees a child row for every namespace, so without the cascade a namespace hard-delete would be rejected by a row the namespace itself caused to exist. The row is derived bookkeeping rather than user data, which puts it on the cascade side of the rule stated for [repositories](#repositories) — cascade where the children are pure structure, reject where they are user data. Its primary key is exactly `(namespace_id)`, with no separate `id` column, and no foreign key in this schema references it, so it is not partitioned under the second condition in [Exceptions](#exceptions) to the [Partitioning invariant](#partitioning-invariant) — and it is the only table that takes it.
  - `deduplicated_size_bytes`: total storage used by the namespace, with blob deduplication already applied (see [ADR-002](002_storage_deduplication_scope.md)). The column is named this way (rather than `size_bytes`) to be forward-compatible, distinguishing it from any future raw or logical size metrics.
  - `components_count`: total number of artifact versions stored in the namespace's hosted and remote repositories:
    - Container: `container_manifests` + `container_remote_manifests`.
    - Maven: `maven_versions` + `maven_remote_versions`.
    - npm: `npm_versions` + `npm_remote_versions`.

    Soft-deleted rows continue to count until garbage collection hard-deletes them after the [soft-delete window](010_data_retention.md#soft-delete) expires. This matches `deduplicated_size_bytes`, which keeps the bytes of soft-deleted artifacts until garbage collection reclaims the underlying blobs. Virtual repositories are not counted separately because they have no version tables of their own. A virtual repository resolves requests through an ordered list of upstreams (see [`container_virtual_repository_upstreams`](#virtual-container-repositories) and its Maven and npm equivalents), and each upstream is itself a hosted or remote repository whose versions are already included via the tables above. Counting the virtual repository on top would double-count its upstreams. This is the namespace-level dimension for consumption-based pricing and metering, complementing `deduplicated_size_bytes`. Surfaced on the namespace overview alongside storage usage.

  - `last_reconciled_at`: the wall-clock time the namespace last completed a full reconciliation pass, stamped only on full success. It is bookkeeping, not a counter and not a billing input: it drives catch-up candidate selection and the staleness scan, and is never surfaced through the API. The `'epoch'` default (1970-01-01) makes a freshly seeded row sort as the stalest row in the table, so it is always selected until its first successful pass stamps a real time, and it means no row ever holds NULL for this column. `'-infinity'` states that intent more plainly and was the first choice, but it is not readable back: no `time.Time` can hold it, so a generated model that types this column `time.Time` fails to scan any row still carrying the default — which is every row until its first pass — and every read of the table would have to either project the column out or carry it in a type that models infinity. A sentinel that makes the rows it marks unreadable through the ordinary model is the wrong trade for a bookkeeping column. `'epoch'` costs the guarantee that no real pass could ever stamp the sentinel value, which is accepted: a pass stamping 1970-01-01 requires a system clock wrong by decades, and the column is bookkeeping that drives candidate selection only — never a billing input, never surfaced through the API — so a misread would delay or repeat a reconciliation pass, not corrupt a counter.

#### Namespace-level storage accounting reconciliation

The `namespace_statistics.deduplicated_size_bytes` counter and repository-level `repositories.size_bytes` counter serve the display path with sub-millisecond reads. However, two reconciliation scenarios require computing exact storage from source data rather than the cached counter:

1. **On-demand verification**: A customer asks "is my billing accurate?" and we need to compute the exact namespace storage from source data. This means `SUM(size) FROM blob_storage_blobs WHERE namespace_id = ?` across all 64 `sha256`-partitions.
2. **Drift correction**: A failed GC run, partial flush, or other event desynchronizes the cached counters, and we need to recompute the exact value to correct it.

Because `blob_storage_blobs` is partitioned by `HASH(sha256)`, any `namespace_id`-only query fans out to all 64 partitions. [Benchmarks](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18456#note_3166018048) on a CloudSQL PostgreSQL 18 instance ([seeded](https://gitlab.com/jdrpereira/artifact-registry-poc/-/tree/main/cmd/seed) dataset: ~1.6M blobs across 64 `sha256`-partitions, 500K namespaces with Zipf-distributed blob ownership, blob-heaviest namespace at 353K blobs) show the baseline at 78 ms and ~3K+ buffer hits for the heaviest namespace. Two additive insurance policies can improve this:

**Option A — Covering index on `blob_storage_blobs`**: Add `INCLUDE (size)` to the existing `namespace_id` index on each partition. This turns the 64-partition fan-out into 64 index-only scans with minimal or no heap fetches. Space overhead is negligible (only the `size` column is added to the existing index leaf pages).

**Option B — Namespace-partitioned shadow table**: A dedicated `blob_storage_blobs_by_namespace` table partitioned by `HASH(namespace_id)` with 64 partitions, maintained via `AFTER INSERT`/`DELETE` triggers on `blob_storage_blobs`. This collapses the reconciliation query to a single-partition index-only scan. Space overhead is moderate (duplicates a minimal subset of blob data — `namespace_id`, `sha256`, `size` — across 64 new partitions plus indexes, growing linearly with blob count). The tradeoff is write amplification on every blob `INSERT`/`DELETE`, but it keeps the reconciliation load away from the main `blob_storage_blobs` table (hot path).

```mermaid
erDiagram
    blob_storage_blobs_by_namespace {
        uuid namespace_id PK,FK "NOT NULL, PK with sha256, references namespaces(id) ON DELETE CASCADE"
        bytea sha256 PK "NOT NULL, PK with namespace_id"
        bigint size "NOT NULL, INCLUDEd in both indexes"
    }
```

Triggers on `blob_storage_blobs` maintain this table: `AFTER INSERT` copies `(namespace_id, sha256, size)` into the shadow table; `AFTER DELETE` removes the matching row. No `AFTER UPDATE` trigger is needed because `blob_storage_blobs` rows are immutable — content-addressable storage means any change to the content produces a new `sha256` and thus a new row (see [ADR-008](008_content_addressable_storage.md)). The primary key `(namespace_id, sha256) INCLUDE (size)` must include the partition key (`namespace_id`) and mirrors the unique key on `blob_storage_blobs`; `size` rides in it so that a lookup by digest is index-only instead of costing a heap fetch per matched row. The table uses the same 64-partition count as other `HASH(namespace_id)` tables. Covering index on `(namespace_id) INCLUDE (size)` enables index-only scans for the whole-namespace sum. The primary key can satisfy that sum index-only as well, since `namespace_id` leads it, so the covering index is kept for scan cost rather than capability: its entries omit the 32-byte `sha256` the sum never reads, which is most of the width the wider index would make it walk.

The `namespace_id` foreign key references `namespaces(id)` with `ON DELETE CASCADE`, which puts it on the cascade side of the rule stated for [repositories](#repositories) for the same reason `namespace_statistics` is there: a shadow row is a derived copy of a `blob_storage_blobs` row, not user data.
A shadow row's lifetime is bounded by the shorter of two, and two reapers enforce it: the `AFTER DELETE` trigger removes the row when garbage collection reclaims its `blob_storage_blobs` row, and this cascade removes it when the namespace goes.
Whichever fires first is correct, because a shadow row exists only to make a per-namespace read cheap, and both events end the possibility of that read.
That the shadow and its source do not share a lifetime is the design rather than a divergence the design tolerates: the shadow is a read accelerator derived from `blob_storage_blobs`, not a replica of it.

`blob_storage_blobs` deliberately carries no `namespaces(id)` reference, and the absence is a decision rather than an unfinished deferral.
The row owns `object_storage_key`, the only handle to the stored object, and [ADR-025](025_garbage_collection.md) has garbage collection delete that object before the row it came from; a cascade from `namespaces` would therefore destroy the handle while the object was still live, leaking it with nothing left in the database that knows it exists.
A blocking reference is no better, because it would stall every namespace deletion behind a garbage-collection cycle that is deliberately deferred and rate-limited.
The migration that created the table, `20260612130000_create_blob_storage_blobs.sql`, describes both its missing references as deferred to a follow-up migration; for the `namespaces(id)` half that framing is superseded, and the `repositories(id, namespace_id)` half is a separate question this section takes no position on.

A namespace hard-delete therefore removes the shadow's rows and leaves the `blob_storage_blobs` rows they copy, until garbage collection reclaims those on its own schedule.
No reader of the shadow observes the gap: `repositories` and `blob_storage_attachments` reference `namespaces` without a referential action, so the delete cannot proceed until every repository and attachment under the namespace is gone, and the `namespace_statistics` row that would drive a reconciliation pass cascades away in the same statement.

| Approach | Timing | Buffers | Partitions scanned | Write overhead |
| --- | --- | --- | --- | --- |
| `namespace_statistics` counter (display path) | 0.013 ms | 1 | 0 | Async flusher |
| Shadow table + covering index (Option B) | 29 ms | 1,361 | 1 | Triggers |
| Covering index on blobs (Option A) | 43 ms | 1,599 | 64 | None |
| Baseline (no changes) | 78 ms | ~3K+ | 64 | None |

Both options are purely additive — no changes to `blob_storage_blobs` itself — and can be added or removed independently. They are not mutually exclusive; both are included in the initial schema. It is easier to start with more coverage and drop indexes or auxiliary tables later once production metrics confirm they are not needed.

#### Namespace-level component count reconciliation

The `namespace_statistics.components_count` counter serves the display path and metering pipeline. As with the storage counter, two scenarios call for recomputing the exact value from source data:

1. **On-demand verification**: A customer (or billing) asks whether the component count is accurate, and we need to derive it from source rows.
2. **Drift correction**: A failed flush, partial buffer loss, or background-job bug desynchronizes the counter and we need to recompute it.

Reconciliation sums six independent counts scoped to a namespace's rows: three hosted (`container_manifests`, `maven_versions`, `npm_versions`) and three remote (`container_remote_manifests`, `maven_remote_versions`, `npm_remote_versions`).
Soft-deleted rows are included so the recomputed value matches what `components_count` tracks (insert increments, garbage-collection hard-delete decrements; soft-delete and restore are no-ops).
The "garbage-collection hard-delete" in that parenthetical covers any hard delete of a counted row, whichever path performs it, and two paths perform it.
A format's own delete removes the row in its own transaction, and the lifecycle purger removes a row that no such route can address.

```sql
SELECT
  (SELECT COUNT(*) FROM container_manifests        WHERE namespace_id = $1)
+ (SELECT COUNT(*) FROM container_remote_manifests WHERE namespace_id = $1)
+ (SELECT COUNT(*) FROM maven_versions             WHERE namespace_id = $1)
+ (SELECT COUNT(*) FROM maven_remote_versions      WHERE namespace_id = $1)
+ (SELECT COUNT(*) FROM npm_versions               WHERE namespace_id = $1)
+ (SELECT COUNT(*) FROM npm_remote_versions        WHERE namespace_id = $1)
  AS components_count;
```

Each subquery is a count by `namespace_id` on a single source table, with no `soft_deleted_at` predicate so the rows still in the table (live plus soft-deleted within the [soft-delete window](010_data_retention.md#soft-delete)) match what `components_count` tracks. All six source tables are partitioned by `HASH(namespace_id)`, so every subquery prunes to a single partition and scans that partition for the namespace's rows. The existing partial unique indexes (`WHERE soft_deleted_at IS NULL`) cover only live rows, so they cannot satisfy the count directly. Per-namespace cardinality is bounded by the data model (one row per version, not per file or blob reference) and reconciliation is infrequent (on-demand or drift correction, not a hot path), so the bounded scan is acceptable. No additional insurance policies (covering indexes or shadow tables) are introduced. If production metrics ever show this is too slow, a non-partial `(namespace_id)` index on each source table is the cheapest next step before considering a shadow table.

#### Repository-level storage accounting reconciliation

The `repositories.size_bytes` counter is maintained via [buffered/async writes](#buffered-and-asynchronous-writes) and serves the landing page hybrid list with sub-millisecond reads. As with the namespace-level counter, two scenarios call for recomputing the exact value from source data:

1. **On-demand verification**: A user asks "how much storage does this repository really use?" and we need to derive the exact value from source rows.
2. **Drift correction**: A failed flush, partial buffer loss, or background-job bug desynchronizes the counter and we need to recompute it.

Reconciliation branches on `(repositories.format, repositories.kind)` because each combination reaches blob storage through a different chain of tables. For each format, the query collects every blob `sha256` referenced from artifacts in the repository, applies `DISTINCT` for intra-repository deduplication, and joins to `blob_storage_blobs_by_namespace` for the size. The query filters the mid-tier tables by their `*_repository_id` columns, which reference the format-specific stub table's own `id`, not `repositories.id`. The example queries below resolve the stub `id` from `repositories.id` via a small CTE, so they can be invoked with the parent identifier.

- **Container**: `container_images` (filtered by `container_repository_id`) → `container_blobs` and `container_manifests`. Both tables carry `blob_sha256`; the union covers layer blobs and manifest payloads.
- **Maven**: `maven_packages` (filtered by `maven_repository_id`) → `maven_files`. The single file table covers a package's version-specific and package-level files.
- **npm**: `npm_packages` (filtered by `npm_repository_id`) → `npm_versions` → `npm_files`, with a union against `npm_metadata_files` (which is keyed at the package, not the version, level).
- **Remote variants** (`kind = remote`) follow the same shape against the cache tables (`*_remote_*`). The cache is part of the repository's footprint.

`SUM(DISTINCT bsb.size)` would be incorrect: different blobs can share a `size` value (small files of identical length collapse). Reconciliation must `SELECT DISTINCT blob_sha256` first and only then join to `blob_storage_blobs_by_namespace` for the sum. The sizes come from the namespace shadow table rather than `blob_storage_blobs` itself: the shadow is keyed `(namespace_id, sha256) INCLUDE (size)`, so each digest resolves index-only inside one partition — `namespace_id` is a literal here, which prunes to a single partition, and `size` rides in the primary key, so no heap fetch follows. The shadow's other index, the covering `(namespace_id) INCLUDE (size)`, does not serve this read: it cannot locate a row by `sha256`. Every `sha256` reachable from a repository is by construction present for that repository's namespace. The example queries below all resolve sizes this way.

Soft-deleted rows are included so the recomputed value matches what `repositories.size_bytes` tracks.
The counter is deduplicated within the repository (matching the `DISTINCT blob_sha256` in reconciliation): it increments only when a `sha256` first becomes attached in the repository and decrements when the last attachment of that `sha256` leaves the repository, and two paths remove it.
A format's own delete removes the attachment in its own transaction.
An attachment under a soft-deleted artifact is not addressable from that route, and the lifecycle purger removes it instead.
Neither path waits for a garbage-collection pass: garbage collection reclaims the blob and decrements the namespace-scoped `deduplicated_size_bytes`, a counter at a different scope.
Soft-delete and restore are no-ops, matching the namespace-level behavior described above.

Reconciliation cost is bounded by the partition the namespace hashes to, not by the repository's artifact count. The format-specific file, blob, and manifest tables (`container_blobs` and `container_manifests` for container, `maven_files` for Maven, `npm_files` and `npm_metadata_files` for npm, plus their `*_remote_*` cache variants) are partitioned by `HASH(namespace_id)` with 64 partitions, so each side of the walk prunes to a single partition. Inside that partition the planner takes the sequential path: the repository predicate sits on the format-specific stub table, two join levels above the blob-bearing table, and PostgreSQL keeps no cross-table correlation statistics for that path, so the walk is planned at 30,000 rows where 200 exist. Measured on PostgreSQL 17.10 over eleven `EXPLAIN (ANALYZE, BUFFERS)` plans ([artifact-registry!1712](https://gitlab.com/gitlab-org/ops/artifact-registry/-/merge_requests/1712)), on the container walk, with the repository held at 200 digests:

| What else sits in the collecting table's partition | Plan for the walk | Timing |
| --- | --- | --- |
| Nothing; the addressed repository's rows are the only ones | Nested loop, `Index Only Scan` on `blob_storage_blobs_by_namespace` | 0.508 ms |
| A sibling repository of the same namespace, 59,800 rows | `Seq Scan` with `Filter: (namespace_id = ...)` on the collecting table and the shadow | 18.157 ms |

A hash partition holds rows from roughly 1/64 of all namespaces, so the sequential pass is a fleet-scale quantity rather than a namespace-scale one; that last step is inferred from the node type and the partition count rather than measured. The format-specific indexes on those tables are not uniformly partial: `npm_metadata_files` and `npm_remote_metadata_files` carry no `soft_deleted_at` column at all; on `container_blobs` and `container_manifests` the column this document specifies arrives with soft delete at GA ([ADR-010](010_data_retention.md#release-phasing)), so their unique indexes carry no predicate today and the soft-delete-inclusive framing does not reach them. `npm_files`, `npm_remote_files`, `container_remote_blobs`, and `container_remote_manifests` are partial on exactly `soft_deleted_at IS NULL`, and the `maven_files` and `maven_remote_files` unique indexes add a second conjunct on the version id (`maven_version_id IS NULL` for the package-level index and `IS NOT NULL` for the version-level one, with the same pair on `maven_remote_version_id`). A repository-proportional cost is therefore reachable rather than excluded, and what holds the walk to the sequential path is the row estimate, not a missing or partial index. Reconciliation is infrequent (on-demand or drift correction, not a hot path), so the partition scan is acceptable. The final `blob_storage_blobs_by_namespace` lookup from [namespace-level reconciliation](#namespace-level-storage-accounting-reconciliation) prunes to a single partition in every measured plan and resolves index-only when the planner sizes the walk correctly, and falls to a sequential scan of that partition under the same over-estimate.

Repository-level reconciliation now carries one insurance structure: `index_maven_files_on_ns_id_pkg_id_blob_sha256`, a non-partial index on `maven_files (namespace_id, maven_package_id, blob_sha256)`. It arrived to serve the `maven_package_id` foreign-key check, and its third column is the digest `recomputeMavenFilesSizeStmt` reads; the measured freed-bytes cell drops from 1,001,427 buffers and 3,066 ms to 318 buffers and 1.8 ms under it. Every table in these chains therefore carries a non-partial index that leads with `(namespace_id, <its parent id>)`, `maven_files` included. [artifact-registry#684](https://gitlab.com/gitlab-org/ops/artifact-registry/-/work_items/684) proposed the two-column `(namespace_id, maven_package_id)` form; the shipped three-column form is the decision, the third column being what the join reads. Beyond that index, the walk reuses the `blob_storage_blobs_by_namespace` shadow that [namespace-level reconciliation](#namespace-level-storage-accounting-reconciliation) already introduces and adds no shadow table of its own. A repository-partitioned shadow table mapping `(namespace_id, repository_id, sha256, size)`, maintained from the format-specific tables at attach/detach time, would mirror the [Option B](#namespace-level-storage-accounting-reconciliation) shape at a finer scope.

#### Artifact-level storage accounting

Artifact-level storage usage is the byte footprint of a single artifact version (a container manifest, a Maven version, an npm version). It powers per-artifact UI displays (for example, "this image is 142 MB", "this package version is 4 MB") and is consumed by [lifecycle rules](010_data_retention.md) and reporting queries that filter or sort by size.

The accounting model differs by format because the underlying artifact shape differs:

- **Container manifests**: `container_manifests.size` is pre-computed at push time and is immutable. A manifest is content-addressed ([ADR-008](008_content_addressable_storage.md)), so any change to its bytes produces a new manifest with a new digest and a new `size`. The column is the source of truth, so no reconciliation is needed. The remote cache mirrors this with `container_remote_manifests.size`, which has [progressive semantics](#container-remote-repositories) for manifest lists whose children are cached lazily.
- **Maven and npm versions**: each version row carries a pre-computed `size_bytes` column (on `maven_versions`, `maven_remote_versions`, `npm_versions`, and `npm_remote_versions`) that is the source of truth for the version's footprint.
  Unlike `container_manifests.size`, it cannot be set immutably at push time: Maven and npm versions are not content-addressed at the version level, and files can be added or removed over a version's lifetime.
  It is therefore maintained as a buffered counter via [buffered/async writes](#buffered-and-asynchronous-writes), like `repositories.size_bytes`: it increments when a `blob_sha256` first becomes attached to the version and decrements when the last attachment of that `sha256` leaves the version (deduplicated within the version, matching the `DISTINCT blob_sha256` used in reconciliation), and two paths remove it.
  A format's own file delete removes the row in its own transaction and recomputes the column there, and the lifecycle purger removes a file that no such route can address.
  Neither path waits for a garbage-collection pass.
  The display path and the version list read the indexed column directly, including when sorting or filtering by size.

Soft-deleted files continue to contribute to the per-version `size_bytes` until garbage collection hard-deletes them; soft-delete and restore are no-ops for the counter, matching the namespace and repository semantics.
The hard delete is what ends the contribution, and two paths perform it.
A Maven or npm file delete removes the row in its own transaction and recomputes the version's `size_bytes` there.
A file under a soft-deleted version is not addressable from those routes, and the lifecycle purger removes it instead.
The purger removes the version row in the same reap, so the counter goes with its row rather than being recomputed.
Neither path waits for a garbage-collection pass: garbage collection reclaims the blob and decrements `deduplicated_size_bytes`, a counter at a different scope.

Precomputing the column, rather than deriving it at read time, is what lets the version list sort and filter by size. Deriving a single version's size is cheap either way (a bounded few-file join), but once size becomes a sortable or filterable column on the version list, deriving it for every row no longer scales. Validated on a Cloud SQL PostgreSQL 17 instance (`large` profile, ~26K Maven and ~26K npm versions in the deepest namespace):

| Top 50 versions by size | Maven | npm |
| --- | --- | --- |
| derive at read (sum each version's blobs) | 58 ms | 29 ms |
| pre-computed `size_bytes` column + index | 0.06 ms | 0.08 ms |

That is three to four orders of magnitude, the deduplicated derive-at-read variant is slower still (~190 ms for Maven), and the gap widens with version count. Since the landing page already sorts repositories by `size_bytes`, the same expectation applies to the version list, so the column is precomputed for parity across scopes.

#### Artifact-level storage accounting reconciliation

`container_manifests.size` is immutable and content-addressed, so it needs no reconciliation. The Maven and npm `size_bytes` counters, like the repository- and namespace-level counters, can drift from a failed flush, partial buffer loss, or background-job bug, so the exact value is recomputed from source data for on-demand verification or drift correction.

Reconciliation for one version selects the version's distinct `blob_sha256` values from the format-specific file table, scoped to a single `maven_version_id` or `npm_version_id`, and resolves each digest's size against `blob_storage_blobs_by_namespace`, the same shadow the namespace- and repository-level walks read. Soft-deleted files are included so the recomputed value matches what the counter tracks, and package-level rows are excluded by the version-id equality.

A per-version walk holds its digests before it reads any size, so the pruning rationale that sends the namespace- and repository-level walks to the shadow (reads that cannot name their digests up front) does not apply at this scope, and a base-table read is the alternative to weigh. Binding the digest set as a single `bytea[]` array parameter (`blob_storage_blobs.sha256 = ANY($n)`) prunes statically to the digests' hash partitions, and one partition per distinct digest is the right count up to roughly 15 digests. Pruning bounds the partition count and not the probe count: each surviving partition evaluates the whole array against its own index, so the walk costs partitions times digests rather than digests. A [production-cardinality measurement](https://gitlab.com/gitlab-org/ops/artifact-registry/-/issues/564) across PostgreSQL 16, 17, and 18, over namespaces from 100 to 1,000,000 blobs and digest sets from 1 to 512, holds the shadow between 0.09 ms and 2.44 ms per call in every cell. The bound-array form beats that only at 1, 3, or 5 digests, never at 15 or above, and it loses by 2 to 6 times at 15 and by 9 to 48 times at 100. Both forms are sub-millisecond at the 4 to 15 files typical for Maven, so the shadow gives up nothing at typical cardinality and wins from 15 digests up.

Joining the digests as a derived table against the base table, rather than binding them as an array, prunes nothing at all: it opens all 64 partitions on every call and beat the shadow in none of the 123 cells measured. The Artifact Registry service runs the simple query protocol and re-plans every statement, so planning across 64 partitions dominates that walk rather than the reads.

Reading the shadow at this scope costs nothing the schema does not already pay. The trigger-maintenance write amplification lands per blob write, on the `AFTER INSERT` and `AFTER DELETE` triggers `blob_storage_blobs` already carries for the namespace- and repository-level walks, so a per-version reader adds none of it. The second copy of `size` cannot go stale through any write path that exists: blob sizes are content-addressed, so a change to a blob's bytes is a different `sha256` and therefore a different row, and no write path updates a row in place. `size` is immutable after insert, and a correction is a delete and reinsert, which the triggers propagate, never an `UPDATE`, because the shadow does not track updates. That immutability is a convention rather than something the schema enforces: nothing rejects an `UPDATE` of `blob_storage_blobs.size`, and with no `AFTER UPDATE` trigger the shadow would keep the pre-update value and answer a sum from it without raising. The exposure is the one the namespace- and repository-level walks already carry rather than one this scope introduces.

Per-version cardinality is bounded by the format protocol (typically 4-15 files for Maven, 1-3 for npm), so the recompute is a sub-millisecond single-partition read.

Backfilling the column when it is introduced is a set-based recompute grouped by version. It is cheap at current volumes (~26K versions in the deepest namespace backfill in roughly 284 ms, so the whole table is seconds at this scale) and far cheaper than deferring precomputation and backfilling against production volumes later. Doing it now also keeps the data model and API consistent across all three formats.

### Indexes

- **`blob_storage_blobs`**: unique index on `(namespace_id, sha256)` — enforce deduplication and check for blob existence by sha256 within an Organization. This constraint includes the partition key (`sha256`), so PostgreSQL enforces it correctly across all hash partitions. Covering index on `(namespace_id) INCLUDE (size)` — enables index-only scans for [namespace-level storage accounting reconciliation](#namespace-level-storage-accounting-reconciliation) without heap fetches.
- **`blob_storage_attachments`**: index on `(namespace_id, sha256)` — check for attachment existence given a blob's content hash (used by the [cleanup process](#cleanup-tasks) for orphan checks).
- **`blob_storage_blobs_by_namespace`**: primary key on `(namespace_id, sha256) INCLUDE (size)` — enforces 1:1 correspondence with `blob_storage_blobs` rows, and resolves the per-digest size lookups that [repository-level](#repository-level-storage-accounting-reconciliation) and [artifact-level](#artifact-level-storage-accounting-reconciliation) reconciliation issue without a heap fetch. Covering index on `(namespace_id) INCLUDE (size)` — the cheaper single-partition index-only scan for [namespace-level storage accounting reconciliation](#namespace-level-storage-accounting-reconciliation)'s whole-namespace sum, which reads no `sha256`; the primary key can serve that scan too, over entries carrying a 32-byte key column the sum does not use.
- **`namespace_statistics`**: primary key on `(namespace_id)` — one statistics record per namespace. The uniqueness this table needs is exactly the primary key's, so no separate unique index on the same single column is created; an implementation that adds one enforces nothing further. Index on `(last_reconciled_at, namespace_id)` — the catch-up staleness scan, which selects the namespaces whose last successful reconciliation pass is furthest in the past, and the backlog count over the same predicate. Both read this table alone: a scan that joins `namespaces` to catch a namespace with no row here cannot use this index at all, because the resulting `IS NULL` disjunct is a post-join filter rather than an index condition, so the query that consumes this index is the one restricted to `namespace_statistics`. The index is deliberately not `namespace_id`-led, unlike almost every other index in this document: the scan orders by recency across the whole table rather than within a namespace, and the table is unpartitioned, so a leading `namespace_id` would buy neither pruning nor ordering. `namespace_id` trails as a tiebreaker rather than a filter — it makes the sort key unique, which is what lets the scan page through keyset-wise rather than by offset, and it matters most immediately after the column is created, when every row shares the `'epoch'` default and the timestamp alone orders nothing. It also covers both queries — each selects only the two indexed columns — so on a vacuumed table both are answered from the index alone.

For hash-partitioned tables, indexes are local per partition — index operations are scoped to a single partition and do not lock the entire table.

### Blob storage query examples

- Pulling an artifact (read-path shortcut: `*_files` → `blob_storage_blobs`, skips attachments — 1 partition)

  ```sql
  SELECT bsb.object_storage_key, bsb.size
  FROM maven_files mf
  JOIN blob_storage_blobs bsb ON bsb.namespace_id = mf.namespace_id AND bsb.sha256 = mf.blob_sha256
  WHERE mf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND mf.maven_version_id = '019a1b2c-0456-7abc-8def-000000000456' AND mf.file_name = 'myapp-1.0.0.jar'
    AND mf.soft_deleted_at IS NULL;
  ```

- Dedup upsert on blob upload (1 partition, race-free)

  ```sql
  INSERT INTO blob_storage_blobs (namespace_id, sha256, size, object_storage_key, metadata_sha1)
  VALUES ('018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8', 'abcd1234efgh5678...'::bytea, 1048576, 'artifact_registry/.../objects/ab/cd/abcd1234efgh5678...', NULL)
  ON CONFLICT (namespace_id, sha256) DO NOTHING
  RETURNING id, sha256;
  ```

- Checking for a blob existence by sha256 within an Organization (1 partition)

  ```sql
  SELECT 1 AS one
  FROM blob_storage_blobs
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND sha256 = 'abcd1234efgh5678...'::bytea
  LIMIT 1;
  ```

- Orphan check: is this blob still referenced by any attachment? (1 partition)

  ```sql
  SELECT 1 AS one
  FROM blob_storage_attachments
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND sha256 = 'abcd1234efgh5678...'::bytea
  LIMIT 1;
  ```

- Storage accounting reconciliation via covering index on blobs (Option A): compute exact namespace storage from source data (64 partitions, index-only scan)

  ```sql
  SELECT SUM(size) AS total_size_bytes
  FROM blob_storage_blobs
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8';
  ```

- Storage accounting reconciliation via shadow table (Option B): compute exact namespace storage (1 partition, index-only scan)

  ```sql
  SELECT SUM(size) AS total_size_bytes
  FROM blob_storage_blobs_by_namespace
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8';
  ```

- Display path: read pre-computed namespace counters (single row lookup)

  ```sql
  SELECT deduplicated_size_bytes, components_count
  FROM namespace_statistics
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8';
  ```

- Display path: read the pre-computed repository counter (single row lookup, used by the landing page hybrid list)

  ```sql
  SELECT size_bytes
  FROM repositories
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND id = '019a1b2c-0456-7abc-8def-000000000456';
  ```

- [Repository-level reconciliation](#repository-level-storage-accounting-reconciliation): exact storage for a single repository, by format. Each leading CTE resolves the format-specific stub `id` (`container_repositories`, `maven_repositories`, or `npm_repositories`) from `repositories.id`; the mid-tier `*_repository_id` columns reference the stub table's own `id`, not `repositories.id`.

  - **Container**: walks images, unions blob refs from `container_blobs` and `container_manifests`, deduplicates by `blob_sha256`, sums via the namespace shadow table:

    ```sql
    WITH cr AS (
      SELECT id
      FROM container_repositories
      WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND repository_id = '019a1b2c-0456-7abc-8def-000000000456'
    ),
    uniq_blobs AS (
      SELECT cb.blob_sha256
      FROM container_blobs cb
      JOIN container_images ci
        ON ci.namespace_id = cb.namespace_id AND ci.id = cb.container_image_id
      WHERE ci.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
        AND ci.container_repository_id = (SELECT id FROM cr)
      UNION
      SELECT cm.blob_sha256
      FROM container_manifests cm
      JOIN container_images ci
        ON ci.namespace_id = cm.namespace_id AND ci.id = cm.container_image_id
      WHERE ci.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
        AND ci.container_repository_id = (SELECT id FROM cr)
    )
    SELECT COALESCE(SUM(bsb.size), 0) AS total_size_bytes
    FROM uniq_blobs u
    JOIN blob_storage_blobs_by_namespace bsb
      ON bsb.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND bsb.sha256 = u.blob_sha256;
    ```

  - **Maven**: a single file table covers version-specific and package-level files:

    ```sql
    WITH mr AS (
      SELECT id
      FROM maven_repositories
      WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND repository_id = '019a1b2c-0456-7abc-8def-000000000456'
    ),
    uniq_blobs AS (
      SELECT DISTINCT mf.blob_sha256
      FROM maven_files mf
      JOIN maven_packages mp
        ON mp.namespace_id = mf.namespace_id AND mp.id = mf.maven_package_id
      WHERE mp.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
        AND mp.maven_repository_id = (SELECT id FROM mr)
    )
    SELECT COALESCE(SUM(bsb.size), 0) AS total_size_bytes
    FROM uniq_blobs u
    JOIN blob_storage_blobs_by_namespace bsb
      ON bsb.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND bsb.sha256 = u.blob_sha256;
    ```

  - **npm**: walks packages → versions → files, unions package-level metadata files, deduplicates by `blob_sha256`:

    ```sql
    WITH nr AS (
      SELECT id
      FROM npm_repositories
      WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND repository_id = '019a1b2c-0456-7abc-8def-000000000456'
    ),
    uniq_blobs AS (
      SELECT nf.blob_sha256
      FROM npm_files nf
      JOIN npm_versions nv
        ON nv.namespace_id = nf.namespace_id AND nv.id = nf.npm_version_id
      JOIN npm_packages np
        ON np.namespace_id = nv.namespace_id AND np.id = nv.npm_package_id
      WHERE np.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
        AND np.npm_repository_id = (SELECT id FROM nr)
      UNION
      SELECT nmf.blob_sha256
      FROM npm_metadata_files nmf
      JOIN npm_packages np
        ON np.namespace_id = nmf.namespace_id AND np.id = nmf.npm_package_id
      WHERE np.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8'
        AND np.npm_repository_id = (SELECT id FROM nr)
    )
    SELECT COALESCE(SUM(bsb.size), 0) AS total_size_bytes
    FROM uniq_blobs u
    JOIN blob_storage_blobs_by_namespace bsb
      ON bsb.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND bsb.sha256 = u.blob_sha256;
    ```

- [Artifact-level](#artifact-level-storage-accounting): read the pre-computed container manifest size (immutable, single row lookup)

  ```sql
  SELECT size
  FROM container_manifests
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND id = '019a1b2c-0789-7abc-8def-000000000789';
  ```

- [Artifact-level](#artifact-level-storage-accounting): read the pre-computed Maven version size (source of truth, single row lookup)

  ```sql
  SELECT size_bytes
  FROM maven_versions
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND id = '019a1b2c-0456-7abc-8def-000000000456';
  ```

- [Artifact-level](#artifact-level-storage-accounting): list a Maven package's versions sorted by size for the version-list display (uses the `(namespace_id, maven_package_id, size_bytes DESC)` index; npm is analogous)

  ```sql
  SELECT id, version, size_bytes
  FROM maven_versions
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND maven_package_id = '019a1b2c-0123-7abc-8def-000000000123'
    AND soft_deleted_at IS NULL
  ORDER BY size_bytes DESC
  LIMIT 50;
  ```

- [Artifact-level reconciliation](#artifact-level-storage-accounting-reconciliation): recompute a Maven version's exact size from source data to verify or correct the counter (typically 4-15 files; bounded cardinality). Step 1 collects the version's distinct digests from `maven_files`, and step 2 sums their sizes from `blob_storage_blobs_by_namespace`, where the literal `namespace_id` prunes to one partition and each digest resolves index-only inside it:

  ```sql
  -- Step 1: the version's distinct digests (keyset-paged on blob_sha256)
  SELECT DISTINCT mf.blob_sha256
  FROM maven_files mf
  WHERE mf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND mf.maven_version_id = '019a1b2c-0456-7abc-8def-000000000456';

  -- Step 2: the digests from step 1, resolved against the namespace shadow
  SELECT COALESCE(SUM(bsb.size), 0) AS bytes
  FROM blob_storage_blobs_by_namespace bsb
  WHERE bsb.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND bsb.sha256 = ANY($1::bytea[]);
  ```

- [Artifact-level](#artifact-level-storage-accounting): read the pre-computed npm version size (source of truth, single row lookup)

  ```sql
  SELECT size_bytes
  FROM npm_versions
  WHERE namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND id = '019a1b2c-0456-7abc-8def-000000000456';
  ```

- [Artifact-level reconciliation](#artifact-level-storage-accounting-reconciliation): recompute an npm version's exact size from source data (typically 1-3 files per version; `npm_metadata_files` is keyed at the package level and is not part of a single version's footprint). Sums sizes from `blob_storage_blobs_by_namespace`, joining the version's distinct digests, the read the reconciliation section describes:

  ```sql
  WITH uniq_blobs AS (
    SELECT DISTINCT nf.blob_sha256
    FROM npm_files nf
    WHERE nf.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND nf.npm_version_id = '019a1b2c-0456-7abc-8def-000000000456'
  )
  SELECT COALESCE(SUM(bsb.size), 0) AS bytes
  FROM uniq_blobs u
  JOIN blob_storage_blobs_by_namespace bsb
    ON bsb.namespace_id = '018f4d6f-0e10-7e3a-9bfd-23a4c5d6e7f8' AND bsb.sha256 = u.blob_sha256;
  ```

## Consequences

### Positive

1. **Data organization tailored to each artifact format**: Using dedicated tables for each artifact format allows us maximum flexibility on the tables organization. We can have any number of additional columns that the format protocol requires. Additional auxiliary tables are not required since we're already using dedicated tables.

2. **Each format data tables will have the related usage pattern**: Each format dedicated tables will receive the usage pattern from the Rest and GraphQL APIs and the related artifact management clients. This provides isolation from the usage patterns of the other formats.

3. **Format-related data performance isolation**: A performance bottleneck on a specific artifact format table will not have an immediate impact on other formats.

4. **Transparent object storage cleanup**: Since the [object storage cleanup tasks](#cleanup-tasks) is centralized into the [blob storage](#blob-storage) domain, the parent domain (in this case, each format specific domain) doesn't need to handle this part. Additionally, this cleanup is not impacted by how the delete operation happened (single element destruction, bulk destruction, background cleanup policy executing a destruction on a selected set of elements).

5. **Blob storage isolation provides re-usability**: Blob storage tables are not tied to the Artifact Registry feature that we describe here. As such, this part can be re-used for file uploads needs in other areas.

6. **Efficient storage accounting**: Organization-scoped deduplication and deduplicated blob records per Organization make storage usage queries simple and efficient. Note: with `sha256`-based partitioning, Organization-level aggregates scan all 64 partitions. This is mitigated by dedicated rollup tables updated via delayed increments (see [partitioning strategy](#blob-storage-partitioning-strategy)).

7. **Unified cross-format listing**: The parent `repositories` table provides a single source for listing all repositories across all formats and kinds (hosted, virtual, remote) within a namespace, powering the landing page hybrid list without `UNION ALL` across multiple tables.

8. **Standalone remote repositories enable sharing**: Remote repositories as standalone entities with their own lifecycle can be shared across multiple virtual repositories, reducing duplication of configuration and cache entries.

### Negative

1. **Cross-format detail queries still require joins**: While the parent `repositories` table solves the landing page listing use case, accessing format-specific details (for example, container images, Maven packages) still requires joining to the format-specific tables.

2. **Centralized tables for blob storage**: This brings two downsides. First, we will have a very large amount of rows in these tables. Careful table design is required to handle this situation. Second, an issue with these tables (like a table wide lock) will potentially impact all artifact types.

3. **Per-repository storage attribution requires joins**: Accurate storage usage attribution at the repository level is derived through joins from format-specific tables through `blob_storage_attachments` to `blob_storage_blobs`. This keeps blob storage generic and deduplicated, but adds some complexity compared to denormalized per-repository counters.

4. **Two-step repository creation**: Creating a repository requires inserting into both the parent `repositories` table and the format-specific table. This adds transactional complexity compared to a single-table insert.

## Alternatives

### Centralize common data

A different approach here could be to store all the common data of the artifact format areas in common and centralized tables.

This would immensely help with the mixed artifact formats data access as it can answer those queries without joining multiple sources together.

This approach has already been used in the [Package Registry feature](https://docs.gitlab.com/user/packages/package_registry/) and at the time of this writing, those common tables have a high amount of rows as expected but also a high number of specialized indexes. Each of these indexes will support an access pattern specific to an artifact format. The amount of indexes being quite high that today, adding a new index, for example if a new format support is added to Package Registry feature, will have more scrutiny and even pushbacks.

Additionally, each artifact format has specific data that needs to be stored (for example, a normalized package name). This specific data can't be stored in common tables since it would create columns used by some rows only. This leads to the creation of several auxiliary tables. Those auxiliary tables will increase the amount of joins required for the access patterns of a given artifact type.

The introduction of the `repositories` parent table adopts a limited version of this approach: only the cross-format metadata needed for listing and filtering (name, visibility, format, kind, counters) is centralized. Format-specific data remains in dedicated tables, avoiding the index proliferation and auxiliary table problems described above.

## References

- [ADR-001: Organizations as Anchor Point](001_organizations_as_anchor_point.md) - Why the registry anchors to Organizations
- [ADR-002: Storage Deduplication Scope](002_storage_deduplication_scope.md) - Detailed decision on deduplication scope
<!-- - [ADR-010: Data Retention](010_data_retention.md) - Retention policies including soft delete and blob cleanup timing -->
- [Package Registry common tables decomposition](https://gitlab.com/groups/gitlab-org/-/work_items/16000) - Details the issues faced when storing common artifact related data in central tables.
