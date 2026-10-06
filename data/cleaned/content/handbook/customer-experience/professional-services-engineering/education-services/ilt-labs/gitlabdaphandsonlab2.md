---
title: "GitLab Duo Agent Platform - Hands-On Lab: Use Agentic Chat to Create an Issue"
description: "This Hands-On Guide walks you through the basics of using GitLab Agent Platform"
---

> Estimated time to complete: 30 minutes

## Learning Objectives

By the end of this lab, you will be able to:

- Configure and operate GitLab Duo Agent Platform with Agentic Chat.
- Inspect a project runbook file to understand pre-planned work items before creating them.
- Automate issue and merge request creation using AI agents.
- Implement AI-assisted project planning and analysis.

## Overview

Agentic Chat puts you in direct control. Every write action requires your approval before it executes. Where Lab 1 showed you what a foundational flow can do on its own, this lab puts you in the driver's seat.

The fix from Lab 1 merged cleanly, but the issue that triggered it had no acceptance criteria, no assignee, no estimate. The backlog is worse; most issues are missing the same things, and there's a runbook that was never acted on.

In this lab, you will use agentic chat to work through the backlog: creating issues, linking merge requests, closing gaps. It will be clean by the end. But cleaning it manually is reactive. It won't stay clean on its own.

## Task A: Inspect the Runbook, and Create Issues and Merge Requests

### Task A.1: Inspect the Runbook

Before you ask Agentic Chat to create anything, take a moment to read the file it will use as its source of truth. This gives you full context for what is about to be created and why, making the approval steps that follow much easier to evaluate.

1. Navigate to your **GitLab Swag Shop Flows** project.

1. In the left sidebar, select **Code > Repository**.

1. Navigate to the `RunBooks` folder and open the file **issues_and_mrs_lvl-101.json**.

1. Read through the file. Note the following for each item in the issues array:

      - **title** and **description:** These become the issue content.
      - **source_branch:** This is the branch name the agent will create.
      - **mr_title** and **mr_description:** These become the merge request.
      - **add_note:** One item has `add_note` set to true. For that item, the agent will post a comment on the MR after creating it. The others are set to false, so they will not have a comment added.

### Task A.2: Run the Agentic Chat Prompt

With the runbook contents in mind, you are now ready to ask agentic chat to create the issues, branches, and merge requests defined in that file.

1. Navigate to your **GitLab Swag Shop Flows** project.

1. In the right toolbar, click the **Add New Chat** icon and select **GitLab Duo**. Confirm agentic mode is on.

1. Copy and paste the following prompt into the chat, and click the **Submit** button:

      ```markdown
      Read the file `RunBooks/issues_and_mrs_lvl-101.json` and create GitLab issues and merge requests.

      **RULES:**
      - Process items sequentially - finish one completely before starting the next
      - Once an issue is created, move on (do NOT recreate)
      - Skip labels entirely (not supported)

      **For each item in "issues" array:**
      1. **Create Issue** - use "title" and "description" fields
      2. **Create Branch** - use exact "source_branch" name, base from main
      3. **Create MR** - use "mr_title", "mr_description" + "Closes #<issue_iid>", target main
      4. **Add Note** - only if "add_note" is true, use "note_content"

      **Expected Result:**
      - 3 issues
      - 3 branches
      - 3 MRs (each linked to its issue)
      - 1 note on the third MR

      **After completion, report:**
      - Each issue IID and URL
      - Each MR IID, URL, and linked issue
      - Any errors encountered
      ```

1. Each time Agentic Chat requests approval, click **Approve** to continue.

      > **Approvals explained:** You will approve approximately 10 actions in total, which are all write actions. Because you have already read the runbook, you can confirm each action matches what you expected. Read actions happen silently in the background without interrupting you.

1. When complete, agentic chat will display a Completion Report listing each issue's IID, Merge Request IID, and any errors encountered.

      > **Note:** IID, or Internal ID, is GitLab's internal identifier for issues and merge requests within a specific project.

### Task A.3: Verify Agentic Chat Output

Confirm that the agent completed all expected actions by checking for the issues, merge requests, branches, and comments it created.

1. Navigate to **Plan > Work items** and confirm three issues have been created.

      >**Note:** You will see three issues in your project that were created by Duo Agentic chat. If the new issues are not yet visible, manually refresh the page.

1. Navigate to **Code > Merge Requests** and confirm three merge requests have been created, each linked to its corresponding issue.

1. Open the merge request **fix: improve text contrast on product cards for WCAG compliance** and confirm a comment has been added.

1. Navigate to **Code > Branches** and confirm three new branches are visible.

      > **Note**: To verify that a merge request is linked to an issue, open the merge request Overview tab and look for `Closes <issue-id>` in the description.

### Expected Output: Task A

