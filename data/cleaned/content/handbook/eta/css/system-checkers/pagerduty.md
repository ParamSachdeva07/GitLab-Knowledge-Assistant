---
title: 'Pagerduty'
description: 'Documentation on the Pagerduty system checker'
---

<sup>Introduced via [gitlab-com/support/support-ops/support-ops-project#1891](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/1891)</sup>

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [gitlab-support-readiness/system-checkers/pagerduty](https://gitlab.com/gitlab-support-readiness/system-checkers/pagerduty)

{{% /alert %}}

## Understanding the Pagerduty system checker

### What is the Pagerduty system checker

The Pagerduty system checker is a setup using pipeline triggers (sent from Pagerduty) to report the status of Pagerduty. It posts to the [#feed_status-pagerduty Slack channel](https://gitlab.enterprise.slack.com/archives/C086Z7LAFB2).

### How does it work

When Pagerduty notifies the project (via a Pagerduty webhook), the `bin/process_webhook` script runs, which does the following:

- Converts the Pagerduty payload into a formatted Slack message
- Posts the message to the [#feed_status-pagerduty Slack channel](https://gitlab.enterprise.slack.com/archives/C086Z7LAFB2)

## Changing the Pagerduty system checker

{{% alert title="Note" color="primary" %}}

- This requires at least `Developer` access to the project.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To make changes to the Pagerduty system checker, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR (which will have them applied on the next triggered run).

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
