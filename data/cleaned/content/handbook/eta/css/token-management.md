---
title: 'Token management'
description: 'Documentation on token management'
---

This guide covers token management practices for Customer Support Systems, including token rotation procedures and automated token expiration monitoring.

Proper token management is critical for maintaining security across our systems. Regular token rotation reduces the risk of unauthorized access from compromised credentials, and our Token Checker automation helps ensure tokens are rotated before expiration. This document provides step-by-step procedures for rotating tokens across various platforms (Zendesk, GitLab) and explains how to work with Token Checker alerts.

## Rotating tokens

### Rotating a Zendesk API token

To rotate a token in Zendesk:

1. Navigate to the admin panel for the Zendesk instance in question:
   - [Zendesk Global](https://gitlab.zendesk.com/admin)
   - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin)
   - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin)
1. Navigate to `Apps and integrations > APIs > API tokens`:
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apis/api-tokens)
   - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apis/api-tokens)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apis/api-tokens)
   - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apis/api-tokens)
1. Deactivate the existing token (as you cannot delete the token until it is deactivated)
   1. Locate the existing entry for the token and click the three vertical dots to the right of it
   1. Click `Deactivate`
   1. Click `Deactivate` on the popup box to confirm it
1. Delete the existing token
   1. Locate the existing entry for the token and click the three vertical dots to the right of it
   1. Click `Delete`
   1. Click `Delete` on the popup box to confirm it
1. Create a new token
   1. Click `Add API token` in the top-right of the page
   1. Enter a description
   1. Click `Save`
   1. Copy the token in the `Token` field
   1. Click `Save` once again

### Rotating a GitLab personal access token

To rotate a GitLab personal access token, you will need to use a curl command and must have the following information:

- A valid personal access token for the user who owns the personal access token you are rotating
- The ID of the personal access token being rotated

You will then make the following curl request:

```bash
curl -ss -X POST "https://gitlab.com/api/v4/personal_access_tokens/TOKEN_ID/rotate?expires_at=$(DATE_COMMAND)" \
  --header "Content-Type: application/json" \
  --header "PRIVATE-TOKEN: VALID_TOKEN"
```

Replacing:

- `TOKEN_ID` with the ID of the personal access token being rotated
- `VALID_TOKEN` with the valid personal access token for the user who owns the personal access token you are rotating
- `DATE_COMMAND` with the following (depending on your OS):
  - Linux: `date -I -d'+1 year'`
  - Mac: `date -v+1y +%Y-%m-%d`

This will rotate the token in question and output the new token. It is often advised to pipe that command into `jq '.token'` so it just outputs the new token value. An example of this is:

```bash
curl -ss -X POST "https://gitlab.com/api/v4/personal_access_tokens/123456/rotate?expires_at=$(date -I -d'+1 year')" \
  --header "Content-Type: application/json" \
  --header "PRIVATE-TOKEN: abc123" | jq '.token'
"def456"
```

### Rotating a GitLab project access token

To rotate a GitLab project access token, you will need to use a curl command and must have the following information:

- A valid personal access token for the user with `Maintainer` permissions to the project
- The ID of the project that contains the project access token
- The ID of the project access token being rotated

You will then make the following curl request:

```bash
curl -ss -X POST "https://gitlab.com/api/v4/projects/PROJECT_ID/access_tokens/TOKEN_ID/rotate?expires_at=$(DATE_COMMAND)" \
  --header "Content-Type: application/json" \
  --header "PRIVATE-TOKEN: VALID_TOKEN"
```

Replacing:

- `PROJECT_ID` with the ID of the project that contains the project access token
- `TOKEN_ID` with the ID of the personal access token being rotated
- `VALID_TOKEN` with the valid personal access token for the user with `Maintainer` permissions to the project
- `DATE_COMMAND` with the following (depending on your OS):
  - Linux: `date -I -d'+1 year'`
  - Mac: `date -v+1y +%Y-%m-%d`

This will rotate the token in question and output the new token. It is often advised to pipe that command into `jq '.token'` so it just outputs the new token value. An example of this is:

