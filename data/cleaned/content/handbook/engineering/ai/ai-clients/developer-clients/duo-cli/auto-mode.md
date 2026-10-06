---
title: Duo CLI auto mode (beta)
description: "How GitLab team members can turn on and test the beta auto mode in Duo CLI, and the risks of using it."
---

## Overview

Auto mode is a beta Duo CLI mode that runs tools without asking for approval first. It is available
to GitLab team members for dogfooding and testing only. It is not yet promoted to customers.

Progress is tracked in the [auto mode rollout epic](https://gitlab.com/groups/gitlab-org/-/work_items/23697).

{{% alert title="Warning" color="danger" %}}
Auto mode lets the agent act on your machine and on GitLab without asking you first. Where your
settings allow it, the agent can:

- Run any shell command, including commands that delete files or change your system.
- Run `git` commands, including commits and pushes.
- Write to GitLab: create or update issues, merge requests, and other resources.
- Run MCP tools and start flows.

The agent can make mistakes, and content it reads (files, issues, merge requests, web pages) can
contain instructions that steer it (prompt injection). To limit the risk:

- Use auto mode only in repositories you trust and on disposable branches.
- Do not use it on machines or shells that have production or other sensitive credentials loaded.
- Stay in the session and review every change before you merge it.
- Switch back to `build` mode when you do not need auto mode.
{{% /alert %}}

## Prerequisites

- Duo CLI v9.22.0 or later. Use the latest version if you can.
- The `duo_auto_mode` feature flag must be enabled for your top-level group. If it is not, ask on the
  [auto mode feedback issue](https://gitlab.com/gitlab-org/gitlab/-/work_items/630593).

## Turn on auto mode

The feature flag alone is not enough. The **Auto mode** setting defaults to off, so you must also
turn it on for a group or project.

### Turn on auto mode for a group

Use this to turn on auto mode for every subgroup and project in a group.

1. In the top bar, select **Search or go to** and find your group.
1. Select **Settings** > **GitLab Duo**.
1. Select **Change configuration**.
1. From the **Auto mode** dropdown list, select one of:
   - **On by default**: on for all subgroups and projects. Subgroups and projects can still turn it off.
   - **Off by default**: off, but subgroups and projects can turn it on.
   - **Always off**: off, and locked so subgroups and projects cannot turn it on.
1. Save your changes.

### Turn on auto mode for a project

Use this to turn on auto mode for a single project.

1. In the top bar, select **Search or go to** and find your project.
1. Select **Settings** > **General**.
1. Expand **GitLab Duo**.
1. Turn on **Auto mode**.
1. Save your changes.

If a parent group is set to **Always off**, the project setting is locked and you cannot change it.

## Use auto mode

To use auto mode:

1. Restart Duo CLI in the project so it picks up the new setting.
1. Press <kbd>Tab</kbd> to cycle through the modes: `build`, `plan`, and `auto`. Auto mode shows in
   yellow with a `&` prefix.
1. Send a prompt. Auto mode takes effect from that prompt onward.

Auto mode does not persist. Each new, resumed, or `/new` session starts in `build` mode.

To stop using auto mode, press <kbd>Tab</kbd> to switch to another mode. The change applies to your
next prompt.

## Troubleshooting

If `auto` does not appear when you press <kbd>Tab</kbd>:

1. Confirm the `duo_auto_mode` feature flag is enabled for your top-level group.
1. Confirm the **Auto mode** setting is on for the project, or on by default from its group.
1. Confirm a parent group is not set to **Always off**.
1. Restart Duo CLI.

Some tools can still ask for approval in auto mode. This is expected when an administrator's
policy requires approval for them.

## Feedback

Share what worked, what was confusing, and any safety concerns on the
[auto mode feedback issue](https://gitlab.com/gitlab-org/gitlab/-/work_items/630593).
