---
title: Support Training Module Maintainer
description: Understanding the role of a Support training module maintainer
---

## Overview

A **Training Module Maintainer** is the primary steward of a specific Support training module. Maintainers are responsible for keeping the module accurate, aligned with current Support workflows and product documentation, and effective as a learning/onboarding experience. They are also the default reviewers for proposed changes to the module.

Everyone can contribute improvements to a module; maintainers provide structure, review, and continuity.

## Who can be a maintainer

A Training Module Maintainer is typically any of the following:

- A Support Engineer with demonstrated expertise in the module’s **area** (for example, Product Knowledge, Troubleshooting & Diagnostics, Customer Service).
- A [support stable counterpart](/handbook/support/support-stable-counterparts/) for the relevant [product group](/handbook/product/categories/features/).
- Someone who has:
  - Completed the module themselves (or an equivalent level of knowledge), and
  - Worked a meaningful number of tickets in the module’s topic.

Modules should have **at least one _active_ maintainer**, however, it is possible for a complex module to have multiple maintainers. Having multiple maintainers offers several benefits: they can peer review each other's changes and avoid a single point of failure. It is also beneficial to have maintainers spread across different regions to ensure broader availability and faster response times.

If you are a training module maintainer, be sure to let your manager know in your 1:1 and share updates you are making to modules in your document to make your manager aware!

## Time commitment and cadence

Approximate expectations per module:

- **Baseline:** ~1–2 hours per month on average.
- **Reviews:**
  - Respond to review requests on MRs that modify the module.
  - Respond to automated, scheduled or manual pings that a module review is needed.
- **Refresh:**
  - Perform a review at least every **6 months**, and sooner when related product features, docs, or workflows change significantly.

If a maintainer’s availability changes (for example, role change, extended leave), they should work with their manager to hand off ownership.

## Responsibilities

### 1. Content accuracy and alignment

Maintainers ensure the module:

- Has an accurate **Goal** and **Objectives** section that reflects what learners should be able to do after completion.
- Lists correct **prerequisites** and dependencies (for example, required earlier modules or baseline knowledge).
- References up-to-date:
  - Product documentation.
  - Handbook workflows.
  - External resources (courses, vendor docs, videos), where used.

When maintainers become aware of material changes (for example, new features, renamed settings, deprecations, or new workflows), they either:

- Update the module themselves, or
- Create/triage an issue and help review an MR from another contributor.

### 2. Template and workflow stewardship

Each training module lives as an issue template in the Support Training project. Maintainers are responsible for keeping the template itself in good shape:

- Keep the **stage structure** from the training [module template](https://gitlab.com/gitlab-com/support/support-training/-/blob/main/module-template.md?ref_type=heads).
- Ensure **tasks and checklists** reflect how we actually work (for example, ticket volumes, tools, required issue links, self-assessment steps).
- Ensure the module is relevant to support's work on tickets in the area.
- Maintain **metadata and labels**, including:
  - `maintainers:` list in the YAML frontmatter, if present.
  - Standard labels (for example `~module`, `~"Module::<Name>"`, and relevant group or category labels).
- Ensure the module is correctly discoverable, categorised and advertised in:
  - The Skills Catalog / module inventory.
  - Any learning pathways that reference it.
  - [Support Week in Review](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review#support-week-in-review) (SWIR)

### 3. Review and collaboration

Maintainers act as the **first-line reviewers** for proposed changes to their module:

- Review MRs that modify the module content, structure, or metadata.
- Apply the Support “[Guideline to update Support Training module](https://gitlab.com/gitlab-com/support/support-training/-/blob/main/README.md?ref_type=heads#guideline-to-update-support-training-module)” process:
  - If a maintainer is available, they review and either approve or give feedback.
  - If they are unavailable, they help route to:
    - Another module maintainer, or
    - A subject-matter expert or Support Manager.
    - A relevant [Support Pods](/handbook/support/support-pods/) Slack channel

For substantive changes (for example, major restructuring, new assessments, or significant scope changes), maintainers:

- Loop in relevant subject-matter experts, SSCs, or product area leads (where needed).
- Confirm the updated module still fits into the broader learning paths and Support education strategy.
- Promote/advertise the changes in team calls and SWIR.

### 4. Learner experience and assessment

Maintainers help ensure the module is usable and effective for learners:

- Periodically (every 6 months) sanity-check that:
  - Tasks are clear and not unnecessarily blocking.
        - Learners should be able to complete the modules themselves.
  - Ticket and call requirements are realistic given expectations/workload capabilities.
  - Any quizzes or self-assessments are accessible.
- Review trainee and manager feedback (where available) and convert recurring themes into improvements:
  - Clarifying ambiguous instructions.
  - Adjusting the expected order of tasks where it makes sense.
  - Adding or simplifying examples, diagrams, or practice tasks.

### 5. Lifecycle decisions

Maintainers are key voices in deciding how the module evolves over time:

- Identify when a module should be:
  - **Refreshed** (minor content updates).
  - **Restructured** (for example, split into “Basics” and “Advanced”, or aligned to topic-based paths).
  - **Deprecated or merged** into another module.

## Expectations and success criteria

A Training Module Maintainer is succeeding when:

- **Freshness:** The module is reasonably up to date (no obviously broken links, obsolete workflows, or deprecated features in core tasks).
- **Responsiveness:** MRs and review requests receive an initial response within a reasonable timeframe.
- **Clarity:** New learners and their managers report that:
  - Instructions are clear.
  - The required work is achievable.
  - It’s obvious how to start, progress, and mark the module as complete.

## Out of scope

Maintainers are **not** solely responsible for:

- Personally delivering all training sessions tied to the module.
- Coaching every learner 1:1 through the entire module.
- Owning all content creation for the topic.

Instead, they:

- Provide a clear, up-to-date structure for others to contribute to.
- Review and guide contributions from Support Engineers, SSCs, product teams, and other stakeholders.
