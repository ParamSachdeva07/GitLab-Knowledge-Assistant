---
title: 'Automated Dependency Updates ADR 005: Refresh open merge requests instead of rebasing them'
description: 'Decision to resolve stale and conflicted auto-remediation merge requests by re-running the update workload, rather than the originally proposed rebase service.'
---

## Context

The original proposal listed a `RebaseMergeRequestService` responsible for
rebasing open dependency update merge requests when they hit a merge
conflict. That service was never built.

Rebasing turned out to be the wrong operation. A dependency update merge
request that conflicts with its target branch has usually conflicted
*because the manifest or lock file moved underneath it* — exactly the input
the resolver needs in order to reconsider. A rebase would replay a stale
resolution onto new state. It also would not help the adjacent case, where
the merge request merges cleanly but a newer patched version has since been
published.

## Decision

We re-run the update workload against the existing branch instead of
rebasing it. Before scanning for new work, the scheduler walks the merge
requests it already has open and re-runs the update for the ones that need
it. Because the update commits to the merge request's existing source branch
and updates the existing merge request rather than opening a new one, the
refresh lands in place — no new branch, no new merge request, review history
preserved.

An open merge request is refreshed in two cases:

1. **Its refresh cooldown has elapsed**, so a newer patched version can reach
   the open merge request. Gating on a cooldown is what keeps this from
   running a workload on every pipeline.
1. **It is recorded as conflicted** and both branches still exist. Nothing
   else recovers this state: the branch writes bypass the mergeability
   recheck that a normal push triggers, and there is no periodic sweep. This
   case is deliberately not cooldown-gated, because a conflicted merge
   request stays stuck until something refreshes it.

Refreshing up front, rather than whenever the scan happens to encounter the
component again, also keeps the open-merge-request accounting in
[001](./001_bounded_severity_prioritized_remediation.md) correct. A
vulnerability can be dismissed, resolved, or fall outside the configured
severity threshold and so never reappear in the scan, which would otherwise
stop the scan from terminating early once the limit is reached.

## References

1. `ee/app/services/dependency_management/security_update/scheduler_service.rb`
1. `ee/app/services/dependency_management/security_update/refresh_cooldown.rb`
1. `ee/app/services/dependency_management/security_update/create_merge_request_service.rb`
1. [001: Bounded, severity-prioritized remediation](./001_bounded_severity_prioritized_remediation.md)
1. [004: Package release cooldown](./004_package_release_cooldown.md)
