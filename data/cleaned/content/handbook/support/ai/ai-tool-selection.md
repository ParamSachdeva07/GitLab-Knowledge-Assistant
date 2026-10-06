---
title: AI tool selection
description: Guidelines around selecting the best AI tool for the task at hand
---

GitLab Support provides access to various AI tools with different capabilities and specializations. This guide helps you select the right tool based on your specific task requirements.

> [!note]
> This guide assumes you've read the [AI and Support Work](_index.md) page and determined that AI will help with your task. If you're unsure whether to use AI, start there first.

## Quick Reference Table

| Tool | Best For | Customer Data | GitLab Access | Approval Status |
|------|----------|---------------|---------------|-----------------|
| [GitLab Duo Chat](https://docs.gitlab.com/user/gitlab_duo_chat/) | GitLab-specific questions, code analysis | ✅ Safe | Product knowledge | ✅ Approved (RED) |
| [GitLab Duo Agentic Chat](https://docs.gitlab.com/user/gitlab_duo_chat/agentic_chat/) | Complex research, multi-step analysis | ✅ Safe | Full ecosystem access | ✅ Approved (RED) |
| [Glean](../../eta/css/zendesk/apps/global/#glean) | Zendesk ticket summaries, KB articles, enterprise search | ✅ Safe | Product knowledge (via Duo Chat) | ✅ Approved (ORANGE) |
| [Anthropic Claude (Web)](#anthropic-claude-web) | Drafting, summarization, research, reasoning |  ⚠️ Requires sanitization | None | ✅ Approved (ORANGE) |
| [Slack AI](#slack-ai) | Summaries and drafting inside Slack |  ⚠️ Requires sanitization | None | ✅ Approved (ORANGE) |
| [Gemini Chat (Workspace)](#gemini-chat-workspace) | Writing, research, Q&A in Google Workspace |  ⚠️ Requires sanitization | None | ✅ Approved (ORANGE) |
| [Gemini API](#gemini-api) | Custom apps and integrations | ⚠️ Requires sanitization | None | ✅ Approved (ORANGE, only with prior Legal/CorpSec API‑key review) |
| [NotebookLM](#notebooklm) | Document-grounded analysis and summaries |  ⚠️ Requires sanitization | None | ✅ Approved (ORANGE) |
| [Zoom AI Assistant](#zoom-ai-assistant) | Meeting transcription, summaries, action items |  ⚠️ Requires sanitization | None | ✅ Approved (ORANGE) |
| [Metaview](#metaview) | Interview transcription and notes |  ⚠️ Requires sanitization | None | ✅ Approved (ORANGE, recruiting) |
| [Reclaim AI](#reclaim-ai) | Calendar and time-blocking |  ⚠️ Requires sanitization | None | ✅ Approved (ORANGE, request access) |
| [duo-helper-image](#duo-helper-image) | Governed `glab` + Duo environment, semantic ticket search | ✅ Safe | GitLab MCP, Glean, Semantic Search | ✅ Approved (RED) |
| [Request for Help (RFH) Agent](#request-for-help-rfh-agent---search-and-create-issues) | Search and create RFH issues | ✅ Safe | RFH project | ✅ Approved (RED) |
| [internal-soslab](#internal-soslab) | SOS bundle investigation, log/config analysis | ✅ Safe | Glean, 27+ MCP tools | ✅ Approved (RED) |

## Tool Comparison

### GitLab Duo Chat

**Ideal for:** Quick GitLab feature questions, code explanations, standard troubleshooting

**Data Classification:** [RED](/handbook/security/policies_and_standards/data-classification-standard/#red)

**Reference:** [GitLab Handbook – GitLab Duo](/handbook/tools-and-tips/ai/gitlab-duo/)

GitLab Duo is GitLab's AI-native DevSecOps suite, including chat, code suggestions, and agentic workflows. It is the **only AI tool approved for Red data** (e.g., customer data in tickets, credentials, PII). Available in both the GitLab UI and supported IDEs.

**Strengths:**

- Deep GitLab product knowledge and documentation access
- Fast responses for straightforward questions
- Safe for customer data processing — the only tool cleared for Red classification
- Integrated into GitLab workflow and IDEs (VS Code, JetBrains, etc.)
- Code suggestions and explanations powered by GitLab-trained models

**Best use cases:**

- "How does GitLab feature X work?"
- "Explain this customer's configuration"
- "What could cause this GitLab error?"
- Processing logs from customer environments
- Getting code suggestions and explanations inline in your editor

### GitLab Duo Agentic Chat

**Ideal for:** Research across GitLab ecosystem, complex multi-step workflows

**Data Classification:** [RED](/handbook/security/policies_and_standards/data-classification-standard/#red)

**Reference:** [GitLab Duo Agentic Chat Docs](https://docs.gitlab.com/user/gitlab_duo_chat/agentic_chat/)

Part of the Duo Agent Platform, Agentic Chat can autonomously plan and execute multi-step tasks across the GitLab ecosystem. Unlike standard Duo Chat, it can traverse issues, MRs, and project data to assemble answers that require context from multiple sources.

**Strengths:**

- Only tool with direct access to GitLab projects, issues, and MRs
- Handles complex, multi-step analysis
- Can generate documentation drafts and MRs
- Safe for customer data processing

**Best use cases:**

- "Find existing issues related to this customer problem"
- "Research workarounds in long issue discussions"
- "Generate documentation updates and MRs"
- "Code contributions to GitLab codebase"
- Complex ticket analysis requiring multiple sources

### Anthropic Claude (Web)

**Ideal for:** Drafting, summarization, research, general-purpose reasoning, and communication enhancement

**Data Classification:** [ORANGE](/handbook/security/policies_and_standards/data-classification-standard/#orange)

**Reference:** [GitLab Handbook – Claude](/handbook/tools-and-tips/ai/claude/)

Anthropic Claude is the approved general-purpose AI assistant for GitLab team members. Access is provided via the web interface at [claude.ai](https://claude.ai). It must not be used with Red data (e.g., customer PII, credentials, or other sensitive customer information) — all inputs must be sanitized to Orange level or below.

**Available models:**

| Model | Best For | Characteristics |
|-------|----------|-----------------|
| Claude Sonnet 4 | Day-to-day tasks, fast iteration | Fastest responses, strong reasoning, cost-efficient. Best default for most Support tasks. |
| Claude Opus 4 | Complex analysis, nuanced writing | Most capable model. Ideal for intricate multi-step reasoning, detailed technical writing, and ambiguous problems where depth matters more than speed. |
| Claude Haiku 4 | Lightweight tasks, high throughput | Most compact model. Suitable for quick classification, simple Q&A, or when you need a fast answer to a straightforward question. |

**Strengths:**

- Excellent for communication enhancement — improving clarity, tone, and structure of ticket responses
- Strong at summarization, drafting, and creative problem-solving
- Capable reasoning across technical and non-technical domains
- Supports long context windows for analyzing large documents or logs (after sanitization)
- Web search capability for researching current topics

**Best use cases:**

- Improving response clarity and tone for customer-facing communication
- Summarizing or restructuring lengthy internal documents
- Quick analysis of complex scenarios (with sanitized data only)
- Brainstorming troubleshooting approaches or workarounds
- Drafting internal documentation, runbooks, or process guides
- General reasoning tasks that don't require direct GitLab product access

**Limitations:**

- No access to GitLab product data, issues, MRs, or internal systems — use GitLab Duo for those tasks
- Cannot process Red data — always sanitize inputs before use
- Knowledge is based on training data and web search; may not reflect the latest GitLab-specific changes

### Glean

**Ideal for:** Summarizing Zendesk ticket conversations, suggesting relevant KB articles, cross-platform enterprise search

**Data Classification:** [ORANGE](/handbook/security/policies_and_standards/data-classification-standard/#orange)

**Reference:** [GitLab Handbook – Glean Guide](/handbook/eta/ai/tools/glean/)

Glean is an enterprise AI knowledge and search platform that indexes content across the Handbook, GitLab, Google Drive, Slack, Zendesk, Salesforce, and other connected data sources. For Support, its primary value is the Zendesk sidebar integration, which provides ticket-aware AI assistance without leaving the ticket interface. It is also used for support workflows via the Zendesk connector.

**Strengths:**

- Enterprise-wide search across multiple data sources in a single query
- Built directly into the Zendesk ticket sidebar for in-context assistance
- Ticket-linked history makes it easy to continue or revisit past conversations
- Can surface relevant KB articles, handbook pages, and past ticket resolutions together

**Best use cases:**

- "Summarize this ticket's conversation for a handoff"
- "Suggest a relevant KB article for this issue"
- Finding related information scattered across Handbook, Slack, and Google Drive
- Creating and reusing custom prompts tailored to Support workflows
- Quickly generating structured AI insights without leaving Zendesk

## Other Approved Tools

The following tools are approved for use at Orange data classification level. They must not be used with Red data (e.g., customer data) unless otherwise noted.

### Slack AI

**Approval:** Approved (Orange)

**Reference:** [Internal AI Tool Usage Requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements)

AI-powered summaries and drafting built into Slack. Useful for catching up on channels you've missed, summarizing long threads, and composing messages. Operates within your existing Slack workspace — no data leaves the platform beyond what Slack already handles.

**Common uses:** Summarize a channel while you were on PTO, get the gist of a long decision thread, draft a quick message.

### Gemini Chat (Workspace)

**Approval:** Approved (Orange)

**Reference:** [Internal AI Tool Usage Requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements)

Gemini assistant embedded in Google Workspace (Docs, Sheets, Gmail, etc.). Useful for writing assistance, research, and general Q&A directly within the tools you're already working in. Since it's integrated into Workspace, it can reference your Drive content in context.

**Common uses:** Draft or refine text in Google Docs, generate formulas in Sheets, compose Gmail replies.

### Gemini API

**Approval:** Approved (Orange, API-key approval required)

**Reference:** [Legal & CorpSec – API Key Requests](https://internal.gitlab.com/handbook/legal-and-corporate-affairs/legal-privacy/#requests-for-api-key-use-for-anthropic-claude-and-google-gemini)

Gemini API for custom applications and integrations. **Requires prior Legal/CorpSec review and API-key approval before use** — do not provision keys yourself. Orange data only; no Red data may be sent through custom integrations.

**Common uses:** Building internal tooling, custom automations, or experimental workflows that need an LLM backend.

### NotebookLM

**Approval:** Approved (Orange; careful when sharing notebooks)

**Reference:** [The Loop – NotebookLM](https://simpplr.link/d/e/theloop.gitlab.com/site/f2d115dc-bc7c-4925-8cab-2e55e97646ad/page/282d0c50-b2b3-4465-bfad-9cc9d32e4893)

Google's AI tool for document-grounded analysis and summaries. You upload source documents and NotebookLM answers questions strictly based on those sources — reducing hallucination risk for document-heavy research.

> [!warning]
> Notebooks do **not** inherit Google Drive sharing permissions. A notebook you share may expose its source content to anyone with the link, even if the underlying Drive files are restricted. Exercise caution when sharing notebooks that contain sensitive (but non-Red) material.

**Common uses:** Analyzing lengthy RFCs or architecture docs, synthesizing information across multiple handbook pages, preparing for meetings by uploading agendas and background docs.

### Zoom AI Assistant

**Approval:** Approved (Orange)

**Reference:** [Internal AI Tool Usage Requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements)

Zoom's built-in AI assistant for meeting transcription, summaries, and action items. Generates post-meeting recaps automatically so attendees can focus on the conversation rather than note-taking.

**Common uses:** Auto-generated meeting summaries, extracting action items from recorded calls, catching up on meetings you missed.

### Gong

**Approval:** Approved (Orange, sales only)

**Reference:** [Internal AI Tool Usage Requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements)

AI meeting intelligence platform for sales calls. Records, transcribes, and analyzes customer conversations to surface insights, track deal progress, and coach reps.

> [!important]
> Approved for **customer/sales calls only**. Must not be used for HR conversations, legal meetings, internal personnel discussions, or any non-sales context.

**Common uses:** Reviewing customer call highlights, tracking objections across deals, sales coaching and enablement.

### Metaview

**Approval:** Approved (Orange, recruiting)

**Reference:** [Internal AI Tool Usage Requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements)

AI interview transcription and structured notes tool for the recruiting team. Automatically generates interview summaries and scorecards. **Requires candidate consent** before use — ensure the candidate has been informed and agreed to AI-assisted note-taking.

**Common uses:** Generating structured interview notes, reducing interviewer bias through consistent documentation, speeding up hiring feedback loops.

### Reclaim AI

**Approval:** Approved (Orange, request access)

**Reference:** [Internal AI Tool Usage Requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements)

AI-powered calendar and time-blocking assistant that automatically schedules focus time, breaks, and tasks around your existing meetings. Access must be **requested via Lumos** — it is not self-service.

**Common uses:** Protecting focus time on your calendar, auto-scheduling recurring habits (lunch, exercise), optimizing meeting-heavy weeks.

## Support agentic harnesses

They typically connect [Duo CLI](https://docs.gitlab.com/cli/duo/cli/) or `[OpenCode](https://opencode.ai/)` to GitLab and other systems through the [Model Context Protocol (MCP)](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/), and are tailored to ticket work, investigation, and workflow automation.

### duo-helper-image

**Approval:** Approved (Red)

**Reference:** [duo-helper-image](https://gitlab.com/gitlab-com/support/toolbox/duo-helper-image)

A governed containerized Support toolkit that packages `glab` + Duo plus Glean, GitLab MCP, Semantic Search, and Ticket Search over sanitized past Zendesk tickets.

**Common uses:**

1. Running `glab` and Duo in a ready-to-use, governed environment.
1. Searching sanitized historical tickets with semantic and ticket search.

### Request for Help (RFH) Agent - Search and Create issues

**Approval:** Approved (Red)

**Reference:** [Request for Help](https://gitlab.com/gitlab-com/request-for-help/)

An AI agent that lives in the RFH project, used to search for and create issues. As a Duo custom agent, it operates under Red data approval.

**Common uses:**

1. Finding existing RFH issues.
1. Creating new RFH issues directly from the RFH project.

### internal-soslab

**Approval:** Approved (Red)

**Reference:** [internal-soslab](https://gitlab.com/gitlab-com/support/toolbox/internal-soslab)

An agentic investigation harness for SOS bundles, logs, configs, screenshots, and ticket conversations. It provides Glean access and 27+ purpose-built MCP tools.

> [!note]
> The harness itself handles Red data locally, but its Glean integration is restricted to **Orange data only**.

**Common uses:**

1. Investigating SOS bundles and correlating logs and configs.
1. Reviewing screenshots and ticket conversations during deep-dive troubleshooting.

## Non-Approved Tools

The following AI tools are **not approved** for internal use in normal workflows. Using them with GitLab or customer data violates internal policy.

| Tool | Status | Notes | Reference |
|------|--------|-------|-----------|
| OpenAI ChatGPT / OpenAI API | ❌ Not approved | Direct use of OpenAI models for work is prohibited. A narrow exception exists for competitive analysis under the AI usage policy. | [Internal AI Tool Usage Requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements) |
| Microsoft / GitHub Copilot | ❌ Not approved | Both Microsoft Copilot and GitHub Copilot are explicitly prohibited for internal workflows. Limited competitive research may be allowed under policy. | [Internal AI Tool Usage Requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements) |
| Grammarly | ❌ Not approved | Being deprecated internally. Listed as not approved in the corporate AI tool policy. | [Internal Handbook – AI at GitLab](https://internal.gitlab.com/handbook/company/ai-at-gitlab) |

> [!note]
> If you need to evaluate a non-approved tool for competitive research purposes, consult the [AI Tool Usage Requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements) for the specific exceptions and approval process. When in doubt, ask in `#ai-security`.
