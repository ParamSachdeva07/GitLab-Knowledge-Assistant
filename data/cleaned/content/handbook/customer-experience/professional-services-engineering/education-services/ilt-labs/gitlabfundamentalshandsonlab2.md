---
title: "GitLab Fundamentals - Hands-On Lab: Project Management with Epics and Issue Boards"
description: "This Hands-On Guide walks you through the process of working with epics and Issue Boards in GitLab."
---

> Estimated time to complete: 15 minutes

## Objectives

The goal of this lab is to get an overview of the different plan features available in GitLab, including epics and issue boards.

## Task A. Defining an epic

An epic is created at a group level and defines larger sets of work on a project. To create an epic:

1. Navigate to your **QA** group.

1. In the left sidebar, select **Plan > Work Items**.

1. Select **New item**.

1. Ensure that the **Type** field is set to **Epic**.

1. For the title, enter `My first epic`.

1. Enter any description you like and select **Create epic**.

1. Select `My first epic`.

In this view, you will see details on your epic. Similar to issues, epics can contain child items and linked items, as well as activity related to the epic. In the right sidebar, there is metadata for the epic, including labels, health status, parent, and time tracking.

## Task B. Defining a milestone

A milestone represents a set of work being completed over a fixed time period. A milestone can contain both epics and issues. To create a milestone:

1. Navigate to your `QA` group.

1. In the left sidebar, select **Plan > Milestones**.

1. Select **New milestone**.

1. In the title, enter `My first milestone`.

1. Enter any **Start Date** and **Due Date** you would like.

1. Input any **Description**, then select **Create milestone**.

      Next, we need to assign issues to the milestone.

1. In the left sidebar, select **Plan > Work items**.

1. Select `First issue`.

1. In the right sidebar, select **Edit** next to **Milestone**.

1. Select `My first milestone` from the resulting dropdown list.

1. Select `My first milestone` in the right sidebar to be redirected back to the milestone.

You will now see all issues related to the milestone, along with burndown and burnup charts for the milestone dates provided.

## Task C. Issue boards

To help with viewing issues and epics in a singular place, you can utilize issue and epic boards. To start:

1. Navigate to the `QA` group.

1. In the left sidebar, select **Plan > Issue boards**.

      > In this view, you will see all your issues associated with their statuses.

1. We are going to create a new list to store our issues that are associated with us. Click the **New List** button on the right.

1. Select **Assignee**, then select your username.

1. Select **Add to board**.

1. You should see your issue you created before in the 'Open' list. Click and drag the issue from the 'Open' list to the list with your username.

1. Click on the issue. You should see that you have been automatically assigned to the issue.

It is possible to further customize issue boards to display different sets of information depending on your requirements. For more details on issue boards, check out the [documentation](https://docs.gitlab.com/ee/user/project/issue_board.html).

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabfundamentalshandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
