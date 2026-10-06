---
title: "GitLab Duo Principles - Hands-On Lab: GitLab Duo Agent Platform"
description: "This Hands-On Guide walks you through using GitLab Duo Agent Platform to process complex topics."
---

## Objectives

By the end of this lab, you will learn how to:

- Configure and operate GitLab Duo Agent Platform
- Automate issue and merge request creation using AI agents
- Implement AI-assisted project planning and analysis

> Estimated time to complete: 15 minutes

## Task A: Create issues and Merge Requests through Duo Agentic Chat

1. On the top of your screen, select **+ > New project/repository**.

1. Select the **Create from template** tile.

1. Select the **Group** tab.

1. Select the **GitLab Learn Labs / Sample Projects** to open it.

1. Select **Use template** next to the **DAP Swag Shop** template. You may find it on Page 3.

1. In the Project name field, enter **DAP Demo**.

1. In the Project URL field, select your **group** from the dropdown list (not your user).

1. Leave everything else as default and select **Create project**

      > Throughout this workshop, you will get Agentic AI-generated support from GitLab Duo Chat.

1. In the upper-right corner, select the GitLab Duo Chat icon.

1. Select the GitLab Duo agent. If you are already using the GitLab Duo agent, click **Current GitLab Duo Chat**.

      **NOTE:** If you didn't get the option of choosing the agent, it is probably because you are not using Agentic chat. If this is the case, simply click on the `Agentic` slider just above the input field to activate Agentic chat. Then repeat the step above.

1. Type `/reset` to clear the context.

1. Copy and paste the following prompt into chat:

      ```prompt
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

1. If you are asked to `Approve` an action Duo Chat wants to execute, please do so.

      > Duo Chat will create issues, merge Request on existing branches for us, so that we have a project setup we can work with. It will be around 9 approvals you need to give. You are the HITL (Human in the Loop). Then you will see as a closing statement a `Completion Report`

1. Once the Flow completes, view your issues and merge requests to see the tasks have been completed.

Let's explore how GitLab Duo Chat can act as an intelligent agent to help with various development tasks:

## Task B. Ask Duo Chat to analyze your current project

1. Using the right hand navigation options click the **Add New Chat** button, and select **GitLab Duo** as the agent we want to converse with.

1. In the new chat window ask the following prompt:

      ```prompt
      Analyze this project's structure and suggest improvements for maintainability and scalability
      ```

1. Follow up after you read the output with this prompt:

      ```prompt
      Create an issue in this project based on your recommendations.
      ```

1. Approve the Tool usage and read the issue Duo has created.

1. Edit the Assignees section, and assign the issue to yourself.

1. Select the **Add new chat** button, and select the **Planner** agent.

1. Prompt the agent with the following:

      ```prompt
      Give me the Quick Wins for this project.
      ```

1. We see how AI understands the entire project context and prioritizes our work. Let us follow those recommendations of the agent, and continue working with our agent by typing in this prompt:

      ```prompt
      Give me the link to the item in Priority 1.
      ```

## Task C. Review the state of your project issues

1. Open `Plan > Work items` using the menu on the left. You get a list with existing issues.

1. In the upper-right corner, click the **Add New Chat** icon and select the **Planner** Agent. During this workshop we will be taking advantage of our new Agentic AI features, so make sure **Agentic mode** is still selected.

1. Prompt them with:

      ```prompt
      Which issues are missing estimates, due dates or assignees?
      ```

      Observe the results, which help you and your team to get a better grip on your project state.

## Task D. Explore Duo Chat for Development Tasks

Let's explore how Duo Chat can assist with various development planning and analysis tasks.

1. Click the **Add new chat** icon in the upper-right corner and select the **GitLab Duo** Agent. Make sure **Agentic mode** is still selected.

1. Try asking Duo about testing strategies for your project:

      ```prompt
      Recommend a comprehensive testing strategy for this application, including unit, integration, and end-to-end tests
      ```

1. Get performance insights:

      ```prompt
      Analyze this Python application for potential performance bottlenecks and suggest optimizations. Output suggestions in chat.
      ```

1. Ask about deployment approaches:

      ```prompt
      What would be the best deployment strategy for this Python application? Include considerations for scaling and monitoring.
      ```

1. Explore modernization recommendations:

      ```prompt
      How can I modernize this Python application to use current best practices and frameworks?
      ```

## Optional: Further Practice

Feel free to try out more of what Duo can do for you. For example, create a detailed issue with an implementation plan:

```prompt
Create an issue with implementation plan for adding a product carousel to the swag shop.

Requirements:
- Horizontal carousel for product articles with prev/next navigation and touch support
- Show product image, title, price, and CTA button per item
- Responsive, accessible (ARIA, keyboard nav)
- Use existing tech stack, minimal dependencies

Issue should include:
- User story
- Acceptance criteria
- Technical implementation plan broken into subtasks
- Estimated effort per task
- Testing requirements
```

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/devsecopswithduo).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
