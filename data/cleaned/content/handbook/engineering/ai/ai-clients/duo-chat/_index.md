---
title: Duo Chat Group
description: "The Duo Chat group is dedicated to enhancing DevSecOps productivity by building an AI natural language interface to GitLab's Platform, delivered across web and IDE surfaces."
---

## 🚀 Vision

The Duo Chat group is focused on developing GitLab Duo Chat as a platform by supporting other product groups and the wider community in integrating more capabilities. For more information on GitLab's Duo Chat as a product category, please see our [Product Category Direction](https://about.gitlab.com/direction/ai-powered/duo_chat/) page.

This group is part of the [AI Clients stage](/handbook/engineering/ai/ai-clients/).

---

## 👨‍💻 Team Members

{{< group-by-slugs donaldcook enrique-alcantara tomasbulva rfrederico evakadlecova kaveh_nejad_gitlab john-slaughter >}}

---

## 🤝 Stable Counterparts

Below are our [stable counterparts](/handbook/leadership/#stable-counterparts):

{{< group-by-slugs dashaadu nickleonard >}}

---

## 💬 Where to Find Us

### Slack

- **Duo Chat lounge:** [#duo-chat-lounge](https://gitlab.enterprise.slack.com/archives/C06LWENL58F)
- **General Duo Chat questions:** [#g_duo_chat](https://gitlab.slack.com/archives/g_duo_chat)
- **Public stage channel:** [#s_ai-clients-questions](https://gitlab.enterprise.slack.com/archives/C058YCHP17C) — questions and outreach
- **Internal stage channel:** [#s_ai-clients](https://gitlab.slack.com/archives/s_ai-clients) — team syncs only

---

## 🏠 Functional Teams

| Team | Scope | Channel |
|---|---|---|
| [Web Chat](/handbook/engineering/ai/ai-clients/duo-chat/web-chat/) | Duo Chat in the GitLab web UI | [#duo-chat-lounge](https://gitlab.enterprise.slack.com/archives/C06LWENL58F) |
| [Chat Engine](/handbook/engineering/ai/ai-clients/duo-chat/chat-engine/) | Core chat engine powering Duo Chat across all surfaces | [#duo-chat-lounge](https://gitlab.enterprise.slack.com/archives/C06LWENL58F) |

---

## 📚 How We Work

### Host Systems

A host system is a platform where Duo Chat is integrated. Below is a list of all currently existing host systems:

| Host System | Description | Repository Link |
| -------- | ------- | ------- |
| GitLab Web UI | Web-based user interface for Duo Chat | [gitlab-org/gitlab](https://gitlab.com/gitlab-org/gitlab) |
| VS Code | The Visual Studio Code extension integrating Duo Chat | [gitlab-org/gitlab-vscode-extension](https://gitlab.com/gitlab-org/gitlab-vscode-extension) |
| Visual Studio | The Visual Studio extension integrating Duo Chat | [gitlab-org/editor-extensions/gitlab-visual-studio-extension](https://gitlab.com/gitlab-org/editor-extensions/gitlab-visual-studio-extension) |
| JetBrains | The JetBrains IDE plugin for Duo Chat | [gitlab-org/editor-extensions/gitlab-jetbrains-plugin](https://gitlab.com/gitlab-org/editor-extensions/gitlab-jetbrains-plugin) |

### Ownership and Maintenance of Duo Chat Integrations

This defines the ownership and maintenance responsibilities for Duo Chat integrations, detailing the roles of the Duo Chat team and the Developer Clients team.

| System part | Group Responsible |
| -------- | ------- |
| Shared UI components in Duo-UI | group: duo chat |
| VS Code - Chat Webview | group: duo chat (support: developer clients) |
| VS Code - Chat Business Logic | group: developer clients |
| Visual Studio - Chat Webview (web page) | group: duo chat (support: developer clients) |
| Visual Studio - Chat Business Logic | group: developer clients |
| JetBrains - Chat Webview (web page) | group: duo chat (support: developer clients) |
| JetBrains - Chat Business Logic | group: developer clients |

#### Responsibilities

1. Simple Component Updates: The UI component group (group: duo chat) is responsible.
2. Complex Feature Integrations: The UI component group (group: duo chat) drives the integration, creating stubs for extension communication with dummy data. group: developer clients supports the integration effort into IDE plugins.
3. Breaking Changes: All breaking changes should be communicated early. Consider making new features optional whenever possible to prevent disruptions in IDE extension workflows.

#### Tools

- [GitLab Duo Hosts Status Page](https://jannik_lehmann.gitlab.io/gitlab-ui-hosts-status-page/): Tracks the GitLab UI & Duo UI version used by each host system.

### Planning Process

This flowchart describes the planning process for the Duo Chat team:

![Duo Chat Planning Flowchart](/images/duo_chat_planning_flowchart.png)

The top part of the chart is what we do prior to the formal milestone planning. Those pre-planning activities should happen in an ongoing continuous manner over time as new issues are created.

The bottom part of the diagram depicts what happens in the first two weeks of the calendar month, when we formally add issues for the milestone, assess the overall load and commit to the deliverables.

For the **planning breakdown** step, here are the questions that engineers should be able to answer before assigning a weight:

- Are the requirements clear, concrete and I fully understand what is expected to be delivered?
- Are the requirements comprehensive and cover some of the less obvious paths of execution? (i.e. those out of the "happy path" like edge cases, packaging, and error handling).
- Are considerations around non-functional requirements accounted for? i.e. Scalability, accessibility, compliance, security, instrumentation etc.
- Is the requirement around quality expectation and/or level of testing/evaluation clear and understood?
- Can I see a path to technical implementation that allows me to provide a reasonable estimation for the issue? i.e. are all technical unknowns resolved or manageable without any additional technical research spikes?

If the answer to any of these questions is 'no', then the issue should be moved back to `~workflow::refinement`.

### Issue Estimation

This system should be used when estimating tasks:

- **0 - Little to no effort is required** Something that would be quicker to do than it was to create the issue.
- **1 - Extra small** The engineers feel they understand most requirements and consider it relatively easy, probably the smallest item in the milestone and mostly likely completed in one day.
- **2 - Small** A little bit of thought, effort, or problem-solving is required, but the engineers have confidence in the requirements.
- **3 - Average** Engineers have done this a lot; they know what needs to be done. There may be a few extra steps, but that's it.
- **5 - Large** This is complex work, or the engineers don't do this very often. Most engineers will need assistance from someone else on the team. This is probably one of the largest items that can be completed within a milestone.
- **8 - Extra large** This is going to take some time and research and probably more than one engineer to complete within the milestone. At this size, we should be looking at how we can split this into smaller issues/tasks.
- **13+ - Too large** This issue is far too complex, large, or under-defined. Anything with a weight of this size should go back to `~workflow::refinement` to be refined and split into more manageable chunks.

### Status Updates

To keep stakeholders informed and support async collaboration, all status updates for deliverables in the **current milestone** must be reported directly in the deliverable's issue using the standard template below.

#### When to Post an Update

Post an update whenever there is a meaningful change in status — for example, when work begins, when a risk is identified, when scope changes are being considered, or at regular check-in points during the milestone. At minimum, you should post one update every week.

#### Template

Use the following template when posting your update as a comment in the issue:

```markdown
## Async issue update

- Current status: <describe the deliverable's status>.
- Shipping this milestone: <yes/no>
- Scope reduction opportunities: <yes/no>

/health_status <on_track|at_risk>
/cc <stakeholders for this deliverable>
```

- **Current status** — Briefly describe where things stand. Include what has been completed, what is in progress, and any blockers or dependencies that may affect delivery.
- **Shipping this milestone** — Indicate `yes` if the deliverable is on track to ship within the current milestone, or `no` if it will slip. If the answer is `no`, add a short explanation in the current status field.
- **Scope reduction opportunities** — Indicate `yes` if there are parts of the deliverable that could be descoped to meet the milestone deadline, or `no` if the current scope is the minimum viable delivery. If `yes`, briefly describe what could be reduced.
- **`/health_status`** — Apply `on_track` if the deliverable is progressing as expected, or `at_risk` if there is uncertainty around shipping on time or at full scope.
- **`/cc`** — Tag any team members or stakeholders who should be notified of this update (e.g., PM, EM, designer, downstream teams).

---

## 🔗 Other Useful Links

### 📝 Dashboards (internal only)

- [Duo Chat xAU, retention, event count, and response time](https://10az.online.tableau.com/#/site/gitlab/views/AiFeatures/Focusview?:iid=3)
- [Slash command usage and user counts](https://10az.online.tableau.com/#/site/gitlab/views/SlashUseDuo/SlashUseDashboard/3e8fd0ba-f45b-4dd0-b649-84db3636553d/8db30355-e2c0-4636-9c43-5429bb952a41?:iid=4)
- [Duo Chat Error Rate in Elastic](https://log.gprd.gitlab.net/app/dashboards#/view/5f334d60-cfd7-11ee-bc6b-0b206b291ea1?_g=(refreshInterval:(pause:!t,value:60000),time:(from:now-2d,to:now)))
- [Duo Chat Error Budget in Grafana](https://dashboards.gitlab.net/d/stage-groups-detail-duo_chat/6c28d63a-60e8-5db3-9797-39f988a1900b?orgId=1)
- [Duo Feedback](https://10az.online.tableau.com/#/site/gitlab/views/DuoFeedbackDashboard/DuoFeedbackDashboard?:iid=1)
- [Duo Chat Question Categorization](https://10az.online.tableau.com/#/site/gitlab/views/DuoCategoriesofQuestions/DuoCategory?:iid=1)
- [Chat QA Evaluation](https://gitlab.com/gitlab-org/ai-powered/ai-framework/qa-evaluation)
- [AI Gateway Reporting](https://10az.online.tableau.com/#/site/gitlab/views/AIGatewayReporting/Overview/61d07174-d973-4552-a582-48be74efea8c/f463620d-a659-4cfb-9700-952a5c103fa8?:iid=1)

### Support

- [Duo Chat Runbook](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/duo-chat/README.md?ref_type=heads)
- [Duo Chat Support project](https://gitlab.com/gitlab-org/ai-powered/duo-chat/support)
