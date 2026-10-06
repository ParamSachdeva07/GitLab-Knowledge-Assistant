---
title: "GitLab CI/CD - Hands-On Lab: Rules and Merging Changes"
description: "This Hands-On Guide demonstrates how to configure rules and Merge Request pipelines"
---

> Estimated time to complete: 15 minutes

## Preface

After successfully implementing automated builds, your team at Tanuki Enterprises discovered a new problem. Every code commit triggers the entire pipeline—including the release job that creates production releases. This means:

- **Premature Releases**: Experimental features in development branches accidentally trigger production releases
- **Wasted Resources**: Build and test jobs run on every tiny commit, even on work-in-progress code
- **No Quality Gates**: Code merges directly to main without running through proper validation in Merge Requests
- **Pipeline Chaos**: Infinite loops occur when release jobs create tags that trigger more pipelines
- **Lost Context**: Developers can't easily see which pipeline runs are associated with their Merge Requests

## Objectives

In this lab, you'll implement workflow rules and Merge Request pipelines to control when and how your CI/CD pipeline executes. You'll learn to differentiate between development workflows and production releases, ensuring that the right jobs run at the right time based on the context of your code changes.

## Task A. Workflow Rules

With our build process complete, we can now start making changes to our code. Most changes will take place in a Merge Request. When changes are made to code in a Merge Request, it is ideal to run a pipeline against the Merge Request. This will ensure that all code changes are production ready, making it easier to merge changes into production. Let's take a look at a few ways to set up and configure a pipeline.

Workflow rules allow you to control when a pipeline runs. These rules give you control over the execution flow of your entire CI/CD pipeline. For example, consider our current `.gitlab-ci.yml` file:

```yml
default:
  image: golang

stages:
  - build
  - run

build go:
  stage: build
  script:
    - go build
  artifacts:
    paths:
      - array

run go:
  stage: run
  script:
    - ./array
```

Let's introduce a new job that adds a release based on the current project code.

1. GitLab tracks releases of your project in the **Deploy > Releases** section. To create a new release, select **Build > Pipeline Editor**.

1. In the pipeline editor, add the `release` job to your `stages`:

      ```yml
      stages:
        - build
        - run
        - release
      ```

1. Add a new job in the release stage below the `run go` job:

      ```yml
      release go:
        stage: release
        script:
          - echo "Generating the latest Tanuki App release!"
      ```

1. The release job requires a special CLI tool. Add the image that contains the required tool to your release job as per the code below:

      ```yml
      release go:
        stage: release
        image: registry.gitlab.com/gitlab-org/release-cli:latest
        script:
          - echo "Generating the latest Tanuki App release!"
      ```

1. To create a release, you need to provide a `tag_name` and a `description` for the release. To produce a unique version number, we will use the `CI_PIPELINE_IID` built in variable. This variable contains a project level ID of the current pipeline. Add the release keyword below the `script` of your `release job` job:

      ```yml
        image: registry.gitlab.com/gitlab-org/release-cli:latest
        script:
          - echo "Generating the latest Tanuki App release!"
        release:
          tag_name: 'v0.$CI_PIPELINE_IID'
          description: 'The latest release!'
      ```

      The job should now look like this:

      ```yml
      release go:
        stage: release
        image: registry.gitlab.com/gitlab-org/release-cli:latest
        script:
          - echo "Generating the latest Tanuki App release!"
        release:
          tag_name: 'v0.$CI_PIPELINE_IID'
          description: 'The latest release!'
      ```

    When the release job runs, it will create a tag in your repository. The creation of a tag by default will trigger a pipeline to run. This creates an infinite loop, where each time the pipeline finishes, it creates a new tag, which then triggers a new pipeline.

    To prevent the infinite loop, we can utilize a workflow to prevent a pipeline from triggering when a new commit tag is added.

1. Define the following workflow at the top of your `.gitlab-ci.yml` file:

      ```yml
      workflow:
        rules:
          - if: $CI_COMMIT_TAG
            when: never
          - when: always
      ```

