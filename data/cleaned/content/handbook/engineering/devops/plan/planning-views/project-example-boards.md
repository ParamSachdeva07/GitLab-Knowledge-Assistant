---
title: "Boards on Saved Views: Project Example"
---

## Timeline

```mermaid
gantt
    title Lifecycle Boards
    dateFormat YYYY-MM-DD
    axisFormat %b %d

    section Milestones
    18.10                    :m1810, 2026-02-14, 2026-03-13
    18.11                    :m1811, 2026-03-14, 2026-04-10
    19.0                     :m190, 2026-04-11, 2026-05-15
    19.1                     :m191, 2026-05-16, 2026-06-12
    19.2                     :m192, 2026-06-13, 2026-07-10
    19.3                     :m193, 2026-07-11, 2026-08-14

    section Pre-work
    Requirements discovery   :discovery, 2026-02-14, 2026-04-18
    Groundwork            :prereqs, 2026-03-14, 2026-04-24

    section Active development
    Alpha                    :alpha, 2026-04-18, 2026-05-29
    Internal rollout         :crit, milestone, 2026-05-29, 0d
    GA                       :ga, 2026-05-29, 2026-07-10
    GitLab.com rollout       :crit, rollout, 2026-06-26, 2026-07-10

    section Feedback and clean-up
    Post-GA follow-ups       :followups, 2026-06-26, 2026-08-14
```

## Stages

We break projects into time-limited stages and cut scope to a [minimal viable change](/handbook/values/#minimal-valuable-change-mvc) to:

- Reduce cognitive load — engineers work on smaller changes, smaller sets of requirements, and fewer issues.
- Simplify project management and spot delays early — smaller stages are easier to keep on track and it's easier to notice when one is late.
- Surface bugs and feedback earlier.

| Stage | Outcome |
|-------|---------|
| **Requirements discovery** | Decision on scope for subsequent stages. Work broken down into issues. Rough estimation of the project. Clear definition of what is out of scope. |
| **Groundwork** | Refactorings and adaptations that make the rest of the development easier. |
| **Alpha** | Core workflow can be used for dogfooding and internal testing, but can be rough on the edges. Includes addressing internal testing feedback. |
| **GA** | The smallest coherent experience we're comfortable releasing to users. Includes addressing user feedback from alpha, fixing rough edges, and a feature flag rollout period (~2 weeks before milestone cut-off). |
| **Post-GA follow-ups** | Features deferred past the initial release, user feedback, code and test cleanup. Must be completed within 1–2 milestones after GA. When in doubt, put issues in out of scope. |
| **Out of scope** | No commitment. May be done later, reprioritized, or closed. |

## Epic organization

```plain
Lifecycle Boards (top-level epic)
├── Lifecycle Boards — Requirements discovery
│   ├── UX discussions (issue)
│   ├── Lifecycle Boards — Card (epic)
│   ├── Lifecycle Boards — Columns (epic)
│   └── ...
├── Lifecycle Boards — Groundwork
│   ├── Refactor work item listing page (epic)
│   ├── Load work items via REST API instead of GraphQL on listing pages (epic)
│   └── ...
├── Lifecycle Boards — Alpha
│   ├── Status columns (epic)
│   │   ├── Load available statuses (issue)
│   │   └── Load work items by column (issue)
│   ├── Card (epic)
│   ├── API changes (epic)
│   ├── Transform view preferences dropdown into drawer (epic)
│   ├── Card drag and drop (epic)
│   │   ├── Persist changes (issue)
│   │   └── Basic animation (issue)
│   └── ...
├── Lifecycle Boards — GA
│   ├── Internal testing feedback (issue)
│   ├── Card enhancements (epic)
│   ├── Feature flag rollout (epic)
│   ├── Card drag and drop (epic)
│   │   ├── Improved animation (issue)
│   │   └── Highlight available and unavailable columns (issue)
│   └── ...
├── Lifecycle Boards — Post-GA follow-ups
│   ├── User feedback (issue)
│   ├── Feature flag removal (epic)
│   ├── Old code cleanup (epic)
│   ├── Tests cleanup (epic)
│   └── ...
└── Lifecycle Boards — Out of scope
```
