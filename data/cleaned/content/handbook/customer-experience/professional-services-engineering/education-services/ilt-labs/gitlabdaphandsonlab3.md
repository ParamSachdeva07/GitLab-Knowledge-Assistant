---
title: "GitLab Duo Agent Platform - Hands-On Lab: Build a Custom Agent"
description: "This Hands-On Guide walks you how to create a custom agent"
---

> Estimated time to complete: 15 minutes

## Learning Objectives

By the end of this lab, you will be able to:

- Configure and create a custom GitLab Duo Agent.
- Enable a custom agent at the group and project level.
- Use a custom Duo Agent to perform tasks.

## Overview

Sometimes the right agent for your team doesn't exist yet. Custom agents let you define exactly what an agent knows, what it can do, and who can access it — built for your codebase and your team's specific needs.

Every question since joining has required interrupting someone. There's no good way to ask about the codebase without pulling a teammate away. You decide to fix that and build a tool for the next person who joins.

In this lab, you will build the Swag Shop Onboarding Agent: a custom agent that knows the project, answers questions, and creates issues when a new developer finds something worth fixing.

## Task A: Create a Custom Agent

In this task, you will configure the Swag Shop Onboarding Agent from scratch. Every decision you make here, such as what the agent knows, what it can do, and who can access it, directly shapes how it behaves in Task C.

>**Two ways to create a custom agent:** Custom agents can be created from within a project (Automate > Agents) or directly from the AI Catalog. In this lab you will use the project path, which is the right choice when building and testing for a specific codebase. Use the AI Catalog path when deploying org-wide or enabling an agent someone else built.

1. Navigate to your **GitLab Swag Shop Flows** project.

1. In the left sidebar, select **Automate > Agents**.

1. Select **New agent**.

1. In the **Display name** field, enter `Swag Shop Onboarding Agent`.

1. In the **Description** field, enter:

      ```prompt
      Helps new developers get up to speed on the DAP Swag Shop codebase, answers questions about the project architecture, and creates issues for improvements or bugs they discover while onboarding.
      ```

      > **Note:** The description appears in the AI Catalog and in the agent dropdown list in agentic chat. It helps teammates understand what the agent does and when to use it. Keep it concise and specific.

1. For **Visibility**, select **Private**.

      > **Why private?** Start with private visibility while you test your agent. A private agent is only accessible within your project and group. Once it is proven and ready to share with other teams, you can switch it to public and it will become discoverable in the AI Catalog.

1. In **Configuration**, search for and select **Create Issue** in the Tools dropdown list.

      >**Why only one tool?** Selecting only the tools your agent actually needs is the principle of least privilege in practice. Your onboarding agent needs to create issues, but it does not need access to pipelines, merge requests, or code. Granting unnecessary tools increases risk without adding value. Start with fewer tools and add more only when a specific need arises.

1. In the **System prompt** section, enter the following:

      ```markdown
      You are the Swag Shop Onboarding Agent for the DAP Swag Shop project.

      Your responsibilities:

      1. Help new developers understand the project structure and architecture
      2. Answer questions about how the codebase works (Python/Flask, templates, CSS)
      3. Explain development workflows, testing, and CI/CD pipelines
      4. Create issues when developers identify bugs or suggest improvements

      When creating issues:
      - Use label "good first issue" for simple fixes new developers could tackle
      - Use label "documentation" for documentation improvements
      - Use label "bug" for bugs discovered during onboarding
      - Include clear context and acceptance criteria

      Restrictions:
      Do not modify code, merge requests, or pipeline configurations.
      Be friendly and encouraging. Remember that new team members may not know GitLab or this codebase well yet.
      ```

1. Select **Create agent**.

### Expected Output: Task A

- A new agent named **Swag Shop Onboarding Agent** is visible under **Automate > Agents**.
- Visibility is set to **Private**.
- **Create Issue** is listed as the only configured tool.
- The system prompt is saved and visible in the agent configuration.

## Task B: Enable the Agent at Group Level

Before you can use the agent in your project, it needs to be enabled at the group level. Group-level enablement makes the agent available to all projects within the group, not just the one you created it in.

1. From the same page that you have created your agent, click **Enable** in the upper-right corner.

1. Then, click **Enable** again to confirm.

      > **Note:** The two-step Enable confirmation ensures you do not accidentally publish an agent before it is ready. The first click opens a confirmation prompt; the second click commits the enablement.

### Expected Output: Task B

- The agent is visible under **Automate > Agents** at the project level.

## Task C: Use the Agent to answer Questions and Create Issues

In this task, you will interact with the agent as a new developer would, testing how well it understands the project and whether it can take action on your behalf.

### Task C.1: Use the Agent in a Live Session

1. Select the **New chat** icon to start a new chat session.

1. Select **Swag Shop Onboarding Agent** from the agent dropdown list.

      >**Note:** If you do not see this agent, try refreshing your page.

1. Enter the following prompt:

      ```prompt
      I'm new. What's something I could help contribute to on this project?
      ```

1. Review the agent's response.

      **What to look for:** The response should reflect the system prompt you wrote in Task A. The tone should be friendly and encouraging. The suggestion should reference the actual project — Python/Flask, templates, CSS — not generic onboarding advice. It should not offer to modify code or pipelines because you explicitly restricted that.

1. Now ask the agent to create an issue. Enter the following prompt:

      ```prompt
      Create an issue for me to help onboard and start contributing to help the team.
      ```

1. The agent will present a tool call for your approval. Review the title, description, and label, then click **Approve**.

1. Navigate to **Plan > Work items** and open the newly created issue.

### Task C.2: Verification

Confirm the following before marking this task complete:

- The issue title clearly describes the contribution or task.
- The issue description includes context explaining why the work is needed.
- The issue description includes acceptance criteria.
- The appropriate label has been applied (`good first issue`, `bug`, or `documentation`).

### Expected Output: Task C

- The Swag Shop Onboarding Agent is selectable from the agent dropdown list in agentic chat.
- A response from the agent references the project's actual structure and suggests a specific first contribution.
- A new issue exists under **Plan > Work items** with a descriptive title, full description, acceptance criteria, and appropriate label.
- The agent's behavior reflects the system prompt: friendly tone, project-specific knowledge, and no offers to modify code or pipelines.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabdaphandson/).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
