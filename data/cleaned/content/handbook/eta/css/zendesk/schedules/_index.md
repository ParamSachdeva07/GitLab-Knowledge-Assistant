---
title: 'Schedules'
description: 'Documentation on Zendesk schedules'
---

This guide covers how to create, edit, and manage Zendesk schedules at GitLab. Administrators should review the [Administrator tasks](#administrator-tasks) section.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Standard`
- Sync repos
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/schedules)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/schedules)
- `CustSuppOps Zendesk Test Suite Generator` enabled

{{% /alert %}}

## Understanding schedules

### What are schedules

Schedules in Zendesk are like schedules in most other things: windows of time. We use these to determine business hours and various regional working hours. This is a critical component for how Zendesk SLA policies work (as it details the window of time in which an SLA policy runs).

Within Zendesk, these have the ability to use a specific timezone and allow for the setting of holidays, both of which are vital components of how schedules work.

### Using a schedule in Zendesk

Schedules are used to determine business hours for SLA calculations and time-based automations. Common uses include:

- SLA policies (measuring FRT, NRT during business hours only)
- Business hours triggers (actions that fire only during working hours)
- Automations with time conditions

Schedules are typically applied at the ticket level through SLA policies or referenced in trigger/automation conditions.

### Holidays

A holiday in a schedule is a set date where the "timers" do not run.

We do not currently use this feature in Zendesk (as decided by our legal team). The use of this feature will require legal approval as it has an impact on contractual requirements.

### How we manage schedules

While Zendesk offers a full way to manage schedules via the UI, we turn to a more version controlled methodology. This allows for a set review process, the ability to perform rollbacks as needed, etc.

That being the case, we utilize sync repos.

### Current schedules in use

{{% alert title="Note" color="danger" %}}

This should be the single source of truth for the schedules used. Never make changes outside of approved workflows.

Always be cautious of changes. Many of these can have significant downstream impacts.

{{% /alert %}}

- Zendesk Global
  - Business Hours
    - Timezone: Pacific Time (US & Canada)
    - Weekly schedule:
      - Sunday: 1500-2400
      - Monday: 0000-2400
      - Tuesday: 0000-2400
      - Wednesday: 0000-2400
      - Thursday: 0000-2400
      - Friday: 0000-1700
      - Saturday: Closed
    - Holidays: none
  - 24x7 Support
    - Timezone: Pacific Time (US & Canada)
    - Weekly schedule:
      - Sunday: 0000-2400
      - Monday: 0000-2400
      - Tuesday: 0000-2400
      - Wednesday: 0000-2400
      - Thursday: 0000-2400
      - Friday: 0000-2400
      - Saturday: 0000-2400
    - Holidays: none
  - AMER
    - Timezone: Pacific Time (US & Canada)
    - Weekly schedule:
      - Sunday: Closed
      - Monday: 0500-1700
      - Tuesday: 0500-1700
      - Wednesday: 0500-1700
      - Thursday: 0500-1700
      - Friday: 0500-1700
      - Saturday: Closed
    - Holidays: none
  - APAC
    - Timezone: Brisbane
    - Weekly schedule:
      - Sunday: Closed
      - Monday: 0900-2100
      - Tuesday: 0900-2100
      - Wednesday: 0900-2100
      - Thursday: 0900-2100
      - Friday: 0900-2100
      - Saturday: Closed
    - Holidays: none
  - EMEA
    - Timezone: Amsterdam
    - Weekly schedule:
      - Sunday: Closed
      - Monday: 0800-1800
      - Tuesday: 0800-1800
      - Wednesday: 0800-1800
      - Thursday: 0800-1800
      - Friday: 0800-1800
      - Saturday: Closed
    - Holidays: none
- Zendesk US Government
  - Standard Business Hours
    - Timezone: Pacific Time (US & Canada)
    - Weekly schedule:
      - Sunday: Closed
      - Monday: 0500-1700
      - Tuesday: 0500-1700
      - Wednesday: 0500-1700
      - Thursday: 0500-1700
      - Friday: 0500-1700
      - Saturday: Closed
    - Holidays: none
  - 24x7 Business Hours
    - Timezone: Pacific Time (US & Canada)
    - Weekly schedule:
      - Sunday: 0000-2400
      - Monday: 0000-2400
      - Tuesday: 0000-2400
      - Wednesday: 0000-2400
      - Thursday: 0000-2400
      - Friday: 0000-2400
      - Saturday: 0000-2400
    - Holidays: none

