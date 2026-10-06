---
title: Renewals Managers - How we do it
---

View the Renewals Manager handbook pages:

- [Home](/handbook/customer-experience/renewals-managers/home) - Information about the organization.
- [What we do](/handbook/customer-experience/renewals-managers/what) - Information about what tasks and activities renewals managers perform.

Renewals Managers --> visit the internal handbook [page](https://internal.gitlab.com/handbook/sales/go-to-market/renewals/) and [Highspot](https://gitlab.highspot.com/items/65831c38686f413428300ccd?lfrm=isd.9) for more information.

---

## Execution: Establishing fundamental excellence

Renewals managers (RMs) execute a series of activities across a specifically defined customer renewal lifecycle. These activities are both internal and customer facing. We seek excellence in performing the fundamental tasks of renewals management.

## Renewals lifecycle

The renewals team organizes it's coverage of a customer subscriptions around particular key stages during a customers journey through the renewal process. During each stage we prescribe specific activities that encourage renewals managers to deliver distinct, stage relevant customer outcomes.

| Time Frame | Renewals Stage | Customer Outcomes (Qualitative)                                          |
|-------|--------|-------------------------------------------------------------------------------------|
| Month 1    | 1. Deploy      | Customer welcomed/back, environment set-up/affirmed, startup issues identified/triaged, licenses utilized |
| Month 2    | 2. Activate    | The majority of licenses are being utilized, customer is enabled to enter the adopt stage |
| Month 3,4,5,6 | 3. Adopt | Customers encouraged to optimize platform, early risk signals identified/mitigated, subscriptions show high utilization |
| Month 7    | 4. Advocate    | Customers identifying expansion opportunities, verbalizing advocacy        |
| Month 8,9 | 5. Expand      | Customers have evaluated needs for more subs, up-tiering                     |
| Month 9,10| 6. Prepare     | Comfortable and starting the commercial portion of the renewal lifecycle     |
| Month 11   | 7. Quoted      | Timely access to an accurate quote                                          |
| Month 12   | 8. Signing     | Signatures on quote, PO raised/sent (when necessary)                         |
| Month 12   | 9. Closed Won  | Entitled, shown gratitude, and equipped for day zero success                  |

## Renewals policies

To build and maintain an efficient, fair, and high impact renewals organization, we have adopted the following policies and processes to describe our engagement with field sales, partners and customers.

## Rules of engagement

- **Growth opportunities**
  - First order business is handled by Account Executives
  - Customer add-ons are identified by Renewals Managers, and primarily managed by Account Executives (exceptions made for timing risk to customers environment; risk to experience)
  - Connected-new opportunities are handled by Account Executive
- **Renewal opportunities**
  - Customer true-ups are handled by Renewal Manager
  - Renewals Managers do not waive true-ups
- **Channel opportunities**
  - We respect the incumbency of partners unless a lack of action by the partner puts a customers environment at risk
- **Opportunity Coverage**
  - Renewals managers primary focus is managing renewal `ATR` ; coverage for new business and add-on's `growth NetARR` should default to the account executives team

## Late renewals management

Our management philosophy regarding the expectations of booking renewals is simple - always timely and always accurate.

- **Timely**:
  - It is expected that a renewal opportunity be closed-won or closed-lost by the `subscription renewal date`.
  - We close-lost opportunities when we have full confidence that the customers will not renew (we don't use sales automation to close opportunities)
- **Accurate**:
  - *No pushing*: We do not manipulate the close date to influence personal performance metrics (i.e. pushing churning opportunities into the next quarter/year)
  - *No detrimental pulling*: We do not pull opportunities forward into quarters for the purpose of personal performance metric effect if it results in compression (i.e. offering a discount for an early contract reset to improve a quarters performance)
  - *Corresponding subscriptions*: We book opportunities that correspond, together (aka SaaS and Self-Managed migrations are booked at the same time)

## Compensation

## Churn and Contraction – Order Type Guide for Renewals

### Purpose

This section explains how Contraction and Churn are represented in Order Type, specifically for Renewals Managers, and how to interpret common scenarios in Salesforce.

---

### Order Type values relevant to Renewals

From a Renewals perspective, the key Order Type values are:

- Growth – Renewal or add-on that maintains or increases ARR.  
- Contraction – Renewal or add-on that reduces ARR but the customer is still active.  
- Churn - Partial – Final outcome when some subscriptions in the Account Family churn but others remain.  
- Churn - Final – Final outcome when all subscriptions in the Account Family churn (no remaining active subs).  
- PS / Other – Non-recurring or technical transactions that typically do not impact ARR (for example, certain credits or one-time services).

(See the Sales Terms Glossary for full Order Type definitions.)

---

### How Renewal opportunities flow through Order Type

For Renewal opportunities:

1. While open or Closed Won with negative Net ARR  
   - Order Type = Contraction.  
   - This indicates a downsell: lower ARR than the prior term, but the customer is still present.

2. When moved to Closed Lost with negative Net ARR  
   - Order Type transitions from Contraction to:
     - Churn - Final if the Account Family has no remaining active subscriptions after the associated subscription end date.  
     - Churn - Partial if the Account Family still has one or more active subscriptions (for example, one entity or product line churns while others remain).

3. Positive or flat Net ARR renewals  
   - Positive Net ARR → Growth (renewal upsell).  
   - Net ARR = 0 but recurring amount remains > 0 → Growth (flat renewal).

4. Non-standard / PS-only renewals  
   - Some technical or non-recurring renewals (for example, PS-only corrections) may be classified as PS / Other.

---

### Common Renewal scenarios

Scenario 1 – Standard positive renewal (upsell)

- Renewal opp with Net ARR > 0 compared to prior term.
- Expected Order Type: Growth.

Scenario 2 – Flat renewal

- Renewal opp with Net ARR = 0, but recurring amount remains > 0.
- Expected Order Type: Growth (flat renewal).

Scenario 3 – Downsell but still a customer

- Renewal opp with Net ARR < 0 (for example, seat reduction or downgrade).
- While open or Closed Won:
  - Expected Order Type: Contraction.
- The customer is still active; this is not full churn.

Scenario 4 – Full churn

- Renewal opp with Net ARR < 0, moved to Closed Lost, and there are no remaining active subscriptions under the UPA after the subscription end date.
- Expected Order Type: Churn - Final.

Scenario 5 – Partial churn

- Renewal opp with Net ARR < 0, moved to Closed Lost, but there are still active subscriptions under the UPA.
- Expected Order Type: Churn - Partial.

---

### How Renewals Managers should use Order Type

Use Order Type to:

- Distinguish:
  - Healthy / expanding renewals (Growth),
  - At-risk / downsell renewals (Contraction),
  - True churn (Churn - Partial / Churn - Final).
- Understand:
  - Where churn is driven by a single subscription vs the entire hierarchy.
  - Where Renewal outcomes may require follow-up with Sales Ops or Sales Commissions (for churn exceptions, etc.).

Order Type is not the only input to compensation; for churn exceptions, follow the Sales Commissions process.

---

### If Order Type looks wrong on a Renewal

1. Check core renewal fields  
   - Type (Subscription Type) – Confirm the opportunity is a Renewal, not mis-labeled as New Business or Add-On.  
   - Net ARR – Confirm Net ARR is correct relative to the prior term.  
   - Opportunity Category – Confirm it is a standard Renewal category (not Decommission, Credit, etc.).

2. Check the customer state  
   - Are there still active subscriptions after this renewal’s end date?  
     - If yes and the renewal is Closed Lost with negative Net ARR → expect Churn - Partial.  
     - If no and the renewal is Closed Lost with negative Net ARR → expect Churn - Final.

3. Check timing  
   - If the opportunity’s status or related subscriptions changed very recently, allow up to 24 hours for nightly jobs to update account-level rollups that influence churn classification.

4. When and how to escalate  
   - If, after the above checks, Order Type still looks incorrect:
     - Open a Sales Operations case using the Request Support process in Salesforce:  
       - From the Renewal Opportunity, click Request Support.  
       - Select Sales Operations as the team.  
       - Choose the appropriate Request Type (for example “Order Type” or “Opportunity Data Review”).  
       - In the description, include:
         - Prior term ARR and new ARR,
         - What you believe the correct Order Type should be,
         - Subscription details (for example, which subs are still active).

This follows the Requesting Internal Support in Salesforce workflow and the Go To Market RoE guidance that Order Type changes should be requested via Request Support → Sales Ops on the opportunity.

## Churn Exceptions

- Churn exceptions are possible, but not guaranteed. Each circumstance will be considered independetly. Some common scenarios considered for churn exceptions are:
  1. Misrepresented or temporary Churn/Contraction
  - a. Near-term add-on contraction (true up negotiations, budget optimizations)
  - b. Subscription migration and consolidations - where we can prove that users simply moved to another subscription (not-merged) on another opportunity, or to another account
  - c. System errors (non-standard contract resets that may net incorrectly, incorrectly merged opps)
  1. Strategic Churn/Contraction
  - a. Change in GTM (direct to indirect) and the associated margin event that results in contraction
  - b. Change in term length (must pass approvals)
  1. Protected Churn/Contraction
  - a. Large/Influential Tier 3 deals where a churn event encompasses more than 10% of a Renewals Managers overall quarterly target may be considered
  - b. Recent account transition churn/contraction - opps that have been recently acquired as a result of account transition

- Timing: Have all exceptions submitted by the first two days of the new quarter.
- Threshold: Consider the amount of churn/contraction - small renewals in these scenarios should be balanced with the amount of effort to find/submit them (i.e. submitting a 200 dollar opp may take more time than it's worth)

- Submission
  - Here are the steps to request a review of your churn exception:
  1. From the Opportunity you are seeking an exception, select the "Request Support" button and enter the following information:
  2. Team: Renewal Ops
  3. Request Type: Churn Exception Request
  4. Migrated Opportunity: The "new" opportunity where the ATR was transferred or that helps justify the exception request
  5. Exception Request ARR: How much ARR are you requesting as exempt?
  6. Justification: Please provide any information on why you are seeking an exemption
  7. After you have entered the above information, select Submit Case.
  8. Follow the link to your new case and using Chatter, mention your manager for approval.

-Checking the Approval Status
  -Once you have submitted the Exception Request, Renewal Ops will put the status as "Work in Progress".
  -Exceptions will be reviewed on the first business day of the next month. For example, a churn exemption that was submitted in February and had a close date in February will be reviewed on March 1.
  -If the "new" opportunity where the justification was provided is not Closed Won, we will change the status to "In Progress: Blocked"
  -If your request is approved, the boxes "Leadership Approval" and "Compensation Approval" will be checked.
  -If your request is not approved, there will be notes in the Ops/Compensation Notes field. We typically also engage via Chatter on the Case. Chatter should not be used on the Opportunity.
  -Once all approvals are complete and Sales Comp has been notified, your case will move to Closed.

## Metrics

The renewals organization puts a focus on execution through a balanced series of metrics.

## Primary Metrics

- Renewal Rate (% of dollar)
   `[Won ARR Basis (for Clari)]` / `[ARR Basis (for Clari)]`
- On-time renewal rate (% of dollar) (# of opps)
  `Close date` >= `subscription renewal date`
- Lifecycle Activity Completion Rate
  `Completion Rate` >= `Lifecycle Tasks Completed/Number of Lifecycle Tasks Assigned`  

## Secondary Metrics

- Growth NetARR (%)  - everything but first-order business
`[Comp] Net ARR (growth)`

## Tertiary Metrics

- Opportunity health: Next steps completion, stage progression, activity execution
- Under management: $ and # opps in each tier (0,1,2,3)
- Compression: Average discount
- Scaling: % of business executed through partners
- Closing Velocity: Average quote to close time (measured by stage progression)
- Customer Satisifacation: NPS, CSat scores
