---
title: Log and audit requests
description: "Overview of aggregated information which GitLab Support may provide to customers, from the gitlab.com logs. Details beyond a summary require a Security request."
category: GitLab.com
subcategory: Security
---

## Log requests for GitLab.com

> 📝 **Note:**
> As of April 2026, the Security Log Request process has changed. Customer Support can now fulfill log requests using [this process](https://internal.gitlab.com/handbook/support/workflows/security-logs-runbook/).

Users often ask for access to GitLab.com logs, typically, due to [IP blocks](/handbook/support/workflows/ip-blocks), a possible security issue, or for internal auditing purposes.

Always include a link to the log as an internal note, with additional information if needed.

A standard response is available in ZenDesk as a macro [`Support::SaaS::Gitlab.com::Audit logs access request`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Audit%20logs%20access%20request.md?ref_type=heads).

If required, you can escalate the ticket/issue by following our [escalation process](/handbook/support/internal-support/support-ticket-attention-requests).

You can consider using the [Kibana workflow](/handbook/support/workflows/kibana/) page for tips on retrieving logs for requests within the last 30 days. Log requests beyond a summary (similar to the examples below) or where logs are not readily available on Kibana should be handled according to the process outlined in the handbook page dedicated to [providing assistance to GitLab.com customers during customer-based security incidents](/handbook/security/customer-requests/). GitLab's Security Incident Response Team handles complex, extensive requests according to an internal [runbook](https://internal.gitlab.com/handbook/security/cross_functional_runbooks/customer_security_incidents/) for customer response operations.

If the customer has raised an emergency request for logs in relation to a security incident, first verify that the customer has revoked or changed any potentially affected tokens and passwords to prevent any additional unintended access. In most cases, the emergency ticket should be downgraded to high priority and handled with the [providing assistance to GitLab.com customers during customer-based security incidents](/handbook/security/customer-requests/) process. Review with the [Support Manager on Call](/handbook/support/on-call/#engaging-the-on-call-manager) if the customer requests a more urgent response.

### Who can make a request

#### Paid Subscriptions

- Only a Group Owner of a pre-existing paid namespace can make a request.
- [Account ownership verification](/handbook/support/workflows/account_verification/) **must** be completed before any log requests are processed.

> NOTE: A user cannot upgrade to a paid subscription to gain access to logging requests.

#### Free Users

Support will only provide information [when GitLab initiates contact due to an incident](https://about.gitlab.com/support/statement-of-support/#free-users).

If a free user/group needs information for an investigation their options are:

- Access audit events by either requesting an [Ultimate trial](https://gitlab.com/-/trials/new) or purchasing a subscription.
  Audit events are locked behind a valid subscription, so even GitLab admins are unable to view events of a free group.
  The user will need to perform their own investigation using the audit events whether they use a trial or purchase a subscription.
- Review events from the group activity overview (`https://gitlab.com/groups/<group-name>/-/activity`).

Free users receiving 429 responses should review [GitLab.com rate limits documentation](https://docs.gitlab.com/user/gitlab_com/#rate-limits-on-gitlabcom).

### What we can provide

If the customer request matches one of the templates defined in the [internal runbook](https://internal.gitlab.com/handbook/support/workflows/security-logs-runbook/), Customer Support can fulfill the log request directly by following the process outlined there.

If the request does not match an available template, we can provide generic summary information such as the below.

- Information found in the [Audit Events Features](https://docs.gitlab.com/administration/audit_event_reports/)
- Information about who has accessed the account/projects that the customers owns.  This can include:
  - number of users
  - number of times accessed
  - number of unique IPs
  - range of timestamp of occurrence
  - project path
- Provide the above excluding a known list. For example, number of IP addresses not originating from a user's "work office".
- Ensure you add the Zendesk ticket tag: `customer_log_requests` for reporting and audit purposes.

### What we cannot provide without a SIRT escalation

We cannot provide the following information:

- Information about accounts or projects that the requester does not own.
- Any information considered [Personal Data](/handbook/support/workflows/personal_data_access_account_deletion/) that is not specifically about the individual requester.
- Any information that would disclose GitLab confidential information or processes.

### When to create a SIRT escalation

If a user requests log data that may contain [Personal Data](/handbook/support/workflows/personal_data_access_account_deletion/) we will need to verify their identity and create a [SIRT Log Access Request](/handbook/security/customer-requests/) using the "Customer Request" issue type.

### What to do if the question is not covered here?

Escalate to #support_leadership in Slack and reach out to the `@support-manager-oncall`.

### Sending logs and other Personal Data

**Do not share logs or personal data until [account ownership](/handbook/support/workflows/account_verification/) has been verified.**

Any [Personal Data](/handbook/support/workflows/personal_data_access_account_deletion/) information that is pulled by the Security Incident Response Team (SIRT),
such as for a [log request](/handbook/security/customer-requests/), needs to be delivered compressed and password protected to the requester with the following guidelines:

- The password should be a random string of at least 10+ characters including numbers, lower and upper case letters.
- The password protected file should be attached to the ZenDesk ticket
  - Use the command `zip -er [TicketNumber].zip filename` or other encryption tool to encrypt the file.
  - Use 1Password to generate the random secure password for the encryption
  - Save the password in 1Password as `[ticket number].zip`
  - Share the password to the customer using [the 1Password Share Items feature](https://support.1password.com/share-items/). Add the customer's e-mail address to the shared password item.
  - Set the share duration to seven days
  - Let the customer know that the shared password will expire in seven days and will need to be recorded locally if future access is required.
  - Send the link to the shared password item separately through your email account directly to the customer's email address.
- Once the customer had successfully received and opened the files you should delete the pulled data from your computer and the password from 1Password
If the log files are too large to attach to the ticket in ZenDesk, refer to the [Provide large files to GitLab support](https://about.gitlab.com/support/providing-large-files/) page.

In case you need to share the data pull results internally, such as in an internal issue, upload the files to Google Drive, such as the [Support Ticket Attachments folder](https://drive.google.com/drive/folders/1RpCb_li2RTYsE8GnVFExCux3QpZ2i0TD) (internal).

### Examples

The following are examples to provide a better idea of what responses we can provide.

#### Example 1: Who accessed a specific repo

A customer, who had accidentally set their project to the incorrect visibility setting, wanted to know if anyone outside the company accessed their project. Here is a modified excerpt of the response:

> Excluding users who have the company email domain, 2 users viewed the main project page a total of 4 times between 20:06 and 20:10 UTC 2019-08-15. However, I can confirm that all 4 instances originated from one of the IP addresses you provided as being from your office.

From ticket: [129594](https://gitlab.zendesk.com/agent/tickets/129594)

#### Example 2: IP block

User writes in to say their entire team is getting blocked and they want to know the source. When the user writing in has access to the projects in question, we can provide the specific path(s).

> It appears that the majority of requests that returned `401`, which likely caused the temporary block, involved `/project/path`.

Example ticket: [132652](https://gitlab.zendesk.com/agent/tickets/132652)

Also see ["Identifying the Cause of IP Blocks on GitLab.com"](/handbook/support/workflows/ip-blocks).

#### Example 3: GitLab requests action due to high load

GitLab reached out to the owners of a project that was causing concern for the production team, who asked Support to reach out. The user wanted to know where the requests were originating from.

> There are 3 different IPs showing in our logs, 2 of which are based in CountryA and 1 in CountryB (please note these locations may not be accurate as they are based purely on geolocation web searches). They also all have the same user agent.

Example ticket: [130153](https://gitlab.zendesk.com/agent/tickets/130153)

#### Example 4: Enterprise users accidentally creates a public repository and pushes confidential data

A namespace owner may request access logs when a repository is accidentally created by [a user in their organization](https://docs.gitlab.com/user/enterprise_user/#identifying-enterprise-users) and left public. The specific user and path(s) need to be identified for a properly-scoped request.

> User `username` accidentally created project `testproject-name` and left it open. We have removed the project and would like to verify if anyone accessed or cloned the project while it was public.

Example ticket: [690251](https://gitlab.zendesk.com/agent/tickets/690251)
