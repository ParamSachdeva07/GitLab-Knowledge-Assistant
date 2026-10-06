---
title: "Glean End User Guide"
description: ""
---

## Glean End User Guide

Glean is GitLab's AI Knowledge Platform, used to find people, documents, issues, tickets, and conversations across our internal tools in one place.

This page is for all GitLab team members as a quick reference for why Glean exists, what it does, how to use it, and how to get help or request changes.

## Why Glean

GitLab's knowledge is spread across many systems (external and internal handbooks, GitLab.com, Highspot, Slack, Salesforce, Snowflake, Google Workspace, Gong, etc.).

This creates a few consistent problems:

- **Fragmented knowledge** - important information exists, but it is hard to know where to look.
- **Time lost searching** - team members report spending multiple hours per week searching across tools instead of doing work.
- **Conflicting answers** - multiple "sources of truth" sometimes disagree, making it unclear which to trust.
- **Onboarding friction** - new team members in particular struggle to find the "right" doc, issue, or policy quickly.

Glean exists to make it fast and reliable to find what you need, so you spend more time acting on information and less time hunting for it.

## What Glean does

At a high level, Glean:

**Unifies search across tools**

- Connects to high-value systems (for example: GitLab handbooks, GitLab.com, Salesforce, Gmail, Google Drive, Slack, Highspot, Gong, and others over time).

**Uses AI to answer questions**

- Understands natural language queries and can summarize or combine results into a concise answer, with links back to the original sources.

**Respects existing permissions**

- You only see information you already have access to in the source system (for example, Gong, Google Drive, Salesforce). Glean does not create new access or bypass any security controls.

**Aligns to source retention**

- Indexed content follows the retention policies of the underlying tool (for example, Gong data is retained for ~365 days, and removed from Glean shortly after it is deleted in Gong).

**Is not a performance-monitoring tool**

- Glean is a search and knowledge discovery platform; it is not used to introduce new employee performance monitoring or evaluation signals.

### Connected Systems

