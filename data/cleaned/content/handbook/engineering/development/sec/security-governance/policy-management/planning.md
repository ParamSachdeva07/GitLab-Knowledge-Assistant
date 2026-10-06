---
title: Security Policies - Planning
---

This page describes the planning and development processes specific to the **Policy Management** group. For the stage-level planning process, see the [Security Governance Planning page](/handbook/engineering/development/sec/security-governance/planning/).

## How we do planning

Our planning follows a quarterly interlock-driven approach. Each quarter, the Director, Product Manager (PM), and Engineering Manager (EM) align on the high-level product roadmap through the **interlock process**. This determines which epics and features the team will focus on for the upcoming quarter and beyond.

Once the quarterly plan is established, the EM collaborates with individual contributors (ICs) to assign a backend and frontend [DRI](#epic-engineering-dri) to each epic. Engineers are asked if they want to take ownership of a given epic rather than being unilaterally assigned.

Milestone-level planning is handled asynchronously. The EM creates a **planning issue** each milestone (see [example](https://gitlab.com/gitlab-org/gitlab/-/work_items/594167)) to collect and organize the work the team should deliver. Issues are pre-assigned to engineers before the milestone starts or during the first week.

### Capacity Allocation

By default, we target the following capacity split:

- **~80%** on feature delivery (epic work, interlock commitments)
- **~20%** on bug fixing, refactoring, and technical debt

This is a guideline, not a rigid rule. The EM adjusts the split based on the current bug backlog, upcoming deadlines, and team health.

### Three-Phase Release Plan (Experiment → Beta → GA)

For interlock-level and epic-level features planned for the current or next quarters, we follow a phased release approach by default:

| Phase | Target Timing | Purpose |
|-------|--------------|----------|
| **Experiment** | 2 milestones before target | Ship a working version early to capture feedback. Feature flag is disabled by default. Not ready for production use. |
| **Beta** | 1 milestone before target | Near-complete user experience. Feature flag may be selectively enabled. Supported on a commercially-reasonable effort basis. |
| **GA (General Availability)** | Target milestone | Feature flag enabled by default. Production-ready, fully tested, documented, and with adoption metrics. |

This is a **default guideline** with flexibility. Sometimes we want to ship Experiment earlier to gather feedback sooner, or move to Beta ahead of schedule. The exact phasing depends on the complexity of the epic and the confidence level of the team. The EM and DRI should agree on the phasing during epic planning.

For more details on GitLab's maturity stages, see [Development Stages and Support](https://docs.gitlab.com/policy/development_stages_support/).

### Spike-First Approach for Epics

When a new epic or interlock item is planned, we begin with a **spike** (time-boxed technical exploration) **before the quarter where the item is interlocked begins**. This ensures the team enters the quarter with validated approaches and ready implementation plans.

The goal of the spike is to:

1. Build a proof-of-concept (PoC) of the working solution.
2. Prove that the approach is feasible without investing significant time.
3. Leverage modern AI tooling to accelerate PoC development where appropriate.

Once the PoC demonstrates the feature is viable, the DRI proceeds to create the implementation plan and individual implementation issues. This approach reduces risk by validating technical assumptions early before committing to full implementation.

### Weekly Team Meeting

The team holds a **weekly team meeting** where the PM may share upcoming priorities and the team has time to ask questions. The goal is to ensure the team understands the intent and scope of upcoming work.

### Backend Ahead of Frontend

When an epic has dependent backend and frontend work, we plan **backend issues one milestone ahead of frontend** where possible. This ensures that:

- Frontend engineers have stable APIs to integrate against.
- Backend work doesn't land at the end of a milestone, leaving no time for frontend integration.
- The overall epic delivery is more predictable.

This is a guideline for dependent work. When backend and frontend are independent, they can be planned for the same milestone.

### Weekly Triage

The EM performs **weekly async triage** of newly opened issues. During triage, each issue receives:

- **Priority** and **Severity** labels
- **Assignee** (the engineer who will work on it)
- **Planned milestone**

This ensures new issues are promptly categorized and scheduled without blocking the team's current work.

---

## Refinement

The Security Policies group takes a lightweight approach to refinement compared to the [stage-level refinement guidelines](/handbook/engineering/development/sec/security-governance/planning/#refinement-guidelines). Refinement is the responsibility of the **individual engineer** assigned to an issue. Rather than being a separate workflow step with formal handoffs, refinement is embedded in the process of delivering a merge request.

The goal of refinement remains the same:

- Identify and resolve outstanding questions or discussions.
- Identify missing dependencies (e.g. `backend` API).
- Raise any questions, concerns or alternative approaches.
- Outline an implementation plan.
- Assign a weight to the issue.

### How Refinement Works

1. The engineer assigned to an issue reviews it for completeness and clarity.
2. If the issue is **complex** or the engineer would like a second opinion, they **can** create a refinement plan and ask another team member to review it. This is **optional**, not mandatory.
3. If the issue is straightforward, the engineer should proceed directly to creating the MR, treating refinement as part of the MR delivery process.
4. The engineer updates the issue description with an [implementation plan](/handbook/engineering/development/sec/security-governance/planning/#implementation-plan) and [verification steps](/handbook/engineering/development/sec/security-governance/planning/#verification-steps) as they work through the solution.

This approach reduces friction by eliminating the separate `workflow::refinement` step while still ensuring engineers think through their approach before coding. For complex issues, the review safety net remains available.

For bugs, spikes, and security issues, follow the guidelines on the [Security Governance Planning page](/handbook/engineering/development/sec/security-governance/planning/#bug-diagnosis).

---

## Definition of Done for Epics

An epic is considered **done** when all of the following criteria are met:

### Functional Completeness

- [ ] The feature is working as specified in the acceptance criteria.
- [ ] All implementation issues above the feature flag rollout issue are closed.
- [ ] All required merge requests have been merged into `main`.

### Feature Flag & Rollout

- [ ] The feature flag is **enabled by default** (globally, not just for select customers).
- [ ] A feature flag cleanup issue has been created and scheduled.

### Testing & Quality

- [ ] Unit, integration, and feature tests are implemented as appropriate.
- [ ] The feature has been verified on staging and production.
- [ ] No critical bugs or performance regressions.

### Adoption Metrics

- [ ] Adoption metrics are implemented to track usage (users, projects, namespaces).
- [ ] The team is aware of adoption levels and can verify how often the feature is used.
- [ ] Metrics are properly attributed to the correct group and feature category.

### Documentation & Communication

- [ ] Documentation is complete and published.
- [ ] A release post entry has been merged (if applicable).
- [ ] The feature has been demoed internally or shared with relevant stakeholders.

Complete items are removed from the [Interlock Deck](https://interlock-deck.gitlab.io/#filter=group%3A%3Asecurity_policies) once all criteria above are satisfied. The epic is closed at this point.

For reference, see also GitLab's [Feature-level Definition of Done](https://docs.gitlab.com/development/definition_of_done/).

---

## Epic Engineering DRI

As an epic is ready to move into active development, the EM collaborates with ICs to assign a DRI for each required tech stack (backend, frontend). Engineers are asked if they want to take ownership of a given epic.

As the DRI for an Epic, the engineer is **not** responsible for executing all the work but they are responsible for:

1. Starting with a [spike](#spike-first-approach-for-epics) to validate the technical approach with a PoC.
1. Suggesting the implementation issue breakdown and requesting feedback.
1. Writing the agreed implementation issues.
1. Identifying when further research is required and writing the spike issue(s).
1. Making technical decisions.
1. Providing status updates when requested.
1. Identifying and communicating blockers.
1. Identifying potential security implications and involving a security engineer if necessary.
1. Taking measurements to reduce the impact of far-reaching work.

The DRI may choose to work on the issues they created but they're not expected to deliver the whole Epic on their own.
