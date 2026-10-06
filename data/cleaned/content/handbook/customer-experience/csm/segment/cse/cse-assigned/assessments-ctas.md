---
title: "CSE Assigned: Health Assessments & CTAs"
description: "How to run health assessments and use CTAs to track follow-up work for CSE Assigned accounts."
weight: 40
---

## Health assessments

- **Cadence:** one per account per rolling 90 days (the first quarter of CSE Assigned operation is used to complete the initial full-pass across the entire book).
- **Mandatory sections:** one TL;DR sentence, then an executive overview covering account basics (product/tier/seats/renewal date), usage summary, support, customer interactions, risk assessment, and proposed next steps.
- Health assessments are **internal-facing only**, they are not customer-facing.
- The output lives in the **Gainsight Timeline** as a Health Update entry, it is not automatically a CTA.
- **Suggested method:** run an automated data pull (today via [this script](https://gitlab.com/gitlab-com/customer-success/csmerm/customer-success-engineering/scale-cse/-/tree/main/CSE%20Health%20Assessment?ref_type=heads)), review and augment with your own account knowledge gained from customer interactions and AE/RM catch-ups, then post the TL;DR + executive summary as a Health Update in Gainsight.
- **If usage data isn't in Gainsight:** check whether the instance is set to "Production," ask the customer directly if needed, and use engagement frequency, interactions, and support tickets as signal in the meantime. Reach out in `#gainsight-users` if something looks technically broken.

## CTAs

- CTAs are **not a performance metric**. They exist to structure work and give portfolio visibility.
- A CTA is only opened when a health assessment surfaces follow-up work, or a customer requests guidance on a specific topic. A healthy account with no follow-up needs no CTA.
- Use the **Lifecycle CTA** type for adoption follow-ups. If the follow-up includes a series of several light questions, the recommendation is to do one general CTA, however if the topics are wider and more complex, and require more work, create one CTA per topic. Close with documented outcomes (topics covered, recommendations with links, customer's next actions).
- Use the **Escalation CTA** type for escalations, following the [CSM escalation process](/handbook/customer-experience/csm/escalations/):
  1. Risk surfaces: health assessment or signal identifies an issue.
  2. Immediate flag: notify AE/RM and CSE manager; don't wait.
  3. Open Escalation CTA: track in Gainsight following the CSM escalation process.
  4. End-to-end ownership: the assigned CSE manages through resolution, with the account team in the loop throughout.
- Customer-introduction CTAs are recommended, not mandatory.

## CTA types at a glance

Beyond Lifecycle and Escalation above, a few other CTA types show up on assigned accounts. Some are CSE-opened, some are system-generated and just need a CSE response:

| Type | Opened by | Use it for |
|---|---|---|
| **Lifecycle** | CSE | Non-risk adoption follow-up |
| **Escalation** | CSE (via SFDC case) | Customer in a challenging situation. Tracked in Gainsight under the At-Risk CTA type |
| **At-Risk / Save Play** | CSE | Renewal risk: a Red Review save-play assignment, low adoption, exec change, or budget-risk signals. If an Escalation CTA already exists for the account, add to it rather than opening a parallel Save Play |
| **Activity** | CSE | Personal follow-up items and reminders. Internal-only, not part of portfolio reporting |
| **DAP** | System | Auto-created on a new DAP commitment or near-zero credit burn; CSE owns activation on assigned accounts alongside AE/RM |
| **Onboarding** | System | Auto-created for net-new First Order accounts; CSE is the primary technical contact through kickoff |
| **Digital Journey** | System | Created from a Calendly or digital-touchpoint trigger; review if it lands on an assigned account and escalate to a CSE-led CTA if needed |
| **CSE Case** | System | Support case routed to the CSE queue from Salesforce; if it turns into a real escalation, open a separate Escalation CTA rather than reusing this one |

## Prioritizing which accounts to assess first

Highest ARR + forecast churn/contraction + near-term renewals + worrying adoption patterns, then work down.
