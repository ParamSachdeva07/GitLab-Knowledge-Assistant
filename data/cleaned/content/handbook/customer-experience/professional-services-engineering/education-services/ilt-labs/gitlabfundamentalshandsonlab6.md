---
title: "GitLab Fundamentals - Hands-On Lab: Implementing Security Scanners"
description: "This Hands-On Guide walks you through the process of adding security scanners to your CI/CD process."
---

> Estimated time to complete: 30 minutes

## Objectives

This lab uses SAST, an optional feature in CI/CD pipelines, to identify security vulnerabilities in your code. GitLab's Vulnerability Report then shows any old or new vulnerabilities found with each pipeline run. You can learn more in the [documentation](https://docs.gitlab.com/ee/user/application_security/sast/).

## Task A. Finding the SAST Component

GitLab provides a variety of CI/CD components, which are prebuilt CI/CD configurations you can include in your projects. To view all of the available components on your GitLab instance:

1. In the left sidebar, select **Search or go to**.

1. In the resulting dialog, select **Explore**.

1. In the left sidebar, select **CI/CD Catalog**. This will show you a list of all of the CI/CD catalog items available in your GitLab instance. For this lab, you will be adding SAST to your project. Select the SAST component.

When you select a CI/CD component, you will see a `Readme`, which describes how to use the component, as well as configuration options for the component. For the SAST component, you will see that it can be included using the following code:

```yaml
include:
  - component: $CI_SERVER_FQDN/components/sast/sast@1.1.0
```

Let's add this to our CI/CD file.

## Task B. Adding the SAST component

1. Navigate to your CI/CD project by clicking on the Tanuki logo in the top left corner of the page, then click on your `Cool App QA` project.

1. In the left sidebar, select **Code > Branches**.

1. Select the `initial-code` branch.

1. Select **Build > Pipeline Editor**.

1. At the top of your file, add the SAST import at the current version.

      ```yaml
      include:
        - component: $CI_SERVER_FQDN/components/sast/sast@1.1.0
      ```

1. In the stages section of the file, add a stage named `test`, as shown below:

      ```yaml
      stages:
        - build
        - test
      ```

      After making these changes, your file will look like this:

      ```yaml
      include:
        - component: $CI_SERVER_FQDN/components/sast/sast@1.1.0

      stages:
        - build
        - test

      build go:
        image: golang
        stage: build
        script:
          - go build
          - ./array
      ```

1. Ensure that your **Branch** is set to `initial-code`. Select **Commit changes**.

1. After committing your changes, in the left sidebar, navigate to the **Build > Pipelines**.

1. Select the most recent pipeline.

1. You will now see a new job named *semgrep-sast*. This job is the security scan imported using the `include` keyword.

## Task C. Add `run.py` and review SAST scanning results

In this task, you'll add a file with known vulnerabilities and see if SAST detects it.

1. Return to the **Project overview** page by clicking on the name of your project in the breadcrumbs section.

1. Switch to your initial-code branch using the branch dropdown list.

1. At the top of the project landing page, to the right of the branch dropdown list, click **(+) > This directory > New file**.

1. For the **File name** field, type in `run.py`.

1. Copy the content below into the file:

      ```python
      import subprocess

      in = input("Enter your server ip: ")
      subprocess.run(["ping", in])

      print("Attempting to connect to the server")
      print("Application authentication was successful")
      ```

1. Select **Commit changes**, add an appropriate **Commit message** and click the **Commit changes** button. Merge the code on the `initial-code` branch.

1. In the left-hand navigation pane, click **Build > Pipelines**.

1. At the top of the row of the table of pipelines, click on the **running** (if it is still running) or **passed** (if the pipeline has been completed) status labels.

    > The SAST scan may take a few moments, so feel free to grab a cup of coffee while you wait.

1. Once the SAST scan has completed, refresh the page and click on the new tab in the pipeline details page called **Security**.

1. Click on the vulnerability listed and read about a potential security problem detected by SAST scanning in `run.py`.

1. Feel free to edit the code to fix the issue raised (such as removing the `subprocess.run` command), and commit the changes. Does the vulnerability report still note the issue as present?

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabfundamentalshandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
