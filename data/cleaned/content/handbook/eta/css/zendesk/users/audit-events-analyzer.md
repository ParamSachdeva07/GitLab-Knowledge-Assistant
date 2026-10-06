---
title: 'Audit Events Analyzer'
description: 'Documentation on Audit Events Analyzer'
---

This guide covers Audit Events Analyzer, a custom setup we have created for use in Zendesk.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Projects:
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/audit-events-analyzer)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/audit-events-analyzer)

{{% /alert %}}

## Understanding Audit Events Analyzer

### What is Audit Events Analyzer

Audit Events Analyzer is a combination of Zendesk webhooks and CI/CD scripts that analyze specific types of audit events and notify the Customer Support Systems team accordingly.

### How does Audit Events Analyzer work

Utilizing [Zendesk User events webhooks](https://developer.zendesk.com/api-reference/webhooks/event-types/user-events/), CI/CD pipelines are triggered with a payload (sent by the webhook) in the corresponding project (based on the Zendesk instance). The current monitored user events are:

- Support user role changed

When the CI/CD pipeline is created, the script `bin/analyze` runs, which does the following:

- Checks if the event was a role downgrade (new role is `end-user` OR an `admin` was made into an `agent`)
  - If it was, it exits with a status code of 0
- Checks if the event was a light agent upgrade (previous role was `end-user`, new role is `agent`, and the email ends with `@gitlab.com`)
  - If it was, it exits with a status code of 0
- If the upgraded user's previous role was `end-user`, a post to Slack is made using the `@channel` tag
- If the upgraded user's previous role was `agent`, a post to Slack is made using the `@here` tag

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.
- All sections in this section require `Developer` level access to the project.

{{% /alert %}}

### Modifying the Audit Events Analyzer project

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To modify the Audit Events Analyzer project, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. Being this is an `Ad-hoc` deployment type, the changes will be live immediately.

### Modifying the webhooks

For information on modifying webhooks, see our documentation on [Webhooks](/handbook/eta/css/zendesk/webhooks/).

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
