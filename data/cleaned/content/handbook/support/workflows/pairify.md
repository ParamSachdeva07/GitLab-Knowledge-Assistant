---
title: Pairify
description: "This document provides information on what Pairify is and how to use it to record pairing sessions."
category: References
---

## Overview

This document provides information on what Pairify is and how to use it to record [pairing sessions](pairing-sessions.md)

## What is Pairify?

[Pairify](https://gitlab.com/gitlab-com/support/toolbox/pairify) is a Slack bot application that will scan monitored Slack channels on a schedule for any conversations reacted with ![Pairify emoji](/images/support/workflows/assets/pairify.png "Pairify emoji") (`:pairify:`).

It will then extract all Zendesk URLs, GitLab URLs (epics, issues, merge requests, handbook and docs), Slack participants/mentions and automatically create a pairing issue with the extracted URLs, participants (converted to GitLab.com usernames) and closes out the issue. The raw Slack thread is also captured in the issue, however attachments remain in Slack.

![Pairify demo](/images/support/workflows/assets/pairify_demo.gif)

## Using Pairify

**NOTE**: For Pairify to correctly map your Slack user to your GitLab.com user, you must configure your Slack profile's **GitLab.com profile** field. See [edit your profile](https://slack.com/intl/en-gb/help/articles/204092246-Edit-your-profile) for more details.

To incorporate Pairify into your pairing session workflow:

1. Create a thread in one of the [supported channels](#channels-monitored-by-pairify) and pair with your colleagues!

1. Ensure that the thread conversation contains the following information:

   a. All Zendesk ticket URLs worked on

   b. All participants in the pairing session need to comment on the thread, or mentioned `@slack_username` in the thread

1. Optional. [Specify the pairing session type](#specifying-the-pairing-session-type).

1. React to the thread with the ![Pairify emoji](/images/support/workflows/assets/pairify.png "Pairify emoji") (`:pairify:`) emoji **once the pairing is completed** to mark a conversation for Pairify to process.

You then need to wait for the next scheduled execution of Pairify, as explained in [how Pairify works](#how-pairify-works).

## How Pairify works

Pairify executes every 30 minutes via a [scheduled pipeline](https://gitlab.com/gitlab-com/support/toolbox/pairify#production). When the pipeline begins, Pairify will search [all monitored channels](#channels-monitored-by-pairify)
for any conversation reacted with the ![Pairify emoji](/images/support/workflows/assets/pairify.png "Pairify emoji") (`:pairify:`) emoji that was created within the last 12 hours.

Pairify will then:

1. Extract any Zendesk URLs, participants and mentions within the conversation
1. Extract the raw Slack conversation (excluding attachments)
1. Convert all Slack users to their GitLab.com counterparts
1. Create a GitLab issue in the [Support Pairing](https://gitlab.com/gitlab-com/support/support-pairing) project with the details extracted. The `pairify` label will be automatically applied to the issue, along with any other labels determined during processing.
1. Creates a message on the conversation thread indicating that the conversation has been processed. The response will also include a link to the issue created
1. React to the conversation with an ![Issue created emoji](/images/support/workflows/assets/pairify_issue-created.png "Issue created emoji") (`:issue-created:`) emoji so the conversation is not processed again on subsequent executions.

## Specifying the pairing session type

Pairify can apply additional labels to pairing issues to indicate the pairing session type if you react with additional emojis.

The reactions are mutually exclusive - Pairify will only process the first reaction added to the conversation if multiple reactions are found.

See [specifying the pairing issue type](https://gitlab.com/gitlab-com/support/toolbox/pairify#specifying-the-pairing-session-type) for more information.

## Automatic labels

Pairify automatically applies certain labels based on the content and context of pairing sessions. For a complete list of automatic labels, see [automatic labels](https://gitlab.com/gitlab-com/support/toolbox/pairify#automatic-labels) for more information.

## Reminders

Pairify can also send automatic reminder messages for idle threads. See [reminders](https://gitlab.com/gitlab-com/support/toolbox/pairify#reminders) for more information.

## Channels monitored by Pairify

Refer to the [`.settings.production.yml`](https://gitlab.com/gitlab-com/support/toolbox/pairify/-/blob/main/config/.settings.production.yml) file for a list of channels being monitored by Pairify.

## Troubleshooting

- Refer to the [troubleshooting](https://gitlab.com/gitlab-com/support/toolbox/pairify#troubleshooting) section in the Pairify project.
- Review the [issue tracker](https://gitlab.com/gitlab-com/support/toolbox/pairify/-/issues) as you might be encountering a known issue.
