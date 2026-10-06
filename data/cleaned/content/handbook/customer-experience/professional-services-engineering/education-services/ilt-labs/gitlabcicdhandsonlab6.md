---
title: "GitLab CI/CD - Hands-On Lab: Deploying Applications"
description: "This Hands-On Guide demonstrates how to deploy applications in a pipeline"
---

> Estimated time to complete: 15 minutes

## Preface

Tanuki Enterprises has built, tested, and validated their applications through automated pipelines, but a critical gap remains—getting code into production still requires manual intervention. The deployment challenges are mounting:

- **Manual Deployment Steps**: Engineers must SSH into servers, copy files, configure services, and restart applications by hand
- **Human Error Risk**: Manual deployments lead to forgotten steps, incorrect file permissions, and misconfigured services
- **No Deployment Tracking**: The team has no visibility into what version is running in production or when deployments occurred
- **Inconsistent Environments**: Each deployment might be slightly different depending on who performs it
- **Deployment Delays**: Waiting for someone with server access and knowledge to perform deployments creates bottlenecks

## Objectives

In this lab, you'll complete the CI/CD journey by implementing automated deployment to production servers. You'll transform your Go application into a web service, use SSH and SCP to deploy artifacts, configure systemd services for process management, and create tracked deployment environments in GitLab—enabling one-click deployments from commit to production.

## Task A. Preparing Code

First, let's make some small adjustments to our code so that it runs as a web application:

1. Open `main.go`.

1. Delete the existing code, and replace it with the following:

      ```go
      package main

      import (
        "fmt"
        "log"
        "net/http"
      )

      func handler(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hi there")
      }

      func main() {
        http.HandleFunc("/", handler)
        log.Fatal(http.ListenAndServe(":80", nil))
      }
      ```

      This application will listen on port 80 for any requests to the "/" (root) endpoint. When it receives a request, it will print out the message *Hi there*.

      To accommodate our new application type, we will modify our CI/CD process by removing the tests to run the application binary. These tests will no longer work, as they will cause the application to pause and wait for connections. Instead, we will deploy this application to a test server to be able to test our application. To start, your CI/CD file should look like this:

      ```yaml
      workflow:
        rules:
          - if: $CI_COMMIT_TAG
            when: never
          - when: always

      default:
        image: golang

      include:
        - component: <replace-with-link-to-your-component>
          inputs:
            stage: build

      stages:
        - test
        - build
        - run
        - release
        - deploy

      test go:
        stage: test
        script: go test array/ArrayUtils
        allow_failure: true

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

      release job:
        stage: release
        image: registry.gitlab.com/gitlab-org/release-cli:latest
        script:
          - echo "Generating the latest release!"
        release:
          tag_name: 'v0.$CI_PIPELINE_IID'
          description: 'The latest release!'
        rules:
          - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH

      deploy app:
        stage: deploy
        environment:
          name: prod
          url: "http://$ip:80"
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
      ```

1. To ensure we have access to the build artifact in the deploy job, remove the run condition (rules block) from the job:

      ```yaml
      build go:
        stage: build
        script:
          - go build
        artifacts:
          paths:
            - array
      ```

## Task B. The Deployment Process

We now have an SSH connection working between the GitLab runner and our target server. The final step we have is to deploy our application to the server! Ideally, we would only do this on commits to the default branch.

To be able to launch and maintain the execution of our web application, we will need to add it as a system service for our server. To achieve this, we will write a simple system service.

1. Create a new file at the root of your project named `array.service`. In this file, add the following text:

      ```bash
      [Unit]
      Description=
      After=network.target

      [Service]
      Type=simple
      ExecStart=/www/array

      [Install]
      WantedBy=multi-user.target
      ```

1. In your `.gitlab-ci.yml` file, add a rule to only run the deploy job on default branch commits.

      ```yaml
      deploy app:
        stage: deploy
        image: ubuntu:latest
        before_script:
          - "which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )"
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
        rules:
          - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
      ```

1. Our code will need to move the array binary to the `www` directory, and move the service definition file to the /lib/systemd/system directory. To achieve this, you can use the `scp` command. Add the following code block to your `script` section after the `ssh root@$ip 'ls /'` command:

      ```bash
        - ssh root@$ip 'mkdir -p /www'
        - ssh root@$ip 'test -e /www/array && rm -f /www/array || echo "No existing /www/array to delete"'
        - scp array root@$ip:/www
        - scp array.service root@$ip:/lib/systemd/system/
        - ssh root@$ip 'ls /www'
        - ssh root@$ip 'ls /lib/systemd/system'
        - ssh root@$ip 'systemctl enable array.service'
        - ssh root@$ip 'systemctl restart array.service'
        - ssh root@$ip 'systemctl status array.service'
      ```

    >Your `deploy app` job should now look like this:

      ```yaml
      deploy app:
        stage: deploy
        image: ubuntu:latest
        before_script:
          - "which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )"
          - eval $(ssh-agent -s)
          - chmod 400 "$SSH_PRIVATE_KEY"
          - ssh-add "$SSH_PRIVATE_KEY"
          - mkdir -p ~/.ssh
          - chmod 700 ~/.ssh
        script:
          - ssh-keyscan -t rsa,ed25519 $ip >> ~/.ssh/known_hosts
          - ssh root@$ip 'mkdir -p /www'
          - ssh root@$ip 'test -e /www/array && rm -f /www/array || echo "No existing /www/array to delete"'
          - scp array root@$ip:/www
          - scp array.service root@$ip:/lib/systemd/system/
          - ssh root@$ip 'ls /www'
          - ssh root@$ip 'ls /lib/systemd/system'
          - ssh root@$ip 'systemctl enable array.service'
          - ssh root@$ip 'systemctl restart array.service'
          - ssh root@$ip 'systemctl status array.service'
        environment:
          name: prod
          url: "http://$ip:80"
        rules:
          - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
      ```

1. After the pipeline has successfully completed, you can navigate to **Operate > Environments** , and see your environment has been deployed. Click on the **Open** button to access your newly deployed application.

## Postface

With automated deployment in place, your team achieved true continuous delivery. Every commit to the main branch now automatically deploys to production—the application binary is copied to the server, the systemd service is configured and restarted, and the deployment is tracked in GitLab's Environments page with a direct link to the running application. The combination of SSH automation, artifact management, and environment tracking eliminated manual deployment steps entirely, reduced deployment time from 30 minutes to under 3 minutes, and removed human error from the process. The team gained complete visibility into their production environment, including deployment history, who deployed what, and when. Most importantly, Tanuki Enterprises now operates with genuine continuous delivery—code flows automatically from commit through build, test, and deployment to production, allowing developers to ship features to users multiple times per day with confidence and zero manual intervention.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabcicdhandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
