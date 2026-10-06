---
title: Growth Stage
description: "The Growth Stage consists of development teams working in the product delivering enhancements and running experiments"
---

## Vision

Our vision is to make it effortless for individuals and teams to discover, activate, and expand enduring value in GitLab by running a full-funnel growth system that connects acquisition, activation, retention and monetization into measurable, self‑served loops.

```mermaid
flowchart TD
    ACQ["Acquisition\nSignup"]
    ACT["Activation\nGet value from the product"]
    MON["Monetization\nPay for the product"]
    ENG["Engagement\nContinue using the product"]
    RET["Retention\nContinue paying for product"]
    INV["Invite Velocity\nInvite others to the product"]

    ACQ --> ACT
    ACT --> MON
    ACT --> ENG
    ENG --> RET
    ENG --> INV
    MON --> RET
    INV --> ACQ
    ACQ --> MON
```

For more details on Growth's mission, direction, and product strategy, see the [Growth product handbook](/handbook/marketing/growth-marketing/).

## How We Work

Working inline with our [values](/handbook/values/), we focus on [iteration](/handbook/values/#iteration) and [collaboration](/handbook/values/#collaboration), working with and across areas of the product our development department counterparts maintain.

We work on the issues prioritized by our product teams including running [experiments](/handbook/engineering/development/growth/experimentation/) on GitLab.com. Growth stage teams have Fullstack Engineers. The reason for this is that the Growth stage has a need for both Frontend and Backend skill-sets, but as a small team, has optimized for team member efficiency to adopt the Fullstack role.

## Growth Leadership & Teams

### Leadership

| Role | Person |
|------|--------|
| Product Director | {{< member-by-name "Elyse Mallinger" >}} |
| Engineering Director | {{< member-by-name "Ekwa Duala-Ekoko" >}} |
| Engineering Manager | {{< member-by-name "Travis Shields" >}} |
| Senior Staff Fullstack Engineer | {{< member-by-name "Doug Stull" >}} |
| UX Design Manager | {{<member-by-name "Emily Sybrant">}} |

### Product & Design

| Role | Person |
|------|--------|
| Product Managers | {{< member-by-name "Elyse Mallinger" >}} |
| Product Designers | {{< member-by-name "Jesse Young" >}}, {{< member-by-name "Katie Macoy" >}} |

### Teams & Communication

All Growth teams share one Slack channel: [#s_growth](https://gitlab.slack.com/channels/s_growth).

| Team | GitLab Handle |
|------|---------------|
| Growth (All) | `@gitlab-org/growth` , `@gitlab-org/growth/engineers` |
| Acquisition | `@gitlab-org/growth/acquisition` |
| Activation | `@gitlab-org/growth/activation` |
| Engagement | `@gitlab-org/growth/engagement` |

### All Team Members

{{< team-by-manager-slug manager="tshields1" >}}

## Shared Processes

Our teams collaborate using shared processes and tools:

- [Operating Model](operating_model_growth.md) - operating rhythm for growth
- [Milestone Planning, Refinement and Estimation](initiative_refinement_estimation) - continuous refinement process and estimation guidelines
- [Engineering DRI for Large-Scale Initiatives](engineering_dri) - managing complex workstreams and epics
- [Modular Code Guiding Principle](modular_code) - why and how we write modular code by default
- [Technical Exploration Guidelines](technical_spikes) - guidelines for research and spike work
- [Growth Experimentation Guidelines](experimentation) - guidelines for growth experimentations

## Experimentation

Growth teams contribute to GitLab [experimentation](/handbook/engineering/development/growth/experimentation/) to make it easier to run experiments and make data driven product decisions on GitLab.com.

## Resources

Some useful links to see how and what we are working on include:

- [Growth direction](/handbook/marketing/growth-marketing/)
- [Growth Epic Kanban board](https://gitlab.com/groups/gitlab-org/-/epic_boards/2079888)
- [Growth Issue Kanban board for development](https://gitlab.com/groups/gitlab-org/-/boards/1392106?&label_name%5B%5D=devops%3A%3Agrowth)
- [Experimentation](experimentation/)
- [GLEX](https://gitlab.com/gitlab-org/ruby/gems/gitlab-experiment)
- [Experiment rollout](https://gitlab.com/groups/gitlab-org/-/boards/1352542?label_name[]=experiment-rollout)

### Team Boards

We track our current work on these boards:

- [Driving First Orders epic board](https://gitlab.com/groups/gitlab-org/-/epic_boards/2079888?label_name[]=Growth%3A%20Driving%20First%20Orders&label_name[]=Next%20Up&label_name[]=section%3A%3Agrowth) - Driving First Orders epics that are next up
- [Feature work board](https://gitlab.com/groups/gitlab-org/-/boards/11511990?not[label_name][]=Category%3AEngineering%20Excellence&not[label_name][]=type%3A%3Amaintenance&label_name[]=section%3A%3Agrowth&label_name[]=Growth%3A%20Driving%20First%20Orders&milestone_title=Started) - Driving First Orders feature work in the current milestone
- [Priority bugs board](https://gitlab.com/groups/gitlab-org/-/boards/11512116?milestone_title=Started&label_name[]=section%3A%3Agrowth&label_name[]=type%3A%3Abug) - bugs in the current milestone
- [Tech debt board](https://gitlab.com/groups/gitlab-org/-/boards/11512114?not[label_name][]=Category%3AEngineering%20Excellence&not[label_name][]=Engineering%20Time&label_name[]=section%3A%3Agrowth&label_name[]=type%3A%3Amaintenance&milestone_title=Started) - maintenance work in the current milestone
- [Engineering Excellence board](https://gitlab.com/groups/gitlab-org/-/boards/11512115?milestone_title=Started&label_name[]=section%3A%3Agrowth&label_name[]=Engineering%20Time&label_name[]=Category%3AEngineering%20Excellence) - Engineering Time and Engineering Excellence work in the current milestone

## Team Days

On occasion we hold virtual team days or meetings to take a break and participate in fun, social activities with our Growth counterparts.

- [FY23-Q2 2022](https://gitlab.com/gitlab-org/growth/team-tasks/-/issues/625)
- [December 2021](https://gitlab.com/gitlab-org/growth/team-tasks/-/issues/522)
- [April 2021](https://gitlab.com/gitlab-org/growth/product/-/issues/1675)
- [September 2020](https://gitlab.com/gitlab-org/growth/team-tasks/-/issues/175)
- [May 2020](https://gitlab.com/gitlab-org/growth/team-tasks/-/issues/119)

## Common Links

- [Growth stage](/handbook/engineering/development/growth/)
- [Growth workflow board](https://gitlab.com/groups/gitlab-org/-/boards/4152639)
- `#s_growth` in [Slack](https://gitlab.slack.com/archives/s_growth) (GitLab internal)
- [Growth opportunities](https://gitlab.com/gitlab-org/growth/product/-/issues)
- [Growth meetings and agendas](https://drive.google.com/drive/search?q=type:document%20title:%22Growth%20Weekly%22) (GitLab internal)
- [GitLab values](/handbook/values/)

## CustomersDot Trials Collaboration

For information about trials ownership and collaborating with the Fulfillment/Monetization team on trials work, see our [Trials Ownership and Collaboration Framework](trials-ownership.md). This framework defines the conceptual ownership model — Growth owns trial entry points; Fulfillment/Monetization owns the deeper trial codebase and all CustomersDot support — along with the decision framework and escalation paths for priority conflicts.
