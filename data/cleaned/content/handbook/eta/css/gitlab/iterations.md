---
title: 'Iterations'
description: 'Documentation on iterations'
---

This guide explains how Customer Support Systems uses GitLab iterations to organize and track work in one-week time periods. Iterations help the team manage workload, maintain focus on current priorities, and provide visibility into weekly progress.

## Understanding iterations

### What are iterations

For Customer Support Systems, iterations are one-week time periods used to group and track issues being actively worked on. Each iteration runs from Sunday to Saturday, helping the team focus on current priorities and providing visibility into weekly workload and progress.

Technically, an iteration is GitLab's time-boxed workflow feature that groups issues for a specific period. While iterations can be configured for various durations (typically 1-3 weeks), Customer Support Systems uses consistent one-week intervals aligned with our weekly workflow rhythm.

### How Customer Support Systems uses iterations

We use iterations to organize our weekly workflow and provide visibility into what work is in progress. Iterations help us:

- **Track weekly workload**: See what issues are being worked on this week
- **Maintain focus**: Group related work into manageable time periods  
- **Plan capacity**: Understand team bandwidth and commitments
- **Measure progress**: Review what was completed each week
- **Enable rollover**: Issues that aren't completed automatically move to the next iteration, preventing work from being lost or forgotten

Team members assign iterations to issues during triage or when they begin working on them. This creates a clear view of current priorities and helps prevent work from falling through the cracks.

### Automatic issue rollover

If an issue is not closed before an iteration ends (Saturday at 11:59 PM), GitLab automatically moves it to the next week's iteration on Sunday when the new iteration begins. This ensures work in progress continues to be tracked and doesn't disappear from the team's view.

You can prevent automatic rollover for specific issues by removing the iteration before the period ends (if the work is being postponed rather than continued).

## Viewing a list of current iterations

To view a list of Customer Support Systems's current iterations, you would go to [this page](https://gitlab.com/groups/gitlab-com/gl-security/corp/cust-support-ops/-/cadences/?createdCadenceId=2062775).

You can click on the iteration time periods shown to review what issues are linked to that time period.

## Applying an iteration to an issue

To apply an iteration to an issue, you can either click `Edit` next to `Iteration` on the right-side panel of an issue or you can use the [iteration quick command](https://docs.gitlab.com/user/project/quick_actions/#iteration).

If you want to use the [iteration quick command](https://docs.gitlab.com/user/project/quick_actions/#iteration) to apply the current iteration, the specific text to use is:

```plaintext
/iteration [cadence:"Customer Support Operations"] --current
```

Note: The square brackets are part of the command syntax

## Removing an iteration from an issue

To remove an iteration from an issue, you can either click `Edit` next to `Iteration` on the right-side panel of an issue or you can use the [remove_iteration quick command](https://docs.gitlab.com/user/project/quick_actions/#remove_iteration):

```plaintext
/remove_iteration
```

## Iteration setup

For reference, Customer Support Systems iterations use these settings:

- Title: `Customer Support Operations`
- Description: `Weekly iteration for Customer Support Operations`
- Automatic scheduling
  - [x] Enable automatic scheduling
  - Automatic start date: `2025-04-06` (this is the date we setup the iterations)
  - Duration: 1 (meaning an iteration lasts 1 week)
  - Upcoming iterations: 10 (meaning have the current + 9 future iterations available)
  - Roll over issues
    - [x] Enable roll over
