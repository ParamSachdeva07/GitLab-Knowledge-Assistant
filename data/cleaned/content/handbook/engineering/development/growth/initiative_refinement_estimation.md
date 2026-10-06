---
title: Growth Milestone Planning, Refinement and Estimation
description: "Continuous refinement process and estimation guidelines for Growth teams"
---

## Milestone Planning Phase

Growth operates on a continuous flow model anchored by milestone planning. The milestone planning issue serves as the central coordination hub, aligning priorities, ownership, and timelines.

- Milestone planning starts at-least two weeks before the actual start date of milestones
- A milestone planning Issue is created following [milestone planning template](https://gitlab.com/gitlab-org/growth/team-tasks/-/blob/master/.gitlab/issue_templates/milestone-planning-issue.md)
- Planning Issue includes strategic themes, focused work tracks for Design, Feature work, Tech Debt, Bugs and available capacity of the Engineers
- PM, EM, UXM, Designers and Engineers identifies epics and Issues for the target milestone across the feature, experiment, bugs and annotate with target milestone
- PMs work with EM to break down priority projects into implementation Issues usually before milestone start date (as required)
- Ideally, issues assigned to a target milestone should have cleared the design stage before milestone begins. This gives engineering enough clarity to scope and plan delivery with confidence. If market commitments require locking a target milestone before design is complete, we will treat it as an exception.
- EM organizes a milestone kickoff meeting on the start date of the target milestone. Engineers are expected to review the milestone issues ahead of time and self-assign [DRI](./engineering_dri.md) based on interest, capacity, and complexity. The kickoff is a discussion forum and not an assignment session for surfacing blockers, dependencies, and open questions before work begins.

## Execution Phase

- DRIs coordinate work across Issues, manage dependencies, and flag blockers immediately
- The complete development process follows [Work Progression Guidelines](#work-progression-guidelines)
<!-- markdownlint-disable-next-line MD051 : the anchor is valid; lint miscomputes it because of the {.h5} heading attribute -->
- The priority projects and work listed in milestone planning take precedence. Once those are completed and there is available capacity, engineers can pick up additional Issues from the [work queue boards](#work-queue-boards).
- Bot posts weekly progress update in milestone planning Issue showing work completed, in-progress, blocked, risks, and velocity
- Retrospective feedback is collected in the milestone planning Issue thread rather than a separate retrospective Issue

### Two Modes of Work Intake {.h5}

Not all planned work will reach `Ready for Development` by the time a milestone starts — issues will continue to trickle in as they clear design and refinement. We therefore operate in two modes during a milestone:

1. **Assigned at kickoff** — Issues that are `Ready for Development` when the milestone starts. Engineers review these ahead of the kickoff and self-assign as DRI based on interest, capacity, and complexity.
   <!-- markdownlint-disable-next-line MD051 : the anchor is valid; lint miscomputes it because of the {.h5} heading attribute -->
1. **Kanban pull during the milestone** — Priority issues that reach `Ready for Development` after the milestone starts. The [work queue boards](#work-queue-boards) (also linked from the milestone planning issue) act as queues for this work. Engineers are expected to monitor those boards and pick up newly-ready issues in priority order (top to bottom) as their capacity allows, before pulling from the general backlog.

### Work Queue Boards {.h5}

We centralize milestone execution around four boards that match the tracks in the milestone planning issue. Issues on these boards are ranked top-to-bottom by priority — pick in order.

1. [Growth - Feature Work](https://gitlab.com/groups/gitlab-org/-/boards/11511990?not[label_name][]=Category%3AEngineering%20Excellence&not[label_name][]=type%3A%3Amaintenance&label_name[]=section%3A%3Agrowth&label_name[]=Growth%3A%20Driving%20First%20Orders&milestone_title=Started)
1. [Growth - Priority Bugs](https://gitlab.com/groups/gitlab-org/-/boards/11512116?milestone_title=Started&label_name[]=section%3A%3Agrowth&label_name[]=type%3A%3Abug)
1. [Growth - Tech Debt Work](https://gitlab.com/groups/gitlab-org/-/boards/11512114?not[label_name][]=Category%3AEngineering%20Excellence&not[label_name][]=Engineering%20Time&label_name[]=section%3A%3Agrowth&label_name[]=type%3A%3Amaintenance&milestone_title=Started)
1. [Growth - Engineering Excellence Work](https://gitlab.com/groups/gitlab-org/-/boards/11512115?milestone_title=Started&label_name[]=section%3A%3Agrowth&label_name[]=Engineering%20Time&label_name[]=Category%3AEngineering%20Excellence)

## Milestone Closure Phase

- Bot summarizes outcomes, generates velocity metrics (cycle time, completion rate etc), and auto-forwards incomplete work to next milestone with efficiency analysis
- Bot manages the spill over by adding a milestone missed label to the issues still open and move them into next milestone
- Bot closes the milestone

## Work Progression Guidelines

### Problem Validation {.h5}

- Product Manager validates that the problem is clearly defined, worth solving, and free of blockers
- Product Manager moves the status of the Epic/Issue to `Ready for Design`

### In-Design {.h5}

- Product Designer creates an Issue under the Epic to create necessary Design
- Designer iterates on designs and gathers early feedback:
  - Designer tags 2-3 engineers at random, so feedback requests are distributed evenly across the team.
  - Ideally, engineers provide feedback within 24-48 hours.
- Designer refines designs based on discussion
- When the scope is clear and the discussions have been addressed, Designer/PM moves the Issue to `Planning Breakdown` status
- If there is no Design Issue, Product Managers creates a bare minimal implementation Issues using [Experiment Implementation](https://gitlab.com/gitlab-org/gitlab/-/Issues/new?description_template=Experiment%20Implementation) or [Implementation](https://gitlab.com/gitlab-org/gitlab/-/Issues/new?description_template=Implementation) and proceed to `Planning Breakdown` status

### Refinement {.h5}

Despite the name, refinement is a planning-breakdown and engineering-feasibility step — not just weight voting. It's where the team works through *how* the Issue would actually be built: the technical approach, dependencies, risks, and whether the scope is right. See [Team Participation in Refinement](#team-participation-in-refinement) for what that looks like in practice. The weight estimate is an *output* of that analysis, not the point of it.

- Issues are moved from the `Planning Breakdown` status to the `Refinement` status automatically by the triage bot in order of priority (from top to bottom). An Issue qualifies for automatic refinement if it either has the `Next Up` label or is assigned a current or future milestone (an active milestone whose due date is today or later). Both pools compete for the same limited refinement slots: `Next Up` Issues fill slots first, then milestone-assigned Issues backfill any remaining slots, in priority order. The bot will only move Issues to refinement if there is room in refinement column, meaning there is less Issues than maximum limit for this column. This is first chance for PMs to prioritize Issues by moving them higher in the `planning breakdown` column. After the Issue is moved to refinement, a dedicated `refinement thread` is created, which acts as a place for discussion and weight estimation.
  - When the refinement thread is created, the bot tags a rotating cohort of 3 available growth engineers (out-of-office engineers are skipped) rather than the whole engineering group. Being tagged means you are on the refinement cohort for that Issue, and the expectation is that tagged engineers provide their weight estimate and any feedback within 48 hours at most, ideally within 24.
  - 💡 Hint: In rare case when an Issue has to be expedited, it's possible to move it to refinement manually by setting the Issue's status to `Refinement`. This will invoke a reaction from triage bot, which will add `refinement thread` for such Issue instantly so the refinement can proceed the same way as with automated path.
- During refinement the team ensures that the Issue is well described and requirements are clear. They can use the `refinement thread` to discuss but they should make sure that any changes and decisions made there are also reflected in Issue's description. Once each engineer is comfortable with the way the Issue is described, they can vote their estimation of weight based on our [guidelines](#estimation-guidelines). The voting happens by reacting to the thread with one of few possible weight estimates: 1️⃣ 2️⃣ 3️⃣ 5️⃣ or 🚀 (indicates 5+, meaning the Issue is likely too big and needs splitting into smaller Issues - please also suggest how by starting a discussion). When you vote, add a short comment justifying your weight — the key factors driving your estimate (complexity, unknowns, code footprint, dependencies). A number alone gives the team no signal to reconcile differing estimates. If estimates diverge significantly, or you have concerns about feasibility or scope, start a discussion in the thread rather than silently voting; reaching a shared understanding matters more than the raw number.
  - 💡 Hint: You can also try the [Growth Refinement Review](https://gitlab.com/gitlab-org/growth/ai/growth-refinement-review) AI skill to help with refinement.
  <!-- markdownlint-disable-next-line MD051 : the anchor is valid; lint miscomputes it because of the {.h5} heading attribute -->
- If an issue has a weight of `5` or higher, it likely needs to be broken down into smaller issues. The Engineering DRI of the associated Epic (or the EM, if no DRI is assigned) is responsible for splitting the issue and moving the new issues through refinement. To prevent the bot from progressing the original issue in the meantime, add a ❌ reaction to the refinement thread (see the hint in the [Development Phase](#development-phase) section below).

> ⚠️ Once design and refinement are complete, the planned design, functionality, and UX approach should be treated as stable. Changes proposed during development or review are expensive and disruptive. Use the design and refinement phases to get as confident as possible in the implementation plan before the development phase begins.

### Development Phase {.h5}

- Each day the triage bot checks all Issues in the `Refinement` status and if an Issue has required minimum number of estimation votes (see `MIN_REACTIONS` constant [here](https://gitlab.com/gitlab-org/quality/triage-ops/-/blob/master/lib/growth_refine_automation_helper.rb) for the current setting), the bot sets the Issue's weight to the highest voted value, reacts to the refinement thread with ✅, and moves the Issue to the `Ready for Development` status.
  - 💡 Hint: If there is some problem with the Issue and it shouldn't be moved forward even if enough engineers estimate it, ❌ reaction can be added to the thread which will stop the bot from transitioning the Issue to `Ready for Development` as long as this reaction sticks to the thread. This means that whoever put it is also responsible for removing it once the problem is gone.
- Prioritization of ready work happens through milestone assignment: PMs signal that an Issue is scheduled by setting its milestone. There is no separate scheduling status — the milestone acts as the scheduling signal.
- Engineers pick the Issue from `Ready for Development` and move the status to `In Dev`. If the Issue is not already scheduled to a milestone, the triage bot assigns the current milestone.
- Once the MR associated with the Issue reaches to review stage, the status of the Issue is changed to `In Review`
- Once the MR is merged and MR changes is deployed to production, the status of the Issue is changed to `Verification`
- If an Issue is moved to any post-refinement status (`Ready for development`, `In dev`, `In review`, `Verification`, `Blocked`, or `Complete`) while its weight is missing, the triage bot pings the person who moved it to assign a weight according to the [estimation guidelines](#estimation-guidelines).

### Verification {.h5}

- The Engineering DRI determines the appropriate verification level - either mentioning the PM and closing for straightforward completions, or requesting formal PM verification for complex changes.

## Estimation Guidelines

[The development estimation is the time spent in the `In dev` status until the Issue is moved to `Complete`, key factor is the review cycle that is uncertain with pipeline failures and reviewer availability]

| Weight | Usual Timeline | Description                                                                                                                                                                                                                                                                                      |
| ------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1      | < 1 week            | The simplest possible change. We are confident there will be no side effects.                                                                                                                                                                                                                    |
| 2      | 1-2 weeks         | A simple change (minimal code changes), where we understand all of the requirements.                                                                                                                                                                                                             |
| 3      | 2-3 weeks            | A simple change, but the code footprint is bigger (e.g. lots of different files, or tests affected). The requirements are clear.                                                                                                                                                                 |
| 5      | 3-4 weeks          | A more complex change that will impact multiple areas of the codebase, there may also be some refactoring involved. Requirements are understood but you feel there are likely to be some gaps along the way.                                                                                     |
| 5+     | 4 weeks+            | A significant change that may have dependencies (other teams or third-parties) and we likely still don't understand all of the requirements. It's unlikely we would commit to this in a milestone, and the preference would be to further clarify requirements and/or break into smaller Issues. |

In planning and estimation, we value [velocity over predictability](/handbook/engineering/development/principles/#velocity). The main goal of our planning and estimation is to focus on the [MVC](/handbook/values/#minimal-valuable-change-mvc), uncover blind spots, and help us achieve a baseline level of predictability without over optimizing. We aim for 70% predictability instead of 90%. We believe that optimizing for velocity (merge request rate) enables our Growth teams to achieve a [weekly experimentation cadence](/handbook/product/groups/growth/#weekly-growth-meeting).

- If an Issue has many unknowns where it's unclear if it's a 1 or a 5, we will be cautious and estimate high (5).
- If an Issue has many unknowns, we can break it into two Issues. The first Issue is for research, also referred to as a [Spike](<https://en.wikipedia.org/wiki/Spike_(software_development)>), where we de-risk the unknowns and explore potential solutions. The second Issue is for the implementation.
- If an initial estimate is incorrect and needs to be adjusted, we revise the estimate immediately and inform the Product Manager. The Product Manager and team will decide if a milestone commitment needs to be adjusted.

## Team Participation in Refinement

<!-- markdownlint-disable-next-line MD051 : the anchor is valid; lint miscomputes it because of the {.h5} heading attribute -->
Operating asynchronously means refinement can't rely on scheduled meetings where everyone shows up at the same time. Instead, the team should adopt a continuous refinement mindset where engineers regularly check the [growth Epic board](https://gitlab.com/groups/gitlab-org/-/epic_boards/2079888) and the [work queue boards](#work-queue-boards) for items in refinement status. When an Epic appears in the `Refinement` status, engineers should review it, ask clarifying questions, evaluate technical feasibility, and provide feedback on the proposed direction. Engineers who develop interest and context during refinement are encouraged to volunteer as the Engineering DRI by self-assigning the Epic. This isn't a passive activity - the goal is to surface concerns, suggest alternatives, ensure the Epic is well-understood, and ideally volunteer to own the breakdown and implementation.

<!-- markdownlint-disable-next-line MD051 : the anchor is valid; lint miscomputes it because of the {.h5} heading attribute -->
Similarly, the [work queue boards](#work-queue-boards) should be monitored for Issues in the `Refinement` and `Ready for Development` statuses. Issues in refinement need estimation votes and technical feedback. Issues in ready for development are immediately available for pickup. By regularly scanning these columns, engineers maintain awareness of upcoming work, can identify Issues that align with their expertise or interests, and keep the pipeline moving.

Currently, the team should prioritize any work labeled with ~"Growth::Driving First Orders". These represent high-priority items that need immediate attention.

## Issue sequencing

In order to convey Issue implementation order and blocking concepts, we leverage the [blocking Issue linking feature](https://docs.gitlab.com/ee/user/project/Issues/related_Issues.html#blocking-Issues).

More on the discussion can be seen in https://gitlab.com/gitlab-org/growth/team-tasks/-/Issues/752.

## Labelling Issues & Epics

We use workflow boards to track Issue progress throughout a milestone. Workflow boards should be viewed at the highest group level for visibility into all nested projects in a group.

The Growth stage uses the `~"devops::growth"` label and the following groups for tracking merge request rate and ownership of Issues and merge requests.

| Name          | Label                   | gitlab-org                                                                                                                          | All Groups                                                                                                                                         |
| ------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Growth        | `~"devops::growth"`     | [Growth Workflow](https://gitlab.com/groups/gitlab-org/-/boards/11511990)                                                            | [-](https://gitlab.com/dashboard/Issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=devops%3A%3Agrowth)                                     |
| Acquisition   | `~"group::acquisition"` | [Acquisition Workflow](https://gitlab.com/groups/gitlab-org/-/boards/11511990)                                                       | [-](https://gitlab.com/dashboard/Issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=devops%3A%3Agrowth&label_name[]=group%3A%3Aacquisition) |
| Activation    | `~"group::activation"`  | [Activation Workflow](https://gitlab.com/groups/gitlab-org/-/boards/11511990)                                                        | [-](https://gitlab.com/dashboard/Issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=devops%3A%3Agrowth&label_name[]=group%3A%3Aactivation)  |
| Engagement    | `~"group::engagement"`  | [Engagement Workflow](https://gitlab.com/groups/gitlab-org/-/boards/11511990)                                                        | [-](https://gitlab.com/dashboard/Issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=devops%3A%3Agrowth&label_name[]=group%3A%3Aengagement)  |
| Experiments   | `~"experiment-rollout"` | [Experiment tracking](https://gitlab.com/groups/gitlab-org/-/boards/1352542)                                                        | [-](https://gitlab.com/dashboard/Issues?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=experiment-rollout)                                     |
| Feature Flags | `~"feature flag"`       | [Feature flags](https://gitlab.com/groups/gitlab-org/-/boards/1725470?&label_name[]=devops%3A%3Agrowth&label_name[]=feature%20flag) |                                                                                                                                                    |

Growth teams work across the GitLab codebase on multiple groups and projects including:

- The [gitlab.com/gitlab-org](https://gitlab.com/gitlab-org/) group
- [gitlab](https://gitlab.com/gitlab-org/gitlab)
- [GLEX](https://gitlab.com/gitlab-org/ruby/gems/gitlab-experiment)
- [customers-gitlab-com](https://gitlab.com/gitlab-org/customers-gitlab-com)
- The [gitlab.com/gitlab-com](https://gitlab.com/gitlab-com/) group
- [about.gitlab.com](https://gitlab.com/gitlab-com/marketing/digital-experience/about-gitlab-com)
