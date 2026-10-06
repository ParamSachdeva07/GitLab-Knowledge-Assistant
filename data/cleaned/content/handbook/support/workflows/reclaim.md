---
title: Reclaim.ai Setup for Support
category: References
description: "Workflow for setting up and using Reclaim.ai scheduling links in Support Engineering"
---

**Note**: Always use [single use scheduling links](#generating-a-customized-hidden-scheduling-link) when offering a call with customers. Never share your default scheduling page URL.

## Overview

Reclaim.ai is GitLab's scheduling tool for Support customer calls. This workflow uses a customized, hidden, and unique scheduling link for each Zendesk ticket, to prevent unintended access to your scheduling page.

## Availability schedule setup

Setting up your availability schedules ensures you get scheduled calls during your intended hours.

- Navigate to [Reclaim Settings > Scheduling](https://app.reclaim.ai/settings)
  - Set your preferred `Scheduling Window`. This defaults to 12 weeks - recommend reducing to 4-8 weeks depending on your preference
  - Set your `Date Format` to ISO (YYYY/MM/DD)
- Navigate to [Settings | Hours](https://app.reclaim.ai/settings/hours)
  - Set your `Home timezone`
  - Optionally, set a temporary timezone while traveling - see [below](#temporarily-changing-your-timezone) for guidance.
  - Set your `Hours` - you can have up to 3 different schedules which you can configure in your scheduling links, so you may be happy to use a wider set of hours for your 15 minute meeting offerings, versus longer call offerings which you may only want to offer in your mornings (or similar!). The **default** for Meeting Links will be the `Meeting Hours` schedule, so if you're only configuring one - make it this one! Configure as many, or as few of these as suits your needs.
- If desired, set Buffer times between meetings by going to [`Settings | Buffers`](https://app.reclaim.ai/settings/buffer-time), or `Time blocking | Buffers` from the left sidebar.

### Temporarily changing your timezone

If you are temporarily working hours different to your usual schedule, you can update Reclaim so that customer calls will be booked during your updated timezone.

1. Log in to Reclaim and navigate to Settings | Hours
1. Choose the Travel timezone
1. Set the start and end dates that you will be in that Timezone.

You can have multiple travel timezones set up for different dates, so if you have a travel itinerary in various locations, you can set these all up at once, or any time you know the dates you'll be in a different timezone you can immediately add these into Reclaim.ai.

## Reclaim scheduling links setup

For Support use, we remove the Scheduling Links that are visible when anyone goes to your main Booking Page, and instead make use of Hidden Links, as noted above.

Modify your setup as follows (do this once!):

1. Access Reclaim by using the Okta tile, ensure you have your primary work calendar connected
1. Set up Zoom integration in your Reclaim account under [Integrations](https://app.reclaim.ai/settings/integrations)
1. Navigate to `Meetings | Scheduling Links`
1. You should have 3 links there by default - 1 hour, 15 or 30 minutes & 15 minutes.
1. Modify each of them as follows (and create additional durations if required).
   - **Event Details**
     - Modify the title of each to include 'Support'
     - Modify the description to `x minute meeting with GitLab Support`
   - **Organizers**
     - The Organizers field allows you to choose which of your 3 time schedules to offer - it will default to `Meeting Hours`, but if you want to use either of the other 2 schedules, OR set up a very specific set of available hours, modify this here
   - Make Zoom the default video conference option - **Organizers** > **Videoconference link & location**
   - **Scheduling**
     - The graph will show your available hours based on the schedule you chose in the Organizers section. You cannot modify this here, this purely for review purposes.
     - Set `Durations` to match what you've put in the description - use only 1 duration per link to prevent surprises!
     - `Soonest Scheduling time` determines how soon after creating the link you can be booked. It defaults to 4 hours, if you are happy to allow a customer to book you sooner than that, modify it to suit
   - **Link settings**
     - Toggle on the `Hide link on your booking page` option to make the link hidden
   - **Booking page customization**
     - Change the branding to `Use custom branding`
     - Under `Webhooks` click `+ Add webhook` and choose either `Add to Global Support calendar`, or `Add to US Gov Support calendar` depending on your role. [Learn how to opt into the Support calendar webhook](/handbook/eta/css/reclaim/#how-to-opt-into-it). This gives the team visibility of scheduled customer calls.

    Ok, once you've done all of that once, you don't need to do it again! Read on for how to generate a [Customized hidden link](#generating-a-customized-hidden-scheduling-link) for a ticket to provide to your customer.

### Why hidden links matter

When you make your scheduling links hidden:

- Your public page (e.g. `https://app.reclaim.ai/m/your-username`) shows "No scheduling link found" (provided you have reconfigured all of the default Reclaim.ai links or replaced them with hidden scheduling links)
- Only people with the direct hidden link URL can access and book time
- This prevents unauthorized or unexpected bookings from people who find your scheduling page
- Each ticket-specific link remains functional for the intended customer

## Generating a customized hidden scheduling link

Customized, hidden links are the recommended method for scheduling customer calls. Each ticket should have its own unique link.

### Creating a link for a ticket

Follow these steps to create a ticket-specific scheduling link (Note: this assumes you've completed the setup detailed under [Reclaim scheduling links setup](#reclaim-scheduling-links-setup):

1. Open [Reclaim](https://app.reclaim.ai/) and navigate to your Support scheduling links under `Meetings | Scheduling Links | Hidden Links`
1. Use the link for the duration you want to offer and select **...** (three dots menu) `Share & personalize`
1. Click the `Personalize` button at the bottom of the dialog.
   - Add the customer's name and email to `Details | Invitee`
   - Modify the `Meeting name` in the `Details` section to include the Zendesk ticket number - this allows other team members to see this reference in the Support Calendar
   - Check your availability is what you expect under `Attendees & Location`
   - Check that the `Location` is Zoom.
1. Under `Scheduling` you can customize the `Soonest time` you are available along with the `Latest time` - set either an end date for availability, or limit it to a number of days into the future.
1. Toggle the `Link options` section and modify the `URL` slug to use a unique identifier including the ticket number, such as `support-zd-123456`
1. Click `Copy link`. The URL will follow this pattern:

   ```plaintext
   https://app.reclaim.ai/m/your-username/support-zd-123456
   ```

1. **Important**: Save the link in the Zendesk ticket. Reclaim does not retain customized hidden links in the normal Scheduling Links list, so the URL must be saved if it needs to be reshared. (Note that these links cannot be edited).
1. Send the link to the customer using the applicable customer-call macro.

### Managing multiple scheduling links

When working on concurrent tickets that require customer calls:

- Create a separate single use link for **every** ticket
- Use the ticket number in the URL slug to easily identify links (e.g., `support-zd-123456`, `support-zd-123457`)
- Store each link URL in its corresponding Zendesk ticket for reference

## Link expiration and limitations

### Current limitations

Reclaim customized links have some limitations:

- Customized hidden links do **not** currently provide a single-booking enforcement
- Links may remain reusable for 30 days from creation

### Compensating controls

Until Reclaim provides explicit link invalidation after booking, the following compensating controls are in place:

1. **Ticket-specific URLs**: Each ticket has its own unique link, limiting exposure
1. **Hidden links**: Links are not discoverable from your public scheduling page
1. **Saved ticket records**: Link URLs are stored in Zendesk for tracking
1. **Offer a short window**: When configuring the availability window, set an end date or a rolling window that is long enough to give the customer options, but short enough to limit multiple bookings on that link.
1. **30-day expiry**: Links automatically expire after 30 days
1. **Right to decline**: Apply the existing right-to-decline process to duplicate, unrelated, or abusive bookings

## Support calls in the team calendar

Customer calls should be visible in the GitLab Support Google calendar for team awareness. This is handled by configuring the [Support calendar webhook](/handbook/eta/css/reclaim/#how-to-opt-into-it) in your links.

- The ticket number in the meeting title provides context for others who may join

## Protecting your scheduling page

Customer calls should be invitation-only. By using customized hidden links:

- Your public Reclaim page shows no available scheduling options
- Only customers with the direct link can book time with you
- This prevents unauthorized access to your calendar

## References

- [Reclaim: Using link groups to organize and share your links](https://help.reclaim.ai/en/articles/6806567-using-link-groups-to-organize-and-share-your-links)
- [Reclaim: Scheduling Links documentation](https://help.reclaim.ai/en/collections/3527648-scheduling-links)
