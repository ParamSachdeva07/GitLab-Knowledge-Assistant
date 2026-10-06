---
title: Fulfillment and Monetization Ways of Working
description: "Shared project management process, stable counterparts, and channels for the Fulfillment and Monetization sections."
---

The [Monetization](/handbook/engineering/development/monetization/) and [Fulfillment](/handbook/engineering/development/fulfillment/) sections share one way of working. Section specific content, including CustomersDot engineering and incident processes on the Monetization page, lives on each section page.

## Shared Slack channels

| Channel | Purpose |
|---------|---------|
| [#fulfillment_monetization_fyi](https://gitlab.slack.com/app_redirect?channel=fulfillment_monetization_fyi) | Front door for questions to either section |
| [#fulfillment_monetization_engineering](https://gitlab.slack.com/app_redirect?channel=fulfillment_monetization_engineering) | Shared engineering room |
| [#fulfillment_monetization_daily](https://gitlab.slack.com/app_redirect?channel=fulfillment_monetization_daily) | Daily standup updates |
| [#fulfillment_monetization_pm](https://gitlab.slack.com/app_redirect?channel=fulfillment_monetization_pm) | Product management |
| [#fulfillment_monetization_design](https://gitlab.slack.com/app_redirect?channel=fulfillment_monetization_design), [#fulfillment_monetization_research](https://gitlab.slack.com/app_redirect?channel=fulfillment_monetization_research) | Product Design and UX Research |
| [#fulfillment_monetization_speak_spark](https://gitlab.slack.com/app_redirect?channel=fulfillment_monetization_speak_spark) | Social |

When asking in the front door channel, react with ✅ once answered. For urgent customer issues use [STAR escalation](/handbook/support/internal-support/support-ticket-attention-requests/). For licensing or subscription requests involving a customer, use the [internal request form](https://support-super-form-gitlab-com-support-support-op-651f22e90ce6d7.gitlab.io/).

## Stable counterparts

### Sales and Go-To-Market

{{< member-and-role-by-gitlab "cnodari" "jrabbits" "Gsodhi" >}}

### Finance and IT

{{< member-and-role-by-gitlab "s_mccauley" "annapiaseczna" "andrew_murray" "smundy" "lmendonca2" >}}

### Support Engineering

{{< member-and-role-by-gitlab "jlyttle" "mdunninger" "kslaats" >}}

### Product Technical Program Management

{{< member-and-role-by-gitlab "cersoz" >}}

## Project management process

We work transparently, keep nearly everything public, and follow the [Product Development Flow](/handbook/product-development/how-we-work/product-development-flow/#workflow-summary).

### SAFE

Our work touches financial and sensitive information. Keep [SAFE](/handbook/legal/safe-framework/) epics, issues, videos, and MRs confidential, and use the [internal handbook](https://internal.gitlab.com/handbook/product/fulfillment/) for anything that cannot be public. See [promising features in future versions](https://docs.gitlab.com/ee/development/documentation/styleguide/availability_details.html#promising-features-in-future-versions).

### Planning

We plan in monthly milestones following the [Product Development Timeline](/handbook/engineering/workflow/#product-development-timeline). Each group has a [planning issue](https://gitlab.com/gitlab-org/fulfillment/meta/-/work_items/?sort=priority_desc&state=opened&label_name%5B%5D=Planning%20Issue&first_page_size=100) that lists prioritized issues and capacity. Around the 26th, PMs and EMs review and weight candidate issues. Scope is final by the 1st.

Engineers work on `Deliverable` issues first, then pick from the top of the remaining milestone issues. Recurring operational work (monitoring rotations, triage) is planned as weighted issues so it counts against capacity.

### Intake request

To request roadmap work, open an [intake issue](https://gitlab.com/gitlab-org/fulfillment/meta/-/work_items/new?type=ISSUE&description_template=intake) and tag a PM. The PM evaluates it, creates an epic on the roadmap, links it from the intake issue, and closes the intake issue. We do not action requests outside this process.

### Prioritization

We follow the [prioritization framework](/handbook/product/product-processes/#prioritization) and [cross-functional prioritization](/handbook/product/product-processes/cross-functional-prioritization/). Inputs include SLAs, OKRs, the [Support priority issues list](/handbook/support/license-and-renewals/workflows/managing_product_issues/#supports-issue-list-for-fulfillment), and technical debt. We use the company 60/40 split between new work and maintenance as a guideline, not a rule. Each group sets its balance in its OKRs, escalating to the section if needed. Every team runs the [monthly prioritization template](https://gitlab.com/gitlab-org/fulfillment-meta/-/blob/master/.gitlab/issue_templates/monthly-prioritization.md) for cross-functional dashboard reviews.

### Estimation

Estimate after a preliminary investigation, usually during planning.

| Weight | Description |
|--------|-------------|
| 1 | Simplest possible change, no side effects. |
| 2 | Simple change, requirements fully understood. |
| 3 | Simple change with a bigger footprint. Requirements clear. |
| 5 | Complex change across areas, possibly refactoring. Some gaps likely. |
| 8 | Complex change touching much of the codebase or needing lots of input. |
| 13 | Significant change with dependencies and unclear requirements. Break it down before committing. |

We value [velocity over predictability](/handbook/engineering/development/principles/#velocity) but aim for 80% predictability because our work is cross-functional. When unsure, estimate high or split into a [spike](/handbook/product/product-processes/#spikes) and an implementation issue. Revise estimates immediately when they change and tell the PM.

### Weekly async issue updates

Engineers update their assigned issues weekly:

```markdown
### Async issue update

1. Current status (one sentence):
1. Confidence this lands in the milestone: not / slightly / very
1. Can this be broken down further? yes / no
1. Were expectations from the last update met? If not, why:

/health_status on_track | needs_attention | at_risk
```

Larger projects post weekly status in the parent epic covering % complete, status against key dates, risks and blockers with mitigation, and results.

### Demos

Share progress on multi-milestone work through demos in the [Fulfillment Demos playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0KpOKxufy-slaR-6swIfkDLP), following the [demo process](/handbook/engineering/workflow/demos/). Link the epic or MR in the description.

### User experience

Product Designers follow the [Product Design workflows](/handbook/upstream-studios/product-design/workflow/) and are assigned to projects, not groups, reviewed quarterly in the [UX priorities issue](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/?label_name%5B%5D=Fulfillment%20UX%20Priorities). Medium and large projects use a `[UX]` issue as the SSOT for designs. Request UX help or MR reviews in [#fulfillment_monetization_design](https://gitlab.slack.com/app_redirect?channel=fulfillment_monetization_design).

### Retrospectives

We run a monthly [async retrospective](/handbook/engineering/careers/management/group-retrospectives/) in [gl-retrospectives/fulfillment](https://gitlab.com/gl-retrospectives/fulfillment/issues/) after the 8th, followed by a recorded sync discussion around the 26th on a rotating timezone. Groups may also run quarterly [iteration retrospectives](/handbook/engineering/workflow/iteration/) on a specific issue or epic.

## Onboarding and social

New engineers use the [onboarding template](https://gitlab.com/gitlab-org/fulfillment-meta/-/blob/master/.gitlab/issue_templates/onboarding.md) and get an onboarding buddy. Optional weekly socials and quarterly [team days](https://gitlab.com/gitlab-org/fulfillment-meta/-/issues?sort=created_date&state=all&label_name[]=Team+Day) are on the [shared calendar](https://calendar.google.com/calendar/embed?src=gitlab.com_7199q584haas4tgeuk9qnd48nc%40group.calendar.google.com).

## Links

- [Fulfillment direction](/handbook/product/groups/fulfillment/direction/fulfillment_section/)
- [Fulfillment Guide](/handbook/product/groups/fulfillment/) (CustomersDot admin and process docs)
- [Issue tracker](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues)
- [Performance indicators](https://internal.gitlab.com/handbook/company/performance-indicators/product/fulfillment-section/) and [engineering dashboards](/handbook/product/groups/product-analysis/engineering/dashboards/)
- [Pair programming](https://gitlab.com/gitlab-org/fulfillment/meta/-/tree/master/docs/pair_programming.md)
