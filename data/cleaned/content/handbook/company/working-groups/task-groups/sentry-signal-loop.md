---
title: "Sentry Signal Loop"
description: "A Task Group restoring frontend Sentry as a useful triage tool: cutting noise at source, and prototyping a Sentry-to-GitLab-issue automation with Duo Developer doing the triage."
---

## Attributes

| Property        | Value                                                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| Date Created    | 2026-05-19                                                                                               |
| Target End Date | 2026-09-27                                                                                                     |
| End Date        | 2026-09-28                                                                                                     |
| Current Status  | Closed. The automation keeps running in maintenance mode (see [Closing report](#closing-report))              |
| Project         | [duo-sentry-insights](https://gitlab.com/gitlab-org/frontend/duo-sentry-insights)                              |
| Epic            | [gitlab-org&22089](https://gitlab.com/groups/gitlab-org/-/epics/22089)                                        |
| Slack           | [#tg_sentry_signal_loop](https://gitlab.enterprise.slack.com/archives/C0B41EVB4J3) (only accessible from within the company)       |

## Context

GitLab's frontend Sentry project (`gitlabcom-clientside`) accepts approximately 25 million events every 30 days. The signal-to-noise ratio has degraded to the point where the project is functionally unused for triage: the loudest issues are not bugs, and the bugs that *do* exist are buried and unowned.

![Sentry baseline — gitlabcom-clientside, March 2026 (~24.8M error events)](/images/company/working-groups/task-groups/sentry-signal-loop/baseline-march-2026.png)

Baseline: ~24.8M error events in March 2026.

A meaningful share of that volume is not "our application is broken 25 million times" — it is events that should never have been reported in the first place. Browser-extension CSP reports (for example, ad-blockers blocking our own Snowplow endpoint, third-party browser telemetry) and expected `4xx` responses from the application correctly enforcing its rules dominate the top of the list. **Sentry should report unexpected failures of our code, and nothing more than that.**

On top of the volume problem, there is no triage process. Every event already carries a `feature_category` tag, and the canonical `feature_category` → owning group mapping (see [`/handbook/product/categories/features/`](/handbook/product/categories/features/)) lives in [`stages.yml`](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/stages.yml). Ownership is declared. What's missing is anyone or anything looking at the data — a real bug affecting hundreds of thousands of users sits unassigned not because we don't know whose it is, but because nothing is looking.

The [Frontend Observability Working Group](/handbook/company/working-groups/frontend-observability/) (2021–2023) built the technical instrumentation and exited cleanly. The framework works. What was never built is the operating loop on top of it — the signal loop this Task Group sets out to close.

### Goals

The work splits into two phases that together form the loop:

1. **Primary Goal — Reduce noise at the source.** Update the Sentry SDK configuration and Sentry inbound filters so that the project reports unexpected failures of our code, and nothing more. The exit criterion is a ≥50% drop in 30-day event volume, excluding events from issues triaged and archived on the platform, from the ~26M baseline (see [Exit Criteria](#exit-criteria) for the cited measurement and the rationale for excluding archived issues). The exact filters are decided iteratively as MRs land and Sentry data updates.

2. **Secondary Goal — Build a Sentry → GitLab issue → Duo Developer triage automation, and run it.** Once the noise floor is lowered, we build the system that keeps us on top of the events. The automation runs on a daily schedule, fetches the latest Sentry issues, opens corresponding GitLab issues routed to the owning group through `feature_category`, and uses Duo Developer to produce triage on each. The unifying pattern: an agent separates noise from signal, and on each side produces a proposal that a human acts on. No MRs are opened autonomously — the handoff to the human is part of the design, not a limitation of it.

### Challenges

- **Agent-assisted work on signal is genuinely hard.** Frontend errors are often symptoms of root causes elsewhere in the stack, so the agent's output has to be a useful starting point for a human, not a finished answer. Calibrating that bar is part of the experiment, not a precondition for it.
- **Routing depends on signals we don't fully control.** The automation routes Sentry issues to owning groups through `feature_category`, and relies on CODEOWNERS for human collaboration on the resulting GitLab issues. Both signals exist today, but it is not yet known how cleanly they map to "a human who can actually act on this issue." Some routing failures are expected; how we handle them is part of what the experiment surfaces.
- **Deduplication across daily runs.** The automation runs on a 24-hour cadence. A Sentry issue that exists today will, in most cases, still exist tomorrow — the underlying problem won't be resolved overnight. The automation must reliably recognise a Sentry issue it has already opened a GitLab issue for and skip it, rather than producing a duplicate every day. Getting this wrong floods owning groups with copies of the same issue and immediately destroys trust in the automation. The mapping from Sentry issue identity to GitLab issue is one of the first design decisions we need to get right.
- **Finding a long-term owner is not guaranteed.** The automation only survives the Task Group if a group accepts it as their permanent responsibility (see [Exit Criteria](#exit-criteria)). If no owner is found, the automation is sunset at the end of the quarter, and that is itself a valid outcome — it tells us the value isn't sufficient for any group to invest in.
- **Deploy and rollup latency.** In order to test if our changes are effective, we need to wait for more events to roll in. This will cause the work to take longer than it would if we were seeing results in real time. 

These are the known challenges, but there may be additional issues that have yet to be identified.

### Measuring noise: why archived-issue events are excluded

Sentry's event-volume statistic counts every accepted event, including those from issues already triaged and archived-until-escalation. The raw number therefore understates the triage-experience improvement.

Suppressing these events at the source doesn't work for shared error handlers: they carry both noise and signal, and removing the capture call deletes both. Archiving in Sentry keeps the signal, resurfaces issues if they escalate, and is reversible. Source-level filters remain the right tool for events that are never signal.

The measurement is the 30-day `count()` via the Sentry events API minus the same query filtered to `is:ignored`. `is:ignored` reflects current issue state, so trailing events of freshly archived issues count retroactively — intended, since the metric reflects the current triage state.

#### Reporting the archived total

Excluding archived events makes the metric sensitive to triage decisions, not just shipped code. An issue archived-until-escalation only resurfaces if it exceeds its own volume forecast, so a steady high-volume issue can stay archived indefinitely.

To keep this visible, the Task Group's closing report states all three figures: raw accepted volume, archived-issue events, and the net. The Task Group establishes the baseline; keeping noise low afterwards is the owning teams' responsibility.

## Exit Criteria

1. **Noise reduced at source and through triage (primary outcome).** Sentry SDK configuration and inbound filters are updated, and known non-actionable issues are archived in Sentry, such that 30-day event volume in `gitlabcom-clientside`, **excluding events from archived issues**, is reduced by ≥50% to less than 12.4M events from the March 2026 baseline of ~24.8M error events (see [Context](#context) for the screenshot and live view, and [Measuring noise](#measuring-noise-why-archived-issue-events-are-excluded) for why archived-issue events are excluded).
2. **Automation exists and has run on real issues.** The automation runs on a daily schedule, fetches Sentry issues, opens corresponding GitLab issues routed through `feature_category`, and produces Duo Developer triage (root cause, code references, proposed fix) on each. The automation has run for at least 2 weeks against real owning groups, with results recorded somewhere reviewable (issue link, Duo's output, owning-group action taken).
3. **The automation is useful enough to keep running.** The main thing we look at: when the automation opens a GitLab issue, does the owning group actually do something with it within 14 days — pick it up, assign it, put it on a milestone, fix it — or do they just close it and move on? That tells us whether Duo's triage is helping or just adding noise. Two extra checks back this up: we read through a handful of Duo's analyses by hand to see if they actually point at the real bug, and we look at how many issues got opened in total (a few good ones is a very different result from a flood of mediocre ones). At the end, the Task Group writes down a clear yes-or-no call with the reasoning. **"No, this didn't work, and here's what we learned" is a fine answer** — we don't pick a target percentage up front, because figuring out what "useful" looks like is the whole point of trying this.
4. **Long-term ownership is resolved.** Either a long-term owner has been identified for the automation, has been involved in the last 4 weeks of the Task Group, and has accepted a documented handover **or** no owner has been found and the automation is sunset at Task Group end with the rationale documented.

## Closing report

The Task Group closed on 2026-09-28. Exit criteria 1 to 3 are met. Exit criterion 4 is resolved with an amendment: no group took over long-term ownership of the automation, and it was not sunset either. It continues in maintenance mode under the former DRI. The reasoning is below.

### 1. Noise reduction

All three figures, measured on 2026-09-28 over the trailing 30 days through the Sentry events API (`project=4`, `dataset=errors`, `statsPeriod=30d`, `field=count()`):

| Figure                                             | Events         |
| -------------------------------------------------- | -------------- |
| Raw accepted volume                                | 7,903,384      |
| Events from archived issues (`is:ignored`)         | 4,558,842      |
| **Net (raw minus archived)**                       | **3,344,542**  |
| March 2026 baseline                                | ~24,800,000    |
| Target (at least 50% reduction)                    | <12,400,000    |

The net figure is down 86.5% from the baseline; the raw figure alone is down 68%. Both are well inside the target.

![Sentry Discover, gitlabcom-clientside, September 2026: 7.9M error events in 30 days](/images/company/working-groups/task-groups/sentry-signal-loop/closing-september-2026.png)

Closing measurement: 7.9M raw error events in the 30 days to 2026-09-28, compared to ~24.8M in March.

Where the reduction came from: source-level filters in the Sentry SDK configuration (non-actionable error patterns, expected `4xx` responses, extension noise), Sentry inbound filters, and archiving known non-actionable issues in Sentry so they no longer surface in triage.

### 2. The automation

The Sentry Signal Loop is a scheduled pipeline in [duo-sentry-insights](https://gitlab.com/gitlab-org/frontend/duo-sentry-insights). Once a day (or week, per schedule) it fetches the new Sentry issues for one `feature_category`, mirrors each into a confidential `gitlab-org/gitlab` issue, and asks Duo Developer to triage it. Humans decide; the pipeline does the legwork.

What shipped:

- Fetch, enrich, reconcile, plan, apply stages. Dry-run by default, with a human-readable plan as a pipeline artifact.
- Deduplication through a `<!-- sentry-issue-id -->` marker in the issue description, plus a link back from the Sentry issue.
- Routing by `feature_category`, with DRI assignment, optional group label, and optional parent epic.
- Duo Developer triage on every created or reopened issue: Signal or Noise verdict, confidence, evidence level, root cause, code references, proposed fix, and a recommended Sentry disposition.
- A dominance gate: an error is only mirrored for the category that produces most of its events, so shared components (navigation, session modal, timestamps) do not land in every team's run.
- A per-run creation cap ranked by affected users, added after a dry run for a high-volume category showed it would have opened about 100 issues.
- Release-aware regression detection: a closed issue is only reopened when a release created after the close throws the error. Events from long-lived browser tabs on old bundles get a single comment instead of a reopen.
- Onboarding is one pipeline schedule; offboarding is turning it off.

The loop ran from 2026-05-22 to Task Group close and mirrored 258 Sentry issues to 9 groups. Six groups have set up a pipeline schedule for their feature category; five of those schedules are active at close.

The original plan scaled from opt-in to default opt-out. We stayed opt-in. Opening issues for teams that did not ask for them was the biggest risk to trust in the automation, and slower adoption was the better trade.

### 3. Is it useful enough to keep running? Yes

Measured on 2026-09-28 across all issues labeled `Task Group::Sentry Signal Loop`:

- **78% pickup.** Of the 154 mirrored issues older than 14 days, 120 were assigned, put on a milestone, closed, or linked to a merge request by the owning group. 50 were closed, 24 of them through a fix MR. Four groups acted on every issue they received.
- **Duo triage on 248 of 258 issues.** 151 Signal, 97 Noise; 193 backed by a resolved stack trace. Signal verdicts led to 44 fix MRs, Noise verdicts to 2. Owning groups treat the verdict as a usable first pass.
- **No flood, no duplicates.** No group asked to stop, and the pipeline never opened two GitLab issues for the same Sentry issue.

### 4. Ownership: maintenance mode under the former DRI

Exit criterion 4 allowed two outcomes: an owning group, or sunset. Neither happened.

Developer Experience and the Observability team were both asked and both declined for capacity reasons. They confirmed Sentry itself is in maintenance mode and has no usage owner, and that self-service ownership ("you build it, you run it") is the expected default going forward.

Sunsetting a tool that five groups actively rely on, and that they were encouraged to adopt, would have been the worse outcome. So the resolution is:

- The automation stays running. Each consuming group owns its own pipeline schedule and can switch it off at any time.
- The former DRI maintains the shared repository, the two access tokens it runs on, and their rotation. Scope is bug fixes and breakage caused by Sentry or GitLab API changes. No new features. Expected effort is close to zero hours per month.
- Operational details live in the project's `OPERATIONS.md`.
- Kill switch: disable the pipeline schedules. Nothing else runs.
- This arrangement is re-evaluated if the maintainer changes role, if token custody cannot be kept, or if a group wants to take ownership.

## Roles and Responsibilities

| Task Group Role            | Person          | Title                                                        |
| -------------------------- | --------------- | ------------------------------------------------------------ |
| DRI                        | [Jannik Lehmann](https://gitlab.com/jannik_lehmann)  | Senior Frontend Engineer, AI-Powered:AI Catalog              |
| Maintainer (after close)   | [Jannik Lehmann](https://gitlab.com/jannik_lehmann)  | Senior Frontend Engineer, AI-Powered:AI Catalog              |
