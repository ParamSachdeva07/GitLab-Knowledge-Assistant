---
title: "Agent plan (MVC)"
description: "Design for the Agent plan work item widget that stores the core Markdown artifact of the SDD flow."
status: ongoing
maturity: mature
creation-date: "2026-04-16"
authors: [ "@fredericcaplette", "@vanessaotto" ]
owning-stage: "~devops::plan"
toc_hide: true
---

Read more about SDD in [Spec-Driven Development](_index.md).

**Maturity: Mature**

## Summary

The Agent plan is a new Work Item widget that stores a Markdown document. It is the core artifact of the SDD flow: shaped by humans and agents, then consumed downstream by Duo Developer and Duo Review or any other AI Agent.

Epic: [Workstream 0 — Agent plan](https://gitlab.com/groups/gitlab-org/-/work_items/21511)

## Data model

Agent plans are stored in a **separate table** (`work_item_work_plans`) joined to the Work Item by `work_item_id`. The issues table is too large to extend directly, so the plan data lives in its own table and is fetched through a `JOIN` when the widget is requested. For the MVC the table stores a single Markdown text column. The widget is added to all work item types but gated behind a feature flag.

The Agent plan is queryable through both the existing widget pattern and the new `features` field:

```graphql
fragment BaseWorkItemWidgets on WorkItemWidget {
  ... on WorkItemWidgetAgentPlan {
    content
  }
}
```

```graphql
fragment BaseWorkItemFeatures on WorkItemFeatures {
  agentPlan {
    content
  }
}
```

Draft MRs: [BE](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/230936), [AI Assist](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/merge_requests/5215)

## Widget rendering

The widget has three states:

1. **Empty** — placeholder with a prompt to generate or write a plan.
2. **Read** — rendered Markdown preview.
3. **Edit** — plain text editor (with Markdown preview toggle).

When AI generates or updates the plan through a tool call, the widget transitions to the read state showing the new content.

## AI generation

The plan is generated and refined through sync Duo Chat using work item tools in AI Gateway.

- A new or extended tool writes specifically to the Agent plan widget (not the work item description).
- Context assembled for generation: work item description, comments, labels, Decision Log entries.
- The agent can perform partial updates or full rewrites of the plan content.
- Output conforms to work item templates when configured on the project.

## API surface

The Agent plan is exposed through the standard Work Item widget GraphQL API pattern. It is also available through REST so external tools (`curl`, `glab`, IDE extensions) can read and write plans.

## Lifecycle

Draft -> Agent-ready. Graduation criteria are defined in [Plan readiness scoring](scoring.md).

## Decisions

| Date | Decision | Who |
| ------ | ---------- | ----- |
| 2026-03-30 | Agent plan is **not a standalone entity** — it is a widget on the Work Item, supporting all work item types. | Workshop |
| 2026-03-31 | Output format is **Markdown**, shaped by Work Item Templates. | @fredericcaplette |
| 2026-04-09 | Use **sync Duo Chat** (not async/streaming) for AI interactions on the Work Item. | @vanessaotto, @fredericcaplette |
| 2026-04-09 | **Markdown over YAML** for simplicity and human readability. | @fredericcaplette, @vanessaotto, @timzallmann |
| 2026-04-09 | Named **"Agent plan"** for the first iteration. | @izzychu, @fredericcaplette |
| 2026-04-16 | Agent plan stored in a **separate table** joined to the Work Item (issues table too large to extend). | @fredericcaplette |
| 2026-04-16 | AI Gateway will **expand the existing Work Item tool** (not create a new tool) to read/write the Agent plan widget. | @fredericcaplette |
| 2026-04-16 | Agent plan content is stored and served as **raw Markdown**. No structured schema or YAML front matter. | @fredericcaplette |

## Permissions and feature gating

Discussion: [MR !231689 thread](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/231689#note_3260440309)

The Agent plan widget visibility is controlled through multiple layers:

1. **Feature flag (WIP)** — The `wip` feature flag `agent_plan` gates the widget on both backend and frontend while the feature is under development. The frontend flag lets the team ship across multiple MRs without exposure risk. Once development is complete, the team will revisit whether to ship as `beta` or remove the frontend flag and rely on backend flags only.
2. **Licensed feature** — The widget is an EE feature (at least Premium tier). It will reuse an existing licensed feature (`ai_workflows` or `ai_features`) rather than creating a new one, unless SDD gets its own licensed feature later.
3. **Duo availability (for the AI quick action only)** — The widget itself is visible to anyone with access through the feature flag + license. The Duo Chat quick action to *generate* the plan additionally requires Duo Chat availability (`duoChatAvailable` GraphQL query) plus agentic mode (`tanuki_bot.agentic_mode_available?` in Ruby). Once Classic Chat is deprecated, the `duoChatAvailable` check alone should suffice.
4. **Cascading namespace setting (future)** — A toggle to allow admins/group owners to turn the feature off at the namespace level. Not part of MVC1 but needed before external rollout.

Backend permissions on the widget data (`userPermissions` fields) and tighter gating through configurable work item types are deferred — to be revisited before GA.

## Active issues

- [Feature flag + placeholder UI](https://gitlab.com/gitlab-org/gitlab/-/work_items/596915)
- [Update Work item tool with Agent plan](https://gitlab.com/gitlab-org/gitlab/-/work_items/596371)
- [Agent plan widget UI](https://gitlab.com/gitlab-org/gitlab/-/work_items/596370)
- [Agent plan widget API](https://gitlab.com/gitlab-org/gitlab/-/work_items/596369)
