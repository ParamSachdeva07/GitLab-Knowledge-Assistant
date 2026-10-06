---
title: "GitLab Compliance - Hands-On Lab: Pipeline Execution Policies"
description: "This Hands-On Guide walks you through enabling and using Pipeline Execution Policies in your projects."
---

> Estimated time to complete: 15 minutes

## Objectives

To ensure that your CI/CD jobs run in a consistent and compliant way, you can enforce job configurations through pipeline execution policies. In this lab, you will practice enabling and configuring pipeline execution policies in your project.

## Task A. Creating a standard pipeline

To start, we will create a standard pipeline to use in our compliance projects.

1. Navigate back to your ILT group.

1. Select **New project**.

1. Select **Create blank project**.

1. In the project name, enter `CICD Template`.

1. Leave all other options as default and select **Create project**.

1. Select **+ > New file**.

1. In the **Filename**, input `.gitlab-ci.yml`.

1. In the file, add the following contents:

      ```yml
      stages:
          - test

      include:
          component: ilt.gitlabtraining.cloud/components/sast/sast@main

      semgrep-sast:
          rules:
              - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
      ```

1. Commit these changes to the main branch of the project.

This CI/CD configuration contains a SAST scanner. By adding this in a pipeline execution policy, we can ensure that our project always runs a SAST scan. Let's see how to configure this for our project.

## Task B. Adding a Pipeline Execution Policy

1. Return to your `Compliance project`.

1. In the left sidebar, select **Secure > Policies**.

1. Select **New policy**.

1. Under **Pipeline execution policy**, select **Select policy**.

1. Set the **Name** to `Enforce Security`.

1. Under **Actions**, select **Inject** from the **CICD Template** project.

1. Point the file path to your `.gitlab-ci.yml` file.

1. Leave all options as default and select **Configure with merge request**.

1. Select **Merge**.

1. Return to the `Compliance project` project.

      > To test these changes, let's create a change in the project.

1. In the left sidebar, select **Code > Repository**.

1. Select **+ > New file**.

1. In the **Filename**, input `test.py`. In the contents, add the following code:

      ```python
      import hashlib as h

      h.md5('1')
      ```

1. Select **Commit changes**.

1. For the commit message, add something similar to "Added some python code for security scanning to test".

1. Change the **Branch** selection to **Commit to a new branch** and title the new branch **add-code-for-sast**.

1. Ensure **Create a merge request for this change** is selected and click **Commit changes**.

1. Leave all options as default in the Merge Request and click **Create merge request**.

1. Review the branch pipeline created. Notice that it has a `semgrep-sast` job even though it's not defined in `Compliance Project`. This job comes from our pipeline execution policy. Note that we were able to *add* a job into the pipeline because we used the 'inject' keyword when setting up our policy. If we instead used the 'override' keyword, it would run this job *instead of* the jobs in your pipeline.

1. Return to your merge request. You will see that there is one new vulnerability, detected by the SAST scanner.

1. Select **Merge** to complete your merge request.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabcompliancehandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
