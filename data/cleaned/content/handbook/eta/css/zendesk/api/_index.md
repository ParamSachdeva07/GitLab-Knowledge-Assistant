---
title: 'API'
description: 'Documentation on Zendesk API'
---

## Understanding Zendesk API

### What is Zendesk API

The [Zendesk Support API](https://developer.zendesk.com/api-reference/ticketing/introduction/) is a collection of Zendesk endpoints you can use to get various information or do various tasks. It is quite robust and something we use quite often.

### What are Zendesk API tokens

{{% alert title="Warning" color="warning" %}}

Zendesk API token use is [being deprecated](https://support.zendesk.com/hc/en-us/articles/10840968198042-Announcing-the-removal-of-API-tokens-as-an-authentication-method-for-API-requests) 2027-04-30.

{{% /alert %}}

Zendesk API tokens are used in authentication for Zendesk API requests. These tokens are always at the administrator level and cannot be issued at lower permission/role levels. As such, you should always use caution in using and issuing these tokens.

### What are Zendesk integrations

Zendesk integrations are permanent connections between Zendesk and third-party services. Unlike API tokens which can be easily revoked, integrations are more deeply embedded in Zendesk's configuration and are significantly harder to remove. Integrations should only be used for production systems that require persistent access.

### API Rate Limits

Zendesk enforces rate limits on API requests. See [Zendesk rate limits documentation](https://developer.zendesk.com/api-reference/introduction/rate-limits/) for current limits and best practices.

### Requesting an API token or integration

Both API tokens and integrations follow this approval process:

1. **Submit Request**: File an [access request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=API_Token_Request)
1. **Manager Approval**: The requester's manager must approve the request
1. **Security Review**: A Fullstack Engineer, Customer Support Systems reviews the business justification
1. **Decision**: If approved, the engineer will create the token or integration

**Key Differences:**

- **API Tokens**: Created directly in Zendesk, shared via 1Password
- **Integrations**: Created using Integration bot account, process varies by integration type

### How to authenticate to the Zendesk API

#### Basic authentication

{{% alert title="Note" color="primary" %}}

The ability to do this is not enabled on our production Zendesk instances.

{{% /alert %}}

To authenticate using basic authentication, you’ll need to know your username (email) and password for your Zendesk account. With those in hand, you can either use those directly or encode the string into base64 (and use it in the headers).

Example of using it raw:

```bash
curl https://example.zendesk.com/api/v2/users.json \
  -u jcolyer@example.com:my_password
```

Example of using it via headers:

```bash
echo 'jcolyer@example.com:my_password' | base64
amNvbHllckBnaXRsYWIuY29tOm15X3Bhc3N3b3JkCg==

curl https://example.zendesk.com/api/v2/users.json \
  -H "Authorization: Basic amNvbHllckBnaXRsYWIuY29tOm15X3Bhc3N3b3JkCg=="
```

#### API token authentication

To authenticate via an API token, you’ll need to know your username and the API token in question. With those in hand, you can either use those directly or encode the string into base64 (and use it in the headers). When using an API token, you must add /token after your username.

Example of using it raw:

```bash
curl https://example.zendesk.com/api/v2/users.json \
  -u jcolyer@example.com/token:api_token
```

Example of using it via headers:

```bash
echo 'jcolyer@example.com/token:api_token' | base64
amNvbHllckBnaXRsYWIuY29tL3Rva2VuOmFwaV90b2tlbgo=

curl https://example.zendesk.com/api/v2/users.json \
  -H "Authorization: Basic amNvbHllckBnaXRsYWIuY29tL3Rva2VuOmFwaV90b2tlbgo="
```

#### OAuth access token authentication

To use an OAuth access token, you’d first need to create an OAuth app in Zendesk (see [Zendesk documentation](https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application) for more information). With the access token in hand, you would pass this into the headers.

```bash
curl https://example.zendesk.com/api/v2/users.json \
  -H "Authorization: Bearer gErypPlm4dOVgGRvA1ZzMH5MQ3nLo8bo"
```

### How to use the Zendesk API

{{% alert title="Note" color="primary" %}}

This focuses solely on the Zendesk API via curl. For more information on using a library, check out the corresponding library’s documentation.

{{% /alert %}}

To get started, you would need to know the endpoint you wish to use. Generally speaking, the most common ones you might use for quick actions are:

- [Zendesk Support API Tickets endpoints](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/)
- [Zendesk Support API Users endpoints](https://developer.zendesk.com/api-reference/ticketing/users/users/)
- [Zendesk Support API Organizations endpoints](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/)

For more administrative tasks, the common ones you might use are:

- [Zendesk Support API Ticket Forms endpoints](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_forms/)
- [Zendesk Support API Ticket Fields endpoints](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields/)
- [Zendesk Support API Views endpoints](https://developer.zendesk.com/api-reference/ticketing/business-rules/views/)
- [Zendesk Support API Triggers endpoints](https://developer.zendesk.com/api-reference/ticketing/business-rules/triggers/)
- [Zendesk Support API Macros endpoints](https://developer.zendesk.com/api-reference/ticketing/business-rules/macros/)
- [Zendesk Support API Automations endpoints](https://developer.zendesk.com/api-reference/ticketing/business-rules/automations/)

Once you have determined what you wish to do, go to the corresponding API endpoint documentation and make note of:

- The request type
  - `GET`
  - `POST`
  - `PUT`
  - `PATCH`
  - `DELETE`
- The endpoint URL
- Any required parameters

From there, you will craft a curl command in the format of:

```bash
curl ZENDESK_URL/api/v2/ENDPOINT \
  -X REQUEST_TYPE \
  -H HEADER_INFO \
  -u AUTHENTICATION \
  -d DATA_TO_USE
```

Where:

- `ZENDESK_URL` is the URL of the Zendesk instance
- `ENDPOINT` is the endpoint to use
- `-X REQUEST_TYPE` is the request type from the documentation (not needed if making a GET request)
- `-H HEADER_INFO` is any needed header information (not always needed)
- `-u AUTHENTICATION` is the user/pass or user/token combo (not needed if using header based authentication)
- `-d DATA_TO_USE` is the data to send with the request (not always needed)

As an example, if you wanted to get the details for automation `12345`, your curl command might look like:

```bash
curl https://example.zendesk.com/api/v2/automations/12345 \
  -H "Authorization: Basic amNvbHllckBnaXRsYWIuY29tL3Rva2VuOmFwaV90b2tlbgo="
```

Likewise, if you wanted to update automation `12345` to set `active` to `false` (i.e. deactivate it), your curl command might look like:

```bash
curl https://example.zendesk.com/api/v2/automations/12345 \
  -H "Authorization: Basic amNvbHllckBnaXRsYWIuY29tL3Rva2VuOmFwaV90b2tlbgo=" \
  -H "Content-Type: application/json" \
  -X PUT \
  -d '{"automation": {"active": false}}'
```

If we wanted to delete automation `12345`, your curl command might look like:

```bash
curl https://example.zendesk.com/api/v2/automations/12345 \
  -H "Authorization: Basic amNvbHllckBnaXRsYWIuY29tL3Rva2VuOmFwaV90b2tlbgo=" \
  -H "Content-Type: application/json" \
  -X DELETE
```

## Administrator tasks

{{% alert title="Danger" color="danger" %}}

**Security Considerations:**

- All Zendesk API tokens are admin-level and extremely dangerous. Issue only when absolutely necessary.
- Integrations are significantly harder to revoke than API tokens and pose higher security risks.

**Requirements:**

- Integrations must be created via the Integration bot agent account.
- Integration requests for Zendesk US Government are not currently supported due to security requirements.

{{% /alert %}}

### Token creation requests

{{% alert title="Important" color="info" %}}

The token description in Zendesk must be the URL of the access request issue for tracking and auditing purposes.

{{% /alert %}}

All requests for an API token should be done via an [access request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=API_Token_Request).

There are two exceptions to this:

- API tokens for Customer Support Systems team members personal use
- API tokens for Support Systems scripts/automations/etc.

Once an access request is filed, the requester’s manager must approve the request.

After that has been done, the provisioner for the instance (traditionally a Fullstack Engineer, Customer Support Systems) will review the request.

During this review, we carefully review the business reasons and use-case of each request due to the significant access level that an API token provides.

If deemed acceptable, the Fullstack Engineer, Customer Support Systems will then create the API token. To create the API token:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Navigate to `Apps and integrations > APIs > API tokens`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apis/api-tokens)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apis/api-tokens)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apis/api-tokens)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apis/api-tokens)
1. Click `Add API token` in the top-right of the page
1. Enter a description (remember, it should be the access request issue's URL)
1. Click `Save`
1. Copy the token in the `Token` field
1. Click `Save` once again

The API token will then be shared with the requester via a one-time accessible 1Password item.

### Integration requests

All requests for an integration should be done via an [access request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=API_Token_Request).

Once an access request is filed, the requester’s manager must approve the request.

After that has been done, the provisioner for the instance (traditionally a Fullstack Engineer, Customer Support Systems) will review the request.

During this review, we carefully analyze the business reasons and use-case due to the significant access level that integrations provide. Integrations pose even higher risks and should be avoided whenever possible. While API tokens can be quickly and easily revoked, integrations cannot.

If deemed acceptable, the Fullstack Engineer, Customer Support Systems will then create the integration.

The exact means for this will vary by integration type. Refer to the specific integration's documentation for setup steps. All integrations must be created using the Integration bot account for the Zendesk instance to ensure proper tracking and revocation capabilities.

### Revoking an API token

To revoke an API token:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Navigate to `Apps and integrations > APIs > API tokens`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/apps-integrations/apis/api-tokens)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/apps-integrations/apis/api-tokens)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/apps-integrations/apis/api-tokens)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/apps-integrations/apis/api-tokens)
1. Locate the token in question and click the three vertical dots (at the far right of the token entry)
1. Click `Deactivate`
1. Confirm the revocation by clicking `Deactivate` in the pop-up box

### Revoking an integration

Specifics cannot be provided here as it will vary from integration to integration.
