---
title: "How we report progress"
description: How the Co-Create & Community Engineering team structures objectives, KPIs, and the supporting work that ships them
---

## Why this exists

We report a significant amount of work against a small number of goals. This page defines the shared language we use so anyone, inside or outside the team, can understand a work item's deliverable type, measurement criteria, and owner. It keeps our reporting aligned with the operating model and creates a consistent language across the company.

## The structure

Each fiscal year, we set an **objective** and define **KPIs** to measure our success against it. Each quarter, we assign ownership for the KPIs and track the work that advances them beneath the relevant KPI. The hierarchy is as follows:

1. **Objective**: the qualitative direction for the year. It does not carry a number itself.
1. **KPI**: a measurable outcome that proves the objective is being reached.
1. **PI**, **action**, and **recurring** work: the measurable signals and the concrete work that move a KPI.

We use KPI and PI as two levels, a KPI on top with PIs supporting it. The [company KPI definition](/handbook/company/kpis/) treats them as one set with KPIs as the important subset of performance indicators; we apply a light hierarchy on top so reporting stays simple.

## The categories

Every work item under an objective belongs to exactly one of these four categories. This is the most important distinction on this page. Each category is defined by what the item is and by how fixed it is up front.

| Category | What it is | How progress is reported | How often it changes |
|---|---|---|---|
| **KPI** | Our main measurable outcome, the step toward the five-year goal. | The headline number against its target. Rolls up to the objective. | Set up front. Fixed for the period. |
| **PI** | A measurable signal that supports a KPI. | Its own number against its own baseline and target. Evidence of progress toward a KPI. | Added deliberately, rarely, with good reason. |
| **Action** | Work we deliver to move a PI or KPI. | Done, in progress, or not started. | Added constantly, on the fly. |
| **Recurring** | Standing team work that is part of the job and repeats every cycle, which we still want to track and recognize. Often a bucket, for example [Notable Contributor selection](/handbook/marketing/developer-relations/engineering/notable-contributor-process), [community office hours](/handbook/marketing/developer-relations/engineering/community-contributors-workflows/#community-office-hours), [product bonus points](/handbook/marketing/developer-relations/engineering/community-contributors-workflows/#highlighting-high-value-contributions-with-product-bonuses), and [contributor onboarding](https://gitlab.com/gitlab-community/maintainers/onboarding-maintainers/private-onboarding-notes). It moves each cycle and links in its body to the process it tracks. | Done, in progress, or not started, per cycle. | Repeats on a cadence. |

In summary: a **KPI** is the goal, a **PI** explains movement toward the goal, and an **action** is the work that drives progress. **Recurring** is that work when it repeats on a cadence.

An action does not need a metric to be valid. It stays relevant as tracked work. If an action can be sharpened into a measurable outcome, it can graduate to a PI or KPI.

## How the category is recorded

The category is a scoped label on a work item in GitLab. Every item under an objective contains one of:

| Label | Category |
|---|---|
| `report-as::kpi` | KPI |
| `report-as::pi` | PI |
| `report-as::action` | Action |
| `report-as::recurring` | Recurring |

The label is scoped, so an item can hold only one value at a time. This makes the category machine-readable: a person, a board filter, or an agent can tell what an item is without reading the description. Our reporting tooling reads these labels to build the status update, reporting each KPI with its number, each PI as evidence, and each action as done or in progress. If an item under an objective carries no `report-as::` label, it is unclassified and needs one.

The hierarchy is as follows: a KPI sits directly under the objective, while the individual work items beneath it are usually actions. Because exceptions exist, explicit labels remain important: they clarify reporting expectations for everyone from the outset.

## Who decides, and who owns

Two responsibilities, kept separate:

1. **Classification is decided at the team level, with the objective owner as the decisive voice.** Which category an item is (KPI, PI, action, or recurring) is agreed together and confirmed by the objective owner. We reformulate and iterate as our understanding sharpens.
1. **Every item has a DRI.** As a [Directly Responsible Individual](/handbook/people-group/directly-responsible-individuals/), you are not required to execute all the work alone. All of our work is a team effort. Being the DRI means you own the reporting of the item and the strategy for accomplishing it. As DRI, you own the decision and escalate when you see risks or opportunities.

The category tells you how an item is measured; the DRI tells you who owns it.
