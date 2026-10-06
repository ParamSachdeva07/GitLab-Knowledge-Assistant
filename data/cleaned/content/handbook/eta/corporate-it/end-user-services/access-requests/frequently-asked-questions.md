---
title: "Access Requests (AR) in Compass FAQs"
---

## Need help?

- Submit and track access requests through **Compass** — either the Compass app in Slack (type "Compass" in the top search bar to find it) or the Compass web app (accessible via Okta).
- If your request is urgent, please contact IT via the Compass app in Slack or it-help@gitlab.com.

## I need access

### My AR request has been open for a while, how can I get traction on it?

1. Check the status of your request in Compass (Slack app or web app) — the ticket will show where it is in the ToDo/Progress/Waiting On Another Team flow.
2. Confirm the ticket includes the system/vault/group/project you need access to plus the role or permissions needed.
3. Manager approval, where required, is now handled directly within the ticket itself in Compass — check the ticket to confirm whether it's awaiting your manager's approval, and follow up with them there if needed.
4. If the ticket has been approved but is still awaiting provisioning, follow up with the provisioning team via the ticket, or find their Slack channel in our [Tech Stack](https://techstack.gtlb.com/).
5. If you're stuck, reach out to IT via the Compass app in Slack or it-help@gitlab.com.

### So you need access to a system or a group/vault?

1. Submit your request through **Compass** — either the Compass Slack app or the Compass web app (via Okta). This creates an ticket for your request.
2. Do not submit a request for anything that is part of a baseline entitlement unless it got missed during onboarding.
    1. [All team members baseline entitlements](https://internal.gitlab.com/handbook/eta/corporate-it/end-user-services/access-request/baseline-entitlements/#baseline-entitlements-all-gitlab-team-members)
    2. [Role-based baseline entitlements](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/tree/master/.gitlab/issue_templates/role_baseline_access_request_tasks)
3. Necessary approvals (e.g., manager approval) are requested and captured within the ticket itself — no separate labels or GitLab Access Requests.
4. The ticket will route to the appropriate provisioning team automatically. You can also check who provisions access to a given system in our [Tech Stack](https://techstack.gtlb.com/).

### Do I need manager approval? Sometimes

You don't need manager approval if you are requesting the following:

1. An internal team member being added to a Google Workspace email alias or group (unless that group provides permissions to Google Cloud Platform)
2. An internal team member being added to a Slack group
3. Something included in your role-based entitlement

Where manager approval is required, it is requested and tracked automatically within the Compass ticket.

### I need access to the Rails or database production console (grpd)

Please use Teleport to request temporary access to either
[the Rails console](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/teleport/Connect_to_Rails_Console_via_Teleport.md) or
[the database console](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/teleport/Connect_to_Database_Console_via_Teleport.md).

### I need access to version.gitlab.com

You might already have it: [Test if you have a dev account.](https://dev.gitlab.org/)

- If you need a dev account, submit a request through Compass (Slack app or web app via Okta).
- If you have a dev account, go to [version](https://version.gitlab.com/users/sign_in) and login with GitLab and authorize them to use your credentials.

### I need access to Zendesk as a Light Agent

You don't need to submit an access request for Zendesk light access. [Follow the instructions to get access by email](/handbook/support/internal-support/)

### I need to add an email alias, or name change

Please submit your request through Compass (Slack app or web app via Okta) for any email alias additions or name changes.
There are no restrictions on what can be requested, or how many, but please include a short explanation for the addition or change. Some alias requests may be denied if deemed inappropriate or at the discretion of operations.

While this application automation will take place in Okta, "true" system provisioning and deprovisioning will still need to be manually completed within the impacted systems.

### Closing outdated access requests

It is expected that an access request will be completed as soon as possible (7 days).

Tickets that remain open past 7 days from creation may be automatically closed to reduce stale requests and clear out the backlog. Team members will be notified on the ticket three times if it is being automatically closed, along with next steps for any remaining tasks.

Please note: as the process has moved to Compass, we'll continue to refine and confirm the specifics of this auto-closing behavior in the new system.

### I need to remove an existing access

Submit a request through Compass (Slack app or web app via Okta) specifying which access and which person needs to be removed.
