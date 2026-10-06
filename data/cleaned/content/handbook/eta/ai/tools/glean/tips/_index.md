---
title: "Glean Tips & Tutorials"
description: "Quick video guides and practical tips to help you get the most out of Glean, GitLab's AI Knowledge Platform."
---

{{% alert color="info" %}}

For comprehensive documentation on what Glean is, see the [Glean End User Guide](/handbook/eta/ai/tools/glean/).
{{% /alert %}}

## Getting Started

### How to Access Glean

**What you'll learn:**

- Logging in with Okta, app.glean.com, and mobile app
- Navigating the Glean interface for the first time
- Installing and using the Chrome browser extension

**Quick Tips:**

- Install on mobile for on-the-go searching
- Join [#glean-community](https://gitlab.enterprise.slack.com/archives/C0A897TSKNG) for questions

<div style="padding:56.25% 0 0 0;position:relative;">
  <iframe src="https://www.youtube.com/embed/Tkult5xOEk0"
    frameborder="0"
    allow="autoplay; fullscreen; picture-in-picture"
    style="position:absolute;top:0;left:0;width:100%;height:100%;"
    title="Descriptive Video Title"></iframe>
</div>

{{% alert color="info" %}}

Youtube link: [Confidential: Glean 101 - 1. Logging In](https://www.youtube.com/watch?v=Tkult5xOEk0&list=PL05JrBw4t0Ko6y092ciE_CMpGiYyKChFN&index=2)

{{% /alert %}}

### Search vs Assistant (Chat)

**What you'll learn:**

- When to use Search (finding specific documents, people, info)
- When to use Assistant/Chat (getting AI-generated answers and summaries)
- Examples of each in action

**Quick Tips:**

- Use Search when you know what you're looking for: "AMER swag process", customer names, specific documents
- Use Assistant when you want an answer: "How do I submit expenses?", "What's my Parental Leave policy?"

<div style="padding:56.25% 0 0 0;position:relative;">
  <iframe src="https://www.youtube.com/embed/dZY47FKcVfc"
    frameborder="0"
    allow="autoplay; fullscreen; picture-in-picture"
    style="position:absolute;top:0;left:0;width:100%;height:100%;"
    title="Search vs Assistant - Know the Difference"></iframe>
</div>

{{% alert color="info" %}}

Youtube link: [Confidential: Glean 101 - 2. Glean Chat and Search](https://www.youtube.com/watch?v=dZY47FKcVfc&list=PL05JrBw4t0Ko6y092ciE_CMpGiYyKChFN&index=3)

{{% /alert %}}

## Advanced Search Techniques

### Advanced Search Filters

**What you'll learn:**

- What systems Glean searches (Handbook, Slack, Salesforce, GitLab, Google Workspace, etc.)
- Using search filters to narrow results
- Combining multiple filters for precision

**Quick Tips:**

- Filter by source: `app:slack`, `app:gitlab`, `app:drive`
- Filter by date: `updated:today`, `updated:past_2_weeks`
- Filter by type: `type:issue`, `type:email`
- Combine filters: `customer-name app:salesforce updated:>7d`

### Fast Mode vs Thinking Mode vs Deep Research

**What you'll learn:**

- Understanding the three modes and when to use each
- How to switch between modes

**Quick Tips:**

- **Fast Mode (Default):** Use by default for your searches - document lookup, Q&A, summaries, drafting
  - _"Find expense policy", "Summarize this meeting", "Draft email response"_
- **Thinking Mode:** Use it for complex analysis requiring deep reasoning
  - _"Compare Q3 and Q4 approaches and recommend changes with trade-offs"_
- **Deep Research:** Use when you need a comprehensive report from multiple sources
  - _"Analyze our sales strategy across all customer segments and provide comprehensive recommendations"_

<div style="padding:56.25% 0 0 0;position:relative;">
  <iframe src="https://www.youtube.com/embed/FaRFgF39W5Y"
    frameborder="0"
    allow="autoplay; fullscreen; picture-in-picture"
    style="position:absolute;top:0;left:0;width:100%;height:100%;"
    title="Chat Modes"></iframe>
</div>

{{% alert color="info" %}}

Youtube link: [Confidential: Glean 101 - 3. Chat Modes](https://www.youtube.com/watch?v=FaRFgF39W5Y&list=PL05JrBw4t0Ko6y092ciE_CMpGiYyKChFN&index=4)

{{% /alert %}}

### GoLinks

**What you'll learn:**

- How to create custom shortcuts (GoLinks) for frequently accessed resources
- Where GoLinks work (Glean search and browser address bar)
- How to find and use existing GoLinks created by others
- When GoLinks are most useful (frequently shared resources, common processes)

**How to Create a GoLink**

From a search result:

- Search for the document or page
- Click the three dots (⋮) on the result
- Select "Create Go Link"
- Choose your shortcut name
- Expand "More options" if needed to set as "Unlisted" (Unlisted Go Links won’t appear for others anywhere in Glean. They can still be used by anyone you share the link with)
- Create

Create directly:

- From the Glean homepage, click "New" in the top-right corner
- Select "Go Link"
- Enter the destination URL
- Choose your shortcut name
- Expand "More options" if needed to set as "Unlisted" (Unlisted Go Links won’t appear for others anywhere in Glean. They can still be used by anyone you share the link with)
- Create

**Quick Tips:**

- Install the Glean browser extension to use GoLinks in your browser address bar
- Use team conventions: if your team calls it "the playbook," make it go/playbook
- Browse existing GoLinks before creating new ones to avoid duplicates - see the [complete list here](https://app.glean.com/knowledge/golinks)
- GoLinks work in Glean search and your browser address bar (type go/expenses and press Enter)

{{% alert color="warning" %}}
**Important Guidelines:**

- **Never point GoLinks to Slack threads or posts** - Slack content expires after 90 days and your GoLink will break.
- **Work content only** - Don't create GoLinks for memes, YouTube videos, personal content, or non-work resources.
- **Be specific and clear** - Future you (and related team members) should immediately understand what the GoLink leads to.
{{% /alert %}}

<div style="padding:56.25% 0 0 0;position:relative;">
  <iframe src="https://www.youtube.com/embed/dh4K5-fTmf0"
    frameborder="0"
    allow="autoplay; fullscreen; picture-in-picture"
    style="position:absolute;top:0;left:0;width:100%;height:100%;"
    title="GoLinks"></iframe>
</div>

{{% alert color="info" %}}

Youtube link: [Confidential: Glean 101 - 4. GoLinks](https://www.youtube.com/watch?v=dh4K5-fTmf0&list=PL05JrBw4t0Ko6y092ciE_CMpGiYyKChFN&index=5)

{{% /alert %}}

## Glean Agents

What you’ll learn:

- What Glean Agents are and when to use them
- The two main agent types (conversational and task-based)
- How example agents like _Morning Brief – Gamified Edition_ work
- How to start building your own agent

<div style="padding:56.25% 0 0 0;position:relative;">
  <iframe src="https://www.youtube.com/embed/oAm00iy36SA"
    frameborder="0"
    allow="autoplay; fullscreen; picture-in-picture"
    style="position:absolute;top:0;left:0;width:100%;height:100%;"
    title="Agents"></iframe>
</div>

{{% alert color="info" %}}

Youtube link: [Confidential: Glean 201 - 1. Agents](https://www.youtube.com/watch?v=oAm00iy36SA&list=PL05JrBw4t0Ko6y092ciE_CMpGiYyKChFN&index=6)

{{% /alert %}}

**What are Glean Agents?**

Glean Agents are no-code, permission-aware AI tools that use GitLab’s existing knowledge (Handbook, GitLab, Slack, Gmail, Calendar, Salesforce, and more) to perform tasks on your behalf.

Agents are intelligent workflows that:

- Collect inputs from you (and optionally on a schedule)
- Run through a series of actions (search, read, analyze, plan)
- Deliver a specific outcome (summary, plan, checklist, brief, etc.)

Agents are most useful for:

- High-volume, recurring activities
- Standardizable processes
- Time-intensive work with high-value outcomes
- Use cases where limiting data sources or adding specific context improves quality and consistency

**Agent types**

- **Conversational agents**: Chat-style agents that can answer a wide variety of questions using curated context (for example, the Duo Agent Platform Expert agent).
- **Task-based agents**: Automate a complex task end-to-end (for example, generating a morning brief or weekly summary from multiple systems).

![glean-agents1](/images/business-technology/enterprise-applications/guides/glean/agents2.png)

**Example: Morning Brief – Gamified Edition**

The _Morning Brief – Gamified Edition_ agent prepares a daily “dev quest” by pulling together everything you need to start your day, so you don’t have to manually search across tools.

It typically:

- Checks your assigned GitLab issues, merge requests, and related work items
- Scans recent Slack updates from the past day
- Reviews recent email activity from the last few days
- Looks at your calendar for upcoming meetings
- Aggregates and synthesizes all of this into an actionable, prioritized brief

**How agents work**

Under the hood, an agent is a set of connected action blocks that:

- Read from different data sources (for example, GitLab, Slack, Gmail, Calendar)
- Plan and think about what to do with the retrieved information
- Respond with a final, human-readable output tailored to the goal of the agent

This pattern is reused across many agent use cases. The main differences are which data sources are used and what the final response should look like.

**How to find and run agents**

1. In Glean’s left navigation, select **Agents**.  
2. Use search and filters to explore agents available to you.  
3. Click an agent to open its details, review the description and permissions, then select **Run agent**.  
4. For recurring workflows, use **Set schedule** so the agent runs automatically (for example, every weekday morning).

![glean-agents2](/images/business-technology/enterprise-applications/guides/glean/agents.png)

**Getting started with your own agent**

1. Go to **Agents** in the left navigation and select **Create agent**.
2. Choose how you want to build. Glean offers two modes, and you can switch between them at any time:
   - **Build with natural language (recommended starting point).** Describe what you want the agent to do, which systems it should use, and what the output should look like (for example, "Draft a concise Slack update for my project working group channel based on the latest issues, MRs, notes, and meeting docs"). Glean generates the steps for you.
   - **Build step by step (advanced).** Add triggers, actions, branches, memory, and sub-agents yourself. Use this when you need precise control over each step, conditional logic, custom actions, or sub-agents that work independently.
3. Or start from a template if there's one that fits. Glean ships templates for common patterns (daily action items, customer reference summaries, persona-based messaging, and more) which you can customise.
4. Test the agent, review the output, and iterate on the prompts and steps to improve quality and usability.
5. Once you're happy, optionally set a schedule or share the agent with relevant teams.

**Agent verification and sharing**

- **Verification:** To verify an agent in Glean, you must work with the Enterprise AI team. Individual users cannot verify agents themselves.  
- **Sharing:** To share your agent with everyone at GitLab, partner with the Enterprise AI team. Individual users can only share agents directly with specific team members.
- **Publishing agents:** Publishing options (for example, via API or Slack integration) are not enabled for all agents by default. To get publishing set up for your agent, work with the Enterprise AI team.

{{% alert color="info" %}}

To work with the Enterprise AI team, ask in `#glean-community` or tag `@glean-admin`.
{{% /alert %}}

**Quick tips for agents**

- Start from existing example agents (like _Morning Brief_ or _Weekly Summary & Plans_) and adapt them, rather than building from scratch.
- Keep each agent focused on a single clear outcome (for example, “prepare my morning brief” vs “do everything for my day”).
- When accuracy matters, review cited sources in the agent output before sharing with customers or leadership, just as you do with Assistant answers.

## Tips & Best Practices

### Search Best Practices

**Write clear, specific queries:**

- Include product names, customer names, or system names
- Use natural language: "How do I...?", "What's the process for...?"
- Start simple, add filters if needed

**Verify sources:**

- Always check where information comes from
- Open cited sources before using in customer-facing materials
- Cross-reference for critical decisions

**Use quotation marks:**

- Put exact phrases in quotes for precise matching
- Example: "expense reimbursement policy" finds that exact phrase

### Chat/Assistant Best Practices

**Ask clear questions:**

- End questions with a question mark (?)
- Include relevant context: "Can you find recent support tickets from Zendesk for CustomerX?"
- Specify systems when needed: "Search Slack for discussions about ProjectY"

**Verify AI answers:**

- Check cited sources before acting on information
- Especially important for customer-facing content or policy decisions
- Sources are linked in every AI response

## Need Help?

Can't find what you're looking for in these videos?

- Check the [Glean End User Guide](/handbook/eta/ai/tools/glean/) for detailed documentation
- Ask in [#glean-community](https://gitlab.enterprise.slack.com/archives/C0A897TSKNG) on Slack
- Tag @glean-admin for technical issues

---

**Videos are added as they're created - check back regularly for new content!**
