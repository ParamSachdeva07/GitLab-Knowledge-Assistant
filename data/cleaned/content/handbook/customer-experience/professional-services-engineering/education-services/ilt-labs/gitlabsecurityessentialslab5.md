---
title: "GitLab Security Essentials - Hands-On Lab: DAST and API Scans"
description: "This Hands-On Guide walks you through the process of using container scanning in your projects"
---

> Estimated time to complete: 40 minutes

## Objectives

Many projects are deployed as web applications with API components. To be able to scan these components, you can utilize the DAST and API security scanners.

In this lab, you will learn how to implement both scanners for your projects.

## Task A. Setting up DAST Scans

To test out DAST scans, we are going to set up an instance of a vulnerability web application called [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/). Scanning this application will show you the full range of DAST scan results you can expect to see.

1. Create a new blank project. Name the project `DAST`.

1. In the DAST project, create a `.gitlab-ci.yml` file.

1. To start, add the DAST stage to your configuration:

      ```yml
      stages:
        - dast
      ```

1. DAST currently uses a CI/CD template, which we will include just below our stages.

      ```yml
      include:
        - template: DAST.gitlab-ci.yml
      ```

1. Since we don't have a dedicated server, we will opt to pass the Juice Box application into DAST as a Docker service. To do this, start by defining the service below the template include:

      ```yml
      dast:
        services:
          - name: bkimminich/juice-shop:v16.0.0
            alias: juiceshop
      ```

1. We can provide many different variables to our DAST scanner. We will add the following values to the DAST scanner:

      ```yml
      variables:
          DAST_TARGET_URL: "http://juiceshop:3000/"
          DAST_AUTH_URL: "http://juiceshop:3000/#/login"
          DAST_FULL_SCAN: "false"
          DAST_AUTH_USERNAME: "admin@juice-sh.op"
          DAST_AUTH_PASSWORD: "admin123" # use protected/masked variables, this is only for demonstration purposes
          DAST_AUTH_USERNAME_FIELD: "css:input[id=email]"
          DAST_AUTH_PASSWORD_FIELD: "css:input[id=password]"
          DAST_AUTH_SUBMIT_FIELD: "css:button[id=loginButton]"
          DAST_SCOPE_EXCLUDE_ELEMENTS: "css:[id=navbarLogoutButton]"
          DAST_AUTH_REPORT: "false"
          DAST_REQUEST_COOKIES: "welcomebanner_status:dismiss,cookieconsent_status:dismiss"
          DAST_CRAWL_GRAPH: "false"
      ```

      > To highlight some variables, `DAST_TARGET_URL` and `DAST_AUTH_URL` provide a target for scanning and authentication. We provide credentials for authentication with `DAST_AUTH_USERNAME` and `DAST_AUTH_PASSWORD`. The `DAST_AUTH_USERNAME_FIELD` and related field variables tell DAST where to input login data. Our remaining settings are scan settings to help reduce the scan time for this demonstration.

1. After entering all of these values, your YAML file should look like this:

      ```yml
      stages: # List of stages for jobs, and their order of execution
        - dast

      include:
        - template: DAST.gitlab-ci.yml

      dast:
        services:
          - name: bkimminich/juice-shop:v16.0.0
            alias: juiceshop
        variables:
            DAST_TARGET_URL: "http://juiceshop:3000/"
            DAST_AUTH_URL: "http://juiceshop:3000/#/login"
            DAST_FULL_SCAN: "false"
            DAST_AUTH_USERNAME: "admin@juice-sh.op"
            DAST_AUTH_PASSWORD: "admin123" # use protected/masked variables, this is only for demonstration purposes
            DAST_AUTH_USERNAME_FIELD: "css:input[id=email]"
            DAST_AUTH_PASSWORD_FIELD: "css:input[id=password]"
            DAST_AUTH_SUBMIT_FIELD: "css:button[id=loginButton]"
            DAST_SCOPE_EXCLUDE_ELEMENTS: "css:[id=navbarLogoutButton]"
            DAST_AUTH_REPORT: "false"
            DAST_REQUEST_COOKIES: "welcomebanner_status:dismiss,cookieconsent_status:dismiss"
            DAST_CRAWL_GRAPH: "false"
      ```

1. Commit these changes and let the DAST scan run. You can monitor the job progress from **Build > Pipelines**.

      > Note: This job can take up to 15 minutes to complete.

1. After this completes, in the left sidebar, select **Secure > Vulnerability report**.

1. Review the results found by the DAST scanner.

## Task B. Setting up API Scanners

API scanners allow you to scan your application API endpoints for potential vulnerabilities. To demonstrate this process, we will use an application template which contains an API configuration.

1. Navigate to your **Security Labs** project.

1. Take some time here to review the `postman_collection.json` file. This file contains the definitions required to run API scanning against the application in this project. After reviewing the file and structure, you can proceed with enabling API scanning.

1. Navigate to **Code > Repository** and edit `.gitlab-ci.yml`.

1. To add API scanning to our container, define the `dast` stage and add the API security template.

      ```yml
      include:
      #Other scanners would be here as well.
          - template: API-Security.gitlab-ci.yml

      stages:
          - build
          - test
          - dast
      ```

1. Add the job definition for the API scanner.

      ```yml
      api_security:
          services:
              - name: $CI_REGISTRY_IMAGE/$CI_COMMIT_REF_SLUG:$CI_COMMIT_SHA
                alias: target
          variables:
              APISEC_POSTMAN_COLLECTION: postman_collection.json
              APISEC_TARGET_URL: http://target:7777
      ```

> This template, as well as all the other templates you have seen throughout this course, can be found in the [GitLab CI/CD templates repository](https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/gitlab/ci/templates).

1. Commit these changes and view the results once the pipeline completes.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabsecurityessentials).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
