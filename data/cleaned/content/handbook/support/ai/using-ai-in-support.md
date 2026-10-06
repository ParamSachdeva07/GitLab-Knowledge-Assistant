---
title: Using AI in Support
description: Practical guide for Support Engineers on using AI tools day-to-day, including tool selection by scenario, prompt engineering and model selection
---

## Overview

This page provides practical, scenario-driven guidance for using AI tools for daily Support Engineering work. It brings together tool capabilities, data classification rules, prompt engineering techniques and model selection advice into a single reference.

Before using this page, ensure you have read:

1. [AI and Support Work](_index.md) for the decision framework on when to use AI
1. [AI tool selection](ai-tool-selection.md) for detailed tool capabilities and approval status
1. [AI usage recommendations](ai-usage-recommendations.md) for general prompting strategies

## Tools by scenario

Different tools are suited to different tasks. The table below maps common Support Engineering scenarios to the recommended tool, based on data classification, access capabilities and strengths.

| Scenario | Recommended tool | Why |
|----------|-----------------|-----|
| Summarising a long Zendesk ticket for handover | [Glean](ai-tool-selection.md#glean) | Reads ticket context directly from the Zendesk sidebar without copy-pasting |
| Finding similar past tickets, issues or MRs | [Glean](/handbook/support/ai/ai-tool-selection/#glean) or [GitLab Duo Agentic Chat](/handbook/support/ai/ai-tool-selection/#gitlab-duo-agentic-chat) | Glean searches across Zendesk, Handbook and Slack; Agentic Chat searches GitLab issues and MRs directly |
| Diagnosing a CI/CD failure using customer logs | [GitLab Duo Chat](/handbook/support/ai/ai-tool-selection/#gitlab-duo-chat) | Approved for Red data; has GitLab product knowledge and can process logs safely |
| Multi-step investigation across issues, MRs and code | [GitLab Duo Agentic Chat](/handbook/support/ai/ai-tool-selection/#gitlab-duo-agentic-chat) | Can autonomously traverse the GitLab ecosystem and synthesise findings from multiple sources |
| Drafting or refining an internal document or workflow | [Anthropic Claude](/handbook/support/ai/ai-tool-selection/#anthropic-claude-web) | Strong at drafting, summarisation and reasoning with long context windows |
| Polishing wording in a Google Doc or Gmail | [Gemini (Workspace)](/handbook/support/ai/ai-tool-selection/#gemini-chat-workspace) | Integrated directly into Google Workspace where the content already lives |
| Catching up on a Slack channel after PTO | [Slack AI](/handbook/support/ai/ai-tool-selection/#slack-ai) or [Glean](/handbook/support/ai/ai-tool-selection/#glean) | Slack AI summarises in-place; Glean can provide a broader cross-platform summary |
| Generating a draft KB article from a resolved ticket | [GitLab Duo Agentic Chat](/handbook/support/ai/ai-tool-selection/#gitlab-duo-agentic-chat) | Can access the ticket context (Red data approved) and generate structured output following a template |
| Brainstorming troubleshooting approaches | [Anthropic Claude](/handbook/support/ai/ai-tool-selection/#anthropic-claude-web) or [GitLab Duo Chat](/handbook/support/ai/ai-tool-selection/#gitlab-duo-chat) | Claude for general reasoning; Duo Chat when the problem is GitLab-specific |
| Prototyping prompt ideas for Duo custom rules | [Anthropic Claude](/handbook/support/ai/ai-tool-selection/#anthropic-claude-web) | Good for iterative drafting and refinement before deploying prompts elsewhere |

## Data classification: quick rules

Choosing the right tool starts with understanding the data you are working with. The full classification standard is at [Data Classification Standard](../../security/policies_and_standards/data-classification-standard/).

| Data type | Classification | Approved tools |
|-----------|---------------|----------------|
| Customer PII, credentials, logs with sensitive data, ticket attachments | [RED](/handbook/security/policies_and_standards/data-classification-standard/#red) | GitLab Duo (Chat, Agentic Chat, Agent Platform) only |
| Internal documentation, handbook content, anonymised examples, workflow drafts | [ORANGE](/handbook/security/policies_and_standards/data-classification-standard/#orange) | All approved tools (Glean, Claude, Gemini, Slack AI, NotebookLM, Zoom AI, etc.) |

> When in doubt, treat data as Red. Sanitise customer-identifying information before using any Orange-classified tool. See the [working on tickets guidance on LLM use](../workflows/working-on-tickets.md#can-i-use-output-from-an-llm-in-ticket-replies) for verification requirements.

## Prompt engineering for Support Engineers

Effective prompting reduces wasted iterations and produces more actionable output. The principles below apply across all AI tools.

### Core principles

1. **State the goal clearly** - specify the artifact you need (a diagnosis, a KB draft, a reply skeleton or a checklist) rather than asking open-ended questions.
1. **Provide context** - include the GitLab version, environment type (SaaS or self-managed), install method, error messages and what has already been tried.
1. **Constrain the output** - ask for a specific format such as three to five bullets, a step-by-step checklist or two options with pros and cons.
1. **Allow uncertainty** - make it acceptable for the tool to say it is not sure rather than guessing when evidence is weak.
1. **Iterate** - refine prompts based on responses by adding missing details instead of starting from scratch.

### Support-specific prompt patterns

#### Issue analysis and diagnosis

> You are a GitLab Support Engineer. Here is a ticket summary, environment and logs.
>
> Please:
>
> - Identify the most likely root cause or causes.
> - Suggest up to five concrete next troubleshooting steps.
> - Use the GitLab docs, MRs, issues and codebase for your investigation.

#### Solution research

> I am working on a GitLab support case with the problem: [describe briefly].
>
> Please find relevant GitLab documentation, known issues and merge requests.

#### Formatting a customer reply

> Act as a GitLab Support Engineer.
>
> I have drafted the following response to a customer. Please help me improve the formatting, clarity and structure while preserving my original meaning and technical content:
>
> [paste your drafted response here]
>
> Ensure the response:
>
> - Restates the problem clearly.
> - Explains what is happening in simple terms.
> - Presents the next steps in a logical order with brief reasoning.
> - Sets expectations on what we will do next and when we will update them.
>
> Do not add information that is not present in my draft.

AI should be used to help format and polish responses you have already drafted yourself. Never generate a customer-facing reply entirely from an LLM. Write your response first based on your own understanding and investigation, then use AI to improve clarity, structure and tone. You remain responsible for the accuracy and completeness of every response sent to a customer.

#### Knowledge base or workflow draft

> Using the following ticket notes and solution, draft a short internal Support knowledge base article or workflow.
>
> Include sections: Description, Environment, Symptoms, Cause, Solution or Workaround, Additional Information.
>
> Keep it concise and technical and avoid customer-specific identifiers.

## Using GitLab Duo Agent Platform for troubleshooting

When Red data is involved (full ticket content, logs, configuration snippets), GitLab Duo Agent Platform (DAP) is the preferred tool. It is the only AI tool approved for Red data and has direct access to the GitLab ecosystem.

### When DAP is most useful

- The ticket involves complex CI/CD behaviour, scaling questions or configuration where code, pipelines and documentation are all relevant.
- Multiple GitLab projects or components need to be considered together.
- Proposed steps need to be grounded in actual GitLab code and documentation rather than generic advice.

### What to ask DAP to do

- Read the ticket context you provide, including summary, environment, logs and recent changes.
- Check the GitLab codebase for relevant components, feature flags and configuration keys.
- Search GitLab documentation for pages that describe the behaviour, feature or error.
- Look for existing issues and merge requests that match the symptoms, including regressions, feature changes and known limitations.
- Separate evidence from hypothesis, for example by distinguishing "Based on code in `<file>` and issue `<link>`" from "Possible but unconfirmed cause".

### Model selection

You can select which large language model (LLM) to use with DAP. The choice affects response quality, speed and reasoning depth, and the right choice depends on whether you are using Duo Chat directly or an agentic harness.

| Model | Speed | Reasoning depth | Best for |
|-------|-------|-----------------|----------|
| Claude Haiku | Fastest | Basic | Quick lookups, simple summaries, reformatting text |
| Claude Sonnet | Fast | Strong | Most day-to-day support work: diagnosis, drafting, research |
| Claude Opus | Slow | Strongest | Deep investigation, ambiguous problems, long multi-step reasoning |

#### Using Duo Chat directly

1. Start with **Sonnet** for most tickets. It handles diagnosis, solution research and drafting well.
1. If the response lacks depth or misses key details, retry the same prompt with **Opus**.
1. Use **Haiku** for high-volume, low-complexity tasks where speed matters, such as batch-summarising tickets or converting bullet points into prose.
1. For deep-dive investigations that cross-reference code, issues, MRs and documentation, **Opus** produces the most thorough results.

#### Using an agentic harness

When using an agentic harness such as `internal-soslab` or Agent Capabilities for GitLab Support, prefer a larger model. The bigger context window and stronger reasoning handle the log-heavy, multi-source investigation these tools are built for.

1. Start with a large model such as **Opus** when working a ticket end to end.
1. Drop down to a smaller model such as **Sonnet** for well-scoped, individual tasks.

The model selected with Duo does not affect what data the tool can access.

## Best practices

### Before you prompt

- **Know your baseline** - estimate how long the task would take manually. If AI does not beat that, it is not helping.
- **Check data classification first** - determine whether you are working with Red or Orange data before choosing a tool. This is not optional.
- **Start with what you know** - draft your own understanding before asking AI. Use AI to enhance, not replace, your thinking.

### While using AI

- **Verify everything** - check environment variables, configuration options, documentation URLs, API endpoints, CLI options and version-specific details against authoritative sources. LLMs confidently produce plausible but incorrect technical details.
- **Watch for version and date confusion** - LLMs frequently suggest outdated versions, incorrect release dates or features that do not exist in the customer's version. Always confirm version applicability.
- **Do not trust numbers or maths** - LLMs are unreliable with numerical reasoning. Use dedicated tools for statistical analysis.
- **Iterate rather than restart** - if the first response is close but incomplete, add the missing details in a follow-up prompt rather than starting a new conversation.
- **Keep conversations focused** - one topic per conversation produces better results than context-switching mid-thread.

### In customer interactions

- **Use AI to format, not to author** - always write your response first based on your own investigation and understanding. Use AI to improve the formatting, clarity, structure and tone of what you have already written. Never send a response generated entirely by an LLM.
- **Test commands and code before sharing** - you must be able to understand, explain and have tested any commands or code snippets before sending them to a customer.
- **Anonymise before using Orange tools** - strip customer names, account identifiers, credentials and other PII before pasting into Claude, Glean or any non-Duo tool.
- **Disclose when appropriate** - if a customer asks whether AI was used, be transparent. GitLab values [transparency](/handbook/values/#transparency).

### After using AI

- **Track what works** - note which prompts and tools produce useful results for specific problem types. Share effective patterns with your team.
- **Recognise when AI is hurting** - if you spend more time prompting than solving, if you are following advice you do not understand or if colleagues notice quality dropping, step back and work manually.
- **Continue building expertise** - AI should accelerate your growth, not replace it. If you find yourself avoiding learning because AI can answer for you, that is a sign to refocus on fundamentals.

## Related pages

- [AI and Support Work](_index.md)
- [AI tool selection](ai-tool-selection.md)
- [AI usage recommendations](ai-usage-recommendations.md)
- [Using LLM output in ticket replies](../workflows/working-on-tickets.md#can-i-use-output-from-an-llm-in-ticket-replies)
- [Data Classification Standard](/handbook/security/policies_and_standards/data-classification-standard/)
