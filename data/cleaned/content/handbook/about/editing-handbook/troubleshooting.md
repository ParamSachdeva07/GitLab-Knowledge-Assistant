---
title: Troubleshooting handbook edits
description: Find and fix access, preview, and pipeline problems when editing the handbook
---

Start with the symptom below. For help, share the page or failed job URL in
[#handbook](https://gitlab.enterprise.slack.com/archives/C81PT2ALD) or
[#mr-buddies](https://gitlab.slack.com/archives/CLM8K5LF4).
Keep internal content in channels approved for that information.

| Problem | Where to start |
| --- | --- |
| Edit action returns 404 | [Access and sign-in](#404-errors-with-edit-action) |
| New page or image is missing | [Page names](#404-error-on-new-page) or [images](#images-not-loading-properly) |
| A pipeline failed | [Find the failing check](#failing-pipelines) |
| A link or heading is broken | [Link and anchor errors](#link-and-anchor-errors) |
| Local preview will not start | [Environment troubleshooting](https://handbook.gitlab.com/docs/development/troubleshooting/) |
| Unrelated pages changed after saving | [Formatter settings](#prettier-is-formatting-markdown-files) |

## 404 errors with edit action

When clicking on `Edit this page` in the upper right corner on a handbook page in your browser, you might get a `404` error in the GitLab Web IDE.

As a team member, this problem can be related to an expired SAML SSO session for your GitLab.com profile and Okta.
In order to mitigate and solve the problem, click on `View page source` to trigger the SAML authentication with Okta again.

Alternatively, navigate into our GitLab.com profile into [your To-Do list](https://gitlab.com/dashboard/todos), or try to open a confidential issue, to trigger the authentication.

It can also be browser related: Try clearing the cache, open an incognito window (on macOS: `cmd shift n`), or use a different browser to test.

## 404 error on new page

If a new page is created as part of a merge request, but the page is not showing up on the site,
check the file name.

The most common issue is using `index.md` instead of `_index.md` in a folder that has other pages.
The other pages will not display.

See [pages and folder structure](_index.md#naming-pages-and-folder-structure) for more information.

## Images not loading properly

If you added new images and they are not loading properly in your review app, please review the
[Images section of the markdown guide](https://handbook.gitlab.com/docs/markdown-guide/#images).

## Failing pipelines

You can give an agent the failed job URL or paste the relevant lint output. Ask it
to explain the cause, reproduce the check locally, and fix only the reported issue.
Local checks can cover different files from CI, especially after committing; ask
which files and baseline were tested. An infrastructure failure is not a lint error.

Use one of the following agents for help:

1. For focussed CI/CD help: [Fix CI/CD Pipeline Flow](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/fix_pipeline/), [CI Expert agent](https://docs.gitlab.com/user/duo_agent_platform/agents/foundational_agents/ci_expert_agent/)
1. For general help: [Developer Flow](https://docs.gitlab.com/user/duo_agent_platform/flows/foundational_flows/developer/) and [Agentic Chat](https://docs.gitlab.com/user/gitlab_duo_chat/agentic_chat/)
1. Local agents: [GitLab Duo CLI](https://docs.gitlab.com/user/gitlab_duo_cli/), [Claude Code](/handbook/tools-and-tips/ai/claude/), or any other approved AI tool, together with the [GitLab MCP server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/).

To see why your pipeline is failing, there are two main places to look:

1. The latest comment by the bot on your merge request. It should have a list of all linter errors. However, build errors do not generate a comment.
1. Individual failed jobs. On the MR > "Pipelines" tab > select any red circle > select a failed job. Error messages are near the bottom of the job log and start with `Error`.

In the job log, error messages typically provide you:

1. the error
1. the file where the error occurred
1. the line number
1. the character number (where on the line it is)

For example:

```text
Error: error building site: assemble: "/builds/gitlab-com/content-sites/handbook/content/handbook/security/security-assurance/field-security/trust_center_guide.md:1:2": closing tag for shortcode 'details' does not match start tag`

- File: `content/handbook/security/security-assurance/field-security/trust_center_guide.md`
- Line: 1
- Character: 2
```

To fix markdown errors, review the message. Alternatively, review the relevant section in the [markdown style guide](https://handbook.gitlab.com/docs/markdown-guide/).

For build or setup errors, see the [development troubleshooting guide](https://handbook.gitlab.com/docs/development/troubleshooting/).
If the cause is unclear, include the failed job URL when asking for help.

See the following sections for specific errors.

If the problem was on the `main` branch, you may need to [rebase](https://docs.gitlab.com/ee/user/project/quick_actions.html#issues-merge-requests-and-epics).

If you're unsure, you can [reach out for help](_index.md#need-help).

### Link and anchor errors

There is a linter (Hugolint) that validates links and anchors across the handbook. If your change introduces _new_ broken links, then the pipeline job will fail. Follow the instructions in the [previous failing pipelines section](#failing-pipelines) for how to find the list of errors.

There are two main reasons it will fail:

1. Content added in the MR includes a broken link.
1. Content changed in the MR breaks an existing link.

Here's an example of a failed `hugolint` job error message when viewed in the job log:

```plain
Newly broken (only in "linkcheck.json", 3 issues):
❌ [content/handbook/security/product-security/_index.md:43]: <major> Link destination "architecture/" does not exist
❌ [content/handbook/security/product-security/security-architecture/_index.md:269]: <major> Link destination "/handbook/business-technology/tech-stack/#panther" does not exist
❌ [content/handbook/security/product-security/security-architecture/zero-trust.md:45]: <major> Link destination "/handbook/security/corporate/systems/#laptop-or-desktop-system-configuration" does not exist
```

1. The error starts with the file where the broken link is present, followed by the line number.
   (For example, file path - `content/handbook/security/product-security/_index.md`, line number: 43.)
1. Next, the error indicates which link is broken. (For example, `architecture/` is the broken link destination.)
1. For broken or non-existent anchor links (for example, `#panther`):
   1. Did the MR change a heading that is being linked to? If so, you'll need to update the linked anchor to match the new heading.
   1. If you're linking to a heading, does it exists? Check the file in the repository instead of on the website. The links are checked pre-build, so generated content (from shortcodes and includes) don't "exist" for the link checker.
      - If the page you're linking to has a large amount of generated content (such as performance indicator pages), you can [add an exclusion to `hugolint`](https://gitlab.com/gitlab-com/content-sites/handbook-tools/hugolint/#configuration) in the relevant configuration file.

### Community contributions

Pipelines for community contributions to the handbook from private forks will fail.
Contributors should use a public fork, or preferably [the community fork](https://gitlab.com/gitlab-community/meta#gitlab-community-forks).

## Fixing default branch errors

If several unrelated MRs fail with the same error, compare their logs with the
latest default-branch pipeline. Ask in [#handbook Slack](https://gitlab.enterprise.slack.com/archives/C81PT2ALD)
with the job URLs before changing unrelated content. A shared failure may come from
configuration, imported data, infrastructure, or a dependency; the log determines
where to investigate. See the [maintenance guide](https://handbook.gitlab.com/docs/development/maintenance/).

### Example: Fixing broken main on tech writing shortcode

This historical incident used older Hugo templates and repository paths. It shows
how to follow an error into its source data, rather than commands to copy today.

Consider this [example error](https://gitlab.com/gitlab-com/content-sites/handbook/-/jobs/5968799321#L123):

```plain
Error: error building site: failed to render shortcode: "/builds/gitlab-com/content-sites/handbook/content/handbook/marketing/product-and-technical-marketing/technical-writing/_index.md:126:1": failed to render shortcode "tech-writing": failed to process shortcode: "/builds/gitlab-com/content-sites/handbook/layouts/shortcodes/tech-writing.html:16:28": execute of template failed: template: shortcodes/tech-writing.html:16:28: executing "shortcodes/tech-writing.html" at <ref page (printf "/handbook/product/categories#%s-section" $section)>: error calling ref: parse "/handbook/product/categories#%!s(<nil>)-section": invalid URL escape "%!s"
```

Following the error trace, notice that the last error with a full path and line number is:
`failed to process shortcode: "/builds/gitlab-com/content-sites/handbook/layouts/shortcodes/tech-writing.html:16:28"`.

Looking [at the `tech-writing` shortcode](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/114d8f9bf00342360be14dce8cf6e55e1d8a6edd/layouts/shortcodes/tech-writing.html#L16),
the issue is an unexpected value in `printf "/handbook/product/categories#%s-section" $section`,
which matches the last part of the error message.

From there, [line 11 of the `tech-writing` shortcode](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/114d8f9bf00342360be14dce8cf6e55e1d8a6edd/layouts/shortcodes/tech-writing.html#L11)
tells us that the data is from `site.Data.public.stages.stages "section"`.

If you have a local build of the site, you can find all the data files in the `data/public` folder.
The relevant file (usually a `yml` file) should tell you at the top where to find the original.

If you do not have a local build, you can still likely find it in the [www-gitlab-com data folder](https://gitlab.com/gitlab-com/www-gitlab-com/-/tree/master/data).

Based on the code, you can figure out the filename. `site.Data.public.stages.stages` means it's
in `data/public` and the file is `stages.yml`.

The last parts `.stages "section"` means it's inside of `stages:` and it's pulling data from
each `section:` line.

You can check the most recent changes to the file, and/or compare it to when `main` started failing.

In this case, [an empty `section:` line](https://gitlab.com/gitlab-com/www-gitlab-com/-/commit/17a5406b9a8fd33756cd5e0c4a2343ea2b4ab7a7)
was the issue.

The quick and easy fix is to add text to the empty `section:` line, merge it, and run a new pipeline
in the public handbook project.

In this case, [the handbook code was made more robust](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/2820/diffs).

## Prettier is formatting markdown files

If you have `prettier` set up in VS Code and it is formatting the `.md` files when they are not supposed to, check if you have Prettier set to be your default formatter with `"editor.defaultFormatter": "esbenp.prettier-vscode"` in your user settings.

Additionally, consider using the [Glob Pattern](https://code.visualstudio.com/api/references/vscode-api#GlobPattern) in the extension settings to specify which files to prettify automatically.
