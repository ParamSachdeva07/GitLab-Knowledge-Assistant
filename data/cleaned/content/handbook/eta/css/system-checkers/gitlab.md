---
title: 'GitLab'
description: 'Documentation on the GitLab system checker'
---

<sup>Introduced via [gitlab-com/support/support-ops/support-ops-project#1895](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/1895)</sup>

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [gitlab-support-readiness/system-checkers/gitlab](https://gitlab.com/gitlab-support-readiness/system-checkers/gitlab)

{{% /alert %}}

## Understanding the GitLab system checker

### What is the GitLab system checker

The GitLab system checker is a setup using scheduled pipelines to check the status of GitLab. It is specifically checking the following:

- Customer Support Systems projects containing more than 50 pending CI/CD jobs
- Customer Support Systems projects containing CI/CD jobs running for longer than 25 minutes

It posts to the [#css-audit-events Slack channel](https://gitlab.enterprise.slack.com/archives/C04A6E1KB89).

### How does it work

At the top of every hour UTC (`0 * * * *`), a scheduled pipeline causes the `bin/run` script to execute. This does the following:

- Iterates over a list of projects, checking:
  - How many pending CI/CD jobs they have
    - If the value exceeds 50, it stores the information to an array of problems
  - How many CI/CD jobs running that have exceeded 25 minutes of runtime
    - If there are any, it stores the information to an array of problems
- Posts in the [#css-audit-events Slack channel](https://gitlab.enterprise.slack.com/archives/C04A6E1KB89) for each piece of information in the array of problems

## Changing the GitLab system checker

{{% alert title="Note" color="primary" %}}

- This requires at least `Developer` access to the project.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To make changes to the GitLab system checker, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR (which will have them applied on the next triggered run).

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
