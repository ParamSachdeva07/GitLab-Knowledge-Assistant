---
title: "Editing the Handbook"
description: "Choose an editing method, preview your changes, and prepare a handbook merge request."
---

Start with the handbook page you want to improve. You can edit in your browser,
use a local editor, or ask an agent to help. Every method produces a merge request
(MR) where you can review the changes and request the appropriate approval.
For how and why we use the handbook, see [handbook usage](../handbook-usage.md).

## Choose how to edit

Choose a starting point for your task. You can switch methods as you work.

### Make a change

| What you want to do | Start here |
| --- | --- |
| Correct a sentence or link on one page | [Single-file editor](#edit-one-file-in-your-browser) |
| Edit several files in your browser | [Web IDE](#use-the-web-ide-to-edit-the-handbook) |
| Move a page and update its links | [Move or rename a page](#move-or-rename-a-page) |
| Use an agent, an app, or a local editor | [Choose your editing environment](#choose-your-editing-environment) |

### Check or finish an MR

| What you want to do | Start here |
| --- | --- |
| Preview your changes | [Review app](#preview-changes-on-gitlab-pages) or [local preview](#local-live-preview) |
| Fix formatting or link-check errors | [Fix linter errors](#fix-linter-errors) |
| Resolve conflicting changes | [Fix merge conflicts](#fix-merge-conflicts) |
| Request review and merge | [Review and submit](#review-and-submit-your-change) |

### Choose your editing environment

Start with where you already work:

- **In GitLab or a connected app:**
  - In the GitLab project → [Agentic Chat or Developer Flow](#ask-an-agent-in-gitlab).
  - In Glean → [Glean desktop app](#handbook-edits-with-glean).
  - In Claude → [Claude Desktop](#handbook-edits-with-claude-desktop).
  - In a Slack discussion → [GitLab Duo in Slack](#turn-slack-discussions-into-handbook-updates).
- **In a local checkout:**
  - Edit files yourself → [Edit locally and let GitLab check your changes](#edit-locally-and-let-gitlab-check-your-changes).
  - Ask an agent to edit → [VS Code, GitLab Duo CLI, or Claude Code](#use-an-agent-in-your-editor-or-terminal).
  - See changes as you edit → [Local live preview](#local-live-preview).

Use the [public handbook repository](https://gitlab.com/gitlab-com/content-sites/handbook)
for public content and the [internal handbook](https://gitlab.com/gitlab-com/content-sites/internal-handbook)
repository for internal content. Shared theme and development documentation live
in [Docsy GitLab](https://gitlab.com/gitlab-com/content-sites/docsy-gitlab).
Check the [SAFE framework](/handbook/legal/safe-framework/) before moving internal information into public content.

> **Tip**: The page's **View page source** action helps identify the source.
> You can also see the page maintainers, which helps assign reviewers later.

![Handbook page with upper right corner page, View page source](/images/handbook/about/editing-handbook/handbook-edit-page-upper-right-corner.png)

### Need help?

👋 If you run into trouble editing the GitLab Handbook, help is available.

Team members, referred to as [MR Buddies](/handbook/people-group/general-onboarding/mr-buddies/),
are available to help you create a merge request or debug any problems you might run into while
updating the GitLab Handbook. Post your request with a link in the [`#mr-buddies`](https://gitlab.slack.com/archives/CLM8K5LF4/p1678812429884979)
Slack channel.

For general questions about the handbook, post in the [#handbook Slack channel](https://gitlab.enterprise.slack.com/archives/C81PT2ALD).
For more urgent problems, especially ones that are time sensitive or prohibiting access to
important information, there is an [escalation process](../escalation.md#when-to-escalate-an-issue)
to reach out to team members who are able to help resolve the problem.

## Common editing workflows

For a small correction on a known page, the single-file editor is a quick starting point.
An agent can help when you need to find the right files, update several pages, or
troubleshoot a failed check. Choose the method you're comfortable with and review
the resulting changes.

> These examples draw on extensive hands-on use of agentic workflows during FY27. Tools and interfaces
> can change. If you find a better approach or something that no longer works, please update
> this guide with what you learned and share the MR in
> [#handbook Slack](https://gitlab.enterprise.slack.com/archives/C81PT2ALD). Thanks!
>
> Want to learn together? Schedule a coffee chat with
> [Michael Friedrich (@dnsmichi)](https://gitlab.com/dnsmichi) to explore these workflows.

### Edit one file in your browser

Use this for small changes that do not require updating several files together.

1. On the handbook page, select **View page source**.
1. In GitLab, select **Edit > Edit single file**.

   ![Single file edit in GitLab](/images/handbook/about/editing-handbook/handbook-edit-single-file-source-edit.png)

1. Make the correction and review the diff changes.
1. Commit to a new Git branch and create an MR. Explain why the change is needed in the description.
1. Follow [review and submit](#review-and-submit-your-change).

For follow-up edits, open the file on the existing MR branch. Use the Web IDE or
an agent for changes spanning multiple files, including page moves and incoming links.
See the [Web Editor documentation](https://docs.gitlab.com/user/project/repository/web_editor/).

### Edit with GitLab Duo in the UI

Ask GitLab Duo to find the right pages, plan an update, or help make changes directly
from the handbook project in your browser.

> **Repository instructions:** The handbook provides [AGENTS.md](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/main/AGENTS.md)
> for agent editing and validation, and [Duo code review instructions](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/main/.gitlab/duo/mr-review-instructions.yaml)
> for reviewing MRs. GitLab Duo loads these instructions automatically, so you can
> focus your prompt on the intended change.

#### Ask an agent in GitLab

Open the handbook project in GitLab. On the right side panel, open [GitLab Duo Agentic Chat](https://docs.gitlab.com/user/gitlab_duo_chat/agentic_chat/)
and prompt it with your questions.

1. Ask for help with a specific task, or a good planning strategy for larger updates.
   Example prompt:

   ```markdown
   I want to add the #gitlab-gtm Slack channel to Product and Technical Marketing in https://handbook.gitlab.com/handbook/marketing/
   Can you help me make the handbook changes please?
   ```

1. Search through Git commit history and merge requests to understand why changes were made.
   Example prompt from a conversation between Elsje Smart and Michael Friedrich:

   ```markdown
   I need to find a Git change to the sales development handbook page, which lived in marketing and was recently moved to sales.

   The change is around performance management, made by Brian Tabbert. Time around Jan 2024 and Feb 2025.
   ```

1. Find existing merge requests and proposed changes to avoid duplicated work.
   Example prompt:

   ```markdown
   Is there work underway to update the engineering DRIs in the AI section?
   ```

1. Find DRIs to review your merge request, or include in a discussion.
   Example prompt:

   ```markdown
   Can you help me find the DRI for the AI section, specifically the GitLab Duo Slack integration.
   ```

![GitLab UI side panel with Agentic Chat, and Developer Flow handover](/images/handbook/about/editing-handbook/handbook-edit-ui-gitlab-duo-agentic-chat-dev-flow.png)

#### Move a page with Agentic Chat

In the handbook project on GitLab, open [GitLab Duo Agentic Chat](https://docs.gitlab.com/user/gitlab_duo_chat/agentic_chat/)
with the relevant project context and expected outcome, for example:

```text
Create a plan to move <page URL> to <new location>, preserving its content.
Include updates to affected links, navigation, and CODEOWNERS, and a redirect
from the old URL.
```

#### Plan larger changes with Developer Flow

For larger edits, you can also ask Agentic Chat to [delegate the task to the Developer Flow](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/developer/#use-the-flow-in-agentic-chat),
which runs a session in the background and notifies you on finish. Developer Flow typically
creates a plan first, and will request human input if there are blockers.

Alternatively, create an issue in the appropriate handbook project and use one of the
[Developer Flow interaction methods](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/developer/#use-the-flow):

1. Select **Implement work item**, or
1. Assign the configured Duo Developer service account `@duo-developer-gitlab-com`, or
1. Mention the account in a comment, `@duo-developer-gitlab-com Please help me implement this change`

Follow progress in **AI > Sessions**, then review the resulting MR and validation results.

> **Tip**: you can also ask Duo Developer to address review feedback in your MR, or help fix linter errors.

![Mention Duo Developer in a comment to address changes](/images/handbook/about/editing-handbook/handbook-edit-duo-developer-at-mention.png)

### Use the Web IDE to edit the handbook

The [GitLab Web IDE](https://docs.gitlab.com/user/project/web_ide/) lets you edit several files
and commit them together in your browser. You do not need to clone the repository or install Hugo locally.

Follow these steps:

1. On the handbook page, select **Edit this page**. Alternatively, open its source
   in GitLab and select **Edit > Open in Web IDE**.
1. Edit the page.
   - Use the **File Explorer** panel to open related files.
   - You can also upload images into
   `static/images/handbook/`, following the [image guidance](https://handbook.gitlab.com/docs/markdown-guide/#images).

   ![Web IDE - editor and file explorer](/images/handbook/about/editing-handbook/handbook-edit-web-ide-editor-overview.png)

   ![Web IDE - upload files](/images/handbook/about/editing-handbook/handbook-edit-web-ide-upload-file.png)

1. Open **Source Control** and inspect each changed file.
1. Enter a short commit message and choose **Create a new branch** when committing.
   - Leave the Git branch question empty and press **Enter** to use the default branch name.

   ![Web IDE - create a git branch and commit](/images/handbook/about/editing-handbook/handbook-edit-web-ide-source-control-git-commit-branch.png)

1. Select **Create MR** in the notification, then [review and submit](#review-and-submit-your-change).
   - This action will open the GitLab merge request creation form in a new tab.

   ![Web IDE - create merge request](/images/handbook/about/editing-handbook/handbook-edit-web-ide-create-merge-request.png)

#### Edit an existing MR

1. Open the MR and select **Code > Open in Web IDE**.
1. Edit the files and review the diff in **Source Control**.
1. Commit to the existing MR branch.

#### Quick tips

- **Find a file:** **Go to File** (`Command+P` on macOS).
- **Find a command:** Command Palette (`Shift+Command+P` on macOS).
- **Recover the Create MR notification:** select the bell icon in the status bar.

Search only covers open files. Use a local checkout or an agent for repository-wide
searches. To preview Hugo shortcodes and the handbook theme, use a
[review app](#preview-changes-on-gitlab-pages).
See the [Web IDE documentation](https://docs.gitlab.com/user/project/web_ide/) for more options.

### Edit with connected apps

Start from an app you already use, such as Glean, Claude, or Slack. Give it the page
and intended change to turn your question or discussion into a handbook update.

#### Handbook edits with Glean

Install the [Glean desktop app](/handbook/eta/ai/tools/glean/#access). GitLab internal context is already pre-configured,
so you can start working immediately on handbook updates.

Example prompt:

```markdown
I want to add the #gitlab-gtm Slack channel to Product and Technical Marketing. Can you help me make the handbook changes please?

https://handbook.gitlab.com/handbook/marketing/
```

![Glean desktop - Handbook edit with GitLab MCP](/images/handbook/about/editing-handbook/handbook-edit-glean-desktop-chat-mcp.png)

#### Handbook edits with Claude Desktop

Install the [Claude for Desktop app](/handbook/tools-and-tips/ai/claude/#applications-and-cli)
and ensure that the [GitLab MCP Server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)
is configured and connected in **Settings > Connectors > GitLab**.

Make smaller changes in **Chat** conversations to create remote MRs,
using the GitLab MCP connector.

Example prompt:

```markdown
I want to add the #gitlab-gtm Slack channel to Product and Technical Marketing. Can you help me make the handbook changes please?

https://handbook.gitlab.com/handbook/marketing/
```

![Claude for Desktop - make a change from Chat](/images/handbook/about/editing-handbook/handbook-edit-claude-desktop-chat.png)

For larger changes, switch to **Cowork** and add the folder with the
cloned Git repository to allow Claude to make changes and validate the results.

![Claude for Desktop - Cowork with handbook folder](/images/handbook/about/editing-handbook/handbook-edit-claude-desktop-cowork-local-folder.png)

You can also use the **Code** tab to work with Claude Code in the
handbook files in your local environment.

#### Turn Slack discussions into handbook updates

Verify that the [GitLab Duo Slack integration](https://docs.gitlab.com/user/project/integrations/gitlab_slack_application/#gitlab-duo)
is enabled in your channel, mention `@GitLab` with the repository URL, page URL,
agreed change, and requested output. For example:

```text
@GitLab In <repository URL>, update <page URL> with the agreed decision:
<public-safe summary and source>. Create a draft MR with a focused change.
Explain what was validated. Do not merge or assign reviewers.
```

GitLab Duo can use the thread and recent channel history as context. Only use a thread
whose information is appropriate for the integration and target repository.
Follow the [GitLab Duo in Slack setup](https://docs.gitlab.com/user/project/integrations/gitlab_slack_application/#gitlab-duo)
for account linking and availability. Review the returned MR before requesting approval.

Example prompt:

```markdown
@GitLab I want to add the `#gitlab-gtm` Slack channel to Product and Technical Marketing. Can you help me make the handbook changes please?

https://handbook.gitlab.com/handbook/marketing/
```

![Slack thread with GitLab working on handbook updates](/images/handbook/about/editing-handbook/handbook-edit-slack-gitlab-duo-app.png)

### Edit locally with an editor or agent {#editing-the-handbook-locally}

Use [VS Code or another editor](/handbook/tools-and-tips/editors-and-ides/) to work on a copy
of the handbook on your laptop. Edit files yourself or ask an agent to help, then
use GitLab to review and check the changes.

#### Edit locally and let GitLab check your changes

You can edit handbook files on your laptop without installing Hugo, Docker, or the
preview tools. [Clone the repository](https://handbook.gitlab.com/docs/development/#clone-the-handbook-git-repository),
open it in your editor, and make your changes on a new branch. Commit and push your
changes, then create a merge request. GitLab runs the checks and reports any problems there.

![Terminal with git clone](/images/handbook/about/editing-handbook/handbook-edit-local-clone.png)

Open the cloned `handbook` folder in your editor. Find the page in the file explorer
and start editing its Markdown.

If you use VS Code, install the
[GitLab for VS Code extension](https://docs.gitlab.com/editor_extensions/visual_studio_code/setup/)
and follow its setup guide to sign in to GitLab.com and connect your project.
This lets you work with issues, merge requests, and pipeline status from your editor.

![VS Code with handbook project](/images/handbook/about/editing-handbook/handbook-edit-local-vscode.png)

You can use a [review app](#preview-changes-on-gitlab-pages) to see how the page looks before merging.

> **Tip:** An agent can help you clone the repository, create a branch, and push your changes.
Ask it to show you the changes before pushing.

#### Use an agent in your editor or terminal

Open the checkout in [VS Code with GitLab Duo Agentic Chat](https://docs.gitlab.com/user/gitlab_duo_chat/agentic_chat/), [GitLab Duo CLI](https://docs.gitlab.com/user/gitlab_duo_cli/), Claude Code, or another approved AI tool. Follow the tool's setup instructions before starting.

Start by opening the cloned repository in your agent tool. It can edit local files
without GitLab MCP access.

To read issues, inspect pipelines, or create MRs, connect GitLab through
[MCP](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) or
[glab](https://docs.gitlab.com/cli/). GitLab Duo tools use their existing GitLab connection.

Local build tools are optional. Let [GitLab CI check your changes](#fix-linter-errors)
after pushing, or set up [Docker](#local-live-preview) or
[local tools](https://handbook.gitlab.com/docs/development/running-locally/) when you want checks and previews
on your laptop.

Ask the agent to help you with your task. For example:

```text
Update <page URL> to reflect <change>, using <source link or agreed wording>.
Flag anything unclear, validate the edit, and show me the diff and checks run.
Keep the changes local for now.
```

The repository's `AGENTS.md` provides the handbook style guides and validation instructions (for example, [AGENTS.md in the handbook](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/main/AGENTS.md?ref_type=heads)), so you can focus your prompt on the task.

Example with GitLab Duo CLI:

```markdown
I want to add the #gitlab-gtm Slack channel to Product and Technical Marketing. Can you help me make the handbook changes please?

https://handbook.gitlab.com/handbook/marketing/
```

![GitLab Duo CLI edit prompt](/images/handbook/about/editing-handbook/handbook-edit-local-gitlab-duo-cli-01.png)

![GitLab Duo CLI - requested changes, validated locally](/images/handbook/about/editing-handbook/handbook-edit-local-gitlab-duo-cli-02.png)

#### Local live preview

For a live preview, install and start a [Docker-compatible runtime with Compose](https://handbook.gitlab.com/docs/development/running-in-docker/), then open a new terminal and run this command from the handbook repository root level:

```shell
docker compose up
```

![Docker Compose installing dependencies and starting the Hugo preview](/images/handbook/about/editing-handbook/handbook-edit-docker-compose-up.png)

Wait for Hugo to finish building, then open <http://localhost:1313/> in your browser.
Edit files in your editor. Saving changes triggers a rebuild automatically, and the website reloads
in your browser. The container prepares the pinned tools, npm dependencies, and required data.
The first start takes longer. Press **Control+C** to stop.

See [Docker setup](https://handbook.gitlab.com/docs/development/running-in-docker/)
for full instructions, Git worktrees, and manual Docker alternatives. With Rancher
Desktop, use its [Moby (dockerd) engine](https://docs.rancherdesktop.io/ui/preferences/container-engine/general/) for the Docker CLI workflow.

If you prefer tools installed on your laptop, follow the
[native setup and preview commands](https://handbook.gitlab.com/docs/development/running-locally/#running-hugo).
These include installing npm dependencies and running `./scripts/sync-data.sh` before Hugo.
With Make installed, `make view` handles that preparation automatically. Agents can
use the repository's Makefile targets or direct commands with either setup.

An agent can also help start the preview:

```text
Preview <page URL> using this repository's existing local setup.
Reuse an existing preview if available, or help me start one.
Give me the exact local page URL.
```

For follow-up checks and page moves, use the [common handbook tasks](#common-handbook-tasks)
below. Keep changes local until you have reviewed the diff and are ready to submit.

## Review and submit your change

Before merging, check that your change says what you intended and works for readers.
These steps apply whichever editing method you used.

1. Review the complete diff, including links, images, and any agent-generated wording.
1. Explain why the change is needed in the MR description. Keep confidential context out of public MRs.
1. Check the CI/CD pipeline and check the preview of the changes to page structure or rendering.
1. Request the appropriate [review and approval](../handbook-usage.md#when-to-get-approval).
1. Address feedback on the same MR. Merge or enable auto-merge only when the required checks and approvals are satisfied.

### Preview changes on GitLab Pages

A review app lets you check the rendered handbook page in your browser before merging.
You do not need a local preview setup.

1. Wait for the MR build and checks to succeed.
1. Click the **Deploy** button in the CI/CD widget.

   ![GitLab MR with review app deploy action](/images/handbook/about/editing-handbook/handbook-edit-preview-changes-review-app-gitlab-pages.png)

   This starts the `pages` CI/CD job and deploys a GitLab Pages preview for this MR.
1. Wait for the deployment, then select **View app** in the MR. Availability can lag behind job completion.

   ![View app button after the review app deployment succeeds](/images/handbook/about/editing-handbook/handbook-edit-preview-changes-review-app-gitlab-pages-view-app.png)

1. Navigate to the changed page within the review app. Keep the review URL prefix
   when following or constructing a link.

   ![Handbook review app with the MR number in the browser URL](/images/handbook/about/editing-handbook/handbook-edit-preview-changes-review-app-gitlab-pages-handbook-mr.png)

The `deploy-review-app-always` label requests a deployment after each MR update.
See [Pages deployment](https://handbook.gitlab.com/docs/development/#gitlab-pages-deployment) for technical details.

## Common handbook tasks

Use these examples when updating text, moving pages, adding images, or changing page
maintainers. Choose the steps or agent prompt that fits your task.

### Add yourself to the team page

Use the [team page guide](edit-team-page.md) to edit your profile, or
[ask an agent to review and update your YAML entry](edit-team-page.md#ask-an-agent-for-help).

### Markdown formatting

Use the [Markdown guide](https://handbook.gitlab.com/docs/markdown-guide/) for formatting, images, and shortcodes.

Example prompt for agents:

```text
Format <page URL or file> using the handbook Markdown guide.
Preserve the wording, fix formatting issues, and validate the changes.
Show me the diff before committing.
```

### Find and replace content

Use this for a renamed team, an updated resource link, or a term that appears on
several pages. Review the matches before replacing them: a historical reference
may need to keep its original wording.

#### Using Visual Studio Code

1. Open the handbook checkout and create a branch using **Source Control**.
1. Open **Search** and enter the existing text or URL.
1. Limit **Files to include** to the relevant folder, such as `content/handbook/marketing/`.
1. Expand **Replace**, enter the new text, and review each proposed replacement.
1. Replace individual matches, or use **Replace All** when every match is appropriate.
1. Inspect every changed file in **Source Control**, then run the relevant checks.
1. Commit the intended files and [prepare an MR](#review-and-submit-your-change).

#### Ask an agent

```text
Replace <old text or URL> with <new text or URL> within <scope>.
Review the matches first and flag historical references or ambiguous wording.
Preserve unrelated work. Show the diff and run the relevant checks.
Do not commit or push yet.
```

### Move or rename a page

Changing a filename or directory can change the published URL. Renaming a page's
`title` is different: it changes its displayed heading, and may leave the URL intact.
Explain which outcome you want before moving files.

#### Use an editor

1. Locate the page and create a branch. For a page bundle, identify its images and
   other resources before moving the directory.
1. In VS Code's Explorer, use **Rename** or move the file or folder to its new location.
1. Search the repository for the old file path and published URL. Update incoming
   links, navigation, and affected CODEOWNERS entries. Check both handbooks when
   you have access, and flag external references for their owners. Check relative links from
   the moved page too.
1. Add the appropriate [redirect](https://handbook.gitlab.com/docs/development/#redirects) so the old published
   URL still reaches the page. Do not assume your editor creates redirects.
1. Run the relevant checks, preview the new page, and verify the redirect in an
   environment that serves it. A local content preview alone may not exercise
   GitLab Pages redirects.
1. Review the complete diff and create an MR.

#### Use Agentic Chat or an issue

In GitLab Duo Agentic Chat, select the relevant project context and ask it to use
Developer Flow. For example:

```text
Use Developer Flow to move <page URL> to <new location> in <repository URL>.
Preserve the content and page resources. Update incoming links, relative links,
navigation, and affected CODEOWNERS paths. Add a redirect from the old URL
and check links to headings. Do not merge or assign reviewers.
```

Alternatively, create an issue containing the same task and select **Implement work item**
when available. See [Developer Flow in Agentic Chat](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/developer/#use-the-flow-in-agentic-chat)
for availability and [the issue workflow](#ask-an-agent-in-gitlab).
You can also give the task to Duo CLI, Claude Code, or VS Code with Duo Agent Platform
in your local checkout. Review the resulting changes regardless of the entry point.

### Add images

Use a screenshot or illustration when it helps readers follow the instructions.
Add it to the repository so it can be displayed on the page.

1. Add the image under `static/images/handbook/` in a directory matching your page.
   Use the Web IDE's **Upload** action or copy the file in your local editor.

   ![Web IDE - upload files](/images/handbook/about/editing-handbook/handbook-edit-web-ide-upload-file.png)

1. Insert a Markdown image with descriptive alternative text. The published path
   starts with `/images/`, without `static/`.
1. Follow the [image guidance](https://handbook.gitlab.com/docs/markdown-guide/#images) for file size and formatting.
1. Preview the page and check that the image fits on desktop and narrow screens.

```text
Add <image file> to <page URL> with suitable alternative text.
Follow the handbook image guidelines and show me the rendered page.
Keep the changes local for review.
```

Apps like Claude Cowork or Glean can reference uploaded images in the prompt,
and upload them to the merge request.

### Naming pages and folder structure {#naming-pages-and-folder-structure}

The site uses the concept of page bundles, sections, and leaf pages.  A section can have multiple leaf pages, which requires a `_index.md` for the section.  A page bundle is a single page with a group of images, which can be an `index.md`.

In general, Handbook URLs should describe their content and be as clean and easy to remember as possible.

Directories (folders) and pages should use lowercase `a-z`, hyphen `-`, and underscore `_`.
While Git and Hugo allow any UTF-8 character to be used in the file path, using other characters (such as a space) can cause issues with the pipeline, and thus, disallowed.

Section:

```plain
section-dir/
|- _index.md
|- leaf-page1.md
|- leaf-page2.md
```

Page bundle:

```plain
page-name/
|- index.md
|- image1.png
|- image2.png
```

Section with a page bundle:

```plain
section-dir/
|- _index.md
|- leaf-page1.md
|- leaf-page2/
|  |- index.md
|  |- image.pmg
|- leaf-page3.md
```

#### Moving, deleting, or renaming a page

Follow the [page-move checklist](#move-or-rename-a-page). For deletion, choose a
useful replacement destination and update incoming links before adding a redirect.

### Editing page maintainers

On the right side of the page, there is a list "Maintainers".

The list is generated from the `CODEOWNERS` file in the relevant repository, such as in [the handbook repository](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/main/.gitlab/CODEOWNERS):

- Only specific users are listed. Members of a group are not listed.
- The list is generated based on the most specific path:

  - If users are specified for a directory and then for a specific page in that directory,
    the list only includes the users for the specific page.
  - If groups or subgroups are listed for a specific page without any specific users,
    the list of maintainers is empty.

Changes to the `.gitlab/CODEOWNERS` file require approval.
Review the bot comment for instructions on how to get the appropriate approval.

### Editing content from shortcodes

Some pages display content from includes, shortcodes, or imported data. Edit the
canonical source rather than generated output. Ask an agent to trace the displayed
text to its source, or ask in [#handbook](https://gitlab.enterprise.slack.com/archives/C81PT2ALD).
See the [shortcode guide](https://handbook.gitlab.com/docs/shortcodes/) for how these work.

### Team member merge requests being labeled as Community contributions

If you recently created a merge request that was labeled as a Community contribution, you can fix this mislabeling issue going forward by updating the GitLab username in your personal entry in the team member directory to match the GitLab account you use for work.

Use the [team page editing instructions](edit-team-page.md) to find your team page entry file, and update the `gitlab` attribute (typically found on line 10) to be an **exact match** for the GitLab.com username you use for work.

## Working with merge requests

If a check fails or something looks wrong in your MR, use the steps below to fix it.
You can make the correction yourself or ask an agent for help.

### Fix linter errors

Linter errors usually occur when a specific style guide rule is not followed.
For example, a linter error might occur if a line ends with additional whitespaces,
or if a URL anchor is not in the correct format. The handbook projects use different
tools to ensure the style guide, which are run automatically in merge requests. They
create a summary report as a new comment.

Example with different error types. Each table entry links to the specific file and line
where inline suggestions can be created and applied. Note: This works best for smaller changes.

![MR comment with linter errors table](/images/handbook/about/editing-handbook/merge-request-linter-errors.png)

There are multiple ways to fix linter errors with agent help:

1. Copy the comment URL and add it to an agentic chat prompt.
   - Verified working in GitLab UI - Agentic Chat, Apps (Glean, Claude, Slack), local in editors and CLI tools (GitLab Duo CLI, Claude Code, etc.)

   ```markdown
   Please help me fix the linter errors in https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/21126#note_3839248743
   ```

1. Ask the Developer Flow for help by mentioning it in the comment thread:

   ```markdown
   @duo-developer-gitlab-com Please help me fix the linter errors in this MR
   ```

   ![Mention Duo Developer in a comment to fix linter errors](/images/handbook/about/editing-handbook/handbook-edit-duo-developer-at-mention.png)

Manual editing options:

1. In the GitLab UI:
   - Open line URL in the error reports, or
   - Open the MR `changes` tab and inspect the [code quality findings](https://docs.gitlab.com/ci/testing/code_quality/#merge-request-changes-view)
   - Add a [comment with suggested changes](https://docs.gitlab.com/user/project/merge_requests/reviews/suggestions/).
1. In the single file editor, the Web IDE, or locally in an editor.

### Fix images that do not load

If an image is missing in the preview, give an agent the page URL and the MR URL
or local checkout. Ask it to check the image file and its reference. Common causes
include a misspelled filename, different capitalization, a duplicated extension such
as `.png.png`, or an image that was not added to the MR.

```text
Fix the image that does not load on <page URL> in <MR URL or local checkout>.
Check that the image file exists and the page references the correct path.
Verify that it loads in a local preview or review app. Show the diff and report
anything you could not verify.
```

For files under `static/images/`, the published URL starts with `/images/`.
For page bundles, check the image path relative to the page. If the image file is
missing, provide the intended image rather than asking the agent to invent a replacement.
See the [image guidance](https://handbook.gitlab.com/docs/markdown-guide/#images).

### Fix merge conflicts

If a merge request signals a merge conflict, this means that the changes in this MR conflict with changes in the default main branch.
To fix this, you need to update your branch to include the changes in the main branch.

If your branch is only behind `main` and has no merge conflicts, use the
[`/rebase` quick action](https://docs.gitlab.com/user/project/merge_requests/conflicts/#rebase-in-the-gitlab-ui)
in a new MR comment. GitLab's UI rebase requires a branch without conflicts.

For actual merge conflicts:

1. Use the new [Resolve Conflicts with GitLab Duo](https://docs.gitlab.com/user/project/merge_requests/conflicts/#resolve-conflicts-with-gitlab-duo).
   - Click the button in the merge request.
   - This action triggers a specialized Developer Flow which will attempt to implement a fix and commit to the merge request. If it cannot achieve the goals, it will comment a summary.
1. Resolve the conflicts in the UI or locally in an editor.

## Contributing

### Improve agent instructions and skills

If an agent keeps missing a step, help improve the shared guidance. See the
[Docsy maintenance guide](https://handbook.gitlab.com/docs/development/maintenance/)
for contributing `AGENTS.md`, code review instructions, and skills, including testing
and synchronizing changes across the handbook projects.

<!-- Preserve links from existing pipeline comments and escalation references. -->
<span id="failing-pipelines"></span>
<span id="link-and-anchor-errors"></span>

## Troubleshooting

See [the troubleshooting guide](troubleshooting.md), including
[failing pipelines](troubleshooting.md#failing-pipelines) and
[link and anchor errors](troubleshooting.md#link-and-anchor-errors).
