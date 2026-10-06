---
title: Preparation for U.S. Government On-Call Shift
category: Handling tickets
description: "Support Engineering workflow detailing how to prepare for U.S. Government On-Call Shift"
---

Before you begin a U.S. Government Support On-Call shift--especially your first, or after a change of device--be sure to check that your integrations and access are correct to receive, acknowledge, and work an emergency case.

## PagerDuty

During the work week before your On-Call shift begins:

- Log in to [PagerDuty](https://gitlab.pagerduty.com/). Review the Notification Rules inside your profile. Ensure that they are configured reasonably to reach you.
- Log in to the PagerDuty app on your phone
- Test Page yourself using the Manually Trigger an Incident instructions

### Testing PagerDuty notifications

Ask another SE to manually trigger an incident in PagerDuty.

Login to [gitlab.pagerduty.com](https://gitlab.pagerduty.com) and select **+ New Incident** from the upper right corner. Then fill out the form as follows:

- **Title**: Test Page for $you
- **Impacted Service**: Customer Support Operations
- **Urgency**: High
- **Assignee**: $you

No other fields need to be filled out, therefore you may then click **Create Incident**

## Dedicated for Government

If you are locked out of [FedRAMP Okta](https://gitlabus.okta.com/), the unlock process can take some time.  Be sure to test this early in the week _before_ your on-call shift starts

- Log in to [FedRAMP Okta](https://gitlabus.okta.com/).
- From that Okta, log in to [CompSecGov](https://compsecgov.gitlab-dedicated.us/)
- Connect to the AppGuard VPN.  If you've never set this up, find the instructions in the [Support Materials](https://compsecgov.gitlab-dedicated.us/gov-support/support-materials) project
- Find credentials for one of the OpenSearch or Grafana instances in 1Password and ensure you can connect.

Note: When connected to the AppGuard VPN, CompSecGov is not reachable, without tweaking your `/etc/hosts`
