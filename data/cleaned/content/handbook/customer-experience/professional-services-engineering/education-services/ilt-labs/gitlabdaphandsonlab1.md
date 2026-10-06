---
title: "GitLab Duo Agent Platform - Hands-On Lab: Use a Foundational Flow"
description: "This Hands-On Guide walks you through the basics of using a Foundational Flow in GitLab"
---

> Estimated time to complete: 20 minutes

## Objectives

By the end of this lab, you will be able to:

- Enable foundational flows in your GitLab environment.
- Create an issue using a pre-written description.
- Use the **Generate MR With Duo** foundational flow to automatically create a merge request from an issue.
- Trigger the Code Review Flow on the agent-generated merge request and review AI feedback.
- Review and merge the agent-generated code changes.

## Overview

Foundational flows are workflows built directly into GitLab that automate common development tasks without any custom configuration or additional code. Rather than manually scaffolding branches, writing boilerplate, and opening merge requests by hand, foundational flows delegate that work to GitLab Duo, moving you from idea to code faster and with less context switching.

Imagine it's your first week as a developer on the Swag Shop team. The homepage doesn't distinguish featured products, and it should. You've never used a foundational flow before, but this is the right moment to try.

In this lab, you will generate a merge request from an issue using a foundational flow, trigger the Code Review Flow, and merge. By the end the featured badge will be live, and you'll have a working sense of what flows can do without you.

## Task A: Set up Your Project and Create an Issue

### Task A.1: Fork the Sample Project

This lab uses a pre-built sample project to give the agent a realistic codebase to work against. Forking it into your own namespace gives you a personal copy you can modify freely without affecting the source.

1. Navigate to the GitLab Swag Shop project at: https://ilt.gitlabtraining.cloud/professional-services-classes/templates/gitlab-swag-shop

1. In the top-right corner, click **Fork**.

1. In the **Project name** field, enter `GitLab Swag Shop Flows`.

1. In the **Project URL** field, under **Select a namespace**, select your top-level group (for example, `group-abcde-user_fghijk`).

1. Leave all remaining settings as-is and click **Fork project**.

The fork might take a moment or two to complete. After it completes, take a moment to review the pre-built files included in the project. They will be used throughout the remaining labs.

### Task A.2: Enable Foundational Flows

First, you will need to verify your foundational flows are enabled. This setting allows GitLab Duo to automate workflows, such as creating branches and generating merge requests, within projects in your group.

1. In your **Swag Shop DAP Workshop** project, navigate to **Settings > General**.

1. Expand the **GitLab Duo features** section.

1. Verify that **Allow foundational flows** has been enabled. If it is not enabled, click the toggle to enable it. Click **Save changes**.

### Task A.3: Remove the Fork Relationship

Removing the fork relationship establishes your copy as a fully independent repository and ensures that foundational flows act only on your fork.

1. In the left sidebar, select **Settings > General > Advanced**.

1. Locate the **Remove fork relationship** section and click **Remove fork relationship**.

1. Enter your project name and select **Confirm**.

### Task A.4: Run the Initial Pipeline

The Swag Shop Flows project uses GitLab Pages to host the web application. Pages deployments are triggered by a CI/CD pipeline. Until at least one pipeline has run successfully, there is no deployed site to view. You need to trigger that first pipeline manually.

1. In the left sidebar, select **Build > Pipelines**.

1. Click **New pipeline**.

1. Leave all settings as default and click **New pipeline**.

1. Wait for the pipeline to complete successfully before proceeding. This will take several minutes.

### Task A.5: View the Application

With the pipeline complete, the Swag Shop is now deployed and ready to preview.

1. Navigate to **Deploy > Pages** in the left sidebar.

1. Click **Visit site** to open the live Swag Shop in a browser.

   *Please note:* Depending on your network's access rules / firewalls, you may get an error when you click on this link due to the review deployment not having a signed SSL certificate. If that is the case, simply carry on with the rest of the lab, as this will not stop you from performing any subsequent steps. Feel free to ask your Instructor to show you their deployment if you want to see how it looks.

   >**Note:** There are no featured products on the homepage yet. This is your baseline. After you merge the agent's changes later in the lab, you will return here and refresh to confirm the featured badge and border have appeared.

1. Keep this tab open.

### Task A.6: Create an Issue

The agent reads the issue title and description to understand what code changes are needed. A well-written issue is essential for generating accurate results.

1. Navigate back to the `GitLab Swag Shop Flows` project.

1. Navigate to **Plan > Work items**.

1. Click **New item**.

1. Ensure that the **Type** field is set to **Issue**.

1. Enter the following title:

   ```prompt
   Add Featured Products Styling to Homepage
   ```

1. At the bottom of the description box, select `Switch to plain text editing` to enter markdown editing mode.

