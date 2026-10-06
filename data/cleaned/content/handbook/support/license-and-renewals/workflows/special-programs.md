---
title: "Supporting GitLab Community Programs"
category: General
description: Instructions for redirecting community programs subscription inquiries
---

GitLab offers several programs to help introduce GitLab's most powerful features to communities who may not otherwise have the means to access them. These include:

- [GitLab for Education](/handbook/marketing/developer-relations/programs/education-program/)
- [GitLab for Open Source](/handbook/marketing/developer-relations/programs/open-source-program/)

[The Developer Relations Programs team](/handbook/marketing/developer-relations/programs/) is the DRI for these programs.

For registered non-profit organizations, GitLab also offers discounts. Contact GitLab's [Environmental, Social, and Governance (ESG) team](/handbook/legal/esg/#faq) for more information regarding this program. And for Startups, the HVS and FOs team offer discounts through the [GitLab for Startups](/handbook/marketing/growth-marketing/growth-community-programs/#gitlab-for-startups-program) program.

Use the relevant workflows below when you receive a ticket about [GitLab for Education](https://about.gitlab.com/solutions/education/), [GitLab for Open Source](https://about.gitlab.com/solutions/open-source/) or [GitLab for Startups](https://about.gitlab.com/solutions/startups/).

{{% alert title="Note" color="info" %}}
Program members receive only limited support with subscriptions granted through community programs. They are able to open a support ticket via the [GitLab Support Portal](https://about.gitlab.com/support/#issues-with-billing-purchasing-subscriptions-or-licenses) only for errors involving the Community Self-checkout Portal on CustomersDOT or for errors relating to their subscription. Internal escalations for GitLab for Education and GitLab for Open Source can be made via Slack channel [`#developer-relations-programs`](https://gitlab.enterprise.slack.com/archives/CB21NTDJQ). For Startups Program use the Slack channel [`#startups-program-questions`](https://gitlab.enterprise.slack.com/archives/C04SS1ERWP9)
{{% /alert %}}

## Workflows

### Applications and renewals

When the requester seeks to apply for membership in a program or to
renew an existing membership, they will need to submit the program's
application form. Use the appropriate Zendesk macro:

- GitLab for Education (EDU):
  [`General::EDU Response`](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/EDU%20Response.yaml)
- GitLab for Open Source (OSS):
  [`General::OSS Response`](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/OSS%20Response.yaml)
- GitLab for Startups:
  [`General::Startup Response`](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/Startup%20Response.yaml)

If the requester is seeking to renew, also advise them:

1. Use the same form as for new applications
1. The person claiming the renewal for the subscription **must** be the one
   who created the subscription in the GitLab Customer Portal for this institution
1. If they need to have a different person claim the renewal, the existing owner
   needs to
   [transfer ownership of the Customers Portal account](https://support.gitlab.com/hc/en-us/articles/17767356437148-How-to-transfer-subscription-ownership).

### Product Transfer

While redeeming a community program coupon customers may select the wrong
product type by accident (SaaS instead of Self-Managed, or vice-versa). Link
and use [this KB article](https://support.gitlab.com/hc/en-us/articles/22725476432028-Making-changes-to-Community-programs-EDU-OSS-Non-profits-or-Startups-subscriptions).
Also use the
[Program-specific contact inboxes](#program-specific-contact-inboxes) workflow.

### "This code has already been used." error when attempting to redeem coupon

Please raise the ticket in `#developer-relations-programs` as the coupon may have been erroneously issued.

### Customer is concerned by their seat usage or true-ups

While applying, customers are asked to provide their desired seat count -
during their subscription term they can exceed this and then upon renewal the
true-up cost will be zero (and the overage seats will be added to the renewal
term). If the customer wants to make a change to the number of seats associated,
link and use [this KB article](https://support.gitlab.com/hc/en-us/articles/22725476432028-Making-changes-to-Community-programs-EDU-OSS-Non-profits-or-Startups-subscriptions).

## Program-specific contact inboxes

For any enquiry relating to a specific program, whether described above or not,
please follow this workflow:

1. Advise the requester to contact the program using its direct email inbox:
   1. EDU: `education@gitlab.com`
   1. OSS: `opensource@gitlab.com`
   1. Startups: `startups@gitlab.com`
   1. Non-Profits: `nonprofits@gitlab.com`
1. Ask the customer to update us as soon as they get a meaningful response, or
   to let us know they have not received a meaningful response after waiting
   for 2 business days, whichever comes first
1. Put the ticket on hold
1. If the customer reports back that they are being helped, close the ticket
1. Otherwise, if the customer reports back that they are not being helped, let them know
   that you will contact the program team yourself to ensure they get the help
   they need, and then reach out in the `#developer-relations-programs` Slack channel. For non-profits, reach out in `#gitlab-for-nonprofits` channel.
1. Otherwise, if the customer does **not** report back and the ticket returns
   from being on hold, close the ticket with an appropriate message

## Troubleshooting

GitLab's Developer Relations Programs team processess program applications according to [an automated workflow](/handbook/marketing/developer-relations/programs/program-resources/#automated-application-workflow). Review the handbook pages related to that workflow for additional details on how it works.

To troubleshoot errors during the registration process, follow the [Troubleshoot Errors While Making Purchases on CustomersDot document](/handbook/support/license-and-renewals/workflows/customersdot/troubleshoot_errors_while_making_purchases#getting-error-message-from-sentry).

{{% alert title="Note" color="info" %}}
Since the customer has not signed up yet, there is no `user:customerID`. Use `user.ip:CustomerIP` instead.
{{% /alert %}}

You can retrieve `CustomerIP` by:

1. On Zendesk ticket, click on `Conversations`
1. Choose `Events` from the drop down
1. The IP is shown under every customer reply.

{{% alert title="Note" color="info" %}}
The IP is only available when the customer is signed in on Zendesk. If the customer submits the ticket via email, and IP is not available, please ask the customer for the IP they used during the signup process.
{{% /alert %}}

## Example of previous cases

- [ZD Ticket 288871](https://gitlab.zendesk.com/agent/tickets/288871)
- [Related Sentry event 2575450](https://sentry.gitlab.net/gitlab/customersgitlabcom/issues/2575450/events/40335146/)
- [Bug issue](https://gitlab.com/gitlab-org/customers-gitlab-com/-/issues/4288)

## See Also

- [Collaborating with Developer Relations Programs (Sales Training)](/handbook/sales/training/sales-enablement-sessions/enablement/collaborating-community-programs/)
