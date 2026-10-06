---
title: 'Audits'
description: 'Documentation on Customer Support Systems audits'
---

## Understanding audits

### What are audits

Audits are what we call the process (and core responsibility) that involves reviewing who has what access to various platforms.

### Why do we perform audits

There are a good number of reasons that could be made for doing audits, but the biggest ones for us are:

- Ensure no security issues are occurring in the agent/user space.
- Ensure we have accurate information for procurements and renewals.
- Ensure we follow best practices for reviewing who is using the various systems we manage.

### What is audited

- Customer Support Systems projects
- Zendesk Global
- Zendesk US Government

### When are audits done

On the 1st day of each quarter, issues will be generated via the [System Audits](https://gitlab.com/gitlab-support-readiness/system-audits) project. After issue creation, audits are then performed.

## Customer Support Systems projects

This is done via the `bin/ops_project_audit` script. When the script runs, it does the following:

- Gathers a list of all projects within our group
- Gathers all protected branches within the found projects
- Gathers all merge request settings within the found projects
- Analyzes all projects for issues, including:
  - Incorrect author approval settings
  - Incorrect commit approval settings
  - Incorrect approval override settings
  - Incorrect approval retention settings
  - Incorrect list of those who can merge
  - Incorrect list of those who can push to the default branch
- Creates an issue detailing all findings

Those working the issue generated will review the issue for any problems and look into any issue present in the issue.

After rectifying any problems, the issue is then closed out.

## Zendesk Global audit

This is done via the `bin/zendesk_global` script. When the script runs, it does the following:

- Gathers a list of all agents in Zendesk (i.e. those with a role of `admin` or `agent`)
- Creates three lists of users:
  - Light agents (those with a custom role ID of `360004984553`)
  - Admins (those with a custom role ID of `360004957599`)
  - Full agents (those not listed in the Light agents and Admins lists)
- Loops over all agents in Zendesk to check if any of them are suspended (as they should not be)
- Creates an issue, detailing the following
  - List of all light agents
  - List of all full agents
  - List of all admins
  - List of all suspended agents

Those working the issue generated will review the issue for any problems and look into any issue present in the issue.

After rectifying any problems, the issue is then closed out.

## Zendesk US Government audit

This is done via the `bin/zendesk_us_government` script. When the script runs, it does the following:

- Gathers a list of all agents in Zendesk (i.e. those with a role of `admin` or `agent`)
- Creates three lists of users:
  - Light agents (those with a custom role ID of `360008074111`)
  - Admins (those with a custom role ID of `360016820032`)
  - Full agents (those not listed in the Light agents and Admins lists)
- Loops over all agents in Zendesk to check if any of them are suspended (as they should not be)
- Creates an issue, detailing the following
  - List of all light agents
  - List of all full agents
  - List of all admins
  - List of all suspended agents

Those working the issue generated will review the issue for any problems and look into any issue present in the issue.

After rectifying any problems, the issue is then closed out.
