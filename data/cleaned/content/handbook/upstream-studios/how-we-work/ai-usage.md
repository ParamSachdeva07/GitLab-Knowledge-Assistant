---
title: "AI usage"
description: "Learn when to use AI for design work: Best practices, what to avoid, and how to keep users at the center."
date: 2026-06-15
---

This page covers how to use AI for Upstream Studios work — research, design, prototyping, documentation, and more.

If you want to know how to **work on AI experiences**, see [these resources](/handbook/product/ai/#design-and-ux-research-for-ai-features).

## Before you start

Read these before using AI tools at GitLab:

- [AI usage requirements and FAQs](https://internal.gitlab.com/handbook/company/ai-at-gitlab/#usage-requirements-and-faqs) (internal)
- [General purpose AI tool usage requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements/) (internal)
- [Communicating when using generative AI tools](/handbook/communication/#communicating-when-using-generative-ai-tools)

## Approved tools

| Tool | Best for |
|---|---|
| Claude | Research, writing, analysis, general tasks |
| Claude Design | Visual design, prototypes, slides, wireframes, mockups |
| Claude Code | Coding tasks, agentic development, MR reviews |
| Dovetail | Interview transcriptions |
| [FigJam](https://help.figma.com/hc/en-us/articles/16822138920343-Use-AI-tools-in-FigJam) | Whiteboards and diagrams |
| [Figma Design](https://help.figma.com/hc/en-us/articles/23870272542231-Use-AI-tools-in-Figma-Design) | Content, images, design, basic prototypes |
| [GitLab Duo](https://docs.gitlab.com/user/gitlab_duo/) | GitLab and software development tasks |
| Rally | Interview transcriptions |

**Note:** Figma Make is a prototyping tool that is available with paid Figma seats. Consider Claude Design or Claude Code first to avoid running out of available credits.
Our [Tech Stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml) may list other tools with AI features you can use.

## What AI is good for

Use AI as a creative helper and critic — not a replacement for judgment or user research.

**Feedback**

- Review documents, images, and Figma links with Claude
- Ask [GitLab Duo Code Review](https://docs.gitlab.com/user/project/merge_requests/duo_in_merge_requests/#have-gitlab-duo-review-your-code) to review a merge request
- Use AI to get quick feedback before asking a colleague for expert review

**Research**

- Draft study plans, interview guides, survey questions, and usability test tasks (Claude)
- Transcribe interviews with [Dovetail](https://docs.dovetail.com/help/transcribe-and-translate) or [Rally](https://help.rallyuxr.com/en/articles/9213503-observer-rooms), then analyze in Claude
- Summarize background info and find references (GitLab Duo for GitLab info, Claude for web research)
- Spot patterns and themes in data — always verify claims and ask for sources
- Draft personas and proto-personas — mark hypothetical ones clearly and validate with real users

**Design**

- Explore multiple design directions, edge cases, and error states quickly
- Write and iterate on UI text: error messages, tooltips, empty states, and microcopy
- Adjust tone to match [GitLab's brand voice](https://design.gitlab.com/content/voice-tone)
- Replace placeholder content with real UI text
- Generate wireframe starting points — treat as first drafts, not final designs
- Check designs for accessibility issues: color contrast, focus order, label clarity

**Prototyping**

- Build basic prototypes with Figma Design
- Build functional prototypes with Figma Make (supports Pajamas components) or Claude (generic UI)

**Diagrams and workshops**

- Prepare whiteboards and sticky note exercises with FigJam
- Create diagrams, mind maps, and flowcharts. Claude and GitLab Duo support [GitLab Flavored Markdown diagrams](https://docs.gitlab.com/user/markdown/#diagrams-and-flowcharts)

**Documentation**

- Draft, improve, and restructure documentation with Claude or GitLab Duo
- See [how to use AI for GitLab documentation](https://docs.gitlab.com/development/documentation/ai_guide/)

See also: [UX Research Prompts](https://gitlab.com/gitlab-com/office-of-the-ceo/ai-at-gitlab/ai-at-gitlab-usecases/-/issues/64) (internal) for research-specific prompts.

## What AI is not for

- **Replacing real users:** AI cannot simulate real behavior, emotions, or context. Never use AI feedback as a substitute for user research.
- **Final designs without review:** Every AI-generated design that reaches users must be reviewed, refined, and owned by a human.
- **Sensitive or high-stakes decisions:** Security, privacy, and accessibility require careful human oversight.
- **Skipping Pajamas:** Always verify AI-generated design patterns and components conform to [Pajamas](https://design.gitlab.com/).
- **Production output without checking:** Never ship AI-generated content without human review.
- **Tasks that are faster done manually:** If you have spent 30 minutes on a prompt, it may be quicker to do it yourself.

## Using AI well

### Write good prompts

Provide rich context in every prompt:

| Include | Example |
|---|---|
| **Role and audience** | "You are a UX designer on a DevSecOps platform. The user is a senior engineer managing CI/CD pipelines." |
| **Specific task** | "Write three error messages for when a security scan fails during a merge request pipeline." |
| **Constraints** | "Follow GitLab's Pajamas design system. Use sentence case. Keep under 80 characters." |
| **Examples** | "Here is an existing message we use: X. Match this tone and format." |
| **Success criteria** | "Explain what failed, why it matters, and what the user can do next." |

Iterate through conversation rather than starting over. Ask for 3-10 variations and combine the best parts.

Use [Claude projects](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects) to store persistent context like personas, design principles, and style guides.

### Review everything

Before sharing any AI output:

- Own it. Review, edit, and take responsibility before sharing
- Fact-check all claims, numbers, and statistics
- Check for bias. Ask if any group could be misrepresented
- Verify accessibility suggestions against [WCAG guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) and test with assistive technologies
- Validate designs with real users. AI output is a hypothesis, not a finding
- Disclose AI involvement. Note which parts of your deliverable used AI help ([disclosure requirements](https://internal.gitlab.com/handbook/ai-security-at-gitlab/ai-tool-usage-requirements/#attribution-of-published-content))

### Stay current and share

The AI landscape changes fast. Share what you learn with the team:

- [AI at GitLab Tips](/handbook/tools-and-tips/ai/)
- [AI use cases and prompts project](https://gitlab.com/gitlab-com/office-of-the-ceo/ai-at-gitlab/ai-at-gitlab-usecases) (internal)
- [Company learning resources](/handbook/people-group/learning-and-development/#team-member-resources)
- Have a suggestion? Open an issue in the [GitLab Design project](https://gitlab.com/gitlab-org/gitlab-design/issues/)
