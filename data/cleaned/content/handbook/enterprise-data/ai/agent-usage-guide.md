---
title: "Agent Usage Guide"
description: "Best practices for working with AI agents in daily development"
---

[TOC]

## How Agents Work

An AI model is a single call — you send a prompt, you get a response. An agent is that same model running in a loop: it receives your request, decides on an action (read a file, run a command, edit code), observes the result, and repeats until the task is done.

For a deeper dive, see Anthropic's [building effective agents](https://www.anthropic.com/research/building-effective-agents) writeup.

## How MCPs Work

MCP (Model Context Protocol) servers extend what an agent can do by connecting it to external tools and data sources — think GitLab, dbt, Slack. Each active MCP adds to the agent's context window, so only enable what you actually need for the task at hand.

Not every integration is an MCP server. The Snowflake MCP server is no longer maintained, so Snowflake access goes through the [Snowflake CLI](/handbook/enterprise-data/platform/snowflake/snowflake-cli/) (`snow`), which an agent calls like any other command-line tool.

## Configuration

Both tools merge a global config with a project-level one, and project settings override global ones when they collide:

| | Global | Project-level |
| --- | --- | --- |
| Claude Code | `~/.claude/settings.json`, `~/.claude.json` | `.claude/settings.json`, `.mcp.json` at the repo root |
| OpenCode | `~/.config/opencode/opencode.jsonc` | `.opencode/config.json` at the repo root |

Keep your global config minimal. The main thing worth putting there is MCPs you need in every session regardless of what you're working on. Everything else — especially repo-specific MCPs like `dbt-mcp` — belongs in the project config. For example, `dbt-mcp` lives only in the analytics repo config since it's only relevant there.

A good rule of thumb: if you'd want the MCP active even when you open your agent outside of any project, it goes global. Otherwise, keep it local.

In Claude Code, prefer `/config` over hand-editing — it writes the settings file for you.

## Best Practices

Keep context lean. Start a new conversation any time you shift focus — a new feature, a different bug, an unrelated review. When in doubt, fresh window. Use `/clear` in Claude Code or `/new` in OpenCode to do that. This improves quality of responses as well as costs

If a skill exists for what you're doing, use it — skills give the agent domain-specific context it wouldn't otherwise have.

### Analytics Engineer

The AE team uses OpenCode across the full development lifecycle — building and modifying dbt models, responding to MR review feedback, troubleshooting pipeline failures, testing and validating data, exploring datasets, and drafting issues from context like Slack threads or review comments.

#### Recommended Workflow

- For new or unfamiliar tasks, start in **Plan** mode — review the proposed approach before making any changes
- For well-understood tasks, go directly to **Build** or the AE agent
- Begin prompts with "I want to…" and describe the change, review comment, or question you are working through
- For MR reviews, open a fresh session scoped to that review
- For more detail on the two modes, see [When to Use Plan Mode](#when-to-use-plan-mode) below

#### Session Management, Model Selection, and Cost Efficiency

- Start a new session per MR, topic, or day — the guiding question is whether the prior context is actually needed for the next task; if not, start fresh
- A medium sized model, like **Sonnet 4.6**, is the recommended default model — they offer a good balance of quality, speed, and cost; larger models are slower and more expensive without proportional gains for most AE tasks
- Input tokens seem to be the most expensive component of a session — keep context lean, use `/compact` when it grows large, and start a new session before reaching the 200K token threshold
- Only enable the MCPs needed for the current task — in OpenCode, `/mcps` toggles servers on or off with `space`; in Claude Code, `/mcp` lists the connected servers and which ones load is set in config

#### Data Access Setup

The [Snowflake CLI](/handbook/enterprise-data/platform/snowflake/snowflake-cli/) is required for most AE development work — it is how an agent queries Snowflake during a session. The [dbt MCP server](agent-setup.md#dbt-mcp-server) is worth adding on top of it for dbt model structure, lineage, and node details.

## When to Use Plan Mode

Both tools separate planning from execution:

- **Plan mode** — reviews your request and relevant code, then proposes a detailed approach *before* making any changes
- **Execution** — Build mode in OpenCode, the default or edit-accepting modes in Claude Code — makes changes directly

Always run plan mode first for anything non-trivial. It's surprisingly good at catching design issues before you're already mid-implementation.

The setup guide recommends making plan the default for both tools — see [Claude Code Setup](agent-setup.md#claude-code-setup) for `defaultMode` and [OpenCode Setup](agent-setup.md#opencode-setup) for the default agent. You then leave plan mode explicitly when you're ready to execute.

## Skills

Skills encode reusable, team-specific knowledge — conventions, workflows, and best practices that would otherwise need to be re-explained every session. Rather than prompting from scratch, invoking a skill gives the agent the right context immediately.

### How to Use Skills

Skills are automatically invoked by AI coding tools like Claude Code and OpenCode when the task described in your prompt matches the skill's frontmatter metadata. Well-written frontmatter (especially `name` and `description` fields) enables automatic discovery. You can also explicitly mention a skill by name in your prompt if you know it exists.

### Available Skills

For a list of skills developed by the Data Team, see the [Available Skills](agentic-tool-development.md#available-skills) section in the Agentic Tool Development guide.

### Setup

To enable skills in Claude Code or OpenCode, follow the [Skills Setup](agent-setup.md#skills-setup) instructions in the Agent Setup guide.
