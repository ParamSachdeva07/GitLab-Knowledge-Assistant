---
title: "Artifact Registry ADR 022: Namespace Decoupling"
owning-stage: "~devops::package"
description: "Proposal to introduce an internal namespaces entity with immutable slugs and a virtual anchor tuple, decoupling the Artifact Registry from Rails internal identifiers"
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Status

**Proposed.**

## Context

[ADR-001](001_organizations_as_anchor_point.md) established Organizations as the anchor point for the Artifact Registry.
Organizations represent the natural boundary for enterprise artifact management, align with GitLab's long-term
direction, and avoid the migration burden of building on top-level groups first. The current design follows ADR-001
directly: the Rails `organization_id` would be stored in database tables as a sharding key, embedded in API URLs, and
included in JWT token scopes.

While working on the authorization and API design ADRs, we decided that repository names should be
[immutable](https://gitlab.com/gitlab-org/gitlab/-/work_items/592582) to prevent client configuration breakage, OCI
reference invalidation, and authorization bypass risks from name reclaim. That decision naturally raised the question:
should the same principle apply at the namespace level? Organization paths are mutable (same as top-level group paths:
companies rename), so using them directly in Artifact Registry URLs would mean that every rename breaks client
configurations (`.npmrc`, `settings.xml`, Dockerfiles, CI pipelines), invalidates cached references, creates JWT token
scope staleness, and requires rename propagation and race condition handling between Rails and the Artifact Registry.
Enforcing immutability at the namespace level would eliminate all of this and simplify the design.

Separately, during the latest [CTO review](https://docs.google.com/document/d/1qkcOZYSHM_h9k9pYjHze2KHG5qZYMDeZ1UE4GZgD1jw/edit?tab=t.1dg0o6ns9uiw#bookmark=id.t5ky1ssp818r),
a virtual anchor point pattern was suggested for all satellite services so that tight coupling to `organization_id` does
not become costly to undo if the anchor entity evolves. The rationale is that GitLab's organizational hierarchy is
expected to continue to develop: nested organizations and organization merges are future considerations, and the
long-term plan for organization rollout is still unclear, so the Artifact Registry cannot assume universal organization
coverage.

Then, during [cross-team discussion](https://docs.google.com/document/d/1n81b4NNtwddtS419TA8Of-Yoymj2MNNM89FRBo43e8E/edit?tab=t.0#bookmark=id.ps8037nih9pa)
of this topic, it was questioned whether the Artifact Registry could use an immutable namespace identifier. This would
make the namespace identity fully owned by the Artifact Registry and independent of any external entity's naming.

A further observation is that a decoupled namespace identity could enable the Artifact
Registry to be packaged as an independent product whose sole dependency would be a third-party authentication and
authorization provider, not GitLab Rails. This is not a design driver but a positive side effect. It could open the door for reusing the product internally for GitLab.com in other ways, such as replacing Pulp with a separate
isolated instance of the Artifact Registry.

The idea of an indirection layer is not completely new. Early iterations of
[ADR-007](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18456) considered a `registries` table
as an abstraction between the anchor entity and internal tables, back when the team was still deciding between top-level
groups and organizations. This proposal builds on that pattern by adding an immutable, externally visible identity (the
slug) and making the anchor entity fully opaque.

These converging inputs led us to explore whether the Artifact Registry should own its own namespace identity rather
than referencing Rails' `organization_id` directly. Organizations remain the default anchor. The question is how the
Artifact Registry references them: directly, or through an internal indirection with its own immutable identifier.

## Proposal

Introduce an internal `namespaces` entity in the Artifact Registry with three properties:

1. **Immutable slug**: a globally unique, customer-chosen, human-readable identifier that appears in all URLs and never
   changes. Similar to how GCS/S3 storage bucket names work.
2. **Virtual anchor tuple**: an `(platform, entity_type, entity_id)` tuple that links the namespace to an external
   entity without interpreting its semantics
3. **UUIDv7 ID**: used for database partitioning, internal queries, and as the namespace's stable resource identifier
   for authorization, the resource that role assignments target ([ADR-021](021_authorization.md#role-assignment)). It
   is not an addressing identifier: the slug is the only namespace identifier in client-facing URLs, while the internal
   GitLab API is keyed by the UUID ([ADR-009](009_api_design.md))

Organizations remain the first anchor type. This proposal does not change
[ADR-001](001_organizations_as_anchor_point.md); it adds an abstraction layer between the Artifact Registry and the
anchor entity.

### Database Schema

```sql
CREATE TABLE namespaces (
    id                  UUID PRIMARY KEY,  -- UUIDv7 per ADR-007
    slug                TEXT NOT NULL UNIQUE,
    platform            TEXT NOT NULL,
    entity_type         TEXT NOT NULL,
    entity_id           TEXT NOT NULL,
    billing_entity_type TEXT NOT NULL,
    billing_entity_id   TEXT NOT NULL,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE (platform, entity_type, entity_id)
);
```

- `slug` is immutable after creation.
- `entity_id` is an opaque string (`TEXT`), whatever the value's format: numeric for some anchor types, a UUID for
  others. The Artifact Registry never interprets the external entity's semantics; `entity_type` tells a consumer
  which entity the value identifies.
- The unique constraint on `(platform, entity_type, entity_id)` prevents duplicate anchors.
- For Organizations v1, every row has `('gitlab', 'organization', '<organizations.uuid>')`: the organization's
  UUIDv7, not the numeric `organizations.id`. IAM's Relationships API rejects a non-UUIDv7 object id for the whole
  request it appears in, so the numeric id could not name the organization ancestor.
- No other unique constraint may be placed on the organization value: [Organization Merges](#organization-merges)
  requires a surviving organization to hold more than one namespace.
- Future anchor types add rows with different `entity_type` values. No schema migration needed.
- `billing_entity_type` and `billing_entity_id` identify the billing anchor for usage events. AR stamps these on
  every billing event without interpreting them. The Core Module (Rails) provides these values at namespace creation
  time. For FY27-Q2, the billing entity is the TLG (`billing_entity_type = 'top_level_group'`,
  `billing_entity_id = '<root_namespace_id>'`). When org-level billing lands in CDot, the values change to
  `('organization', '<organization_id>')` without an AR code change. This keeps AR billing-structure-agnostic.
- None of the externally-provided columns (`platform`, `entity_type`, `entity_id`, `billing_entity_type`,
  `billing_entity_id`) carry schema-level defaults. The Core Module must supply every value at namespace creation
  time so that the Artifact Registry schema remains agnostic to the external identity and billing models.

Tables that use `organization_id` as a sharding or partition key would use `namespace_id` instead. Foreign keys and
indexes follow the same patterns. The partition key is stable: internal IDs never change.

The [Cells sharding key requirement](https://docs.gitlab.com/development/organization/sharding/#choosing-the-right-sharding-key)
applies to the Rails monolith databases. Cell-local services only need to [attribute rows to an organization](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18808#note_3144391363)
(directly or indirectly) for data movement. The namespace model does this through `namespace_id -> anchor tuple -> organization`.

### URL Structure

```plaintext
Management:  /api/v1/<slug>/maven/repositories
Maven:       /<slug>/maven/my-repo/com/example/myapp/1.0.0/myapp-1.0.0.jar
npm:         /<slug>/npm/my-repo/@scope/package
OCI:         /v2/<slug>/repositories/my-repo/manifests/latest
```

No numeric IDs anywhere in any URL. The first path segment after the API prefix is always the slug. Both the slug and
repository names are immutable, so the entire URL path is permanently stable.

### Slug Design

The slug is chosen by the customer when creating a namespace and is exposed in every client surface. Its user-facing name in customer documentation and UX is **registry handle** (see [gitlab-org/gitlab#593366](https://gitlab.com/gitlab-org/gitlab/-/work_items/593366)). Design properties:

- **Immutable**: once set, it never changes. Consistent with repository name immutability and with industry practice.
- **Customer-chosen**: human-readable and typeable, since it appears in client configurations, CI pipelines, and
  Kubernetes manifests.
- **Globally unique**: no two namespaces can share a slug.

Validation rules, default derivation from the organization name, reservation policy, and lifecycle controls (security
block and transfer) are defined in [ADR-015: Slug Policy (internal)](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/artifact_registry/decisions/015_slug_policy/).

### Namespace Lifecycle

**Creation:** When a customer creates an Artifact Registry namespace (via the management API or a purchase flow), they
choose a slug and the namespace is linked to their organization via the anchor tuple. The namespace record is created in
the database and the slug is claimed with the topology service for Cells routing.

**Organization rename:** No impact on the Artifact Registry. The slug is immutable and independent of the organization
name. Nothing changes in the database, URLs, JWT scopes, or client configurations.

**Anchor promotion:** If a namespace needs to be re-anchored to a different entity, only the anchor tuple columns are
updated. The slug does not change. All URLs remain stable. All partitioned tables are unaffected. This is a future
capability; for Organizations v1, no promotion events exist.

**Status:** A namespace's serviceability derives from the lifecycle events and service conditions defined in [ADR-007](007_database_schema.md#namespaces): the one-way `deleted_at` and `purged_at` events, and the reversible `blocked_at` (security), `disabled_at` (organization turned the registry off), and `suspended_at` (billing, read-only) conditions. The Artifact Registry enforces these on every request regardless of what the Rails side has cached, and its API exposes the derived status, which Rails caches for display (see [Slug Discovery](#slug-discovery)).

**Deletion:** The Artifact Registry soft-deletes the namespace. The slug is reserved and cannot be reclaimed
by another customer, to avoid the same security risks as repository name reclaiming (authorization bypass, cache
poisoning). See [ADR-015 (internal)](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/artifact_registry/decisions/015_slug_policy/#slug-lifecycle) for the full lifecycle (soft-delete window allowing
reclaim, hard-delete with permanent retirement) and the security-block and transfer controls.

### Organization Merges

If GitLab supports organization merges in the future, the namespace model handles this without data migration:

1. Two organizations (each with its own namespace) merge into one.
2. The anchor tuple on the absorbed namespace is updated to point to the surviving organization. One metadata update per namespace.
3. The surviving organization now has two namespaces, each with its own repositories and independent deduplication boundary (tradeoff).
4. No data movement across database partitions.
5. Object storage blobs, caches, and any other stored data are keyed by namespace, not organization. Nothing moves in the storage backend either.
6. Slugs do not change. All URLs, JWT scopes, and client configurations remain stable.

On the Rails side, the UI could display multiple namespaces under the merged organization, each with its own
repositories:

```plaintext
Organization: Acme Corp (merged)
  Namespace: acme-engineering
    - maven/my-app
    - docker/service-a
  Namespace: acme-platform (from merged org)
    - maven/platform-lib
    - docker/service-b
```

If the customer later wants to consolidate into a single namespace, that would be an explicit migration (move
repositories from one namespace to another), not an automatic consequence of the merge.

Without the namespace abstraction, an organization merge could require migrating all partitioned data from one
`organization_id` to another, updating all URLs, reconciling deduplication boundaries, and handling JWT scope
staleness.

### Cells Routing

The topology service (a Go gRPC service) maintains a mapping of claimed identifiers to cells. The Artifact Registry
integrates by claiming slugs:

1. When a namespace is created, the Artifact Registry claims the slug with the topology service, mapping it to the cell
   where the namespace's data resides.
2. When a request arrives, the HTTP router extracts the slug (first path segment), queries the topology service, and
   routes to the correct cell.
3. For unauthenticated requests (e.g., anonymous Docker pulls), the slug is the only routing signal. This works because
   the slug is in the URL and can be classified without authentication.

The topology service is a shared Cells dependency, not specific to the Artifact Registry. Only namespace creation
requires the topology service to be writable (slug claiming). Read-path requests only need the routing lookup, which can be cached.

### Request Flow

Every request (authenticated or not) starts the same way:

1. HTTP router extracts slug from URL, routes to correct cell via topology service
2. Artifact Registry looks up `namespaces WHERE slug = '<slug>'` to get the namespace ID
3. Artifact Registry looks up the repository by `(namespace_id, name)` to get the repo record and visibility

The `namespaces` table is unpartitioned with a unique index on `slug`. One indexed lookup, then partition-routed queries
for everything else. Since the slug-to-namespace-ID mapping is immutable, it can be aggressively cached (in-memory or
Redis) to avoid a database query on every request.

**Authenticated requests** use the JWT exchange flow defined in
[ADR-020](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18462). All clients authenticate through the Artifact Registry, which resolves the slug to an org ID from its own namespace table and
includes it in the transparent exchange with Rails. Rails never needs to know about slugs on this path; the UI path is different (see [Slug Discovery](#slug-discovery)).

**Unauthenticated requests** skip the JWT exchange
([ADR-020](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18462)), are assigned `no_access`
directly, and the Artifact Registry evaluates access rules locally. No Rails call needed for public downloads.

### Authorization Compatibility

This proposal is compatible with [ADR-021](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18717):

- **Scope format**: ADR-021 currently uses `o/<org_id>/repositories/<format>/<type>/<repo_id>`. With this proposal,
  scopes would use the slug instead of the org ID (e.g., `<slug>/repositories/maven/hosted/my-repo`). The Artifact
  Registry resolves the slug to an org ID and includes it in the exchange with Rails.
- **JWT**: ADR-020 currently includes the organization ID in the JWT. With this proposal, the `organization_id` claim
  would no longer be needed. The Artifact Registry already has the namespace ID from its own lookup before the exchange
  happens. The JWT only needs to carry `access_level`.
- **Organization owners** receive Owner access level directly from Rails' org membership. No impact from the namespace
  approach.

### Slug Discovery

The GitLab frontend reaches the Artifact Registry through the Rails monolith ([ADR-014](014_frontend_to_artifact_registry.md)). Every Artifact Registry API call requires the slug in the URL, so Rails needs the slug before it can make any request.

Rails durably stores only the namespace UUID, one row per namespace, written at provisioning ([gitlab#603023](https://gitlab.com/gitlab-org/gitlab/-/work_items/603023)). For Organizations v1, that is a single row per organization; an [organization merge](#organization-merges) would add the absorbed namespace's row to the surviving organization. The UUID is immutable, so this reference never needs synchronization and survives merges and anchor changes.

The slug and the namespace status are not persisted on the Rails side. Rails resolves them from the Artifact Registry by UUID and caches them. Both can change only on the Artifact Registry's authority: the slug through the emergency escape hatch from its immutability (a legal escalation; see [slug immutability](007_database_schema.md#slug-immutability) in ADR-007), and the status through the service conditions ([ADR-007](007_database_schema.md#namespaces)), for example when a namespace must be disabled quickly. In the hybrid deployment model (Self-Managed Rails against a SaaS Artifact Registry), these changes can only originate on the Artifact Registry side, so Rails cannot be their source of truth.

A stale cache never weakens enforcement: the Artifact Registry enforces the namespace status on every request. For the status, staleness only affects display (for example, the navigation briefly showing the registry while the namespace is disabled) until the next refresh. For the slug, a stale value can render broken links until the next refresh; slug changes are rare emergency events, and the cache refresh interval bounds that window.

## Consequences

### Positive

1. **Complete Rails decoupling**: no Rails IDs in the Artifact Registry's schema, URLs, or logic. If Rails changes org
   IDs or structure, the Artifact Registry is unaffected.
2. **Immutable URLs**: both the slug and repository names are immutable. The entire URL path is permanently stable. No
   rename events, no path drift, no JWT scope staleness, no client config breakage from renames.
3. **Stable partitioning**: namespace IDs are internal and never change, even on anchor change. No impact on partitioned
   tables, foreign keys, or indexes.
4. **Virtual anchor flexibility**: the `(platform, entity_type, entity_id)` tuple enables attaching namespaces to organizations today
   and to other entities later without schema migration or data movement. Promotion between entity levels is a metadata
   update.
5. **Cells-ready**: slug claiming with the topology service provides a clean routing mechanism without depending on org
   path resolution.
6. **Self-sufficient for unauthenticated reads**: the Artifact Registry has its own namespaces table. No Rails call
   needed for public downloads.
7. **Organization merges without data migration**: if organizations merge, the anchor tuple is updated and the surviving
   organization holds multiple namespaces. No data movement, URL changes or client config breakage. See
   [Organization Merges](#organization-merges) for details.
8. **Standalone product potential** (aspirational): because the Artifact Registry owns its own namespace identity and treats the anchor
   as opaque, the architecture does not structurally depend on GitLab Rails. This opens the door to packaging the
   Artifact Registry as an independent product that relies on a third-party authentication and authorization provider
   instead of GitLab.

### Negative

1. **Slug uniqueness enforcement**: globally unique slugs introduce a squatting risk. Needs a policy for reserved names,
   high-value slug protection, and minimum length. This is a solved problem in the industry (S3, Docker Hub) but
   requires product decisions.
2. **All auth routes through the Artifact Registry**: since the Artifact Registry owns the slug-to-org mapping, all
   clients must authenticate through it rather than directly with Rails. This adds load to the Artifact Registry but avoids duplicating the mapping on the Rails side.
3. **Namespace creation is an explicit action**: the management API or purchase flow must create the namespace before
   any client requests can succeed. The Artifact Registry cannot serve requests for an org that has not set up a
   namespace.
4. **Topology service dependency**: the Artifact Registry needs to integrate the topology service Go client for slug
   claiming.
5. **Slug discoverability**: unlike organization paths which users already know from their GitLab experience, the slug
   is a new concept specific to the Artifact Registry. Users need to remember or look up their slug. Client
   configuration documentation and the UI need to account for this.
6. **Deduplication boundary change**: deduplication ([ADR-002](002_storage_deduplication_scope.md)) moves from
   organization to namespace. For v1 these are 1:1, but multiple namespaces per customer means each namespace has an
   independent deduplication boundary. Cross-namespace deduplication is out of scope.

## Impact on ADRs

If accepted, this proposal would require changes to the following ADRs that are currently open for review:

- **[ADR-007: Database Schema](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18456)**: the
  `organization_id` column in all partitioned tables would be renamed to `namespace_id`, referencing the internal
  namespace ID instead of the Rails org ID. A new unpartitioned `namespaces` table would be added to the schema.
  Partitioning strategy, composite primary keys, and foreign key patterns remain unchanged.
- **[ADR-009: API Design](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18458)**: the
  `/o/<org_id>/` prefix in URLs would be replaced by `/<slug>/`. The slug is the first path segment after the API prefix
  for all protocols (management, Maven, npm, OCI). No numeric IDs would appear in any URL. The Rails-to-Artifact-Registry endpoints (namespace creation, which returns the UUID Rails persists, and the UUID-keyed namespace resolution returning slug and status) belong to the internal API surface, defined in ADR-009 alongside the public surface but exempt from its slug-prefix rule.
- **[ADR-020: Authentication Flow](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18462)**: all
  clients would authenticate through the Artifact Registry, which resolves the slug to an org ID
  before exchanging with Rails. The `organization_id` claim in the JWT would no longer be needed.
- **[ADR-021: Authorization](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18717)**: scope
  format changes from `o/<org_id>/repositories/<format>/<type>/<repo_id>` to
  `<slug>/repositories/<format>/<type>/<repo_name>`. The authorization model (dedicated groups/projects, access levels,
  visibility sync) is otherwise unaffected.

- **[ADR-008: Content-Addressable Storage](008_content_addressable_storage.md)**:
  the object storage key hierarchy uses a SHA256 hash of the namespace's internal UUIDv7 ID for top-level isolation.
  Hashed paths are immutable by construction (no human-readable value to change), aligning with
  [GitLab's hashed storage standard](https://gitlab.com/groups/gitlab-org/-/work_items/2320). All artifacts for a
  namespace are co-located under the same hash prefix.

Already-merged ADRs are not structurally changed:

- **[ADR-001](001_organizations_as_anchor_point.md)**: Organizations as the anchor point stands. This proposal adds an
  abstraction layer, not a replacement.
- **[ADR-002](002_storage_deduplication_scope.md)**: Deduplication scope moves from organization to namespace. For the
  initial release these are 1:1. Storage is deduplicated within a namespace boundary: identical content within the same
  namespace is stored once.

## References

- [ADR-001: Organizations as Anchor Point](001_organizations_as_anchor_point.md)
- [ADR-002: Storage Deduplication Scope](002_storage_deduplication_scope.md)
- [ADR-007: Database Schema](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18456)
- [ADR-008: Content-Addressable Storage](008_content_addressable_storage.md)
- [ADR-009: API Design](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18458)
- [ADR-020: Authentication Flow](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18462)
- [ADR-021: Authorization](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18717)
- [Repository name immutability](https://gitlab.com/gitlab-org/gitlab/-/work_items/592582)
- [CTO review: virtual anchor point](https://docs.google.com/document/d/1qkcOZYSHM_h9k9pYjHze2KHG5qZYMDeZ1UE4GZgD1jw/edit?tab=t.1dg0o6ns9uiw#bookmark=id.t5ky1ssp818r)
- [Cross-team meeting: immutable slug idea](https://docs.google.com/document/d/1n81b4NNtwddtS419TA8Of-Yoymj2MNNM89FRBo43e8E/edit?tab=t.0#bookmark=id.ps8037nih9pa)
