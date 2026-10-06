---
title: 'US Government apps'
description: 'Documentation on Zendesk US Government apps'
---

This guide covers the Zendesk apps currently used in the US Government Zendesk instance.

## Advanced SAST App

<sup>*Introduced via [support-team-meta#6652](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/6652)*</sup>

The Advanced SAST App is a ticket app that enables a quick working of User requests for source code of LGPL-licensed components in GitLab Advanced SAST.

{{% alert title="Technical Details" color="primary" %}}

- Location: Ticket sidebar
- Restricted by Group:
  - Support
  - Support Managers
  - Support Operations
- This application was developed in-house and can be found [Advanced SAST App project](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/apps/advanced-sast-app).

{{% /alert %}}

## Advanced Search

Advanced Search is an app that provides a simple visual interface for constructing complex search queries against tickets, users, and organizations (orgs). It also enables you to export the search results in a CSV format.

{{% alert title="Technical Details" color="primary" %}}

- Location: Navbar
- This application was developed by [Zendesk](https://www.zendesk.com/marketplace/partners/zendesk/) and is available in the [Zendesk Marketplace](https://www.zendesk.com/marketplace/apps/support/198393/advanced-search/).

{{% /alert %}}

## Architecture Diagrams

<sup>*Introduced via [support-ops-project#801](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/801)*</sup>

This app uses the Organization field `AM Project ID` to check for an existing Account Management project. If it finds it, it will then link to that project’s Architecture Diagram.

{{% alert title="Technical Details" color="primary" %}}

- Location: Ticket sidebar
- This application was developed in-house and can be found [Architecture Diagrams project](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/apps/gitlab-architecture).

{{% /alert %}}

## GitLab Reminders App

<sup>*Introduced via [support-team-meta#3036](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/3036)*</sup>

The Reminders App appears in the navbar and allows the agent a more specialized view of tickets they are involved in. It currently shows:

- Tickets assigned to you with a pending/overdue task that are not in a Closed state
- Recent tickets you have viewed
- Tickets assigned to you that are not in a Closed state
- Tickets you are CC’d on that are not in a Closed state

It also allows you to quickly manage your tasks by seeing the notes you have left for said task, when it is due, and a button to quickly mark the task as done (remove the notes and due date).

{{% alert title="Technical Details" color="primary" %}}

- Location: Navbar
- This application was developed in-house and can be found [GitLab Reminders App project](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/apps/reminders-app).

{{% /alert %}}

## Salesforce Account Info

Shows basic information about a Salesforce account when provided the account's ID value.

{{% alert title="Technical Details" color="primary" %}}

- Location: Navbar
- Restricted by Role:
  - Admins
  - Support Managers
- This application was developed in-house and can be found [SFDC Account Info project](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/apps/sfdc-account-info).

{{% /alert %}}

## Salesforce Contact Info

Shows basic information about Salesforce contacts when provided the email address.

{{% alert title="Technical Details" color="primary" %}}

- Location: Navbar
- Restricted by Role:
  - Admins
  - Support Managers
- This application was developed in-house and can be found [SFDC Contact Info project](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/apps/sfdc-contact-info).

{{% /alert %}}

## Show Related Tickets

This uses the ticket subject to search for other tickets with a similar subject. This helps to locate potentially related tickets you can check to see how they were solved.

{{% alert title="Technical Details" color="primary" %}}

- Location: Ticket sidebar
- This application was developed by [Zendesk](https://www.zendesk.com/marketplace/partners/zendesk/) and is available in the [Zendesk Marketplace](https://www.zendesk.com/marketplace/apps/support/5131/show-related-tickets/).

{{% /alert %}}

## STAR

<sup>*Introduced via [support-team-meta#4694](https://gitlab.com/gitlab-com/support/support-team-meta/-/work_items/4694)*</sup>

Support Ticket Attention Requests (STAR) are the mechanism by which GitLab Team Members can request additional attention be placed on tickets. This is the app agents use in Zendesk to start a STAR process.

{{% alert title="Technical Details" color="primary" %}}

- Location: Ticket sidebar
- This application was developed in-house and can be found [STAR project](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/apps/star).

{{% /alert %}}

## Zendesk Super App

<sup>*Introduced via [support-ops-project#801](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/801)*</sup>

A plugin controlled app that can do several things Zendesk related

- Create new ticket
  > Allows an agent to create a new ticket using the same user as the ticket they are currently on.
- Due date picker
  > This allows you to customize what the Due Date for a Task ticket is set for. By default, Zendesk only allows setting the date. This enables you to set the date, time, and timezone.
  >
  > You can also set the Due Date Note and disable (or enable) task notifications using this app.
- Escalated tickets
  > This searches for tickets under the organization that have been escalated within the last 6 months.
- Related tickets
  > This looks for tickets related to the current one based off the category (or subcategory) the ticket is currently using. It then displays up to 5 of them (sorted by the update_at value of the ticket, descending).
- Attachments
  > Displays attachments present on the ticket.
- Ticket Info
  > Shows various metric information about a ticket:
  >
  > - Agent Wait Time
  > - Customer wait time
  > - Last assignee update
  > - Last customer update
  > - Assigned at
  > - On-hold time
  > - Time to first reply
  > - SLA Policy
  > - First reply SLA
  > - Next reply SLA
  > - Schedule

{{% alert title="Technical Details" color="primary" %}}

- Location: Ticket sidebar
- Restricted by Group:
  - Support
  - Support Managers
  - Support Operations
- This application was developed in-house and can be found [Zendesk Super App project](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/apps/zendesk-super-app).

{{% /alert %}}
