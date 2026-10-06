---
title: "GitLab Compliance - Hands-On Lab: Repository Control"
description: "This Hands-On Guide demonstrates how to control repository access and modification."
---

> Estimated time to complete: 15 minutes

## Objectives

Learners will implement various repository controls to help manage repository access and modification.

## Task A. Push rules

In this task, you will enable push rules in your repository to ensure that pushes follow a specific set of standards.

1. Navigate to your project.

1. In the left sidebar, select **Settings > Repository** and expand **Push Rules**.

      > For this example, we want to ensure that every commit is targeted towards an issue in the project. Having the issue ID present in the commit message ensures that all activity related to the issue is logged in the issue. To do this, we can enforce an expression to ensure every commit message contains either an epic or an issue ID.

1. In the **Require expression in commit messages**, add the following regular expression:

      ```regex
      ^.*(#\d+|&\d+).*
      ```

      The regular expression will match the string based on the pattern:

      - ^ - Matches the start of the string
      - .* - Matches any character (except newline) zero or more times
      - (#\d+|&\d+) - This is a capturing group that matches either:
          - #\d+ - A hash symbol followed by one or more digits
          - &\d+ - An ampersand symbol followed by one or more digits
      - .* - Matches any character (except newline) zero or more times
      - $ - Matches the end of the string (implicit in this case)

1. Select **Save push rules**.

      > To test this, let's first create a new issue in our project.

1. In the left sidebar, select **Plan > Work items**.

1. Select **New item**.

1. Ensure that the **Type** field is set to **Issue**

1. In the issue title, input `Create compliance frameworks`.

1. Leave all other options as default and select **Create issue**.

      > Now, let's create a commit and see how our push rules impacts our commit messages.

1. In the left sidebar, select **Code > Repository**.

1. Select **+ > New file**.

1. In the **Filename**, input the title `compliance_plan.txt`.

1. Without changing the **Commit message** or **Target Branch**, select **Commit changes**.

      > Notice here that you will get an error stating that the commit message does not follow the proper pattern.

1. In the **Commit message**, input the text `Starting work on issue #1`.

1. Select **Commit changes**.

      > Now, your commit will complete successfully. From here, you can navigate back to your issues to see that the commit is tracked in the issue now.

## Task B. Setting Branch Rules

In this task, you will create a branch rule to prevent direct pushes to main in your repository. If main is a deployment target for your project, it's often ideal to prevent direct pushes to main, since you only want to deploy code that has run through a proper review process.

1. Navigate to your project.

1. In the left sidebar, select **Settings > Repository**.

1. Expand the **Branch rules** section.

1. Select **View Details** next to **main**.

1. Select **Edit** in **Allowed to push and merge**.

1. Check the `No one` option, then select **Save changes**.

      > With this change, now no one can directly push to main. Only merges into main are allowed. To test this:

1. In the left sidebar, select **Code > Repository**.

1. Select **+ > New file**.

1. Add any **Filename** and add any content into the file body.

1. Select **Commit changes**.

      > Note that you now don't have the option of pushing onto the main branch.

1. Change the **Target Branch** field (which will currently have a generated branch name in) to `main` and select **Commit changes**.

      > You will see an error stating that you are not allowed to push into this branch.

1. *Optionally* add a different branch name and commit your new code.

## Task C. Cleaning Up Rules

Before proceeding to the next set of labs, it's recommended to remove the commit message rules in your repository, as well as the rule that prevents pushing on the main branch. This will prevent any issues of preventing commits due to violations.

1. In the left sidebar, select **Settings > Repository**.

1. Expand the **Push rules** section.

1. Remove the content in **Require expression in commit message**.

1. Select **Save push rules**.

1. Expand the **Branch rules** section.

1. Click on the **View Details** option to the right of the main branch.

1. Click on the **Edit** option to the right of the 'Allowed to push and merge' section.

1. Change the setting from **No one** to **Developers and Maintainers**.

1. Click the **Save changes** button.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabcompliancehandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
