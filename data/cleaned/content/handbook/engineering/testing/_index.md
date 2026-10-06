---
title: Testing
---

> ⚠️ Note: As part of the DevOps transformation, testing is no longer a centrally-managed function. Feature teams (and the monolith) own their full testing lifecycle, and release readiness is decided within the team. Developer Experience (DevEx) provides guidance and upskilling and owns the shared test infrastructure, acting as a last-resort escalation only. The former Test Governance group has been [retired](../infrastructure-platforms/developer-experience/test-governance/), the Software Engineer in Test (SET) role has transitioned to Backend Engineer, and the Pipeline DRI process is being removed. Some pages in this section are still being revised to fully reflect this model.

Welcome to the Testing Guide. Pages in this section provides information about
testing practices, methodologies, and tools used in our development workflow.
Effective testing is crucial for maintaining code quality, preventing
regressions, and ensuring that our software meets requirements.

## Introduction to Testing at GitLab

This introduction provides new engineers with an
overview of our testing philosophy, practices, and the support available to help
you contribute effectively to our quality engineering efforts.

## How We Test

### Our Testing Philosophy

At GitLab, we believe that quality is everyone's responsibility, and testing is
integrated into every stage of our development process rather than being a
separate phase. Our approach is built on industry best practices and GitLab's
core values.

