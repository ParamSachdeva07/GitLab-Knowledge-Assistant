---
title: "Detailed Operating Workflow"
description: "ProdSecEng team-specific operating workflows and processes"
---

ProdSecEng follows the [operating model](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/#operating-model) defined in the team charter for planning cadences, priority labels, sizing/weights, and unplanned work tracking. This page covers ProdSecEng-specific workflows.

## Backlog Management

The `~ProdSecEng Candidate` label identifies issues as potential ProdSecEng work. Anyone can add this label; the team reviews and triages these issues monthly (as part of milestone planning) and moves them into the appropriate board:

- [Internal Issue Board (gitlab-com)](https://gitlab.com/groups/gitlab-com/-/boards/7098644) — ProdSec automation needs
- [Product Issue Board (gitlab-org)](https://gitlab.com/groups/gitlab-org/-/boards/7098625) — Product security enhancements, paved roads

### Taking On Work

When we commit to an issue, we:

1. Discuss the issue as a team and with other ProdSec or Security division teams to assess the high-level effort, value, and priority.
2. Add the `~"Product Security Engineering Team"` label.
3. For internal automation/tooling issues: check it meets the [intake automation request criteria](/handbook/security/product-security/security-platforms-architecture/security-interlock/prodsec-to-product-workflow/#intake-workflow).
4. For product issues: identify the relevant PM/EM via `group::` labels (or best effort), get alignment on the solution and priority, and flag that ownership will transfer after release.
5. Apply the appropriate `ProdSecEngMetric::` [metric label](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/#success-metrics), [priority](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/#priority) label, [weight](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/#sizing-and-estimates), and milestone if known. Apply the [`~Unplanned`](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/#unplanned-work) label if brought into the current milestone.

### Removing Work From the Backlog

If we decide not to take on an issue, we:

1. Remove the `~"Product Security Engineering Team"` or `~ProdSecEng Candidate` label
2. Comment with the reasoning
3. Best-effort `@-mention` the appropriate EM, PM, or team
4. Consider applying `~Seeking community contributions` if the issue is public.

## Refinement and Planning

Like [Single Engineer Groups](/handbook/company/structure/#single-engineer-groups), each Product Security Engineer will *"encompass all of product development (product management, engineering, design, and quality) at the smallest scale. They are free to learn from, and collaborate with, those larger departments at GitLab but not at the expense of slowing down unnecessarily".* This means all ProdSecEng team members can contribute to prioritisation, validation, refinement, solution design. The Security Engineering Manager is ultimately responsible and the DRI.

We use the issue statuses and phases described [Product Development Flow](/handbook/product-development/how-we-work/product-development-flow/), and have the flexibility to skip parts that are not needed. At the end of a product contribution, features are handed over to the Product and Engineering teams.

### Refinement Cadence

Refinement is always done during routine planning (such as milestone or quarterly planning), and sometimes may be done ad-hoc (such as when the issue is discovered and we need to understand effort for prioritisation).

### Refinement Process

During refinement, we:

1. Pick an unrefined issue (one with a `New` status, or with the `~ProdSecEng Candidate` label, or a previously refined issue that has become stale). Timebox refinement to ~1 hour per issue.
2. Understand the goal or the problem that needs to be solved. Ask questions of the creator or relevant teams. Consider breaking the issue down or creating an epic.
3. Add detail so someone can understand the [definition of done](#definition-of-done), acceptance criteria, goals, and requirements.
4. Investigate potential solutions. Engage with product, engineering, or security teams if needed.
5. Update the issue until it meets the [definition of ready](#definition-of-ready).

## Definition of Done

A work item can generally be considered done when:

1. Acceptance criteria is met.
2. Code changes: produced, reviewed, passing CI, merged, and deployed to applicable environments.
3. Performance and error monitoring set up where relevant.
4. Documentation produced or updated.
5. Any cross-team communication completed.

## Definition of Ready

Some projects use issue templates. In the absence of specific guidance, use the criteria below.

### Trivial or Small Tasks (Weight < 3)

1. Write a description including context, a proposal, and (if applicable) a technical implementation plan answering: "why?", "when?", and "who needs to be involved?"
2. Define acceptance criteria as checkboxes.
3. Assign or update [weight](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/#sizing-and-estimates) and [priority labels](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/#priority).
4. Set `~Product Security Engineering Team` and `~ProdSecEngMetrics::` [metric label](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/#success-metrics) if not already done.
5. `Ready for Development` issue status is set

### Moderate or Complex Tasks (Weight >= 3)

Everything from simple tasks, plus:

1. Discuss and document relevant risks (team, timeline, implementation, stability, security).
2. Define a technical implementation plan including development steps from design through deployment, documentation updates, and monitoring/alerting considerations.
3. Check acceptance criteria includes deployment to appropriate environments and stakeholder notification.
4. Have the issue peer reviewed (by a manager or team member) before setting status to `Ready for Development`.

## Milestone Planning

ProdSecEng plans work around [GitLab Product Milestones](/handbook/product/product-processes/milestones/), following the [planning and milestones process](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/#planning-and-milestones) in the team charter.

Each milestone has a single [Milestone Planning issue](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/product-security-engineering-team/-/issues/?label_name%5B%5D=Milestone+Planning) created using the [template](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/product-security-engineering-team/-/issues/new?issuable_template=milestone_planning). This issue is the source of truth for all planning decisions and discussions for that milestone.

### Planning Process

**Plan prep:**

1. Create the milestone planning issue immediately after the current milestone's planning is finalized.
2. Update the issue description with correct milestone numbers, quarters, and dates.
3. Team members fill in the capacity table: availability (weekdays minus PTO/holidays) and work capacity (availability minus non-work time like G&D, social, admin — assume ~1 day/week when in doubt).
4. Create a retrospective sub-task using the retrospective template.

**Planning:**

1. Review open epics prioritized for the quarter and update milestones on related issues.
2. Review the Issue Parking Lot: move items we want to commit to into the milestone, and leave the rest.
3. Review the issue boards (`~Product Security Engineering Team` and `~ProdSecEng Candidate`) and the parent FY planning epic for other candidate work.
4. Ensure each planned work item has a clear definition, weight, `~ProdSecEngMetric::*` and `~priority::*` labels, and a status of `Ready for Development` (or a clear path to get there).
5. Check total planned weight against available capacity, using the planned/unplanned ratio agreed in the parent FY epic. Remove work and update stakeholders if overcommitted.
6. Team members review and provide feedback. Once feedback is addressed, planning is finalized at least 3 days before the milestone start date.

**Plan close down:**

1. Open the next milestone's planning issue and move remaining Parking Lot items to it.
2. Confirm the retrospective was completed and follow-up actions recorded, then close the issue.

### Unplanned Work

Items added mid-milestone should have the milestone set on the issue and the `~Unplanned` label applied. These are tracked in the planning issue so we can assess our planned / unplanned capacity split over time.

### Retrospectives

After each milestone, the team holds an async retrospective captured as a sub-task on the planning issue. Items can be added throughout the milestone or afterward. This is completed 1 week after the milestone has ended.

## Development

### Open Source Contributions

When possible, we contribute new features or security improvements directly to the dependencies that GitLab relies on so that everyone can benefit from those enhancements. Since those contributions happen in external repositories, they can't be tracked with our labels. In those cases, we should apply the appropriate labels to the merge requests we create for updating the dependency version to the one that includes our contributed changes.

### Merge Request Reviews

For projects owned by other teams, we follow their review conventions.

For ProdSecEng-owned projects:

- Default to requesting reviews from other ProdSecEng team members to encourage collaboration and knowledge sharing.
- We acknowledge that as a small team, thorough reviews may not always happen quickly — we evaluate the knowledge-sharing v.s. velocity tradeoff case-by-case.
- Skip formal review if something is blocking, time-sensitive, or resolving an urgent need.
- We pick up issues in tooling other team members have written.

### Project namespaces

We default to the namespaces of the stakeholder that we're performing the work for:

- GitLab product contributions: relevant product repositories
- AppSec work: [AppSec tooling namespace](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/tooling)
- Team repositories: [ProdSecEng tooling namespace](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/tooling)

## Tooling Integration

One of ProdSecEng's key focus areas is integrating custom ProdSec tooling into the GitLab product. The full lifecycle for this — from intake through co-creation, maintenance, and sunsetting — is defined in the [ProdSec to Product Workflow](/handbook/security/product-security/security-platforms-architecture/security-interlock/prodsec-to-product-workflow/).

This section covers the ProdSecEng-specific mechanics for tracking and executing tooling integration work.

### Tracking

ProdSecEng maintains a tooling inventory in the [internal handbook](https://internal.gitlab.com/handbook/security/product_security/product_security_engineering/#project-inventory) (accessible to GitLab team members only), which lists all tools, their path-forward categories, and maintenance details.

For each tool undergoing integration:

- A tooling integration epic is created to organize the work
- Child epics are created for each discrete piece of functionality, labeled `~ProdSecEngMetric::Tooling Integration`
- A tooling handover epic or child issue is created for coordination with eventual owning teams

### Breaking Down Functionality

We break tools into discrete pieces of functionality — distinct things the application does (user-facing or foundational). For example, a to-do list might break into: creation, viewing, editing, removal, reordering, and categorization of items. This helps us understand value, create actionable work items, and enable parallelization.

### Tooling Handover Epics

For functionality being built into the product, we create handover epics early to coordinate with the teams that will own it. These epics establish a single source of truth for handover decisions, help identify owning teams, and enable collaboration on definition of done, feature flags, rollout, and transition.

### Sunsetting Issues

We track the high-level requirements to deprecate custom tools using the [sunsetting template](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/product-security-engineering-team/-/work_items/new?description_template=sunset_tooling). Issues are closed as requirements are fulfilled. For the broader transition and sunset process, see the [Transition & Sunset Workflow](/handbook/security/product-security/security-platforms-architecture/security-interlock/prodsec-to-product-workflow/#transition-and-sunset-workflow).

### Step-by-Step Process

**Starting integration work:**

1. Create a tooling integration epic to organize the work
2. Create a tooling handover epic or issue (depending on size of the work) as its child
3. Ensure the tool is listed in the [internal handbook inventory](https://internal.gitlab.com/handbook/security/product_security/product_security_engineering/)

**During planning:**

1. Create/document an [Architecture Design Workflow](/handbook/engineering/architecture/workflow/) if one doesn't exist
2. Create child epics for each discrete piece of functionality (label with `~ProdSecEngMetric::Tooling Integration`)
3. Recommend a starting order for the work

**During development ([Co-create Workflow](/handbook/security/product-security/security-platforms-architecture/security-interlock/prodsec-to-product-workflow/#co-create-workflow)):**

1. Create issues under functionality epics
2. Engage PMs and EMs in the handover epic: confirm alignment, discuss concerns, agree on definition of done and handover criteria

**After completing a contribution:**

1. Close relevant sunsetting issues if appropriate
2. Begin the [Transition & Sunset Workflow](/handbook/security/product-security/security-platforms-architecture/security-interlock/prodsec-to-product-workflow/#transition-and-sunset-workflow) to migrate internal users and decommission the tool
