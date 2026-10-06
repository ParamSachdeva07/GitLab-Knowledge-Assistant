---
title: Weekend Emergencies - Self-Managed License Request
description: "Support process for Self-managed weekend license emergencies"
category: GitLab Self-Managed licenses
---

## Overview

There are times when a customer submits an emergency support request for a new
license to replace their expired one immediately. But on-call Support Engineers
do not usually have access to CustomersDot, and cannot manually generate licenses.

This workflow describes steps that can be followed by anyone in Support,
regardless of whether they have CustomersDot access, to generate a short-term
temporary Ultimate Trial license to de-escalate a **weekend** emergency.

**NOTE:** This workflow is applicable even if the customer has previously received a
[Sales-generated temporary extension](/handbook/support/license-and-renewals/workflows/self-managed/trials/#how-to-extend-an-expired-or-soon-to-expire-license).

This workflow does not cover SaaS Subscription Emergencies, see [Customer Emergencies Workflow - SaaS License Emergencies](/handbook/support/workflows/customer_emergencies_workflows#saas-subscription-emergencies).

## Scope

License requests for a Self-managed customer with a **paid** plan, where the license period has ended within the last 3 days from the current emergency's date.

## Out of Scope

1. Organizations without a **paid** plan.
1. Prospects.

---

## Workflow

### Step 1: Confirm customer subscription

1. Request from the customer the following screenshots:

    - Admin Area -> Overview -> Dashboard
    - The license page from Admin Area -> License (in newer versions, may say subscription)
1. Add the screenshots to the ticket.

### Step 2: Generate the trial license

The previous Mechanizer-based workflow for issuing temporary self-managed licenses has been **deprecated**. Instead, use the new CustomersDot Admin Support Tool workflow named [Trials For SM](../customersdot/support_tools.md#trials-for-sm)

Use the Legacy `License Trials` tool to:

- Create a legacy trial license with an appropriate **user count**, **plan code**, and **expiry date** for the emergency.
- Please note that the license email will mention a 10-day Trial GitLab License, it is recommended to set the expiry date 10 days from now to avoid confusion.
- Send the license to the requester’s email address (or as otherwise specified in the ticket).
- Add the **Zendesk ticket link** in the form so the action is auditable.

This replaces the old Mechanizer ZenDesk App process; all emergency self-managed trial licenses should now follow the CustomersDot "Trials for SM" workflow.
