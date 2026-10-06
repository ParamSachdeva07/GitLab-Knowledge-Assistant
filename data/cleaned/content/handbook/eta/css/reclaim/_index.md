---
title: 'Reclaim'
description: 'Documentation on Reclaim'
---

## Reclaim to gCal

{{% alert title="Technical Details" color="primary" %}}

- Deployment type: `Ad-hoc`
- Project repo: [Reclaim to gCal](https://gitlab.com/gitlab-support-readiness/reclaim-to-gcal)

{{% /alert %}}

### What is Reclaim to gCal

Reclaim to gCal is a setup that takes payloads from Reclaim webhooks and translates them to Google calendar entries.

### How to opt into it

By default, your [scheduling links](https://app.reclaim.ai/scheduling-links) will not send any payload to the project when others use the event. To opt in to sending the payload to the project (which will result in it being added to your team's Google calendar), you must edit the scheduling link to add a webhook to it. When editing the event, it is at the bottom of the setting (Booking Page Customization). The exact webhook you use depends on your team:

- For Global Customer Support: `Add to Global Support calendar`
- For US Government Customer Support: `Add to US Gov Support calendar`

### Changing Reclaim to gCal

{{% alert title="Note" color="primary" %}}

- This requires at least `Developer` access to the [Reclaim to gCal](https://gitlab.com/gitlab-support-readiness/reclaim-to-gcal) project.
- This should only be done if there is a corresponding request issue (Feature Request, Administrative, Bug, etc.). If one does not exist, you should first create one (and let it go through the standard process before working it).

{{% /alert %}}

To make changes to Reclaim to gCal, you will need to create a MR in the project repo. The exact changes being made will depend on the request itself.

After a peer reviews and approves your MR, you can merge the MR (which will have them applied on the next scheduled run).

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
