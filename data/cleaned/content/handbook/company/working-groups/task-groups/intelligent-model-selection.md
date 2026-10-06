---
title: "Intelligent Model Selection"
description: "A Task Group introducing intelligent model selection for GitLab Duo: GitLab picks the best model for each task across all Duo features, proven first on the Duo Developer flow."
---

## Attributes

| Property        | Value                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Date Created    | 2026-08-31                                                                                                                               |
| Target End Date | 2026-10-09 (close of [GitLab 19.5](https://gitlab.com/groups/gitlab-org/-/milestones/139))                                               |
| Slack           | [#intelligent-model-selection-working-group](https://gitlab.slack.com/archives/C0BN1LBMBU6) (only accessible from within the company)     |
| Sync notes      | [Google Doc](https://docs.google.com/document/d/1LZ81H8tfsHXIQzF3uUs9lPHPp1Mc3Jjiqlfvbv6aR-0) (only accessible from within the company)   |
| Main epic       | [Intelligent model selection for Duo Agent Platform & Duo features](https://gitlab.com/groups/gitlab-org/-/epics/22485)                   |

## Context

Admins and group owners already choose which model each GitLab Duo feature uses through [model selection](https://docs.gitlab.com/administration/gitlab_duo/model_selection/). That choice is static: the selected model serves every request the feature makes. For agentic features such as the Duo Agent Platform, this is a poor fit. A single flow mixes trivial steps (reading a file, a short lookup) with complex, multi-step reasoning, and the same large model handles all of them today, regardless of what each step actually needs.

Intelligent model selection lets GitLab pick the best model for each task instead. Small tasks go to smaller, faster models and complex tasks go to larger ones. End users get a sensible default without having to reason about model choice, and cost and latency drop without giving up quality on complex work. [GitHub Copilot's auto model selection](https://docs.github.com/en/copilot/concepts/models/auto-model-selection) is the closest industry reference for this behavior.

### Goals

Routing on a single flow is not the goal. The objective is for every Duo feature to select the best model for the task it is running. Getting there safely means proving the mechanism on one well-bounded flow first, so the work is planned in two phases:

1. **Groundwork.** Reframe the existing "GitLab default model" option from a model into a policy: one "GitLab managed" setting that covers everything GitLab optimizes on the customer's behalf, including default model management, load balancing, and intelligent model routing. Split the Duo Developer flow into its own feature setting with a dedicated model selector, giving the routing work a small, well-bounded surface to validate against ([Phase 1 epic](https://gitlab.com/groups/gitlab-org/-/epics/23227), confidential).
2. **Small/large model routing for Duo Developer.** Run evaluations over a representative set of Duo Developer tasks to establish quality, latency, and cost baselines for candidate small and large models, then implement routing guided by those baselines ([Phase 2 epic](https://gitlab.com/groups/gitlab-org/-/epics/23228), confidential). The routing layer's design is recorded in an [architecture decision record](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/work_items/2707). Routing ships behind a feature flag scoped to the "GitLab managed" setting, so it can be rolled back quickly if results degrade.

## Exit Criteria

1. The "GitLab default model" option is reframed as the "GitLab managed" policy setting, and Duo Developer has its own feature setting with a dedicated model selector (Phase 1).
2. Evaluation baselines for candidate small and large models exist for a representative set of Duo Developer tasks, and can be re-run when the candidates change (Phase 2).
3. Small/large model routing for Duo Developer is available behind a feature flag, with evaluated quality on par with the large-model baseline and a measured cost reduction (Phase 2).

## Long term vision

There are further optimizations we expect to want eventually. They are recorded here rather than in the phases above because this task group is not committing to them:

- Expanding intelligent model selection to the remaining Duo features, reusing the evaluation and release process proven on Duo Developer.
- Model allow-listing, so group owners and admins can constrain the set of models routing is allowed to choose from.
- LLM-based routers, replacing heuristic routing with a model that classifies how hard a task is.
- Additional UI customization for how model selection surfaces to end users.

## Roles and Responsibilities

| Task Group Role | Person                                                   | Title                                     |
| --------------- | -------------------------------------------------------- | ----------------------------------------- |
| DRI             | [Julie Huang](https://gitlab.com/julie_huang)            | Senior Fullstack Engineer, AI Engineering |
| Member          | [Alejandro Rodríguez](https://gitlab.com/alejandro)      | Staff Backend Engineer, AI Engineering    |
| Member          | [Manoj M J](https://gitlab.com/manojmj)                  | Staff Backend Engineer, AI Engineering    |
| Member          | [Nathan Weinshenker](https://gitlab.com/nateweinshenker) | Backend Engineer, AI Engineering          |
| Member          | [Newvick Lee](https://gitlab.com/nlee8)                  | Backend Engineer, AI Engineering          |
