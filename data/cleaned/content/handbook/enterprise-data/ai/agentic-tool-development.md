---
title: "Agentic Tool Development"
description: "Data Team guide for developing agentic tools that work in our repositories."
---

The Data Team's approach to agentic tooling is built around a **skills-first, compose-upward** model. Rather than building monolithic agents, the team decomposes work into small, testable, reusable **skills** — each handling a single well-defined task. Agents are then composed from those skills, delegating to them based on the type of work requested.

This approach builds on emerging standards from [OpenCode](https://opencode.ai) and Anthropic — including conventions like `AGENTS.md` for repository-level agent context — and will be continuously evaluated and evolved as GitLab Duo matures as a platform.

## Directory Structure Convention

Every repository that adopts this pattern organizes agentic tooling under an `agents/` directory with four subdirectories:

```console
agents/
├── memory/     # Shared context files for coordinating parallel agent work
├── skills/     # Atomic, reusable capabilities; each skill has a SKILL.md
└── agents/     # Composed agents ready for use; each agent has a markdown spec
```

## Skills

Skills are the atomic building blocks. Each skill lives in its own directory with a `SKILL.md` that defines its purpose, inputs, process steps, and constraints.
Skills are scoped to a single responsibility and are designed to be invoked by agents or directly by engineers.

### Skill Specification

The team's skills follow the emerging [Agent Skills specification](https://agentskills.io/specification), an open standard that defines a portable, interoperable format for packaging AI agent capabilities. By conforming to this specification, skills can be discovered, loaded, and executed consistently across different AI coding tools and clients — making them portable beyond any single platform.

The two main specifications are:

1. **Directory structure:**

A skill is a directory containing, at minimum, a SKILL.md file:

```text
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

**SKILL.md format:**

The SKILL.md file must contain YAML frontmatter followed by Markdown content. The frontmatter includes metadata fields such as `name` and `description`, which are the most important for enabling automatic skill discovery by AI coding tools.

### Skill Development

Skills should be **modular** and **tested** — the same bar we hold for code.

#### Guideline 1: Modular

**One purpose per skill. Compose, don't bundle.**

A skill can be simple (`run_dbt_locally`, `gitlab-mr`) or an end-to-end workflow that chains skills together. What matters is that each skill has one clearly stated purpose, and any sub-task that could be its own skill *is* its own skill.

A skill called `build_and_open_mr` might call `run_dbt_locally` then `gitlab-mr` — that's modular. The orchestration logic lives in the workflow skill; the implementation logic lives in the sub-skills.

#### Guideline 2: Tested

**You ran it. It worked.**

A skill that hasn't been run end-to-end isn't ready to merge. That means:

1. You invoked it via the agent (not just read through the instructions)
1. The full workflow completed without the agent getting stuck or asking for unexpected clarification
1. The expected output was produced

The [agentic_skills_changes MR template](https://gitlab.com/gitlab-data/analytics/-/blob/master/.gitlab/merge_request_templates/python_changes.md?ref_type=heads) enforces both of these before merge.

## Agents

Agents are composed from skills and subagents. Each agent is defined by a markdown file that specifies:

- **System prompt** — the agent's role and behavioral constraints
- **Skills** — which atomic skills it may invoke
- **Subagents** — which peer agents it may delegate to
- **MCP servers** — which external tools (databases, APIs, knowledge bases) it has access to
- **Process** — a structured workflow the agent follows

Agents are designed to be transparent and auditable: all capabilities are explicitly enumerated and no agent improvises outside its defined toolset.

## Development and Change Management

New skills and agents are validated before being promoted to production using tools like Anthropic's [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator), which provides a structured framework for evaluating, testing, and benchmarking skills prior to merging. This ensures that only well-tested, reliable capabilities are promoted to the `skills/` and `agents/` directories.

Once ready, changes follow the same merge request workflow as any other code change in the repository, ensuring peer review, version history, and rollback capability. Because skills and agents are plain markdown files, they are diffable, reviewable, and auditable like any other code artifact.

The `AGENTS.md` file at the repository root serves as the entry point for agentic context — it describes the directory structure and conventions so that any AI coding assistant working in the repository can orient itself immediately.

As the field of agentic AI evolves rapidly, the team's conventions, tooling choices, and agent designs will be continuously re-evaluated. Patterns that work well today may be superseded by new capabilities in GitLab Duo or updated standards from the broader ecosystem, and the team will adapt accordingly.

## Available Skills

The Data Team's skills are maintained directly in the repositories where they're used. Browse the skills directories to see what's available:

- **[Data Team agentic skills](https://gitlab.com/gitlab-data/data-team-agentic-skills)** - Shared skills that can be used across other data repositories rather than creating the same skill in each repo
- **[Analytics repository skills](https://gitlab.com/gitlab-data/analytics/-/tree/master/agents/skills?ref_type=heads)** - Skills for dbt, Snowflake, and analytics workflows
- **[Extract repository skills](https://gitlab.com/gitlab-data/extract/-/tree/main/agents/skills?ref_type=heads)** - Skills for data extraction and pipeline work
- **[Snowflake permissions skills](https://gitlab.com/gitlab-data/snowflake-permissions/-/tree/main/agents/skills?ref_type=heads)** - Skills to provision Snowflake users and roles via Permafrost

As of writing, there still are NOT many skills available, but we will be adding more regularly.
