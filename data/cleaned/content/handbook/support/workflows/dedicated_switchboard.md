---
title: GitLab Dedicated Switchboard Troubleshooting
category: GitLab Dedicated
description: "GitLab Dedicated Support - Switchboard"
---

## Overview

Switchboard is a portal customers use to manage their GitLab Dedicated instance. Select GitLab team members have access to Switchboard.
Read more about what the goals of Switchboard are on the [Switchboard handbook page](/handbook/engineering/infrastructure-platforms/gitlab-dedicated/switchboard/).

## Accessing Switchboard

GitLab Support Engineers can access the [Switchboard](/handbook/engineering/infrastructure-platforms/gitlab-dedicated/switchboard/) application by searching for **Switchboard (production)** in the [Okta](/handbook/eta/corporate-it/end-user-services/okta/) homepage.

You can also access directly:

1. Navigate to https://console.gitlab-dedicated.com
1. Enter your GitLab email and click **Continue**
1. You should be signed in to Switchboard through Okta

A complete list of Switchboard URLs can be found [in the Switchboard project docs](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/switchboard/-/blob/main/README.md#deployed-environments).

During [onboarding](https://docs.gitlab.com/administration/dedicated/#onboarding-to-gitlab-dedicated-using-switchboard), GitLab Dedicated customers get access to Switchboard. Temporary credentials are sent to these customers through email. If these credentials expire, customers may open a Support ticket. Support Engineers should open a [request for help](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-Switchboard) with Switchboard.

### Customers with Dedicated Preprod deployments

GitLab Support Engineers can access [Switchboard for Preprod](https://console.gitlab-dedicated.systems/) deployments. Look for the **Switchboard Preprod Dedicated** tile in Okta.

### Viewing Switchboard as a customer

To see Switchboard exactly as customers do, a test tenant admin account (`supportsandbox`) is available. Credentials are stored in the **GitLab Dedicated - Support** 1Password vault. See [work item 13573](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/work_items/13573) for details.

### Password reset

External Switchboard users can reset their password independently using the Switchboard application.

### Multi-factor authentication (MFA) reset

Switchboard users cannot reset their MFA themselves.

To reset MFA, create a [request for help issue](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-Switchboard) for the Switchboard team.

## Accessing customer configuration

When launching Switchboard, you should default to the `/tenants` page with a list of tenant customers.
**Name**, **Identifier**, **Internal reference**, and **External URL** are listed in a table.
Click on **Manage** to view settings for that customer.

### Understanding Tenant Status Indicators

The Switchboard Overview page displays real-time status information for each GitLab Dedicated instance. When troubleshooting customer-reported incidents, support engineers should refer to the [GitLab documentation](https://docs.gitlab.com/administration/dedicated/tenant_overview/#tenant-status) to understand these status indicators.

Watch this [demo on YouTube](https://www.youtube.com/watch?v=RANeaAeitsU) to see how tenant status indicators appear to customers and internal users (Support and Dedicated SREs).

#### Support Actions on Customer-reported Incidents

When responding to customer-reported incidents:

1. [Log in to Switchboard](dedicated_switchboard.md#accessing-switchboard)
1. Select the affected tenant
1. Check the tenant status and take the appropriate action:

**Normal status:**

- No known internal incidents
- [Raise a Dedicated incident](dedicated.md#raise-a-dedicated-incident) to engage the Dedicated SRE on-call

**Degraded Performance** or **Service Disruption:**

- Review **Active incidents** to determine if the customer-reported impact matches an internal incident

  - **If a relevant incident exists:** Inform the customer that SREs are actively investigating and they will receive [ongoing incident updates through Switchboard](dedicated_cmoc.md#providing-ongoing-incident-updates-using-switchboard)
  - **If no relevant incident exists:** [Raise a Dedicated incident](dedicated.md#raise-a-dedicated-incident) to engage the Dedicated SRE on-call

#### Important Notes for Support

- Status indicators are **informational only** and not factored into SLA calculations
- Status updates may take 1-2 minutes to appear after incident state changes
- Severity 3 or 4 incidents aren't displayed (minimal customer impact)
- Incidents in non-impacting lifecycle stages won't appear
- If incident occurs during maintenance, both incident and maintenance statuses will be displayed

### Checking for Past Notifications in Switchboard

Switchboard allows for the [Communications Lead](/handbook/engineering/infrastructure-platforms/incident-management/roles/communications-lead/) to create outbound communications (see [Sending Notifications Using Switchboard](dedicated_cmoc/#sending-notifications-using-switchboard)). When troubleshooting Dedicated support tickets, checking if any Notifications have been sent can be a helpful first step.

All customer notifications are logged in Switchboard.

#### View notifications for a specific tenant

To view past notifications sent to a specific tenant:

1. Select the relevant tenant.
1. In the left sidebar, select **Notifications**.
1. Select the title of a notification to view its message and recipients.

You can filter the list by title, status, or trigger type.

#### View notifications sent to all tenants

To view past notifications sent to all tenants:

1. Click on your profile in the top left corner.
1. Select **Customer notifications**.
1. Click on the Title of the relevant notification to view the message and its recipients.

Watch this [overview on YouTube](https://www.youtube.com/watch?v=e2ZRD8csjow) of how these notifications are created and how they can be viewed in Switchboard.

- **Visibility of what the email looks like from a customer's perspective**

  The following is an example of a notification about an incident. It is from the test environment but formatting will be the same.

  ![Example email screenshot](/images/support/switchboard_comms_email_example.png)

- **Sender's email address**

  The sender's email address will depend on the Switchboard environment. Here are the two email addresses used for customer tenants:

  - Production: `switchboard@gitlab-dedicated.com`
  - Preprod: `switchboard@gitlab-dedicated.systems`

- **Email subject(s) used**

  - Investigating alerts on your GitLab Dedicated instance
  - Update: Investigating your GitLab Dedicated instance
  - Update: High-priority response for your GitLab Dedicated instance
  - Update: Working to resolve your GitLab Dedicated instance issue
  - Resolved: Your GitLab Dedicated instance is operational
  - Emergency maintenance scheduled for your GitLab Dedicated instance
  - Emergency maintenance completed

  These can also be found in the [templates](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/switchboard/-/tree/main/lib/tenants/notification_templates) and new ones may be added over time.

- **Possible backend checks to confirm if an email has been delivered to the customer's mail servers**

  This will not be available. Switchboard can confirm that an email was sent and you can access historical notifications using Switchboard but we cannot confirm whether an email was successfully delivered to the customer's mail server. We can only confirm that it was sent.

### Version information

Check the `Tenant Details` collapsible section.

### Maintenance schedule

Check the `Maintenance` collapsible section.

### Opensearch links

These are available to Support team members on the Tenant Overview page.

### Customer contacts

Check the `Customer Communication` section on the Tenant Overview page.

Customer CSM (formerly TAM) is also included in this section.

### AWS regions

Check the Tenant Overview page.

### View history

- Click the **Audit Logs** link at the top of the page.
- Filter for `Tenant`.
- Check the **Tenant#<tenant_id>** records to view changes.

## GitLab Dedicated Switchboard SSO Provisioning

To provision SSO for a GitLab Dedicated customer via Switchboard:

1. Open an issue in the [Request for Help](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-Switchboard-SSO) issue tracker using the `SupportRequestTemplate-Switchboard-SSO` template.
1. An Engineer from Switchboard will action and provision the SSO configuration, ready for Support to enable it when the customer is ready.
1. The Support Engineer can access the SSO configuration on the Tenant's configuration page in Switchboard:
   1. Click **Edit**
   1. Click the **Enabled** checkbox
   1. Click **Save**
1. The SSO configuration will be enabled immediately for the Tenant.

   **⚠️ Important:** Once enabled, tenant users can **only** log in with their Identity Provider via SSO, unless it is disabled again. Ensure the customer is ready for this change before enabling.
