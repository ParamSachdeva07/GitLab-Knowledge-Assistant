---
title: 'Support team YAML files'
description: 'Documentation on Support team YAML files'
---

This guide documents the Support team YAML files - a centralized data source containing team member information used by various Customer Support Systems automation and integrations. These files enable consistent agent data across systems and serve as the source of truth for team structure, skills, schedules, and assignments.

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [Support Team project](https://gitlab.com/gitlab-support-readiness/support-team)

{{% /alert %}}

## Understanding the Support team YAML files

### What are the Support team YAML files

The Support team YAML files are a group of YAML files containing team member information including work schedules, skill areas, system IDs (Zendesk, Slack, GitLab, PagerDuty), regional assignments, and focus allocations. This data serves as the single source of truth for team member information used across multiple Customer Support Systems systems.

### Where are the Support team YAML files

The Support team YAML files live within the [Support Team project](https://gitlab.com/gitlab-support-readiness/support-team).

### How are the Support team YAML files used

Various scripts and projects will use [GitLab Deploy Keys](https://docs.gitlab.com/user/project/deploy_keys/) to clone the repo and then parse the YAML files.

Some examples of use for the files:

- Managing Zendesk agent data and settings ([source](/handbook/eta/css/zendesk/users/agents))
- Determining a list of US Government support agents ([source](/handbook/eta/css/zendesk/tickets/round-robin))
- Mapping Zendesk agents to Slack user IDs ([source](/handbook/eta/css/slack/#notify-oncall))

## Changing Support team YAML files

### Changing your own file

{{% alert title="Note" color="primary" %}}

The following attributes will require your manager to approve the merge request by the Customer Support Systems team can proceed:

- Title
- Working Hours
- Focuses
- Zendesk Groups (either instance)
- Display name / Alias updates
- Round robin settings (US Government only)

{{% /alert %}}

If you need to change your own Support team YAML file, you may do so by creating a merge request. From there, the Customer Support Systems team will review, approve, and merge the merge request. Should any issues arise, the Customer Support Systems team will notify you via the merge request.

### Changing your report's file

If you need to change the Support team YAML file of a person you manage, you may do so by creating a merge request. From there, the Customer Support Systems team will review, approve, and merge the merge request. Should any issues arise, the Customer Support Systems team will notify you via the merge request.

### Changing anything else

To have anything else changed in the Support team YAML files, please create a [Feature Request issue](https://gitlab.com/gitlab-com/eta/css/issue-tracker/-/issues/new?description_template=Feature) (as it will require manual intervention by the Customer Support Systems team).

## Anatomy of a Support team YAML file

With a Support team YAML file are many attributes. Below you will find details on each one (and any sub-attributes contained within).

### name

The team member’s name

### email

{{% alert title="Warning" color="warning" %}}

This should never be an alias

{{% /alert %}}

The team member’s official GitLab email.

### title

The team member’s job title

### entity

The GitLab entity the team member belongs to. A list of available entities is:

- GitLab BV
- GitLab Canada Corp
- GitLab GmbH
- GitLab Inc
- GitLab IT BV
- GitLab Korea LTD
- GitLab PTY Ltd
- GitLab PTY Ltd NZ
- GitLab Singapore PTE. LTD
- GitLab UK Ltd

### working_hours

A String representing team member's working hours. You should specify the timezone to be safe. (examples being 0800-1600 Central time or 0000-0800 UTC).

### reports_to

The name of the person to whom the team member reports

### region

The team member’s region. The current regions we have available are:

- AMER-W
- AMER-C
- AMER-E
- APAC
- EMEA

### start_date

The date the team member started at GitLab (in ISO format).

### calendly

The link to the team member’s calendly. Should always be the link to their main page, not an event.

### languages

An array of languages the team member knows

### pagerduty

A hash containing Pagerduty information. It contains a single attribute:

- `id`, which is the team member’s Pagerduty user ID

### focuses

An array containing the team member’s focuses. Each focuses array contains a hash with the attribute of:

- `name`, which is the name of the focus
- `percentage`, which is the percentage of the focus

All percentages should add up to be 100.

A list of current focuses available are:

`Onboarding` - focused on onboarding to their position
`SaaS` - focused on working Global SaaS support tickets
`License and Renewals` - focused on working Global L&R support tickets
`Self-Managed` - focused on working Global Self-Managed support tickets
`Operations` - focused on Customer Support Systems responsibilities
`Management` - focused on Support Leadership responsibilities
`US Federal` - focused on working US Federal support tickets
`ASE` - focused on Assigned Support Engineer work

#### Additional info about the ASE focus

When the name of the focus is `ASE`, additional attributes can be added to the hash:

- `zendesk`, which specifies the instance the organizations are on
- `organizations`, which is an array of information about the specific organizations, having the attributes of:
  - `id`, which is the Zendesk ID for the organization
  - `percentage`, which specifies the percent of ASE time spent on that organization

As an example, if Bob spent 50% of his time as an ASE in the Global Zendesk instance, and managed two organizations (123 and 456) evenly, he would enter his ASE focus object like so:

```yaml
focuses:
- name: 'Self-managed'
  percentage: 50
- name: 'ASE'
  percentage: 50
  zendesk: global
  organizations:
  - id: 123
    percentage: 50
  - id: 456
    percentage: 50
```

This means Bob spends 50% of his time doing Self-Managed work, and 50% of his time doing ASE work. And of that ASE work, 50% of it is for org 123 and 50% is for org 456.

Another example, if Bob spent 60% of his time as an ASE in the US Government, and managed two organizations (123 and 456) with different percentages, he would enter his ASE focus object like so:

```yaml
focuses:
- name: 'Self-managed'
  percentage: 40
- name: 'ASE'
  percentage: 60
  zendesk: us-federal
  organizations:
  - id: 123
    percentage: 25
  - id: 456
    percentage: 75
```

This means Bob spends 40% of his time doing Self-Managed work, and 60% of his time doing ASE work. And of that ASE work, 25% of it is for org 123 and 75% is for org 456.

### zendesk

A hash containing Zendesk information. The attributes are:

- `main`, which is a hash containing the information pertaining to Zendesk Global (note: the YAML key is `main` even though we refer to it as "Zendesk Global" in documentation)
- `us-federal`, which is a hash containing the information pertaining to Zendesk US Government (note: the YAML key is `us-federal` even though we refer to it as "Zendesk US Government" in documentation)

Each of those attributes have further child attributes within them:

- `id`, which is the team member’s Zendesk user ID
- `groups`, which is the groups the team member’s Zendesk user is in
- `role`, which is the role the team member’s Zendesk user has
- `show_in_signature`, which is a hash containing an attribute of:
  - `gitlab_handle`, which tells the agent sync to add a line to your signature including your GitLab.com handle
- `alias`, which is what display name to use in Zendesk. If left blank, your full name will be used as the default
- `salutations`, which is an array of salutations to use in a team member’s Zendesk user’s signature

#### Additional info about the US Government round robin

For the `us-federal` attribute, there is an additional attribute:

- `round_robin`, which is a Hash containing the attributes:
  - `active`, which dictates whether you are part of the round robin or not
  - `modifier`, which is the modifier to multiply by when calculating your total workload weight
    - In the event this number is 0, the round robin will use 1
  - `forms_enabled`, which is an array of ticket forms (by the form's name) that could be assigned to the agent

As an example:

```yaml
    round_robin:
      active: true
      modifier: 1.5
      forms_enabled:
      - 'GitLab Dedicated'
      - 'Support'
      - 'Upgrade Assistance'
```

Using this entry, the agent would be part of the round robin, would have their workload increased by a factor of 1.5, and would only be assigned tickets using the forms `GitLab Dedicated`, `Support`, or `Upgrade Assistance`.

### gitlab

A hash containing GitLab.com information. The attributes are:

- `id`, which is the team member’s GitLab.com user ID
- `username`, which is the team member’s GitLab.com username

### slack

A hash containing Slack information. The attributes are:

- `id`, which is the team member’s Slack user ID
- `username`, which is the team member’s Slack handle

### modules

An array of learning modules the team member has completed.

### knowledge_areas

An array of areas in which the team member is knowledgeable.

Each item is a Hash containing information about the team member’s perceived knowledge of along with the corresponding skill level they have on it.

Each item’s attributes are:

- `name`, which is the knowledge area’s name
- `level`, which is the team member’s knowledge level of the area
  1. Learning - I’m still learning the basics and I’m not yet ready to take tickets.
  1. Ready to work tickets - I’m ready to work on tickets, or learn by working on tickets.
  1. Looking to help others - I want to help others with tickets or learning.

### product_categories

An array of team member competencies tied to GitLab product categories.

Each item is a Hash containing:

- `name`, which is the product category name (e.g., "CI/CD", "Security", "Backup/Restore")
- `level`, which is the competency level (uses same 1-3 scale as `knowledge_areas`)

### pronouns

The preferred pronouns of the team member.

## Administrator tasks

### Making changes to the Support team YAML files

{{% alert title="Warning" color="warning" %}}

- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

You will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR (which will have the changes start being used moving forward).
