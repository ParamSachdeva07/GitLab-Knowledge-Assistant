---
title: 'Automated Dependency Updates ADR 001: Bounded, severity-prioritized remediation'
description: 'Decision to enforce the open-MR cap across scheduler runs, expose the limit as a per-project setting, and prioritize slots by vulnerability severity.'
---

## Context

The `SchedulerService` caps the number of open auto-remediation merge requests
per project so that a busy project doesn't get flooded with dependency update
MRs every time the scheduler runs. Because that cap is finite, we also need a
rule for which vulnerabilities get one of the limited MR slots when there are
more remediable vulnerabilities than the cap allows.

The original implementation checked a hardcoded limit
(`MAX_OPEN_MERGE_REQUEST_LIMIT = 3`), but only counted merge requests opened
during the *current* scheduler run. It didn't account for merge requests
still open from previous runs, so a project could accumulate far more open
MRs than the intended cap: every run could add up to the limit again, on top
of whatever was already open.

## Decision

We enforce the open-MR limit cumulatively **across scheduler runs**, not per
run, expose the limit as a per-project setting that can only be lowered from
the default, and spend the limited slots on the highest-severity
vulnerabilities first.

### Cross-run counting

An auto-remediation merge request is identified by its **author**:
`OpenRemediationsFinder` returns the project's open merge requests authored by
the dependency management service account. The scheduler starts each run from
that count rather than from zero, and compares the running total against the
limit. So the cap bounds *concurrently open* merge requests, not merge
requests opened per run — which is the behavior the original implementation
got wrong.

What the scheduler adds to that count during a run is an **attempted**
remediation, not an opened merge request. Scheduling the update workload is as
far as the scheduler goes; the merge request is created later, once the
workload's pipeline completes, and it may never be created at all — the update
can resolve to no dependency change, produce unusable output, exceed the
file-count ceiling, or be skipped because a maintainer already closed a merge
request for that vulnerability. Each of those consumes a slot for the duration
of the run and then frees it, because the next run recounts from what is
actually open.

This is a deliberate trade. Counting attempts means the cap sometimes reserves
slots for updates that never become merge requests, so a run can stop short of
the limit's worth of real merge requests. The alternative — counting only
confirmed merge requests — would mean the scheduler had no way to bound work
it has already put in flight, and a single run could queue far more workloads
than the project's cap allows. We would rather under-fill the cap than
overshoot it.

The same lookup does double duty: it also tells the scan which branches
already have an open merge request, so a component that is already covered is
skipped rather than re-proposed.

### Configurable limit

The limit lives in the `auto_remediation` section of a project's remediation
scan profile configuration, as `open_merge_requests_limit`, defaulting to
`10`. The configuration schema caps it at that same value, so today a project
can only lower the limit, never raise it. Allowing a higher ceiling is a
schema change, not just a configuration change.

### Severity-first ordering

Because the limit is finite, `SchedulerService` walks package managers and
severity levels in a fixed, sorted order
(`critical > high > medium > low`), stopping as soon as the limit is reached.
This guarantees the limited slots are spent attempting remediation for the
highest-severity vulnerabilities first, regardless of scan order.

### Known edge case

If a customer lowers the limit below the number of merge requests already
open, the project is already over its cap and no new remediation can start
until enough of the existing merge requests are merged or closed. The
comparison is deliberately not stricter than that, so the project recovers on
its own rather than deadlocking.

## References

1. `ee/app/services/dependency_management/security_update/scheduler_service.rb`
1. `ee/app/finders/dependency_management/security_update/open_remediations_finder.rb`
1. `ee/app/models/security/scan_profiles/configuration/defaults/dependency_scanning_post_processing.rb`
1. `ee/app/validators/json_schemas/security_profile_dependency_scanning_post_processing_configuration.json`
1. [Work item: Implement `currently_open_remediation_count` in `SchedulerService`](https://gitlab.com/gitlab-org/gitlab/-/work_items/594095)
1. [!234478: Count currently open MRs when limiting auto remediation runs](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/234478)
1. [002: Trigger via SBOM-ingestion scan profile](./002_trigger_via_sbom_ingestion.md)
1. [004: Package release cooldown](./004_package_release_cooldown.md)
1. [005: Refresh open merge requests instead of rebasing them](./005_refresh_instead_of_rebase.md)
