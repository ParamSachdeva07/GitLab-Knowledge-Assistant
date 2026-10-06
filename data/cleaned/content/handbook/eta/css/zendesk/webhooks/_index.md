---
title: 'Webhooks'
description: 'Documentation on Zendesk webhooks'
---

This guide covers how to create, edit, and manage Zendesk webhooks at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
  - **Note:** Some special webhooks are managed manually in Zendesk (and would thus use ad-hoc deployment methods)
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/webhooks)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/webhooks)

{{% /alert %}}

## Understanding webhooks

### What are webhooks

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks-to-interact-with-third-party-systems):

> A webhook sends an HTTP request to a specified URL in response to an event, such as a trigger or automation firing in Zendesk Support. Web developers typically use webhooks to invoke behavior in another system.

Simplified, it is an HTTP request made to another system. These can be used for things such as GitLab issue creation, alerting Slack, etc.

### Using a webhook in Zendesk

Webhooks are used exclusively by other items in Zendesk (usually Zendesk events, automations, and triggers). As such, you do not "directly" use them. You instead "indirectly" use them when the triggering object runs.

### How we manage webhooks

We currently manage all webhooks within Zendesk itself.

## Creating webhooks as a non-admin

For the creation of a webhook, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing webhooks as a non-admin

For the modification of a webhook, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting webhooks as a non-admin

For the deletion of a webhook, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing webhooks in Zendesk

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Apps and integrations > Webhooks > Webhooks`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/webhooks/webhooks)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/webhooks/webhooks)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/webhooks/webhooks)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/webhooks/webhooks)

You can click on the webhook's name for more information.

### Viewing logs for a webhook

To view the logs for a webhook:

1. Go to the [webhooks page](#viewing-webhooks-in-zendesk)
1. Click on the name of the webhook you wish to view the logs for
1. Click on the `Activity` tab

From there, you can click the Invocation ID of an event to see more details.

### Testing a webhook

To test a webhook:

1. Go to the [webhooks page](#viewing-webhooks-in-zendesk)
1. Click on the name of the webhook you wish to view the logs for
1. Click the `Actions` link at the top-right of the page
1. Click `Test Webhook`
1. Enter the payload information (what exactly you use will vary based off the webhook itself)
1. Click the `Send test` button

### Webhook subscriptions

Webhooks use subscriptions to determine when they run. For more information on webhook subscriptions, see [Zendesk's documentation](https://developer.zendesk.com/api-reference/webhooks/event-types/webhook-event-types/).

### Webhook request formats

The valid request formats for Zendesk webhooks are:

- JSON (API value: `json`)
- XML (API value: `xml`)
- Form encoded (API value: `form_encoded`)

### Webhook authentication

Webhooks can use the following authentication methods:

- None (API value: `none`)
- API Key (API value: `api_key`)
- Basic authentication (API value: `basic_auth`)
- Bearer token (API value: `bearer_token`)

The intricacies of how those work can be read about via [Zendesk's documentation](https://developer.zendesk.com/documentation/webhooks/webhook-security-and-authentication/)

### Creating a webhook

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- Remember just creating a webhook doesn't mean it will be used.

{{% /alert %}}

If the webhook is clean of sensitive information in its endpoint or custom headers, you can utilize the sync repo. However, if it contains sensitive information, such as an API token or a secret, in its endpoint/custom headers, you will need to create it in Zendesk itself. The preference should always be a setup that enables the use of the sync repo whenever possible.

When creating it using the sync repo, the exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
name: 'Name of webhook'
previous_name: 'Name of webhook'
description: 'Description of webhook'
status: 'active'
subscriptions:
- 'subscription_to_use'
endpoint: 'URL to use'
http_method: 'Method type to use'
request_format: 'Format of the request'
authentication: null
custom_headers: null
```

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

If you need to create it manually in Zendesk:

