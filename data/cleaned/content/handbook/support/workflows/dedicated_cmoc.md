---
title: How to Perform GitLab Dedicated CMOC Duties
category: On-call
description: "Describes the role and responsibilities for the GitLab Dedicated CMOC rotation in Support Engineering"
---

## Introduction

The GitLab Dedicated Communications Manager on Call (GDCMOC) is an async role with the purpose of keeping GitLab Dedicated customers up-to-date about their environments. It involves liaising with Dedicated infrastructure team members on Slack or GitLab issues, and then relaying the information to the customer.

The GDCMOC rotation currently uses the GitLab.com CMOC rotation to determine who is oncall. When you go oncall as a GitLab.com CMOC, you will also be the GDCMOC. The [Communications Lead](/handbook/engineering/infrastructure-platforms/incident-management/roles/communications-lead) is currently staffed by CMOC and GDCMOC, with plans to evolve this structure in the future.

## Guidelines for the Role

- There is no expectation on the GDCMOC to be performing troubleshooting responsibilities.
- GDCMOCs do not need to put all their focus to actively monitor the relevant threads or issues. As a guideline, check every 30 minutes on existing communication threads for updates that need to be shared with the customer.

## Modes of Communication

The GDCMOC role involves two types of customer communication, each serving a different purpose and using different tools. When paged, the GitLab Dedicated SRE can advise which method is needed based on whether you need to inform customers or gather information from them. There is no expectation on the GDCMOC to be performing troubleshooting responsibilities.

**Mode One: Switchboard Notifications**

