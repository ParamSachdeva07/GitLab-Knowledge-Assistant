---
title: 'SLA Policies'
description: 'Operations documentation page for Zendesk SLA Policies'
---

This guide covers how to create, edit, and manage Zendesk SLA policies at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/sla-policies)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/sla-policies)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}
{{% alert title="Zendesk calls them service level agreements, we do not" color="warning" %}}

What appears here is all titled service level agreements, or SLAs, but many of these are internal service level objectives, or SLOs, instead. They are titled as service level agreement, or SLA, because that is what Zendesk calls the setting. Nothing detailed herein is an actual, legal service level agreement.

{{% /alert %}}

## Understanding SLA policies

### What are SLA policies

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-SLA-policies):

> A Service Level Agreement, or SLA, is an agreed upon measure of the response and resolution times that your support team delivers to your customers. Providing support based on service levels ensures that you’re delivering measured and predictable service. It also provides greater visibility when problems arise.

### Metric policies involved

| Policy name | API name | What it means |
|-------------|----------|---------------|
| First reply time | `first_reply_time` | The time between the first customer comment and the first public comment from an agent, displayed in minutes. |
| Next reply time | `next_reply_time` | The time between the oldest, unanswered customer comment and the next public comment from an agent, displayed in minutes. |
| Pausable update | `pausable_update_time` | The time between each public comment from agents, displayed in minutes. The SLA will pause on Pending. |
| Periodic update | `periodic_update_time` | The time between each public comment from agents, displayed in minutes. |
| Agent work time | `agent_work_time` | The combined total time spent in the New and Open statuses. The SLA will pause on Pending and On-hold. |
| Requester wait time | `requester_wait_time` | This is the time a ticket spends in the New, Open, and On-hold statuses. |
| Total resolution time | `total_resolution_time` | This is the maximum time it should take to resolve a ticket, including all statuses. |

Of these, the ones we use most commonly are First reply time (FRT) and Next reply time (NRT).

### SLA policies use filter logic

SLA policies use filter logic:

- `all`: ALL of the conditions in the array must be true (AND logic)
- `any`: AT LEAST ONE condition in the array must be true (OR logic)
- You can use either only one set or both sets (but there must be at least one set used)

### How we manage SLA policies

While Zendesk offers a full way to manage SLA policies via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize the Zendesk internal forms, sync repos, and managed content repos.

#### Human readable replacements

{{% alert title="Note" color="primary" %}}

- Only applies to `administrators` creating/editing SLA policies via YAML files

{{% /alert %}}

Currently, the sync repo can perform replacements of various items from a human readable item to the "Zendesk" equivalent item. This includes:

| Human readable item | Zendesk field item | Filter location | Notes |
|---------------------|--------------------|-----------------|-------|
| `'Brand: XXX'` | `brand_id` | `value` | Replace `XXX` with the `name` of the brand |
| `'Field: XXX'` | `custom_fields_xxx` | `field` | Replace `XXX` with the `title` of the ticket field |
| `'Group: XXX'` | `group_id` | `value` | Replace `XXX` with the `name` of the group |
| `'XXX'` | `role` | `value` | Replace `XXX` with the `name` of the role type OR the email address of the requester |
| `'Form: XXX'` | `ticket_form_id` | `value` | Replace `XXX` with the `name` of the ticket form |
| `'Schedule: XXX'` | `set_schedule` | `value` | Replace `XXX` with the `name` of the schedule |
| `'Schedule: XXX'` | `schedule_id` | `value` | Replace `XXX` with the `name` of the schedule |
| `'XXX'` | `organization_id` | `value` | Replace `XXX` with the `salesforce_id` attribute of the organization |
| `'XXX'` | `assignee_id` | `value` | Replace `XXX` with the email address of the agent |
| `'XXX'` | `satisfaction_reason_code` | `value` | Replace `XXX` with the `name` of the satisfaction reason |
| `'XXX'` | `via_id` | `value` | Replace `XXX` with the `name` of the via type |
| `'XXX'` | `requester_role` | `value` | Replace `XXX` with the `name` of the requester role type |

As an example, if you needed a filter to check if the form of a ticket is not the `SaaS` form, you would do:

```yaml
- field: 'ticket_form_id'
  operator: 'is_not'
  value: 'Form: SaaS'
```

## Creating SLA policies as a non-admin

For the creation of an SLA policy, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing SLA policies as a non-admin

For the modification of an SLA policy, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting SLA policies as a non-admin

For the deletion of an SLA policy, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing SLA policies in Zendesk

