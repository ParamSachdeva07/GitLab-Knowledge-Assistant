---
title: 'Milestones'
description: 'Documentation on milestones'
---

This guide explains how Customer Support Systems uses GitLab milestones to track changes (and work) contained within a deployment period (one month). Milestones group all issues and merge requests for our monthly deployments.

## Understanding milestones

### What are milestones

For Customer Support Systems, milestones are used to group and track changes (and work) involved in a given deployment period. Each milestone represents one month, from the 1st of one month through the 1st of the next month.

## Viewing a list of current milestones

To view a list of Customer Support Systems's milestones, you would go to [this page](https://gitlab.com/groups/gitlab-com/gl-security/corp/-/milestones?sort=due_date_desc&state=all).

You can click on a milestone to review what issues and merge requests are linked to that deployment period.

## Applying a milestone to an item

To apply a milestone to an issue or merge request, you can either click `Edit` next to `Milestone` on the right-side panel of the issue/merge request or you can use the [milestone quick command](https://docs.gitlab.com/user/project/quick_actions/#milestone):

```plaintext
/milestone %"TITLE_OF_MILESTONE"
```

Note: The percentage sign (`%`) is required and you should replace `TITLE_OF_MILESTONE` with the title of the milestone itself. As an example:

```plaintext
/milestone %"CustSuppOps Deployment 2026-02-01"
```

## Removing a milestone from an item

To remove a milestone from an issue or merge request, you can either click `Edit` next to `Milestone` on the right-side panel of the issue/merge request or you can use the [remove_milestone quick command](https://docs.gitlab.com/user/project/quick_actions/#remove_milestone):

```plaintext
/remove_milestone
```

## Milestone setup

All our milestones are made manually in the time leading up to final months of a GitLab fiscal year. Traditionally this is done in the last month of the GitLab fiscal year (January) but can be done sooner if required for future planning efforts.

Each milestone uses the following format:

- Title: `CustSuppOps Deployment YYYY-MM-01`
  - `YYYY-MM-01` is the four digit year and two digit month of the deployment date
- Start Date: This is one month prior to the date in the title
  - Example: If the deployment date is `2025-05-01`, the start date is `2025-04-01`
- Due Date: This is the same as the date in the title
