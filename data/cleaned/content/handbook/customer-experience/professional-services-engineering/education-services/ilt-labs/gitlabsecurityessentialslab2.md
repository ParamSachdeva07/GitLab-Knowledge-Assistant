---
title: "GitLab Security Essentials - Hands-On Lab: Addressing Vulnerabilities"
description: "This Hands-On Guide walks you through how to triage and respond vulnerabilities in your application"
---

> Estimated time to complete: 15 minutes

In the last lab, you introduced the SAST and Secret Detection scanners into your project. In this lab, we will explore methods to triage and resolve vulnerabilities.

## Task A. Vulnerability Triage Process

1. Navigate to your Security Labs project.

1. In the left sidebar, select **Secure > Vulnerability Report**. To start your triage process, it is recommended to sort your vulnerabilities by severity, focusing on vulnerabilities that have not yet been triaged. This is the default setting.

1. In the security report, select **Severity** to change the sort order. Ensure that the arrow is pointing down so that severity is sorted from highest to lowest.

1. Select the vulnerability **Active debug code** that was found by the **GitLab Advanced SAST** scan.

1. Review the vulnerability. You will see that the finding is valid, as the `main.py`'s HTTP debug code is set to 'True'.

1. In the top right corner, click **Edit Vulnerability**, and then choose **Change status**. Set the status to **Confirmed**, and click **Change status**.

1. Scroll down to the bottom of the page, and select **Create issue**.

1. You will see that the issue automatically populates the vulnerability title and details. Review the issue details, then select **Create issue**.

1. Return to **Secure > Vulnerability Report**.

1. Select the first instance of the vulnerability **Improper neutralization of special elements used in a SQL command ('SQL Injection')**.

1. Select the **Code flow** tab.

1. Review the code flow to see how the vulnerability occurs. In the top right corner, click **Edit Vulnerability**, and then choose **Change status**. Set the status to **Confirmed**, and click **Change status**.

1. Select the **Details** tab.

1. Scroll down to the bottom of the page, and select **Create issue**.

1. Review the issue and select **Create issue**.

At this point, we've created two issues to address as security issues in our application. Let's review the process for fixing these vulnerabilities.

## Task B. Fixing Vulnerabilities

To resolve these vulnerabilities, we are going to use Duo Agent Platform (DAP). Duo Agent Platform is GitLab's AI solution that can help you build issues, review merge requests, fix broken pipelines, and in this case, remediate a vulnerability.

1. Navigate to your **Settings > General**, and click on **GitLab Duo**. Click the switches under **Turn on SAST false positive detection**, and **Turn on SAST vulnerability resolution workflow**. These options will help us handle vulnerability remediation, as well as check for potential false positives.

1. Select **Save changes**.

1. Navigate to **Security > Vulnerability Report**. Select the *Improper neutralization of special elements used in an SQL Command ('SQL Injection')* vulnerability that was found on line 244.

1. In the top right corner of the vulnerability, select **AI Vulnerability Management**, and then select **Explain with AI**. The DAP tool will analyze the vulnerability, and explain how the vulnerability can be used against you. The agent will also explain ways to be able to remediate the vulnerability.

1. Select **AI Vulnerability Management**, and then select **Check for False Positive**. The AI will now analyze how your codebase is using the code that has the vulnerability, and check if it is a false positive or not. This will take a few minutes to run.

1. Select **AI Vulnerability Management**, and then select **Resolve with AI**. This will create a merge request that will remediate the vulnerability. Once the AI has completed creating the vulnerability, it will take you directly to the Merge Request.

1. Review the changes made by the Merge Request, and select **Merge** when satisfied.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabsecurityessentials).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
