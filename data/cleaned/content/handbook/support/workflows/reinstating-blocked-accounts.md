---
title: Locked, Blocked and Banned Accounts
category: GitLab.com
subcategory: Security
description: How to determine if a blocked user can be re-instated
---

This workflow page will describe how to action on **Locked**,  **Blocked** and **Banned** accounts. Sometimes users believe they are blocked, but their accounts are locked. There are several ways to verify:

1. The best way to view this information is via the [Zendesk User Lookup app (part of the GitLab Super App)](/handbook/eta/css/zendesk/apps/global#gitlab-super-app), through the `Locked` and `State` fields.
1. The Admin User UI in `/admin/user/USERNAME` will say `(Locked)`, `(Blocked)` or `(Banned)` next to the name at the top.
1. The [Users API](https://docs.gitlab.com/api/users/#get-a-single-user) through the URL `https://gitlab.com/api/v4/users/<user_id>` in your browser while logged in as an Admin User, also indicates the `locked` and `state` status of the user.

Our implementation of [Arkose Protect](https://docs.gitlab.com/integration/arkose/#arkose-protect) does *not* affect account locking, but instead can prevent users from signing in without solving the challenge.

## Locked accounts

When a user has been identified as locked, you can use the [`Support::SaaS::Account Locked` macro](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Account%20Locked.md?ref_type=heads) to help explain the situation to the user. A user can be locked if:

2FA is **not** enabled:

- They do not have 2FA enabled and there have been 3 or more failed login attempts within 24 hours.
- Accounts are **not** unlocked automatically. The user receives an email with a six-digit unlock code *after* a successful login. They are then redirected to a verification page where they can unlock their account by entering the code. The code is valid for 60 minutes only, but they can request a new code by clicking a link on the verification page.

2FA **is** enabled:

- There have been 5 or more failed login attempts within 10 minutes.
- Accounts are unlocked automatically after a 10 minute waiting period.

If the user does not receive a verification email with the 6-digit code, it's likely that the primary email address is inactive or inaccessible. If a user does not have access to their primary email address, they cannot unlock their account or reset their password. Consider other workflows such as [swapping email addresses](/handbook/support/workflows/account_changes#account-access-requests) if a user is not able to access their primary email.

All verification emails with unlock codes and password reset emails bypass Mailgun suppressions. Mail delivery of these emails can also be seen in Mailgun.

You can see `Account Locked` states in [Kibana](/handbook/support/workflows/kibana/) by searching for `json.message: Account Locked`. Here's an example of what it might look like it Kibana:

![locked_account](/images/support/locked_example.png)

### Manual unlock

A user should attempt all self-serve methods first.

If self-serve methods have been exhausted and a member of a group with a paid subscription still cannot access their account,
we can consider a manual unlock if necessary. For example, if a user cannot receive external email to receive codes, a manual unlock may be required. Note that only an admin user can modify a user account on SaaS.

Process:

1. Follow the locked accounts workflow above and ensure that the user has exhausted all self-serve methods first.
1. For other cases, [comment or create an issue](/handbook/support/workflows/working-with-issues/) as applicable.
1. Do an [account ownership verification](/handbook/support/workflows/account_verification/).
1. [Unlock the account from the admin area](https://docs.gitlab.com/security/unlock_user/#unlock-user-accounts-from-the-admin-area)
1. [Add an admin note](/handbook/support/workflows/admin_note/).

Feature request for group owners to self-serve is in [anti-abuse#339](https://gitlab.com/gitlab-org/modelops/anti-abuse/team-tasks/-/issues/339).

### Identity verification exemption requests

### Accounts experiencing problems verifying with a credit card and/or phone number

When a user is unable to complete credit card and/or phone number verification.

Support team members can create an exemption by following the instructions available in the [Internal Handbook](https://internal.gitlab.com/handbook/support/workflows/identity-verification-exemptions/)

## Blocked Accounts

This workflow is used to determine if a blocked or a banned user can be reinstated.

### Why is account blocked?

If the account is blocked, look for the admin note on the account to determine why it has been blocked.
    - The [GitLab user lookup app](/handbook/eta/css/zendesk/apps/global#gitlab-super-app) in Zendesk will show the admin notes for the user if they have contacted support using the email address associated with their account.  Alternatively -
    - If you have access to ChatOps you can use the below command in any chatops enabled Slack channel to read admin notes for the user
        > `/chatops run user find <username or email>`

### Blocked by Trust and Safety Team

T&S will not block accounts at this time; they will only ban them.

### User is blocked with no admin note

In some situations, a user may be blocked without an Admin Note. In these situations, we need to investigate the reason for the block.

#### User did not confirm their account and are scheduled for deletion

If a user does not confirm their account within 3 days of creation, the account is automatically blocked and scheduled for deletion.

The user's primary email will typically show as "Unverified" on their admin profile: `https://gitlab.com/admin/users/<username>`

Organizations that provision user accounts through SAML or SCIM without a verified domain, will still require user email confirmation. The email may be verified for the account, but the user may still not have completed email verification. In these situations, we need to check the logs to determine if a user is scheduled for deletion:

- Search Kibana for user deletion events [query](https://log.gprd.gitlab.net/app/r/s/Ot5q3):

    `json.meta.caller_id.keyword: DeleteUserWorker and json.details.custom_message: '<username>'`

- If the user is scheduled for deletion, you will see a message in the `json.details.custom_message` field like:

    `User <username> scheduled for deletion. Reason: GitLab automatically deletes unconfirmed users after 3 days since their creation`

Note: There is no mechanism to remove an unconfirmed account from the deletion queue. See [work item 7646](https://gitlab.com/gitlab-com/support/support-team-meta/-/work_items/7646) for more details.

### User initiated self-serve deletion

If the Admin Note is `User deleted own account on {timestamp}`, this means the user initiated the self-serve deletion. See [Cancelling delayed account deletion](#cancelling-delayed-account-deletion).

1. **Free user** accounts need to wait 7 days, starting the day of the deletion request, to create a new account with the same email address or username. Use the [`Support::SaaS::Gitlab.com::Blocked Accounts::Blocked due to account deletion`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Blocked%20Accounts/Blocked%20due%20to%20account%20deletion.md?ref_type=heads) macro.
1. **Exceptions in which Support can force deletion** - If a user is not part of a paid namespace but needs to be added to a paid namespace (user or top-level group owner creates the ticket), or if a paid user added below the top-level group and still subject to the 7-day delay period (True until [this issue](https://gitlab.com/gitlab-org/gitlab/-/issues/416651) is fixed): then Support can follow the steps below to bypass the 7 day delay:
   - Use the [`Support::SaaS::Gitlab.com::Blocked Accounts::Blocked due to account deletion`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Blocked%20Accounts/Blocked%20due%20to%20account%20deletion.md?ref_type=heads) macro and ask for explicit permission from the user to bypass the 7d wait period and delete the account.
   - When confirmation is received, SE (with Admin access) deletes the account.
   - SE updates the ticket with the result of the deletion.
1. **Paid user** accounts that are direct members of a top-level paid namespace have no deletion delay and their account is deleted immediately (within 1 hour), see [this MR](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/121912).

### Embargoed countries

If the block or complaint is related to access from an embargoed country, use the [`Support::SaaS::Gitlab.com::Abuse::TOS Section 10 (Embargoed Countries)`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Abuse/TOS%20Section%2010%20(Embargoed%20Countries).md?ref_type=heads) macro.
    - If the user provides the requested information, then complete the `Trust and Safety` [Account Reinstatement Request](https://gitlab.com/gitlab-com/gl-security/security-operations/trust-and-safety/TS_Operations/account-reinstatements/-/issues/new?issuable_template=Account%20Reinstatement) template in the Trust and Safety Operations tracker. Otherwise, reaffirm the block cannot be removed.
    - Proceed with this action for both **free** and **paid** users.

### Business and regulatory obligations (China region)

Users may be blocked in order to comply with business and regulatory obligations in Mainland China, Hong Kong and Macau. This will be reflected in an admin note on the user's account.

More information and the support workflow for these accounts can be found in the [Internal Handbook](https://internal.gitlab.com/handbook/support/workflows/regulatory-region-blocks/).

### Professional Services migrations

Professional Services migrations can also block users as part of their process. Admin notes for migrations were added as of `2022-08-19` through [this issue](https://gitlab.com/gitlab-org/professional-services-automation/tools/migration/congregate/-/issues/818). Older migrated accounts may not have an admin note. As of `2024-09-18`, requests to unblock accounts that were blocked during a Professional Services migration are worked automatically (see [STM #6336](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/6336)).

If you receive a ticket for an unblock request and you think it should have been automatically worked, you should:

1. Check that all ticket fields are at expected values
1. Notify Support Operations so that they can investigate
1. Work the ticket manually using the guidance below to ensure a timely resolution for the requestor

If a ticket was not automatically worked, Support can manually unblock the user in the following cases:

- Blocked users or top-level group owners can submit a support ticket to be unblocked. Once they are [verified](/handbook/support/workflows/account_verification), the user can be unblocked. Leave an [admin note](/handbook/support/workflows/admin_note) on the user stating they were unblocked, with the date and ticket number.
- For [Enterprise users](/handbook/support/workflows/gitlab-com_overview/#enterprise-users), the `owner` of the top-level namespace the user belongs to can submit the ticket. Follow the [account verification](/handbook/support/workflows/account_verification/), and add an [admin note](/handbook/support/workflows/admin_note/) as usual, including if it was user or owner requested.
- You can also ask for clarification or assistance in the [#professional_services](https://gitlab.slack.com/archives/CFRLYG77X) channel if needed.
- Proceed with this action for both **free** and **paid** users.

### No admin note and none of the above

- **Paid accounts** can be unblocked with authorization from a user with the Owner role in the top level namespace. [Account ownership verification](/handbook/support/workflows/account_verification) must be completed by the group Owner first.
- **Free accounts** can only be unblocked under exceptional circumstances and in combination with leadership approval. [Account ownership verification](/handbook/support/workflows/account_verification) must be completed first.

### Account is successfully unblocked

If an account is unblocked, use the [`Support::SaaS::Gitlab.com::Blocked Accounts::Account Reinstated- Success`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Blocked%20Accounts/Account%20Reinstated-%20Success.md?ref_type=heads) macro to notify the user the account has been unblocked.

### Account to remain blocked (no reinstatement)

If the final decision is that the user's account is not to be reinstated, apply the [`Support::SaaS::Gitlab.com::Blocked Accounts::RemainBlocked`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Blocked%20Accounts/RemainBlocked.md) macro. This will provide a standard statement to the user and the ticket **will be closed**.

Applying the macro will provide the user no opportunity of reply through the existing ticket, care should be taken before applying the macro to ensure that this is the intended action.

## Banned accounts

1. Proceed with the next steps **only** if at least one of the following scenarios is true:
    1. The email address the user has used to raise their request matches an email address associated with the account the request is intended for. This criteria can be applied to both free users and customers.
    1. The user account is classified as an [Enterprise user](/handbook/support/workflows/gitlab-com_overview#enterprise-users) and an owner of the top-level group raises the ticket.

### Bans by Trust and Safety

Trust and Safety will only ban accounts, not block them. These actions are frequently actioned by automation.

Reasons for the bans will appear in the Custom attributes section at the bottom of the user's admin page.

For these accounts, if no T&S issue exists, complete the [Account Reinstatement Request](https://gitlab.com/gitlab-com/gl-security/security-operations/trust-and-safety/TS_Operations/account-reinstatements/-/issues/new?issuable_template=Account%20Reinstatement)
template.

A security member of the team will review the request within 24 hours. If the request is urgent,
please reach out in the [#abuse](https://gitlab.enterprise.slack.com/archives/C0HPYBJ3D) Slack channel.

1. Send the [`Support::SaaS::Gitlab.com::Blocked Accounts::Escalated-TrustAndSafety`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Blocked%20Accounts/Escalated-TrustAndSafety.md?ref_type=heads) macro for the initial response to the user.
1. If account is restored, use the [`Support::SaaS::Gitlab.com::Blocked Accounts::Account Reinstated- Success`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Blocked%20Accounts/Account%20Reinstated-%20Success.md?ref_type=heads) macro to notify the user the account has been restored. Otherwise, provide the reasoning from the Reinstatement Request as to why their account will remain banned.

#### Omamori automated bans

Accounts that are banned by Omamori automation will contain the following:

- Omamori_mitigation_plan
- blocked_feature
- blocked_category
- omamori_mitigation_plan_executed_by

#### auto_banned_by

Users may be auto-banned based on certain characteristics, such as, inputting a banned phone number for verification.

The reason for ban will appear in the Custom attributes section in the field `auto_banned_by`.

### Bans for other reasons

Support does not currently have examples of accounts that are banned without automation from Trust and Safety.

If you encounter an example that is not documented above, reach out in the [#abuse](https://gitlab.enterprise.slack.com/archives/C0HPYBJ3D) Slack channel
for confirmation on if an [Account Reinstatement Request](https://gitlab.com/gitlab-com/gl-security/security-operations/trust-and-safety/TS_Operations/account-reinstatements/-/issues/new?issuable_template=Account%20Reinstatement)
should be opened or if Support can unban the user.

If instructed to unban the user leave an admin note with the date and action taken.

For all other blocks or bans that do not match any of the above scenarios, unblock or unban the user, and leave an admin note with the date and action taken.

## Cancelling delayed account deletion

It is possible for self-initiated account deletion to be cancelled within the 7-day delay period. See [Unblocking the account will cancel the account deletion](https://gitlab.com/gitlab-org/modelops/anti-abuse/team-tasks/-/issues/423).

A request to cancel the deletion of an account may be made by a member of a *paid* group or a top-level owner if the user is an [Enterprise user](/handbook/support/workflows/gitlab-com_overview#enterprise-users). We do not cancel account deletion for free users.

Process:

1. The paid user or top-level owner must successfully pass [account verification](/handbook/support/workflows/account_verification).
1. [Unblock the user](https://docs.gitlab.com/administration/moderate_users/#unblock-a-user) and leave an [admin note](/handbook/support/workflows/admin_note) on the user stating they were unblocked, with the date and ticket number.

### Namespace admin requests deletion cancel for claimed user

A namespace admin (top-level group Owner) may request cancellation of a
pending account deletion for a [claimed (Enterprise) user](/handbook/support/workflows/gitlab-com_overview#enterprise-users)
within the 7-day delay period. This applies when the user initiated
self-serve deletion but the namespace admin needs the account retained
for business continuity.

**Example scenario:** A developer (`@dev-user`) who is an Enterprise user
under the `acme-corp` top-level group initiates self-serve account
deletion. The group Owner (`@acme-admin`) notices the pending deletion
and submits a support ticket requesting it be cancelled because the user
is still needed.

Process:

1. Verify the requester is an Owner of the top-level group that claims
   the user. Use the
   [GitLab user lookup app](/handbook/eta/css/zendesk/apps/global#gitlab-super-app)
   or the [Members API](https://docs.gitlab.com/api/members/) to
   confirm the Owner role.
1. Confirm the target account is an
   [Enterprise user](/handbook/support/workflows/gitlab-com_overview#enterprise-users)
   claimed by the requester's namespace.
1. The namespace Owner must successfully pass
   [account verification](/handbook/support/workflows/account_verification).
1. [Unblock the user](https://docs.gitlab.com/administration/moderate_users/#unblock-a-user)
   to cancel the pending deletion.
1. Leave an [admin note](/handbook/support/workflows/admin_note) on the
   user stating the deletion was cancelled at the namespace Owner's
   request, with the date and ticket number.
1. Notify the namespace Owner that the
   deletion has been cancelled.

> **Note:** The user's own consent is not required for this action
> because Enterprise users' accounts are managed by the namespace admin.
> However, if the user subsequently re-initiates deletion, the namespace
> admin may need to address the underlying reason with the user directly.

---

NOTE:
The rest of this page is for **reference** only and should be updated to point to Security's workflow.

### Policy Reference

1. All decisions about account reinstatement are final and there is no process for appeals.
1. These criteria are to be taken as examples **only**, and **not** as binding principles.
1. If the account violates our ToS again within a 12 month period, it could result in being permanently banned.

#### An account can be reinstated when

1. The user agrees to remove the content in question within the requested time frame.
1. The user has provided a sufficient use case for violating our Terms of Use.
1. The user agrees to remove or export the content away from GitLab.com within 24 hours.
1. The DMCA/Trademark complaint has been resolved.

#### An account **cannot** be reinstated when

1. The user refuses to take corrective measures on the account.
1. The user continues to violate our ToS.
1. The user intentionally violates our ToS.
1. Any abusive language or hostile activity towards the support engineer.
1. The account presents damage to the GitLab business and/or brand.
