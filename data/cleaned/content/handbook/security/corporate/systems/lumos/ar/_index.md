---
title: Lumos Access Request Guide
---

## Overview

You can request access to applications by creating an access request in the [Lumos App Store](https://app.lumosidentity.com/app_store).

Lumos will automatically notify and get approval from your manager, system owner, and any other approvals needed.

If provisioning automation exists, Lumos will perform the app provisioning automatically. If not, Lumos will notify the system owner to perform the manual provisioning steps and will report back when the system owner has confirmed provisioning is complete.

We are migrating tech stack applications to Lumos iteratively and not all apps are available yet. We are prioritizing applications based on provisioning automation capabilities and those with higher volume of access requests.

## Create an Access Request

1. Open Lumos from the Okta tile or in the Slack sidebar
2. Select the app from the list
3. Select the following options:

    - Who the access is for
    - Permission needed
    - Access length
    - Business justification — "why" the access is needed

    <img src="/images/security/corporate/systems/lumos/ar/lumos_appstore_and_app.png" alt="Lumos App Store and Access Request" width="600"/><br>

### Or in Slack

1. Find the Lumos app
2. Click **Request Access**
3. Select the app, permission, and the target user

<img src="/images/security/corporate/systems/lumos/ar/lumos_appstore_slack.png" alt="Lumos App Store in Slack" width="400"/><br>

When all approvals are completed, Lumos will notify you that access is granted

## Approve an Access Request

1. Open the message that was received in Slack or Email, or visit Lumos from the Okta tile
2. If in Slack, simply click Approve, add comments, or Deny the request
3. Or from the email, click **View Request on Lumos** and Approve, add comments, or Deny the request

    <img src="/images/security/corporate/systems/lumos/ar/lumos_appstore_slack_approve.png" alt="Lumos Approval in Slack" width="600"/><br>

    <img src="/images/security/corporate/systems/lumos/ar/lumos_appstore_email_approve.png" alt="Lumos Approval in Email" width="600"/><br>

    <img src="/images/security/corporate/systems/lumos/ar/lumos_appstore_web_approve.png" alt="Request Approval in Lumos" width="600"/><br>

{{% alert title="Can you change the level of access being granted before approval?" color="warning" %}}

Yes! Click the “Edit” button on the Slack approval request, or click on the approval request in Lumos, then change the groups to which the user requested.

You might need to do this if someone is being added to an “admin” group and shouldn’t be in that group. If the user shouldn’t have access at all, just deny the request!

{{% /alert %}}

## Provision an app

**Note:** For apps with manual provisioning, the app admin will be requested to confirm the provisioning was performed

1. Open the message that was received in Slack or Email, or visit Lumos from the Okta tile
2. Perform the user creation within the app's admin interface
3. Return to Lumos and confirm that the user has been created

    <img src="/images/security/corporate/systems/lumos/ar/lumos_appstore_slack_provision.png" alt="Confirm user provisioned in app" width="600"/><br>

## What is the status of my Lumos Access Request?

You can find the status of your Lumos Access Request in the *Messages* tab of the Lumos Slack app. All requests you have made will appear in the Messages tab, and they will be dynamically updated as their status changes.

When the access request is complete, the request status will update to indicate access is granted.

  <img src="/images/security/corporate/systems/lumos/ar/lumos_access_granted.png" alt="Message indicating successful app access request" width="600"/><br>

## Request an app is added to the Lumos App Store

- Any app with an Okta login can be added to Lumos. The best candidates have role-based access permissions controlled by Okta groups. [Open an issue](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?issuable_template=lumos_appstore_add_app) to be scheduled for a future iteration.