- One-way broadcast communication for notifying customers of incident status or emergency maintenances planned, impacting one or more customer environments
- Requires creating a notification using pre-approved templates in [Switchboard](dedicated_switchboard.md)
- Notifications are sent to the **[Operational Email Addresses](https://docs.gitlab.com/administration/dedicated/tenant_overview/#contact-information)** list of the tenant and Switchboard Users with email notifications enabled
- This mode of communication replaces the previous manual process of creating individual support tickets for each tenant, to provide scalable and compliant customer communication during incidents. [See STM#6768](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/6768)
- Watch an [internal demo](https://www.youtube.com/watch?v=e2ZRD8csjow) of this feature using the GitLab Unfiltered YouTube account
- → Follow [Sending Notifications using Switchboard](#sending-notifications-using-switchboard)

**Mode Two: Contact Request using Zendesk**

- Used for two-way communication for information gathering, and when no appropriate Switchboard template exists
- Requires creating a Zendesk ticket
- → Follow [Initiating a Contact Request](#initiating-a-contact-request-on-zendesk)

## Engaging the GDCMOC

The GDCMOC can be paged using Slack or directly using PagerDuty.

- **Slack**: Using the `/pd trigger` command in Slack, select `Incident Management - GDCMOC` in the **Impacted Service** modal. Fill in the **Title** and click the **Add Details** button. Add a description with a link to the issue or Slack channel where you need the GDCMOC's attention, then click **Create**.
- **PagerDuty**: From the [Incident Management - GDCMOC](https://gitlab.pagerduty.com/service-directory/P8WVAI0) page, click **New Incident**. Fill in the **Title**, add a desscription with a link to the issue or Slack channel where you need the GDCMOC's attention, and click **Create Incident**.

The **Description** field is optional, however it is the only way to inform the on-call support engineer about what is required or where they are needed, so please ensure it is filled in.

There is additional information about engaging the GDCMOC in the [on-call runbook](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/blob/main/runbooks/on-call.md#paging-the-gdcmoc) for the GitLab Dedicated team.

## Incident Management for GDCMOC

### Acknowledge the PagerDuty Page

Mark the page as [acknowledged](cmoc_workflows.md#pagerduty-status-definitions). This can be done through the mobile app, web interface or PagerDuty App in the `#support_gitlab-dedicated` Slack channel.

Dedicated SREs will reach out when customer communication is needed. The description in the PagerDuty alert should contain details about an issue, or a Slack thread you need to follow. Follow any communication threads, and let the Dedicated Incident team know you are available to assist. If you're unsure, check [the GitLab Dedicated incidents issue tracker](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/incident-management/-/issues/?label_name%5B%5D=Incident%3A%3AActive) or ask in the `#g_dedicated-team` Slack channel.

### Understand What Action to Take

Understand from the Dedicated SRE what type of communication is required:

- [Create an Incident Status Notification](#creating-an-incident-status-notification-using-switchboard),
- [Create an Emergency Maintenance Notification](#creating-an-emergency-maintenance-notification-on-switchboard) or
- [Initiate a Contact Request](#initiating-a-contact-request-on-zendesk)

### Sending Notifications Using Switchboard

#### Creating an Incident Status Notification Using Switchboard

1. [Log in to Switchboard](https://console.gitlab-dedicated.com/v2/login/).
1. Navigate directly to [**Customer notifications**](https://console.gitlab-dedicated.com/customer_notifications) page. This is found in the left sidebar of the homepage.
1. Select **+ New notification**.
1. Select the impacted tenants.
1. Select the relevant template for the incident:
   1. `Incident investigation start` — used at the beginning of the incident. This is the
      most generic template available.
   1. `Incident investigation update` — used to show progress and share new information.
   1. `Incident escalated response` — used to show the incident has maximum priority.
   1. `Incident mitigation in progress` — used to show active mitigation work.
   1. `Incident resolved` — sent to close out the incident when a fix or mitigation is
      deployed.
   If none of these templates exactly match your situation, select the most relevant one and edit the message accordingly. For a full list of available templates, see [Switchboard notification templates](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/switchboard/-/tree/main#notification-templates).
1. Optional. In the **Message** text box, edit the message before you send the notification:
   - For simple templates (`Incident investigation start`, `Incident resolved`), you can edit
     the entire message body.
   - For complex templates (`Incident investigation update`, `Incident escalated response`,
     `Incident mitigation in progress`), you can edit only the introductory paragraph.
   - Structured fields (**Investigation Focus Area**, **Affected Components**, **Customer
     Reported Impact**) remain form-driven and are configured in the steps below.
   - Editing is plain text only. Rich text and Markdown formatting are not supported.
   - The message cannot be left blank. The **Send** button is disabled if the message is empty.
   - Switching templates resets the message to the new template's default text.
1. Optional. For `Incident investigation update`, `Incident escalated response`, and
   `Incident mitigation in progress` templates:
   1. If known, select an **Investigation focus area** and **Affected components**.
   1. If the customer has reported impact that aligns with the incident, select
      **Include customer reported impact** and enter the details.
      Use this text box for customer-reported impact only.
      The goal is to confirm alignment by sharing the impact details the customer reported.
1. Preview the notification to confirm the message and any structured fields are correct.
1. Select **Send**.
1. After you send the notification, mark the PagerDuty alert as **Resolved** to notify the
   GDCMOC that communication has started.
1. Continue to [provide ongoing incident updates](#providing-ongoing-incident-updates-using-switchboard).

#### Providing Ongoing Incident Updates Using Switchboard

Update the customer on the incident status by [creating a new incident status notification](#creating-an-incident-status-notification-using-switchboard). If the last update hasn't changed, use the same information.

Ensure to provide an update **every 60 minutes**, or whenever the incident progresses to a new stage (Investigation Start → Investigation Update → Mitigation in Progress → Resolved), whichever comes first.

#### How to access customer contact details when Switchboard is unavailable

1. Daily at 6am UTC customer contact details are exported from Switchboard
2. The data is accessible on this [Switchboard customer contact details export issue](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/work_items/12182)

#### Handling Customer-created Zendesk Tickets during Incidents

After creating incident notifications on Switchboard, customers may open new Zendesk tickets seeking information about the incident. Inform them that the incident is being actively investigated and updates will be provided through Switchboard notifications as progress is made, or at least every 60 minutes.

**Continue regular notification updates using Switchboard:** Responding to Zendesk tickets does not replace updating Switchboard notifications. Continue to [provide ongoing incident updates using Switchboard](#providing-ongoing-incident-updates-using-switchboard).

#### Viewing Past Notifications on Switchboard

All customer notifications are logged in Switchboard. To view past notifications:

1. Click on your profile in the top left corner
1. Select `Customer notifications`
1. Click on the Title of the relevant notification to view the message and its recipients

#### Creating an Emergency Maintenance Notification on Switchboard

A security vulnerability fix might result in emergency maintenance for GitLab Dedicated environments.

NOTE:
"Emergency maintenance" refers exclusively to security-related maintenance. Maintenance that
happens outside of the weekly scheduled maintenance window are referred to as "out-of-band
maintenance", and this workflow does not apply.

Follow the steps in [Creating an Incident Status Notification Using Switchboard](#creating-an-incident-status-notification-using-switchboard), and select the templates for maintenance:

   1. `Emergency maintenance planned` is used for advance notice for emergency maintenance due to critical vulnerability
   1. `Emergency maintenance completed` is used to confirm that the emergency maintenance finished successfully

### Initiating a Contact Request on Zendesk

Use this workflow when you need to gather additional information from customers for incident investigation or when no pre-existing Switchboard template is available for the communication.

Locate the customer's contact email in Switchboard, then create a customer support ticket in Zendesk using the contact information.

#### Locating Customer Email Addresses in Switchboard

1. [Log in to Switchboard](dedicated_switchboard.md/#accessing-switchboard)
1. You should see the `Tenants` page when logged in. Find the relevant tenant and click `Manage`.
1. Expand the `Cloud Account Config` section, and look for the `Primary Region`. This should tell us which region the customer is based in. See the [AWS docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) if you're unsure of the AWS region code. Make a note of the region.
1. Search for the `Contact information` section, and expand it. You should see values for `Operational email addresses` and `Customer Success Manager CSM`.

#### Creating a Zendesk Ticket

1. Follow the instructions [here](/handbook/support/workflows/sending_notices/#manually-create-a-zendesk-ticket) to create a Zendesk ticket for the outbound request.
   1. For the **subject** of the ticket, use the following template: `GitLab Dedicated Notice: <description>`.
   1. Apply the macro `General::Outbound Contact Request`
   1. For the ticket **requestor**, use the first Operational Email Address listed.
   1. **CC** the other Operational Email Addresses and the Customer CSM and ASE (if any).
   1. Set the **Preferred Region for Support** to the region similar to where the tenants' `Primary Region` is located.
   1. Add a `dedicated_contacted_request` **tag** to the ticket.
   1. Set the "Support Resolution Codes" to **Incident**.
1. Assign the ticket to yourself.
1. [Avoid sending RED data](/handbook/support/workflows/sending_notices/#avoid-sending-red-data) in the ticket:
    1. Include information in a password protected, zipped file following the steps for [sending logs and personal data](/handbook/support/workflows/log_requests/#sending-logs-and-other-personal-data).
    1. For project/group links, use the [built in redirects](/handbook/support/workflows/sending_notices/#tips-for-avoiding-red-data-in-notices) to hide path names.
1. After sending the initial outreach message to the customer, mark the PagerDuty alert as **resolved**. The alert's purpose is specifically to engage the GDCMOC to start communication.

#### Closing the Zendesk Ticket

Before closing the Zendesk ticket, you should:

1. Send a final update to the customer confirming the completion.
1. Close the outreach ticket.
1. Add a brief internal note summarizing the communication timeline (optional).

Note: If the customer responds with follow-up questions after closure, create a new ticket to handle those inquiries separately from the original outreach communication.

## Keep the Customer Informed

- Work with the customer to set expectations about the frequency of updates, especially if you are the GDCMOC within the same region as the customer. They will likely expect more updates during their regional business hours.
  - If we proceed with lower frequency updates, the important thing is that we communicate our expected update frequency to them. For example, we can let the customer know that during their regional business hours, we will provide an update every 1-2 hours, and during their non-regional hours we will update them if there is anything substantial to share.
- Keep in mind the [information that we **should not** share with the customer](/handbook/support/workflows/dedicated/#sharing-internal-logs-data--graphs)
- If you'd like a second pair of eyes to review messages before sending them out to customers,
  refer to the table below to find an appropriate DRI.
  - Approval of message content is required for security-related communications.
  - Approval is optional for all other communication.

| Communication type                       | Who reviews content?   | Who approves content? |
|------------------------------------------|------------------------|-----------------------|
| Non-security out-of-band maintenance     | SRE                    | Optional              |
| Security-related out-of-band maintenance | SIRT                   | SIRT                  |
| Incident communication                   | SRE / Incident manager | Optional              |
| Other urgent communication               | It depends             | Optional              |

## Getting Paged for Concurrent Incidents

Support Engineers are not expected to manage multiple incidents. If a concurrent GitLab.com incident or GitLab Dedicated contact request comes in, engage with the [Support Leader on the Hook (SLOTH)](/handbook/support/workflows/support-leader-on-the-hook/) to help find cover for the new incident.

You can ping the Support Manager oncall in Slack with `@support-manager-oncall`.

## GDCMOC Handover

Follow the [End of Shift Handover Procedure](/handbook/support/workflows/cmoc_workflows/#end-of-shift-handover-procedure) from the CMOC workflows. Make the ingress GDCMOC aware of any Switchboard notifications sent out, issues, Slack threads or tickets they should CC themselves on. Assign the Zendesk ticket used for communication to the next CMOC.
