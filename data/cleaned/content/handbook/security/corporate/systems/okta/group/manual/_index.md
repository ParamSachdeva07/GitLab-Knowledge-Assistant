---
title: Manual Okta Groups
---

## Overview

Manual groups are those whose memberships are primarily ad-hoc and cannot be automated based on user attributes. Membership can be populated by either manually adjusting in Okta, or eventually by using an Identity Governance and Administration (IGA) tool like Lumos.

## When to Use Manual Groups

Manual groups should be used for:

* **App membership:** Apps like Figma may be useful for any team member at GitLab. By using a manual group, we can allow team members to request access to what they need, and gain approval through our IGA tool, Lumos
* **Project-based teams:** Cross-functional project teams that don't align with organizational structure
* **Temporary access:** Time-limited groups for contractors, consultants, or special initiatives
* **Exception cases:** Users who need access outside their normal organizational attributes
* **Custom business groups:** Groups that combine users based on non-standardized criteria (For example: "Product Launch Team," "Executive Leadership," "Budget Approvers")

## When NOT to Use Manual Groups

**If it can be automated, it should be automated.** Manual groups create maintenance burden and risk of stale memberships.
Avoid manual groups if the membership can be defined by Workday attributes such as:

* Division, or Department
* Country, Company, or Location
* Management Level or User Type
* Any combination of the above

## Naming Conventions

Manual groups should generally follow application-specific naming patterns from the [Okta Group Nomenclature:](/handbook/security/corporate/systems/okta/group/nomenclature/)

Examples:

* app.figma.collab
* app.zendesk.customer_support.admins
* app.google.kickoff_team_planners
