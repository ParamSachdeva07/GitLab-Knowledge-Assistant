---
title: "Opensense Email Signatures"
description: "Opensense centralized platform for managing email signatures and dynamic marketing banners."
---

## Overview

The Marketing Operations team uses Opensense to centrally manage corporate email signatures across the Sales Dev team. This ensures brand consistency, legal compliance, and provides a platform for dynamic marketing banners. Unlike client-side tools, Opensense uses server-side stamping to apply signatures. This ensures that every email sent—whether from Gmail, Outreach, or a mobile device—carries a consistent, high-fidelity brand experience without relying on local browser extensions.

## Why we use Opensense

- **Brand Consistency:** Ensures SD team members have the correct logo, font, and brand colors.
- **Data Accuracy:** Automatically syncs user data (name, title, department) from our Okta group directory.
- **Marketing Real Estate:** Allows Marketing to run banner campaigns in BDR/SDR signatures for events, product launches, or webinars.
- **Security:** Centralized management reduces the risk of malicious links or unauthorized changes to corporate signatures.

## Single Source of Truth

We have Okta as the primary source of truth for all signature data. This ensures that when a team member's title or department changes in Okta, it is automatically reflected in their email signature within the next sync cycle.

## New User Access

information coming soon.

## For New Team Members

Signatures are automatically provisioned based on your Okta profile. Once you are added to the relevant Okta group, your signature will be automatically 'pushed' to your email clients, including both Gmail and Outreach.

## How to Verify Your Signature

**Log in to Gmail/Outreach:** Your signature may appear as a "code block" or a placeholder ([[+]]) in your compose window.
**Send a Test:** Send an email to a personal address or a colleague.
**Check Rendering:** The recipient will see the fully rendered HTML signature.
**Note:** In your "Sent" folder, you will see the code block; this is expected behavior as the stamping happens post-send.

## Requesting Changes or Support

**Updating Your Profile Data:** If your title, phone number, or department is incorrect in your signature, please create an issue [here](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/work_items). Changes typically sync to Opensense within 24–48 hours.

## Technical Support

If your signature is not rendering or you encounter "Access Denied" errors when logging into the Opensense dashboard:

- Verify you are using the GitLab-dedicated SSO URL.
- Reach out in the #mktgops Slack channels.
- Create an issue for the [MOPs team folder](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/work_items).

## Marketing Campaign Banners

If you have a request for a new banner campaign or want to exclude a specific department from a banner, please open a Marketing Operations [Issue](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/work_items/new?type=ISSUE&description_template=opensense-banner-campaign).

## Resources

**Signature Setup Guides: Outreach, Gmail, and Mobile:** [Here](https://docs.google.com/document/d/1x1_MwJ_gtbStYBiNiasZY6kCaTbXKq43ylHvpA26WFo/edit?tab=t.0)
