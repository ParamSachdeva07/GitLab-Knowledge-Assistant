---
title: 'Tickets'
description: 'Documentation on Zendesk tickets'
---

This guide covers ticket management in Zendesk, including ticket statuses, system settings, and common Support Systems workflows.

## Understanding tickets

### Creating tickets

Traditionally, we want end-users creating their own tickets. In situations where that may be less than ideal, there are set options available to be used.

#### Via the Zendesk Super App

{{% alert title="Note" color="primary" %}}

- This option is only available to those on the Customer Support Systems or Support teams

{{% /alert %}}

This should be used when you need to make a new ticket from an existing user. For this, you would use the corresponding app:

- For Zendesk Global: [Zendesk Super App](/handbook/eta/css/zendesk/apps/global#zendesk-super-app)
- For Zendesk US Government: [Zendesk Super App](/handbook/eta/css/zendesk/apps/us-government#zendesk-super-app)

#### For outbound communication

{{% alert title="Note" color="primary" %}}

- This option is only available to those:
  - who are on the Customer Support Systems team
  - who are on the Support team AND have the agent role of `Support Staff - CMOC` (Zendesk Global only)

{{% /alert %}}

See the Support team's [Sending Notices documentation](/handbook/support/workflows/sending_notices) for more information.

### Viewing tickets

For information on viewing tickets, please see:

- [Views](/handbook/eta/css/zendesk/views/)
- [Searching](/handbook/eta/css/zendesk/searching/)

### Statuses

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408832151834-Updating-and-solving-tickets#topic_i3y_np1_vt) the various status are defined as:

- New
  - This indicates that no action has been taken on the ticket. Once a New ticket’s status has been changed, it can never be set back to New.
- Open
  - This indicates that the ticket is waiting for action by the agent.
- Pending
  - This indicates that the agent is waiting for more information from the requester. When the requester responds and a new comment is added, the ticket status is automatically reset to Open.
- On-hold
  - This indicates that the agent is waiting for information or action from someone other than the requester. It is similar to the Pending status in that you as an agent can’t proceed with resolving the ticket until you receive more information from someone else. However, the On-hold is an internal status that the ticket requester never sees. While a ticket is set to On-hold, the requester sees the status as Open.
- Solved
  - This indicates that the agent has submitted a solution or the end-user has marked it as such. A solved ticket can still be edited or re-opened.
- Closed
  - This indicates that the ticket is in a state where it can no longer receive updates. Replying to a closed ticket opens a follow-up ticket, which contains all previous tags and links to the previous ticket.

At GitLab, we define them a bit differently:

- New
  - This is a new ticket. This means it has not yet been worked by GitLab.
- Open
  - This means the ticket is awaiting our reply.
- Pending
  - This means we are waiting on the end-user to reply. We should only use this specifically when the user will reply back to the ticket (or it will auto-solve). If you need to keep a ticket in a “pending” like state for lengthy periods of time, use On-hold.
- On-hold
  - This means the end-user is waiting on us, but we are waiting on something that is blocking us from replying. We should only be using this in situations where we are waiting on something such as a different department, time to pass (namesquatting requests as an example), or some other criteria that fits along the same concept.
- Solved
  - This means the ticket has been resolved, but the end-user might come back to us.
- Closed
  - We use them exactly as Zendesk defines them.

### Current system ticket settings

These settings are documented here for reference and should rarely be changed.

<details>
<summary>For Zendesk Global</summary>

- Comments
  - [x] Set composer to public channel by default
  - [x] Agent comments via email are public by default
  - [ ] Allow first comment on tickets to be private
  - [ ] Default to draft mode
  - [ ] Allow email comments from CCed end users to be public (not recommended)
  - [x] Turn on spelling and grammar check
  - [x] Allow emoji text replacement
  - [x] Allow agents to change the text color
  - [x] Allow agents to translate conversations
    - Translate with AWS Translate
      - [x] AI translations for all channels
      - [x] Show AI translation disclosure
  - Select how transcript will be added to the ticket: `As a public reply`
  - Render URIs are hyperlinks: `["[]"]`
  - [x] Allow agents to send audio messages
- Attachments
  - [x] Customers can attach files
  - [x] Enable secure downloads
  - [x] All file types
- Tags
  - [x] Enable tags on tickets
  - [ ] Enable automatic ticket tagging
- CCs and followers on tickets
  - [x] Allow followers
    - Customize your follower email: `{{ticket.title}}`
    - Create your email text

      ```plaintext
      You are a follower on this request ({{ticket.link}}). {{ticket.follower_reply_type_message}}
      ```

  - [x] Allow CCs
    - CCs and followers blocklist: `noreply@google.com`
    - [x] Allow light agents to be added to tickets
    - [x] Allow end users to add CCs to requests
  - [x] Automatically make a CCed agent a follower
  - [ ] Allow agents to change requester
- Assignment
  - [x] Auto-assign tickets upon solve
  - [x] Allow re-assignment back to the general group
- Follow-Ups
  - [ ] Copy original assignee and group to follow-up ticket
- Suspended Ticket Notifications
  - `Never` How often you want to receive email about new suspended tickets.
  - Email list:
- Ticket IDs
  - Set the ticket ID counter
    - This value is going to change based on ticket volume. Do not touch it
- Modify closed ticket
  - [ ] Turn on
- Email Archiving
  - Archive email address:
- Transcript visibility
  - How conversation transcript is incrementally appended to the ticket: `As public reply`
- Continuous conversations
  - [ ] Switch messaging conversations to email
- Translations
  - [x] Agents can translate conversations
- Solved Ticket Reassignment
  - [ ]  Turn on solved ticket reassignment
    - [ ] Show solved ticket reassignment
    - Set an account level default for solved ticket reassignment option for newly created groups: `To an admin or longest active team member`
    - [ ] Force all the groups to assume the account level default now
- Agent collaboration for messaging
  - [x]  Multiple agents can collaborate in messaging conversations

</details>
<details>
<summary>For Zendesk US Government</summary>

- Comments
  - [x] Set composer to public channel by default
  - [x] Agent comments via email are public by default
  - [ ] Default to draft mode
  - [ ] Allow email comments from CCed end users to be public (not recommended)
  - [x] Turn on spelling and grammar check
  - [x] Allow emoji text replacement
  - [x] Allow agents to change the text color
  - [x] Allow agents to translate conversations
    - Translate with AWS Translate
      - [ ] AI translations for all channels
      - [~] Show AI translation disclosure
  - Select how transcript will be added to the ticket: `As a public reply`
  - Render URIs are hyperlinks: `["[]"]`
  - [x] Allow agents to send audio messages
- Attachments
  - [x] Customers can attach files
  - [x] Enable secure downloads
- Tags
  - [x] Enable tags on tickets
    - [ ] Enable automatic ticket tagging
- CCs and followers on tickets
  - [x] Allow followers
    - Customize your follower email: `{{ticket.title}}`
    - Create your email text

      ```plaintext
      You are a follower on this request ({{ticket.link}}). {{ticket.follower_reply_type_message}}
      ```

  - [ ] Allow CCs
  - [~] Automatically make a CCed agent a follower
  - [ ] Allow agents to change requester
- Requester
  - [ ] Agents can change requester
- Assignment
  - [x] Auto-assign tickets upon solve
  - [x] Allow re-assignment back to the general group
- Follow-Ups
  - [ ] Copy original assignee and group to follow-up ticket
- Suspended Ticket Notifications
  - `Never` How often you want to receive email about new suspended tickets.
  - Email list:
- Ticket IDs
  - Set the ticket ID counter
    - This value is going to change based on ticket volume. Do not touch it
- Modify closed ticket
  - [ ] Turn on
- Email Archiving
  - Archive email address:
- Transcript visibility
  - How conversation transcript is incrementally appended to the ticket: `As public reply`
- Continuous conversations
  - [ ] Switch messaging conversations to email
- Translations
  - [x] Agents can translate conversations
- Solved Ticket Reassignment
  - [ ]  Turn on solved ticket reassignment
    - [ ] Show solved ticket reassignment
    - Set an account level default for solved ticket reassignment option for newly created groups: `To an admin or longest active team member`
    - [ ] Force all the groups to assume the account level default now
- Agent collaboration for messaging
  - [x]  Multiple agents can collaborate in messaging conversations

</details>

### Current ticket sharing settings

These settings are documented here for reference and should rarely be changed.

<details>
<summary>For Zendesk Global</summary>

- Sending agreements: 0
- Receiving agreements
  - `Pivotal @ Zendesk` `Public comments allowed. Sync status and share tags` `Accepted`
- Opt out of sharing
  - [ ] Decline all sharing agreement invites

</details>
<details>
<summary>For Zendesk US Government</summary>

- Sending agreements: 0
- Receiving agreements: 0
- Opt out of sharing
  - [ ] Decline all sharing agreement invites

</details>

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Modifying closed tickets

While Zendesk has the ability to update some values within closed tickets, it is not an action that we will perform. After discussions with several teams utilizing data from Zendesk and a review of the customer facing impact modifying closed tickets would have, the decision is based off the following reasons:

- Updating closed tickets would have a negative impact on customers (with no viable workaround)
- Updating closed tickets would severely impact reports/dashboards in Zendesk Explore, requiring full re-configuration
- Updating closed tickets would severely impact reports in our data warehouse, requiring full re-configuration
- Updating closed tickets would require a full re-index of the data within our data warehouse (consuming massive amounts of resources and requiring 5+ days)
- We have viable workarounds that can be done within our data warehouse using custom views, custom tables, and AI (negating any perceived benefits to performing updates on closed tickets)

### Modifying system ticket settings

{{% alert title="Danger" color="danger" %}}

- Exercise extreme caution in doing this, as it can greatly impact the usability of the support portal.
- This should only ever be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.)
- Always ensure [Current system ticket settings](#current-system-ticket-settings) is updated on this page if you change the system ticket settings

{{% /alert %}}

To modify the system ticket settings:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Tickets > Settings`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/tickets/ticket-settings)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/tickets/ticket-settings)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/tickets/ticket-settings)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/tickets/ticket-settings)
1. Make modifications to the settings you wish to change
1. Click `Save` at the bottom-right of the page

### Modifying ticket sharing settings

{{% alert title="Danger" color="danger" %}}

- Exercise extreme caution in doing this, as it can greatly impact the usability of the support portal.
- This should only ever be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.)
- Always ensure [Current ticket sharing settings](#current-ticket-sharing-settings) is updated on this page if you change the ticket sharing settings

{{% /alert %}}

To modify the ticket sharing settings:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Tickets > Sharing`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/tickets/ticket-sharing)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/tickets/ticket-sharing)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/tickets/ticket-sharing)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/tickets/ticket-sharing)
1. Make modifications to the settings you wish to change
1. Click `Save tab` at the bottom-right of the page