Glean searches across the below applications (you only see what you're authorized to access):

- **GitLab.com Namespaces** (Projects, Issues, Merge Requests, Epics):
  - `gitlab-com`
  - `gitlab-org`
  - `gitlab-data`
- **Websites:**
  - Marketing site (about.gitlab.com)
  - GitLab Docs (docs.gitlab.com)
  - Public Handbook (handbook.gitlab.com)
  - Internal Handbook(internal.gitlab.com/handbook/)
- **Communication:** Slack, Gmail, Google Calendar, The Loop
- **Sales & Customer:** Salesforce, Gong, Highspot
- **Files & Docs:** Google Drive
- **Other:** Okta People Data

_Additional systems will be connected over time._

## How to use Glean

### Access

**Web app**, either:

- Open Okta, search for the Glean tile, and launch the app.
- Go to https://app.glean.com and sign in with Okta

**Browser extension (recommended):**

- From the Glean web app, install the Chrome extension for quick access and in-page sidebar search.
- We would also recommend accepting the option to replace the "new tab" experience.
- However, this is optional and can be rolled back if you decide in future that you don't like it!

**Mobile or desktop app:**

- Download the [Glean app](https://www.glean.com/download-glean) for
  - Mobile: iOS App Store or Google Play Store
  - Desktop: macOS App Store
- Sign in with Okta to search GitLab information on-the-go.

### Navigating the Homepage

The Glean homepage uses a unified **composer** as the primary entry point for search, questions, and actions.

**Composer**

![glean-composer1](/images/business-technology/enterprise-applications/guides/glean/composer.png)

The composer sits at the top of the homepage. As you type, search results appear immediately below. You can grab a direct link to any result without leaving the page.

The composer defaults to `Chat` mode. Pressing `Enter` or clicking `Ask` opens the full chat interface where you can continue the conversation. Within the composer you can:

- Apply filters (source, type, owner, etc.)
- Attach files or tag people

To go directly to the search page with your query pre-populated, click the search icon on the left sidebar.

![glean-composer3](/images/business-technology/enterprise-applications/guides/glean/composer3.png)

**Focus Cards**

Focus cards surface ongoing activities, @-mentions, and actions that may need your attention. You can read context inline or open the item directly to act on it.

![glean-composer2](/images/business-technology/enterprise-applications/guides/glean/composer2.png)

**Other homepage sections**

The following sections remain available on the homepage and are unchanged:

- **Today** — your upcoming schedule
- **Trending Documents** — what's popular across the company
- **Suggested**, **Recent**, and **Mentions**

### When to use Search vs Chat

**Use Search** when you know roughly what you're looking for:

- Examples: AMER swag process, GitLab for Slack app docs, a specific customer or project name.

**Use Chat** when you want a synthesized answer:

- Examples: "How do I request a new internal SaaS license?", "Where is the process for internal hiring?"

{{% alert color="info" %}}
**Learn More:**

For detailed walkthroughs of Glean's core features:

- Check Glean's [Search Video Overview](https://www.loom.com/share/7e46955f169041d7b22dcfb0bcc89352) for how to use search functionality
- Check Glean's [Assistant (Chat) Video Overview](https://www.loom.com/share/c6ff87293baf4ba5b1a35f10db691cbc?sid=e50a46cb-2723-4f64-851c-05570983b145) for how to use chat functionality
{{% /alert %}}

## Good practices

- Start with a short, specific query (include product, customer, or system names).
- Use filters (source, type, owner, etc.) to narrow results where needed.
- When Assistant gives an answer, open the cited sources before using content in:
  - Customer-facing materials.
  - Legal, security, or policy decisions.

{{% alert color="info" %}}
**Need inspiration for what to ask?**

Check [Glean's Own Chat Prompting Guide](https://docs.google.com/document/d/1YGd8k-8DLS2oaUF6TgdxnVpBXIywUJsEwRUwGe2kpyE/edit?tab=t.0) (created by Glean) for example questions and use cases.
{{% /alert %}}

### Using Fast Mode vs Thinking Mode

Glean Chat offers two modes for different needs:

**Fast Mode (Default - Your Go-To for Nearly Everything):**

- Best for: Document search, Q&A, analysis, summarisation, writing assistance, research
- Speed: Near instant responses (2-5 seconds)
- When to use: Your default choice for virtually all tasks
- Examples: "Talk me through the expense policy", "Draft an executive summary of the Acme Corp account", "Summarise the key decisions from this meeting", "Draft a response to this customer"

**Thinking Mode (Specialised Tool for Complex Reasoning):**

- Best for: Multi-step analysis requiring deep reasoning, highly complex problem-solving
- Speed: Slower responses (10-30 seconds)
- When to use: Only when you need extended reasoning chains or if Fast mode's answer lacks depth
- Examples: "Compare our Q3 and Q4 sales approaches and recommend changes with trade-offs", "Analyse this quarter's data and create a strategic plan with dependencies"
- Cost: Uses significantly more computing resources

{{% alert color="warning" %}}
Start with Fast mode - it handles sophisticated tasks brilliantly. Only switch to Thinking mode if you need deeper reasoning or if Fast mode's answer isn't sufficient.
{{% /alert %}}

## Ownership

Primary ownership of Glean sits with the AI Engineering team, within Enterprise Technology & AI (ETA):

- Vision, roadmap, and prioritization.
- Internal enablement and usage patterns.
- Day-to-day administration

## Community & discussion

For day-to-day questions and community tips:

Join [**#glean-community**](https://gitlab.enterprise.slack.com/archives/C0A897TSKNG) on Slack for:

- "How do I…?" questions.
- Sharing useful queries, patterns, and examples.
- Non-urgent feedback or suggestions.

For obvious bugs or outages:

- Post in [**#glean-community**](https://gitlab.enterprise.slack.com/archives/C0A897TSKNG) with a short description and (where possible) a screenshot and URL.
- Tag `@glean-admin` team in the slack message

### Share Your Best Practices

Found a great way to use Glean? Help other team member by sharing your use case!

**How to share:**

1. In [**#glean-community**](https://gitlab.enterprise.slack.com/archives/C0A897TSKNG), type `/share` in the message box
2. Select "Glean - Share Glean Use Case"
3. Fill out the quick form (2-3 minutes)
4. Submit!

Your examples may help others discover new and interesting ways to use Glean.

### Build a Glean Agent

All GitLab team members can build their own Glean agents through Glean's Agent Builder. Two modes are available, and you can switch between them at any time during building:

- **Natural language.** Describe what you want the agent to do in plain English, and Glean generates the steps for you. The best place to start.
- **Advanced, step by step.** Build the agent manually with triggers, actions, branches, memory, and sub-agents. Use this when you need precise control over each step, conditional logic, or custom actions.

Templates are available as starting points (daily action items, customer reference summaries, persona-based messaging, and more), and you can customise them to fit your needs.

For the full how-to, see Glean's [agents documentation](https://docs.glean.com/agents/) and the [Glean Tips & Tutorials](./tips/) page for GitLab-specific guidance.

**What still goes through Enterprise AI:**

- **Agent verification.** The "verified" badge that signals an agent is trusted for broad use is granted by the Enterprise AI team.
- **Function-wide rollout.** Sharing an agent across an entire function, rather than directly with specific colleagues, is coordinated with the function's ATO and Enterprise AI.
- **Custom actions and connector changes.** New write-back actions, new data sources, or changes to indexed connectors go through Enterprise AI for security, privacy, and licensing review.
- **Publishing modes.** Publishing via the API, scheduled execution, or Slack integration is not enabled for all agents by default. Work with Enterprise AI to set these up.

Raise any of the above in [**#glean-community**](https://gitlab.enterprise.slack.com/archives/C0A897TSKNG) or via the [**Enterprise AI Intake Request**](https://gitlab.com/groups/gitlab-com/eta/ent-ai/-/work_items/new?type=EPIC&initialCreationContext=list-route).

## Requesting new data connectors

If you need Glean to index a new system (or make a major change to an existing connector), please use the [**Enterprise AI Intake Request**](https://gitlab.com/groups/gitlab-com/eta/ent-ai/-/work_items/new?type=EPIC&initialCreationContext=list-route) so Enterprise Applications and AI Engineering can review security, privacy, and licensing.

**To request a new data connector:**

1. Post your request in the [**Enterprise AI Intake Request**](https://gitlab.com/groups/gitlab-com/eta/ent-ai/-/work_items/new?type=EPIC&initialCreationContext=list-route)
2. Include:
   - System name and business owner
   - Data classification (public, internal, restricted/red)
   - Who needs it and typical use cases
   - Any timelines or dependencies (for example, specific customers or projects)

The owning teams will review, prioritize, and respond.

## Frequently Asked Questions (FAQ)

### Can people see what I'm searching

No, your search history is private.

### Will my private data or documents be searchable by others?

No, your private information remains private. Glean mirrors the permissions in our connected applications. For example, some Slack channels are private; only members of a private channel will see conversations shared in that channel.

### Can I verify where Glean is getting its answers?

Yes! Glean's answers reference the source materials within our content so you can always check that it is referencing the latest and greatest.

### My colleague and I asked Glean the same question, but we got different answers: why?

Glean searches and generates a response based on the specific documents and resources that each person can access, what that person interacts with the most, and more, so answers can vary because the user's context can vary.

### I noticed that Glean has some results from my browser history. How did it get that?

When you install the browser extension, Glean will use your history to make it easy to navigate to recent documents in enterprise apps that do not have full support, no-code apps and general collaboration. This is based on your browser history and this data is personal to you so it is not stored anywhere else.

### Does Glean understand and use my GitLab To‑Dos?

Not yet. The current GitLab connector does not have first‑class support for To‑Dos, so asking Glean to prioritize “all my To‑Dos” may confuse it or lead to incomplete answers. We see To‑Do integration as a high‑value improvement and are discussing it with Glean.

### How often does Glean sync with GitLab?

Glean uses a combination of initial crawls, incremental “updatedAfter” API queries, and webhooks. Most updates are near‑real‑time once webhooks and incremental flows are correctly configured. If you see “recently created documents may not yet be available,” it usually means that the item is in a namespace not yet ingested, or the webhook or incremental update hasn’t processed it yet.

### What Salesforce data can Glean use?

Currently Glean's Salesforce Connector only indexes the following objects: Account, Case, Opportunity, Task. If there is an object you would like to see indexed, share your use case and  reasoning in #glean-community.

### Does Glean index Salesforce reports?

Glean’s connector does index some reports, but in practice the value is mostly in helping you discover the right reports (names, metadata, where they live) rather than deeply querying the report data itself. Permissions mapping on some reports is still being debugged, so you might see “no access” even when you can open the report. This is an active integration issue.

### Will Glean search or reference my private Slack channels and direct messages?

By default, no. You must opt in:

- Go to Glean → Settings → Data sources → "Slack Real Time Search Enterprise".
- Enable the option to include private channels and DMs.
- After that, Glean will return private content and show it **only to you**. There can be a delay of a few hours after you toggle this while permissions sync.

### Does Glean respect Slack and other system retention policies?

Yes. Glean inherits retention from the source systems. If Slack messages are deleted or aged out (e.g., 90‑day retention), Glean will also stop showing them. There is no separate, longer‑lived archive of Slack inside Glean.

### How do I enable the Glean Daily Digest in Slack?

_Note:_ This feature is currently not working, Glean are aware, and are working on fixing it. It is as a result of the recent Slack ToS changes, forcing them to adapt the way in which this feature works.

In Slack:

- Open the Glean app → Home tab
- Click Manage Digest Settings
- **To enable:** Set to On and choose your preferred cadence and channels, then save
- **To disable:** Set to Off and save
- **To stop reminders:** Click "Not interested" on the Daily Digest prompt to stop repeat reminders

### Is there a daily Slack digest for specific channels?

Yes. The Glean Slack app can send a daily channel digest:

- You select which channels to monitor.
- At ~9:00 AM (local or configured time), you receive a summary of key conversations, topics, and participants, with links back into Slack.
- This is useful for high‑traffic channels you can’t fully read.

### Can I use /glean [query] inside Slack threads?

Currently, the /glean slash command works in the channel main context, not within threaded replies. This is a limitation of Glean’s current Slack command implementation.

### How do I add the Glean Slack app (Gleanbot) to a Slack channel and control when it responds?

We recommend adding Glean to channels where it will be genuinely useful, and configuring it so that it only responds when explicitly asked. This keeps noise (and AI cost) low while still making Glean easy to use.

**1. Add Glean to a Slack channel**

You can only do this in channels where app installation is allowed for our workspace:

- In Slack, open the channel where you want to use Glean.
- In the message box, type `/` and select **Add apps to this channel** (or use the channel header → **Integrations** → **Add an app**).
- Search for **Glean** and add it to the channel.

**2. Configure how often Glean responds in that channel (recommended: “Don’t respond”)**

By default, we recommend that Glean **does not** auto‑respond to channel‑level questions. Instead, Glean should respond only when someone explicitly asks it to (for example with `@Glean` or `/glean`), to avoid unnecessary channel noise.

To set this up:

- In the Slack channel, type:

  ```text
  /glean configure
  ```

- In the configuration dialog, under **Channel level messages**, select **Don’t respond** (GitLab recommended default).
- Save your changes.

With this setting:

- Glean **won’t** automatically jump into normal channel conversations.
- Team members can still:
  - Use `/glean <query>` to search from within the channel.
  - Mention `@Glean` when they explicitly want an answer or summary. (In a message or thread!)
- Responses remain personalised and permission‑aware, based only on what the requesting person can access.

**3. When to enable more proactive responses**

In some curated channels (for example, a dedicated **#XYZ-help** or **#internal-how-to** channel), it may make sense for Glean to respond more proactively. In those cases:

- Use `/glean configure` in the channel.
- Choose a more permissive option under **Channel level messages** (for example, respond when confident).
- Coordinate with **@glean-admin** before enabling broad auto‑responses, to balance usefulness, signal‑to‑noise, and cost.

**Further reading**

- Glean docs – **Enable Gleanbot to respond in Slack channels** (covers channel settings, “Don’t respond”, and workspace‑level controls):
  https://docs.glean.com/administration/platform/embedded-integrations/slackbot/use-glean-in-slack/respond-in-slack-channels
- Glean docs – **Glean in Slack (Gleanbot) overview**:
  https://help.glean.com/en/articles/6581357-glean-in-slack

### How does Glean handle security, data classification, and permissions?

- Glean is authorized for Orange data.
- Glean respects all source‑system permissions. It does not see anything you cannot see natively.
- Browser integration (Glean Companion) has no access to page content in your browser unless you explicitly highlight and send to Glean, or if permission is explicitly given to allow it to summarize a full page.
- GitLab remains the data controller. Glean operates under strict DPA, security, and privacy reviews and a zero‑day AI usage retention policy.

Team members are still responsible for not pasting Red data into tools authorized only for Orange.

### Does Glean retain or expose data beyond what the underlying tools do?

- No. Glean’s retention aligns with each source system, and search results disappear once content leaves the source (e.g., Slack retention). It does not keep an independent long‑term copy that bypasses Slack/Drive/GitLab policies.

### What models does Glean use? Are we tied to a single LLM vendor?

Glean is multi‑model:

- It can route to Anthropic, Google, OpenAI, and others behind the scenes.
- GitLab controls which models are used for which use cases.
- Glean abstracts cost as “Glean credits” rather than tokens. Credits depend on model complexity, context length, and output size.

### When should I use Glean vs Claude?

Claude is GitLab's desktop AI for getting work done: drafting, reasoning, code, multi-step agentic tasks. Glean is GitLab's personal AI for knowledge management and personal-scope automation, grounded in our internal systems.

The two complement each other: Claude has a Glean connector built in, so you can pull GitLab context into a Claude conversation without switching tools. Use the right tool for the job, not one over the other.

**Important**: Glean does not train on our data. It uses LLMs with GitLab context, but the underlying models are not fine‑tuned on our internal content.

### Can I use Glean and Claude together?

Yes, connecting the two is possible. Go to [https://claude.ai/customize/connectors](https://claude.ai/customize/connectors) and connect Glean. Once set up, Claude can search and retrieve from Glean's indexed GitLab sources mid-conversation, giving you the best of both: Claude's advanced reasoning and writing capabilities grounded in real GitLab context.

This is especially useful when you need to:

- Draft a document that requires pulling in internal research.
- Synthesize information across multiple systems in one response.
- Answer complex questions where depth of analysis and company-specific accuracy both matter.

**Important**: Permissions are fully respected. Claude will only surface content you already have access to in Glean.

### Can I create my own Glean agents?

Yes, all GitLab team members can build their own. See [Build a Glean Agent](#build-a-glean-agent) above for the two building modes (natural language and step-by-step advanced), templates as starting points, and the bits that still go through Enterprise AI (verification, function-wide rollout, custom actions and connector changes, and publishing modes).

### Can I create my own collections in Glean?

By default, team members cannot self‑create collections. Today, Glean admins can create a collection for you and make you an owner (e.g., “Legal Service Desk”, “Environment Automation”, “PS Essential Documentation”). This is our interim governance model. Long‑term we aim for more self‑service with good lifecycle practices.

### How do permissions work inside collections?

Collections respect the underlying document permissions. If you add a doc but a viewer lacks access, they’ll see an “Item needs access” placeholder and cannot open it. Collections are a discovery/curation layer, not a way to bypass ACLs.

### Can I rename chats or organize them into projects/folders?

Chat naming and grouping are not yet available, though chat renaming is on Glean’s roadmap and has been explicitly requested. For now, you need to rely on recency and content when finding past chats.

### Is Glean allowed to write back to Google Docs, Slack, or other systems (export, send, create)?

Yes. Glean can now export content to Google Docs, create Gmail drafts, and draft content for Slack, and we’ll continue adding more actions over time as they’re enabled.

### Why did the Glean extension change my browser’s new tab page, and can I change it back?

The extension can set Glean as the default new tab / home view. You can:

- Decline this during install, or
- Later disable it via the extension settings.

We would still highly recommend using the Glean extension, even if you do not intend to change your default landing page.

### Does Glean support Google Docs comments and action items?

Currently, the Google Drive connector indexes the body text of Docs but does not flatten inline comments into the searchable body. That’s why “add comment” actions in Docs may not show up when you ask Glean for “action items from this doc.” This is logged as a feature request with Glean.

### Does Glean show “mentions” based on @‑mentions in docs?

The Mentions view is largely driven by @‑mentions of your user in documents, sometimes including historical mentions that were later edited/deleted, and how we use agenda templates (which can over‑surface recurring docs where you’re mentioned). If you see a mention in Glean but not in the current doc, it may have been present in a previous version.

### Can Glean replace our existing knowledge‑management systems (handbooks, Highspot, etc.)?

No. Glean is not a source of record. It is an index and assistant over existing sources. We will continue to maintain content in handbook.gitlab.com, GitLab repos, Google Docs, Highspot, etc. Use Glean to surface and unify that content. Any consolidation or rationalization of content systems is a separate strategy.

### Can I connect Glean to other AI tools (e.g., make Claude call Glean)?

Yes, in some cases. Glean now exposes an approved MCP server that you can connect from tools like Claude Code (and other MCP-aware clients such as OpenCode) so they can search and retrieve from Glean’s indexed GitLab sources mid-conversation. For setup details and security guidance, follow the [Setting Up the Glean MCP Server](https://internal.gitlab.com/handbook/ai-security-at-gitlab/guides/setup-guides/glean-mcp-setup/) instructions in the AI Security handbook.

### Can I opt out of Glean scanning my Gmail?

Yes. If you don’t want Gmail content indexed in Glean, you can opt out by adding yourself the Google Group `glean-gmail-opt-out@gitlab.com`. Glean is configured to exclude all members of this group from Gmail scanning.

### Why do I see an OAuth authentication error when connecting to the Glean MCP server?

This error appears when the locally cached OAuth client registration becomes stale or corrupt. It has been reported when connecting tools like opencode to the Glean MCP server:

```text
Client authentication failed (e.g., unknown client, no client authentication included,
or unsupported authentication method). The requested OAuth 2.0 Client does not exist.
```

Clear the cached credentials and trigger a fresh registration:

1. Remove stored credentials: `opencode mcp logout glean_default`
2. Delete the auth file: `rm ~/.local/share/opencode/mcp-auth.json`
3. Trigger a fresh re-auth: `opencode mcp auth glean_default`
