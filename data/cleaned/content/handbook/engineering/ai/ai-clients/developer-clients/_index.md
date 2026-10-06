---
title: Developer Clients Group
description: "The Developer Clients group owns and maintains the editor extensions for VS Code and JetBrains IDEs, as well as the Duo CLI, bringing GitLab's core features and AI capabilities directly into developer workflows."
---

## 🚀 Vision

We bring GitLab's core features and AI capabilities directly into developer workflows, unlocking productivity by making GitLab accessible in the tools developers use every day.

This group is part of the [AI Clients stage](/handbook/engineering/ai/ai-clients/).

---

## 👨‍💻 Team Members

**Engineering Manager:** Amr Elhusseiny

**Product Manager:** James Casey

**UX:** Yi-Ann Chen

{{< team-by-manager-slug "aelhusseiny" >}}

---

## 🤝 Stable Counterparts

Below are our [stable counterparts](/handbook/leadership/#stable-counterparts):

{{< group-by-slugs james.casey sam_reiss ychen16 jglassman1 >}}

---

## 💬 Where to Find Us

### Slack

- **Public stage channel:** [#s_ai-clients-questions](https://gitlab.enterprise.slack.com/archives/C058YCHP17C) — questions and outreach
- **Internal stage channel:** [#s_ai-clients](https://gitlab.slack.com/archives/s_ai-clients) — team syncs only
- **Functional teams' slack channels:**
  - Duo CLI: [#f_duo_cli](https://gitlab.slack.com/archives/f_duo_cli)
  - VS Code extension: [#f_vscode_extension](https://gitlab.slack.com/archives/C013QJ9NEPL)
  - JetBrains plugin: [#f_jetbrains_plugin](https://gitlab.slack.com/archives/C02UY9XKABH)
- **Other slack channels we maintain:**
  - Visual Studio extension: [#f_visual_studio_extension](https://gitlab.enterprise.slack.com/archives/C0581SE363C)
  - Eclipse plugin: [#f_eclipse_plugin](https://gitlab.enterprise.slack.com/archives/C07MKHCFGHG)
  - Neovim Plugin: [#f_neovim_plugin](https://gitlab.enterprise.slack.com/archives/C05BF7L6PEX)
  - Web IDE: [#f_vscode_web_ide](https://gitlab.enterprise.slack.com/archives/C03CEHDPQGH)

### Shared Calendar

We use [AI Clients's shared calendar](/handbook/engineering/ai/ai-clients/#shared-calendar)

---

## 🏠 Functional Teams

| Team | Scope | Channel |
|---|---|---|
| [Duo CLI](/handbook/engineering/ai/ai-clients/developer-clients/duo-cli/) | AI-powered command-line interface | [#f_duo_cli](https://gitlab.slack.com/archives/f_duo_cli) |
| [VS Code](/handbook/engineering/ai/ai-clients/developer-clients/vscode/) | GitLab Workflow VS Code extension & Web IDE | [#f_vscode_extension](https://gitlab.slack.com/archives/C013QJ9NEPL) |
| [JetBrains](/handbook/engineering/ai/ai-clients/developer-clients/jetbrains/) | GitLab plugin for JetBrains IDEs | [#f_jetbrains_plugin](https://gitlab.slack.com/archives/C02UY9XKABH) |

---

## 💻 Scope

### Products owned by this group

1. **GitLab Extension for JetBrains**
   1. [Repo](https://gitlab.com/gitlab-org/editor-extensions/gitlab-jetbrains-plugin)
   2. [Docs](https://docs.gitlab.com/editor_extensions/jetbrains_ide/)
   3. [Backlog](https://gitlab.com/groups/gitlab-org/-/issues/?label_name%5B%5D=Editor%20Extensions%3A%3AJetBrains)
   4. Slack Channel: [#f_jetbrains_plugin](https://gitlab.enterprise.slack.com/archives/C02UY9XKABH)
2. **GitLab Workflow Extension for VS Code**
   1. [Repo](https://gitlab.com/gitlab-org/gitlab-vscode-extension)
   2. [Docs](https://docs.gitlab.com/editor_extensions/visual_studio_code/)
   3. [Backlog](https://gitlab.com/groups/gitlab-org/-/issues/?label_name%5B%5D=group%3A%3Aeditor%20extensions)
   4. Slack Channel: [#f_vscode_extension](https://gitlab.slack.com/archives/C013QJ9NEPL)
3. **Duo CLI**
   1. [Repo](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp/-/tree/main/packages/cli)
   2. [Backlog](https://gitlab.com/groups/gitlab-org/-/boards/9839597?epic_id=3743089)
   3. Slack Channel: [#f_duo_cli](https://gitlab.slack.com/archives/f_duo_cli)

---

## 📚 How We Work

### Issues' State

We use the issue `Status` field to indicate state, following the [Product Development Flow](/handbook/product-development/how-we-work/product-development-flow/).

{{% details summary="Expand for more details" %}}

To keep things simple, we focus on the main states below and optionally use others when appropriate.

- **New →** Not yet prioritized or refined.

- **Planning breakdown →** Needs team attention soon (within ~1–2 months); gather scope, risks/deps, acceptance criteria.

- **Ready for development →** Immediate priority; clear scope; should be picked up next and ideally completed within ~2 weeks.

- **In dev →** Assigned DRI(s), milestone set, work in progress.

- **In review →** Implementation complete; MR opened and under review/verification.

- **Blocked →** Cannot proceed due to a dependency or external constraint; comment the blocker and next check-in date.

- **Closed →** Done (or closed as duplicate/won't fix) with outcome noted.

**Note:** We chose `Planning breakdown` & `Ready for development` as these statuses exist on both Issues and Tasks, letting us build one unified set of boards and embedded tables with a single status filter easily.

{{% /details %}}

### Milestone Planning

We plan per [milestone](https://mnohr.gitlab.io/milestone-dates/). We release much more often and with more flexibility, but the milestone cadence keeps us aligned with release posts for new features and with other teams when alignment is needed.

> This process is intentionally minimal — we start small and iterate based on the [feedback loop](#feedback-loop).

At a glance — two artifacts, two rituals:

| Artifact | Used | Answers |
|---|---|---|
| [Team backlogs](#team-backlogs) | Before planning | What should we work on next? |
| [Planning boards](#planning-boards) | During the milestone | What is the status? What is in progress? |

| Ritual | Cadence | What happens |
|---|---|---|
| Planning call — one per functional team | Monthly | Commit issues based on team capacity, assign [weights](#issues-weight); assignees and `Deliverable` / `Stretch` [labels](#issues-labels) are set in 1:1s instead, to save call time |
| [Async updates](#weekly-async-updates) | Weekly (by Tuesday EOD) | Everyone posts progress on their issues; automation aggregates them into one group-wide issue |

{{% details summary="The flow in detail (chronological)" %}}

1. **Throughout the milestone — prepare for the next one.** Flag issues you want prioritized next milestone with the [`workflow::scheduling`](https://gitlab.com/groups/gitlab-org/-/issues?sort=updated_asc&state=opened&label_name%5B%5D=workflow%3A%3Ascheduling&label_name%5B%5D=group%3A%3Adeveloper+clients) label. For an uncertain effort with no issue yet, create a placeholder (an empty description is fine) with a timeboxed [weight](#issues-weight). Keep statuses and labels current — the [planning boards](#planning-boards) double as our live view of milestone progress.
1. **Before the planning call.** EM + PM do an async backlog pre-pass, focusing on flagged issues, then send a Slack message a few days in advance with the agenda: the list of priorities and the updated [backlog page](#team-backlogs) — check it before the call. Everyone: have a rough idea of your availability (for example, planned vacation days). Plans can change — that's fine, we adapt.
1. **Monthly planning call — one per functional team.** Agree on the issues committed to the milestone based on team capacity, assign [weights](#issues-weight), and plan capacity using the planning board's capacity feature. To save call time, assignees and the `Deliverable` / `Stretch` [labels](#issues-labels) are set in 1:1s afterwards.
1. **During the milestone.** The planning board shows the milestone state and in-progress work. Post your [weekly async updates](#weekly-async-updates).

{{% /details %}}

#### Planning Boards

| Team | Board | Issues shown |
|---|---|---|
| Duo CLI | [dc-duo-cli](https://milestone-planning-board-0c5b79.gitlab.io/?board=dc-duo-cli) | `category:duo cli` label, or in the [gitlab-lsp](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp) repo with "cli" in the title |
| VS Code | [dc-vs-code](https://milestone-planning-board-0c5b79.gitlab.io/?board=dc-vs-code) | `category:vs code` label, or in the [gitlab-vscode-extension](https://gitlab.com/gitlab-org/gitlab-vscode-extension) repo |
| JetBrains | [dc-jetbrains](https://milestone-planning-board-0c5b79.gitlab.io/?board=dc-jetbrains) | `category:jetbrains` label, or in the [gitlab-jetbrains-plugin](https://gitlab.com/gitlab-org/editor-extensions/gitlab-jetbrains-plugin) repo |

#### Team Backlogs

Each functional team has a live backlog wiki page — the tables refresh automatically on page load, and cover **Added this milestone**, **Next to prioritize**, **Top community requests**, and the **full backlog**:

- [Duo CLI backlog](https://gitlab.com/gitlab-org/editor-extensions/meta/-/wikis/Developer-Clients:-Duo-CLI-Backlog)
- [VS Code backlog](https://gitlab.com/gitlab-org/editor-extensions/meta/-/wikis/Developer-Clients:-VS-Code-Backlog)
- [JetBrains backlog](https://gitlab.com/gitlab-org/editor-extensions/meta/-/wikis/Developer-Clients:-JetBrains-Backlog)

> 💡 An issue only shows up on a team's backlog page if it carries the team's category label: `category:duo cli`, `category:vs code`, or `category:jetbrains`. Each page has a "missing category label" section that surfaces unlabelled issues in the team's repository, and automating the labelling is tracked in [meta#398](https://gitlab.com/gitlab-org/editor-extensions/meta/-/work_items/398).

#### How to Participate (for non-team members)

If you want to bring an issue to the attention of the team, please create an issue. If no issue exists yet, then reach out on [#s_ai-clients-questions](https://gitlab.enterprise.slack.com/archives/C058YCHP17C).

#### Feedback Loop

This process is v1. We run a quick feedback poll in the team channels every ~2 milestones, plus a standing 5-minute retro slot in each monthly planning call.

### Team Sync Meetings

We join the weekly sync meeting held across the entire [AI Clients stage](/handbook/engineering/ai/ai-clients/).

- The call alternates every week between APAC/AMER & EMEA/AMER friendly times, so everyone can join conveniently at least every other call — and everyone can contribute async every week.
- The [Weekly Sync Meeting Agenda](https://docs.google.com/document/d/1UJg-Prf5qGjiGImvaYl5HNjMcJddoeE4u33Ri6SxQ6g) is open; everyone is invited to bring relevant topics to align on.
- Recordings are uploaded to the [Editor Extensions Category](https://www.youtube.com/playlist?list=PL05JrBw4t0KoC0pFfuNOAQjKxe4_ypFKc) playlist on GitLab Unfiltered.

### Weekly Async Updates

Post an update on each issue you're actively working on, using the [Dev Check-in (editor-extensions)](https://gitlab.com/groups/gitlab-org/editor-extensions/-/comment_templates) comment template.

**Note: async updates should be posted by Tuesday EOD every week** (or earlier if you're off).

Updates are aggregated automatically into a single weekly Developer Clients issue with a section per functional team ([example issue](https://gitlab.com/gitlab-org/editor-extensions/meta/-/work_items/400)).

### Issues' Labels

Check [AI Clients labeling guidance](/handbook/engineering/ai/ai-clients/#-how-we-label-issues-and-merge-requests)

Some extra labels we use:

| Label | Description |
|---|---|
| [`Deliverable`](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=all&label_name%5B%5D=Deliverable&first_page_size=20) | Committed items for the milestone / must-ship work. |
| [`Stretch`](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=all&label_name%5B%5D=Stretch&first_page_size=20) | Next items on the priority list, added as optimistic goals for the milestone |

### Issues' Weight

Weights are assigned during [milestone planning](#milestone-planning) as a rough estimate of complexity, using the [Fibonacci sequence](https://www.mountaingoatsoftware.com/blog/why-the-fibonacci-sequence-works-well-for-estimating) (`1, 2, 3, 5`):

| Weight | Rough effort |
|---|---|
| `1` | About half a day — including coffee-sized fixes (typo, small config tweak) |
| `2` | 1–2 days |
| `3` | About three days |
| `5` | About a week |
| `8` | A week and a half to two weeks — break it down |

- The scale is proportional: a weight is roughly that many working days (a `5` is a week). Weights can therefore be summed and compared, e.g., any issues totalling `8` are roughly a similar commitment to one `8`.
- This should serve as a rough sizing exercise, to give us a sense of the milestone capacity, so avoid spending too much effort trying to get an exact estimate — it's likely to change once we dive into implementation details.
- An `8` shouldn't be worked on as-is: we should break it down to smaller issues, or spike & time-box it first.

### Cross-Group Ownership and Boundaries

Editor extensions systems host features and modules owned by different groups.

The [Ownership and Boundaries](/handbook/engineering/ai/ai-clients/ownership/) page provides clarity and a clear expectation between all parties who author/maintain features in our systems.

---

## 🔗 Useful Links

- **Planning**
  - [Planning boards](#planning-boards)
  - [Team backlogs](#team-backlogs)
- **Dashboard & Monitoring**
  - <a href="https://app.snowflake.com/ys68254/gitlab/#/streamlit-apps/PROD.STREAMLIT_TEST.EDITOR_EXTENSION_DAU/!/editor_extension_dau" target="_blank">Snowflake: Developer Clients DAU & Usage</a>
  - <a href="https://app.snowflake.com/ys68254/gitlab/#/streamlit-apps/PROD.STREAMLIT_TEST.EDITOR_EXTENSION_DAU/!/language_server_metrics" target="_blank">Snowflake: LSP Speed Performance</a>
  - <a href="https://10az.online.tableau.com/#/site/gitlab/views/PDCodeSuggestions/IDEMetrics" target="_blank">Tableau: Code suggestions IDE metrics</a>
  - <a href="https://10az.online.tableau.com/#/site/gitlab/views/DRAFTCentralizedGMAUDashboard/MetricReporting/48493d6c-cd11-45b9-bdc5-bf5242e0de0b/EditorExtensionsMAU?:iid=2" target="_blank">Tableau: MAU</a>
  - <a href="https://dashboards.gitlab.net/dashboards/f/editor-extensions/?orgId=1" target="_blank">Grafana: Dashboard</a>
  - <a href="https://session-error-rates-dashboard-87d159.gitlab.io/" target="_blank">Agent Platform Session Error Rates</a>
- **Miscellaneous**
  - <a href="https://docs.google.com/document/d/1UJg-Prf5qGjiGImvaYl5HNjMcJddoeE4u33Ri6SxQ6g" target="_blank">Weekly Sync Meeting Agenda</a>
  - <a href="https://www.youtube.com/playlist?list=PL05JrBw4t0KoC0pFfuNOAQjKxe4_ypFKc" target="_blank">Editor Extensions playlist</a> on the GitLab Unfiltered YouTube channel
