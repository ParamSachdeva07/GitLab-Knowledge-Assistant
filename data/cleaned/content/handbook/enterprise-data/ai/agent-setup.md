---
title: "AI Agent Setup"
description: "Data Team guide for setting up agentic AI tools for development"
---

[TOC]

## Context

The data team doesn't have a standard approach for AI-assisted development — this guide fills that gap. It's based on what's already been working for several teammates, so everyone has a solid starting point rather than figuring it out from scratch.

Two terminal-based agents are documented here: **Claude Code** and **OpenCode**. Both are supported and neither is the team default — use whichever fits your workflow. The team's shared skills follow the [Agent Skills format](https://agentskills.io/specification), so one local clone works in either tool.

This guide covers setup for:

- **Claude Code** and **OpenCode** — terminal-based AI coding agents
- **Snowflake CLI and the dbt MCP server** — data access during an agent session
- **MacWhisper** — voice-driven prompting (optional)

---

## Claude Code Setup

A more comprehensive guide is available in the [internal handbook](https://internal.gitlab.com/handbook/ai-security-at-gitlab/guides/setup-guides/claude-code-setup/). The steps below are a simplified, data-team-specific version.

<details>
<summary><strong>Claude Code setup steps</strong></summary>

**Step 1: Install Claude Code**

Install Claude Code by following the [Claude Code setup guide](https://internal.gitlab.com/handbook/ai-security-at-gitlab/guides/setup-guides/claude-code-setup/), which covers installation, authentication with your GitLab account, and the approved usage policy.

Verify the installation:

```bash
claude --version
```

You should see the installed version number.

**Step 2: Start Claude Code from the analytics repo**

```bash
jump analytics
claude
```

**Step 3: Add the GitLab MCP server**

Add the GitLab MCP server by following the [GitLab MCP setup guide](https://internal.gitlab.com/handbook/ai-security-at-gitlab/guides/setup-guides/gitlab-mcp-setup/).

The GitLab MCP server lets an agent work with GitLab directly during a session — reading issues, opening and updating merge requests, reading review comments, and checking pipeline and job status. Several Data Team skills depend on it.

To verify the connection, run `/mcp` inside Claude Code. The GitLab server should be listed as connected.

**Step 4: Set `plan` as your default mode**

Run `/config` inside a Claude Code session to review and change your settings. Anything you change there is written to your Claude Code settings file automatically, so there is no config file to hand-edit.

Set `defaultMode` to `plan`. This keeps you in the safer, more deliberate mode by default — you switch to an editing mode explicitly when you're ready to execute. It is the Claude Code equivalent of the OpenCode default agent setting below.

The model and output style are also worth reviewing in `/config` while you're there.

**Step 5: Review the Agent Usage Guide**

Before you start using Claude Code, review the [Agent Usage Guide](agent-usage-guide.md) to understand:

- How agents and MCPs work
- Configuration best practices (global vs project-level)
- When to use plan mode
- Prompting best practices and context management
- Available skills and agents

</details>

---

## OpenCode Setup

A more comprehensive guide is available in the [internal handbook](https://internal.gitlab.com/handbook/ai-security-at-gitlab/guides/setup-guides/opencode-setup/). The steps below are a simplified, data-team-specific version.

<details>
<summary><strong>OpenCode setup steps</strong></summary>

**Step 1: Install OpenCode**

```bash
curl -fsSL https://opencode.ai/install | bash
```

**Step 2: Verify the installation**

Check that OpenCode is available in your PATH:

```bash
which opencode
```

**If `which opencode` returns nothing**, add OpenCode to your PATH by running:

```bash
echo 'export PATH=~/.opencode/bin:$PATH' >> ~/.zshrc && source ~/.zshrc
```

Now verify the installation:

```bash
opencode --version
```

You should see the installed version number.

**Step 3: Start OpenCode from the analytics repo**

```bash
jump analytics
opencode
```

**Step 4: Configure GitLab Duo as your AI provider**

GitLab Duo uses OAuth — no token to create or manage.

1. Run `/connect` inside OpenCode and select **GitLab Duo**
1. OpenCode will open your browser to complete the OAuth flow
1. Sign in with your `@gitlab.com` account and authorise the app
1. You'll be redirected back to OpenCode automatically

Once connected, test it by saying `hi` to verify OpenCode responds.

**Step 5: Apply the Golden Config**

Apply the config from the [OpenCode Golden Path](https://internal.gitlab.com/handbook/ai-security-at-gitlab/guides/golden-configs/opencode/#golden-path-config).

> **Note:** Use `~/.config/opencode/opencode.jsonc` rather than `opencode.json` — the `.jsonc` extension allows comments, which is useful for annotating your config.

**Step 6: Set `plan` as your default agent**

Open `~/.config/opencode/config.json` (this is a separate file from the `opencode.jsonc` Golden Config in Step 5) and add `default_agent`:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  ...
  "default_agent": "plan"
}
```

This keeps you in the safer, more deliberate mode by default — you switch to Build explicitly when you're ready to execute.

**Step 7: Review the Agent Usage Guide**

Before you start using OpenCode, review the [Agent Usage Guide](agent-usage-guide.md) to understand:

- How agents and MCPs work
- Configuration best practices (global vs project-level)
- When to use Plan vs Build mode
- Prompting best practices and context management
- Available skills and agents

**Video resources**

Requires using **GitLab Unfiltered** account:

- [OpenCode Setup Tutorial](https://www.youtube.com/watch?v=80vTUzgQzoY) (3m 30s)
- [OpenCode Demo](https://www.youtube.com/watch?v=nClVkkI-MFo) (5m 30s)

</details>

---

## Connecting to Other Applications

An agent gets more useful the more of your toolchain it can reach. The sections below cover the connections the data team relies on day to day — querying Snowflake, and awareness of the dbt project.

### Snowflake CLI

Agents query Snowflake through the [Snowflake CLI](/handbook/enterprise-data/platform/snowflake/snowflake-cli/) (`snow`), which is the Data Team standard for local Snowflake access. Follow that page to install and configure it.

Once `snow connection test` passes, both Claude Code and OpenCode can query Snowflake during a session — Claude Code by running `snow sql` in the terminal, OpenCode through its built-in `snowflake` tool.

> **Note:** The Snowflake MCP server previously described here is no longer maintained and has been replaced by the Snowflake CLI. If you set the MCP server up earlier, there is no migration step — install the CLI and use it instead.

### dbt MCP Server

The dbt MCP server gives an agent awareness of the dbt project — model structure, lineage, and node details. It is only relevant in the analytics repo.

First, make sure the dbt virtualenv is set up:

```bash
jump analytics
make run-dbt
ls .venv/bin/dbt  # Should show the dbt executable
```

If `ls .venv/bin/dbt` returns the file path, you're good to go.

Then add the following to your `~/.zshrc`, adjusting `ANALYTICS_DIR` if your analytics repo lives somewhere else:

```bash
# Analytics MCP Environment Variables
export ANALYTICS_DIR="$HOME/repos/analytics"
export DBT_PROJECT_DIR="$ANALYTICS_DIR/transform/snowflake-dbt"
export DBT_PATH="$DBT_PROJECT_DIR/.venv/bin/dbt"
```

Run `source ~/.zshrc` in the shell where you plan to start your agent.

**Verify the connection:**

Run `/mcp` in Claude Code or `/mcps` in OpenCode — the dbt server should be listed as connected.

---

## Skills Setup

When you run an agent inside a repo, that repo's own skills need no setup — the agent reads their frontmatter and invokes them when a task matches.

Skills shared across repos are different. They live in [`data-team-agentic-skills`](https://gitlab.com/gitlab-data/data-team-agentic-skills) and have to be symlinked into your local skills directory before an agent can see them — including when a repo's own skill calls one. Follow the setup steps in that repo's README.

---

## MacWhisper for Voice Prompting (Optional)

Typing out detailed prompts is slow. [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper) is a macOS voice-to-text app that makes it much faster to describe context and work through problems out loud — particularly for longer prompts where you'd otherwise spend more time typing than thinking.

It's noticeably more accurate than built-in macOS Dictation app, and unlike cloud-based transcription it runs entirely on-device, so nothing leaves your machine.
