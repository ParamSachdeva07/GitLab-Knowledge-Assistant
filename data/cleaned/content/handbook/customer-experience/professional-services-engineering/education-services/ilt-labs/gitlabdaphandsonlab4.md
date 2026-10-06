---
title: "GitLab Duo Agent Platform - Hands-On Lab: Create a Custom Flow"
description: "This Hands-On Guide walks you how to create a custom flow"
---

> Estimated time to complete: 20 minutes

## Learning Objectives

By the end of this lab, you will be able to:

- Configure and create a custom flow using YAML.
- Enable a custom flow at group and project level.
- Trigger a custom flow on a live issue and review the output.

## Overview

In Lab 3, you built a custom agent, which is a tool you invoke on demand through a prompt. A custom flow is different. It's a YAML-defined, event-driven workflow that runs automatically once triggered, without any human prompt required.

New issues are already coming in with the same gaps the Planner Agent flagged in Lab 2. The feedback needs to arrive automatically, before anything reaches a sprint, not after someone manually runs a check.

In this lab you will build the Swag Shop Issue Reviewer: a custom flow that evaluates every issue it's assigned to and posts structured feedback automatically. Issue quality becomes something the system enforces, not something the team has to remember.

## Task A: Create a Custom Flow

### Task A.1: Configure the Flow

1. Navigate to your **GitLab Swag Shop Flows** project.

1. In the left sidebar, select **Automate > Flows**.

1. Select **New flow**.

1. In the **Display name** field, enter `Swag Shop Issue Reviewer`.

1. In the **Description** field, enter:

   ```prompt
   This Issue Reviewer assists in checking your issues for completeness, and suggests improvements to ensure high-quality issues.
   ```

1. Under **Visibility**, select **Private**.

### Task A.2: Add the Flow Configuration

The flow configuration is defined in YAML. This is where you specify the components the flow uses, how they connect, and what it produces as output. The configuration below defines two components: a step that fetches the issue, and an agent that reviews it and posts a comment.

Don't worry about understanding every line right now. The key things to note are:

- `fetch_issue`: Retrieves the issue data using the get_issue tool.
- `issue_reviewer`: An agent component that reads the issue data and posts a structured comment using the create_issue_note tool.
- `issue_review_prompt`: The system prompt that defines how the agent evaluates and scores the issue.

1. Under **Configuration**, click the **Clear editor** button.

1. Paste the following YAML into the editor:

      ```yaml
      version: "v1"
      environment: ambient

      components:
        - name: "fetch_issue"
          type: DeterministicStepComponent
          tool_name: "get_issue"
          inputs:
            - from: "context:project_id"
              as: "project_id"
            - from: "context:goal"
              as: "issue_iid"
          ui_log_events:
            - "on_tool_execution_success"
            - "on_tool_execution_failed"

        - name: "issue_reviewer"
          type: AgentComponent
          prompt_id: "issue_review_prompt"
          inputs:
            - from: "context:fetch_issue.tool_responses"
              as: "issue_data"
            - from: "context:project_id"
              as: "project_id"
            - from: "context:goal"
              as: "issue_iid"
          toolset:
            - "create_issue_note"
          ui_log_events:
            - "on_tool_execution_success"
            - "on_tool_execution_failed"
            - "on_agent_final_answer"

      prompts:
        - prompt_id: "issue_review_prompt"
          name: "Issue Review Prompt"
          unit_primitives: []
          prompt_template:
            system: |
              You are a helpful project management assistant integrated into GitLab.
              Your job is to review a GitLab issue for completeness and quality, then post
              a single constructive public comment with improvement suggestions.

              Evaluate the issue against these criteria:
              - Has a clear, detailed description (not empty or vague)
              - Has defined acceptance criteria
              - Has at least one label applied
              - Has an assignee
              - Has a milestone or due date
              - Title is specific and descriptive

              Steps you must follow:
              1. Review the issue data provided to you
              2. Evaluate it against every criterion above
              3. Post exactly one public comment on the issue (project_id: {{project_id}}, issue_iid: {{issue_iid}}) using this structure:

              ## Issue Review

              **Completeness Score: X/6**

              ### Looks good
              - <list criteria that are met>

              ### Needs attention
              - <list criteria that are missing, with a specific suggestion for each>

              ### Suggested acceptance criteria (if missing)
              <only include this section if acceptance criteria are absent>

              ---
              *This review was automatically generated. Please review and apply relevant suggestions.*

              If the issue scores 5 or higher out of 6, open the comment with a positive note.
              If it scores below 3, add a note encouraging the author to refine before development begins.
              Keep the tone friendly, constructive, and concise.
            user: |
              Here is the issue data to review:
              {{issue_data}}

              Post your review as a comment on project_id {{project_id}}, issue IID {{issue_iid}}.
            placeholder: history
          params:
            timeout: 180

      routers:
        - from: "fetch_issue"
          to: "issue_reviewer"
        - from: "issue_reviewer"
          to: "end"

      flow:
        entry_point: "fetch_issue"
      ```

