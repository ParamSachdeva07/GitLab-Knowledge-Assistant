---
title: 'OAuth Clients'
description: 'Documentation on OAuth Clients'
---

## Understanding Zendesk OAuth clients

### Grant types

For information on grant types, please see [Zendesk documentation](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/)

Do note we recommend using the [client_credentials](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/#client-credentials-grant-type) grant type.

### Scope

For information on scope, please see [Zendesk documentation](https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/#scope)

## Using OAuth clients

The generalized process for using an OAuth client is:

- Generate a bearer token
- Perform your API actions
- Revoke the token

### Generating a bearer token

{{% alert title="Note" color="primary" %}}

- You can only generate these via the API or redirect URL flow. This focuses on using the API as the redirect URL flow can vary from setup to setup.

{{% /alert %}}

To generate a bearer token, you need to know the OAuth client's identifier and secret values. You would then make a POST request to the endpoint `oauth/tokens` with the needed payload.

The payload used should be in the format:

```json
{
  "client_id": "CLIENT_IDENTIFIER",
  "client_secret": "CLIENT_SECRET",
  "grant_type": "client_credentials",
  "scope": "SCOPE VALUES TO USE"
}
```

In the returned body, the `access_token` attribute is what you will use as the bearer token.

### Revoking a bearer token

#### Via the UI

To revoke a bearer token via the UI:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Apps and integrations > APIs > OAuth clients`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apis/oauth-clients)
1. Locate the OAuth client you want to revoke a bearer token for
1. Click the three vertical dots to the right of the OAuth client
1. Click `View tokens`
1. Locate the bearer token to revoke and click the three vertical dots to the right
1. Click `Delete`
1. Click `Delete` on the pop-up to confirm

#### Via the API

To revoke a bearer token via the API, you must know the bearer token's ID. You would then make a DELETE request to the endpoint `api/v2/oauth/tokens/:token_id` (replacing `:token_id` with the bearer token's ID).

In the normal process of generating a bearer token via the API, it is very likely you will not know the generated bearer token's ID. As such, you might need to use what you do know (the OAuth client's identifier and the bearer token itself) to get to that end.

As an example, here is what the process might look like for the OAuth client identifier `test123` with the bearer token `abcdefg123456789`:

```ruby
client_identifier = 'test123'
bearer_token = 'abcdefg123456789'

# Get the OAuth client object

url = 'api/v2/oauth/clients'
oauth_clients = request_with_retry(zendesk_client, :get, url)
client_to_use = oauth_clients['clients'].detect { |c| c['identifier'] == client_identifier }

# Get the bearer token object

url = "api/v2/oauth/tokens?client_id=#{client_to_use['id']}"
tokens = request_with_retry(zendesk_client, :get, url)
token_to_use = tokens['tokens'].detect { |t| t['token'] == "...#{bearer_token[-10..]}" }

# Revoke it

url = "api/v2/oauth/tokens/#{token_to_use['id']}"
request_with_retry(zendesk_client, :delete, url)
```

## Administrator tasks

{{% alert title="Danger" color="danger" %}}

**Security Considerations:**

- OAuth clients are able to perform admin-level tasks and can be extremely dangerous.

{{% /alert %}}

### Creating an OAuth client

To create an OAuth client:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Apps and integrations > APIs > OAuth clients`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apis/oauth-clients)
1. Click `Add OAuth client`
1. Enter the needed information
1. Click `Save`
1. Copy the `Secret` value somewhere (as you will need it for generating bearer tokens)
1. Click `Save`
1. Click `Enforce expiration` to confirm

### Editing an OAuth client

To edit an OAuth client:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Apps and integrations > APIs > OAuth clients`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apis/oauth-clients)
1. Locate the OAuth client you want to edit
1. Click the three vertical dots to the right of the OAuth client and click `Edit`
1. Change the values you wish to change
1. Click `Save`

### Deleting an OAuth client

To delete an OAuth client:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Apps and integrations > APIs > OAuth clients`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apis/oauth-clients)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apis/oauth-clients)
1. Locate the OAuth client you want to delete
1. Click the three vertical dots to the right of the OAuth client and click `Delete`
1. Click `Delete client` to confirm the deletion