1. Paste the following markdown text into the issue description field:

   ```markdown
   ## Add Featured Products Styling to Homepage

   ### Description
   The homepage currently displays the first six products from the database without any visual distinction. We should add special styling to highlight featured products and improve the shopping experience.

   ### Requirements
   - Style featured products with a special badge and border to distinguish them from regular products
   - Ensure the section is responsive and looks good on mobile devices
   - Featured products should still be clickable and add-to-cart functional

   ### Acceptance Criteria
   - Featured products have a visual indicator (badge and border)
   - All featured products are clickable and functional
   - The layout is responsive on mobile devices
   - No console errors or warnings
   ```

1. Click **Create issue**.

### Expected Output: Task A

- The GitLab Swag Shop Flows project exists in your namespace with the pre-built file structure visible in the repository.
- Seven foundational flows are enabled under **Settings > General > GitLab Duo features**.
- The Pages URL opens the live Swag Shop with no featured products on the homepage.
- The agent created an issue from the markdown text.

## Task B: Use a Foundational Flow to Create a Merge Request

### Task B.1: Trigger the Foundational Flow

With the issue created, you can now invoke the foundational flow directly from the issue view. GitLab Duo will read the issue description, analyze the codebase, and generate a merge request with the appropriate code changes. There's no manual branch creation or coding required.

1. Open the **Add Featured Products Styling to Homepage** issue. This is the issue that you created earlier in this lab.

1. Click the **Generate MR With Duo** button. This process will take several minutes to complete.

### Task B.2: Verify Session Completion

1. The session should automatically open in the right panel. You can also navigate to **Automate > Sessions** and find your session.

1. Click the session to open it and confirm that the activity feed reports a summary of the actions taken to complete the task.

### Task B.3: Review the Merge Request

With the agent session complete, open the merge request and review what the agent produced. You are not merging yet. This step is about understanding the changes before the code review runs.

1. Navigate to **Code > Merge requests** and open the merge request created by the agent.

1. Select the **Changes** tab to review all files modified or created by the agent.

1. Select the **Pipelines** tab and wait for the pipeline to complete all validation stages and confirm all checks pass.

The pipeline runs a build, test, and deploy to Pages. All three must pass before merging. Confirm everything is green before proceeding.

### Expected Output: Task B

- The merge request is visible under **Code > Merge Requests** and is attributed to GitLab Duo.
- The Activity tab under **Automate > Sessions** shows a step-by-step log of what the agent did.
- The pipeline on the merge request is passing green across all stages.

## Task C: Trigger the Code Review Flow

Before triggering the code review, you need to mark the merge request as ready. The Code Review Flow only runs on merge requests that are out of draft status. Draft MRs signal that work is still in progress and are excluded from review workflows.

### Task C.1: Mark the Merge Request as Ready

1. Navigate to **Code > Merge Requests** and open the merge request created in Task B.

1. Select the **Overview** tab.

1. Scroll down and click **Mark as ready**.

    >**Why draft status?** GitLab Duo creates merge requests in draft status by design. Draft merge requests signal to your team that work is in progress and should not be merged yet. They are excluded from merge queues and auto-merge rules. Marking it as ready is your explicit confirmation that the changes have been reviewed. This is the human-in-the-loop principle: the agent generates, you decide.

### Task C.2: Assign GitLab Duo as a Reviewer

1. On the merge request overview page, locate the **Reviewers** section in the right sidebar.

1. Click **Edit** next to Reviewers and search for GitLabDuo. Select it to assign **GitLab Duo** as a reviewer.

    >**Alternative trigger:** You can also trigger the Code Review Flow by typing /assign_reviewer @GitLabDuo in any comment box on the merge request.

### Task C.3: Review the Code Review Output

1. From the **Overview** tab, scroll to the **Activity** section.

1. Observe the comments in real time.

    >**What you're seeing:** GitLab Duo Code Review automatically reviews your merge request when requested as a reviewer. It analyzes the changes in the diff and posts a summary comment describing what it found, along with inline suggestions directly on the affected lines of code. The suggestions focus on things like code quality, maintainability, and best practices. In this case, it flagged hardcoded values that should use design tokens and a missing CSS property for proper layering.

1. Read through the comments posted by GitLab Duo. For each one, consider whether you agree with the suggestion and how you would act on it before merging.

### Expected Output: Task C

- GitLab Duo appears in the Reviewers section of the merge request.
- At least one comment from GitLab Duo is visible on the merge request **Overview** tab.

## Task D: Review and Merge the Merge Request

You are now ready to merge. This is your explicit sign-off that the changes have been reviewed and are ready for the main branch.

### Task D.1: Review and Merge

1. Navigate to **Code > Merge Requests** and open the merge request.

1. Navigate back to the **Overview** tab.

1. Select the **Merge** button.

### Task D.2: View the Updated Application

With the changes merged, the pipeline will run and deploy the updated application to Pages.

1. Navigate to **Build > Pipelines** and find the merge pipeline.

1. Wait for the pipeline to complete.

1. Return to the Swag Shop browser tab and refresh the page.

1. Confirm the featured products now have a Featured badge and new border on the homepage.

### Expected output: Task D

- The merge request status shows **Merged** and the linked issue is closed.
- The Swag Shop homepage shows a Featured badge and border on featured products.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabdaphandson/).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
