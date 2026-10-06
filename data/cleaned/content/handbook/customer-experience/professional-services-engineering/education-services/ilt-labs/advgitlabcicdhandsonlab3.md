---
title: "GitLab Advanced CI/CD - Hands-On Lab: Review Apps"
description: "This Hands-On Guide walks you through the process of creating review apps"
---

The purpose of this lab is to create a review app from a Node.js application. A review app is a temporary application environment automatically created for each merge request in a project. It allows developers and stakeholders to preview and interact with proposed changes in a live, isolated environment before merging them into the main branch.

> Estimated time to complete: 15 minutes

## Objectives

- Create a review app from the Node.js application

## Task A. Creating a Review App

1. In the left sidebar, select **Operate > Environments**.

1. Select **Enable Review Apps**.

1. Copy the provided script, which will look like this:

      ```yml
      deploy_review:
        stage: deploy
        script:
          - echo "Add script here that deploys the code to your infrastructure"
        environment:
          name: review/$CI_COMMIT_REF_NAME
          url: https://$CI_ENVIRONMENT_SLUG.example.com
        rules:
          - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      ```

      > If for any reason GitLab does not display this script when clicking **Enable Review Apps**, just copy the reference script above to use.

1. Navigate back to your code repository, and set your branch to the **review-app** branch.

1. Select **Build > Pipeline Editor**.

1. Paste the copied `deploy_review` job at the end of the `.gitlab-ci.yml` file.

1. For our example, we will alter the URL slightly to use an IP address as the URL. This variable `$ip` is a group level variable created when you redeemed your invitation code. To use this variable, we will also remove the `HTTPS` since our server only uses `HTTP`. Below is our finished `deploy_review` definition:

      ```yml
      deploy_review:
        stage: deploy
        script:
          - echo "Add script here that deploys the code to your infrastructure"
        environment:
          name: review/$CI_COMMIT_REF_NAME
          url: http://$ip:4001
        rules:
          - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      ```

1. Add the `deploy` stage to the `.gitlab-ci.yml` file.

      ```yml
      stages:
        - deps
        - test
        - deploy
      ```

1. Now, we can deploy our changes to the Review App. In your `deploy_review` job, add an `image` of `ubuntu:latest`.

      ```yml
      deploy_review:
        stage: deploy
        image: ubuntu:latest
      ```

1. Directly above the `script` of the `deploy_review` job, add the following `before_script`. The SSH private key is stored in a variable named SSH_PRIVATE_KEY. This key is added to the SSH agent to use for connections to the remote server:

      ```yml
        before_script:
          - 'which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )'
          - eval $(ssh-agent -s)
          - chmod 400 "$SSH_PRIVATE_KEY"
          - ssh-add "$SSH_PRIVATE_KEY"
          - mkdir -p ~/.ssh
          - chmod 700 ~/.ssh
      ```

1. Finally, update the job script to match the following job definition:

      ```yml
        script:
          - ssh-keyscan -t rsa,ed25519 $ip >> ~/.ssh/known_hosts
          - ssh root@$ip 'mkdir -p /www'
          - ssh root@$ip 'sudo apt-get update'
          - ssh root@$ip 'sudo apt-get install nodejs npm -y'
          - ssh root@$ip 'cd /www/ && npm init -y'
          - ssh root@$ip 'cd /www/ && npm i express'
          - ssh root@$ip 'cd /www/ && npm i -g pm2'
          - scp index.js root@$ip:/www
          - ssh root@$ip 'pm2 start -f /www/index.js'
      ```

1. Here is what your final job script should look like:

      ```yml
      deploy_review:
        stage: deploy
        image: ubuntu:latest
        before_script:
          - 'which ssh-agent || ( apt-get update -y && apt-get install openssh-client git -y )'
          - eval $(ssh-agent -s)
          - chmod 400 "$SSH_PRIVATE_KEY"
          - ssh-add "$SSH_PRIVATE_KEY"
          - mkdir -p ~/.ssh
          - chmod 700 ~/.ssh
        script:
          - ssh-keyscan -t rsa,ed25519 $ip >> ~/.ssh/known_hosts
          - ssh root@$ip 'mkdir -p /www'
          - ssh root@$ip 'sudo apt-get update'
          - ssh root@$ip 'sudo apt-get install nodejs npm -y'
          - ssh root@$ip 'cd /www/ && npm init -y'
          - ssh root@$ip 'cd /www/ && npm i express'
          - ssh root@$ip 'cd /www/ && npm i -g pm2'
          - scp index.js root@$ip:/www
          - ssh root@$ip 'pm2 start -f /www/index.js'
        environment:
          name: review/$CI_COMMIT_REF_NAME
          url: http://$ip:4001
        rules:
          - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      ```

1. Select **Commit changes**.

## Task C. Verify the review app

To test that your review app works, let's create a new merge request.

1. Select **Code > Branches**.

1. Select **New branch**.

1. Set the branch name to `test_review` and select **Create branch**.

1. Create a merge request for this branch.

1. Once you have created this, open the Web IDE from the merge request by selecting **Code > Open in Web IDE**

1. Select your `index.js` file.

1. Update your `res.send` to display any message you like. Below is an example:

      ```js
      const express = require('express')
          const app = express()
          const port = 4001

          app.get('/', (req, res) => {
            res.send('Our app is running!')
          })

          app.listen(port, () => {
            console.log(`Example app listening on port ${port}`)
      })
      ```

1. Select the **source control** icon. Enter a commit message, then click the **Commit and put to...** button to commit your code change.

1. Wait for the pipeline to complete.

1. Open your merge request.

1. Select **View app** after the pipeline completes.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/advgitlabcicdhandson).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
