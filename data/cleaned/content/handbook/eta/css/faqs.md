---
title: FAQs
description: Frequently asked questions for Customer Support Systems
---

## Access related

### What if I want access to something owned by Customer Support Systems?

Following with Security's [Access Management Standards](https://internal.gitlab.com/handbook/security/policies_and_standards/access-management-standard/), we follow the [principle of least privilege](https://csrc.nist.gov/glossary/term/least_privilege). As such, we review each request on a case by case basis.

To begin the process, file an [Individual Bulk Access Request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?description_template=Individual_Bulk_Access_Request) issue. Once approved by your manager, assign it to `@jcolyer` and `@dtragjasi`, who will review the situation and determine how to best proceed.

## Team related

### How can I quickly check the status of the various Customer Support Systems components?

You can use our [status page](https://statuspage.incident.io/cust-support-ops/main) to check on the status our component.

## Zendesk related

### If we receive any problem in using Zendesk, can we contact Zendesk directly?

Please contact Customer Support Systems team first. Discuss the problem by asking a question in channel and tagging @support-ops. It is a high probability that we can help you resolve the problem at hand. In cases where we cannot and we do need to contact Zendesk support directly, it is best to have Customer Support Systems handle that.

### What will happen if Zendesk is down globally?

Zendesk will only go down when the internet is globally affected because they use Pods for services. This ensures that if a region is facing downtime, Zendesk can quickly mitigate that while making sure services run smoothly. However, if you are still facing any problem accessing Zendesk, please contact the Customer Support Systems team. In the case that Zendesk is down globally, we have an email support option available (details of use to be determined as needed).

### Is there any disaster recovery plan available?

Zendesk keeps the data in backup servers with all due diligence. This ensures that we can recover data when it is needed. These backups are utilized to restore Zendesk in the case it fails due to a problem on Zendesk's end.

Also, the Customer Support Systems team ensures all triggers, automations, views, macros, forms, fields, conditions, etc are documented to save the hassle of writing up everything from scratch.

### When using Zendesk, the aspect ratio is off

This would present in the following possible ways:

- Only showing one tab before using group
- Odd blank spaces appearing

While the exact cause has not yet been determined, the spacing and grouping used in Zendesk is dependent on the aspect ratio and screen size of your monitor. When issues surrounding it have occurred, we have found Zooming in and back out (or zooming out and back in) often fixes the problem. We have also found doing a hard refresh (Ctrl+Shift+R / Cmd+Shift+R) can rectify the problem.

Failing all of that working, the suggested fix would be to log out, clear your cache, clear your cookies, and log back in.
