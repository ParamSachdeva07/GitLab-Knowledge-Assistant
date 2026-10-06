---

description: "This page covers the factors to consider for customer health, guidelines for selecting the appropriate rating, communication guidelines, CSM responsibilities and instructions for the account triage issue creation."
title: "Customer Health Assessment and Management"
---

View the [CSM Handbook homepage](/handbook/customer-experience/csm/) for additional CSM-related handbook pages.

---
This page covers the factors to consider for customer health, guidelines for selecting the appropriate rating, communication guidelines, CSM responsibilities and instructions for the account triage issue creation.

See [Customer Health Scoring](/handbook/customer-experience/customer-health-scoring) for an overview on how customer health scoring is defined and calculated at GitLab.

## CSM Responsibilities

The CSM is responsible for coordinating with all relevant parties to develop a plan to address account risks. Typically, this will involve the account team and communication group ([Communication Guidelines](/handbook/customer-experience/csm/health-score-triage/#at-risk-communication-guidelines)), as well as other relevant stakeholders such as Product Managers, marketing, executive, or engineering team members to develop and deliver the plan to address the risks. The CSM then drives execution of the strategy and is responsible for logging regular updates. When the risks have been addressed bringing the customer to a healthy / green status, the account team can agree to move the account out of triage.

## Tracking Customer Health

CSMs can use Red, Yellow, and Green to reflect their sentiment of a customer's health. Below is an explanation about how to think about a customer's health.

### Green

Customer is very likely to renew and/or expand with no known or assumed risk of downsell or churn. Customer's experience: engagement, adoption and experiences are as expected or better than expected, delivering value and outcomes as appropriate the customer's stage in their journey. Examples:

- Progressive adoption of GitLab use cases as defined by their success plan, considering their stage in their journey
- Alignment with stakeholders who can drive desired outcomes
- Regular communication and engagement in meetings
- Positive feedback on the product and experience and/or high scores on NPS surveys
- Leveraging support services as defined by creation of tickets (1-5 tickets per month)
- Interest in providing feedback and engaging with GitLab through other programs and events (e.g., Commit, [Advisory and Executive customer programs](/handbook/marketing/growth-marketing/growth-community-programs/#executive-advisory-board-eab-program))

### Yellow & Yellow "Needs Triage"

Potential risk or significant lack of information leading to uncertainty. Indicates challenges to overcome, with a lower risk of churn or downsell. Customer's experience: engagement, adoption and/or experiences are lower than expected, risking GitLab's ability to deliver customer value and outcomes and/or drive future revenue growth. Examples:

- Slow, delayed, or blocked adoption of GitLab use cases in support of the customer's success plan
- Customer lacks definition of goals or success criteria
- High number of support cases, critical / blocker product issue(s), or poor experience based on the customer's expectations
- Lack of engagement, responsiveness or participation in meetings and/or events
- Loss of sponsor or champion due to change of role or organization or acquisition
- Lack of adoption of releases (self-managed only) where they are more than a major release behind the current release
- Not leveraging technical support services or has a large number of cases and/or high severity cases (6-15 tickets per month, or no ticket(s) opened after being advised by the CSM that Support is the best path to resolution for an issue(s))
- Poor experiences with Support, Professional Services or another part of GitLab
- Working with a single contact at a company (single-threaded).

There might be well understood reasons within the account team why a customer is flagged as Yellow within the current phase of the customer lifecycle. If the CSM decides that corrective actions and follow up from team members outside of the CSM group is required the CSM must create an [At Risk Timeline Entry](/handbook/customer-experience/csm/health-score-triage/#health-update-template).

### Red

Specific, known risks to account retention or upcoming opportunity, or overwhelming lack of information, such as unresponsiveness leading up to renewal. Customer's experience: engagement, adoption and/or experiences are significantly lower than expected where issues are blocking GitLab's ability to deliver expected value, outcomes, or positive experiences as defined by the customer.
Examples:

- Potential risk of contraction or churn (even if this is unconfirmed)
- Lack of alignment with stakeholders who can drive outcomes...
  - [Economic Buyer](/handbook/sales/meddppicc/#economic-buyer)
  - [Champion](/handbook/sales/meddppicc/#champion)
  - Key [Personas](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/user-personas/)
    - [Cameron (Compliance Manager)](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/user-personas/#cameron-compliance-manager)
    - [Delaney (Development Team Lead)](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/user-personas/#delaney-development-team-lead)
- Product does not deliver expected value or outcomes as defined by success plan
- No or low product adoption with no progression
- Communication of poor sentiment
- Lack of any engagement
- Significantly poor experiences with Support or Professional Services
- Significant number of support tickets (16+ per month)

### Will Churn

Very rarely, a customer reaches a point at which it is accepted by the account team and leadership that a customer will contract or churn. As Gainsight does not support a 'grey' color (or any color outside of the standard green to red health scoring), the `will churn` lifecycle stage can be applied in 360º Attributes.

In order for a customer to move to the `will churn` stage, the following must be completed:

1. All options discussed during the health reviews have been exhausted
1. CSM discusses it with their manager and gets agreement on moving to `will churn`
1. RM/AE marks the opportunity as `Will Churn` or `Will Contract`
1. CSM updates the Lifecycle Stage in Gainsight C360 > Attributes > Lifecycle Stage to `Will Churn`

## Reporting and Viewing Customer Health

Use the `Customer Health` (CSM Portfolio Dashboard) report to view the health of every measure for your customers in one single view.

To view Timeline entires where the CSM Sentiment was updated:

1. Go to Global Timeline
1. Filter by Sentiment = Green, Yellow, or Red
1. Apply any other specific filters (CSM Name, Timeline date, etc)

## Gainsight Responsibilities

CSMs are responsible for keeping Gainsight up to date regarding all of their account risks.

### Frequency of Health Update Timeline Entries

CSMAs must regularly log a health update for customers, regardless of their risk status, but there are different requirements for frequency depending on if a customer is at risk or not.

1. If customer is not at risk:
   1. **Monthly** Health Timeline updates
1. If customer is red/at-risk:
   1. **Weekly** Health Timeline updates
      - Entry should include progress towards risk mitigation over the past week and plans for the upcoming week.

![GitLab At-Risk Customer Process](/CSM_At-Risk_Customer_Process.png)

### Health Update Template

For each assigned CSM/A account, submit a monthly health update regardless of current account health status to your customer's timeline. This is separate than your At-Risk Timeline Entries if the account is Red or Yellow. A template has been created and can be accessed through the following steps:

1. In the account timeline, log a `Health Update` activity
2. Select `Apply Template`
3. Click `Monthly Health Update` to apply
4. Make sure to add the accurate `CSM Sentiment` as this will update the account status in Gainsight

Here is a sample of the template with examples:

> *Current State*
>
> - **Usage: Customer is currently utilizing 1,868 of 2,300 users. The remaining users are cycled for onboarding, offboardings, and guest users.**
> - **DAP Journey: Customer is interested in DAP but is evaluating other AI tools as well and not sure how to begin.**
> - **Sentiment: Customer is actively working towards evaluating Ultimate\Duo with increased executive buy in.**
>
> *Considerations*
>
> - **Customer has recently acquired several other organizations that have slowed GitLab and Partner conversations around expansions.**
> - **Our core contact at Customer has been added to the internal AI board to evaluate and recommend AI options for the company. This board reports directly to the executive team.**
>
> *Watch Items*
>
> - **Renewal conversations are beginning soon. There is still tension from the previous multi year renewal.**
> - **Customer is evaluating competing AI tools and has several DAP feature requests they would want implemented.**
> - **Main contact has taken over another organization and will take advantage of enablement starting in the next month or so.**
>
> *Next Steps*
>
> - **DAP Workshop**
> - **Executive alignment call**
> - **Generation of quote options for Premium renewal and renewal including Duo\Ultimate**
>
> *If DAP is Running Cold*
>
> - **Why are they blocked: Teams are having a hard time of where to start with DAP, specific use cases for their teams**
> - **Mitigation Strategy: Hold hands-on DAP demo reviewing foundational agents, custom agents, and customer specific external agents**
> - **Help needed: Demo assistance, potentially leadership call to align on roadmap**

#### Health Update for Resolution of Risk

When a customer's risk has been mitigated and they are no longer at risk, the CSM creates a Health Update timeline entry communicating:

1. The customer is no longer at risk
1. Key details about what mitigated the risk
1. What comes next
1. CSM Sentiment updated to reflect current health status

This is to ensure that everyone is aware of the latest details, and that we affirmatively communicate risk resolution across our systems and teams.

Here is a sample entry for risk resolution:

> CUSTOMER X is no longer at risk. We resolved their upgrade and infrastructure challenges through engagement with Support and Professional Services, and they are now on the latest GitLab version with infrastructure tested using GPT. We are now focused on CI adoption, in line with the agreed-upon success plan.

### When to open an Account Escalation

If a CSM has marked an account as [Red](/handbook/customer-experience/csm/health-score-triage/#red) and further assistance from Product, Support or Managers+ is needed, open an [Account Escalation](/handbook/customer-experience/csm/escalations/).

### Risk impact definitions

1. **Customer Churn** - fully churn the account
1. **Tier Downgrade** - move down tiers
1. **Seat Churn** - reduce license seat count
1. **Customer Sentiment** (Impact Unknown) - customer is unhappy and the impact isn't quantified
1. **Competitor** - any competitive intelligence we might be up against
1. **Stage Name** - stage impact, for example, product deficiencies, direction, or needs.

### Risk reason definitions

#### Lack of adoption

Customer never adopted the product or specific features so they did not get value. This can be because of organizational silos or lack of internal resources. If they didn't adopt because they didn't see / experience value, it should be Product Gap

#### Product Value / Gaps

Prospect or customer used the product and features (i.e., trial, POV, or purchased product), but did not see the value. The product did not meet requirements of the customer. This can also be a prospect where they did not experience perceived value

#### Product Quality / Availability

Prospect or customer used the product and features (i.e., trial, POV, or purchased product) though they did not meet the prospect or customer's needs or expectations. This can be defects, poor performance, or uptime/availability issues. Includes both self-managed and SaaS products

#### Lack of Engagement / Sponsor

We lost or were never able to get engagement with the prospect or customer team. The champion / sponsor left, changed responsibility, or became unresponsive. We were never able to re-establish connection with a new sponsor or champion

#### Loss of Budget

The prospect or customer lost budget due to business contraction, change of priorities, reduction of employees, or other. This was not a competitive loss.

#### Corporate Decision

Due to management decision or policy, the prospect or customer chose a different product but not because of product gaps, adoption, etc. This would be a top-down decision (e.g., ELA, decision to commit to a single provider)

- **Other** - other company issues that contribute to a blocker for the renewal

### Mitigation Strategies

For CSM guidance on mitigating risk, please see the [Risk Types, Discovery & Mitigation Strategies](/handbook/customer-experience/csm/risk-mitigation) page.

## At Risk Communication Guidelines

The following are guidelines on who to notify when an account is yellow or red. Please make sure the following people are notified with the respective customer health ratings.

### Yellow Health Rating

- Account Team (i.e. Account Executive and Solution Architect)
- Regional CSM Manager
- CSM Director (all non-Public Sector customers) or Director of Customer Success Public Sector (for Public Sector customers)

### Red Health Rating

- Include the list above as well as…
- Area Sales Manager and Regional Director
- Vice President of Customer Success

## Related Processes

[Customer Success Escalations Process](/handbook/customer-experience/csm/escalations/)
