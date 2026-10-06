---
title: "Flaky tests"
---

## Introduction

This page describes GitLab's organizational process for detecting, reporting, and managing flaky tests. For technical guidance on debugging and fixing flaky tests, see [Unhealthy Tests (Developer Docs)](https://docs.gitlab.com/development/testing_guide/unhealthy_tests/). For quarantine procedures and syntax, see [Quarantine Process (Handbook)](../quarantine-process/) and [Quarantining Tests (Developer Docs)](https://docs.gitlab.com/development/testing_guide/quarantining_tests/).

A flaky test is an unreliable test that occasionally fails but passes eventually if you retry it enough times. Flaky tests can be a result of brittle tests, unstable test infrastructure, or an unstable application. We should try to identify the cause and remove the instability to improve quality and build trust in test results.

## Why is flaky tests management important?

- Flaky tests undermine test results, leading to engineers disregarding test failures as flaky.
- Manual retries to try to get flaky tests to pass, and the effort needed to investigate flaky tests as failures are a significant waste of time.
- Managing flaky tests by quickly fixing the cause or removing the test from the test suite allows test time and costs to be used where they add value.

## Reporting of Top Flaky Test Files

GitLab uses custom tooling to automatically identify and report the most impactful flaky test files that block CI/CD pipelines. The [ci-alerts automation](https://gitlab.com/gitlab-org/quality/analytics/ci-alerts) creates issues for test files causing repeated pipeline failures, which are then triaged and assigned to Engineering Managers for resolution.

**View all top flaky test file issues:** [automation:top-flaky-test-file label](https://gitlab.com/gitlab-org/quality/test-failure-issues/-/work_items?sort=created_date&state=opened&label_name%5B%5D=automation%3Atop-flaky-test-file&not%5Blabel_name%5D%5B%5D=quarantine&not%5Blabel_name%5D%5B%5D=flaky-test%3A%3Afalse-positive&first_page_size=20)

**Top flaky test file issues open >24 hours:** [GLQL Tracking Issue](https://gitlab.com/gitlab-org/quality/test-failure-issues/-/work_items/43806)

**Flaky test file issues that remain open for longer than 24 hours will be escalated as production incidents.**

### How It Works

The ci-alerts system analyzes test failure data from ClickHouse to identify test files with the highest impact on pipeline stability. It classifies test files into three categories:

1. **Flaky**: Failures spread over 3+ days, still actively failing (≤3 days since last failure)
2. **Master-broken**: High-volume incidents (≥30 in 12h with 40%+ concentration OR 60+ absolute)
3. **Unclear**: Don't meet classification criteria

For detailed information about the classification algorithm and configuration, see the [ci-alerts flaky tests reporting documentation](https://gitlab.com/gitlab-org/quality/analytics/ci-alerts/-/blob/main/doc/flaky_tests_reporting.md).

### Frequency

We create top flaky tests issues weekly (Sundays at 10:00 UTC)

### Triage Process

Issues created by the automation are triaged by the Development Analytics team and dispatched to the responsible Engineering Managers. The complete triage workflow is documented in the [ci-alerts TRIAGE.md](https://gitlab.com/gitlab-org/quality/analytics/ci-alerts/-/blob/main/TRIAGE.md).

**Key steps:**

1. Initial triage to verify genuine flakiness
2. Dispatch to responsible product group with EM mention

### For Engineering Managers

If you've been assigned a top flaky test file issue:

1. **Review the issue description** - Contains impact metrics, Grafana dashboard link, and recommended actions
2. **Assess the situation** - Use the Grafana dashboard to understand failure patterns
3. **Take action** - See [Urgency Tiers and Response Timelines](#urgency-tiers-and-response-timelines) for timeline guidance

For guidance on quarantining tests, see the [Quarantine Process (Handbook)](../quarantine-process/) and [Quarantining Tests (Developer Docs)](https://docs.gitlab.com/development/testing_guide/quarantining_tests/).

### For Assigned ICs

Engineering managers will assign flaky test issues to an IC with immediate capacity. As an IC, if you have capacity and see one for your team unassigned, pick it up immediately for development. When you are assigned to a flaky test issue, you are expected to drop what you're doing and fix the test today.

In service of resolving these issues immediately, please also drop what you're doing to review any of these fixes for someone else who's assigned to the failing test. **This is synchronous work;** ping people directly, have the code reviewed immediately, get your approvals and merge your changes.

Lean hard on the agents to get these fixes written and merged. When unblocking all of the rest of development on the gitlab project, speed is critical!

#### Workflow

1. A flaky test issue is opened in status **New** and assigned to the attributable EM.
2. An IC picks up the issue, or is assigned by an EM. The issue and any sub-tasks should worked on immediately, set to the current milestone, and moved to **In Development**.
3. The review phase for these MRs should be very short. Assigned ICs should be working directly and synchronously with at least one other developer to merge their fixes.
4. If an engineer's day ends and there are still changes to be made, the assigned engineer is responsible for handing off the work to someone in another time zone to be assigned and continue working. These issues and MRs are not to be left idle overnight.
5. When enough fixes have been made that the test should no longer be blocking other developers, the flaky test file issue should be moved to **Verification**.
6. After **3 days** without a failure, the DevEx flaky test automation will close the issue.

#### Urgency Tiers and Response Timelines

Teams have 24 hours from the flaky test file being identified to ship their fixes, after which the issue will be escalated to a Severity 3 production incident and require the post-incident review process.

+After X (TBD) hours at a Severity 3, the incident will escalate to a Severity 2.

These timelines guide when a test should be quarantined if it cannot be fixed. For quarantine procedures and technical implementation, see [Quarantine Process (Handbook)](../quarantine-process/) and [Quarantining Tests (Developer Docs)](https://docs.gitlab.com/development/testing_guide/quarantining_tests/).

## Additional resources

- [Quarantine Process (Handbook)](../quarantine-process/) - Overall process for quarantined tests at GitLab
- [Unhealthy Tests (Developer Docs)](https://docs.gitlab.com/development/testing_guide/unhealthy_tests/) - Technical reference for debugging and reproducing flaky tests
- [Quarantining Tests (Developer Docs)](https://docs.gitlab.com/development/testing_guide/quarantining_tests/) - Technical reference for quarantine syntax and implementation
- [Flaky tests dashboard](https://dashboards.devex.gitlab.net/d/ddjwrqc/flaky-tests-overview)
