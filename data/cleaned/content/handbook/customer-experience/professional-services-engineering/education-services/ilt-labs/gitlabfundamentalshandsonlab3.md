---
title: "GitLab Fundamentals - Hands-On Lab: Repository Management and Branching"
description: "This Hands-On Guide walks you through managing code repositories in GitLab."
---

> Estimated time to complete: 15 minutes

## Objectives

In this lab, we will explore how we can create repositories to organize code, as well as configure the repositories to meet various use cases.

## Task A. Configuring your project

In the left sidebar, you will see a few new options available when you are in your project.

1. Navigate to your **Cool App QA** project.

1. In the left sidebar, select **Settings**. From the resulting dropdown list, select **General**.

1. Review the different settings available in general. Here you can toggle your project visibility, features enabled, as well as advanced options like moving and deleting projects.

1. In the left sidebar, under **Settings**, select **Repository**. This section contains configurations for your project code repository.

      > In most settings, you will want to toggle a few settings for your repository. First, you will want to ensure your project has a consistent default branch. This branch will be the branch that merge requests are made against in your project. For this main branch, you will want to ensure it is protected and not able to be pushed directly to. Let's look at how to configure these options.

1. In **Repository Settings**, select **Branch defaults** to expand this section.

      > Here, you will see that `main` is your default branch.

1. Next, select **Branch rules**.

1. Beside the `main` rules, select **View details**.

1. Explore the settings available here. You will see that by default, `Allow force push` is disabled for the main branch. You will also see that users with a `Maintainer` role can push and merge to `main`. This means the individual can make a commit onto the main branch without using a merge request. Ideally, we want to prevent anyone from pushing into `main` directly.

1. To prevent pushes to main, select **Edit** in the **Allowed to push and merge** section.

1. Check the **No one** checkbox. Select **Save changes**.

With this setting changed, now no one can directly push to `main`. Let's test this out to see the result.

## Task B. Testing pushes to main

1. In the left sidebar, select **Code > Repository**.

1. At the top of the repository section, select **+ > New file**.

1. In the **Filename**, enter `test.txt`.

1. Enter any text into the file contents.

1. Select **Commit changes**.

1. In the **New branch** section, notice that there is a note stating "You don't have permission to commit to `main`". This is a direct result of our branch rules. To accommodate the change, this window has automatically created a new branch for us to use.

1. In **New branch**, change the name to `test-commit`.

1. Uncheck **Create a merge request for this change**.

1. Select **Commit changes**.

After committing the changes, you will now see the file available. This created a new branch in your project. To return to your main branch, select the dropdown list that currently says **test-commit**. From this dropdown list, select **main** to see your main branch again.

Now that we have a change in a branch, we can explore the concept of merge requests to merge the changes into main in the next lab.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabfundamentalshandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