1. Go to the [webhooks page](#viewing-webhooks-in-zendesk)
1. Click the `Create webhook` button at the top-right of the page
1. Select the type of webhook
   - Events: Based off Zendesk events, such as user creation, organization modification, etc.
   - Trigger or automation: Run via trigger or automation
1. Click `Next` (at the bottom-right of the page)
1. If making an `Events` type webhook:
   1. Select the event types to use
   1. Click `Next` (at the bottom-right of the page)
1. Enter the name of the webhook
1. Enter a description for the webhook (optional)
1. Enter an endpoint URL (i.e. where a payload is sent)
1. Select the request method
1. Select the request format
1. Enter the type of authentication to use
1. Enter any additional headers needed (up to 5)
1. While optional, you will have the opportunity to test the webhook you are creating. You should do this to ensure it is going to work properly.
   - Clicking the button will bring up the test prompt. See [Testing a webhook](#testing-a-webhook) for more information.
1. Click `Create webhook` button at the bottom-right of the page

### Editing a webhook

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can have many severe downstream impacts on objects using webhooks. Exercise caution when doing this.

{{% /alert %}}

To edit a webhook, you will need to determine if it is managed in the sync repo or in Zendesk directly.

If it is managed via the sync repo, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

If it is managed in Zendesk directly:

1. Go to the [webhooks page](#viewing-webhooks-in-zendesk)
1. Click on the name of the webhook you wish to edit
1. Click the `Actions` link at the top-right of the page
1. Click `Edit`
1. Make the changes you need to make
1. While optional, you will have the opportunity to test the webhook you are modifying. You should do this to ensure it is going to work properly.
   - Clicking the button will bring up the test prompt. See [Testing a webhook](#testing-a-webhook) for more information.
1. Click the `Update` button at the bottom-right of the page

#### Changing the name of a webhook via the sync repo

If you need to change the name of a webhook, copy the current value into the `previous_name` attribute and then change the `name` attribute. This allows the sync to still locate the webhook in question to update.

### Updating authentication information for a webhook via the sync repo

If you need to update the authentication information for a webhook, such as updating the API key used, there are some special steps you need to take in the sync repo itself:

1. Navigate to the sync repo
1. Navigate to the CI/CD settings
   - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/webhooks/-/settings/ci_cd)
   - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/webhooks/-/settings/ci_cd)
1. Add a `file` type CI/CD variable named `TOKENS`

The contents of the CI/CD variable will be a JSON block with the information needed (encased in an Array).

As an example, if you needed to update the `PRIVATE-TOKEN` value for the webhook `Do a thing` to `abc123`, the contents of the `TOKENS` CI/CD file variable would be:

```json
[
  {
    "name": "Do a thing",
    "PRIVATE-TOKEN": "abc123"
  }
]
```

That is then used by the sync repo to update the `PRIVATE-TOKEN` value for the webhook `Do a thing` on the next deployment run.

This method can be used to update the authentication information for multiple webhooks in one update:

```json
[
  {
    "name": "Do a thing",
    "PRIVATE-TOKEN": "abc123"
  },
  {
    "name": "Do another thing",
    "PRIVATE-TOKEN": "def456"
  }
]
```

The deployment run ends by removing the CI/CD file variable `TOKENS` (to prevent it using that information to force another unneeded update on the next deployment run).

### Deactivating a webhook

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can have many severe downstream impacts on objects using webhooks. Exercise caution when doing this.

{{% /alert %}}

To deactivate a webhook, you will need to determine if it is managed in the sync repo or in Zendesk directly.

If it is managed via the sync repo, you will need to create a MR in the sync repo. In this MR, you should do the following to the corresponding trigger's YAML file:

1. Move the file from the `active` to `inactive` path
1. Modify the value of the `active` attribute to `false`

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

If it is managed in Zendesk directly:

1. Go to the [webhooks page](#viewing-webhooks-in-zendesk)
1. Click on the name of the webhook you wish to deactivate
1. Click the `Actions` link at the top-right of the page
1. Click `Deactivate`
1. Click `Deactivate webhook` to confirm the deactivation

### Deleting a webhook

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- When deleting a webhook, you likely will need to also remove the file from the sync repo.

{{% /alert %}}

As the sync repos do not perform deletions, you will need to do this via Zendesk itself.

To delete a webhook in Zendesk:

1. Go to the [webhooks page](#viewing-webhooks-in-zendesk)
1. Click on the name of the webhook you wish to delete
1. Click the `Actions` link at the top-right of the page
1. Click `Delete`
1. Click `Delete webhook` to confirm the deletion

### Performing an exception deployment

To perform an exception deployment for webhooks managed by the sync repo, navigate to the webhooks sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the webhooks.

## Monitoring

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/webhook-monitor)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/webhook-monitor)

{{% /alert %}}

### How it works

Using [GitLab scheduled pipelines](https://docs.gitlab.com/ci/pipelines/schedules/), the `bin/process` script runs every hour on the 15 minute mark (using UTC timezone). This script does the following:

- Gathers a list of all webhooks in the Zendesk instance
- Gathers a list of all invocations for each webhook (that ran in the last hour)
- Filters out the list of invocations to remove all successful invocations
- Posts in Slack for each non-successful invocation

### Actioning on failed invocations

When you are alerted about failed invocations for a Zendesk instance, you should review the invocation itself to determine next steps. The exact action to perform will depend on the failure itself:

- If the failure stems from the payload used by Zendesk, file a bug issue
- If the failure stems from the endpoint:
  - Retry the invocation by:
    - Copying the `Request body` used
    - [Testing the webhook tied to the invocation](#testing-a-webhook) using a custom payload
  - If the retry fails, file a bug issue

### Making changes to the webhook monitor

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To modify the webhook monitor, you will need to create a MR in the corresponding project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. Being this is an `Ad-hoc` deployment type, the changes will be used in the next scheduled run.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.

### Not seeing webhook changes after a merge

As webhooks follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
