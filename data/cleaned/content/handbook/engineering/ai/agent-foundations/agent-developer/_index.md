---
title: Agent Developer Group
description: "The Agent Developer group is focused on the GitLab Duo Developer foundational flow — improving the flow itself, its evaluation, and flow registry improvements."
---

## Vision

The team that drives core AI/Agent development at GitLab to get and keep it competitive with the rest of the industry when it comes to the quality of the output of the agent, providing the platform for configurability and making sure the agents are as resilient as reasonably possible against prompt injections.

### Team Members

**Engineering Manager & Engineers**

<!-- TODO: Confirm the correct manager slug for Annie Ying (aying-gl / aying). -->
{{< team-by-manager-slug "aying-gl" >}}

**Product, Design & Quality**

| Role | Person |
|------|--------|
| Product Manager | @frwang1, @bjune |

### ☎️ How to reach us

Depending on the context here are the most appropriate ways to reach out to the Agent Developer Group:

* Slack channels: `#f_duo_developer`, `#f_flow_components`, `#dev_agent_developer`
* Slack Groups: `@agent-developer-team` `@flow-components-subteam` `@duo-developer-subteam`

### Technical Components 🛠️

Besides the main GitLab repository these are the key technical components we work with:

1. [Duo Workflow Service within AI Gateway](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/tree/main/duo_workflow_service) 🐍 — our work here centers on the **Duo Developer foundational flow**:
   1. Improving the Developer Flow itself.
   1. Improving the evaluation of the flow.
   1. Flow registry improvements.

   When changing the Duo Developer flow or its shared system prompt, follow our [Duo Developer design principles](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/blob/main/duo_workflow_service/agent_platform/v1/flows/configs/developer/PRINCIPLES.md). They record how we build: Duo Developer as a reusable building block, client-owned goals, principle-based system prompts, and evidence-based changes.

For an understanding of how these components work together, take a look at the [architecture](/handbook/engineering/architecture/design-documents/duo_workflow/).

## 📦 Team Processes

### Goalkeeper Rotation

_TBD — the goalkeeper rotation process is still being defined._

### Retrospective

_TBD — the retrospective process is still being defined._

### 📆 Regular team meetings

**❗️Important**: For every meeting, the [Agent Developer team's meeting notes document](https://docs.google.com/document/d/1wKrNYqP3SwSFa29dWyCMOq_O_31YQ64YX1FIztA6-ag/edit) should be used, and filled with the meeting notes, as well as references to any other sync meeting agendas/notes/recordings which have recently occurred. This will make it easier for people to find any meeting notes.

#### Team Meetings

1. **Agent Developer Standup** (every other Tuesday)
   * **When:** Every other Tuesday, 14:00 UTC <!-- 15:00 CET; note: during CEST (summer) this is 13:00 UTC -->
   * **What:** A standup-style meeting for the full Agent Developer team to share awareness of what each subteam is working on, surface blockers, and stay aligned across subteams.

1. **Weekly Async Update** (every Wednesday)
   * **When:** Every Wednesday (async, no live meeting)
   * **What:** Issue-level async updates posted by each team member — same format as before. See [Weekly Async Updates](#-weekly-async-updates) for the template.

1. **Subteam Syncs** (weekly)
   * **When:** Weekly cadence per subteam (schedule set by each subteam)
   * **What:** Deeper technical discussions within each subteam, covering implementation details, design decisions, and progress that benefits from a smaller-group sync.

### Shared calendars

_TBD._

### 📚 Agent Developer Board Outline

The Agent Developer team is following a milestone process. All currently prioritized issues are visualized in our [milestone board](https://gitlab.com/groups/gitlab-org/-/boards/7828018?milestone_title=Started&label_name[]=group%3A%3Aagent%20developer). Overview issues that outline the goal and focus points of past milestone and the current one can be found in the [overarching epic](https://gitlab.com/groups/gitlab-org/-/work_items/18293).

We aim for ambitious but achievable planning of the current milestone, and only issues in the current milestone should be actively worked on. If there are no more issues available reach out to the EM/PM of the team for clarification.

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
1. **Stretch**: We aim to deliver most of these items, but as part of planning ambitiously some of them might slip.

## 👏 Communication

The Agent Developer Team communicates based on the following guidelines:

1. Always prefer async communication over sync meetings.
1. Don't shy away from arranging a [sync call](#-ad-hoc-sync-calls) when async is proving inefficient, however always record it to share with team members.
1. By default communicate in the open.
1. All work-related communication in Slack happens in the `#dev_agent_developer` channel.

### 📋 Weekly Async Updates

We maintain a practice of weekly async status updates to ensure clear communication, track progress effectively, and maintain transparency across our team. This process aligns with our core values by fostering collaboration, driving results, and promoting efficiency through structured communication.

#### Timing and Frequency

* Team members post updates every Friday, and share them in the team Slack channel (`#dev_agent_developer`).
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

/cc @aying-gl @bastirehm @frwang1 @bjune
```

Be sure to tag your engineering manager, product manager, and any team members you are collaborating with.

#### Best practices

* Be specific and concise in updates
* Always include next steps, even if they're tentative
* Flag blockers early - don't wait until they become critical
* Use the template consistently for easier scanning
* Link to relevant issues or documentation when appropriate

### ⏲ Time Off

Team members should add any [planned time off](/handbook/people-group/time-off-and-absence/time-off-types/) in the "Workday" slack app, in accordance with the [taking time off](/handbook/engineering/#taking-time-off) policy, including creating a [PTO coverage issue](https://gitlab.com/gitlab-com/engineering-division/pto-coverage/-/issues/new).

### 🤙 Ad-hoc sync calls

We operate using async communication by default. There are times when a sync discussion can be beneficial and we encourage team members to schedule sync calls with the required team members as needed.

## 🔗 Useful Links

* [Issue Board (Started milestone)](https://gitlab.com/groups/gitlab-org/-/boards/11381598?milestone_title=Started&label_name%5B%5D=group%3A%3Aagent%20developer)

### 📝 Dashboards (internal only)

* [Developer Trace Analyzer](https://developer-traces-77e941.gitlab.io/index.html)
* [Usage Metrics in Tableau](https://10az.online.tableau.com/#/site/gitlab/views/DuoWorkflowMetricsTracking/DuoWorkflowMetricsTracking?:iid=1)
