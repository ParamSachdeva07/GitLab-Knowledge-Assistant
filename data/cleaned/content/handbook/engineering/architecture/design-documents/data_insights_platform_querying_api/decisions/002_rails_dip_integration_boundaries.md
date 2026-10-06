---
title: 'Data Insights Platform Querying API ADR 002: Rails to Query API integration boundaries'
toc_hide: true
---

## Context

[ADR 001](001_structured_requests_with_ontology.md) settled that Rails sends structured requests and DIP publishes ontology definitions. However, there is a question of where the seam between the two sits for the first real consumer: the Rails Aggregation Engines, which query ClickHouse directly today.

A [spike on Aggregation Engine integration](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/work_items/172) found the integration surface is small: the engines reach a backend through a narrow interface, so a Query API implementation can sit alongside the ClickHouse one without disturbing the GraphQL, authorization, or pagination layers above it.

This ADR records the boundaries followed from this [discussion](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/work_items/176) so implementation can start against a written contract. The implementation itself is tracked in the [Rails Integration of Analytics Query API](https://gitlab.com/groups/gitlab-org/analytics-section/-/work_items/27) epic.

## Decision

**Authorization stays entirely in Rails.** The resolver resolves paths to records, constrains them to a scope, checks `Ability.allowed?` per source, and then computes traversal paths. A second tier in `aggregation/authorization.rb` lets individual dimensions and metrics declare `authorize:`. That tier must run before translation, because an unauthorized metric should be dropped from the plan rather than filtered out of the result. DIP receives already-authorized traversal paths and makes no access decision of its own.

**DIP owns storage semantics.** Deduplication, filtering, grouping, aggregation, and pagination are DIP's responsibility.

**Rails owns domain semantics.** Enum names, GlobalIDs, model associations, and permissions stay in Rails. The existing `aeq_` alias contract plus `format_data` already implements this split, so both backends should produce the same post-`format_data` structure.

**Raw SQL does not cross the API boundary.** Domains declare `measures` (named server-side SQL expressions), `metrics` (a named catalog with function, operand, conditions, parameter allowlists, and value maps), and expression-backed `dimensions` in their ontology YAML. A request carries only names: `AggregateExpr` is `{function, column, alias, condition, quantile_level}` where `column` may name a declared measure, and `MetricRef` is `{name, alias, parameters}`. This shipped in milestone 19.5 via [named metrics](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/merge_requests/174) and [named measures](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/merge_requests/175). Consequently DIP needs no ClickHouse SQL parser, and there is no separate function allowlist to own: the ontology is the allowlist, and it is server-owned.

**The GraphQL field-per-metric stays.** A typed, introspectable schema requires static declaration, so metrics should remain declared fields. Everything below that field should collapse. A new metric needs at least three hops within Rails today, and the target is one Rails declaration per new metric with zero platform work.

**Ontology definitions should be generated.** Rails already auto-dumps table definitions to `db/click_house/schema_cache/main/*.yml`, and the mapping is mechanical: engine arguments become `dedup_config`, the primary key becomes `dedup_config.group_by_keys`, and column types become `columns[].type`. Rails derives this in roughly eight lines in `lib/gitlab/database/aggregation/click_house/engine/dsl.rb`. Generation should cover the derivable parts, with a small hand-authored overlay for what cannot be derived, such as measures, metrics, and human-readable names.

**Backends should be selected per engine behind a feature flag, defaulting to ClickHouse.** An engine opts in with `self.query_backend = :query_api`. Engines should migrate one at a time with the ClickHouse path kept as a live oracle. Deployments is the suggested first engine: eight dimensions and metrics, `traversal_path` plus `_siphon_replicated_at` and `_siphon_deleted`.

**ClickHouse schema ownership remains in Rails in the short term.** Rails' `db/click_house/main.sql` owns the Siphon DDL and the traversal-path dictionaries that populate `traversal_path` at insert time. Siphon writes the data and DIP reads it. Rails should stay the source of truth for the source of ontology YAMLs. Any further publication of schema in a separate repository can be ensured by the tooling in the monolith. There is already effort around streamlining this within Gitlab with [database migration framework](http://gitlab.com/gitlab-org/database-team/database-migration-platform) which we will coordinate with.

## Consequences

### Positive

- The narrow backend interface means the first engine migration stays below the GraphQL and authorization layers.
- Because authorization stays in Rails, DIP does not need a permissions model, and the Query API does not become a policy engine.
- Named measures and metrics remove the request-time SQL surface entirely, so there is nothing to parse or screen against a denylist.
- Generated ontologies make the Rails schema cache the single source for physical shape, which should keep the two repositories from drifting.
- Per-engine flags allow a staged rollout where both backends can be compared on live traffic before the ClickHouse path is retired.

### Negative

- Ontology-authored expressions still reach ClickHouse unparsed through `Raw()`. This is a configuration-trust surface rather than a request-injection surface, because the YAML is server-side and reviewed in a merge request. It should still be treated as privileged configuration, with review expectations to match.
- Keeping two backends per engine means the ClickHouse abstraction must be maintained for as long as the fallback exists.

### Followups

- **Multiple traversal paths.** Rails supports up to `MAX_SOURCES = 20` group or project paths combined with `OR`, while DIP's `traversal_path` is a single required string. This is a different axis from [shared dimension joins](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/work_items/144), which restructures `QueryRequest` into `repeated QuerySource sources` for several domains collapsed on a shared dimension while keeping `traversal_path` a single scalar at field 1. Rails needs several paths for one domain, and the two compose. A request-level `repeated traversal_paths` looks right, because paths are an authorization scope, are uniform across sources, and Rails computes them once, and it can fold into the joins work. Rails-side fan-out is the alternative but breaks server-side pagination. It is expected that there will be a request-level restriction in the beginning.
- **Window-function engines.** `retained_count` and `lagged_count` use window functions with `lag`, which the proto cannot express. It is expected that proto will gain support in future.
- **Is the Aggregation Engine's ClickHouse backend permanent?** Aggregation engine will give way to Query API, first as a shim and later all expected functionalities are expected to move to Query API.

### Out of scope

- Extracting authorization from Rails into a separate service. As [ADR 001](001_structured_requests_with_ontology.md) noted, it does not exist and nothing should be planned around it.

## Alternatives

- **Accept `Expr { sql, alias }` from Rails and validate it in DIP**, either by parsing to an AST and re-rendering, or by screening the string against a denylist. Rejected in favor of named measures and metrics. Parsing a ClickHouse dialect well enough to act as a security boundary is a large surface to build and maintain permanently, and the named-catalog approach removes the need for it. Denylists on SQL do not hold.
- **Migrating all engines at once behind a single flag.** Rejected because it removes the per-engine oracle that makes output equivalence checkable on live traffic.

## References

- [Epic: Rails Integration of Analytics Query API](https://gitlab.com/groups/gitlab-org/analytics-section/-/work_items/27)
- [Rails to DIP Query API: integration boundaries and open decisions](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/work_items/176)
- [Spike: Aggregation Engine integration with DIP Query API](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/work_items/172)
- [Rails: Add Data Insights Service to the Monolith](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/work_items/23)
- [Query API: Add support for JOINs across multiple ClickHouse domains](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/work_items/144)
- [Query API: Add support for derived (transient) dimensions and metrics](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/work_items/175)
- [Add support for domain-specific named metrics](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/merge_requests/174)
- [Add support for named measures and aggregates](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/merge_requests/175)
- [Generic proto](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/blob/main/pkg/proto/gitlab/generic/v1/generic.proto)
- [Ontology definitions](https://gitlab.com/gitlab-org/analytics-section/platform-insights/core/-/blob/main/pkg/query-api/ontology/ontology.go)
- [Rails Aggregation Engines](https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/gitlab/database/aggregation)
