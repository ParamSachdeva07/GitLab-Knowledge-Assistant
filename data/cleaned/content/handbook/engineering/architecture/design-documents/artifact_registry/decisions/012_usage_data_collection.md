---
title: "Artifact Registry ADR 012: Usage Data Collection"
owning-stage: "~devops::package"
description: "Decision on how the Artifact Registry collects usage data for product analytics and business intelligence across SaaS and self-managed deployments"
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Context

The Artifact Registry requires usage data collection for product analytics, business intelligence, and billing. Usage data answers critical questions: which artifact formats are most adopted, how many artifacts are pushed and pulled, how storage grows over time, how many unique users interact with the registry, and what virtual repository cache hit rates look like.

The Artifact Registry is a standalone Go service deployed outside the Rails monolith ([ADR-006](006_technology_stack.md)). GitLab's primary instrumentation framework — [Internal Event Tracking](https://docs.gitlab.com/ee/development/internal_analytics/) backed by Snowplow — is designed around Rails monolith integration. Collecting usage data from a satellite service requires a deliberate strategy.

Collection must work across all deployment types:

- **GitLab.com (SaaS)**: Multi-tenant, GitLab-operated infrastructure with full access to analytics pipelines
- **Self-Managed**: Customer-hosted instances where data collection depends on customer opt-in
- **GitLab Dedicated**: Single-tenant cloud instances managed by GitLab, functionally similar to self-managed for data collection purposes

### Internal Event Tracking via Snowplow

GitLab's primary instrumentation framework. Events are sent to Snowplow collectors, flow through an AWS pipeline with pseudonymization, and land in a data lake to be ingested into the Snowflake data warehouse. Available on SaaS always, and on self-managed/Dedicated from GitLab 18.0+ with customer opt-in.

