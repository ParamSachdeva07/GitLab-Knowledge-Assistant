---
title: "Test Governance Group (Retired)"
description: "The Test Governance group has been retired. Feature teams now own their full testing lifecycle."
---

{{% alert title="This group has been retired" color="warning" %}}
The **Test Governance** group no longer exists. Testing is not a centrally-managed function.
{{% /alert %}}

## What changed

As part of the DevOps transformation, GitLab moved away from a centrally-managed testing function. The Test Governance group has been retired.

**Modular feature teams — and the monolith — own their full testing lifecycle at every level, including end-to-end (E2E)**: test design, authoring, maintenance, triage, and quality. There is no dedicated person or central team that writes or maintains tests — E2E included — on a team's behalf.

**Release readiness is a decision made within the team.** No external team approves a rollout to GitLab.com. Automated pipeline checks (for example, staging-canary smoke tests) are *mechanisms* that support that decision — they are not an external approver.

## What DevEx does now

The [Developer Experience department](../) **provides guidance and upskilling** so teams can own their testing effectively, and it **owns the shared test infrastructure** (test environments, frameworks, tooling, dashboards, and the E2E pipeline).

Triage and first response for failures belong to the **owning feature team**. DevEx is a **last-resort escalation** for severe cases that genuinely require deep expertise — not the default contact when something breaks.

For guidance, reach out in [`#s_developer_experience`](https://gitlab.enterprise.slack.com/archives/C07TWBRER7H).

## Where to go

1. [Testing at GitLab](/handbook/engineering/testing/) — testing philosophy, ownership model, and support
1. [Developer Experience department](/handbook/engineering/infrastructure-platforms/developer-experience/)
1. [Quality is everyone's responsibility](/handbook/engineering/development/principles/#quality)

### Owning your testing — helpful resources

**Coverage strategy and levels**

* [GitLab testing overview](/handbook/engineering/testing/) — sets the overall expectation that teams own comprehensive test coverage across unit, integration, and end-to-end tests, with end-to-end coverage focused on critical user flows.
* [Testing levels](https://docs.gitlab.com/development/testing_guide/testing_levels/) — the clearest statement of the testing pyramid: most coverage should live at the unit level, fewer tests at higher layers, and E2E should be the smallest portion because it is the most expensive to run and maintain.
* [Testing strategy](https://docs.gitlab.com/development/testing_guide/testing_strategy/) — the blueprint for GitLab automated testing: where tests run and when they execute, so teams know which suite carries which risk.
* [Test Coverage](/handbook/engineering/testing/test-coverage/) — how GitLab thinks about coverage across special scenarios such as offline/air-gapped testing and upgrade-path coverage, not just feature-level E2E.

**Writing tests**

* [Testing best practices](https://docs.gitlab.com/development/testing_guide/best_practices/) — everything you should know about writing good tests: test design, RSpec, FactoryBot, system tests, and parameterized tests.
* [Frontend testing standards and style guidelines](https://docs.gitlab.com/development/testing_guide/frontend_testing/) — how to write good frontend tests with Jest, including testing promises and stubbing.
* [Beginner's guide to writing end-to-end tests](https://docs.gitlab.com/development/testing_guide/end_to_end/beginners_guide/) — check existing lower-level coverage first; if unit/feature/integration coverage is already sufficient, an additional E2E test may not be needed.
* [End-to-end testing guide](https://docs.gitlab.com/development/testing_guide/end_to_end/) — how GitLab runs E2E, selective execution, and the principle of avoiding E2E coverage when a lower-level feature test already covers the risk.

**Keeping your tests healthy**

* [Unhealthy tests](https://docs.gitlab.com/development/testing_guide/unhealthy_tests/) — the kinds of flaky tests we encounter and how to identify and fix them, so your team keeps its own suite reliable.
* [Flaky tests](/handbook/engineering/testing/flaky-tests/) — how top flaky tests are automatically detected and reported for teams to act on.
* [Quarantine process](/handbook/engineering/testing/quarantine-process/) — how tests are quarantined and how the owning team (by `feature_category`) is responsible for resolving or removing them.
