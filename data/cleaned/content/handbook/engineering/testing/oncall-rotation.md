---
title: Developer Experience On-call Rotation
description: >-
  Developer Experience runs an EM-led incident management on-call rotation. Pipeline triage is owned by feature teams; there is no longer a centralized DevEx pipeline DRI rotation.
---

## Pipeline triage is owned by feature teams

As part of the DevOps transformation, **there is no longer a centralized Developer Experience pipeline triage (Pipeline DRI) on-call rotation.** Triaging and debugging E2E and scheduled pipeline failures is the responsibility of the **owning feature team** (identified by the failing test's `feature_category`/`product_group`), consistent with teams owning their full testing lifecycle.

Developer Experience owns the shared pipeline infrastructure and is a **last-resort escalation for emergencies only** — for example, a severe, cross-cutting failure that threatens GitLab.com and genuinely requires deep expertise the owning team cannot supply. It is not the default contact for routine pipeline failures.

- How to triage a failure: [Pipeline Triage](/handbook/engineering/testing/pipeline-triage/) — including [Prioritization and response expectations](/handbook/engineering/testing/pipeline-triage/#prioritization-and-response-expectations) — and [Debugging Failing E2E Tests](https://docs.gitlab.com/development/testing_guide/end_to_end/debugging_end_to_end_test_failures/).
- Self-service troubleshooting: [Using Duo to debug test failures](../testing/using-duo-to-debug-test-failures.md) and [Guide to E2E test failure issues](../testing/guide-to-e2e-test-failure-issues.md).
- Failing smoke specs in staging/canary automatically block the deployer pipeline and may be treated as production incidents — follow [I found a regression, what do I do next?](/handbook/engineering/deployments-and-releases/deployments/#i-found-a-regression-what-do-i-do-next).
- **Emergency escalation to DevEx**: for severe, cross-cutting issues, reach out in the [`#s_developer_experience`](https://gitlab.enterprise.slack.com/archives/C07TWBRER7H) Slack channel.

### Infrastructure and environment upgrades

Developer Experience owns the shared test environments and can advise on validating planned upgrades (infrastructure, database, service decomposition, etc.). The owning/requesting team is responsible for running and interpreting the validation tests for its own changes and for the release decision. For guidance planning an upgrade's test coverage, reach out early in [`#s_developer_experience`](https://gitlab.enterprise.slack.com/archives/C07TWBRER7H) and refer to the [Pipeline Triage](/handbook/engineering/testing/pipeline-triage/) guide.

## Developer Experience Sub-Department incident management on-call rotation

The EMs should share the responsibility of monitoring, responding to, and mitigating incidents.
Developer Experience Sub-Department's on-call does not include work outside GitLab's normal business hours. Weekends and [Family and Friends Days](/handbook/company/family-and-friends-day/) are excluded as well.
In the current iteration, incident management activities happen during each team member's working hours.

### Responsibility

- The Engineering Manager should ensure they have joined the Slack channel `#incidents`.
- The Engineering Manager should help with monitoring the incident management channel, tracking, directly helping, delegating, and raising awareness of incidents within the Developer Experience Sub-Department as appropriate.
- The current DRI should be clearly noted on the incident issue.
- If a corrective action is needed, the EM should make sure the DRI has created an issue and labeled it with ~'corrective action'.
- Everyone in the Developer Experience Sub-Department should support the on-call DRI and be available to jump on a Zoom call or offer help if needed.
