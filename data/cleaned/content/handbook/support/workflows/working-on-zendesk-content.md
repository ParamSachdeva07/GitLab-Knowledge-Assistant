---
title: Working on Zendesk automations, triggers, macros, views, etc.
description: "How to collaborate on Zendesk automations, triggers, macros, views, etc."
category: Zendesk
---

## General process

To make it easier for Support Engineers to contribute to things that are managed by the Customer Support Operations team, data and code have been separated for some items. This approach removes the need for Customer Support Operations to review every change proposed for Zendesk views, macros, triggers and automations.

For any **changes** to the content of Zendesk views, macros, triggers and automations consider their impact first. If your changes go beyond something like fixing a typo or updating a link and have broader repercussions for the team, consider the [Change Management in GitLab Support](/handbook/support/managers/change-management/) handbook page. Otherwise you can suggest your changes directly via a merge request in the relevant managed content project.

**For creating new content or renaming existing content** (e.g. a new macro, or renaming a view), an STM issue is required as Customer Support Operations has to handle these actions. The managed content projects only allow *managing content* of existing items.

### Managed content projects

Refer to the corresponding projects and create a merge request with your changes:

- [gitlab-com/support/zendesk-global/automations](https://gitlab.com/gitlab-com/support/zendesk-global/automations)
- [gitlab-com/support/zendesk-global/macros](https://gitlab.com/gitlab-com/support/zendesk-global/macros)
- [gitlab-com/support/zendesk-global/triggers](https://gitlab.com/gitlab-com/support/zendesk-global/triggers)
- [gitlab-com/support/zendesk-global/views](https://gitlab.com/gitlab-com/support/zendesk-global/views)
- [gitlab-com/support/zendesk-us-government/automations](https://gitlab.com/gitlab-com/support/zendesk-us-government/automations)
- [gitlab-com/support/zendesk-us-government/macros](https://gitlab.com/gitlab-com/support/zendesk-us-government/macros)
- [gitlab-com/support/zendesk-us-government/triggers](https://gitlab.com/gitlab-com/support/zendesk-us-government/triggers)
- [gitlab-com/support/zendesk-us-government/views](https://gitlab.com/gitlab-com/support/zendesk-us-government/views)

Whether you're proposing minor changes directly or something bigger following an RFC discussion, tag a Support Manager for review and ask them to merge the changes. Once changes have been merged in one of these projects, you'll notice that the `Sync Stage` badge says `Awaiting Deployment` on the project overview page. This indicates that there's changes in the project that will be rolled out during the next regular deployment.

#### Quarterly Audits

At the start of every quarter, scripts will run in the sync repos checking for "orphaned" managed content files (i.e. files without a matching Zendesk item). If there are any of these, an issue will be made in the Support Team Meta project (pinging the groups/persons listed in the corresponding CODEOWNERS file).

The objective of these is to either delete files no longer in use or to raise issues with Customer Support Operations if a file is reported as "orphaned" but should still be in use.

#### Macros

- If you want to edit the wording of a macro, make an MR to the repo (Zendesk Global or Zendesk U.S. Government).
- If you want to make non-wording changes (renaming it, add/removing options, etc.), create a feature request to the Customer Support Operations team via [this template](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature)
- If you want to deactivate a macro, create a feature request to the Customer Support Operations team via [this template](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature)
- If you want to create a "simple" macro, use the Zendesk internal form for the corresponding Zendesk instance:
  - [Zendesk Global](https://gitlab-internal.zendesk.com/hc/en-us/requests/new?ticket_form_id=22784239213084&tf_22783439650716=custsuppops_ir_category_create_macro)
  - [Zendesk U.S. Government](https://gitlab-federal-internal.zendesk.com/hc/en-us/requests/new?ticket_form_id=41826926738708&tf_41825819758484=custsuppops_ir_category_create_macro)
  - **NOTE**
    - New macro names should follow the format as seen in Zendesk using `::`. For example, `Support/SaaS/GitLab.com/Abuse/Identity Verification Request` Accepts would be `Support::SaaS::GitLab.com::Abuse::Identify Verification Request Accepts`.
    - If a managed content file is needed (as you selected a `Public` or `Internal` comment would be used), the automations will create a placeholder file for you (if said file does not exist). For the quickest resolution, it is best to *not* create the managed content file before your ticket submission.
- If you want to create an "advanced" macro, create a feature request to the Customer Support Operations team via [this template](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature)
  - **NOTE** It is required you create the managed content file before filing the request to avoid significant delays
- To discuss a macro (but not actually action on anything), use a support-team-meta issue.

#### Simple vs Advanced Macros

A simple macro is one that only would modify the following:

- Ticket assignment (or removal thereof)
- Adding tags to the ticket
- Adding a public or private comment to a ticket
- Changing the status of a ticket

Anything beyond that would make it an "advanced" macro.

#### Organizations

Select modifications to Zendesk organizations can be made through the use of the Zendesk internal form for the corresponding Zendesk instance:

- [Zendesk Global](https://gitlab-internal.zendesk.com/hc/en-us/requests/new?ticket_form_id=22784239213084)
- [Zendesk U.S. Government](https://gitlab-federal-internal.zendesk.com/hc/en-us/requests/new?ticket_form_id=41826926738708)

The modifications allowed are:

- Add or remove a project collaboration ID
- Add or remove an ASE (support leadership only)

To make changes to a Global organization's note you would use [the Zendesk Global Organizations project](https://gitlab.com/gitlab-com/support/zendesk-global/organizations) to modify an organizations notes.

For U.S. Government Organizations, all organization notes are managed manually by the Customer Support Operations team. Due to the sensitive nature of the organizations, please reach out to the Customer Support Operations team via slack to make changes.

## Previewing variable replacement

When using [liquid variables](https://support.zendesk.com/hc/en-us/articles/4408886858138-Zendesk-Support-placeholders-reference) it can be useful to verify that they will be working as you expect them to. A simple way to do this is to create a test ticket, pasting the content of your automation, trigger, or macro in there and observing the outcome.