1. Select **Commit changes**.

      This rule applies to the whole pipeline. If a `CI_COMMIT_TAG` is present, the if statement evaluates to true, resulting in the pipeline never running. If the `CI_COMMIT_TAG` is not present, then the pipeline will run.

      > You can also search for specific `CI_COMMIT_TAG` values if you want to only stop the run for releases. In this case, a tag in the form `v0.*` is a part of our release, so we can search for this specific pattern instead.

## Task B. Merge Request Pipelines

Another consideration we have for our new release job is when the job to create a release runs. Currently, this job will run on every commit. However, we ideally only want it to run in commits to the main or default branch. To achieve this, we can implement a Merge Request pipeline.

A Merge Request pipeline will run every time you make a change to a branch with an open Merge Request. By controlling the flow for Merge Requests, we can prevent releases from running until they are fully merged.

To define a job that runs in a Merge Request, we will add a rules definition to the job. The rule we add will check the `CI_PIPELINE_SOURCE` to see if it is merge_request_event.

1. Open your `.gitlab-ci.yml` file in the pipeline editor by selecting **Build > Pipeline Editor**.

1. Below the `script` for your `build go` and `run go` jobs, add the following rule:

      ```yml
        rules:
          - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
      ```

      > Make sure that this rule is indented by two spaces. It should be aligned with the `script` keyword.

      The build and run jobs should now look like this:

      ```yml
      build go:
        stage: build
        script:
          - go build
        artifacts:
          paths:
            - array
        rules:
          - if: $CI_PIPELINE_SOURCE == 'merge_request_event'

      run go:
        stage: run
        script:
          - ./array
        rules:
          - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
      ```

      > Now, the build and run jobs will only run when the pipeline is part of a Merge Request.

1. Next, we can prevent the release job from running in Merge Requests by negating the rule. Below the `release job` script, add the following rule:

      ```yml
        rules:
          - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
      ```

      > Make sure this is indented to the same level as the `script` keyword, 2 spaces.

      The release job should now look like this:

      ```yml
      release go:
        stage: release
        image: registry.gitlab.com/gitlab-org/release-cli:latest
        script:
          - echo "Generating the latest Tanuki App release!"
        release:
          tag_name: 'v0.$CI_PIPELINE_IID'
          description: 'The latest release!'
        rules:
          - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
      ```

1. With these changes made, select **Commit changes** to update your `.gitlab-ci.yml` file.

1. When you commit this to main, select **Build > Pipelines** to view your running jobs. You will notice that only the release job runs, because the commit was run on `main`.

      Let's get the other jobs to run by creating a Merge Request.

1. Navigate to **Code > Branches**.

1. Select **New Branch**.

1. Enter any branch name and select **Create Branch**.

1. Select **Code > Merge requests**.

1. Select **New Merge Request**.

1. Select the branch you created as the source branch.

1. Select **Compare branches and continue**.

1. Leave all options as default and select **Create Merge Request**.

      To trigger the Merge Request pipeline, you need to make some change to the code.

1. Select **Code > Open in Web IDE**.

1. Select the `README.md` file and change anything you want in the file.

1. Once complete, select **Source Control > Commit and push**.

1. From the pop-up that appears on the bottom right of your screen, select **Go to MR** to return to your Merge Request.

1. Navigate to **Build > Pipelines**.  You will see a new pipeline with the Merge Request label.

1. Select it to see its progress. You will see two jobs run, the build and run jobs specified in our `.gitlab-ci.yml file`.

1. Navigate back to the Merge Request by selecting **Code > Merge Requests**.

1. Select your Merge Request. Notice that there is now a section stating Merge Request pipeline. This section will show the progress of the Merge Request pipeline.

## Postface

With workflow rules and Merge Request pipelines in place, you transformed Tanuki Enterprises' CI/CD process from chaotic to controlled. The workflow rules eliminated the infinite loop problem by preventing pipelines from triggering on release tags, while Merge Request pipelines ensured that build and test jobs only run on active development work—not on every commit to main. Most importantly, the release job now executes exclusively on the main branch, preventing accidental production releases from feature branches.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabcicdhandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