```bash
curl -ss -X POST "https://gitlab.com/api/v4/projects/1234/access_tokens/5678/rotate?expires_at=$(date -I -d'+1 year')" \
  --header "Content-Type: application/json" \
  --header "PRIVATE-TOKEN: abc123" | jq '.token'
"def456"
```

### Rotating a GitLab pipeline trigger token

#### As a user

To rotate a GitLab pipeline trigger token as a user:

1. Login to the gitlab.com user the token will be created by
1. Navigate to the project itself
1. Go to the `CI/CD` page (under Settings)
1. Expand the `Pipeline trigger tokens` section
1. Sort through the list of existing tokens to locate the one you need to rotate
1. Delete the existing token
1. Click the `Add new token` button at the top-right of the section
1. Enter an appropriate name:
   - If a Zendesk webhook, put the link to the webhook itself
   - If a Zendesk app, use the format `INSTANCE - NAME_OF_APP`
     - `INSTANCE` is the Zendesk instance itself (ex: Zendesk Global, Zendesk US Government)
     - `NAME_OF_APP` is the name of the app as Zendesk display it
   - If for a CI/CD job within the same project, put the name of the job
   - If for another project, put the link to the project
1. Copy the API token generated
1. Put the token into place where needed

#### As a service bot

To rotate a GitLab pipeline trigger token as a service bot:

1. Create a project access token for the project in question
1. Make note of the project's ID number
1. Use that API token to create a pipeline trigger token via the gitlab.com API

   ```bash
   curl --request POST \
     --header "PRIVATE-TOKEN: TOKEN_YOUR_COPIED" \
     --form description="APPROPRIATE_DESCRIPTION_HERE" \
     "https://gitlab.com/api/v4/projects/PROJECT_ID/triggers"
   ```

   - `TOKEN_YOUR_COPIED` is the project access token you copied
   - `APPROPRIATE_DESCRIPTION_HERE` is an appropriate description:
     - If a Zendesk webhook, put the link to the webhook itself
     - If a Zendesk app, use the format `INSTANCE - NAME_OF_APP`
       - `INSTANCE` is the Zendesk instance itself (ex: Zendesk Global, Zendesk
         US Government)
       - `NAME_OF_APP` is the name of the app as Zendesk display it
     - If for a CI/CD job within the same project, put the name of the job
     - If for another project, put the link to the project
1. Copy the API token generated
1. Put the token into place where needed

## Applying tokens

### For Zendesk apps

To apply a token to a Zendesk app:

1. Navigate to the admin panel for the Zendesk instance in question:
   - [Zendesk Global](https://gitlab.zendesk.com/admin)
   - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin)
   - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin)
1. Navigate to `Apps and integrations > Apps > Zendesk Support apps`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apps/support-apps)
   - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apps/support-apps)
1. Locate the app in question and click on it
1. Locate the field that needs the API token in question
1. Put the token into that field
   - **NOTE** Do not populate or edit any other fields
1. Click the blue `Update` button at the bottom of the page

### For Zendesk webhooks

To apply a token to a Zendesk webhook:

1. Navigate to the admin panel for the Zendesk instance in question:
   - [Zendesk Global](https://gitlab.zendesk.com/admin)
   - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin)
   - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin)
1. Navigate to `Apps and integrations > Webhooks > Webhooks`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/webhooks/webhooks)
   - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin/apps-integrations/webhooks/webhooks)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/webhooks/webhooks)
   - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/webhooks/webhooks)
1. Locate the webhook in question
1. Click the 3 vertical dots to the far-right of the webhook in question
1. Click the `Edit` option
1. Replace the old token with the new token where needed
1. Click the blue `Update` button at the bottom-right of the page

### For GitLab webhooks

Due to being unable to edit the value of masked sections in webhooks, we have to "delete and create" it to rotate a token

1. Navigate to the project itself
1. Go to the `Webhooks` page (under Settings)
1. Locate the webhook in question and copy all relevant information from it (the URL, what it triggers on, etc.)
1. Delete the webhook in question
1. Re-create the webhook using the relevant information and the new token

### For GitLab CI/CD variables

To apply a token for GitLab CI/CD variables:

