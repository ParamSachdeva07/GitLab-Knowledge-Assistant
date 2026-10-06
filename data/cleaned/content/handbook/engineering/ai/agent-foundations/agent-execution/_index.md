---
title: Agent Execution Group
description: "The Agent Execution group is focused on developing GitLab Duo Workflow, an AI system to automate tasks and help increase productivity in your development workflow."
---

## Vision

The Agent Execution group is focused on turning GitLab into the best possible environment to execute Agents across the SDLC.

## 👥 Leadership

{{< group-by-slugs bastirehm arueda emilybauman >}}

## 🧭 Teams

The group is made up of three functional teams, Agent Tools, Agent Observability and Runner Execution. Each team owns a functional area.

### Agent Tools

Agent Tools is focused on building the best tools possible for Agents to interact with GitLab and beyond.
One of its primary responsibilities is GitLab's MCP server.

#### Team Members

{{< group-by-slugs terrichu adruid afilatov fdegier>}}

### Agent Observability

Agent Observability concentrates on providing features to both understand what Agents are doing across GitLab as well as ways to interact with them.

#### Team Members

{{< group-by-slugs lindsey-shelton andrew-f allison_villa romaneisner>}}

### Runner Execution

Runner Execution concentrates on turning GitLab runners into a native environment for agents to execute in.

#### Team Members

{{< group-by-slugs ssuman3 andrasherczeg alperakgun clinacre>}}

## 📦 Team Processes

We are generally aligned with the [process for the overall AI org at GitLab](/handbook/product-development/how-we-work/ai-section-product-development-flow). In detail this means:

### 📆 Regular team meetings

**❗️Important**: For every meeting, the linked meeting doc should be used, and filled with the meeting notes, as well as references to any other sync meeting agendas/notes/recordings which have recently occurred. This will make it easier for people to find any meeting notes.

#### Team Weekly

Every team meets for 30 minutes every Monday. This meeting at the minimum encompasses walking the current progress and blockers in the milestone. It can also be used to present demos or bring up other relevant information

At the beginning of the milestone the meeting is one hour to give additional time to walk through upcoming priorities.

### Goalkeeper Rotation

The Agent Execution group uses a goalkeeper rotation to ensure incoming Request-for-Help, questions, and issues are triaged and directed to the appropriate people or teams. The goalkeeper acts as the first line of support from the team itself, keeping work flowing smoothly and preventing bottlenecks. They are not expected to work on or solve every incoming issue on their own. Every week 1 engineer is assigned to this to ensure appropriate coverage.

