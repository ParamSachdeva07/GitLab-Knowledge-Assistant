---
title: 'End-users'
description: 'Documentation on Zendesk end-users'
---

This guide covers how to create, edit, and manage Zendesk end-users at GitLab. It also covers the end-user settings in Zendesk. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`

{{% /alert %}}

## Understanding end-users

### What are end-users

End-users are the classification of Zendesk user that is below an agent. They are able to access the publicly visible support portals, submit tickets, etc. They are not able to access the agent or backend of Zendesk.

### How we manage end-users

- Zendesk Global: End-users are managed manually in Zendesk  
- Zendesk US Government: End-users are automatically synced via the [Zendesk-Salesforce Sync](/handbook/eta/css/zendesk-salesforce-sync/)

### User notes

User notes and details are two separate text fields on user profiles that store custom information:

- Notes: Internal information visible only to agents
- Details: Additional context about the user

Both fields are automatically posted as internal notes on new tickets via [Zendesk triggers](/handbook/eta/css/zendesk/triggers/).

#### Requesting a user note update as a non-admin

If you need a user note added, modified, or deleted, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

#### Requesting the ban of an end-user as a non-admin

If you need an end-user banned, please post in the #customer_support_systems Slack channel indicating you need a user banned. A member of the Customer Support Systems team will reach out to you (via Direct Message) to work with you on the matter.

### Current system end-user settings

The following settings control how end-users can register, authenticate, and interact with the support portal. These settings are documented here for reference and should rarely be changed.

<details>
<summary>For Zendesk Global</summary>

- Anybody can submit tickets
  - [x] Enabled
    - [x] Require authentication for request and uploads APIs.
    - [ ] Ask users to register
    - User registration message
      > Please fill out this form, and we'll send you a welcome email to verify your email address and log you in.
  - Allowlist
    > gitlab@gitlab.com google.com
  - Blocklist: View directly in Zendesk admin panel - contains sensitive data
- Account emails
  - [ ]  Include a list of active Help Centers in account emails
  - User welcome email text:
    > Welcome to GitLab Support. Please click the link below to create a password and login.
  - [ ] Also send a welcome email when a new user is created by an agent or administrator.
  - Email verification email text
    > We need to verify that you are the owner of this email address. Please follow the link below to verify.
- Allow users to view and edit their profile data
  - [x] Enabled
- Allow users to change their password
  - [x] Enabled
- Validate user phone numbers
  - [ ] Enabled
- Tags on users and organizations
  - [x] Enabled
- Allow users to belong to multiple organizations
  - [ ] Enabled

</details>
<details>
<summary>For Zendesk US Government</summary>

- Anybody can submit tickets
  - [x] Enabled
    - [x] Require authentication for request and uploads APIs.
    - [ ] Ask users to register
    - User registration message
      > Please fill out this form, and we'll send you a welcome email so you can verify your email address and sign in.
  - Allowlist
    > gitlab@gitlab.com google.com
  - Blocklist: View directly in Zendesk admin panel - contains sensitive data
- Account emails
  - [ ]  Include a list of active Help Centers in account emails
  - User welcome email text:
    > Welcome to GitLab Federal Support. Please click the link below to create a password and sign-in.
  - [ ] Also send a welcome email when a new user is created by an agent or administrator.
  - Email verification email text
    > We need to verify that you are the owner of this email address. Please follow the link below to verify.
- Allow users to view and edit their profile data
  - [x] Enabled
- Allow users to change their password
  - [x] Enabled
- Validate user phone numbers
  - [ ] Enabled
- Tags on users and organizations
  - [x] Enabled
- Allow users to belong to multiple organizations
  - [ ] Enabled

</details>

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Creating an end-user

{{% alert title="Warning" color="warning" %}}

- It is exceedingly rare you will need to do this manually. Consider the reason you are doing this carefully and review all documentation to determine if an alternative process should be used.
- We do not alter the `Access` setting of end-users (i.e. the ability to view more than their own tickets). If end-users want to see organization tickets, they need to use a [Shared Organization setup](/handbook/eta/css/zendesk/organizations/shared-orgs).

{{% /alert %}}

To create an end-user in Zendesk:

1. Hover over `+ Add` at the top-left of the page (when not on the admin panel)
1. Click `User`
1. Fill out the `Name`
1. Fill out the `Email`
1. Ensure the `User type` is that of `End user`
1. Click `Add`

### Editing an end-user

{{% alert title="Warning" color="warning" %}}

- For information on organization association, please see our [Organization association documentation](/handbook/eta/css/zendesk/organizations/association).

{{% /alert %}}

By default, we do not edit end-users. We instead encourage them to do so using the support portal itself:

- [For Zendesk Global end-users](https://support.gitlab.com/hc/en-us/articles/11626501035292-Support-Portal-User-Guide#account-management)
- [For Zendesk US Government end-users](https://federal-support.gitlab.com/hc/en-us/articles/22616053222292-Support-Portal-User-Guide#account-management)

There are, however, very specific situations where we would edit an end-user.

#### Resending confirmation email

{{% alert title="Warning" color="warning" %}}

- This can only be done on an unconfirmed email address. Once confirmed, we cannot resend a confirmation email to that address.

{{% /alert %}}

If a user needs the confirmation email resent on their unconfirmed end-user account (i.e. they havent confirmed an email address on their account), you can resend it by doing the following:

1. Navigate to the end-user's page in Zendesk
1. Click the drop-down carrot next to the email address you need to re-send the confirmation email to
1. Click `Resend verification email`

#### Sending a password reset email

To send a password reset email to an end-user:

1. Navigate to the end-user's page in Zendesk
1. Click the `Security settings` tab
1. Click the `Reset` link
1. Select the brand to use
   - For Zendesk Global: `GitLab Support`
   - For Zendesk US Government: `GitLab`
1. Click `Reset password`

#### Adding or removing a secondary email

{{% alert title="Warning" color="warning" %}}

- This cannot be done if the email is in use on a different account

{{% /alert %}}

To add a secondary email to an end-user:

1. Navigate to the end-user's page in Zendesk
1. Click `+ add contact` on the left-side of the page (below the `Primary email` attribute)
1. Click `Email`
1. Type the secondary email address (and hit Enter/Return)

#### Setting a secondary email as the primary

To set a secondary email address as the primary email in Zendesk:

1. Navigate to the end-user's page in Zendesk
1. Click the drop-down carrot next to the email address you want to make the primary
1. Click `Make primary contact`

#### Managing the user note

To modify a user note (or details) of an end-user:

1. Navigate to the end-user's page in Zendesk
1. Click in the textarea you wish to modify (`Notes` or `Details`)
1. Change the text as needed
1. Click anywhere outside of the textarea

### Suspending an end-user

To suspend a user:

1. Navigate to the end-user's page in Zendesk
1. Click the drop-down carrot to the right of `+ New ticket` on the user's page
1. Click `Suspend`
1. Ensure the reason is `Other reason`
1. Ensure the `Additional comment` is blank
1. Click `Suspend user`

### Deleting an end-user

End-user deletions occur, primarily, from three different sources.

#### By end-user request

This occurs where an end-user files a ticket to us requesting their support portal account be deleted. The process for this is:

1. Send the macro `Support::Support-Ops::Confirm Deletion` to the end-user in the ticket
1. If the end-user replies confirming the deletion, then send the macro `Support::Support-Ops::Deletion Forthcoming` to the end-user in the ticket
1. Navigate to the end-user's page in Zendesk
1. Click the drop-down carrot to the right of `+ New ticket` on the user's page
1. Click `Delete`
1. Click `Confirm` on the pop-up that appears

#### By data-privacy request

This occurs (via Transcend) when a user requests a data-privacy deletion. You should be pinged by the system to do so. You will check if the user exists in Zendesk first. If they do, then you should delete the end-user by doing the following:

1. Navigate to the end-user's page in Zendesk
1. Click the drop-down carrot to the right of `+ New ticket` on the user's page
1. Click `Delete`
1. Click `Confirm` on the pop-up that appears

#### By scheduled deletion

For more information on user deletion, please see the documentation on [Automated user deletion](/handbook/eta/css/zendesk/users/automated-user-deletion).

### Compliance level deletion

For more information on compliance level deletions, please see the documentation on [Automated user deletion](/handbook/eta/css/zendesk/users/automated-user-deletion).

### Banning an end-user

{{% alert title="Danger" color="danger" %}}

- This is a serious matter that often needs to involve multiple teams. Confirm if the user needs to be banned from more than the support portal and work with the relevant teams (security, legal, fulfillment, billing, etc.) as needed.

{{% /alert %}}

In the event an end-user needs to be banned (due to various reasons, but especially due to misconduct), someone will post in the #customer_support_systems channel about the matter.

Acknowledge the post and direct message the person to get more details.

Once you have all the details, you would then:

1. Close any non-closed tickets (if needed)
   - For Zendesk Global (replace `TICKET_ID` with the ticket's ID and `API_TOKEN` with your API token):

   ```bash
   curl -ss -X PUT https://gitlab.zendesk.com/api/v2/tickets/TICKET_ID \
     -H "Content-Type: application/json" \
     -d '{"ticket": {"status": "closed"}}' \
     -u support-ops@gitlab.com/token:API_TOKEN
   ```

   - For Zendesk US Government (replace `TICKET_ID` with the ticket's ID and `API_TOKEN` with your API token):

   ```bash
   curl -ss -X PUT https://gitlab-federal-support.zendesk.com/api/v2/tickets/TICKET_ID \
     -H "Content-Type: application/json" \
     -d '{"ticket": {"status": "closed"}}' \
     -u supportops@gitlab.com/token:API_TOKEN
   ```

1. [Modify the end-user's notes](#managing-the-user-note) to add information on the ban (the statement they are being banned, the reason, who to speak to if more details are needed). Something along the lines of this works well:
   > This user has been banned from the support portal as of YYYY-MM-DD by request of TEAM_NAME team.
   >
   > This was due to REASON.
   >
   > If more details are needed, please reach out to the Customer Support Systems team via the #customer_support_systems Slack channel.
   - Replacing:
     - `YYYY-MM-DD` with the current date (in ISO format)
     - `TEAM_NAME` with the name of the team requesting the ban (ex: Support, Security, Legal, etc.)
     - `REASON` with the reason (if a relevant ticket is part of the reason, please ensure that is present in the message)
1. [Suspend the user](#suspending-an-end-user)
1. [Modifying system end-user settings](#modifying-system-end-user-settings), specifically by adding `reject:EMAIL_ADDRESS` to the `Blocklist` setting (replacing `EMAIL_ADDRESS` with the end-user's email address).

After all that is done, confirm via the original request post the end-user has been banned.

### Unbanning an end-user

This is very rare to occur and will likely require a very custom process. Please refer the situation to a Fullstack Engineer to get it looked into.

### Modifying system end-user settings

{{% alert title="Danger" color="danger" %}}

- Exercise extreme caution in doing this, as it can greatly impact the usability of the support portal.
- This should only ever be done in two scenarios:
  - [Banning an end-user](#banning-an-end-user)
  - There is a corresponding request issue (Feature Request, Administrative, Bug, etc.)
- Always ensure [Current system end-user settings](#current-system-end-user-settings) is updated on this page if you change the system end-user settings

{{% /alert %}}

To modify the system end-user settings:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `People > Configuration > End users`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/people/configuration/settings)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/people/configuration/settings)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/people/configuration/settings)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/people/configuration/settings)
1. Make modifications to the settings you wish to change
1. Click `Save tab` at the bottom-right of the page

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