1. Navigate to the project itself
1. Go to the `CI/CD` page (under Settings)
1. Expand the `Variables` section
1. Sort through the list of existing variables to locate the one you need to replace
1. Click the pencil icon at the far-right of the variable (if you hover over it, it says `Edit`)
1. Put the new token in the `Value` field
1. Click the blue `Save changes` button

## OAuth Integrations

### Integrating a new OAuth Application into Zendesk

{{% alert title="Note" color="primary" %}}

- Adding an OAuth integration requires `Owner` access to Zendesk.

{{% /alert %}}

To integrate a new OAuth application into Zendesk:

1. Enable admin bypass for SSO
   1. Navigate to the admin panel for the Zendesk instance in question:
      - [Zendesk Global](https://gitlab.zendesk.com/admin)
      - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin)
      - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin)
      - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin)
   1. Navigate to `Account > Security > Advanced`
      - [Zendesk Global](https://gitlab.zendesk.com/admin/account/security/advanced/authentication)
      - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin/account/security/advanced/authentication)
      - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/account/security/advanced/authentication)
      - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin/account/security/advanced/authentication)
   1. Under `SSO bypass`, click `Admins`
   1. Click the `Save` button at the bottom-right of the page
1. Open a new browser and navigate to `https://gitlab.zendesk.com/access/sso_bypass`
1. Login as the integration user
1. Perform the OAuth flow as directed by the application.
   - Verify the scopes requested are documented and approved in the access request. If they are not, STOP.
1. Log out as the integration user
1. Disable admin bypass for SSO:
   1. Navigate to the admin panel for the Zendesk instance in question:
      - [Zendesk Global](https://gitlab.zendesk.com/admin)
      - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin)
      - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin)
      - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin)
   1. Navigate to `Account > Security > Advanced`
      - [Zendesk Global](https://gitlab.zendesk.com/admin/account/security/advanced/authentication)
      - [Zendesk Global Sandbox](https://gitlab1707170878.zendesk.com/admin/account/security/advanced/authentication)
      - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/account/security/advanced/authentication)
      - [Zendesk US Government Sandbox](https://gitlabfederalsupport1585318082.zendesk.com/admin/account/security/advanced/authentication)
   1. Under `SSO bypass`, click `Account owner`
   1. Click the `Save` button at the bottom-right of the page

## Token Checker

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [Token Checker](https://gitlab.com/gitlab-support-readiness/token-checker)

{{% /alert %}}

### Understanding Token Checker

#### What is Token Checker

Token Checker is a setup we have made using GitLab [scheduled pipelines](https://docs.gitlab.com/ci/pipelines/schedules/) to check for tokens expiring within the next 3 weeks. The types of tokens checked are:

- Personal access tokens
- Project access tokens

#### How Token Checker works

Every Monday at 1400 UTC (`0 14 * * 1`), a GitLab [scheduled pipeline](https://docs.gitlab.com/ci/pipelines/schedules/) executes the `bin/run` script, which does the following:

- Fetches all active personal access tokens (that expire within the next 3 weeks) for the gitlab.com users managed by the Customer Support Systems team, storing the information to an array
- Fetches all projects within gitlab.com groups managed by Customer Support Systems, looping over them to:
  - Fetch all non-revoked project access tokens for the project (that expire within the next 3 weeks), storing the information to an array
- Creates an issue reporting soon to expire tokens (if any were stored in the array)

### Working issues created by Token Checker

{{% alert title="Note" color="primary" %}}

- This requires access to all gitlab.com users, groups, and projects managed by Customer Support Systems.

{{% /alert %}}

To work an issue generated by the Token Checker, you will go through the list of items to either revoke or rotate the listed tokens.

- If the token in question is no longer in use, revoke it. After doing so, check the box next to it on the list and add a comment indicating the token was revoked.
- If the token in question is still in use, rotate it. After doing so, check the box next to it on the list.

Once you have worked all items on the list, add a comment indicating all needed tasks have been completed and close out the issue.

### Making changes to Token Checker

{{% alert title="Note" color="primary" %}}

- This requires at least `Developer` access to the [Token Checker](https://gitlab.com/gitlab-support-readiness/token-checker) project.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To make changes to the Token Checker, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR (which will have them applied on the next scheduled run).
