---
title: "Developer Experience Dashboards"
description: "This handbook page serves as a central repository for all our Developer Experience dashboard details"
---

> In pursuit of a resilient, efficient, and fortified platform, our Test Platform sub-department provides instrumental
> support through the creation and maintenance of an array of dashboards. These critical tools capture detailed test
> health across the environments, flag performance anomalies, and contribute to rigorous test infrastructure.

## Dashboards

|Category|Link (Internal Only)|Description|DRI|
|---|---|---|---|
|CI metrics|[dx: CI Overview](https://dashboards.gitlab.net/d/dx-ci-overview)| CI pipelines per project. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Pipeline Metrics](https://dashboards.gitlab.net/d/dx-pipeline-metrics)| Overview of tiered pipelines. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Job Metrics](https://dashboards.gitlab.net/d/dx-job-metrics)| Overview of CI jobs metrics. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Failure Analysis Dashboard](https://dashboards.gitlab.net/d/dx-failure-analysis)| CI pipelines failure analysis. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Master-Broken Incident Detection](https://dashboards.gitlab.net/d/dx-master-broken-incident-detection)| Master-broken incidents related dashboard. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Test Governance Key Metrics](https://dashboards.gitlab.net/d/dx-test-governance)| Key metrics related to CI/CD pipeline execution in gitlab-org/gitlab. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
|Test metrics|[dx: Test Health](https://dashboards.gitlab.net/d/dx-test-health)| Per-group test-suite health scores across the Flaky, Quarantine, and Slow pillars. [How to read Test Health scores](/handbook/engineering/infrastructure-platforms/developer-experience/development-analytics/test-health). |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Test Suite Overview](https://dashboards.gitlab.net/d/dx-suite-overview/dx3a-test-suite-overview)| Overview of test suite health and status.|[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Predictive Tests](https://dashboards.gitlab.net/d/dx-predictive-tests)| Metrics for predictive tests. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Quarantined Tests](https://dashboards.gitlab.net/d/dx-quarantined-tests)| Quarantined tests overview. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Test File Failure Overview](https://dashboards.gitlab.net/d/dx-test-file-failure-overview)| All test failures aggregated by test file. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Single Test Overview](https://dashboards.gitlab.net/d/dx-single-test-overview)| Individual tests overview per test file. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Flaky Tests Overview](https://dashboards.gitlab.net/d/dx-flaky-tests-overview)| General flaky tests overview. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Flaky Test File Failure Overview](https://dashboards.gitlab.net/d/dx-flaky-test-file-overview)| Overview of test failures by test file. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Test File Runtime Overview](https://dashboards.gitlab.net/d/dx-test-file-runtime-overview)| General overview of runtimes per test file. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: E2E pipeline metrics](https://dashboards.gitlab.net/d/dx-e2e-metrics)| Daily metrics related to E2E test execution in gitlab-org/gitlab. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
|Code & Test Coverage|[dx: Code Coverage Health Check](https://dashboards.gitlab.net/d/dx-code-coverage-health-check)| Code coverage health. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Source to Test Coverage](https://dashboards.gitlab.net/d/dx-source-to-test)| Code coverage overview per source file. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Test to Source File Coverage](https://dashboards.gitlab.net/d/dx-test-to-source-file-coverage)| Code coverage overview per test file. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Coverage Actionables](https://dashboards.gitlab.net/d/dx-code-coverage-actionables)| Test coverage gaps dashboard. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Coverage Infrastructure](https://dashboards.gitlab.net/d/dx-code-coverage-infrastructure)| Test type distribution in test coverage. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|
||[dx: Coverage Trends](https://dashboards.gitlab.net/d/dx-code-coverage-trends)| Coverage metrics over time by category, stage, and product level. |[Development Analytics](../../infrastructure-platforms/developer-experience/development-analytics)|

## Contributing to the Dashboards

If you have any questions or suggestions about the dashboard, please contact the respective DRI or submit an issue in
our [tracking system](https://gitlab.com/gitlab-org/quality/quality-engineering/team-tasks/-/issues/new).
