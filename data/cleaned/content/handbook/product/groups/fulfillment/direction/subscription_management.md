---
title: "Fulfillment: Subscription Management direction"
description: "The Subscription Management team at GitLab is focused on delivering an easy, informed, and reliable experience for customers to purchase GitLab products, manage their subscriptions, and view billing details and contacts."
---

**Last updated**: 2025-10

## Mission

Deliver frictionless, self-service experiences that enable customers to independently manage their entire subscription lifecycle - from purchase through renewal - with confidence, clarity, and ease.

## Strategic Priorities

1. Empower customers to purchase new products and make changes to their subscriptions without requiring assistance from GitLab support or sales teams.
1. Automate subscription management with features like Quarterly Subscription Reconciliation (QSR) and Auto-Renewal to streamline processes for customers and internal teams.
1. Continuously improve the [Customers Portal](https://customers.gitlab.com/) to ensure a seamless and intuitive experience for all customer types, including self-service, sales-assisted, and channel partner customers.
1. Given the global commerce functionality, support compliance, legal, and tax related efforts to safeguard revenue and meet regulations.
1. Expand Customers Portal access beyond current customers to include free trial users and channel partners, creating additional conversion opportunities and payment channels.

## Target audience

- **Direct customers** purchasing GitLab products and subscriptions
- **Billing account managers** responsible for managing subscriptions and payments
- **Channel partner customers** who need visibility into their subscriptions
- **GitLab sales and customer success teams** who support customers through the subscription lifecycle

## Key focus areas

### 1. Self-Service Purchase and Subscription Management

**What we're solving:** Customers should be able to independently purchase GitLab products and modify their subscriptions throughout their lifecycle without requiring sales assistance, through a unified and seamless purchase experience.

#### Current State

- New purchases and subscription expansions (add quantities, upgrades) in the Customers Portal for select products
- Subscription visibility for all products
- Quarterly reconciliation (QSR) for automated seat true-ups
- Credit card payment processing
- Invoice viewing and payment with credit card

#### Problems and Opportunities

- **Incomplete product coverage:** Not all GitLab products are available for self-service purchase, and the current checkout doesn't support complex product rate plan configurations. This forces customers to engage sales for routine transactions and restricts bundling strategies. Expanding self-service availability and [supporting product rate plans with multiple charges](https://gitlab.com/groups/gitlab-org/-/epics/17869) will increase transaction volume, reduce sales friction, and enable sophisticated pricing and bundling.
- **Fragmented purchase experiences:** Purchase flows in the Customers Portal lack a consistent user experience and scalable technical implementation. The process for buying Premium or Ultimate differs significantly from purchasing products like Storage or Compute, as well as from upgrading or renewing. This inconsistency increases the engineering team's workload in building and maintaining these various flows. [Unifying all purchase flows in the Customers Portal](https://gitlab.com/groups/gitlab-org/-/epics/12199) will enhance scalability and improve the user experience.
- **Single-product limitations:** GitLab is continuously adding new products and add-ons for customers to buy. However, our current self-service purchase flows require customers to make separate transactions for each product, creating friction in the buying process when customers need multiple products. [Enabling customers to purchase multiple products in a single transaction](https://gitlab.com/groups/gitlab-org/-/epics/18001) will simplify procurement and increase transaction value.
- **Payment method constraints:** Credit card-only payments exclude customers who prefer or require alternative methods and create collection risk with QSR failures. Introducing additional payment methods (ACH, PayPal, etc.) and [migrating to Zuora Payment Forms](https://gitlab.com/groups/gitlab-org/-/epics/19622) will expand customer reach and reduce payment collection risk.
- **Future-dated subscription visibility:** Customers with future-dated subscription changes cannot see or manage their current active subscription because the portal incorrectly displays future changes as if they're currently in effect. [Improving subscription card display to properly handle current vs future subscription states](https://gitlab.com/groups/gitlab-org/-/epics/18002) will provide separate views so users can access both what they have today and what's coming next.

#### Key Metrics

- Self-service adoption rate (by transaction type)
- Purchase completion rate
- Self-service revenue trending
- Support ticket reduction
- Customer satisfaction with purchase experience

### 2. Self-Service Renewal

**What we're solving:** Simplifying and streamlining the renewal process to increase on-time renewals, reduce involuntary churn, and give customers confidence in their subscription continuity.

#### Current State

- Manual renewal and auto-renewal available via Customers Portal for all major use cases
- Renewal flow supports all renewable products and can combine multiple rate plans for the same product
- Annual true-up for seat overages processed at renewal
- Toggle auto-renewal on/off (cancel subscription)
- Renewal email notifications sent via Zuora and Customers Portal

#### Problems and Opportunities

- **Limited renewal window and late auto-renewal timing:** Current 15-day renewal window and last-day auto-renewal attempts create risk of service disruption when payment issues arise. [Extending to a 30-day renewal window](https://gitlab.com/groups/gitlab-org/-/epics/18665) and attempting auto-renewal several days earlier will provide buffer time to resolve payment issues and reduce involuntary churn.
- **Lack of proactive renewal blocker visibility:** Several auto-renewal blockers are identifiable before the renewal attempt (expired credit card, subscription configuration issues, unpaid overages), but customers only receive email notifications with no visibility in the Customers Portal. Displaying renewal blockers and alerts in the portal will enable proactive resolution and reduce auto-renewal failures.
- **Limited pre-renewal modification options:** Customers cannot modify their subscriptions or pre-configure changes before auto-renewal occurs, forcing them to either disable auto-renewal or accept unwanted charges and modify after renewal. [Enabling customers to modify subscriptions and configure changes in advance that automatically apply on their scheduled auto-renewal date](https://gitlab.com/groups/gitlab-org/-/epics/6970)  will reduce friction and improve customer satisfaction.
- **Lack of renewal pricing visibility:** Customers cannot preview what their renewal will include before the renewal window opens, creating uncertainty about upcoming charges. [Providing clear visibility into renewal pricing and subscription details in advance](https://gitlab.com/gitlab-org/customers-gitlab-com/-/issues/3510) will increase transparency and reduce surprise charges.
- **Confusing renewal communications:** Customers often find upcoming renewal emails confusing, as they tend to be irrelevant, unclear, and lacking actionable information. [Transitioning subscription renewal emails from Zuora to CustomersDot](https://gitlab.com/groups/gitlab-org/-/epics/9303) will enable us to control email frequency and customize email content.
- **Auto-renewal failures:** A subscription set to auto-renew may fail to renew for several reasons: expired credit card, payment failure, unpaid overages, or issues calculating overages. Analyzing data on the number of subscriptions that failed to auto-renew and developing a tactical plan to increase the success rate of auto-renewals will reduce involuntary churn and improve customer retention.

#### Key Metrics

- Number of on-time and early renewals
- Auto-renewal adoption rate
- Auto-renewal success rate
- Self-service renewal completion rate
- Customer satisfaction with renewal process

### 3. Self-Service Promotional Discounts

**What we're solving:** Enable GitLab to leverage promotional discounts as a customer acquisition and retention strategy while maintaining a seamless self-service experience.

#### Current State

- No self-service promotional discount capabilities
- Discounts require sales assistance

#### Problems and Opportunities

- **Lack of self-service promo capabilities:** Customers cannot apply promotional discounts during self-service purchases, requiring manual intervention or sales assistance. [Building scalable discount promo functionality](https://gitlab.com/groups/gitlab-org/-/epics/14931) and [enabling self-service via multi-use promo codes](https://gitlab.com/groups/gitlab-org/-/epics/18600) will reduce friction and increase conversion rates.
- **Limited discount flexibility:** Cannot override discount percentages per promotional campaign, restricting marketing strategies. [Enabling campaign-specific discount override capabilities](https://gitlab.com/gitlab-org/customers-gitlab-com/-/issues/11962) will allow for more targeted and effective promotional strategies.
- **Narrow product coverage:** Promotional discounts are not available for all products (GitLab Duo Pro, Ultimate, etc.) or purchase flows (renewal, upgrade, add-ons). Expanding promo discount support across all products and purchase flows will enable comprehensive promotional campaigns and improve customer acquisition and retention.

#### Key Metrics

- Discount redemption rate
- Conversion rate lift from promotional campaigns
- Increase in First Orders

### 4. Self-Service Billing Account Management

**What we're solving:** Enable customers to easily access and manage their billing accounts with multiple account managers for streamlined billing and subscription administration.

#### Current State

- Users can only belong to one billing account
- Self-service management of multiple billing account managers on a billing account
- Multiple billing accounts may exist for the same .com group
- Contact Us page with Account Executive contact information and direct support links

#### Problems and Opportunities

- **Single account membership limitation:** Approximately 9% of customers are associated with multiple billing accounts, but users are currently restricted to single account membership. This prevents access to legitimately purchased services and blocks proper billing account manager workflows. [Enabling a single CustomersDot user to have multiple billing account memberships](https://gitlab.com/groups/gitlab-org/-/epics/8986) will remove barriers and improve account accessibility.
- **Low billing account manager adoption:** Many billing accounts have only a single billing manager, creating support burden when the primary contact is unavailable. [Increasing adoption of billing account managers](https://gitlab.com/groups/gitlab-org/-/epics/18530) through awareness campaigns and improved workflows will reduce support tickets and ensure business continuity.
- **Fragmented billing for same group:** Multiple purchases for the same .com group may result in separate billing accounts, creating administrative complexity and confusion. Consolidating all purchases for the same .com group under a single billing account will simplify billing management and improve customer experience.
- **Opportunity to align with GitLab Organization model:** As GitLab develops its [Organization model](https://docs.gitlab.com/user/organization/), there's an opportunity to align billing accounts with this structure. Creating a single entity that represents billing across an entire company will make it easier to associate purchases in the Customers Portal with the Organization they belong to in GitLab, simplifying the connection between purchases and organizational structure.

#### Key Metrics

- Support ticket volume reduction (access-related tickets)
- Billing account manager adoption rate (% of accounts with 2+ managers)
- Customer self-service success rate (billing account managers added without support intervention)
- Reduction in support tickets related to account management

## Future Direction

As we continue to evolve our subscription management capabilities, we're exploring opportunities that extend beyond our current focus areas. This section will continue to expand as new strategic opportunities emerge.

- **Expanding Customers Portal Access:** Explore opportunities to expand portal access beyond current paying customers to include free trial users (providing trial visibility and conversion touchpoints) and [channel partners](https://gitlab.com/groups/gitlab-org/-/epics/19449) (enabling invoice access and credit card payments). Success will be measured by increased portal usage across user segments, improved trial-to-paid conversion rates, and reduced payment friction for partners.

## Reference to Quarterly Priorities, Epics, Issues and Boards

Some content is confidential and therefore won't be visible.

- Quarterly Priorities

  - FY25-Q2: [Fulfillment section](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/6895), [Subscription Management group](https://gitlab.com/gitlab-com/gitlab-OKRs/-/issues/?sort=updated_asc&state=all&label_name%5B%5D=group%3A%3Asubscription%20management&label_name%5B%5D=FY25-Q2&first_page_size=50)
  - FY25-Q3: [Fulfillment section](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/8268), [Subscription Management group](https://gitlab.com/gitlab-com/gitlab-OKRs/-/issues/?sort=updated_asc&state=all&label_name%5B%5D=group%3A%3Asubscription%20management&label_name%5B%5D=FY25-Q3&first_page_size=50)
  - FY25-Q4: [Fulfillment section](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/9504), [Subscription Management group](https://gitlab.com/gitlab-com/gitlab-OKRs/-/issues/?sort=updated_asc&state=all&label_name%5B%5D=group%3A%3Asubscription%20management&label_name%5B%5D=FY25-Q4&first_page_size=20)
  - FY26-Q1: [Fulfillment section](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/10382), [Subscription Management group](https://gitlab.com/gitlab-com/gitlab-OKRs/-/issues/?sort=updated_asc&state=all&label_name%5B%5D=group%3A%3Asubscription%20management&label_name%5B%5D=FY26-Q1&first_page_size=20)
  - FY26-Q2: [Fulfillment section](https://gitlab.com/gitlab-com/gitlab-OKRs/-/work_items/10663), [Subscription Management group](https://gitlab.com/groups/gitlab-org/-/epics?sort=created_date&state=opened&label_name%5B%5D=group%3A%3Asubscription%20management&label_name%5B%5D=Fulfillment%20-%20Interlock&label_name%5B%5D=Fulfillment%20FY26-Q2&first_page_size=20)
  - FY26-Q3: TBD

- [Fulfillment Roadmap > Subscription Management](https://gitlab.com/groups/gitlab-org/-/roadmap?state=all&sort=end_date_asc&layout=QUARTERS&timeframe_range_type=THREE_YEARS&label_name%5B%5D=Fulfillment+Roadmap&label_name%5B%5D=group%3A%3Asubscription+management&progress=COUNT&show_progress=true&show_milestones=false&milestones_type=GROUP)
- All Subscription Management epics

  - [List of epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=group::subscription+management)
  - [Organized epics board](https://gitlab.com/groups/gitlab-org/-/epic_boards/31408?label_name[]=group%3A%3Asubscription%20management)

- All Subscription Management issues

  - [List of issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=group%3A%3Asubscription%20management&first_page_size=20)
  - [Organized issues board](https://gitlab.com/groups/gitlab-org/-/boards/4282426?label_name[]=group%3A%3Asubscription%20management)
