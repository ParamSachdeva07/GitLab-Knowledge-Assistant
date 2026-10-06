---
title: "GitLab Fundamentals - Hands-On Lab: Continuous Integration and Development"
description: "This Hands-On Guide walks you through the process of adding CI/CD to your project."
---

> Estimated time to complete: 30 minutes

## Objectives

In this lab, we will explore creating a basic CI/CD pipeline for our QA project.

## Task A. Setting up a code base

Before we start creating a CI/CD process, we need some code to run our CI/CD process against. To start, navigate to your `Cool App QA` project.

1. In your project, select **+ > New file**.

1. In the **Filename** field, type `main.go`.

1. Inside of `main.go`, add the following code:

      ``` go
      package main

      import(
          "fmt"
      )

      func main() {
          fmt.Println("We are up and running!")
      }

      ```

1. Select **Commit changes**.

1. Write an appropriate message for the commit, and change the name of the branch to `initial-code`.

1. Make sure that the merge request checkbox is checked, and click **Commit changes**.

1. Leave all the merge request options at their defaults and select **Create merge request**.

      From here, we have one additional file to add to our code, which is a `go.mod` file. To add this:

1. In the left sidebar, select **Code > Branches**.

1. Select `initial-code`.

1. Select **+ > New file**.

1. In the **Filename** field, type `go.mod`.

1. Add the following code to the file:

      ```go
      module array

      go 1.22.2
      ```

1. Select **Commit changes**.

1. Ensure that **Commit to current `initial-code` branch** is selected. Select **Commit changes**.

With our code created, we can now start to create a CI/CD process for the code.

## Task B. Creating a CI/CD Process

Let's create a CI/CD process for the code we just wrote. Our goal is to create a process that builds the code we wrote. To do this, we need to create a `.gitlab-ci.yml` file. This file will contain all jobs and stages for our CI/CD process.

1. In the left sidebar, select **Code > Repository**.

1. Select **+ > New file**

1. In the **Filename**, input `.gitlab-ci.yml`.

1. Copy the following code into your `.gitlab-ci.yml` file:

      ```yml
      stages:
        - build

      build go:
        image: golang
        stage: build
        script:
          - go build
          - ./array
      ```

      > We defined one stage, which is **build**. In this stage, there is a single job, which runs one script: `go build`. The result of this will be your Go application being compiled. `./array` will then run your compiled application. The `image` keyword is used to ensure the job runs in a Golang Docker container in the GitLab Runner.

1. Select **Commit changes**. Ensure that **Commit to the current `initial-code` branch** is selected.

1. Select **Commit changes**.

## Task C. Viewing the CI/CD Process

1. After committing your code, your pipeline will immediately start. To view the pipeline, navigate to **Build > Pipelines**.

      Here, you will see a summary of all of your project pipelines. Each pipeline shows the following details:
      - The status of the pipeline
      - The pipeline name, ID, branch, and triggering commit
      - Who created the pipeline
      - A breakdown of pipeline status by stage

1. To view more details about the pipeline, select the **Status** of the pipeline. In this UI, you will see a graph of the pipeline, showing each stage, and the jobs associated with the stage.

1. Select your **build go** job.

      > On this screen, you will see details about your job, including all of the commands run during your job execution. On the right, you will see the duration of the job, when the job finished, how long the job was queued, the runner that completed the job, the commit that triggered the job, and further pipeline details related to the job.

      Let's explore each of these in detail. To start, navigate to your job:

1. Select **Build > Jobs**.

1. Select your **build go** job.

      Let's walk through the job log to better understand each job stage. The first thing you will see is something like this:

      **Setting up your job environment**

      ```bash
      Running with gitlab-runner 17.0.0 (44feccdf)
            on ilt-gitlab-runner xZL9uN-ry, system ID: s_e1aab81f250d
      Resolving secrets
      Preparing the "docker-autoscaler" executor
      00:33
      Dialing instance https://www.googleapis.com/compute/v1/projects/demosys-ilt-training-cloud/zones/us-central1-c/instances/added-scale-ilt-runner-group-1138177e63ca2c1e...
      Instance https://www.googleapis.com/compute/v1/projects/demosys-ilt-training-cloud/zones/us-central1-c/instances/added-scale-ilt-runner-group-1138177e63ca2c1e connected
      Using Docker executor with image golang ...
      Pulling docker image golang ...
      Using docker image sha256:92c72d51a65b247eb5672073192030d4964cee907770b0569665499e9880fa48 for golang with digest golang@sha256:ab1f5c47de0f2693ed97c46a646bde2e4f380e40c173454d00352940a379af60 ...
      ```

      The GitLab lab environment uses runner managers to help with scaling jobs. When your job starts, it first enters a queue. When a runner manager is available, it picks up the job. It then creates an instance and sets it up with the defined Docker image, in this case, the Golang image. This image is pulled and loaded onto the runner, making it ready to start processing your job request.

      **Cloning your Git repository**

      After the environment setup, GitLab will clone your repository onto the runner.

      ```bash
      Preparing environment
      00:02
      Running on runner-xzl9un-ry-project-25858-concurrent-0 via ilt-autoscale-runner-manager-2...
      Getting source from Git repository
      00:02
      Fetching changes with git depth set to 20...
      Initialized empty Git repository in /builds/training-users/session-c68006ec/iua7f2zr/fundamentals/qa/cool-app-qa/.git/
      Created fresh repository.
      Checking out e4f0de4d as detached HEAD (ref is initial-code)...
      Skipping Git submodules setup
      ```

      After doing this, all of your code will be available on the runner. One important note is that your runner now has access to your Git repository and has a link to your remote repository. This means two things:

      - You can access and use any files in your Git repository
      - You can commit changes back to your repository if you make any during your job process

      **Optional Task:**
      Want to see this in action? Add the `ls` command to your job scripts. This will list the current directory, showing you all the files that were cloned to the runner.

      ```yaml
      stages:
      - build

      build go:
      stage: build
      image: golang
      script:
      - ls
      - go build
      - ./array
      ```

      **Executing your Scripts:**
      After the environment is set up and your repository is cloned, your job scripts will run.

      ```bash
      Executing "step_script" stage of the job script

      Using docker image sha256:5905f95343e84d1f8f14aff8f8b83747fb39ea0e0fad52a9d14cf41860295fff for golang with digest golang@sha256:f43c6f049f04cbbaeb28f0aad3eea15274a7d0a7899a617d0037aec48d7ab010 ...
      $ go build
      Cleaning up project directory and file based variables

      Job succeeded
      ```

      To summarize, there are a few important ideas to keep in mind when considering running jobs in your pipeline.

      - Jobs will generally use a Docker image to run your job scripts

      - Every job runs on a separate runner, within its own Docker container, so there are no concerns about jobs interfering with each other

      - You have full access to your Git repository and any other system resources during the execution of your jobs

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabfundamentalshandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