The responsibilities and further process are in the [Goalkeeper issue template](https://gitlab.com/gitlab-org/ai-engineering/agent-execution/tasks/-/blob/main/.gitlab/issue_templates/goalkeeper.md), current goalkeeper is noted down in [a google sheet](https://docs.google.com/spreadsheets/d/1BP_b3AttMmAG-Vf9RZ6sMBEoGdJk2-2iKbGxHYshCV4/edit?gid=0#gid=0).
If you are not available for a goalkeeper shift use the #g_agent-execution channel to trade shifts with another team member.

### Shared calendars

* AI-Powered Stage Calendar (Calendar ID: `c_n5pdr2i2i5bjhs8aopahcjtn84@group.calendar.google.com`)

### 📚 Agent Execution Boards Outline

The Agent Execution team is following a milestone process. All currently prioritized issues are visualized in our [milestone board](https://gitlab.com/groups/gitlab-org/-/boards/7828018?milestone_title=Started&label_name[]=group%3A%3Aagent%20execution).
Overview issues that outline the goal and focus points of past milestones and the current one can be found in the [overarching epic](https://gitlab.com/groups/gitlab-org/ai-powered/agent-foundations/agent-execution/-/work_items/3). Every team also has an individual board for daily tracking purposes:

1. [Agent Tools](https://gitlab.com/groups/gitlab-org/-/boards/11408357)
1. [Agent Observability](https://gitlab.com/groups/gitlab-org/-/boards/11405857)
1. [Runner Execution](https://gitlab.com/groups/gitlab-org/-/boards/11407842)

We aim for ambitious but achievable planning of the current milestone, and only issues in the current milestone should be actively worked on. If there are no more issues available reach out to the EM/PM of the team in the `f_[team-name]` slack channel for clarification.

We work with these statuses for issues:

1. **New**: As of yet unclassified issues, which need to be updated to one of the used workflow labels or meta issues such as iteration overview.
1. **Refinement**: Issues in this stage have been identified as important to be worked on but are not ready for development yet. This might be due to a variety of reasons such as missing or not finished designs or architectural questions that need to be clarified.
1. **Ready for development**: Issues that are ready for implementation are moved to this list.
1. **In dev**: When a developer begins work on an issue, they should move it to this list.
1. **Blocked**: Issues in this stage currently cannot be further continued as they depend on other work being done first.
1. **In review**: After development is complete and submitted to be reviewed, the issue should be moved to this list.
1. **Verification**: Following a successful code and UX review, the issue should be moved to this list and the "verification" label should be applied.
1. **Closed**: Once the issue is verified and confirmed to be working properly, it should be moved to this list, the "complete" label should be applied, and the issue should be closed.

We use labels to help with understanding the order in which issues should be worked on:

1. **Deliverable**: These items are the primary deliverables of an iteration and should therefore be picked up first.
1. **Stretch**: We aim to deliver some of these items, but as part of planning ambitiously they might slip.

Every functional team has an equivalent category label to distinguish between the different teams, e.g. "~category:agent tools".

## 👏 Communication

The Agent Execution Team communicates based on the following guidelines:

1. Async via GitLab is the default, use Slack for spontaneous, time critical exchanges.
1. Don't shy away from arranging a sync call when async is proving inefficient, however always record it to share with team members.
1. By default communicate in the open.

### 📋 Weekly Async Updates

We maintain a practice of weekly async status updates to ensure clear communication, track progress effectively, and maintain transparency across our team.

#### Timing and Frequency

* Team members post updates every Wednesday
* Updates are required for all assigned issues that are at least **In Dev**. For other assigned issues it is up to the assignee to decide whether an update is warranted.
* Multiple updates may be needed if working on multiple issues

#### Template

This is the template to use for the updates

```markdown
## Async Status Update yyyy-mm-dd

- **Progress & Status**: _What progress have you made? What's the current state?_
- **Next Steps**: _What are your planned next actions?_
- **Blockers**: _Are you blocked or need assistance with this?_
- **How confident are you that this will make it to the current milestone?**
    - [ ] Not confident
    - [ ] Slightly confident
    - [ ] Very confident

_Remember to update the status!_

/cc @bastirehm @amandarueda [@emilybauman if design involvement]
```

Be sure to tag your engineering manager, product manager, and any team members you are collaborating with. Tag design if the issue has a design component.

#### Best practices

* Be specific and concise in updates
* Always include next steps, even if they're tentative
* Flag blockers early - don't wait until they become critical
* Use the template consistently for easier scanning
* Link to relevant issues or documentation when appropriate

### ⏲ Time Off

Team members should add any [planned time off](/handbook/people-group/time-off-and-absence/time-off-types/) in the "Workday" slack app, in accordance with the [taking time off](/handbook/engineering/#taking-time-off) policy, including creating a [PTO coverage issue](https://gitlab.com/gitlab-com/engineering-division/pto-coverage/-/issues/new).

## 💬 Where to find us

### Slack

We follow the [GitLab Slack channel prefix conventions](/handbook/communication/#slack): `s_` for the cross-team stage/organization channel, `f_` for functional-team channels (engineering + PM + UX together), and `g_` for engineering-only group discussion. Underscores separate distinct things; hyphens join words within a single thing.

| Scope | Channel | Purpose |
| ----- | ------- | ------- |
| Organization | `#g_agent-execution` | Primarily engineering focused discussions not specific to a specific functional team. |
| Agent Tools | `#f_agent-tools` | Agent Tools functional team |
| Agent Observability | `#f_agent-observability` | Agent Observability functional team |
| Runner Execution | `#f_runner-execution` | Runner Execution functional team |
