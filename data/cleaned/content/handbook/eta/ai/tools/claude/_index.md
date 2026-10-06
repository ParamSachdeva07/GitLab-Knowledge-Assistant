---
title: "Claude"
description: "Claude is GitLab's desktop AI for getting work done. Every team member has access via Claude Enterprise."
---

## What Claude is at GitLab

Claude is GitLab's desktop AI for getting work done: drafting, reasoning, code, and multi-step agentic tasks. Glean is GitLab's personal AI for knowledge management and personal-scope automation, grounded in our internal systems. The two complement each other. Claude has a Glean connector built in, so you can pull GitLab context into a Claude conversation without switching tools. Use the right tool for the job, not one over the other.

## Claude.ai (Claude Enterprise)

Every GitLab team member has access to Claude Enterprise via Okta. This is the daily driver AI for most team members, available via the web app, the desktop app for macOS and Windows, and the mobile app for iOS and Android.

Claude Enterprise gives you the full set of capabilities team members reach for day to day:

- **Skills.** Reusable, named capabilities you can invoke inside any conversation.
- **Plugins.** Connect Claude to additional tools and surfaces.
- **Projects.** Persistent workspaces for ongoing work, with their own context and files.
- **Connectors.** Including the Glean connector, which lets you pull GitLab context (handbook, GitLab.com, Slack, Salesforce, Google Drive and more) into a Claude conversation while respecting your existing permissions.

To access Claude.ai, open Okta and find the Claude tile, or sign in at [https://claude.ai](https://claude.ai) using Okta SSO.

## Claude Console (Anthropic Console)

The Claude Console is a distinct product from Claude.ai, separately licensed and **managed by CorpSec**. It is the surface for builders working with the Claude API directly: prompt development, evaluations, and agent building outside the chat product.

Provisioning is controlled, not self-service. Processes for Console access are still being established and will likely run through Serval. API keys are provisioned for two purposes only:

- **Application AI access.** Service accounts behind a managed application.
- **Personal API tokens** used in harnesses other than Claude Code. Claude Code has its own integrated authentication, so it does not need a personal API token.

Team members do not create their own tokens. Tokens are provisioned for the named user or application and shared back to them.

## Claude vs Glean

Glean is the right choice for personal knowledge-management automation grounded in your real GitLab context: the handbook, GitLab.com, Slack, Salesforce, Google Drive and the other systems Glean indexes. Claude is the right choice when you need to get work done: drafting, reasoning, code, multi-step tasks.

The two overlap, intentionally. Claude's Glean connector lets you pull GitLab context into Claude when a piece of work needs both: Claude's reasoning and writing depth, grounded in real internal context. Pick based on the task, not on a strict either/or.

## Governance and data classifications

Claude is authorised for **Orange data and below**, consistent with the Glean guide. Team members remain responsible for not pasting Red data into tools authorised only for Orange.

The AI tool risk framework governs which Claude features are approved for production use.

## Get help

- For questions, post in [**#enterprise-ai-collab**](https://gitlab.enterprise.slack.com/archives/C0AE5DX6SQJ) on Slack.
- For incidents, raise a ticket via Serval.