**Test Pyramid Approach**: [We champion the concept of the test pyramid](https://docs.gitlab.com/development/testing_guide/testing_levels/),
prioritizing fast, reliable tests at the base (unit tests) while using fewer,
more focused tests at higher levels (integration and end-to-end). This approach
gives us:

- Rapid feedback during development
- Reliable detection of regressions
- Efficient use of CI/CD resources
- Maintainable test suites

**Strategic Testing Focus**: Our testing strives to consider risk analysis and
input on test strategy, helping us focus testing efforts on critical user
journeys and high-impact areas. We make strategic decisions about where to
invest our testing efforts based on user impact and business needs.

**Automated Quality Checks**: Testing is embedded throughout our [product development workflow](/handbook/product-development/how-we-work/product-development-flow/) as automated mechanisms — not as approvals from an external team:

- Pre-commit and pre-receive hooks for immediate feedback
- [Merge request pipelines with mandatory code reviews](../../engineering/workflow/code-review/) that must pass before code integration
- Deployment pipelines with comprehensive test suites
- Post-deployment monitoring and validation

### Testing Ownership Model

**Teams own their testing**: Every feature team — and the monolith — owns its **full testing lifecycle at every level, including end-to-end (E2E)**: test design, authoring, maintenance, and triage. Quality is everyone's responsibility, and there is no central team that writes, owns, or maintains tests — E2E tests included — on a team's behalf. Owning your tests includes:

- Writing unit tests for new functionality
- Adding integration tests for API endpoints and service interactions
- Writing and maintaining end-to-end tests for your critical user flows
- Maintaining, triaging, and fixing flaky or outdated tests in your `feature_category`

**Release readiness is the team's decision**: The decision that a release is ready to roll out to GitLab.com is made **within the owning team**. No external team approves the rollout. Automated pipeline checks support that decision but do not replace it.

**What Developer Experience provides**: [DevEx](../../engineering/infrastructure-platforms/developer-experience/) **enables** teams rather than doing the testing for them. DevEx:

1. Provides guidance, best practices, and upskilling so teams can test effectively
1. Owns the shared test infrastructure — test environments, frameworks, tooling, dashboards, and the E2E pipeline
1. Acts as a **last-resort escalation** for severe issues that genuinely require deep expertise — not the default contact when something breaks

## When We Test

### Development Workflow Integration

**Testing Early and Often**: We encourage writing tests alongside feature
development to ensure clear requirements understanding, better code design,
and comprehensive coverage from the start.

**Continuous Integration**: Every merge request triggers automated testing:

- Unit and integration tests run on every push
- Feature tests execute for UI changes
- Performance tests validate critical paths
- Security scans check for vulnerabilities
- End-to-end tests for critical user journeys

### Release and Deployment Testing

**Pre-Deployment Validation**: Before code reaches production, automated mechanisms provide signal to the owning team — the release decision remains the team's:

- [Smoke tests verify basic functionality](https://docs.gitlab.com/development/testing_guide/end_to_end/debugging_end_to_end_test_failures/#staging-canary); failures in staging-canary automatically block the deployment pipeline
- Performance tests ensure acceptable response times
- End-to-end tests validate critical user journeys
- Canary deployments allow gradual rollout with monitoring

**Post-Deployment Monitoring**: Testing doesn't stop at deployment. Post-deployment monitoring is also done including:

- Synthetic monitoring simulating user interactions
- Performance monitoring tracking application health
- Error tracking identifying issues in real-time
- [Feature flag testing enabling safe experimentation](https://docs.gitlab.com/development/testing_guide/end_to_end/feature_flag_testing/)

## Support Available

### Getting Help with Testing

**Getting guidance**: Your team owns its testing, but you don't have to figure everything out alone. For guidance and best practices, reach out to Developer Experience in [`#s_developer_experience`](https://gitlab.enterprise.slack.com/archives/C07TWBRER7H). Please treat DevEx as a resource for guidance and for severe issues that require deep expertise — not as the owner of your tests or your triage.

### Developer Experience Department

**Developer Experience** [provides testing infrastructure, tools, and frameworks](../../engineering/infrastructure-platforms/developer-experience/), and offers guidance and upskilling so teams can own their testing effectively. This includes:

- Testing pipeline optimization
- Test automation libraries and utilities
- CI/CD testing infrastructure
- Performance testing capabilities
- Guidance on testing strategy, coverage, and debugging flaky or complex tests

Teams own the day-to-day work — writing tests, triaging failures, and deciding release readiness. DevEx is a **last-resort escalation** for severe cases that genuinely require deep expertise.

**On-Call Support**: [Engineering teams participate in incident management rotations](../../engineering/on-call/) to ensure rapid response to production issues

### Self-Service Resources

#### Documentation and Guides

- [GitLab Testing Guide](https://docs.gitlab.com/development/testing_guide) - Guidelines for automated testing in the GitLab project
- [Testing Levels, Tooling, and Strategy](https://docs.gitlab.com/development/testing_guide/testing_levels/) - Detailed technical implementation guide
- [Testing Best Practices](https://docs.gitlab.com/development/testing_guide/best_practices/) - Everything you should know about how to write good tests in the GitLab project
- [Code Review Guidelines](../../engineering/workflow/code-review.md) - Mandatory review process for all merge requests

#### Test Health and Pipeline Stability

- [Flaky Tests](flaky-tests/_index.md) - Automated detection and reporting
  - [Reporting of Top Flaky Test Files](flaky-tests/_index.md#reporting-of-top-flaky-test-files) - Weekly assignments for high-impact flaky tests
- [Product Engineer guide to E2E test failure issues](guide-to-e2e-test-failure-issues.md)
- [Unhealthy Tests (Developer Docs)](https://docs.gitlab.com/development/testing_guide/unhealthy_tests/) - Technical debugging reference for GitLab contributors
- [🪄 Debug MR Test Failures with Duo](using-duo-to-debug-test-failures.md#-using-duo-to-debug-and-fix-test-failures-in-your-merge-request) - Use Duo to quickly diagnose and fix test failures in your MR
- [🔥 Debug Live Environment Test Failures with Duo](using-duo-to-debug-test-failures.md#-using-duo-to-debug-live-environment-test-failures) - Use Duo to quickly diagnose and fix test failures in your MR

#### 📹 GitLab End-to-End Testing Overview (Video)

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/KbQzrVJMvNQ" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

**Duration:** ~30 minutes
**Level:** Beginner to Intermediate

This video covers:

- 📁 [Directory structure and test organization](https://www.youtube.com/watch?v=KbQzrVJMvNQ&t=150)
- 🕵️ [Finding and understanding existing tests](https://www.youtube.com/watch?v=KbQzrVJMvNQ&t=322)
- 🤿 [Deep dive into E2E test architecture](https://www.youtube.com/watch?v=KbQzrVJMvNQ&t=399)
- 📍 [Where E2E tests run in our infrastructure](https://www.youtube.com/watch?v=KbQzrVJMvNQ&t=978)
- 🐛 [Debugging test failures from merge requests](https://www.youtube.com/watch?v=KbQzrVJMvNQ&t=1084)
- 🚩 [Working with feature flags in tests](https://www.youtube.com/watch?v=KbQzrVJMvNQ&t=1406)
- 🔧 [Troubleshooting common failure issues](https://www.youtube.com/watch?v=KbQzrVJMvNQ&t=1552)
- 💻 [Running tests locally in your GDK](https://www.youtube.com/watch?v=KbQzrVJMvNQ&t=1721)

- [Presentation Slides](https://docs.google.com/presentation/d/1eYLuTdSpI-H0ZalzoqH7Ee8cprjmL1FNoV0XwRPY4-4/edit?usp=sharing)

#### Further Reading

- [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) - A deep dive into the "Test Pyramid"

#### Community and Communication

- For testing questions and discussions, use the [`#s_developer_experience`](https://gitlab.enterprise.slack.com/archives/C07TWBRER7H) Slack channel

#### Tooling and Automation

- Test generators and templates for common scenarios
- [Automated workflow tooling](../../engineering/infrastructure-platforms/developer-experience/workflow-automation/) for issue and MR triage
- CI/CD pipeline templates with testing best practices
- Performance and coverage monitoring dashboards

---

*For detailed technical implementation guidance, refer to our comprehensive
[Development Testing Guide](https://docs.gitlab.com/development/testing_guide/).
For guidance, reach out to Developer Experience in [`#s_developer_experience`](https://gitlab.enterprise.slack.com/archives/C07TWBRER7H).*