1. Select **Create flow** to save.

### Understanding the Flow Configuration

Now that the flow is saved, take a few minutes to understand what you just configured. The YAML defines three things: the components that do the work, the prompt that drives the agent, and the router that connects them.

#### The Version and the Environment

Every flow begins with a version and environment declaration:

```yml
version: "v1"
environment: ambient
```

The version defines what version of the flow YAML configuration you are using. You will always set this to `v1`. For `environment`, there are three possible values: `chat`, `chat-partial`, and `ambient`. Details for these fields can be found in the [YAML specification](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/blob/main/docs/flow_registry/v1.md#environment). For this example, we've selected `ambient`, which is designed for hands-off experiences, where the assignment is completed by the agent in the background.

#### The Components

Components are reusable building blocks that perform a specific task in your flow. We've defined two components: `fetch_issue` and `issue_reviewer`.

Each component has a [component type](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/blob/main/docs/flow_registry/v1.md#component-types), which defines how the component behaves. To start, let's consider the `fetch_issue` component.

```yml
components:
  - name: "fetch_issue"
    type: DeterministicStepComponent
    tool_name: "get_issue"
    inputs:
      - from: "context:project_id"
        as: "project_id"
      - from: "context:goal"
        as: "issue_iid"
    ui_log_events:
      - "on_tool_execution_success"
      - "on_tool_execution_failed"
```

The `fetch_issue` component is a `DeterministicStepComponent`. This means that it executes a single step in a deterministically with predetermined arguments. The `tool_name` field defines what tool the component uses. In this case, the component will use `get_issue` to get details about an issue. The `inputs` define what data the component should use to accomplish its task. In this case, it gets a project ID, as well as an issue IID. The `as` keyword is an alias, to provide an easy to read name for each input. Finally, the `ui_log_events` determine what events should be logged in the UI. In this case, execution success and failure are logged.

Next, we can look at the `issue_reviewer` component.

```yml
  - name: "issue_reviewer"
    type: AgentComponent
    prompt_id: "issue_review_prompt"
    inputs:
      - from: "context:fetch_issue.tool_responses"
        as: "issue_data"
      - from: "context:project_id"
        as: "project_id"
      - from: "context:goal"
        as: "issue_iid"
    toolset:
      - "create_issue_note"
    ui_log_events:
      - "on_tool_execution_success"
      - "on_tool_execution_failed"
      - "on_agent_final_answer"
```

Our `issue_reviewer` component is an `AgentComponent`. An `AgentComponent` uses a LLM to process inputs and generate responses. Like our previous component, we provide a set of inputs to use. In this case, the `create_issue_note` toolset is used, which will create an issue note. We log tool success, failure, as well as the final answer produced by the component. Since this component uses an LLM, we provide a prompt to use, defined by the `prompt_id` field. The prompt associated with this ID is defined below.

#### The Prompt

Each prompt is given a prompt ID. You will see our prompt has an ID of `issue_review_prompt`, which matches the prompt ID given to the `issue_reviewer` component.

Next, we define our prompt. The `system` field defines the prompt to define the agent behavior and personality. The `user` field defines where the user prompt is placed, as well as how to interpret it. Setting the `placeholder` field to `history` allows for previous chat history to be included in the flow prompt. Finally, we provide a timeout, in this case, 180 seconds.

#### The Router

The `router` and `flow` fields provide details on how data flows from start to finish.

```yml
routers:
  - from: "fetch_issue"
    to: "issue_reviewer"
  - from: "issue_reviewer"
    to: "end"

flow:
  entry_point: "fetch_issue"
```

The `flow` defines an entry point, in this example, `fetch_issue`. The `router` defines what actions to take from there. We can see that the flow starts at `fetch_issue`, then feeds into `issue_reviewer`, then moves to `end` finishing the flow.

Custom flows provide a large amount of customization. To learn more, refer to [YAML specification and documentation](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/blob/main/docs/flow_registry/v1.md#flow-registry-framework-v1-version-documentation).

### Task A.3: Enable the Custom Flow

Enabling the flow at the group level makes it available to all projects within your group. It's the same process you used to enable the custom agent in Lab 3.

1. From the same page that you have created your flow, click **Enable** in the upper-right corner.

1. Deselect the 'Assign Reviewer' option, as this is not relevant to this issue-based flow.

1. Then, click **Enable** again to confirm.

  >**Note:** The two-step confirmation ensures you do not accidentally publish a flow before it is ready. The first click opens a confirmation prompt; the second click commits the enablement.

### Expected Output: Task A

- A new flow named **Swag Shop Issue Reviewer** exists under **Automate > Flows**.
- The flow configuration is saved with the YAML above and visibility set to Private.
- The flow is enabled at the group level.

## Task B: Use the Custom Flow

At this point you have a configured and enabled flow. In this task you will trigger it on an existing issue and observe how it automates the review process.

1. Navigate to your **GitLab Swag Shop Flows** project.

1. In the left sidebar, select **Plan > Work items**.

1. Select an existing open issue.

1. In the **Assignees** section of the issue, assign the **Swag Shop Issue Reviewer** flow. You might need to scroll down to find it.

    > **Why assign a flow in the Assignees field?** Flows are triggered by GitLab events. For this flow, the trigger event is being assigned to an issue, the same mechanism used to assign a person. When you select the flow in the Assignees field, GitLab fires the trigger event and the flow begins executing automatically.

1. A comment will appear on the issue confirming that a new flow session has begun, with a link to the session progress.

    >**Note:** You can also navigate to **Automate > Sessions**, locate the session for the Swag Shop Issue Reviewer, and open it.

1. Return to the issue and review the comment posted by the flow.

The comment will contain a completeness score out of 6, a "Looks good" section listing criteria that are met, a "Needs attention" section with specific suggestions for each missing criterion, and optionally a "Suggested acceptance criteria" section. The score will vary depending on which issue you chose.

  >**Note:** The flow may take a few minutes to complete. If the comment has not appeared after the session shows Finished, refresh the issue page.

### Expected Output: Task B

- The Swag Shop Issue Reviewer flow is assigned to the issue in the Assignees field.
- A flow session is visible under **Automate > Sessions** with a status of Finished.
- A structured comment is posted on the issue containing a completeness score, a Looks good section, and a Needs attention section with specific suggestions.

## Lab Guide Complete

You have completed this lab exercise. You can view the other [lab guides for this course](/handbook/customer-experience/professional-services-engineering/education-services/ilt-labs/gitlabdaphandson/).

## Suggestions?

If you wish to make a change to this lab, please submit your changes through a Merge Request.
