---
title: Plan:Portfolio Planning Engineering Team - How we work
---

## Iteration Planning

> In 19.0 and 19.1 we are experimenting with two-week iterations to simplify planning and reduce work in progress.

Each milestone is split into two two-week iterations. If a milestone has five weeks, the first week of the milestone is dedicated to improving GitLab's developer experience.

The [Plan:Portfolio Planning board](https://gitlab.com/groups/gitlab-org/-/boards/1569369) is the single source of truth for current work:

- **Ready for development** — current iteration only
- **Planning breakdown** — next iteration

Issues should not sit in these columns if we don't plan to work on them soon. The board has WIP limits to enforce this. If an issue has been in Ready for development for over 2 weeks or in Planning breakdown for over 4 weeks and we're not ready to pick it up, move it back to "New".

We use [planning issues](https://gitlab.com/gitlab-org/plan-stage/product/-/issues/?sort=title_asc&state=opened&label_name%5B%5D=group%3A%3Aportfolio%20planning&first_page_size=100) to coordinate and discuss iteration plans. Each project is assigned a [DRI](/handbook/people-group/directly-responsible-individuals/) who is responsible for breaking it down and planning the iteration.

### Quality rotation

Every iteration, one engineer serves as the [quality rotation DRI](https://gitlab.com/groups/gitlab-org/plan-stage/product-planning/-/wikis/Home/Engineering/QualityRotation). The quality DRI monitors error budgets, Sentry alerts, and incoming escalations, and works on high-severity maintenance issues when there are no urgent items. See the wiki page for the full scope and dashboard.

### Keeping work flowing

We use several mechanisms to reduce work in progress and keep issues moving:

- **WIP limits** on board columns prevent overloading any workflow stage.
- **Health status escalation** — we [automatically escalate health status](https://gitlab.com/gitlab-org/quality/triage-ops/-/merge_requests/3993) when an issue stays too long in one column. Health status is [cleared when the workflow state changes](https://gitlab.com/gitlab-org/quality/triage-ops/-/merge_requests/3994). Issues can opt out with the `~"Untrack Health Status"` label.
- **Prioritize reviews** — prioritize work that is further along: reviews over your own in-progress work, in-progress work over starting something new. When possible, keep complex reviews within the team and stick to the same reviewers to reduce ramp-up time.

## Breaking work down

The default work item type is **issue**. When in doubt, create an issue — it can be converted to an epic or task later.

| Type | Corresponds to | Timeline | Examples |
|------|---------------|----------|----------|
| **Issue** | One merge request, one person, one category (FE or BE) | Less than 1 week | "Add board card component", "Create `filter` query parameter for saved views API" |
| **Epic** | A scoped deliverable grouping multiple issues | 1 week to 3 milestones | "Boards on Saved Views Alpha", "Work Item Card" |
| **Task** | A checklist item / reminder inside an issue | — | "Update changelog", "Update documentation" |

For how we use work item types in larger projects, see [Project Example: Boards](../planning-views/project-example-boards.md). We don't use weights.

### What makes a good issue

- Small enough for one engineer to complete in a week or less. If it's bigger, consider promoting it to an epic or creating a [spike](#spikes-and-proof-of-concepts) to break it down.
- Includes enough issue-specific detail (requirements, decisions, constraints) that a team member seeing the issue for the first time has enough to get started.
- Links to requirements or acceptance criteria — Figma designs, wiki pages, epic description, or design documents. No need to copy content into the issue.
- Notes cross-functional needs — e.g., "needs FE + BE", "needs TW review for UI text".
- Marks blocking and related relationships with other issues.

### Spikes and Proof of Concepts

For issues with too many open questions or unclear scope, create a spike or PoC issue using the [Plan - Spike template](https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitlab/issue_templates/Plan%20-%20Spike.md) to dedicate capacity to investigation or a trial implementation.

The goal is a shared understanding between the engineering DRI, product, and UX of what to build, how to build it, and roughly how much effort it takes. This can lead to a project breakdown into issues, a definition of an alpha version, or a [design document](../_index.md#design-documents).

## Meetings

We hold three weekly sync meetings every Monday to cover all time zones: APAC+EMEA, EMEA+AMER, and AMER+APAC. Everyone can bring up topics — current projects, questions, blockers.

In the first week of each milestone, we use these meetings for a retrospective. All three sessions share the same retro board.

## Documentation

Write documentation as you go, even for features behind a feature flag. Use the [feature flag documentation guidelines](https://docs.gitlab.com/ee/development/documentation/feature_flags.html) to mark features that are not yet ready for production. This avoids a documentation rush at the end of a milestone.
