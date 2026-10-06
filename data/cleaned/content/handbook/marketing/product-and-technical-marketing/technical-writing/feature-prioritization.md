---
title: "Docs Engineering: Feature prioritization and process"
description: "How the Docs Engineering team prioritizes work and maintains the GitLab documentation platform."
---

## Overview

The Docs Engineering team maintains the GitLab product documentation platform using [kanban](https://en.wikipedia.org/wiki/Kanban_(development)) and milestone-based prioritization. We organize work into themes that balance new capabilities, platform health, and team productivity.

- [Docs website roadmap](https://gitlab.com/gitlab-org/technical-writing/team-tasks/-/issues/1455)
- [Workflow kanban board](https://gitlab.com/groups/gitlab-org/-/boards/4340643)
- [Feature prioritizaton board](https://gitlab.com/groups/gitlab-org/-/boards/9702008)

We take inspiration from GitLab's [product principles](/handbook/product/product-principles/) and [product development flow](/handbook/product-development/how-we-work/product-development-flow/), adapted for our team context.

## Issue lifecycle

### Create an issue

Anyone can [create an issue](https://gitlab.com/gitlab-org/technical-writing/docs-gitlab-com/-/issues/new?type=ISSUE) for the Docs website. Use the [bug template](https://gitlab.com/gitlab-org/technical-writing/docs-gitlab-com/-/issues/new?type=ISSUE&description_template=Bug) for bugs and the default template for anything else. We'll add labels when triaging, so don't worry about filling
these in correctly.

If you have issues with docs content rather than the website itself,
use the "Suggest updates" button at the bottom of the page in question to open an issue
in the appropriate project.

### Triage process

A Technical Writing staff engineer reviews all new issues 2-3x per week and:

- Applies [work type labels](/handbook/product/groups/product-analysis/engineering/metrics/#work-type-classification)
- Adds [docs-specific labels](https://docs.gitlab.com/development/documentation/workflow/#available-labels) for further categorization
- Sets a weight (1/3/8) for effort estimation on features. Weight is used for prioritization, not capacity planning or estimating completion dates.
- Assigns milestone based on priority and capacity.
- Marks as **Ready for development** when actionable.

## Prioritization framework

### Priority factors

- Delivering [results for customers](/handbook/values/#results)
- Impact against effort
- Alignment with [Technical Writing team roadmap](https://gitlab.com/groups/gitlab-org/-/epics/17363)
- Technical dependencies and blocking work
- 60/40 feature/maintenance target per [R&D guidelines](/handbook/product/product-processes/cross-functional-prioritization/)

## Developer workflow

### Work selection

Team members self-select from the **Ready for development** kanban column, balancing feature work, maintenance, and bug fixes. Choose work that fits your available capacity, and don't hesitate
to ask for guidance when needed.

### Kanban process

Move issues through **Ready for development** → **In dev** → **In review** → **Closed**. In general, work is "done" when deployed and documentation is complete.

### Review and testing guidelines

All code changes should be reviewed by another engineer. These reviews should follow
general GitLab [code review best practices](https://docs.gitlab.com/development/code_review/#best-practices). For complex changes, or changes that could impact team workflows, consider tagging multiple reviewers.

Changes to the look and feel of the site, especially global changes that can impact usability, should also be UX reviewed by a Staff+ Technical Writer or manager.

New shortcodes or other writer-facing features should be tested by a Staff+ Technical Writer or manager, then documented in the [style guide](https://docs.gitlab.com/development/documentation/styleguide/).
