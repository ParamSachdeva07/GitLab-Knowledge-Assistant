---
title: "GitLab Agile Portfolio Management- Hands-On Lab: Task Management & Progress Tracking"
description: "This Hands-On Guide walks you through creating issues and labels in GitLab."
---

> Estimated time to complete: 45 minutes

## Objectives

Issues are a core building block in GitLab that enable collaboration, discussions, planning and tracking of work. Issues are defined in the scope of a **Project**, **not** a Group. You can read more about them in the [documentation](https://docs.gitlab.com/ee/user/project/issues/).

## Task A. Create and manage labels

> You can use labels to categorize epics, issues, and merge requests using colors and descriptive titles like bug, feature request, or docs. This allows you to dynamically filter and manage epics, issues, and merge requests. You can read more about them in the [documentation](https://docs.gitlab.com/ee/user/project/labels.html).

1. Navigate to your **Awesome Inc** group.

1. In the left pane, click **Manage > Labels**.

1. Click the **New label** button.

1. In the **Title** field, enter `Status::Open`. The 2 colons in the label title mean that this will be a [scoped label](https://docs.gitlab.com/ee/user/project/labels.html#scoped-labels).

    > A scoped label uses a double-colon (::) syntax in its title, for example: `workflow::in review`. An issue, merge request, or epic cannot have two scoped labels, of the form `key::value`, with the same key. If you add a new label with the same key but a different value, the previous key label is replaced with the new label.

1. In the **Description** field, type `Item that is ready to begin work` .

1. For the label's color, GitLab supports any hex color code. For this label, choose **Blue-gray** from the suggested color palette (or type `#6699cc` in the **Background color** field).

1. Click **Create label**.

1. Create the following additional labels, setting a description and background color of your choosing. Note that some of these are scoped and some are unscoped.
      - `Status::WIP`
      - `Status::Done`
      - `Priority::High`
      - `Priority::Medium`
      - `Priority::Low`
      - `Dev`
      - `QA`
      - `Security`

1. Go to your **Family Budget Calculator** project. The project is inside the **Awesome Inc > Software > Core** group hierarchy.

1. Click **Manage > Labels** from the left sidebar.

1. Click the star icon to the left of the **Subscribe** button to designate the following labels as prioritized labels. Prioritized labels appear at the top of your labels list.

      - **Priority::High**
      - **Priority::Medium**
      - **Priority::Low**

## Task B. Create issues for tracking work

1. In your **Family Budget Calculator** project, click **Plan > Work items** from the left sidebar.

1. Click the **New item** button.

1. Ensure that the **Type** field is set to **Issue**.

1. In the title section, type `Third-party financial services integration`.

1. The description is an optional section, but feel free to type in your own description for this issue.

1. Using the **Assignees** dropdown list, assign the issue to yourself by clicking on the dropdown list, and then clicking on your username. While we will leave the options as they are for now, it is important to understand what they do:

      - **Parent:** Associates the issue with an epic.

      - **Milestone:** Milestones in GitLab are a way to track issues and merge requests created to achieve a broader goal in a certain period of time.

      - **Labels:** Apply labels to your issue, which are metadata tags that can be used to sort and filter your issues.

      - **Weight:** Apply a weight value to your issue to measure the time, complexity, or value a given issue has or costs.

      - **Dates:** Use in issues to keep track of deadlines and make sure features are shipped on time.

      - **Iteration:** Associate the issue with an iteration to track it over a period of time. This allows teams to track velocity and volatility metrics.

1. Click the **Create issue** button.

1. Open the issue you just created by clicking on its name.

1. In the issue metadata pane, click **Edit** next to the **Labels** field.

1. Select the **Status::Open** label, then click away from the metadata pane to apply the label to the issue.

1. Repeat the previous 2 steps to apply the **Priority::Medium** and **Dev** labels to the issue.

1. In the left pane, click **Plan > Work items**. You will see the issue you just created in the list along with its labels.

1. Create a second issue by clicking **New item** in the top right of the issue list page.

1. In the **Title** section, type `Backend services`.

1. Paste the following in the **Description** section:

      ```markdown
      - Create DB
      - Create service infrastructure
      - Write documentation
      ```

1. Using the **Assignees** dropdown list, assign the issue to yourself by selecting `Edit` and then clicking on your username.

1. Click the **Create issue** button.

1. Apply the following labels to the **Backend services** issue by clicking on the label, then click away from the metadata pane to apply the label to the issue: **Dev**, **Status::Open**, and **Priority::High**.

1. In the left pane, click **Plan > Work items** to see both issues with their labels.

1. Create a third issue by clicking **New item** in the top right of the issue list page.

1. In the **Title** section, type `Frontend services`.

1. Paste the following in the **Description** section:

      ```markdown
      - UX design
      - Integration
      - Write documentation
      ```

1. Using the **Assignees** dropdown list, assign the issue to yourself by selecting `Edit` and then clicking on your username.

1. Click **Create issue**.

1. Apply the following labels to the **Frontend services** by clicking on the label, then click away from the metadata pane to apply the label to the issue: **Dev**, **Status::WIP**, and **Priority::High**.

1. In the left pane, click **Plan > Work items** to see all 3 issues with their labels.

## Task C. Create a View based on your labels

> Now that you have some labels in place, we can start to use these to create your own personalised work item views. These can be used to easily see which work items match certain conditions, allowing you to make views which show work items assigned to you, or that have certain labels, or any of the other filtering capabilities.

1. Navigate to **Plan > Work items**.

1. Click into the filter bar (which should currently be filtered to "State is Open"). From the dropdown list, select **Label**, then select **is**, then select the **Priority::High** label.

1. Filter your workitem list to this label by pressing the filter button (the magnifying glass icon on the right-hand side of the filter bar).

    > This will filter down to just your high priority issues.

1. To turn this into a View, click the **+ Add View** button to the right of the **All Items** header above the filter bar, and select **New View**

1. Title the view with `High Priority Issues`, and add any description you would like.

1. Click **Create View**.

1. Notice that there is now a tab next to the **All items** tab titled `High Priority Issues`, which will maintain the filter that you selected.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabpmhandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
