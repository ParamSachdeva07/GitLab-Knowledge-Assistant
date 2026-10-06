---
title: "Fulfillment: Utilization direction"
description: "The Utilization group aims to ensure customers have access to consumables usage data (storage, compute minutes, and transfer units) so that they can make the optimal decisions for their business needs."
---

## Fulfillment Utilization Overview

The Utilization group aims to ensure customers have access to consumables usage data (storage, compute minutes, and transfer units) so that they can make the optimal decisions for their business needs.

## Vision

_What is our long-term solution concept? Analogy: what will it look like at the top of the mountain?_

Consumables usage would provide predictability to our customers through transparent usage visibility, suggested usage management recommendations, and purchasing directions. Our sales teams would be empowered to have customer discussions about growth with detailed usage data as a foundation for that conversation.

## Feature Overview and Maturity

_What features are the Utilization group responsible for and how mature are they?_

**Legend**:

- 🙂 **Minimal**: Available and works for a small number of use cases. Some transparency for internal teams.
- 😊 **Viable**: Available and works for the majority of use cases. Some transparency for internal teams.
- 😁 **Complete**: Fully functional for all eligible use cases. Full transparency for internal teams.
- 😍 **Lovable**: Glowing reviews from external and internal users.

| Feature | Maturity | Description |
|------------|:--------:|-------------|
| Storage Usage Visibility | 😊 Viable | Customers understand how much storage they are using and what projects/file types are contributing to that usage. |
| Storage Quota | 😊 Viable | Customers understand if they are within the storage limits threshold and how to take action (remove, add more, set storage limits)  |
| Compute Minutes Usage Visibility | 😊 Viable | Customers understand how many compute minutes they are using |
| Quota of Compute Minutes | 😊 Viable | Customers understand if they are running out of compute minutes and how to buy more  |
| Transfer Usage Visibility | Not yet available | Customers understand how much transfer they are consuming |
| Quota of Transfer | Not yet available | Customers understand if they are running out of transfer units and how to buy more  |

## 1-year Plan

_Where are we focused over the next 12 months to make meaningful steps towards achieving our vision and increasing feature maturity?_

### 1-year Vision

In a year from now, we hope to have:

1. ✅ Provided users with [MVC storage visibility](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/1769)
2. ✅ Create a common layout for [Usage Quotas pages](https://gitlab.com/groups/gitlab-org/-/epics/7176). This reduced code duplications, improved developer experience by having all the code of the page in one directory,mitigated future code duplication, and enabled Usage Quotas for all tiers and editions.
3. Complete [compute minute limit](https://gitlab.com/groups/gitlab-org/-/epics/13989) adjustment for GitLab.com Free Tier.

### Roadmap

1. Complete [compute minute limit](https://gitlab.com/groups/gitlab-org/-/epics/13989) adjustment for GitLab.com Free Tier.

### Possible Future Opportunities

| What is the work to do? | Why are we considering doing it  |
|---------|--------|
| Storage Usage [Visibility & Enforcement](https://gitlab.com/groups/gitlab-org/-/epics/10940) | Over time, a GitLab namespace can generate a significant amount of storage. This includes activities like pushing code, creating new containers and packages, running CI/CD jobs, and more. This storage increases the cost of operating a GitLab. |
| Improve the [Self-Managed Storage Experience](https://gitlab.com/groups/gitlab-org/-/epics/11423)         |  Self-managed users need a UI that helps them achieve the jobs related to storage usage visibility and leveraging the storage limit [feature](https://docs.gitlab.com/ee/administration/settings/account_and_limit_settings.html#repository-size-limit). They do not need see UI related to storage enforcement limits.     |
| Transfer Visibility & Enforcement | Over time, a GitLab namespace can have significant transfer usage. This increased the cost of operating GitLab. |
| [Paid Tier Storage Enforcement](https://gitlab.com/groups/gitlab-org/-/epics/8380) | Over time, a GitLab namespace can generate a significant amount of storage. This includes activities like pushing code, creating new containers and packages, running CI/CD jobs, and more. This storage increases the cost of operating a GitLab.  |
| Support [pricing & packaging innovation for storage product](https://gitlab.com/groups/gitlab-org/-/epics/11774) | Current storage limits are set with one size per plan, which does not account for the different needs that a namespace with a higher seat count may have, for example, 20 seats vs 2000 seats.  |
| Support [consumption pricing and packing innovation](https://gitlab.com/gitlab-org/fulfillment/meta/-/issues/1541) for our consumables products. | Seat pricing doesn’t scale with the value of automation. Software increasingly automates manual processes. The more successful a product is, the fewer user seats a customer needs. |

## Additional Information

### Q&A

| Question | Answer |
|---------|-------------|
| What type of customers does Utilization serve? | - SM & SaaS Self-service customers <br>- SM & SaaS Sales assisted customers <br>- SM & SaaS Channel Partners and their customers  |
| What customer personas are Utilization solving for? | Our customers fit the [buyer persona](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/buyer-persona/) and may play a different role in the decision-making and purchasing process depending on their company size and their role.   |
| What customer segment is Utilization focused on? | - For SMB and mid-market companies: [The application development manager](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#app-dev-avery) needs to have visibility into usage across their teams and be able to control usage in a way that fits their company preferences/processes/budget. <br> - For large or enterprise company: [The release and change management director](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/buyer-persona/#release-rory) is concerned with accurate billing and being able to make purchasing decisions based on usage information. |
| What internal teams does Utilization serve? | - [Support](/handbook/support/) <br>- [Customer Success](/handbook/customer-experience/) <br>- [Sales](/handbook/sales/)  |
|What is the Utilization group not responsible for?|The Utilization Group relies on calculations provided by other teams as part of building the right reporting and visualization for customers and admins. However, Utilization is not responsible for the collection or raw calculations of this underlying data. Specifically, Utilization relies on Enablement teams to provide accurate data around things such as: <br>1. Project-level storage calculations (git repo + git LFS)<br>2. Namespace storage calculation: git repo, LFS, artifacts, container registry, etc. <br> 3. Compute minutes |
