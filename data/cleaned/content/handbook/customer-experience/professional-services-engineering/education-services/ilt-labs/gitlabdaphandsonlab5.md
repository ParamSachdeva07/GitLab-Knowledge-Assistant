---
title: "GitLab Duo Agent Platform - Hands-On Lab: Create and Secure Code with GitLab Duo Agent Platform"
description: "This Hands-On Guide walks you how to create and secure code using Duo Agent Platform"
---

> Estimated Time to Complete: 20 minutes

## Learning Objectives

By the end of this lab, you will be able to:

- Use AI vulnerability management to explain a finding in plain language.
- Use DAP to generate a remediation merge request for a SAST vulnerability.
- Use the Fix Pipeline flow to diagnose and repair a failed pipeline on a remediation branch.
- Trigger the Code Review Flow on a security remediation merge request and review AI feedback.
- Merge a remediation MR and confirm the vulnerability has been resolved.

## Overview

Security vulnerabilities are inevitable. The earlier they are caught, the cheaper and faster they are to fix. In this lab, four DAP capabilities come together on a single real problem.

The Swag Shop project has a SQL injection vulnerability in app.py that has been sitting in the vulnerability report unresolved. You generate a fix, but while the merge request is open you also need to update a dependency. A typo in the package name breaks the pipeline. You use the Fix Pipeline flow to diagnose and resolve it, then get an AI code review on the security fix and merge.

## Task A: Locate the Vulnerability

Your starting point is the Swag Shop vulnerability report. The project's security scanners have already run and flagged a number of findings. Your job in this task is to find the one you will fix.

1. Let's start by making sure the flows we need are turned on at project level. Within your project, navigate to **Settings > General > GitLab Duo** and ensure that "Turn on SAST false positive detection" and "Turn on SAST vulnerability resolution workflow" are both switched on.

1. In the left sidebar, select **Secure > Vulnerability report**.

1. Click in the search field, select **Report Type**, and then select **SAST**.

      >**Note:** DAP's vulnerability remediation works with SAST findings only.

1. Locate the vulnerability named **Improper neutralization of special elements used in an SQL Command ('SQL Injection')** on line 214 of `app.py`.

1. Click the vulnerability to open its detail view and review the notes.

### Expected Output: Task A

- The SQL injection vulnerability is visible in the **Vulnerability Report**, filtered by SAST, with the detail view showing the affected file and line number.

## Task B: Understand and Remediate the Vulnerability

You now have one open vulnerability to work with. In this task, you will ask GitLab Duo to explain it in plain language, then generate a merge request that fixes it. By the end of Task B, you will have one open merge request — the remediation merge request — on its own branch.

### Task B.1: Explain the Vulnerability

Before making any changes, ask GitLab Duo to interpret the finding. This confirms you understand what the vulnerability is and why it matters before any code is touched.

1. In the vulnerability detail view, select **AI vulnerability management** in the top-right corner.

1. Select **Explain with AI**.

      An agentic chat session will open and explain the vulnerability in plain language, including the affected code pattern and recommended remediation approaches.

1. Review the explanation before proceeding.

>**What you're looking at:** The SQL injection in app.py at line 214 occurs because user input is embedded directly into a SQL query string. An attacker can manipulate that input to change the query's logic. The fix is to use a parameterized query, which separates the query structure from the data.

### Task B.2: Generate the Remediation Merge Request

Now that you understand the vulnerability, use DAP to generate a fix.

1. Select **AI vulnerability management** again, and then select **Resolve with AI**.

1. Wait for the session to complete. When it finishes, a merge request will open automatically.

### Task B.3: Review the Remediation Merge Request

Before doing anything else with the branch, confirm that the generated fix actually addresses the vulnerability correctly. This is a step you would always take in a real workflow.

1. From the open merge request, select the **Changes** tab.

1. Confirm that the vulnerable string concatenation query has been replaced with a parameterized query. The fix should replace this vulnerable pattern:

      ```python
      vulnerable_query = f"SELECT * FROM demo_products WHERE name LIKE '%{search_term}%' OR description LIKE '%{search_term}%'"

      cursor.execute(vulnerable_query)
      ```

      With this:

      ```python
      secure_query = "SELECT * FROM demo_products WHERE name LIKE ? OR description LIKE ?"

      search_param = f"%{search_term}%"

      cursor.execute(secure_query, (search_param, search_param))
      ```

1. Select the **Pipelines** tab. Once the pipeline has finished, open the pipeline details by selecting the **Passed** status. Select the **Security** tab, and check that the **Improper neutralization of special elements used in an SQL Command ('SQL Injection')** for line 214 of `app.py` is no longer reported.

1. Navigate back to the remediation merge request that you just had open.

### Expected output: Task B

- An agentic chat session explains the SQL injection vulnerability in plain language.
- One merge request — the remediation merge request — is visible under **Code > Merge Requests**, with changes to app.py that address the vulnerability.

## Task C: Fix the Pipeline

With the remediation merge request open, you need to update a project dependency. You add the package to `requirements.txt` but make a typo in the package name. The pipeline runs and fails. Before you can merge the vulnerability fix, you need to resolve this first.

### Task C.1: Introduce the Dependency Error

1. Note the source branch name shown in the remediation merge request header. It will start with something similar to `duo/fix/...`. You will need this in the next step.

1. In the left sidebar, navigate to **Code > Repository**.

