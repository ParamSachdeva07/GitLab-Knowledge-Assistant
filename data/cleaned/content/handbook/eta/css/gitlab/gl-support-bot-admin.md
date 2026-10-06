---
title: 'gl-support-bot-admin'
description: 'Documentation on gl-support-bot-admin'
---

## Understanding gl-support-bot

### What is gl-support-bot

For our scripts and automations that require admin access, we use the [gl-support-bot-admin](https://gitlab.com/gl-support-bot-admin) user to act as a team wide service account. This is to ensure our automations are not tied to a specific human user and run consistently.

## Requesting access

{{% alert title="Warning" color="warning" %}}

This bot account has access to a lot of data. Unless being used in the standard methods we utilize, you should consider using an alternative source (such as service accounts).

{{% /alert %}}

To request the token, file an [acccess request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=API_Token_Request).

For the issue, the `Service Name` is `gl-support-bot-admin`.

Please assign the issue to Jason Colyer and Dylan Tragjasi at this time.
