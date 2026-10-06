---
title: Onboarding an ASE Account
description: Workflow to onboard an account that is new to the ASE service
---

## Overview

As soon as a customer account signs a new contract that includes the Assigned
Support Engineer (ASE) service, the Support Team begins the customer onboarding
process. Through this process we intend to create and deliver a smooth and
professional experience to the customer as we begin our partnership with them.
This involves coordinating with the customer and the account team, as well as
informing the rest of Support about the account's new status.

## Preparation

Ensure that you have completed the appropriate platform training, depending on the environment(s) the customer will utilize. For example:

1. [GitLab Dedicated](https://gitlab.com/gitlab-com/support/support-training/-/blob/main/.gitlab/issue_templates/GitLab%20Dedicated.md?ref_type=heads)
1. [GitLab.com / SaaS](https://gitlab.com/gitlab-com/support/support-training/-/blob/main/.gitlab/issue_templates/GitLab-com%20SaaS%20Basics.md?ref_type=heads)
1. [Self-Managed](https://gitlab.com/gitlab-com/support/support-training/-/blob/main/.gitlab/issue_templates/Self-Managed%20Basics.md?ref_type=heads)

## Customer Communication

[Introduce yourself as the customer's ASE](introductory-meeting.html).

Agree with the customer on either a weekly or every-other-week schedule for a
cadence call. The goals of the call should include completing a review of the
work done since the previous call, and agreeing on what work you'll do for them
before the next call and with what relative priorities.

## Systems Configuration

### Add the account to the Assigned Support Engineers project README file

In the [Assigned Support Engineers](https://gitlab.com/gitlab-com/support/assigned-support-engineers)
project, the
[README](https://gitlab.com/gitlab-com/support/assigned-support-engineers/-/blob/main/README.md)
file contains the table that is the Single Source of Truth that lists all
active ASE accounts and the ASEs for them. The table contains other standard
information for each account as well:

1. Links (Salesforce, Zendesk Org Note)
1. Special Notes
1. Zendesk Org Name
1. Zendesk Account ID
1. Zendesk User (ASE) ID

The Zendesk-titled columns help everyone to find the correct account in Zendesk.

Since ASEs don't have access to Salesforce, coordinate with your manager
to find the necessary details. Then, submit an MR to add the full entry for
the new account in the table in the README.

#### Manager Instructions

Add the ASE to SFDC Account Team as "Assigned Support Engineer". Go to the Account record in Salesforce -> **Account Team** list:

1. Click Add (or Add Default Team / Edit Team as appropriate).
1. Add ASE's Salesforce user created as part of the [ASE Onboarding issue](https://gitlab.com/gitlab-com/support/support-training/-/work_items/new?description_template=ASE-Onboarding).
1. Set the Role to: `Assigned Support Engineer`.
1. Save the changes.

Repeat this for each of your ASE accounts. This ensures SFDC can identify you as the ASE for that account when new Cases are created.

### Org Note mentioning the ASE and how to treat the ticket

A customer having an ASE can be a confusing prospect for others in and out of
GitLab Support. How would they know that a specific customer has an ASE?

This is why an organization note in the ticket will prove useful. It will
guide all interested parties (Support Engineers, Customer Success Managers, 
Account Executives, etc.) to the correct workflows for what to do.

A good organization note will answer the following questions:

- Who is the Assigned Support Engineer (ASE) for this customer?
- Which region is the ASE located in?

This information will come from the contract and from the discussion with the
customer in the [introductory meeting](./introductory-meeting.html).

Create a merge request for the org note
[in the Organizations project](https://gitlab.com/gitlab-com/support/zendesk-global/organizations)
and assign it to your manager for review.

Here's an example:

```yaml
notes: |
  This organization has an Assigned Support Engineer (ASE).

  Global Support should continue to work this account’s tickets using the org note and ASE documentation for context.

  The ASE will engage based on customer prioritization, current needs, and ticket trends. The ASE is not expected to take every case for the account.

  If the ASE is unavailable, please continue working the ticket and engage the ASE during business hours for clarification or escalation as needed.

  Emergency tickets outside the ASE’s business hours should continue to be handled by the global support on-call rotation. The ASE will follow up during their normal business hours.
```

### Set up notification alerts

#### Using Slack webhook to receive Slack notification on new case email

Prerequisites:

- Your manager have [added you as an “Assigned Support Engineer” to SFDC Account Team](#manager-instructions).
- You are receiving new case emails from `operationssupport@gitlab.com` for the account.

You can set up automated Slack notifications for new Salesforce case emails using Google Apps Script. This helps you stay informed about new customer tickets without constantly checking your Gmail inbox.

Follow the detailed instructions in the [Gmail Slack Warpgate project](https://gitlab.com/gitlab-com/cs-tools/gitlab-cs-tools/gmail-slack-warpgate).

#### Using Incident.io to be notified of updates on Dedicated incidents

NOTE: This is applicable only for customers on GitLab Dedicated.

You can subscribe to [Incident.io](https://app.incident.io) personal alerts to be notified of updates on Dedicated incidents for your customers. You can set this up through the following steps:

1. Navigate to your user profile and click on **Incident subscriptions** tab.
1. Under **Subscription destinations**, select your preferred mode of notification, such as through Slack and email.
1. Under **Auto-subscribe**, click on **Add auto-subscribe rule** and on **Add condition** to specify conditions for the notifications, such as **Severity** is at least Severity 2 (High).
   1. Configure the rule specific to your customer by specifying the **internal_reference** or the **tenant_id** for your customer. You can retrieve this information from the [Dedicated Switchboard](https://console.gitlab-dedicated.com/tenants) under **Internal reference** and **Identifier**, respectively.
   1. Click on **Create** to save the rule.

For Slack notifications, you will be notified through a direct message from the Slack user "incident". For email notifications, you will be notified by the email user "incident.io".

The following image shows the configuration.

![Incident.io personal alert configuration](/images/support/incident-io-personal-notifications.png)

### Request access to the `@dedicated-ase` Slack group

NOTE: This is applicable only for ASEs managing customers on GitLab Dedicated.

To request access:

1. File an access request using the [Individual_Bulk_Access_Request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Individual_Bulk_Access_Request) ([example access request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/work_items/45187)).
1. Request manager approval for the access request.
