---
title: 'Data Insights Platform Querying API ADR 001: Structured requests with ontology definitions'
toc_hide: true
---

## Context

The [design document](../_index.md) chose GraphQL and REST for UI communication, with a Protobuf-over-gRPC API between the Monolith and DIP. It left open how queries are expressed over that API: as SQL passed through a gateway, or as structured requests.

Initial groundwork for this landed in milestone 19.0: the [generic `Query` RPC](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/merge_requests/125), which takes the domain as a parameter rather than needing a bespoke RPC per use case, and [reading domains from ontology documents](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/merge_requests/126), which lets a new domain be onboarded in YAML instead of Go.

On 2026-08-11 the team met to discuss the direction of Query API integration.

## Decision

Use structured requests plus ontology definitions, not a SQL gateway.

- The `Query` RPC is generic by design. Its Protobuf definitions are not tied 1:1 to specific tables or columns, and it aims to cover as much of the API surface as possible. Domain-specific RPCs can still be onboarded alongside it where the generic surface doesn't suffice e.g. `GetHierarchyContributions`.
- DIP owns the physical storage: tables, migrations, and materialized views. It publishes ontology documents describing what each domain exposes.
- Rails owns the business logic. It should read the ontology to know what it can query.
- Onboarding a new table or domain does not require a protobuf change. Each domain is described by an ontology YAML file.
- Rails should use the ontology to find out what domains exist. For DIP, it's intended to validate requests: the column exists, the primary key matches, and it specifies which column is the traversal path. DIP validates requests against the ontology today: the domain must be registered, the traversal path must be well-formed, and named metrics and measures are rejected when the domain doesn't declare them. Plain column names aren't checked against the declared columns yet, so those still reach ClickHouse unverified. Ontology files themselves are only checked for a domain and a table.
- Rails should depend on a compatible ontology rather than a specific DIP version. Compatibility should be verified at CI time, and possibly at runtime, with graceful degradation. For example, a feature shows as unavailable if an older DIP doesn't provide a metric.
- GLQL won't query DIP directly. Rails stays in the path for authorization and enrichment, such as resolving user ids into user objects. There's a push to extract authorization from Rails into a separate service, which could in theory let the Query API skip Rails one day, but it doesn't exist yet and nobody should plan around it. Even then, enrichment would still need Rails.

The [design document](../_index.md) has the request flow diagrams and the ontology YAML structure.

## Consequences

### Positive

- New tables and domains are onboarded with a YAML file, without proto changes.
- DIP can support data sources beyond ClickHouse. Direct S3/GCS destinations are on the roadmap, and a SQL gateway would have ruled these out.
- Storage details stay inside DIP, so DIP can restructure tables without breaking Rails, once the mapping question below is resolved.
- The ontology is the interface between DIP (storage) and Rails (business logic).

### Negative

- The current ontology format maps 1:1 to physical tables, but the query API is meant to hide storage details so DIP can restructure without breaking Rails. An internal vs external mapping split is likely needed. It looks feasible but needs investigation. [ADR 002](002_rails_dip_integration_boundaries.md) decides that ontologies should be generated from the Rails schema cache, which pulls towards a 1:1 physical mapping, so the two decisions should be reconciled when that split is designed.
- Sub-queries, CTEs, unions, and multi-domain joins aren't supported yet. Optimize's DORA and vulnerability work needs up to 4 levels of nesting. We believe this is feasible via shared dimensions, but it needs a POC. The API isn't usable for those cases until we've proved that.
- Schema changes and backfills are the least worked-out part. Who defines the new schema, who runs the migration and backfill in DIP, and where the business rule lives is unresolved. A working group on generic database migrations across services is forming.
- Because DIP owns the tables, ClickHouse migrations effectively move from the GitLab monolith to DIP over time. The current setup works for now.
- New metric development may get slower. A new metric could need a DIP release, then a Rails release, then GLQL: three releases where today there are two. The named metric and measure catalogs added since then reduce this, because a new metric is often an ontology change rather than a DIP code release, and [ADR 002](002_rails_dip_integration_boundaries.md) sets the target at one Rails declaration with no platform work.

### Open questions

- How the ontology files get published and how Rails gets them is undecided. [ADR 002](002_rails_dip_integration_boundaries.md) settles the near term: Rails stays the source of truth, and ontologies should be generated from the schema definitions it already dumps. A shared registry that Rails fetches at a version and caches, similar to the Snowplow iglu registry, is the longer-term direction, and the [shared proto registry](https://gitlab.com/gitlab-org/protos) was raised as a possible home for the proto files.

### Out of scope

- We could standardise field names across domains (traversal path, user id, namespace id). Starting with existing column names is fine.
- Metric definitions (the metadata layer) are a separate discussion, overlapping with Analytics Instrumentation's work on internal metrics.
- Any extraction of authorization logic and interaction with external API surface such as Workhorse.

## Alternatives

- A SQL gateway. Rejected because a SQL gateway only makes sense if ClickHouse is the only data source, and DIP will have more. It also leaks storage details to Rails.
- Moving all of the Rails aggregation business logic into DIP. Rejected because Rails keeps the domain semantics. A narrower move is in progress: aggregation mechanics, meaning which function to apply, over which operand, with which conditions and deduplication, should be declared in DIP's ontology. Rails keeps the caller-facing vocabulary, such as enum names and GlobalIDs. The mechanism for this has landed; migrating production domains onto it is ongoing.

## References

- [Epic: Data Insights Platform Querying API](https://gitlab.com/groups/gitlab-org/analytics-section/-/work_items/10)
- [Comparison of approaches](https://gitlab.com/groups/gitlab-org/analytics-section/-/work_items/10#note_3611607229)
- [Worked example](https://gitlab.com/groups/gitlab-org/analytics-section/-/work_items/10#note_3617056760)
- [Generic RPC surface, first iteration](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/merge_requests/125)
- [Reading domains via ontology documents](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/merge_requests/126)
- [Generic proto](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/blob/main/pkg/proto/gitlab/generic/v1/generic.proto)
- [Ontology definitions](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/blob/main/pkg/query-api/ontology/ontology.go)
- [Ontology example](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/blob/main/pkg/query-api/ontology/testdata/labels.yaml)
- [Shared dimension joins](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/work_items/144)
