---
title: "GitLab Duo Tips"
---

Learn how to use GitLab Duo Agent Platform for AI orchestration across the entire software lifecycle: Agentic Chat, specialized agents, flows, Code Suggestions, and the GitLab MCP server.

## Access

- Team members: If GitLab Duo is not available in your group, create a [Compass ticket](/handbook/eta/corporate-it/compass/compass-guide/#how-to-get-help-3-ways-to-reach-compass).
- Community contributors: Request community forks access on [contributors.gitlab.com](https://contributors.gitlab.com/). After approval, you can [use GitLab Duo](https://docs.gitlab.com/development/contributing/first_contribution/) for your contributions.

Follow the [Get started with the GitLab Duo Agent Platform](https://docs.gitlab.com/user/get_started/get_started_agent_platform/) documentation to onboard.

## GitLab Duo in IDEs and CLI

For IDE integration through GitLab Duo extensions, follow the [editor extensions documentation](https://docs.gitlab.com/editor_extensions/#available-extensions).

On the terminal, use the [GitLab Duo CLI](https://docs.gitlab.com/user/gitlab_duo_cli/).

## Resources

- [GitLab Duo Agent Platform documentation](https://docs.gitlab.com/user/duo_agent_platform/)
  - [Get started](https://docs.gitlab.com/user/get_started/get_started_agent_platform/)
  - [GitLab Duo Agentic Chat](https://docs.gitlab.com/user/gitlab_duo_chat/agentic_chat/)
  - [Foundational flows](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/)
  - [Code Suggestions](https://docs.gitlab.com/user/duo_agent_platform/code_suggestions/)
- [GitLab MCP server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) to connect AI tools to GitLab, and [GitLab MCP clients](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_clients/) to connect GitLab Duo to external MCP servers
- [GitLab Duo documentation](https://docs.gitlab.com/user/gitlab_duo/)
  - [Use cases](https://docs.gitlab.com/user/gitlab_duo/use_cases/)
  - [GitLab Duo Non-Agentic Chat](https://docs.gitlab.com/user/gitlab_duo_chat/)
- [Editing the handbook](/handbook/about/editing-handbook/) with GitLab Duo workflows for handbook changes
- [GitLab University](https://university.gitlab.com)
  - [AI and GitLab Duo courses](https://university.gitlab.com/learn/dashboard?labels=%5B%22Topic%22%5D&values=%5B%22AI%22%5D)
  - [GitLab Duo Enterprise learning path](https://university.gitlab.com/learn/learning-path/gitlab-duo-enterprise-learning-path)
- [Developer Advocacy resources](/handbook/marketing/product-and-technical-marketing/developer-advocacy/)
  - [Content library](/handbook/marketing/product-and-technical-marketing/developer-advocacy/content/) with GitLab Duo demos, use cases, product tours, talks, workshops, recordings, etc.
  - [Development environments](/handbook/marketing/product-and-technical-marketing/developer-advocacy/dev-environments/) for IDEs, CLI, and AI tool setups
- [Highspot: Field guide](https://gitlab.highspot.com/items/6459a4f9a583c8ebe9aa5a64) (internal only, field teams)
- Dogfooding: [Developing GitLab Duo blog tutorial series](https://about.gitlab.com/blog/2024/06/03/developing-gitlab-duo-series/)

## Tips

GitLab Duo Agentic Chat can answer many questions about GitLab, programming languages, technology and more. Practice how to ask questions and create follow-up conversations, instead of opening multiple browser search tabs. Explore, experiment, and iterate on chat prompts and responses.

Give agents context:

1. Select the project in Agentic Chat, and reference issues, merge requests, and files in your prompt.
1. Add an `AGENTS.md` file and [custom rules](https://docs.gitlab.com/user/duo_agent_platform/customize/custom_rules/) to your projects, so that agents follow your conventions.
1. Enable [GitLab Orbit](https://docs.gitlab.com/orbit/) (beta), the lifecycle context graph of your code, merge requests, pipelines, deployments, vulnerabilities, and ownership. Agents query the graph for grounded context instead of crawling the code base.
1. Connect external tools and data through [MCP clients](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_clients/).

Support for Code Suggestions in all languages, including Markdown, is rolling out across IDEs. Follow [Support "all" programming languages across Duo Agent Platform](https://gitlab.com/gitlab-org/gitlab/-/work_items/571515) for the current status. Multiple open tabs and more file content can help increase the [context](https://docs.gitlab.com/user/project/repository/code_suggestions/context/) and quality of suggestions.

More use cases and workflows are documented in the [GitLab Duo Agent Platform documentation](https://docs.gitlab.com/user/duo_agent_platform/).

Open feature requests:

1. [Ask GitLab handbook questions in GitLab Duo Chat](https://gitlab.com/gitlab-com/content-sites/handbook/-/issues/212)

## Handbook use cases

The [editing the handbook guide](/handbook/about/editing-handbook/) documents GitLab Duo workflows for handbook changes:

- [Ask an agent in GitLab](/handbook/about/editing-handbook/#ask-an-agent-in-gitlab) with Agentic Chat to find pages, plan, and make changes.
- [Plan larger changes with Developer Flow](/handbook/about/editing-handbook/#plan-larger-changes-with-developer-flow), and ask Duo Developer to address review feedback.
- [Turn Slack discussions into handbook updates](/handbook/about/editing-handbook/#turn-slack-discussions-into-handbook-updates) with GitLab Duo in Slack.
- [Use an agent in your editor or terminal](/handbook/about/editing-handbook/#use-an-agent-in-your-editor-or-terminal) with VS Code and the GitLab Duo CLI.

### Create Markdown tables

Problem to solve: `Is there a way to add a table on a handbook page?`

Use the following prompt in Agentic Chat to create a table with preseed data columns:

```markdown
Create a Markdown table with the following data set
Header: Cloud, GPU type, Costs, Spec, Notes
Fill the entries with sample data for 3 rows.
```

Agentic Chat may visualize the Markdown table. Use that to your advantage to verify that the result matches your expectations, and follow up with a prompt to define the output format as raw Markdown.

```markdown
Show the raw Markdown in a code block
```

### Update or refactor Markdown tables

Sometimes, Markdown tables need to be split into multiple tables, or merged into a single one. Or an additional column needs to be added.

1. Open the file in your IDE and select the table that should be updated or refactored.
1. Ask Agentic Chat the following prompt:

   ```markdown
   Refactor the selected table for better readability. Split it by the first column into separate tables.
   ```

1. Review the proposed changes in the diff view before accepting them.

## Development use cases

[Foundational flows](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/) automate common development tasks:

1. [Developer](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/developer/) to implement issues and address review feedback in merge requests.
1. [Code Review](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/code_review/) to review merge requests.
1. [Fix CI/CD Pipeline](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/fix_pipeline/) to analyze and fix failed pipelines.
1. [Resolve conflicts with GitLab Duo](https://docs.gitlab.com/user/project/merge_requests/conflicts/#resolve-conflicts-with-gitlab-duo) to resolve merge conflicts, commit, and push to the source branch.
1. [Security Review](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/security_review/) to review merge requests for security risks.
1. [SAST False Positive Detection](https://docs.gitlab.com/user/application_security/vulnerabilities/false_positive_detection/) and [Secret False Positive Detection](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/secret_false_positive_detection/) to filter findings that need no action.
1. [SAST Vulnerability Resolution](https://docs.gitlab.com/user/application_security/vulnerabilities/agentic_vulnerability_resolution/) to propose a fix for a vulnerability in a merge request.

[Foundational agents](https://docs.gitlab.com/user/duo_agent_platform/agents/foundational_agents/) such as [Planner](https://docs.gitlab.com/user/duo_agent_platform/agents/foundational_agents/planner/), [CI Expert](https://docs.gitlab.com/user/duo_agent_platform/agents/foundational_agents/ci_expert_agent/), and [Security Analyst](https://docs.gitlab.com/user/duo_agent_platform/agents/foundational_agents/security_analyst_agent/) are available in Agentic Chat.

### Understand an unknown code base

Open Agentic Chat in the project, and ask for an overview:

```markdown
I am new to this project. What does it do, how does it work, and where should I start?
```

With [GitLab Orbit](https://docs.gitlab.com/orbit/) (beta), Agentic Chat gets full code and lifecycle context, and can answer how code relates to merge requests, pipelines, deployments, vulnerabilities, and ownership:

```markdown
How does this project connect to the other projects in the group, and what does that reveal about its development history, owners, dependencies, and risks?
```

### Implement an issue

1. Add an `AGENTS.md` file with project instructions, for example how to build and test.
1. Open a focused issue, and start the Developer Flow from the issue.
1. Open the session to follow the progress, and continue with other work while the flow runs.
1. Review the merge request, including the tests the agent added.

### Troubleshoot failed CI/CD pipelines

1. Navigate into the failed pipeline's job view, and inspect the log.
1. Ask the CI Expert agent in Agentic Chat what failed and why:

   ```markdown
   Analyze the failing pipeline in this MR. Identify which jobs failed, what each failed job was supposed to prove, and the smallest code or test change that fixes the problem without weakening CI.
   ```

1. Start the [Fix CI/CD Pipeline flow](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/fix_pipeline/) to propose a fix in a merge request.

### Resolve merge conflicts

1. In the merge request, select **Resolve conflicts**, then **Resolve with GitLab Duo**. Alternatively, select **Resolve with GitLab Duo** in the merge widget.
1. Review the commit GitLab Duo pushes to the source branch. Both changes should keep their intended behavior, and the tests should still pass.

### Plan larger changes

Ask the Planner agent to review an epic before implementation, for example a runtime or framework upgrade:

```markdown
Review this epic and its child work items against the current repository. Identify missing work, oversized issues, unsafe ordering, unclear acceptance criteria, and absent validation or rollback boundaries. Do not implement anything.
```

### Triage and resolve vulnerabilities

1. Open the vulnerability report, and select a finding.
1. Ask the Security Analyst agent for context:

   ```markdown
   Explain this vulnerability for the developer who owns this project. Summarize the risk, likely exploit path, urgency, affected code, false-positive indicators, and safest next action.
   ```

1. Run false positive detection to check whether the finding needs action.
1. If the finding is valid, start vulnerability resolution, and review the proposed merge request.

Explore more use cases in the [Developer Advocacy content library](/handbook/marketing/product-and-technical-marketing/developer-advocacy/content/).

### Onboarding and contributions

Team members and community contributors can use agents and flows for fast onboarding, learning more about the code base and GitLab, and contributing with faster review cycles.

1. Ask Agentic Chat about the source code base, and explore how to implement a specific feature proposal or bugfix.
1. Use the Code Review flow for faster merge request reviews.
1. Troubleshoot failing CI/CD pipelines with the Fix CI/CD Pipeline flow.

Learn more in the [GitLab Duo use cases documentation](https://docs.gitlab.com/user/gitlab_duo/use_cases/#use-gitlab-duo-to-contribute-to-gitlab).
