---
title: Automated Google Groups
---

## Automated Membership for Google Groups

An automated Google Group is a group where membership is automatically populated and managed based on team member attributes in Okta / Workday. This ensures that your Google Group membership stays current and accurate as team members join, change roles, or leave GitLab.

### How Membership is Determined

Typically, only employees are added to automated Google Groups. Team members classified as Contractors, Contingent Workers, or Professional Services Partners are not included in automated groups unless you specifically request an exception.

Automated Google Groups can be created based on one or more of the following team member attributes:

- Country Code
- Division
- Department
- Management Level
- Region
- User Type
- Workday Company

You can combine attributes to create more specific groups. For example, you could create a group for "All members of the Engineering Department in the Netherlands" by combining Department and Country Code.

_Note: We can not create memberships based on reporting structure, teams (supervisory orgs), or other fields not listed above._

### How Often Membership Updates

Changes in Okta typically sync to Google Groups within minutes, but may take up to a few hours or longer.
This means:

- **New team members:** Employees are automatically added on their first day, as long as their Workday data is accurate.
- **Team members leaving:** Employees are automatically removed once they leave GitLab.
- **Role or department changes:** Membership updates when a team member's relevant attributes change in Okta.

## For your info

**You can not manually manage members directly in the Google Group**

If you want to manage a Google Group that has its membership populated automatically, you cannot manually add or remove members in Google. We can either manage the group members directly in Okta, or we can use our Identity Governance and Administration (IGA) tool - Lumos - to allow team members to request access, and group owners can approve or deny their requests.

As a group manager or owner, you can manage other aspects of the group—such as permissions, settings, and content — but not members.

**Why?** Okta membership is a one-way data sync to Google Groups. If you manually add or remove someone, those changes will be overwritten the next time Okta syncs. For example, if you manually add a team member to the group, they may be removed again when Okta syncs if they don't match the group's automation criteria.

### How to request a new automated Google Group

[Here is the issue template](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?type=ISSUE&initialCreationContext=list-route&description_template=GoogleGroup_Request) for creating a new Google Group.

You can also request to have membership of an existing Google Group managed by an automated Okta group.

### How do I manually add or remove members?

If you would like to have a team member added to your automated Google Group, you have these options:

- **When creating the group:** Request to have specific team members added (such as EBAs or supporting team members)
- **For existing groups:** Create an access request issue to add them
- **If someone isn't being added correctly:** Have them verify their Okta information is accurate. For example, if a new "Systems Operations" department member expects to join the systems-operations@gitlab.com group but their department still shows as "Engineering" in Okta, they need to update this in Workday first.