## Customer Support Systems Workflows

### Working tickets

{{% alert title="Note" color="primary" %}}

- This pertains solely to the Customer Support Systems team and how they work tickets. It does not reflect how any other team might work them.

{{% /alert %}}

#### Managing support contacts

For Zendesk Global tickets about managing contacts, please see our [Organization association documentation](/handbook/eta/css/zendesk/organizations/association).

For Zendesk US Government tickets about managing contacts, all support contact association is done via a sync with the Salesforce account. As such, we cannot assist here. You will need to instruct the requester to contact their account manager via a new email. Make sure to provide the email of the account manager.

#### Shared organization requests

Please see our [Shared Organization setup documentation](/handbook/eta/css/zendesk/organizations/shared-orgs).

#### Portal issues

These are reports of issues within the support portal. While each issue can present unique challenges, the common troubleshooting guide for the users can be found at:

- [Zendesk Global](https://support.gitlab.com/hc/en-us/articles/11626501035292-Support-Portal-User-Guide#support-portal-troubleshooting)
- [Zendesk US Government](https://federal-support.gitlab.com/hc/en-us/articles/22616053222292-Support-Portal-User-Guide#support-portal-troubleshooting)

At the point you get the ticket, the user may or may not have done all of that. If they have not, point them to trying all that out first.

If they have, you will need to analyze the details of what is sent to determine next steps.

#### Adding a secondary email requests

Sometimes a customer will raise issue stating they want to add a secondary email to their support portal account. Secondary emails are used to tie submitted tickets to a specific account, although only the primary email address will be used as the submitter (and thus receive notifications).

- For GitLab.com Users:
  - The GitLab.com account associated to the requester’s email address should have listed the secondary email as verified. You can check this via the User Lookup app. To add secondary email to GitLab.com account, they can follow [this documentation](https://docs.gitlab.com/user/profile/#add-emails-to-your-user-profile)
- For Self Managed and GitLab Dedicated Users:
  - The ticket needs to be submitted from the email address they wish to have added to their existing profile
  - The customer will need to provide proof of support entitlement again via this secondary email address
  - The customer will need to CC the primary email address of the support portal account and have that email reply on the ticket confirming the request to add the secondary email address to their support portal account.
- For Partners:
  - Use the same steps you would for Self Managed and GitLab Dedicated Users

#### Incorrect form tickets

When a ticket is using the incorrect form, agents will use the `General::Forms::Incorrect form used` macro. This will change the form to `Support Ops`, tag the ticket, and leave an internal note. From there, we are expected to review the ticket and determine the next steps.

Your ultimate goal here is to move it to the correct form. The path to doing so depends on a great many factors, but in general:

- If being moved to a "paid only" form and the user is unassociated:
  - Follow the process of Organization association to get the user associated
    - If they are not able to be associated, the ticket cannot be moved
  - Set the `Assignee` value on the ticket to `Support Ops` (a group)
    - This will unassign the ticket. You should always do this unless the internal note added when it was sent to us indicated otherwise
  - Change the `Form` value on the ticket to the new form
  - Fill out all ticket metadata possible for the new form
    - If present on the ticket, set the `Ticket Stage` field to `FRT`
  - Remove the following tags:
    - `base_weight_set`
  - Make sure to submit the ticket as the _same state_ it was sent to us in
- If being moved to a "paid only" form and the user is associated:
  - Set the `Assignee` value on the ticket to `Support Ops` (a group)
    - This will unassign the ticket. You should always do this unless the internal note added when it was sent to us indicated otherwise
  - Change the `Form` value on the ticket to the new form
  - Fill out all ticket metadata possible for the new form
    - If present on the ticket, set the `Ticket Stage` field to `FRT`
  - Make sure to submit the ticket as the _same state_ it was sent to us in
- If being moved to a form available to anyone:
  - Set the `Assignee` value on the ticket to `Support Ops` (a group)
    - This will unassign the ticket. You should always do this unless the internal note added when it was sent to us indicated otherwise
  - Change the `Form` value on the ticket to the new form
  - Fill out all ticket metadata possible for the new form
    - If present on the ticket, set the `Ticket Stage` field to `FRT`
  - Make sure to submit the ticket as the _same state_ it was sent to us in

##### Special form notes

- If moving the ticket to the `2FA Removal` form
  - If the request for removal is for a user different than the requester, the requester **must** provide the email address of the target user. If they have not, leave an internal note stating the requester must provide that piece of information. After doing so, move the ticket to the `SaaS Accounts` form instead.
- If moving the ticket to the `L&R` form
  - When moving tickets to the L&R form, we need to ensure it is routed to the right subteam at the start. To do this, ensure the `BPO Ticket` checkbox (at the bottom of the ticket metadata) is checked. Failing to do so can potentially result in problems in ticket routing.
- If moving the ticket to the `Billing` form
  - You must ensure the `Billing/AR Team` attribute on the ticket is populated. If it is unclear which value to use, set it to `Billing`

#### Handling malicious users

{{% alert title="Danger" color="danger" %}}

- Exercise extreme caution in dealing with malicious users. Do not hesitate to request help from our security team when in doubt. It is **always** better to ask for help than cause a compromise.

{{% /alert %}}

When a ticket arises containing potential malicious actions (hacking, phishing, abuse, etc.), we need to always treat it seriously.

If, after a thorough investigation, it is determined to be malicious, [ban the user](/handbook/eta/css/zendesk/users/end-users#banning-an-end-user)

When in doubt, escalate the matter to your manager, a Customer Support Systems Fullstack Engineer, and/or the GitLab Security team.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