1. Click the branch dropdown list and change the branch from `main` to your remediation branch. The file list now shows the contents of the remediation branch.

1. Open `requirements.txt` from the file list.

1. Click **Edit > Open in Web IDE**.

1. Add the following line anywhere in the file: `nonexistent-package==1.0.0`

1. In the left toolbar, select the **Source Control** icon to see your pending changes.

1. In the **Commit message** field, enter: `updated requirements`.

1. Commit the changes to the remediation branch.

You do not need to create a new merge request. Committing to the remediation branch automatically updates the existing remediation merge request and triggers a new pipeline run.

### Task C.2: Read the Failure

Before triggering the fix, read the error so you understand what the Fix Pipeline flow is about to solve.

1. From the remediation merge request, select the **Pipelines** tab. Wait for the pipeline to complete and confirm it shows a failed status.

1. Click the failed pipeline to open its detail view.

1. Locate the failed job and click it to open its log. Confirm you see output similar to:

      ```yaml
      ERROR: Could not find a version that satisfies the requirement nonexistent-package==1.0.0

      ERROR: No matching distribution found for nonexistent-package==1.0.0
      ```

      >**Note:** You do not need to fix this manually. Reading the log confirms what failed and helps you understand what the Fix Pipeline flow will do next.

### Task C.3: Trigger the Fix Pipeline Flow

1. Navigate to **Build > Pipelines** and select the pipeline ID, like #12345, of your `updated requirements` pipeline.

1. At the top of the page, click **Fix pipeline with Duo**.

      >**Note:** The session should open automatically. If it does not, navigate to **Automate > Sessions** and locate the session for the Fix Pipeline flow.

1. Click the **Activity** tab and observe the steps the flow is executing: log analysis, root cause identification, and file modification.

1. Wait for the session status to change to **Finished** on the **Details** tab before proceeding.

>**What the flow is doing:** The Fix Pipeline flow reads the failed job log, identifies the root cause (a package that does not exist), locates the file responsible (requirements.txt), and opens a new merge request with the bad entry removed. Notice that the flow creates a merge request rather than committing directly to the branch. This is intentional: DAP follows the same review process you would expect from any developer on the team.

### Task C.4: Review and Merge the Fix Merge Request

The Fix Pipeline flow has created a new merge request, the fix merge request, that targets the remediation branch. You are working in the fix merge request for the rest of this task.

1. Follow the link in the session output to the fix merge request. If you don't see the link, navigate to **Code > Merge Requests** and look for the merge request created by the Fix Pipeline flow.

1. On the **Changes** tab, confirm that `nonexistent-package==1.0.0` has been removed from `requirements.txt` and that no other changes have been made.

1. Select the **Pipelines** tab and wait for the pipeline to complete successfully.

1. Navigate back to the merge request and select the **Overview** tab.

1. Select **Mark as ready** to convert the merge request from a draft, and then select **Merge**. This merges the fix into the remediation branch, not the main branch.

1. To confirm the fix, navigate to **Code > Repository** and open `requirements.txt`. Confirm that `nonexistent-package==1.0.0` has been removed.

### Expected output: Task C

- The Fix Pipeline flow session is visible under **Automate > Sessions** with a status of **Finished**.
- The flow opened a merge request removing `nonexistent-package==1.0.0 from requirements.txt`.
- The fix merge request has been merged into the remediation branch.
- The pipeline on the remediation merge request is now passing.

## Task D: Trigger the Code Review Flow

At this point you have one open merge request, the remediation merge request, with a passing pipeline. Before merging, you will run the Code Review Flow to get AI feedback on the fix.

1. Navigate to **Code > Merge Requests** and open the remediation merge request.

1. On the **Overview** page, locate the **Reviewers** section in the right sidebar.

1. Click **Edit** and search for GitLabDuo. Select it to assign GitLab Duo as a reviewer.

      >**Alternative trigger:** You can also type `/assign_reviewer @GitLabDuo` in any comment box on the merge request.

1. On the merge request **Overview** tab, scroll down to the activity feed to observe the Code Review Flow running in real time.

1. Wait for GitLab Duo to finish its review, then read the comments it has posted on the merge request.

### Expected output: Task D

- GitLab Duo is assigned as a reviewer on the remediation MR.
- One or more review comments are posted by GitLab Duo.

## Task E: Merge the Fix and Confirm Resolution

At this point you have one open merge request, the remediation merge request, with a passing pipeline and a completed code review. This is the final step: merge the fix and confirm the vulnerability is gone.

### Task E.1: Merge the Remediation Merge Request

1. Navigate to **Code > Merge Requests** and open the remediation merge request.

1. Select the **Overview** tab.

1. Review the **AI Generated Fix** field. This summarizes the specific code changes made to address the vulnerability, confirming what was fixed and why.

1. Scroll down, and select **Merge**.

1. Select the pipeline number to observe when the merge pipeline completes.

### Task E.2: Confirm the Vulnerability is Resolved

1. In the left sidebar, select **Secure > Vulnerability report**.

1. In the search field, select **Report Type** and then select **SAST**.

1. Confirm the vulnerability, **Improper neutralization of special elements used in an SQL Command ('SQL Injection')** on line 214, is no longer listed.

### Expected output: Task E

- The pipeline passes after the remediation merge request is merged into the main branch.
- The SQL injection vulnerability is no longer visible in the Vulnerability Report filtered by SAST.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabdaphandson/).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
