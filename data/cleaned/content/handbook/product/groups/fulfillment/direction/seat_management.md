---
title: "Fulfillment: Seat Management direction"
description: "The Seat Management group handles user assignment of purchased seats and add-ons and provides visibility into seat usage across namespaces"
---

**Last updated**: 2025-08

## Mission

Enable customers to optimize their GitLab investment through intuitive seat assignment, proactive cost management, and seamless enterprise user provisioning.

## Overview

The Seat Management group is responsible for the Seat Cost Management and User Management product categories, providing customers with comprehensive tools and features needed to efficiently manage user access, control seat costs, and integrate GitLab with existing enterprise identity systems.

By focusing on these areas, the Seat Management group aims to eliminate billing surprises, reduce administrative overhead for user management, and enable organizations to scale their GitLab usage efficiently while maintaining security and cost control.

## Vision

_What is our long-term solution concept? Analogy: what will it look like at the top of the mountain?_

Today, seat assignment, management, user provisioning, and enterprise user controls present opportunities for improvement. Examples of how customers are impacted by these challenges:

- Customers currently manage seat assignment manually for add-ons like Duo Pro and Duo Enterprise, and base plans (Premium/Ultimate) derive seats from user roles rather than explicit assignment, leading to less predictable resource allocation.
- Organizations lack comprehensive visibility into seat usage and proactive controls to prevent unexpected overages during budget planning.
- While enterprise user management through SCIM, SAML, and LDAP works well, there are opportunities to better integrate these capabilities with cost control features like Restricted Access (Block Seat Overages) to enable broader adoption.
- Current role-based seat consumption can create unexpected billing scenarios when users transition between roles.

To solve these problems we are going to:

1. **Develop a seat assignment model (SAM).** We'll move away from users immediately consuming a subscription seat when being added to a group or project based on their role. With SAM, group owners and admins assign users to seat types first, and these seat types then control what roles users can have in groups and projects. This will move us away from users being able to unintentionally transition between roles, which can have billable and compliance consequences.
2. **Prevent unintended overages.** Today, all customers are charged for seat overages. In the future, the default experience will require customers to purchase seats before they can be assigned to users.
3. **Enhance enterprise user management integration with cost controls.** We'll improve how SCIM provisioning, SAML Group Sync, and LDAP synchronization work with Restricted Access (Block Seat Overages), enabling more customers to adopt these cost control features while maintaining seamless user lifecycle management.

These changes will not be universally felt by customers:

- For some customers that are optimizing for frictionless addition of new users, they will be able to continue to interact with GitLab as they do today while also appreciating enhancements like a consolidated users view in GitLab.com and optimized billable calculations. If they want more controls for cost, they can opt-in to those.
- However, for most customers who are optimizing for cost control, we will be providing them with additional controls and visibility for cost management.

### 1-year Roadmap

_Where are we focused over the next 12 months to make meaningful steps towards achieving our vision and increasing feature maturity?_

[Further Details](https://internal.gitlab.com/handbook/product/fulfillment/seat-cost-management/) (Not Public)

| What is the work to do? | Why are we doing this work? |
|---------|--------|
| Implement [Seat Assignment Model](https://gitlab.com/groups/gitlab-org/-/epics/13684) | Provide customers with intuitive, self-service seat assignment for Premium and Ultimate plans and Enterprise Agile Planning add-on, reducing friction and improving resource allocation efficiency. |
| [Complete Restricted Access feature](https://gitlab.com/groups/gitlab-org/-/epics/12452)| Restricted Access is available but has known issues, particularly with user management protocols (SCIM/SAML/LDAP). |
| [Enhance Dormant User detection & management](https://gitlab.com/groups/gitlab-org/-/epics/18322) | Help customers optimize their seat utilization by identifying and managing inactive users, directly impacting cost savings. |

Seat Management [FY26 Roadmap](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/2379).

### Possible Future Opportunities

| What is the work to do? | Why are we considering doing it  |
|---------|--------|
| Streamlined Duo Seat Management |  Integrate Duo seat assignment more seamlessly with existing enterprise user management workflows. |
| Predictive Seat Planning | Provide forecasting capabilities to help customers anticipate future seat needs based on usage trends. |

All Seat Management group epics and issues are organized in the [group's HQ epic](https://gitlab.com/groups/gitlab-org/-/epics/18073).

## Target audiences

The Seat Management group serves:

- Self-managed, GitLab.com and GitLab Dedicated self-service customers
- Self-managed, GitLab.com and GitLab Dedicated sales-assisted customers
- Self-managed, GitLab.com and GitLab Dedicated channel partners and their customers

Our customers fit the [buyer persona](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/buyer-persona/) and may play a different role in the decision-making and purchasing process depending on their company size and their role.

- For SMB and mid-market companies: [The application development manager](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#app-dev-avery) needs to have visibility into usage across their teams and be able to control usage in a way that fits their company preferences/processes/budget.
- For large or enterprise companies: [The release and change management director](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#release-rory) is concerned with accurate billing and being able to make purchasing decisions based on usage information.

Internal teams we serve:

- [Support](/handbook/support/)
- [Customer Success](/handbook/customer-experience/)
- [Sales](/handbook/sales/)

## Feature Overview and Maturity

_What features are the Seat Management group responsible for and how mature are they?_

|  Feature | Maturity | Description |
|-----------|:--------:|-------------|
| Seat Usage Visibility | 😊 Viable | Customers understand how many seats are being used and by whom |
| Billable Users Calculation | 🙂 Minimal | Customers understand how many billable seats are being used, by whom, and when they are being used |
| Seat Limits | 😊 Viable | Customers understand if they are within the user limits threshold and how to take action (remove, add more, set seat limits) |
| Manage Non-billable Promotions| 🙂 Minimal | Customers can control when non-billable users become billable |
| Dormant User Management | 😊 Viable | Customers can identify and manage inactive users to optimize seat utilization |
| Duo Pro & Enterprise Seat Assignment | 😊 Viable | Streamlined assignment and management of GitLab Duo Pro seats |
| Enterprise Agile Planning Seat Assignment | 🙂 Minimal | Assignment of EAP seats through Planner role (limited control mechanisms and not self-service purchasable) |
| Seat Assignment Model (SAM) | 🌱 Planned | Unified seat assignment experience for Premium and Ultimate base plans |
| SCIM User Provisioning | 😊 Viable | Automated user creation, updates, and deprovisioning through identity providers |
| SAML Group Sync | 😊 Viable | Automatic role assignment and group membership based on identity provider groups |
| LDAP Group Sync | 😊 Viable | Hourly sync of user and group information from LDAP directories |

**Legend:**

- 🌱 **Planned**: Not yet implemented, but on our roadmap.
- 🙂 **Minimal**: Available and works for a small number of use cases. Some transparency for internal teams.
- 😊 **Viable**: Available and works for majority of use cases. Some transparency for internal teams.
- 😁 **Complete**: Fully functional for all eligible use cases. Full transparency for internal teams.
- 😍 **Lovable**: Glowing review from external and internal users.
