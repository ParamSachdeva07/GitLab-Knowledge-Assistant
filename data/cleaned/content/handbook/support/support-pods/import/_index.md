---
title: Import Support Pod
description: A dedicated group to work together on Import based tickets.
---

## Purpose

Creating a dedicated group to work together on Import based tickets.

This will allow everyone to gain more knowledge regarding the various GitLab integrations and an easier location to share the knowledge across regions.

## Current objectives

- Collaborate on tickets related to:
  - Import/Export of GitLab projects
  - Migrations of GitLab resources between GitLab instances
  - Imports from 3rd party providers to GitLab
- Gain and share knowledge
- Documentation updates

## Support Pod members

- Lead: {{< member-by-name "Anton Smith" >}} (`@anton`)
- {{< member-by-name "Justin Farmiloe" >}} (`@jfarmiloe`)
- {{< member-by-name "Emily Chang" >}} (`@emchang`)
- {{< member-by-name "David Wainaina" >}} (`@dwainaina`)

## Collaboration channels

- Slack channel: [#spt_pod_import](https://gitlab.slack.com/archives/C052K0Z1F8T)
- Epic - https://gitlab.com/groups/gitlab-com/support/-/epics/145

## Create Import/Export view

Since limitations in Zendesk prevent each pod from having a shared view, you will have to create one manually.
Follow the steps below and you should have a personal view in no time.

1. Click on `Manage views`
1. In the new Window on the top right click `Add view`
1. Give the view a nice name (`Import (All regions)`)
1. Move to `Conditions`
   1. `Tickets must meet all of these conditions to appear in the view`
      1. Click `Add condition` and from left to right
         - `Status`
         - `Less than`
         - `Pending`
      1. Click `Add condition` and from left to right
         - `Tags`
         - `Contains at least one of the following`
         - `support_pg_management_project_import_export support_category_pg_management_project_import_export`
1. Move on to `Formatting options`
   1. This is kind of up to your flavour but below are some suggestions.
      1. Next SLA breach
      1. Priority
      1. Preferred Region for Support
      1. Subject
      1. Organization
      1. Assignee
      1. Request date
      1. Latest update by assignee
1. Change `Order by` to `Next SLA breach`, `Ascending`
1. Click `Save`

Congratulations you now have a personal Integrations Pod View.
