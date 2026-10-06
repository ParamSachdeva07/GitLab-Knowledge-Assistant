---
title: "Geo and Disaster Recovery"
description: "Information about the Geo Team"
---

## The Geo Team

[Geo](https://docs.gitlab.com/ee/administration/geo/index.html) is a [Premium](https://about.gitlab.com/pricing/premium/) feature, built to help speed up the development of distributed teams by providing
one or more read-only mirrors of a primary GitLab instance. This mirror (a Geo secondary node) reduces the time to clone or fetch large
repositories and projects, or can be part of a Disaster Recovery solution.

### Team members

{{< team-by-manager-slug manager="thiagofigueiro" department="Geo Team" >}}

### Stable counterparts

{{< engineering/stable-counterparts role="Geo" manager="thiagofigueiro" >}}

## Goals and Priorities

Our priorities are aligned with the product direction. Current and upcoming work is visible in the [open `group::geo` epics](https://gitlab.com/groups/gitlab-org/-/epics/?state=opened&label_name%5B%5D=group%3A%3Ageo).

Alongside these priorities, we need to constantly assess issues that our customers bring to our
attention. These could take the form of bug reports or feature requests. Geo users are often our largest
customers and some rely on Geo as a critical part of their workflow.

We also work constantly to keep housekeeping chores to a manageable level. Where possible, we address these issues
as part of a related project. Where this is not possible, we use time around our projects to make this happen.

## Geo's Relationship to Disaster Recovery

Disaster Recovery (DR) is a set of policies, tools and procedures put in place to be able to recover from a disaster.

Geo provides data redundancy. The customer will have a redundant copy of data in a separate location. If anything were to happen to their primary instance, a secondary instance still retains a copy of the data.

However, data redundancy is only one part of a complete DR strategy.

High Availability (HA) is also a step towards Disaster Recovery. At the moment Geo does not provide true HA because if the primary instance is not available, certain actions are not possible.

## How to ask for support from Geo

The first line of support will always be the support engineer assigned to the issue raised by the customer. However, at times more expertise is required to resolve the customer concern and a Geo engineer needs to be involved.
This section outlines the process and expectations when requesting support from the team for Geo-related customer support issues.

### Before requesting support

Before submitting a request for support, please review Geo's [documentation](https://docs.gitlab.com/ee/administration/geo/), the [Disaster Recovery](https://docs.gitlab.com/ee/administration/geo/disaster_recovery/) docs, the [Backup and Restore](https://docs.gitlab.com/ee/administration/backup_restore/) docs, the Geo Handbook pages, or search through previous [support requests](https://gitlab.com/gitlab-com/request-for-help/-/issues/?sort=created_date&state=all&label_name%5B%5D=Help%20group%3A%3AGeo&first_page_size=100). The answer to your questions might be found there. **Please reach out in the Geo Support Pod Channel `#spt_pod_geo` first before submitting a RFH.**

### Asking a general question

If you have a general question for which you can't find your answer, then feel free to ask your question in the [#g_geo](https://gitlab.slack.com/archives/C32LCGC1H) channel on Slack. Please keep in mind that engineers will do their best to support you and answer your question from the top of their heads. If they need to do more research and/or address more complicated scenarios, you will need to create a support issue (see next section).

### Create a support request issue

We like to use issues when customers need help from the Geo Team. This helps us to prioritize work and make sure that we don't lose history and maintain context when the Slack retention policy activates.
We ask requestors to create an issue in the [Request for Help Project](https://gitlab.com/gitlab-com/request-for-help).

Please make sure to use and fill the [Geo support request issue template](https://gitlab.com/gitlab-com/request-for-help/-/blob/main/.gitlab/issue_templates/SupportRequestTemplate-Geo.md) for Geo related questions and [Backup and Restore support request issue template](https://gitlab.com/gitlab-com/request-for-help/-/blob/main/.gitlab/issue_templates/SupportRequestTemplate-BackupAndRestore.md). As the requestor you **only** need to fill the Customer Info and Support Question sections.

## Common Links

### Documentation

- [Geo](https://docs.gitlab.com/ee/administration/geo/index.html)
- [Disaster Recovery](https://docs.gitlab.com/ee/administration/geo/disaster_recovery/index.html)
- [Planned Failover](https://docs.gitlab.com/ee/administration/geo/disaster_recovery/planned_failover.html)
- [Background Verification](https://docs.gitlab.com/ee/administration/geo/disaster_recovery/background_verification.html)
- [Geo Glossary](https://docs.gitlab.com/ee/administration/geo/glossary.html)

### Issue Lists

#### Missing type labels

The following links lead to Geo team lists of issues to help with identifying missing subtype labels. After opening each link, select the desired milestone filter.

- [Issues missing the type label](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_asc&state=all&amp;not%5Blabel_name%5D%5B%5D=type%3A%3A%2a&label_name%5B%5D=group%3A%3Ageo&milestone_title=15.6&first_page_size=20)
- [Features issues missing subtype label](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_asc&state=all&label_name%5B%5D=type%3A%3Afeature&label_name%5B%5D=group%3A%3Ageo&milestone_title=15.6&amp;not%5Blabel_name%5D%5B%5D=feature%3A%3A%2a&first_page_size=20)
- [Maintenance issues missing subtype label](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_asc&state=all&label_name%5B%5D=type%3A%3Amaintenance&label_name%5B%5D=group%3A%3Ageo&milestone_title=15.6&amp;not%5Blabel_name%5D%5B%5D=maintenance%3A%3A%2a&first_page_size=20)
- [Bug issues missing subtype label](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_asc&state=all&label_name%5B%5D=type%3A%3Abug&label_name%5B%5D=group%3A%3Ageo&milestone_title=15.6&amp;not%5Blabel_name%5D%5B%5D=bug%3A%3A%2a&first_page_size=20)

### Other Resources

- Issues relating to Geo are mostly to be found on the
[gitlab-ee issue tracker](https://gitlab.com/gitlab-org/gitlab-ee/issues/?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=Geo)
- [Chat channel](https://gitlab.slack.com/archives/g_geo); please use the `#g_geo`
chat channel for questions that don't seem appropriate to use the issue tracker
for.
- [Geo YouTube Playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0KoY_6FXXVgj7wPE9ZDS4cOw)
- [Geo on staging.gitlab.com](staging.html)

## Planning and Process

Our planning and build process is recorded on the [process page](process.html).

## Demos

The demos are recorded and should be stored in Google Drive under "GitLab Recorded Videos --> Geo Demos".
If you recorded the demo, please make sure the recording ends up in that folder.

## Geo Terminology

See the [Geo Glossary](https://docs.gitlab.com/ee/administration/geo/glossary.html).
