---
title: 'Automated user deletion'
description: 'Documentation on our automated user deletion'
---

This documents how automated user deletion occurs within Zendesk.

## Zendesk Global

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project: [User deletion](https://gitlab.com/gitlab-support-readiness/zendesk-global/users/deletion)

{{% /alert %}}

Every day at 0045 UTC, all end-users meeting the following criteria are deleted from the Zendesk instance via the `bin/delete` script:

- Their role is `end-user`
- They are not associated with an organization
- They are not suspended (suspended users require manual review before deletion)
- They were created more than 3 years ago (per data retention policies)

## Zendesk US Government

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project: [User deletion](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/users/deletion)

{{% /alert %}}

Every day at 0045 Pacific, all end-users meeting the following criteria are deleted from the Zendesk instance via the `bin/delete` script:

- Their role is `end-user`
- The value of their attribute `not_in_sfdc` is `true` (i.e. the checkbox is checked)
- They are not suspended (suspended users require manual review before deletion)

## Compliance level deletions

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Projects:
  - [Zendesk Global](https://gitlab.com/gitlab-support-readiness/zendesk-global/maintenance-tasks)
  - [Zendesk US Government](https://gitlab.com/gitlab-support-readiness/zendesk-us-government/maintenance-tasks)

{{% /alert %}}

After users are deleted from Zendesk (via automated deletion or manual deletion), they remain in a "deleted" state for a period. Compliance-level deletion permanently purges these deleted users from Zendesk's systems entirely to meet data retention compliance requirements.

Twice a day (at 0045 and 1245 UTC), the `bin/purge_deleted_users` script of both projects runs to remove the first 700 deleted users  (Zendesk API limit) from the Zendesk instance.
