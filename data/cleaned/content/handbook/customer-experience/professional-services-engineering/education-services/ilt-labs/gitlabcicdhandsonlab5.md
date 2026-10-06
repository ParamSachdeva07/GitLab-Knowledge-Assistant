---
title: "GitLab CI/CD - Hands-On Lab: Investigating Broken Pipelines"
description: "This Hands-On Guide demonstrates how to troubleshoot and fix CI/CD pipelines"
---

> Estimated time to complete: 15 minutes

## Preface

Tanuki Enterprises is ready to take the final step in their CI/CD journey: automated deployments to production servers. However, the team quickly encountered major issues:

- **Cryptic Error Messages**: Jobs fail with unclear errors like "error in libcrypto" that provide no obvious solution
- **Trial and Error Debugging**: Developers waste hours trying random fixes without a systematic troubleshooting approach
- **No Troubleshooting Framework**: The team lacks a structured methodology for diagnosing and resolving pipeline failures
- **Fear of Deployments**: Without confidence in their ability to debug issues, developers avoid setting up deployment automation

## Objectives

In this lab, you'll learn systematic troubleshooting techniques for CI/CD pipelines. You'll intentionally introduce a common SSH key formatting error, practice isolating the root cause, leverage GitLab documentation to find solutions, and apply best practices for organizing job scripts using before_script sections for better maintainability.

## Task A. Setup the SSH Connection

As part of this course, you were provided with an SSH key to use for deployments. You will need to add this SSH key to GitLab to use it during your CI/CD process.

1. Navigate to your Tanuki App project.

1. Select **Build > Pipeline Editor**.

1. Add a new stage named deploy:

      ```yaml
      stages:
        - test
        - build
        - run
        - release
        - deploy
      ```

1. For this stage, we will have a single job named deploy app. The first thing this job will do is check if there is an SSH agent available, and install one if not.

      ```yaml
      deploy app:
        stage: deploy
        script:
          - 'which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )'
          - eval $(ssh-agent -s)
      ```

1. Next, we will set up a PEM file from our SSH key variable, setting the required permissions on the file so it can be used for SSH purposes. Note that we are using the `SSH_PRIVATE_KEY` variable, which is a group-level variable. You can see the full listing of our variables by navigating to your group, and selecting **Settings > CI/CD** and then selecting the **Variables** sub-menu.

      ```yaml
      deploy app:
        stage: deploy
        script:
          - 'which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )'
          - eval $(ssh-agent -s)
          - chmod 400 "$SSH_PRIVATE_KEY"
          - ssh-add "$SSH_PRIVATE_KEY"
          - mkdir -p ~/.ssh
          - chmod 700 ~/.ssh
      ```

1. We can add a simple SSH command to test if the connection is working.

      ```yaml
      deploy app:
        stage: deploy
        script:
          - 'which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )'
          - eval $(ssh-agent -s)
          - chmod 400 "$SSH_PRIVATE_KEY"
          - ssh-add "$SSH_PRIVATE_KEY"
          - mkdir -p ~/.ssh
          - chmod 700 ~/.ssh
          - ssh-keyscan -t rsa,ed2519 $ip >> ~/.ssh/known_hosts
          - ssh root@$ip 'ls /'
      ```

1. Finally, we will add in an `environment` keyword to enable us to track the deployment environment.

      ```yaml
      deploy app:
        stage: deploy
        script:
          - 'which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )'
          - eval $(ssh-agent -s)
          - chmod 400 "$SSH_PRIVATE_KEY"
          - ssh-add "$SSH_PRIVATE_KEY"
          - mkdir -p ~/.ssh
          - chmod 700 ~/.ssh
          - ssh-keyscan -t rsa,ed2519 $ip >> ~/.ssh/known_hosts
          - ssh root@$ip 'ls /'
        environment:
          name: prod
          url: "http://$ip:80"
      ```

1. Commit your changes, and let the pipeline run. You should see that the deploy app job has failed.

Let's figure out what went wrong, and how to fix it!

## Task B. Debugging the pipeline with Duo Agent Platform

1. Click the `deploy app` job. You should see an error message similar to `Unknown key type: "ed2519"` in the job log. We are going to use Duo Agent Platform (DAP) to help us resolve this vulnerability. Duo Agent Platform is GitLab's AI solution that can help you build issues, review merge requests, remediate vulnerabilities, and in this case, fix a broken pipeline.

1. Click on the **New chat** button in the top right.

1. In the `Choose an agent` menu, select **CI Expert**.

1. Write in the chat box "Can you help me fix this broken pipeline?" and press Enter. The CI Expert agent will analyze your job log, and recommend a solution.

1. Write in the chat box "Can you create a merge request to fix the broken pipeline?" and press Enter. The CI Expert agent will work to create a merge request. When the agent asks you for permission to create a commit and a merge request, press **Approve**.

> When it comes to any actions that make changes to your repo, GitLab Duo agents will always ask for permission to do so. This is to ensure you remain the Human In the Loop (HITL) when it comes to using DAP.

1. Click on the Merge Request link provided by the chat, or access the Merge Request by navigating to **Code > Merge Requests**.

1. Review the Merge Request to see what changes were made, and click on the **Merge** button to merge the code.

## Task C. Clean Up Deploy Job

Now that the job has been fixed, it is important to clean up the job so that the steps of the job are more clear. For example, we can move parts of the jobs from the `script` section to the `before_script` section.

1. Let's move the steps from the `'which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )'` to `chmod 700 ~/.ssh` into a `before_script` section. That way, it is clear which parts of the job are for setup, and which are the actual tasks being performed. Also, remember to change the SSH key variable back to the SSH_PRIVATE_KEY.

      The deploy job should now look like this:

      ```yaml
      deploy app:
        stage: deploy
        before_script:
          - 'which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )'
          - eval $(ssh-agent -s)
          - chmod 400 "$SSH_PRIVATE_KEY"
          - ssh-add "$SSH_PRIVATE_KEY"
          - mkdir -p ~/.ssh
          - chmod 700 ~/.ssh
        script:
          - ssh-keyscan -t rsa,ed25519 $ip >> ~/.ssh/known_hosts
          - ssh root@$ip 'ls /'
        environment:
          name: prod
          url: "http://$ip:80"
      ```

1. Run the pipeline to make sure the changes did not break anything in the pipeline.

## Postface

By working through a real-world deployment error, you developed a systematic troubleshooting framework that transformed their team's confidence. Your team learned to isolate failing commands, utilize agentic systems, and verify fixes methodically rather than guessing randomly. The structured approach—identify the error, isolate the command, consult DAP, apply the fix, and verify—reduced average debugging time from hours to minutes. Additionally, by refactoring the deploy job to use `before_script` for setup tasks, your team improved code readability and made their pipelines easier to maintain and troubleshoot in the future. With these troubleshooting skills and a working deployment configuration, Tanuki Enterprises now confidently automates deployments to production, knowing they can quickly diagnose and resolve any pipeline issues that arise.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabcicdhandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
