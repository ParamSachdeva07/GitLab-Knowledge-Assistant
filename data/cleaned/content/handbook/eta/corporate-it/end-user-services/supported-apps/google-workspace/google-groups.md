---
title: Google Groups
description: Google Groups usage and configuration guides
---

Google groups are used to grant members access to specific resources or for mailing lists. As Google Groups is not an app in itself, it is not available via Okta but you can view all groups that you are a member of, and manage groups settings by going to the [Google Groups page](https://groups.google.com/).

This page aims to provide solutions for some of the most commonly asked questions we have received. For more in-depth support, please visit the [official Google Groups support page](https://support.google.com/groups/).

## Index

- [Group Requests](#group-requests)
- [Group Configuration](#group-configuration)
  - [Group Roles](#group-roles)
    - [Group Owners](#group-owners)
    - [Group Managers](#group-managers)
    - [Group Members](#group-members)
  - [Group Information](#group-information)
  - [Group Access Settings](#group-access-settings)
    - [Who can join a group](#who-can-join-a-group)
- [Additional Support](#additional-support)

## Group Requests

You can use Compass (In Slack, type "Compass" in the top search bar to find the app) to request the following:

- Create a new Google Group
- Update a Google Group
- Delete a Google Group

## Group Configuration

In order to have EUS create a new group, or modify an existing group, we need to know a number of details before we can proceed.

### Group Roles

Before creating a group, it is important to understand the roles that can be assigned to each member of the group.

#### Group Owners

Group owners have full control over the group. They can freely add and remove members, and even delete the group altogether.

<div class="w3-panel w3-yellow">
  <h3>Important!</h3>
  <p>We generally do not assign owner access to avoid groups getting accidentally deleted without approval.</p>
</div>

#### Group Managers

Group managers generally have the same permissions as owners, but without the option to delete the group.

#### Group Members

The standard access level within a group. Members are generally included in mailing lists and group conversations but cannot add or remove members.

### Group Information

When creating a new group, you will need to specify a `Group name` and the `Group email` you would like to use. The email address should be related to the group name in order to avoid confusion.

At this stage, you'll also be able to add a description of the group but that is optional.

### Group Access Settings

This section dictates who can see, join, and even contact the group. Misconfiguration here can potentially expose the group's email address to the internet.

<html>
<head>
<style>
table, td {
  border: 1px solid grey;
  border-collapse: collapse;
}
</style>
</head>

<body>

<h3>Access Settings</h3>

<table style="display: inline-block;">
  <tr>
    <td></td>
    <td>Group Owners</td>
    <td>Group Managers</td>
    <td>Group Members</td>
    <td>Entire Organization</td>
    <td>External</td>
  </tr>
  <tr>
    <td>Who can contact group owners</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Who can view conversations</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  <tr>
    <td>Who can post</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Who can view members</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Who can manage members<br>
    (Add, invite, approve)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

</body>
</html>

These settings fine-tune the detailed permissions for each group. In general, we do not recommend checking any permissions for `External` unless the group specifically needs to receive emails from outside the company.\
Please note that it is not possible to enable external people to view members, and for non-group members to approve any changes relating to group membership.

#### Who can join a group

You have the following options for adding new members

- Anyone in the organization can ask
  - Any requests requires group manager approval
- Anyone in the organization can join
  - No approval required
  - This should only be used for public mailing lists
- Only invited users
  - This is our default option
  - New members need to be explicitly invited into the group

## Additional Support

For additional support relating to Google Groups, please feel free to reach out to us directly by [email](malto:it-help@gitlab.com) or contact IT via the Compass app in Slack (type "Compass" in the top search bar to find it).