For Go satellite services, [LabKit v2](https://gitlab.com/gitlab-org/labkit) provides a native Snowplow tracker (`v2/events/snowplow/`) with:

- Custom usage events using the [`custom_event`](https://gitlab.com/gitlab-org/iglu/-/tree/master/public/schemas/com.gitlab/custom_event/jsonschema) schema, with one or more self-describing custom contexts attached to carry typed, schema-validated attributes.
- Billable usage events using the [`billable_usage`](https://gitlab.com/gitlab-org/iglu/-/tree/master/public/schemas/com.gitlab/billable_usage/jsonschema) schema, whose first-class fields include the billing keys (`root_namespace_id`, `unique_instance_id`), `realm`, `deployment_type`, `quantity`, and `unit_of_measure`, plus a free-form `metadata` object for dimensions the schema does not model.
- Asynchronous batch sending with automatic retry and FIFO queue management
- Built-in Prometheus metrics for emitter observability
- In-memory event storage (10,000 event capacity) with overflow protection

This is the same mechanism used by other satellite services (AI Gateway, GitLab Language Server) and is the organizationally recommended path for Go services.

### Context schemas for custom events

Every AR custom event attaches two contexts, layered by scope:

- **[`gitlab_standard`](https://gitlab.com/gitlab-org/iglu/-/tree/master/public/schemas/com.gitlab/gitlab_standard/jsonschema)** — universal identity and environment fields (`environment`, `realm`, `instance_id`, `deployment_type`, `organization_uuid`, `user_id`). The Artifact Registry stores only the Organization's UUID ([ADR-022](022_namespace_decoupling.md)), so it populates `organization_uuid` and never the integer `organization_id`. Lands AR events in the same warehouse columns as monolith events for cross-product analysis.
- **[`artifact_registry_context`](https://gitlab.com/gitlab-org/iglu/-/tree/master/public/schemas/com.gitlab/artifact_registry_context/jsonschema)** — AR-specific dimensions: `ar_instance_version` (required), `ar_namespace_id` (namespace UUID) and `ar_namespace_slug`, `format`, `repository_kind` (`hosted`/`virtual`/`remote`), `repository_id` (repository UUID) and `repository_name`, `cache_hit`, `upstream_type` (`hosted`/`remote`). Namespace and repository each carry their UUID plus a human-readable identifier. The UUIDs are the stable join keys for analytics, because the slug, while immutable for customers, can change through administrative reclamation (squatting disputes, legal claims).

Event-specific one-offs (for example `auth_method`, `deletion_type`, `artifacts_removed_count`) go in the event's own `custom_event` payload rather than in either context.

## Decision

**The Artifact Registry will use the LabKit v2 Snowplow tracker as its sole usage data collection mechanism.** Events are emitted directly from the Go service to the Snowplow collector endpoint. No Rails monolith integration is required for analytics data flow.

This is the simplest path that delivers event-level product analytics for the MVP. It mirrors the approach already used by other Go satellite services (AI Gateway, GitLab Language Server). Aggregated metric collection (for example via Service Ping) is intentionally out of scope; if a future need arises for self-managed instances that opt out of Snowplow, it can be addressed in a follow-up ADR.

### Event-Level Tracking via LabKit v2 Snowplow

**What to track** (initial set, expanded iteratively). Every event carries both `gitlab_standard` and `artifact_registry_context` as custom contexts. Universal fields (`organization_uuid`, `realm`, `deployment_type`, `instance_id`, `environment`, `user_id`) come from `gitlab_standard` and are not repeated below.

| Event | `artifact_registry_context` fields | Event payload (one-off) fields |
| --- | --- | --- |
| `artifact_registry_artifact_pushed` | `format`, `repository_kind=hosted`, `repository_id`, `ar_namespace_id` | `auth_method` |
| `artifact_registry_artifact_pulled` | `format`, `repository_kind` (`hosted`/`virtual`), `repository_id`, `ar_namespace_id`, `cache_hit` (virtual only) | `auth_method`, `delivery_mode` (`proxy`/`redirect`) |
| `artifact_registry_artifact_deleted` | `format`, `repository_kind`, `repository_id`, `ar_namespace_id` | `deletion_type` (`manual`/`lifecycle_policy`) |
| `artifact_registry_namespace_created` | `ar_namespace_id` | — |
| `artifact_registry_repository_created` | `format`, `repository_kind`, `repository_id`, `ar_namespace_id` | — |
| `artifact_registry_repository_deleted` | `format`, `repository_kind`, `repository_id`, `ar_namespace_id` | — |
| `artifact_registry_virtual_cache_miss` | `format`, `repository_kind=virtual`, `repository_id`, `ar_namespace_id`, `upstream_type` (`hosted`/`remote`) | — |
| `artifact_registry_lifecycle_policy_executed` | `format`, `repository_kind`, `repository_id`, `ar_namespace_id` | `artifacts_removed_count` |

#### When a pull event fires

The catalog above names the dimensions but not the moment. "Download success" is ambiguous once a response can fail after its status is committed, and each format slice resolved that ambiguity independently, so the readings diverged. The rule is **each delivery mode reports the strongest signal it can observe**.

[ADR-005](005_artifact_delivery_mode.md) defines the two modes. Because it makes the mode an instance-level default with an always-available per-namespace override, the same artifact can be counted under either rule, depending on the namespace serving it. The event records how the response actually delivered, not the configured setting.

1. **Proxy mode**: the service streams the bytes, so it knows whether delivery completed. The event fires only after the payload copy finishes cleanly. Once the response status is committed, a client disconnect or a storage read fault emits nothing, because a partial transfer is not a download.
1. **Redirect mode**: the service hands the client a pre-signed storage or CDN URL and never sees the transfer. The event fires when the service issues the redirect. That is the only observable moment, and it counts as one pull for product usage.

Leveling proxy mode down to the redirect rule would discard a delivery signal the service holds; leveling redirect mode up to the proxy rule is impossible.

The two modes therefore carry different confidence. Redirect-mode pulls can over-count (the client may never follow the redirect) and under-count (one pre-signed URL may serve several transfers within its TTL, and a CDN may serve many clients from one origin fetch). The event payload carries the mode, per the catalog above, so analysis can separate the two; summing across both blends the confidence levels. Billable quantity in particular cannot rest on redirect-mode events; it needs storage or CDN access logs.

The AR namespace is the slug-anchored entity from [ADR-022](022_namespace_decoupling.md) — an organization can own multiple AR namespaces. The [billing design doc](https://gitlab.com/gitlab-org/architecture/usage-billing/design-doc/-/merge_requests/27) sets the metering boundary at the AR namespace: billable events carry `ar_namespace_id` in `billable_usage.metadata`, and analytics events carry it in `artifact_registry_context`, so both datasets aggregate at the same granularity. `organization_uuid` (in `gitlab_standard`) supports cross-namespace rollups.

**Configuration**: The Snowplow collector endpoint is provided via the service configuration file. On SaaS, this points to `snowplowprd.trx.gitlab.net`. On self-managed and Dedicated instances that opt in, this is configured to point to the same collector. On instances that opt out, the emitter is disabled (no events are sent).

**Coverage**: SaaS (always), self-managed and Dedicated (with customer opt-in, opt-out by default).

**Data destination**: Events flow through the standard Snowplow pipeline (collector, enricher, pseudonymization, S3) into the Snowflake data warehouse. No custom pipeline infrastructure is required.

### Operational Metrics (Non-Product)

The Artifact Registry already uses LabKit v2 for Prometheus metrics (request latency, error rates, connection pool stats). These are operational metrics consumed by infrastructure dashboards and alerting, not product analytics. They are mentioned here for completeness but are not part of the usage data collection decision.

The LabKit Snowplow emitter itself exposes Prometheus metrics (enqueue counts, send success/failure, batch delivery duration, queue depth) that should be registered for operational visibility into the event pipeline health.

## Consequences

### Positive

1. **Full SaaS coverage from day one**: LabKit v2's Snowplow tracker is production-proven and provides event-level granularity with no additional infrastructure
2. **Simple, single-path instrumentation**: One mechanism, one codepath. No coordination with the Rails monolith for analytics data flow
3. **Organization-scoped context**: Every event carries `gitlab_standard.organization_uuid`, aligning with the Organization-anchored architecture ([ADR-001](001_organizations_as_anchor_point.md)). The integer `organization_id` fields stay unpopulated because the service stores only the UUID; billing joins key on `root_namespace_id` (SaaS, from the namespace's billing anchor `billing_entity_type`/`billing_entity_id`, [ADR-007](007_database_schema.md)) and `unique_instance_id` (Self-Managed and Dedicated)
4. **Privacy by default**: Events flow through GitLab's existing pseudonymization pipeline (HMAC-SHA256) without additional privacy engineering
5. **No custom infrastructure**: Uses the existing Snowplow pipeline and Snowflake warehouse
6. **Billing-ready**: LabKit v2's billing tracker provides a direct path to usage-based billing for the Artifact Registry SKU, with fields for realm, unit of measure, and quantity
7. **Aligned with satellite service precedent**: AI Gateway and GitLab Language Server already use LabKit v2 Snowplow directly. The Artifact Registry follows the same pattern.

### Negative

1. **Minimum LabKit v2 and iglu version dependency**: Emitting custom contexts on custom events requires a LabKit v2 release that supports it, and the `artifact_registry_context` schema must be deployed to the Snowplow enrichment pipeline before AR events using it pass validation.
2. **No data from Snowplow opt-out instances**: Self-managed and Dedicated instances that opt out of Snowplow forwarding contribute no usage data at all. This is acceptable for the MVP given the customer's explicit opt-out. If aggregated coverage of opt-out instances becomes a product requirement, a Service Ping integration can be added in a follow-up ADR.
3. **In-memory event buffer risk**: LabKit v2's Snowplow emitter uses in-memory storage (up to 10,000 events). Events are lost on process restart. For the Artifact Registry's expected event volume, this is acceptable — events are analytics data, not transactional records. Prometheus metrics on the emitter provide visibility into overflow or drop rates.

## Alternatives Considered

### Alternative 1: Route All Events Through the Rails Monolith

#### Approach

The Artifact Registry sends all usage events to the Rails monolith via an internal API. The monolith then fires `track_internal_event()` calls on behalf of the registry, using the existing Rails-integrated Snowplow pipeline.

#### Why Not Chosen

1. **Tight coupling**: Every tracked action would require an API call to the monolith, creating a runtime dependency for analytics on the critical path or a background job queue between the services
2. **Latency and availability risk**: If the monolith is slow or unavailable, event tracking degrades or blocks. LabKit's in-process emitter decouples tracking from any external service
3. **Unnecessary indirection**: LabKit v2 provides the same Snowplow tracker that the monolith uses internally, eliminating the need for a middleman
4. **Counter-pattern for satellite services**: Other Go services (AI Gateway, GitLab Language Server) already emit Snowplow events directly. Routing through Rails would be a regression from established patterns

### Alternative 2: OpenTelemetry (OTLP) to ClickHouse

#### Approach

Follow the [CI Job Telemetry](/handbook/engineering/architecture/design-documents/ci_job_telemetry/) pattern: emit OTLP traces/metrics to an OTEL Collector that writes to ClickHouse. Use ClickHouse as the analytics store instead of Snowflake.

#### Why Not Chosen

1. **Different use case**: CI Job Telemetry uses OTLP for operational performance traces (span-level timing of job stages). Artifact Registry usage data is product analytics (who uses what, how much, adoption trends). These are different domains with different query patterns and consumers
2. **ClickHouse availability**: ClickHouse is not yet universally available across all deployment types. Snowplow/Snowflake is the established product analytics infrastructure
3. **Organizational alignment**: The Analytics Instrumentation team owns the Snowplow pipeline and Snowflake warehouse. Product analytics consumers (product managers, data analysts) query Snowflake. Using ClickHouse would require building new query infrastructure and data models outside the established workflow
4. **Future compatibility**: If ClickHouse becomes the standard product analytics store, LabKit v2's Snowplow events can be rerouted at the pipeline level without changing application code. The decision is not mutually exclusive with future OTLP adoption

### Alternative 3: Add Service Ping Integration for Self-Managed Opt-Out Coverage

#### Approach

In addition to Snowplow, expose an internal API on the Artifact Registry that the Rails monolith queries during weekly Service Ping assembly to collect aggregated metrics. This would provide aggregated coverage even for instances that opt out of Snowplow event forwarding.

#### Why Not Chosen

1. **Cardinality problem**: Service Ping payloads aggregate to flat scalar metrics (one number per metric per week). The Artifact Registry's interesting dimensions — format, repository kind (hosted/virtual/remote), authentication method, organization, upstream type — explode into a large number of metric variants once cross-tabulated. Modeling this in Service Ping requires either flattening cardinality (losing analytical value) or registering hundreds of pre-aggregated metric YAML definitions (operational burden). Snowplow events handle high cardinality naturally because dimensions are stored alongside each event in the warehouse.
2. **Expensive SQL aggregations**: Service Ping computes its metrics via SQL queries on the live database. The Artifact Registry's tables (artifacts, blob references, cache entries) are partitioned by namespace and grow into the billions of rows at GitLab.com scale ([ADR-007](007_database_schema.md), [ADR-003](003_system_requirements.md)). Cross-namespace `COUNT`/`SUM` queries to populate weekly Service Ping metrics would scan large amounts of data on every cycle — an expensive operation we do not need to justify when Snowplow already provides the same information from the warehouse without touching the production database.
3. **Avoid Redis counter infrastructure**: The alternative to live SQL is to maintain Redis-backed counters incremented on every artifact operation, then read by Service Ping. This is the pattern the Rails monolith uses for HyperLogLog and Redis HLL metrics. Adopting it here would add a new operational dependency (Redis counters, expiry handling, recovery semantics on Redis flush) and a new instrumentation surface in the hot path of every push/pull. Snowplow already captures this data at the same instrumentation point, so the Redis counter layer would be pure duplication.
4. **Cross-service coordination**: Adds a dependency on the Rails monolith team for the YAML metric definitions, which is the kind of cross-service coupling we are trying to avoid in this ADR.
5. **Bounded gap**: Self-managed customers who opt out of Snowplow are explicitly choosing not to share data. The coverage gap is bounded and aligned with customer intent.
6. **Not foreclosed**: This option remains available as a follow-up if product requires aggregated coverage of opt-out instances. A separate ADR can revisit the tradeoff once we have data on opt-out rates.

## Implementation Sequence

1. **Phase 1 (MVP)**: Integrate the LabKit v2 Snowplow tracker. Emit events for core actions (push, pull, delete, repository create) with `gitlab_standard` and `artifact_registry_context` attached. Register emitter Prometheus metrics. Validate events arrive in Snowflake on staging with both contexts populated.
2. **Phase 2 (Billing)**: Emit billing events for billable actions (storage consumption, artifact transfers), conforming to the `billable_usage` schema: `root_namespace_id` (from the billing anchor, [ADR-007](007_database_schema.md)) identifies the paying subscription on SaaS, `unique_instance_id` on Self-Managed and Dedicated, and `ar_namespace_id` (the metering boundary per the [billing design doc](https://gitlab.com/gitlab-org/architecture/usage-billing/design-doc/-/merge_requests/27)) rides in the event's `metadata` object alongside `feature_qualified_name`. The billing pipeline reads only the top-level `billable_usage` fields and `metadata`, never the Snowplow custom contexts, so AR-specific billing dimensions belong in `metadata` rather than in `artifact_registry_context`. Independent of Phase 1.
3. **Phase 3 (Iteration)**: Expand event coverage based on product analytics requests — virtual repository usage patterns, lifecycle policy effectiveness, format-specific adoption. Extend `artifact_registry_context` (new minor version) if recurring AR-specific dimensions warrant first-class warehouse columns.

## References

- [LabKit v2 Snowplow Tracker](https://gitlab.com/gitlab-org/labkit/-/tree/main/v2/events/snowplow) — Go Snowplow client used by satellite services
- [Iglu `custom_event` schema](https://gitlab.com/gitlab-org/iglu/-/tree/master/public/schemas/com.gitlab/custom_event/jsonschema) — Schema for custom event payloads
- [Iglu `billable_usage` schema](https://gitlab.com/gitlab-org/iglu/-/tree/master/public/schemas/com.gitlab/billable_usage/jsonschema) — Schema for billable usage event payloads (billing keys: `root_namespace_id`, `unique_instance_id`)
- [Iglu `gitlab_standard` schema](https://gitlab.com/gitlab-org/iglu/-/tree/master/public/schemas/com.gitlab/gitlab_standard/jsonschema) — Universal identity/environment context attached to AR custom events
- [Iglu `artifact_registry_context` schema](https://gitlab.com/gitlab-org/iglu/-/tree/master/public/schemas/com.gitlab/artifact_registry_context/jsonschema) — AR-specific context schema (merged in [iglu!190](https://gitlab.com/gitlab-org/iglu/-/merge_requests/190))
- [labkit!498](https://gitlab.com/gitlab-org/labkit/-/merge_requests/498) — Adds custom-context support to LabKit v2's Snowplow tracker
- [labkit#103](https://gitlab.com/gitlab-org/labkit/-/work_items/103) — Tracking work item for custom-context support in LabKit v2 (resolved by labkit!498)
- [Usage Billing Design Doc !27](https://gitlab.com/gitlab-org/architecture/usage-billing/design-doc/-/merge_requests/27) — Sets the AR namespace as the metering boundary; billable events carry `ar_namespace_id` in `metadata`, analytics events in `artifact_registry_context`
- [ADR-022: Namespace Decoupling](022_namespace_decoupling.md) — Defines the AR namespace as a slug-anchored entity distinct from Rails namespaces
- [Internal Analytics Documentation](https://docs.gitlab.com/ee/development/internal_analytics/) — GitLab's analytics instrumentation guide
- [Event Data Collection for Self-Managed and Dedicated](https://docs.gitlab.com/administration/settings/event_data) — Configuration and privacy details for self-managed Snowplow collection (18.0+)
- [Customer Product Usage Events FAQ](/handbook/legal/privacy/product-usage-events-faq/) — Customer-facing FAQ on self-managed event collection, opt-out mechanics, and the 17.11→18.0 rollout
- [Customer Product Usage Information](/handbook/legal/privacy/customer-product-usage-information/) — Privacy and legal framework for Service Ping, Snowplow, and License Sync data collection
- [Internal Events Data Flows](/handbook/engineering/data-engineering/analytics/analytics-instrumentation/technical-blueprint/current-state/internal-events-data-flows/) — Sequence diagrams for event collection across deployment types
- [Analytics Instrumentation Infrastructure](/handbook/engineering/data-engineering/analytics/analytics-instrumentation/infrastructure/) — Snowplow and Service Ping infrastructure details
- [CI Job Telemetry Design Document](/handbook/engineering/architecture/design-documents/ci_job_telemetry/) — OTLP-based telemetry approach (alternative considered)
- [ADR-001: Organizations as Anchor Point](001_organizations_as_anchor_point.md) — Organization-scoped architecture
- [ADR-006: Technology Stack](006_technology_stack.md) — Go language and LabKit v2 adoption
- [ADR-009: API Design](009_api_design.md) — Management and Client API structure
