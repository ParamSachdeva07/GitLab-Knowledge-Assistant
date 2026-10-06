---
title: "Incident Metrics"
description: "Definitions, targets, and scope for incident performance metrics tracked for GitLab.com and Dedicated, including MTTR, detection rates, and mitigation timeframes."
---

This page defines the incident performance metrics that are tracked for GitLab.com and Dedicated. It is the handbook-level reference for what each metric means and how it is scoped. For the underlying data pipeline and SQL-level definitions, see the [technical documentation](https://gitlab.com/gitlab-com/gl-infra/data/sqlmesh-catalog/-/blob/main/docs/design-docs/incident-metrics.md).

The Observability team owns the data pipeline that produces the metrics. The Incident Management team owns the [dashboard](https://dashboards.gitlab.net/d/incident-mttr/incident-mttr-dashboard) where they are reported.

## Target metrics

The targets below were defined as part of the [CTO Incident Metrics epic](https://gitlab.com/groups/gitlab-com/gl-infra/-/work_items/2014).

| Metric | Target |
|--------|--------|
| MTTR (to mitigation) | <30 min |
| % of S1/S2 mitigated within 30 min | >80% |
| Incidents mitigated >60 minutes | Trend towards 0 |
| % of S1/S2 incidents detected internally | >80% |

## Scope

Unless stated otherwise, reported metrics include every incident that has a `resolved_at` timestamp set, regardless of whether its incident.io status is `Closed`, `Merged`, `Paused`, or `Cancelled`. We do *not* restrict to the `Closed` status, because the time between resolution and closure is a process artifact that should not influence the numbers.

Severity-scoped metrics (for example "% of S1/S2 mitigated within 30 min") apply the severity filter on top of that base population.

## Metric definitions

### Time to Recovery (TTR)

TTR measures the elapsed time from when customer impact began to when that impact was mitigated.

- **Start**: `Impact started at`, falling back to `Declared at` when `Impact started at` is not set.
- **End**: `Fixed at`, falling back to `Resolved at` when `Fixed at` is not set.

If both start and end are missing after the fallbacks, TTR is not calculated for that incident. With the fallback strategy, TTR is calculable for essentially all S1/S2 incidents; the underlying field-level coverage is substantially lower (see the [technical doc](https://gitlab.com/gitlab-com/gl-infra/data/sqlmesh-catalog/-/blob/main/docs/design-docs/incident-metrics.md#time-to-recovery-ttr) for the coverage analysis that motivates the fallbacks).

**MTTR** is the median of TTR across the population in scope, over a rolling 30-day window.

### % of S1/S2 mitigated within 30 minutes

Of all S1 and S2 incidents in the rolling 30-day window, the share whose `TTR ≤ 30 minutes`.

### Incidents mitigated >60 minutes

Count of incidents in the rolling 30-day window whose `TTR > 60 minutes`. This is the indicator that informs whether a mandatory retrospective is required.

### Internally detected (`is_internally_detected`)

An incident is considered **internally detected** if:

1. It has at least one linked alert in incident.io, AND
2. The first of those alerts fired *at or before* the incident was created.

This captures the intent behind ">80% of S1/S2 incidents detected internally before the first customer report": the incident must be traceable back to automation that fired no later than the moment the incident existed. Incidents declared manually — where an alert is only associated after the fact — are not counted as internally detected, even if an alert was eventually linked. Incidents without any linked alert are also not counted.

## Where to find the numbers

- [Incident MTTR dashboard](https://dashboards.gitlab.net/d/incident-mttr/incident-mttr-dashboard) — primary reporting surface for the metrics above, including overall, by severity, and by platform (GitLab.com, Dedicated, etc.).
- [Incident metrics technical documentation](https://gitlab.com/gitlab-com/gl-infra/data/sqlmesh-catalog/-/blob/main/docs/design-docs/incident-metrics.md) — pipeline, report views, and the SQL-level definitions that back this page.

## Changing a definition

If a metric definition changes, update this page together with the [technical documentation](https://gitlab.com/gitlab-com/gl-infra/data/sqlmesh-catalog/-/blob/main/docs/design-docs/incident-metrics.md) and the dashboard panels so all three stay in sync.
