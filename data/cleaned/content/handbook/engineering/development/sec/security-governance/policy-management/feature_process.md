---
title: Security Policies - Working on features
---

## Process

Feature development is organized in an epic that collects feature-related issues. Features are usually developed behind a feature flag. The goal of the feature development process is to enable the feature flag by default.

Feature development epics are listed in the [Interlock Deck](https://interlock-deck.gitlab.io/#filter=group%3A%3Asecurity_policies).

### Phased Delivery (Experiment → Beta → GA)

By default, we follow a [three-phase release plan](/handbook/engineering/development/sec/security-governance/policy-management/planning/#three-phase-release-plan-experiment--beta--ga) for epic-level features:

1. **Experiment** (2 milestones before target): Ship a working version behind a disabled feature flag to capture early feedback.
2. **Beta** (1 milestone before target): Near-complete experience, feature flag selectively enabled for specific customers or projects.
3. **GA** (target milestone): Feature flag enabled by default, fully tested, documented, and with adoption metrics.

The exact phasing is flexible and depends on epic complexity and team confidence.

### Spike-First Approach

Each new epic begins with a **spike** where the DRI builds a proof-of-concept (PoC) to validate the technical approach **before the interlocked quarter begins**. This can leverage modern AI tooling to accelerate development. Once the PoC demonstrates feasibility, the DRI creates the implementation plan and individual implementation issues. See [Spike-First Approach for Epics](/handbook/engineering/development/sec/security-governance/policy-management/planning/#spike-first-approach-for-epics) for details.

### Epic's Issues

- Title
  - Add 'BE' or 'FE' into the title to signify backend and frontend. The labels would signify this as well, but adding this to the title makes it easier to spot.
- Milestone
  - The feature flag rollout issue's milestone is the milestone in which we plan to release the feature. Any issue above the feature flag rollout issue should have a milestone <= the feature flag rollout issue milestone.
  - When an epic has dependent backend and frontend work, [plan backend one milestone ahead of frontend](/handbook/engineering/development/sec/security-governance/policy-management/planning/#backend-ahead-of-frontend) where possible.
- Workflow label
  - Needs to be kept up to date so that users/PMs know the status of the epic and can plan their work appropriately (e.g. if all the issues have a label of ~workflow::in dev halfway through the milestone, the epic is progressing well).
- Order of issues in the "Child issues and epics" list
  - Any issue above the feature flag rollout issue is required for release.
  - Any issue below the feature flag rollout issue is not required for release, but either a nice to have or a backlog issue.

### Rolling Out a Feature Epic

- All issues above the feature flag rollout issue should be closed before rolling out a feature flag globally on production.
- The feature flag rollout issue should be the highest open issue on "Child issues and epics" to signify the state of the epic.

### Definition of Done

An epic is considered complete when all [Definition of Done for Epics](/handbook/engineering/development/sec/security-governance/policy-management/planning/#definition-of-done-for-epics) criteria are met, including:

- Feature is working and the feature flag is enabled by default.
- Adoption metrics are implemented and the team can verify usage.
- The feature is verified, tested, and documented.

### Follow-up Work

- When additional work is identified that is not required for a release of a feature, a separate follow-up/improvements epic should be created and the issues should be added to it.
  - This additional epic should not go into the priorities list for the group as not all of the issues may be important enough to schedule for a specific milestone. Instead the issues should be prioritized individually.
- When we close the feature flag rollout issue, which happens when the feature flag has been defaulted on and the feature flag cleanup issue has been created (per the rollout issue template), we close the feature epic and move any remaining issues to the follow-up/improvement epic.

### Bugs

- Bugs found before the feature flag is defaulted should be added to the epic and evaluated for impact.
  - If a bug blocks the release, it should stay with the epic.
  - If a bug does not block the release, it should be added to the follow-up epic.
- Bugs found after the feature flag is defaulted on do not need to be added to any epic.
