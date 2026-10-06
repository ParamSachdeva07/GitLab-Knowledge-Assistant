---
title: Working with U.S. Government Support tickets
category: Handling tickets
description: "Support Engineering workflow detailing how to work on U.S. Government Tickets"
---

U.S. Government Support uses a weighted round-robin workflow for new ticket assignment in the U.S. Government Zendesk instance.

This page is the handbook source of truth for day-to-day work on U.S. Government Support tickets, including ticket assignment, follow-up expectations, confidentiality requirements, and post-emergency ticket handling.

For on-call coverage, paging flow, and emergency response expectations, see [How to Perform U.S. Government On-Call Duties](/handbook/support/workflows/usgovernment_oncall/).

## Access limited to U.S. Citizens

Only our U.S. Citizen Support Engineers have access to the [U.S. Government Zendesk Instance](/handbook/eta/css/zendesk/#zendesk-us-government).

If you are a U.S. Citizen and would like to get access and contribute, you can open an [Access Request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=Individual_Bulk_Access_Request) for either a [light agent](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=Individual_Bulk_Access_Request) or [full agent](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=Individual_Bulk_Access_Request) account (limited to Support and Security team members).

## Communication Guidelines

Issues relating to tickets received in the U.S. Government Zendesk instance may be discussed outside of the U.S. Government instance with a few key caveats.

Identifying information that includes system names, organization names, customer names, specific infrastructure details (IP addresses, hostnames, and similar details), and log files should be limited to internal tickets. Specifics about the technical problem are generally acceptable to discuss in chat, issues, and other internal spaces, but use discretion when communicating log snippets, screenshots, and other data to ensure no identifying information is disclosed.

When in doubt, ask a manager or the customer's CSM whether the information is acceptable to be communicated to non-U.S. citizens.

For any assistance with log review or confidential information within a ticket, it is recommended to directly reach out to other engineers with access to the U.S. Government instance within Zendesk using an internal comment to avoid accidental disclosure.

Government tickets can be linked publicly, such as in an issue or merge request, as the link itself does not reveal any information. Avoid naming the link with any identifiable information. For example:

`[U.S. Government Internal Ticket](<ticket_link>)`

When pairing over video chat, be sure you only pair with engineers that have access to the U.S. Government instance. Avoid screen sharing content from the U.S. Government Support instance, logs, or other information that is required to be kept confidential.

When providing links to documentation, it is possible an organization's mail server may strip embedded links before delivering the ticket update to the receiver. To continue providing documentation to customers, consider using an identifier in the reply body, then "footnotes" toward the end of the ticket. For example:

```text
This is the ticket reply body where we are talking docs Title of documentation Page(1). Here's some more documentation that's relevant, Title of documentation page (2).

---

1. Documentation Link
2. Documentation Link
---
```

### How to reference customer information securely in chat

You may leverage links to records in controlled-access systems such as Salesforce or Zendesk in order to securely provide information. Note that if you have Slack link expansion enabled for Salesforce records, you should immediately remove the expansion after making your comment.

Examples:

- "This user [https://gitlab-federal-support.zendesk.com/users/398443026291/](https://gitlab-federal-support.zendesk.com/users/398443026291/) is struggling with Geo setup..."

- "The person who submitted the case that got bounced back is a member of this organization: [https://gitlab.my.salesforce.com/0014M00001hHHKF](https://gitlab.my.salesforce.com/0014M00001hHHKF)"

The use of an acronym to discuss an organization is not permitted in the `#spt_us-government` channel to prevent disclosure of sensitive information.

### Checking for access

When discussing cases or issues with others in GitLab, it may be difficult to confirm whether they meet the [access requirements](#access-limited-to-us-citizens) to receive confidential or sensitive information via chat, screen share, or call.

The single source of truth is whether or not that person has a U.S. Government Zendesk account, either as a full or light agent. The individuals with access have been confirmed by People Operations to be allowed access to this information.

The Support Ops team has built a tool for team members to check whether a person has access to U.S. Government Zendesk. The tool can be accessed by GitLab team members via [this link](https://gitlab-com.gitlab.io/support/support-ops/zendesk-us-federal-project/). It updates weekly on Sundays at 00:00 UTC.

If you need verification for someone who was added more recently, ask a U.S. Government Support Manager or Support Ops Manager to validate. If you are not able to find a person's name in this tool, the user should be considered ineligible to access the instance and you should follow the [Communication Guidelines](#communication-guidelines).

## Working tickets in the U.S. Government Zendesk instance

U.S. Government Support has a number of engineers with verified U.S. citizenship that have a 100% focus on addressing new and existing cases in the U.S. Government Support Portal. The agents focused on this instance should distribute effort and work new cases from the [Support view](https://gitlab-federal-support.zendesk.com/agent/filters/360196736831).

When replying to a new case, the agent making the public comment should also assign the case to themselves.

Those without a 50% or higher focus on U.S. Government but who do have access to the instance are still encouraged to participate through pairing sessions, joining customer calls, and assisting with gaps in knowledge where possible. Non-fully-focused global engineers are not encouraged to assign new cases to themselves.

Customers will occasionally request to add a co-worker to a Zendesk case. Because [CCs are disabled](https://support.gitlab.com/hc/en-us/articles/11626578409756-Operational-Guidelines-for-U-S-Government-Support#ccs-are-disabled) on the U.S. Government Zendesk instance, we offer instead [Shared Organizations](https://support.gitlab.com/hc/en-us/articles/11626528150172-Managing-Support-Contacts#shared-organizations).

### Following up

The U.S. Government team has implemented an automated follow-up system that checks in with the submitter of a case when the case has been in a `pending` state for 7 days. After 14 consecutive days in a pending state with no replies from the submitter, the case will automatically move to a `solved` state.

#### Extending the follow-up time

There can be situations in which a task may take longer than 7 days for the customer to make changes and provide feedback.

If there has been an agreed-upon day in the future where the customer has said they will update us, an agent may opt to use the `Support::Block Automatic Reopen` macro. This macro adds the `blocked_by` tag and creates an internal comment where the agent must fill in the details indicating why the case should remain pending.

The `blocked_by` tag must be manually removed by an agent when the agreed-upon date has been reached in order to resume the standard pending-to-follow-up workflow.

Some best-practice suggestions for using the macro are below:

- Set a [task reminder](/handbook/eta/css/zendesk/apps/us-government#zendesk-super-app) for the date that we should hear back from the user

- Regularly review pending cases to ensure we are receiving follow-up by the date promised

- Put the relevant issue or case number in the blocked-by reason so that others may be aware and follow up on your behalf

### Ticket assignment via round-robin

During core business hours, tickets are assigned as they are created based on a round-robin tool built by Support Ops. This tool creates a list of available Support Engineers on shift, omitting those who are on PTO per the time off calendar. It then checks each engineer's overall case weighting and assigns the new case to the engineer with the lowest overall weighting.

### Consolidating assignment for org tickets created at the same time

In some cases, a single requester or organization may create multiple tickets within a short period that get round-robin assigned to multiple Support Engineers. Splitting the work in this way can lead to duplicated work as multiple engineers ask for similar files and try to build the same context around the environment and any recent changes.

To avoid this, a method for grouping these tickets under a single assignee goes as follows:

1. A customer creates more than one ticket in a day or two, and those tickets are round-robin assigned.

2. The Support Engineers who were assigned tickets from this customer discuss the tickets in Slack or in a crush session to determine if they are probably about the same environment.

3. One of the Support Engineers agrees to take assignment of all this customer's tickets created during this period and may also take on newly created related tickets shortly after.

4. That engineer marks themselves as overburdened to be taken out of the round-robin until they decide they are ready to take on new tickets again.

5. If new tickets come in from the same customer shortly after an engineer has taken ownership of other tickets, the new tickets should be reviewed to determine if they fit the same environment. If they do, the engineer should take ownership of them as well.

If no one wants to take the tickets, keep the tickets assigned to the people to whom the round-robin first assigned them.

### Getting help with a ticket

Getting help with a U.S. Government ticket can be tricky since some information must be kept confidential. However, there are many times when a non-U.S. Government engineer may be the subject matter expert needed to help efficiently resolve a U.S. Government Support case.

It is encouraged to ask questions in `#support_self-managed` and other Slack channels, provided the [Communication Guidelines](#communication-guidelines) are followed.

If you need a manager's help with a ticket, keep in mind that only U.S. Citizens have access to our U.S. Government instance, which means some of our managers cannot help with ticket-level detail. If you are a U.S. Citizen working in U.S. Government and your manager is not, feel free to reach out to a different manager if you are unable to address an issue without sharing confidential information.

#### Discussion issues from tickets

In order to better facilitate asynchronous collaboration on tickets within the U.S. Government ticket system, we have a macro that allows U.S. Government Support Engineers to trigger the creation of a confidential GitLab issue connected with the ticket. This issue remains open for the duration of the ticket and can provide a way for U.S. Government Support Engineers to relay information to collaborators.

It is important to never include customer-specific information inside of these issues. Even though they are confidential, they are still visible to people who do not have access to the U.S. Government ticket system.

To trigger the creation of one of these issues, select the `General::Create discussion issue` macro from the macros menu, then submit the ticket. The Support Ops bot will create an issue and link to it in an internal note.

At first, this issue will contain very little information. The title will include the ticket number and the body will contain a link to the ticket plus empty sections, marked with headers, where you can provide information as you have it. All of these sections are optional.

Edit the issue to include as much information about the ticket as possible without breaching our confidentiality requirements, then share the link to the issue with collaborators or mention others to engage them through GitLab's To-Do system. Finally, set yourself as the assignee.

Once the ticket has been marked as solved, the Support Ops bot will automatically close the issue.

### U.S. Government Support discovery calls

Sometimes it can be difficult for customers to capture and convey all of the necessary information for troubleshooting the GitLab stack on their own. When filing a technical support case in the U.S. Government portal, a customer may indicate they would like to hold a discovery session with the case assignee to demonstrate their issue, collect necessary logs or screenshots, and then return to working asynchronously in the support case.

When a customer selects the checkbox to indicate they would like a session, there will be an internal note at the beginning of the case history indicating they have made the request. The assignee should review all the provided information and select the `General::Discovery call response` macro to begin scheduling the session. The assignee will need to fill in the single-use Calendly link and request any additional information from the user that may be relevant.

There is a Calendly-managed event template called `GitLab US Government Customer Discovery Call` and it can be assigned to an agent by asking a Calendly admin. This event type is a 30-minute session with 1 day lead time.

It is recommended to continue working the case asynchronously while awaiting the discovery call session.

When the scheduled session occurs, the agent should set the expectation that we will ask the customer to demonstrate the issue and then work with them to create a collection of artifacts that will be uploaded to the case at a later time.

A short post-call synopsis reminding the customer of what artifacts were collected and providing a technical description of what was observed is recommended to ensure both parties have the same understanding of next steps.

## Emergency ticket handling

For on-call shift coverage, paging behavior, and emergency intake expectations, see [How to Perform U.S. Government On-Call Duties](/handbook/support/workflows/usgovernment_oncall/).

For general emergency handling patterns used by Support, see [How to Perform Customer Emergencies Duties](/handbook/support/workflows/customer_emergencies_workflows/).

This section documents how U.S. Government emergency tickets should be handled in Zendesk once the emergency has been accepted and worked.

### During an active emergency

Emergency tickets should be treated as a distinct workflow from standard support work.

While the emergency is active:

- The first responding Support Engineer is automatically assigned the ticket

- The emergency ticket should remain the active coordination record for the emergency event

- The temporary emergency weighting should remain in place only for the period where the customer is actively in an emergency condition

### After an emergency is resolved

Once the emergency condition is resolved, the ticket should no longer remain open as an active emergency.

The goal is to keep the emergency workflow and its temporary ticket weighting limited to the active emergency window.

#### Standard resolution paths

Use one of the following standard paths after the emergency is resolved:

1. If a related non-emergency ticket already exists, merge the emergency ticket into that ticket and continue any follow-up work there.

2. If no related non-emergency ticket exists, solve or close the emergency ticket.

Any post-emergency follow-up work should happen in a non-emergency ticket.

If needed, leave an internal note linking the emergency ticket and the follow-up ticket so the timeline remains easy to follow.

#### Discouraged exception: continuing the same ticket as a non-emergency

In rare cases, it may make sense to continue working from the same ticket after the emergency has been resolved.

If that happens, the Support Engineer must manually remove the emergency weighting so the ticket no longer behaves like an active emergency in workload balancing. In most cases, this means reducing the ticket weight from `5` to `1`, using judgment based on the amount of remaining follow-up work.

This path is discouraged and should only be used when moving the follow-up to a separate non-emergency ticket would create unnecessary confusion for the customer or the team.

When using this exception path, leave an internal note explaining why the ticket remained open and that the weight was manually adjusted.

#### Why this matters

Emergency tickets carry a ticket weight of `5` for workload balancing.

That elevated weight acts as a temporary hold on new case assignments while the engineer is actively managing the emergency. Closing or merging the ticket after the emergency is resolved keeps the weight-5 bonus isolated to the active emergency window and prevents long-term imbalance in the U.S. Government assignment system.

## GitLab Dedicated for Government

### High-level notes

1. Don't panic.

2. In any GitLab Dedicated ticket, determine whether the issue is a GitLab application problem or an infrastructure issue. Use the [logs](/handbook/support/workflows/dedicated_logs/) and [observability metrics](/handbook/support/workflows/dedicated_instance_health) to guide you.

3. Logs and metrics are in-boundary and require VPN access. If you have questions or problems, ask in `#g_dedicated-us-pubsec`. Instructions for setup are [here](https://gitlab.com/gitlab-com/gl-infra/us-public-sector/documentation/-/blob/main/runbooks/remote-access-vpn.md?ref_type=heads).

#### Getting help

|   |   |
|---|---|
|What|Useful for|
|[GitLab Dedicated Overview](/handbook/support/workflows/dedicated/)|A good place to start for basic questions|
|[Troubleshooting Tables](/handbook/support/workflows/saas_sm_cheatsheet/)|Understanding what is different about GitLab Dedicated|
|Open an [RFH](/handbook/support/workflows/how-to-get-help/#how-to-formally-request-help-from-the-gitlab-development-team) on `CompSecGov`|Requesting [configuration changes](/handbook/support/workflows/dedicated/#configuration-changes) on behalf of customers, or getting help from SREs on things that are not incidents|
|[#support_gitlab-dedicated](https://gitlab.enterprise.slack.com/archives/C058LM1RL3V) on Slack|General questions for Support folks focused on GitLab Dedicated, commercial or government|

### Requests for Help

Requests for Help live in-boundary on [CompSecGov](https://compsecgov.gitlab-dedicated.us/gitlab-dedicated-us-public-sector/customer-support). Access to CompSecGov comes through [FedRAMP Okta](https://gitlabus.okta.com). If you need access and do not have it, contact Rommel or Kasey to get the process started.

In any GitLab Dedicated ticket, determine whether the issue is a GitLab application problem or an infrastructure issue. Infrastructure-issue RFHs follow the CompSecGov procedure and application-issue RFHs follow the [typical procedure](/handbook/support/workflows/how-to-get-help/#how-to-formally-request-help-from-the-gitlab-development-team).

To open an RFH on CompSecGov, go to the `Customer Support` group and open a new issue using the RFH issue template.

#### Finding a customer's maintenance hours

Maintenance hours for US Government customers are currently captured in the
[Switchboard PubSec repository](https://gitlab.com/gitlab-com/gl-infra/us-public-sector/switchboard_pubsec/-/tree/main/customers?ref_type=heads).

Once tenants have been migrated to Switchboard, this information will be available there instead. There is no ETA for this migration at this time.

#### Handling emergencies

Emergencies from [GitLab Dedicated for Government](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated_for_government/) customers come through the [U.S. Government Emergency support](https://about.gitlab.com/support/us-government-support/#us-government-emergency-support) rotation.

The Global Support Team's workflow for [Handling GitLab Dedicated emergencies](/handbook/support/workflows/dedicated/#handling-gitlab-dedicated-emergencies) is your guide.

Consider using the `@spt_focus-dedicated` Slack handle to ping members of the GitLab Support team who focus on GitLab Dedicated for additional assistance.

The [GitLab Dedicated U.S. PubSec On-call runbook](https://gitlab.com/gitlab-com/gl-infra/us-public-sector/documentation/-/blob/main/runbooks/on-call.md) is the SSOT and the U.S. Government Support team should bookmark and reference it.

### Getting access

If you do not have access to [FedRAMP Okta](https://gitlabus.okta.com/) or [CompSecGov](https://compsecgov.gitlab-dedicated.us/), follow this [Training Module](https://gitlab.com/gitlab-com/support/support-training/-/blob/main/.gitlab/issue_templates/GitLab%20Dedicated%20for%20Government.md) to work through getting access.

### Troubleshooting

The FedRAMP Okta instance will lock accounts after 90 days of inactivity. To unlock your account, you need an [Access Request](https://compsecgov.gitlab-dedicated.us/corporate-security/access-management/-/issues) opened on CompSecGov, where you have been locked out.

If you need help with this process, post in `#g_dedicated-us-pubsec`