## Creating schedules as a non-admin

For the creation of a schedule, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Editing schedules as a non-admin

For the modification of a schedule, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Deleting schedules as a non-admin

For the deletion of a schedule, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Administrator tasks

{{% alert title="Note" color="primary" %}}

- All sections in this section require `Administrator` level access to Zendesk.

{{% /alert %}}

### Viewing schedules in Zendesk

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Business rules > Schedules`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/rules/schedules)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/rules/schedules)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/rules/schedules)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/rules/schedules)

You can click on the schedule's name if you need to see the actual schedule's timeslots or holiday settings.

### Creating a schedule

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- Remember just creating a schedule doesn't mean it will be used.

{{% /alert %}}

for the creation of a schedule, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself. A starting template you can use would be:

```yaml
---
name: 'Schedule name here'
previous_name: 'Schedule name here'
time_zone: 'Timezone to use here'
sunday: []
monday:
- START-END
tuesday:
- START-END
wednesday:
- START-END
thursday:
- START-END
friday:
- START-END
saturday: []
```

For the `time_zone` attribute, it should be one of the approved time zones we use:

- Zendesk Global
  - For `AMER` schedules: `Pacific Time (US & Canada)`
  - For `APAC` schedules: `Brisbane`
  - For `EMEA` schedules: `Amsterdam`
  - For anything else: `Pacific Time (US & Canada)`
- Zendesk US Government
  - `Pacific Time (US & Canada)`

For the array items under the `sunday`, `monday`, ..., `saturday` attributes, it should be an array of time slots to use (written in 24 hour code format). For the very end of the day (midnight), use `2400`. As an example, if you wanted to have a schedule apply the timeslots of 0700 to 1200 and 1500-2300 on Mondays, you would do:

```yaml
monday:
- 0700-1200
- 1500-2300
```

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

### Editing a schedule

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can have many severe downstream impacts on tickets and their SLAs. Exercise caution when doing this.

{{% /alert %}}

To edit a schedule, you will need to create a MR in the sync repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR. When the next deployment occurs, it will be synced to Zendesk.

#### Changing the name of a schedule

If you need to change the name of a schedule, copy the current value into the `previous_name` attribute and then change the `name` attribute. This allows the sync to still locate the SLA policy in question to update.

### Deleting a schedule

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).
- This can have many severe downstream impacts on tickets and their SLAs. Exercise caution when doing this.

{{% /alert %}}

As the sync repos do not perform deletions, you will have to do 2 actions to delete a schedule.

First, you must delete the corresponding file from the sync repo. After a peer reviews and approves your MR, you can merge the MR.

After that is done, you then must delete it from Zendesk itself.

To delete a schedule in Zendesk:

1. Navigate to the admin dashboard for the Zendesk instance
   - [Zendesk Global (production)](https://gitlab.zendesk.com/admin/home)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/home)
   - [Zendesk US Government (production)](https://gitlab-federal-support.zendesk.com/admin/home)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/home)
1. Go to `Objects and rules > Business rules > Schedules`
   - [Zendesk Global](https://gitlab.zendesk.com/admin/objects-rules/rules/schedules)
   - [Zendesk Global (sandbox)](https://gitlab1707170878.zendesk.com/admin/objects-rules/rules/schedules)
   - [Zendesk US Government](https://gitlab-federal-support.zendesk.com/admin/objects-rules/rules/schedules)
   - [Zendesk US Government (sandbox)](https://gitlabfederalsupport1585318082.zendesk.com/admin/objects-rules/rules/schedules)
1. Click the three vertical dots to the right of the schedule's name
1. Click `Delete`
1. Click `Delete` to confirm the deletion

### Performing an exception deployment

To perform an exception deployment for schedules, navigate to the schedules sync project in question, go to the scheduled pipelines page, and click the play button for the sync item. This will trigger a sync job for the schedules.

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.

### Not seeing schedule changes after a merge

As schedules follow the `Standard` deployment type, they would only be deployed during a normal deployment cycle (or when an exception deployment has been done)
