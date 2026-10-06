---
title: "Okta API Access"
description: "API access to Okta services"
---
## Overview

[Okta API](https://developer.okta.com/docs/api/) provides programmatic access to Okta. This includes access to user, group, app, security, and other data. Due to highly sensitive, confidential, and critical nature of our Okta tenant and data, programmatic access is highly restricted.

## API Services Apps

The default method for programmatic access to Okta at GitLab is the [API Service App (OAuth 2.0)](https://developer.okta.com/docs/guides/implement-oauth-for-okta-serviceapp/main/). API Service apps provide access via the client credentials grant flow using scoped OAuth 2.0 access tokens. API Services app provide greater security than other Okta API access methods.

- More access granularity with scopes
- Shorter token lifetimes
- Permissions are app specific instead of user-inherited
- Programmatic token rotation

### API Service App Requirements

- Unique API Service app created for each integration or service.
- The app may not be used for any other purpose but the one specifically requested.
- The app's scopes must be limited to necessary scopes only.
- The app must have a unique individually assigned admin role.
  - The role must be limited to necessary permissions only.
  - If a custom role is used, the role must be unique.
  - If a custom role is used, the role must be limited to necessary scopes only.
  - If a custom role is used, the resource set must be limited to necessary resources only.
- Demonstrating Proof of Possession (DPoP) enabled and configured when possible.
- Non-interactive token-exchange disabled when possible.
- A network zone with a restricted list of IP addresses must be configured and assigned to the app.

## API Tokens & Service Accounts

{{% alert title="Warning" color="warning" %}}
Access with API token and service account is explicitly denied. Exceptions will be made only for critical systems which require access to Okta and cannot support API Service Apps (OAuth 2.0). Approval of exceptions is under the discretion of the Identity team.
{{% /alert %}}

[API token](https://developer.okta.com/docs/guides/create-an-api-token/main/) provides a http `Authorization` header method for accessing Okta. This method is less secure than the API Services app, and is generally prohibited.

### API Token Requirements

- Token associated with a unique dedicated service account.
- Token not associated with a human user.
- The service account must have an individually assigned admin role.
  - The role must be limited to necessary permissions only.
  - If a custom role is used, the role must be unique.
  - If a custom role is used, the role must be limited to necessary scopes only.
  - If a custom role is used, the resource set must be limited to necessary resources only.
- A network zone with a restricted list of IP addresses must be configured and assigned to the token.
- The service account and API token may only be used for programmatic access to Okta as specifically requested.
- Interactive login blocked on the service account.
- And other additional security requirements.

API tokens are automatically deactivated when the service account is deactivated. Tokens are automatically deactivated after 30 days of inactivity.

## Rate limiting

By default, all API Services apps and tokens are rate-limited at 50% of each API's rate limit. Further rate limiting is strongly recommended for any service interacting with Okta that may regularly encroach on [Okta's API rate limits](https://developer.okta.com/docs/reference/rate-limits).
