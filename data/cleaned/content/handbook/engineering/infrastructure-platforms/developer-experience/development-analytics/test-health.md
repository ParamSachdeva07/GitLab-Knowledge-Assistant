---
title: "Test Health"
description: "Per-group test-suite health scores across the Flaky, Quarantine, and Slow pillars"
---

## What it measures

Test Health scores every stage group's test suite from three angles, called pillars: Flaky (open flaky-test debt and the pipelines it blocks), Quarantine (tests removed from the blocking suite and how long they have sat there), and Slow (test files slow enough to drag pipeline duration). Each pillar is a 0 to 100 score per group, where 100 means no measured debt.

At launch the scores cover RSpec backend tests and QA end-to-end tests in `gitlab-org/gitlab`. Jest, contract tests, and Workhorse Go tests are deferred.

## How to read a score

Scores carry a red/amber/green status: 0 to 29 is red, 30 to 70 is amber, 71 to 100 is green. Every deduction is itemized. Each pillar section on a group's detail dashboard ends with a score-math panel showing exactly what was charged, for example: Issue backlog -7, Blocked pipelines -70 (at cap), Score 23. Stage, section, and org scores are the mean of their member groups' scores, so they read as "the average group in this slice".

## Where to find your group

Start at the [Test Health dashboard](https://dashboards.gitlab.net/d/dx-test-health). The grid shows one row per group with all three pillar scores; your group's row links to its detail dashboard, which carries the score breakdown, 90-day trends, and the specific tests, issues, and files behind each number.

## Acting on a red Flaky score

ci-alerts opens an issue in `gitlab-org/quality/test-failure-issues` for each top flaky test file (label `automation:top-flaky-test-file`) with the failure evidence attached, and sets a due date of the next business day. From there:

1. Triage the issue promptly: one in its first week costs the least, one past its due date with no `workflow::` label costs the most.
1. If the detection is wrong, apply `~"flaky-test::false-positive"`.
1. Quarantining a file moves its backlog cost from the Flaky pillar to the Quarantine pillar (priced by age). Any failures the file still causes keep counting in the Flaky blast radius, so quarantine parks the debt without hiding live damage.
1. Moving a fixed issue to `workflow::verification` drops its cost to the minimum while it waits out the detection window.

## Roadmap

The score formulas are calibrated so every action a team takes moves its score. A low score doesn't trigger anything on its own yet. But flaky-test issues, which feed the scores, now carry a due date of the next business day. Please start improving low scores now.

Questions and feedback: the [Test Health feedback issue](https://gitlab.com/gitlab-org/quality/analytics/team/-/work_items/734) (GitLab internal).
