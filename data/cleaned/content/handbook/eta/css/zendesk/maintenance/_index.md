---
title: 'Maintenance'
description: 'Documentation on Zendesk maintenance'
---

To maintain healthy environments, there are several maintenance tasks that must be done. While the aim is to always automate these, some cannot be automated and must be done manually from time to time.

This guide covers various maintenance tasks that are done for our Zendesk instances at GitLab.

## Automated maintenance tasks

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Projects:
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/maintenance-tasks)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/maintenance-tasks)

{{% /alert %}}

### Fix bad task ticket

<sup>Runs every hour at the 30 min mark</sup>

This locates `Task` type tickets that have a `Due Date` value set before the current time. Any tickets found in this state have their `Due Date` value removed and are set to the type of `Question`.

### Fix false expired tags in orgs

{{% alert title="Note" color="info" %}}

- Only applies to Zendesk Global environments

{{% /alert %}}

<sup>Runs every hour at the 30 min mark</sup>

This locates organization's containing the `expired` tag and a `support_level` value that is not `expired`. For these organizations, we need to remove the false `expired` tag. The script will do so after checking the following:

- Removing the `expired` tag does not remove all `support_level` tags on the organization
- Removing the `expired` tag would yield an actual update

### Permanently delete deleted users

<sup>Runs twice daily at 0045 and 1245</sup>

Deleting a user removes them from the Zendesk workspace, however it does not actually _fully_ remove the user. As such, we need to routinely remove these deleted users from Zendesk.

### Close base GitLab tickets

{{% alert title="Note" color="info" %}}

- Only applies to Zendesk Global environments

{{% /alert %}}

<sup>Runs every hour at the 30 min mark</sup>

This locates tickets under the organization `GitLab` not in approved forms and closes them.

## Manual maintenance tasks

### Enable upcoming version deprecation warning in the themes

To warn customers of a major version being unsupported soon, we display a warning on the theme when they enter their GitLab version on various forms/fields.

To modify this, you will need to create a MR in the sync repo doing the following:

- Update the `data/theme/script.js` file
  - You are wanting to make three changes here:
    1. Update the version number and date in the `upcoming_unsupported_version_message` function
    1. Ensure the following `if` block is uncommented:

       ```javascript
       if ($(this).val().split('.')[0] == xx) {
          $('#gitlab_version_checker_upcoming').show();
        } else {
          $('#gitlab_version_checker_upcoming').hide();
        }
       ```

       - Where `xx` is the previously used version number
    1. Ensure the previously used version number in the `if` block (from point 2) is updated
- Update the version in the `data/theme/manifest.json` file

After a peer reviews and approves your MR, you can merge the MR (which will ensure the changes go into effect on the next deployment date).

This is done in a way to ensure it is enabled on the theme for at least a month prior to the GitLab major release. Refer to [GitLab releases](/handbook/engineering/releases/monthly-releases/#monthly-release-schedule) for more info on upcoming releases. So if the release date is 2025-05-15, you would want to ensure it is done in time for the 2025-04-01 deployment.

### Disable upcoming version deprecation warning in the themes

As the version from the message is now unsupported, we need to remove the warning. To do this, you will need to create a MR in the sync repo doing the following:

- Update the `data/theme/script.js` file
  - Ensure the following `if` block is commented out:

    ```javascript
    if ($(this).val().split('.')[0] == xx) {
       $('#gitlab_version_checker_upcoming').show();
     } else {
       $('#gitlab_version_checker_upcoming').hide();
     }
    ```

    - Where `xx` is the previously used version number
- Update the version in the `data/theme/manifest.json` file

After a peer reviews and approves your MR, you can merge the MR (which will ensure the changes go into effect on the next deployment date).

This is done on the day of a GitLab major release. So if the release is 2025-05-15, these changes would go live on that date.

### Update supported versions in the themes

We need to update the list of supported versions. This is done by modifying the theme via a MR in the sync repo doing the following:

- Update the `data/theme/script.js` file
  - Locate the definition of the `supported_versions` variable and modify the Array to have the currently supported versions.
- Update the version in the `data/theme/manifest.json` file

After a peer reviews and approves your MR, you can merge the MR.

This is done on the day of a GitLab major release. So if the release is 2025-05-15, these changes would go live on that date. As such, you will have to perform an exception deployment on the date to have the changes go live.

## Quarterly Zendesk review

As we make changes often and iterate consistently, unused items can pile up in our Zendesk instances. As such, we do a quarterly review all unused items to determine if they need to be kept around. This is done to keep our systems and repos clean.

In this task, a single DRI will collate all the needed changes together. The DRI will then work with Customer Support Systems leadership to delegate out all the tasks needing to be done.

The process for this can be divided into 5 main steps.

### Step 1: Create an issue

One of the simpler steps to the process, you need to create as `Administrative` issue in the Customer Support Systems issue tracker.

The subject should use the format `Zendesk INSTANCE Review - FYxxQy`, replacing:

- `INSTANCE` with the Zendesk instance it is for (`Global` or `US Government`)
- `xx` with the two digit fiscal year
- `y` with the quarter this is for (`1`, `2`, `3`, or `4`)

The issue will be sparse at this juncture. Make sure it is assigned to yourself (and no one else).

Once created, move to [Step 2](#step-2-determine-what-changes-are-needed)

### Step 2: Determine what changes are needed

{{% alert title="Note" color="info" %}}

- It is possible for there to be no changes needed. If this is the case, add a comment on the issue indicating as much and close the issue out.

{{% /alert %}}

In this step, you need to make a list of everything that needs to be cleaned up in the Zendesk instance. Determining what needs to be deleted varies from item to item:

- Articles
  - If you see archived items older than 6 months, it needs to be deleted
- Automations
  - If you see deactivated items older than 6 months, it needs to be deleted
- Macros
  - If you see deactivated items older than 6 months, it needs to be deleted
- Organization Fields
  - If you see deactivated items older than 6 months, it needs to be deleted
- Ticket Fields
  - If you see deactivated items older than 6 months, it needs to be deleted
  - Any fields not currently being used in a ticket form need to be deactivated
- Ticket Forms
  - If you see deactivated items older than 6 months, it needs to be deleted
- Triggers
  - If you see deactivated items older than 6 months, it needs to be deleted
- User Fields
  - If you see deactivated items older than 6 months, it needs to be deleted
- Views
  - If you see deactivated items older than 6 months, it needs to be deleted

With your list of changes in hand, add a comment indicating what all needs to be changed. Others will be working from this, so consider your formatting carefully.

Once you have added your comment, proceed to [Step 3](#step-3-get-the-issue-triaged)

### Step 3: Get the issue triaged

A simpler step, we need the issue triaged now that all required information is present. For this, do the following:

- Add the triage DRI as an assignee to the issue
- Ping the triage DRI via a comment on the issue letting them know the issue is ready for triage

The triage DRI will review the issue, add the need tags, and speak with Customer Support Systems to determine the delegation for the tasks at hand (adding a comment indicating as much).

### Step 4: Work the issue

Once the issue is triaged, it is ready to be worked. The exact task you may need to do here depends on the item itself.

- For articles, you will need to delete the article itself in Zendesk directly
- For anything else, please see that item's documentation page for details on deactivation/deletion

As you complete your delegated tasks, make sure to ping the issue's DRI to let them know it is completed.

### Step 5: Close the issue

Once all tasks are completed, the issue is ready to be closed out.

Move the issue to the Completed stage (by adding the label `Stage::Completed`) and close out the issue.
