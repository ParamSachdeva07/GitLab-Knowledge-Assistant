---
title: Account Deletion & Data Access Requests - Workflows
category: GitLab.com
subcategory: Legal
description: "How to perform the processing of Account Deletion and Data Access requests"
controlled_document: true
---

{{< label name="Visibility: Audit" color="#E24329" >}}

## Purpose

This document contains instructions on how to process each type of data subject request, including account deletion and data access. It is split into two stages; **Submission Handling** and **Request Processing**, to be followed in that order. **All requests must be fulfilled within the legally permitted time frame according to the jurisdiction of the data subject.**

## Procedure

### **Stage 1:** Submission Handling

We are only able to process privacy requests if they are submitted through the [Privacy Center](https://privacy.gitlab.com/). If a request is received via any other method, we will close it and direct the user to open a request through the `Make a Privacy Request` button on the Privacy Center. The Privacy Center is powered by Transcend and references to "the system" are references to the Transcend platform where privacy requests are ingested and processed.

When a user submits a request through the Privacy Center, the system automatically creates a new request, *even when no GitLab account exists*. All communication with the user will take place within the privacy request.

<details>
<summary markdown="span">To send a message to the data subject within the privacy request</summary>

- Click on the specific request from the Incoming Request view
- Navigate to the Messages tab
- Click on the blue Email icon on the left
- Select the desired template from the Template dropdown box at the top
- Make any adjustments to the text of the email as necessary
- Click the Send button

</details>

The purpose of this stage is to instruct you on how to close out requests which are not submitted through the Privacy Center

#### Zendesk Submissions

When a request is received through Zendesk as a support ticket, do one the following:

- If the ticket is regarding an **Account Deletion** request, apply the [Support::SaaS::Gitlab.com::Account Deletion Instructions - GitLab.com](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Account%20Deletion%20Instructions-%20GitLab.com.md?ref_type=heads) macro, and mark the ticket as solved.

- If the ticket is regarding a **Data Access** request, apply the [General::Personal Data Access Request Instructions - GitLab.com](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/General/Personal%20Data%20Access%20Request%20Instructions%20-%20GitLab.com.md?ref_type=heads) macro to redirect the user to submit their request using the GitLab [Privacy Center](https://privacy.gitlab.com), and mark the ticket as solved.

- If the ticket is regarding a **Data Portability** request, further clarify with the user. A portability request applies only when the user wants to migrate from GitLab to another platform; in which case GitLab provides instructions for self-service via the Project Import and Export functionality; the destination platform will typically provide the migration documentation a user needs to migrate or port from one platform to another.

- If the ticket is regarding a **Data Export** request, this should be treated as an Access Request. Apply the [General::Personal Data Access Request Instructions - GitLab.com](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/General/Personal%20Data%20Access%20Request%20Instructions%20-%20GitLab.com.md?ref_type=heads) macro to redirect the user to submit their request using the GitLab [Privacy Center](https://privacy.gitlab.com), and mark the ticket as solved.

### **Stage 2:** Request Processing

Find the appropriate workflow below to process privacy requests, based on the request type.

- [Deletion Requests](#deletion-requests)
- [Data Access Requests](#data-access-requests)
- [Data Portability Requests]*(coming soon)*

#### **Deletion Requests**

The following are the types of requests that a user can submit. Click the link for each to jump to the associated workflow for processing that request.

- [Deletion by an individual user](#individual-user-deletion) (deletes the GitLab.com account, Zendesk, Customer Portal and all marketing system personal data)
- [Deletion by an enterprise user](#enterprise-user-deletion) (deletes the GitLab.com account, Zendesk, Customer Portal and all marketing system personal data; subject to Enterprise Account Owner authorization)
- [Customer Portal Account Deletion](#portal-account-deletion) (deletes personal data in customers.gitlab.com only)
- [Deletion for a Deceased User](#deceased-account-owner-deletion) (deletes the GitLab.com account, Zendesk, Customer Portal and all marketing system personal data; must be submitted by an authorized agent)
- [Marketing Deletion](#marketing-deletion) (deletes marketing and sales-related personal data only)

Currently, only deletions by an individual user or an enterprise user are validated with automated checks upon submission. Marketing deletions will automatically be processed. A deletion request for a deceased user will undergo additional verification steps due to legal requirements related to proof of authority to act.

##### **Individual User Deletion**

This workflow applies to deletion requests where the data subject identifies themself as an individual user. The following form field entries should be verified:

- Email address (must exist)
- Username (must exist)
- Username and email must match for the same account
- Account is not an Enterprise User ([Badged](https://docs.gitlab.com/user/enterprise_user/) nor [Support defined Enterprise User](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/support/workflows/gitlab-com_overview.md#enterprise-users)).
- Account [does not have an active subscription](#step-3-check-non-enterprise-user-paid-subscription-status)

After submission, the automated checks will return a risk rating if a GitLab account is found. The risk rating is used to determine whether additional verification is needed to delete the user account. Support Engineers can review the method by which the risk rating is calculated in the [Support Workflow page](https://internal.gitlab.com/handbook/support/workflows/data-subject-requests/) *(internal only)*. If the automated checks do not find a user account, the user will be notified via email message generated from the system.

###### **Step 0:** Check for duplicate requests

Check for existing requests from the user by navigating to the Incoming Request view and searching using the core identifier. Should an existing request of the same type be listed, determine the progress of the original request by clicking into the request itself and reviewing the Status tab. Where an existing request is still moving through the `compiling` or `deleting` stage:

1. Send the `Duplicate Request` message to the user.
1. After sending the message, explicitly cancel the duplicate request by clicking `Cancel Request` in Transcend. Sending the Duplicate Request message alone does not close the request automatically; it must be canceled manually.

![Cancel Request button in Transcend](/images/support/workflows/assets/transcend-cancelrequest.png)

PLEASE NOTE: There are 2 separate tasks assigned to Support Engineers for deletion requests.

`Support Engineer (GitLab Deletion)` serves to determine whether a GitLab user account **can be deleted** and if so to perform the deletion. *Currently the step-by-step actions are also visible in the email delivering the task.*

`Support Engineer (Zendesk/cDot Deletion)` serves to determine whether a Customers Portal account and/or Zendesk account exists for the user. No deletion takes place within this task. However, it serves as a trigger for subsequent tasks to be assigned to console engineers to perform the Customers Portal deletion and to Support Readiness to delete the Zendesk account.

###### **Step 1:** Review Risk Rating, Confirm Account Type and Send Additional Verification Questions

1.1. Is the account an Enterprise User

On the Details tab of the request, if the Data Subject type is `Enterprise User` **AND** the automated checks also indicate that the account is for an Enterprise User, STOP and move directly to [Enterprise User Deletion](#enterprise-user-deletion).
Please note that the [support definition of enterprise users](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/support/workflows/gitlab-com_overview.md#enterprise-users) is also applicable.

1.2 Review Risk Rating

Add a note to the task that `Risk Verification Question message sent, 7-day end date is <date>`.

###### No Response

If the user fails to respond within 7 calendar days, send the `Failed Verification` message, add a note that the user failed to respond to verification and mark the task as an `Exception`.

###### **Step 2:** Blocked or Banned Accounts

If the user account is not blocked or banned, skip this section.

If the user is blocked due to a user deleting their own account, send the `Blocked Account Deletion Request` message, then mark the `Support Engineer (GitLab Deletion)` task as Complete.

Send the `Security Review Requested` message to the data subject, leave the task Open.

If the account is unblocked or unbanned, send the `Security Review Complete` message to the data subject, then follow the rest of the process as normal.

If the account remains blocked or banned, send the `Security Review Denied` message to the data subject, then mark the `Support Engineer (GitLab Deletion)` task as an Exception.

###### **Step 3:** Check non-Enterprise user paid subscription status

1. Verify that the account is **not** an Enterprise user. If it is, follow the [Enterprise user deletion](#enterprise-user-deletion) steps.
1. Search Customers Portal using the email address.
1. If a Customers Portal account does not exist, proceed to Step 4.
1. If a Customers Portal account is found AND there is a `Subscription` badge:
    1. Click the `Zuora Subscriptions` tab.
    1. Note the `End Date` and value of `Auto-renew`. If Auto-renew is yes, then auto renewal is enabled, otherwise it is disabled.
1. If **any** subscription `End Date` is in future:
    1. Add a note in the request's `Details` tab in this format: `Cdot account has active subscription (A-S000xxxx) which expires on 202x-xx-xx auto-renewal is <dis/en>abled - https://customers.gitlab.com/admin/customer/<ID>`
    1. Inform Privacy of the added note in the request via the `help-transcend` channel by tagging Bronwyn Barnett and/or Stephanie Ebbert
    1. Do not perform any deletions of the Gitlab.com account, Zendesk Account or CDot Account. DO NOT proceed to Step 4.
1. If **all** the subscriptions `End Date` are in the past or there is no subscription listed, add a note with a link to the Customers Portal account. Continue to Step 4.

For deletion requests that belong to a non-enterprise user who has an active subscription:

- The Privacy team will pause the account deletion request in Transcend until the subscription end date. 
- The Privacy team will inform the data subject that account deletion (excluding marketing account data) cannot be processed while an active subscription exists. This is because our lawful basis for processing account data is to fulfill contractual obligations, which do not include early termination provisions. 
- Upon subscription termination, including after any auto-renewal periods, the Privacy team will resume the account deletion process. At that point, Support Engineers may proceed with deleting the associated GitLab.com account, Zendesk account, or CDot account as applicable.
- The Privacy team will notify the Billing/Accounts team every 30 days to delete paid non-enterprise user accounts from Zuora following subscription termination.

###### **Step 4:** Proceed with Deletion

Unless the condition in Step 4.1 exists, perform the steps in 4.2 to delete the GitLab account.

4.1 - **Account Already Deleted**

It is possible that the user may have deleted their GitLab account after submitting the request. In such cases it will not be possible to perform further account verification or progress the request. Send the `Account Already Deleted` message to the data subject and mark the `Support Engineer (GitLab Deletion)` task completed.

4.2 - **GitLab Account Deletion**

- Delete any groups that are blocking deletion - such as groups where the user is the sole owner. There is a 30 day delay for [group deletion](https://docs.gitlab.com/user/gitlab_com/#delayed-group-deletion) on GitLab.com, so after deleting the group go to Advanced Settings and select `Delete group immediately` to complete the deletion.
- Initiate user deletion with `Delete user and contributions`. Note that this will not delete projects that the user has joined and the user is not the sole owner of. However it will delete any personal projects the user created.
- Verify the user has been fully deleted, as deletion can be delayed.
- Add or edit an existing .csv to perform the deletion in the GitLab Data Platform, following only the [Deleting Data](https://gitlab.com/gitlab-data/runbooks/-/blob/main/gdpr_deletions/gdpr_deletions.md?ref_type=heads#deleting-data) section of the [runbook](https://gitlab.com/gitlab-data/runbooks/-/blob/main/gdpr_deletions/gdpr_deletions.md?ref_type=heads#deleting-data).
- Upload the latest version of the .csv to the GDPR folder.

4.3 - In the `Support Engineer (GitLab Deletion)` task:

- Mark as `Complete` when all of the user account deletion steps are completed.
- Mark as an `Exception` if the user fails additional verification questions or the account cannot be unblocked or unbanned in order to be deleted. Add a note to the tasks to indicate why it is marked as an exception.

###### **Step 5:** Check Zendesk and Customers Portal for account

- If an account is located in both systems, mark the `Support Engineer (Zendesk/cDot Deletion)` task as Complete.
- If an account is not located in either system, mark the `Support Engineer (Zendesk/cDot Deletion)` task as Not Found.
- If an account is found in only one of the systems, mark the `Support Engineer (Zendesk/cDot Deletion)` task as an Exception and add a note to indicate in which system an account was found.

Support Engineers do not perform the deletion of Zendesk or Customers Portal accounts. After the `Support Engineer (Zendesk/cDot Deletion)` task is resolved, a separate task will be triggered for a Console Engineer to delete the customers portal account and/or a Support Readiness Specialist to delete the Zendesk account.

The system will automatically send the user a message to inform them that their request has been fulfilled once all tasks are completed.

##### Enterprise User Deletion

This workflow applies to deletion requests where the data subject identifies themself as an enterprise user. The following form entries are verified using built-in automated checks:

- Email address (must exist)
- Username (must exist)
- Username and email must match for the same account
- Account is an Enterprise User

Enterprise users can be identified from a domain verification [Enterprise User](https://docs.gitlab.com/user/enterprise_user/) badge, or from fitting the [support definition of enterprise users](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/support/workflows/gitlab-com_overview.md#enterprise-users). GitLab is not the Controller of enterprise users. Therefore, an enterprise user account cannot be deleted without the permission of the Top-level Enterprise Group owner. However, upon submission the automated checks will run and return a risk rating if an account is found and confirmed to be an enterprise user. There may be instances where the request is submitted as an `Enterprise User` data subject type, but the automated checks verify the account is NOT an enterprise user; in which case the request should be treated as though it was submitted by an individual user.

Check whether the enterprise user has an existing Zendesk ticket describing account access or similar issues that can be resolved through reinstatement instead of deletion. Follow the appropriate resolution process for the issue, either on the existing ticket or on the outbound ticket to the group owner in Step 1 below.

If the automated checks do not find a user account, the user will be notified via email message generated from the system.

###### **Step 1:** Obtain Permission

When a deletion request is for an enterprise user, send the `Enterprise User` message to the data subject. The data subject has 7 days to respond back and indicate if they want us to attempt to contact the organization system administrator. Leave a note on the Action Item noting that the `Enterprise User message sent, 7-day end date is <date>`. Leave the request Open.

- If the data subject does not respond within 7 days AND the organization administrator has not provided written instructions to delete the account through a Support Ticket, send the `No Enterprise Admin Permission-Deletion` message and mark the task as an Exception.
- If the data subject asks for us to attempt to contact the organization administrator to obtain permission to delete the account, this should be done utilizing `Step 5. Contact Owner` in [this workflow](/handbook/support/workflows/account_changes/#request-from-an-enterprise-user-that-may-or-may-not-be-part-of-the-group) for contacting the owner of an enterprise user account. Give the administrator 10 calendar days to respond.
  - If permission is granted, add a note to the `Support Engineer (GitLab Deletion)` task with a link to the Support Ticket, then proceed to delete the enterprise user account as detailed in Step 2 below.
  - If permission is not granted, send the `No Enterprise Admin Permission - Deletion` message. Add a note to the work item with a link to the Support Ticket to document no permission was received, then mark the task as an Exception.

###### **Step 2:** Proceed with Deletion

Unless the condition in Step 2.1 exists, perform the steps in 2.2 to delete the Gitlab account:

2.1 - **Account already deleted**

It is possible that the user may have deleted the account after submitting the request, or the enterprise admin was able to delete it. In such cases, it will not be possible to perform further account verificiation. Send the `Account Already Deleted` message, and mark the `Support Engineer (GitLab Deletion)` task complete.

2.2 - **GitLab Account Deletion**

- Delete any groups that are blocking deletion - such as groups where the user is the sole owner. There is a 30 day delay for [group deletion](https://docs.gitlab.com/user/gitlab_com/#delayed-group-deletion) on GitLab.com, so after deleting the group go to Advanced Settings and select `Delete group immediately` to complete the deletion.
- Initiate user deletion with `Delete user and contributions`. Note that this will not delete projects that the user has joined and the user is not the sole owner of. However it will delete any personal projects the user created.
- Verify the user has been fully deleted, as deletion can be delayed.
- Add or edit an existing .csv to perform the deletion in the GitLab Data Platform, following only the [Deleting Data](https://gitlab.com/gitlab-data/runbooks/-/blob/main/gdpr_deletions/gdpr_deletions.md?ref_type=heads#deleting-data) section of the [runbook](https://gitlab.com/gitlab-data/runbooks/-/blob/main/gdpr_deletions/gdpr_deletions.md?ref_type=heads#deleting-data).
- Upload the latest version of the .csv to the GDPR folder.

###### **Step 3:** Check Zendesk and Customers Portal for account

- If an account is located in both systems, mark the `Support Engineer (Zendesk/cDot Deletion)` task as Complete.
- If an account is not located in either system, mark the `Support Engineer (Zendesk/cDot Deletion)` task as Not Found.
- If an account is found in only one of the systems, mark the `Support Engineer (Zendesk/cDot Deletion)` task as an Exception and add a note to indicate in which system an account was found.

Support Engineers do not perform the deletion of Zendesk or Customers Portal accounts. After the `Support Engineer (Zendesk/cDot Deletion)` task is resolved, a separate task will be triggered for a Console Engineer to delete the customers portal account and/or a Support Readiness Specialist to delete the Zendesk account.

The system will automatically send the user a message to inform them that their request has been fulfilled once all tasks are completed.

##### Marketing Deletion

Support Enginers have no tasks in marketing deletion requests. No tasks should be assigned from the system to Support for this type of request.

##### **Portal Account Deletion**

This workflow applies to deletion requests where the data subject identifies themself as the owner of a customers portal account (customers.gitlab.com).

- If a customers portal account is located, mark the `Support Engineer (Zendesk/cDot Deletion)` task as complete.
- If a customers portal account is not located, mark the `Support Engineer (Zendesk/cDot Deletion)` task as not found.

Support Engineers do not perform the deletion of customers portal account. After the `Support Engineer (Zendesk/cDot Deletion)` task is resolved, a separate task will be triggered for a Console Engineer to delete the account.

The system will automatically send the user a message to inform them that their request has been fulfilled once all related tasks are completed.

#### Deceased Account Owner Deletion

This workflow applies to deletion requests submitted by an authorized agent or a [Designated Account Successor](https://docs.gitlab.com/user/profile/account/account_succession/) for an individual user. This workflow does not apply to a deletion request submitted by a Designated Account Manager, as that authority ceases upon the death of the account owner.

The following form entries are verified using built-in automated checks:

- Email address (must exist)
- Username (must exist)
- Username and email must match for the same account
- Account is not an Enterprise Account

Please Note: On the form we ask for the email address in a specific order of preference:

1) Primary or secondary email address on the account (used when the authorized agent has access to the account owner email)
2) Account Success email address (used when the authorized agent was added as a Designated Account Successor)
3) Email of the authorized agent (used when the authorized agent does not know what email was included when they were added as a Designated Account Successor, or if they do not know the email address connected to the account).

After submission, the automated checks will return a risk rating if a GitLab account is found. Support Engineers can review the method by which the risk rating is calculated in the [Support Workflow page](https://internal.gitlab.com/handbook/support/workflows/data-subject-requests/) *(internal only)*, however this risk calculation should only be considered AFTER the authority of the individual submitting the request has been validated by the Privacy Team.

If the automated checks do not find a user account, the requestor will be notified via email message generated from the system once all system tasks are completed.

As additional automation is added to the system, a deletion request submitted by an authorized agent or Designated Account Successor will be placed on hold until the Privacy Team validates that the legal requirements have been met. Once this validation is complete, the request will resume and should follow the [Individual User Deletion](#individual-user-deletion) workflow.

The system will automatically send the requestor a message to inform them that their request has been fulfilled once all tasks are completed.

#### **Data Access Requests**

An access request provides a data subjet with information about the personal data that GitLab processes about them. Only individual users may submit an access request. GitLab is not the Controller of personal data for enterprise users, therefore we are not able to fulfill an access request when the account is designated as an enterprise user. The following form entries are verified using built-in automated checks:

- Email address (must exist)
- Username (must exist)
- Username and email must match for the same account
- Account is not an enterprise user

After submission, the automated checks will return a risk rating if a GitLab account is found. The risk rating is used to determine whether additional verification is needed to delete the user account. Support Engineers can review the method by which the risk rating is calculated in the [Support Workflow page](https://internal.gitlab.com/handbook/support/workflows/data-subject-requests/) (*internal only*). If the automated checks do not find a user account, the user will be notified via email message generated from the system.

There is 1 task assigned to Support Engineers for access requests, however it combines querying and pulling data from two separate systems.

When an account is identified in either system:

- Download the cDot/Zendesk Google sheet template from the [Personal Data Requests shared drive folder](https://drive.google.com/drive/folders/0AA4kcF3prJ6pUk9PVA) and input the field values located in the system(s).
- Ensure you are downloading a blank sheet template and not saving a populated sheet in the shared drive.
- Once populated, upload the sheet to the `Support Engineer (Access)` task and mark as complete.

If an account is not identified in either system, mark the `Support Engineer (Access)` task as not found.

The system will automatically send the user a message to inform them that their request has been fulfilled once all tasks are completed.

#### **Data Export Requests (Right to Portability)**

This workflow applies only for data export requests and NOT for data portability requests. Please note that this data subject request type is not currently available in the [Privacy Center](https://privacy.gitlab.com). It will likely be offered in FY27Q1. However a Support Ticket for a data export or data portability request should utilize this workflow for an individual GitLab account owner (free and paid).

Data Portability applies when the individual wishes to migrate from GitLab to another platform. At this time, GitLab only provides instructions for self-service via the Project Import and Export functionality; the destination platform provides the migration documentation a user will need to migrate or port from one platform to another. GitLab is unable to provide instruction or support for this.

A Data Export request follows a similar workflow as an Access Request, with a narrowed scope. We can only take action on export requests for personal projects, or projects in groups where the user is the *only* member. This workflow cannot be completed if the request indicates the user's country is Cuba, Iran, North Korea, Syria, Russia, Belarus, or the Crimea, Donetsk or Luhanks regions of Ukraine as these are embargoed countries and we are not permitted under Trade Compliance laws to engage with individuals in those locations. Reach out in the [#privacy-team_help](https://gitlab.slack.com/archives/C04357HVCJD) Slack channel if you have any questions.

##### **Step 1:** Verify User region

Verify that the user's region is not one of the embargoed countries listed above. If it is, send the `Embargoed Country` message and mark the task as an exception.

##### **Step 2:** Provide instruction for Self-Service

Send the user the `Project Export Self-Serve` message. The user has 7 days to respond with any issues using the self-service steps. The `Support Engineer (Access)` task should remain open during this time.

- If the user does not respond after 7 days, add a note to the `Support Engineer (Access)` task that no response was received and mark as an exception.
- If the user does seek further assistance AND the request has a medium or high risk rating, send either the `Medium Risk GitLab Account Verification Question` message (ONLY if the user has any private projects) or the `High Risk GitLab Account Verification Question` message to the data subject. Users have 7 calendar days to respond to those questions. The `Support Engineer (Access)` task should remain open during this time.

Please Note:  We cannot deny support to free users for exporting their data if they encounter problems exporting their data. However, all assistance and communication should be done within the privacy request and not through a Zendesk Support Ticket.

##### **Step 3:** Begin the Export

Once the user passes additional verification, where required, proceed to start the process to get the project exports.

- If the user cannot sign in, export only personal namespace projects or projects in groups where the user is the only member using the [UI](https://docs.gitlab.com/user/project/settings/import_export/#export-a-project-and-its-data) or the [API](https://docs.gitlab.com/api/project_import_export/#schedule-an-export).
- If there are errors, follow the [project exports for customers](/handbook/support/workflows/exporting_projects/) workflow. If you need additional troubleshooting help or ideas you can search ZenDesk for examples of past project export tickets from paid customers.
- Upload the project export to the `Support Engineer (Access)` task and send the `Project Export Complete` message and mark the task as complete.

## Exceptions

While processing a request, certain scenarios may arise that necessitate the escalation of the request to the Privacy team. The most common of these scenarios can be found in the [Privacy Escalation Meta Issue](https://gitlab.com/gitlab-com/gdpr-request/-/blob/master/.gitlab/issue_templates/Privacy%20Escalation%20Meta%20Issue.md) template. If a request needs to be escalated to the Privacy team, do the following:

1. Create a new related issue using the [Privacy Escalation Meta Issue](https://gitlab.com/gitlab-com/gdpr-request/-/blob/master/.gitlab/issue_templates/Privacy%20Escalation%20Meta%20Issue.md) template.

If you're ever unsure if a particular scenario requires escalating, reach out to the Privacy team via the `#privacy-team_help` Slack channel.

## Forum User Deletion

A data subject can additionally request that their GitLab forum account be deleted. We can only delete users from the GitLab forum and have no control over the Discourse platform. This request type is currently not available via the Privacy Center however a request may come in through a support ticket. To delete a forum user:

1. Ask the user for their user profile link, their forum username, and email address. The email address they are submitting from must match that of the username and they must have responded at least once.
1. Tag one of the [forum admins](https://forum.gitlab.com/about) in an internal comment on the issue and ask them to delete the user and relevant posts.
1. Comment back that the user has been removed.
