---
title: "GitLab Fundamentals - Hands-On Lab: Handling Analytics"
description: "This Hands-On Guide walks you through the process of handling analytics in GitLab."
---

> Estimated time to complete: 20 minutes

## Objectives

The goal of this lab is to get an overview of the different analytics available to you in GitLab, and how to create your own Value Stream Analytics Board.

## Task A. Viewing your analytics

1. To start, navigate to your `Cool App QA` project.

1. In the left sidebar, select **Analyze > Analytics Dashboard**.

1. Select **Value Streams Dashboard**.

      In this report, you will see a variety of analytic details about your current project. Some details you may see populated here after the previous labs are: Merge request throughput, and Median time to merge.

1. In the left sidebar, select **Analyze > CI/CD Analytics**.

      In this report, you will see details about your CI/CD pipelines. Here you can see how many pipelines have run in your project, the duration of the pipelines, and failure rates of pipelines.

1. Feel free to explore the other Analytics board as much as you like to see the different systems you can analyze. Once you are finished, you may move onto the next task.

## Task B. Creating a Value Stream Analytics Dashboard

In this report, you will see a variety of analytic details about your current project. This dashboard is highly customizable.

1. Select **Analyze > Value Stream Analytics**.

1. Select **New Value Stream**.

1. For the **Value Stream name**, write in `Issue Tracker Stream`.

1. There are two options to choose from, creating from a default template and creating from no template. Select **Create from no template**.

1. For Stage 1, type in `Unassigned Issues` for the stage name, and select **Issue created** as our start event. This will mark when a issue will first be tracked in this stage.

1. For the end event, select `Issue first assigned` as our end event. This will create our first Stage to track work in our project.

1. Select **Add a stage**. In the second stage, type in `Backlog` for the stage name, and select **Issue first assigned** as our start event.

1. For the end event, select **Issue First Associated with a Milestone** as our end event. This will create our second Stage to track work in our project.

1. Select **Add a stage**. In the third stage, type in `In Progress` for the stage name, and select **Issue First Associated with a Milestone** as our start event.

1. For the end event, select **Issue closed** as our end event. This will create our final Stage to track work in our project.

1. Select **New Value Stream**. You will be taken to a page where you can see your Value stream analytics in action. If you do not see any data in your stream, check the `Last updated X minutes ago` note in the top right section. It should be noted that existing value streams update roughly every ten minutes. Since this is a new value stream, it may be a bit longer than that until the first refresh.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabfundamentalshandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