To view the list of SLA policies in Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Business rules > Service level agreements`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/rules/slas)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/rules/slas)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/rules/slas)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/rules/slas)

You can click on the SLA policy's name if you need to see more information about the SLA policy.

### A note about positioning

The SLA policy applied on a ticket is determined by the first _matching_ SLA policy (via the filters), read from top to bottom (where order is dictated by the position value). As such, you need to be very careful on positioning if you have multiple SLA policies that could filter to the same ticket(s).

### Creating an SLA policy

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can have many severe downstream impacts on tickets and metrics. Exercise caution when doing this.

{{% /alert %}}

For the creation of an SLA policy, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
title: 'Your title here'
previous_title: 'Your title here'
description: 'Your description here'
position: 1 # Integer representing SLA policy position
filter:
  all:
  - field: 'the_action_to_perform'
    operator: 'the_operator_to_use'
    value: 'the_value_to_use'
  any:
  - field: 'the_action_to_perform'
    operator: 'the_operator_to_use'
    value: 'the_value_to_use'
policy_metrics:
- priority: 'low'
  metric: 'metric_policy_to_use'
  target: 123 # Number of minutes
  business_hours: true # Set to true to use the ticket's schedule, set to false to use 24/7
- priority: 'normal'
  metric: 'metric_policy_to_use'
  target: 123 # Number of minutes
  business_hours: true # Set to true to use the ticket's schedule, set to false to use 24/7
- priority: 'high'
  metric: 'metric_policy_to_use'
  target: 123 # Number of minutes
  business_hours: true # Set to true to use the ticket's schedule, set to false to use 24/7
- priority: 'urgent'
  metric: 'metric_policy_to_use'
  target: 123 # Number of minutes
  business_hours: true # Set to true to use the ticket's schedule, set to false to use 24/7
```

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing an SLA policy

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can have many severe downstream impacts on tickets and metrics. Exercise caution when doing this.

{{% /alert %}}

To edit an SLA policy, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the title of an SLA policy

If you need to change the title of an SLA policy, copy the current value into the `previous_title` attribute and then change the `title` attribute. This allows the sync to still locate the SLA policy in question to update.

### Deleting an SLA policy

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can have many severe downstream impacts on tickets and metrics. Exercise caution when doing this.

{{% /alert %}}

As the sync repos do not perform deletions, you will have to do 2 actions to delete an SLA policy.

First, you must delete the corresponding file from the sync repo. After a peer reviews and approves your MR, you can merge the MR.

After that is done, you then must delete it from Zendesk itself.

To delete an SLA policy from Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Business rules > Service level agreements`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/rules/slas)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/rules/slas)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/rules/slas)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/rules/slas)
1. Click the three vertical dots to the right of the SLA policy you wish to delete
1. Click `Delete`
1. Click `Continue deletion` to confirm the deletion

### Performing an exception deployment

To perform an exception deployment for SLA policies, navigate to the SLA policies sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the SLA policies.

## Common issues and troubleshooting

### Not seeing SLA policy changes after a merge

As SLA policies follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)

### Not seeing an update to the SLA policy on a ticket

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/5600997516058-About-SLA-policies-and-how-they-work#topic_pz5_zzv_rr):

> When a ticket is created or updated, it runs through all the triggers set up in your Zendesk instance. After the triggers have been applied, that ticket goes through the SLA system.

This means for the SLA policy on a ticket to update, the ticket itself must update. As such, you (or the customer) will need to make an update on the ticket to see the SLA policy on the ticket change.

### The timer on a ticket did not change after an SLA policy updated

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/5600997516058-About-SLA-policies-and-how-they-work#topic_pz5_zzv_rr):

> If you’ve created a new, more restrictive policy since that ticket was last updated, it’s possible that the ticket will receive that new policy that didn’t exist before. Or, alternatively, you may have updated the targets for the policy that’s already been applied. In both of those cases, the ticket will receive the new information after a ticket update that affects the SLA, such as a priority or schedule change.

That being the case, you might need to change the priority of the ticket, and then change it back to see the timer update.

### The breach event did not update when the SLA policy's target did

As per [Zendesk](https://support.zendesk.com/hc/en-us/articles/5600997516058-About-SLA-policies-and-how-they-work#topic_pz5_zzv_rr):

> If you apply or change an SLA target that is already breached, the breach will be recorded at the time of the update. SLAs do not back-date breach events.

### The SLA timer is gone from my ticket

SLA timers no longer appear on tickets in one of two common cases:

- There is no SLA policy on a ticket
- The last public comment on the ticket was made by an agent
- The ticket has a status of solved

If the ticket has a status of solved, you can change the status to any other one to restore the SLA timer to the ticket (if one should be appearing).

If the last public comment on the ticket was made by an agent, an end-user will need to make a comment on the ticket before an SLA timer will appear on the ticket.

If neither of those cases are occurring, it is possible there is not an SLA policy on the ticket. You should reach out to the Customer Support Systems team via Slack to have that looked into further.
