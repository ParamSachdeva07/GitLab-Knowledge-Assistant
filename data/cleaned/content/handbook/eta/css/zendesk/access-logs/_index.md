---
title: 'Access logs'
description: 'Documentation on Zendesk access logs'
---

This guide covers how to view and manage Zendesk access logs at GitLab. Access logs track read and write events in Zendesk, providing an audit trail of admin and agent actions.

## Understanding Access Logs

### What are access logs

As per [Zendesk](https://developer.zendesk.com/api-reference/ticketing/account-configuration/access_logs/):

> The access log is a 90-day record of events that captures what an agent or admin has accessed in your account without necessarily updating, creating, or deleting anything. The access log is your record of read and write events for your account.

### Understanding Cursors

Access logs use cursor-based pagination. A cursor is a pointer that marks the last-read position in the log stream, allowing the system to fetch only new entries since the last check.

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing access logs

To view the access logs:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Account > Logs > Access log`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/account/logs/access-log)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/account/logs/access-log)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/account/logs/access-log)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/account/logs/access-log)

## Automated Log Monitoring

### Overview

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/access_logs)

{{% /alert %}}

For Zendesk Global (production), we send access log entries for specific endpoints to Devo and Elasticsearch. Other instances (sandbox instances, US Government) do not currently have this automated monitoring.

This is done via the [Access logs project](https://gitlab.com/gitlab-support-readiness/zendesk-global/access-logs).

### How it works

Via a scheduled pipeline, the `bin/run` script runs (currently every 10 minutes) to capture and forward security-relevant access events. This provides near-real-time monitoring of sensitive admin actions.

The `bin/run` script does the following:

1. Reads the monitored endpoint information via the `data/endpoints.yaml` file
1. Loops over each endpoint to:
   - Get all entries since the last checked cursor value
   - Logs the new cursor value checked
1. Sends the log entries to Devo and Elasticsearch (if any exist)
1. Commits any cursor changes to the `data/endpoints.yaml` file

### Endpoints monitored

Currently, the endpoints monitored are:

- `/admin/api/private/accounts/current/remote_authentications`
- `/admin/api/private/accounts/current/security_settings`
- `/admin/api/private/team_members`

### Requesting more endpoints as a non-admin

If you wish to request more endpoints are monitored, please [file a feature request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?issuable_template=Feature) with the Customer Support Systems team.

### Adding more endpoints as an admin

To add a new endpoint, you will create a MR on the project modifying the `data/endpoints.yaml` file. In the file, you need to add the full URI of the new endpoint as well as a starting cursor.

To locate the starting cursor, check the access logs via the API (using [this endpoint](https://developer.zendesk.com/api-reference/ticketing/account-configuration/access_logs/#list-access-logs)). Replace `YOUR_EMAIL` and `YOUR_API_TOKEN` with your credentials in the example below:

```bash
jason@laptop:~$ curl -ss "https://gitlab.zendesk.com/api/v2/access_logs?filter[path]=/api/v2/users/search&page[size]=100" \
  --header "Content-Type: application/json" \
  -u YOUR_EMAIL/token:YOUR_API_TOKEN | jq '.meta.after_cursor'
"ABCDEF123456"
```

Using that example, our new entry would be:

```yaml
- endpoint: "/api/v2/users/search"
  cursor: ABCDEF123456
```

After a peer reviews and approves your MR, merge it. The new endpoint will be monitored starting with the next scheduled run.

## Common issues and troubleshooting

As this is a fairly new item we are utilizing, there is nothing here yet. Via iteration, we will populate this as needed.
