---
title: 'Slack'
description: 'Documentation on Slack'
---

This guide covers what we manage that uses Slack currently.

## Notify Oncall

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project: [Notify Oncall](https://gitlab.com/gitlab-support-readiness/slack/notify-oncall)
- Works for Zendesk US Government only

{{% /alert %}}

### What is Notify Oncall

Notify Oncall is a setup we have used to alert all available US Government Support team agents when an emergency ticket is created that does not have a direct DRI being paged. It posts a message in the [#spt_us-government  Slack channel](https://gitlab.enterprise.slack.com/archives/C03RTN3JEJ2).

### How does Notify Oncall work

When a US Government emergency ticket is created, Zendesk sends a signal to Pagerduty. Via a [Pagerduty webhook](https://developer.pagerduty.com/docs/db0fa8c8984fc-overview) on the [Customer Support - US Federal service](https://gitlab.pagerduty.com/service-directory/P8K2XHK), a GitLab CI/CD pipeline is triggered on the [Notify Oncall](https://gitlab.com/gitlab-support-readiness/slack/notify-oncall) project.

Notify Oncall then checks the list of assignees on the payload sent from Pagerduty to determine if it should proceed. It if finds a human listed as an assignee, it exits with a 0 status code (as there is no need to notify about the emergency that already paged a human).

Notify Oncall then determines a list of agents available using the following criteria:

- Is a Support team agent on the Zendesk US Government instance
- Is not on PTO (as per the `Support - Time Off` calendar)
- Is within working hours (as per the Support Team YAML files)

It then translates this list of agents to their Slack user IDs (as per the Support Team YAML files). With this information, Notify Oncall then makes a post in the [#spt_us-government  Slack channel](https://gitlab.enterprise.slack.com/archives/C03RTN3JEJ2) to notify about the emergency ticket.

### Changing Notify Oncall

{{% alert title="Note" color="primary" %}}

- This requires at least `Developer` access to the [Notify Oncall](https://gitlab.com/gitlab-support-readiness/slack/notify-oncall) project.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To make changes to Notify Oncall, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR (which will have them applied on the next triggered run).

## Very Breached Ticket slackbot

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project: [Very Breached Ticket Slackbot](https://gitlab.com/gitlab-support-readiness/slack/very-breached-ticket-slackbot)
- Works for Zendesk Global tickets only

{{% /alert %}}

### What is the VBT slackbot

The Very Breached Ticket (VBT) Slackbot is tooling we use to report on specific tickets that have breached beyond 48 hours. It posts notifications about the tickets it finds in the [#spt_leaders-daily Slack channel](https://gitlab.enterprise.slack.com/archives/C03LL7Z2291).

### How does VBT slackbot work

This works by generating a list of tickets using the Zendesk API's [preview views](https://developer.zendesk.com/api-reference/ticketing/business-rules/views/#preview-views) endpoint. The conditions used for the preview are:

- Must meet ALL of the following conditions
  - Time since SLA breach is greater than 48 (business) hours
  - The ticket's `Ticket form` is not `Billing`
  - The ticket's `Ticket form` is not `Support Ops`
  - The ticket's status is less than solved (i.e. `new`, `open`, `on-hold`)
- Must meet ANY of the following conditions
  - The ticket's `Ticket Stage` is `Emergencies`
  - The ticket's `Ticket Stage` is `FRT`

VBT slackbot then makes a post in the [#spt_leaders-daily Slack channel](https://gitlab.enterprise.slack.com/archives/C03LL7Z2291) to notify about the tickets found, with each ticket listed containing:

- A link to the ticket
- The `Ticket form` of the ticket
- The timestamp it breached at
- How many hours ago it breached

### When does VBT slackbot run

The VBT slackbot runs via GitLab scheduled pipelines at 3 set times:

- At 1400 UTC Monday through Friday (`0 14 * * 1-5`)
- At 2130 UTC Sunday through Thursday (`30 21 * * 0-4`)
- At 0700 UTC Monday through Friday (`0 7 * * 1-5`)

### Changing VBT slackbot

{{% alert title="Note" color="primary" %}}

- This requires at least `Developer` access to the [Very Breached Ticket Slackbot](https://gitlab.com/gitlab-support-readiness/slack/very-breached-ticket-slackbot) project.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To make changes to the VBT slackbot, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR (which will have them applied on the next scheduled run).

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