- Three new issues exist under **Plan > Work items**, each with a title and description from the runbook.
- Three merge requests exist under **Code > Merge Requests**, each linked to its corresponding issue.
- Three branches are visible under **Code > Branches**.
- One comment is posted to the **fix: improve text contrast** merge request.
- A Completion Report is visible in the agentic chat panel with all IIDs and URLs.

## Task B: Analyze Your Project and Create an Issue

Agentic chat can read your project's structure, generate tailored recommendations, and then act on them immediately. In this task, you will ask it to analyze the project and create an issue based on what it finds.

1. Click **Add New Chat** and select **GitLab Duo**. Confirm Agentic mode is on.

1. Enter the following prompt:

      ```prompt
      Analyze this project's structure and suggest improvements for maintainability and scalability.
      ```

1. Review the recommendations returned by agentic chat.

1. Follow up in the same conversation with:

      ```prompt
      What are the quick wins that I should prioritize first?
      ```

1. Review the prioritized recommendations.

1. Follow up with:

      ```prompt
      Create an issue in this project based on your recommendations.
      ```

1. When agentic chat presents the issue for approval, click **Approve**.

1. Open the newly created issue and edit the **Assignees** field to assign it to yourself.

>**Tip:** The context from your earlier prompts carries into each follow-up. You do not need to repeat the analysis. Agentic chat remembers what it found within the same conversation.

### Expected Output: Task B

- A structured analysis is visible in the chat panel.
- A prioritized list of quick wins is available in the same conversation.
- A new issue exists under **Plan > Work items** with a title and description derived from the analysis, assigned to yourself.

## Task C: Review Project Health with the Planner Agent

The Planner Agent combines product management expertise with knowledge of GitLab's planning features. In this task you will use it to identify gaps in your backlog and resolve them directly from chat.

1. Navigate to **Plan > Work items** using the left sidebar.

1. Click **Add New Chat** and select **Planner**. Confirm Agentic mode is on.

1. Enter the following prompt:

      ```prompt
      Which issues are missing estimates, due dates, or assignees?
      ```

1. Review the results. The issues created in Tasks A and B should appear in this list. They were not given estimates or due dates during creation.

1. Follow up in the same conversation with:

      ```prompt
      Assign all of these issues to me.
      ```

1. When agentic chat requests approval, click **Approve**.

1. Open one of the flagged issues and confirm you are now listed as the assignee.

1. Return to agentic chat and re-run the original prompt:

      ```prompt
      Which issues are missing estimates, due dates, or assignees?
      ```

1. Review the updated results and confirm the assignee gap has been resolved.

      >**Note:** Estimates and due dates will still be flagged as missing — that is expected. Only the assignee gap was addressed in this task.

### Expected Output: Task C

- A structured list of issues flagged for missing information is visible in the chat panel.
- All flagged issues are assigned to yourself following the approval step.
- The re-run prompt returns an updated list that no longer flags assignee as a missing field.

## Task D: Explore Agentic Chat for Development Planning

Agentic Chat can do more than create issues and merge requests. In this task, you will use it to explore development planning and testing strategy. Notice how the agent draws on your project's actual context to generate specific, relevant recommendations rather than generic advice.

### Task D.1: Request a Testing Strategy

1. Click **Add New Chat** and select **GitLab Duo** from the agent dropdown list. Confirm that Agentic mode is enabled.

1. Enter the following prompt:

      ```prompt
      I want to reduce my change failure rate over time. What testing strategy should I implement?
      ```

1. Review the output. The agent will analyze your project's structure and return a testing strategy tailored to your codebase.

1. Follow up with additional questions to go deeper. For example:

      ```prompt
      Which of these would have the most impact for a project this size?

      Can you show me which files would need to change to implement this?
      ```

### Task D.2: Try Additional Planning Prompts

This step sends you to the GitLab Duo Prompt Library. Practice using it as your go-to starting point for Agentic Chat.

1. Navigate to the [GitLab Duo Prompt Library](https://about.gitlab.com/gitlab-duo/prompt-library/).

1. Filter category by **Planning & Architecture**.

1. Browse the available prompts and copy one that is relevant to your project or team context.

1. For each prompt, check the recommended agent shown on the prompt card. Open a new chat and select that agent before pasting the prompt.

1. Paste the prompt as is or adapt it for the DAP Swag Shop project.

1. Review the output and notice how the agent references your project's actual context rather than returning generic advice.

> **Tip:** Each prompt card shows the recommended agent, complexity level, and Software Development Life Cycle (SDLC) stage. Use these tags to find prompts that match where you are in your workflow.

### Expected Output: Task D

- The testing strategy prompt returns recommendations specific to the Swag Shop's tech stack and file structure.
- At least one Prompt Library response references a specific file, pattern, or convention from the project rather than generic advice.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabdaphandson/).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
