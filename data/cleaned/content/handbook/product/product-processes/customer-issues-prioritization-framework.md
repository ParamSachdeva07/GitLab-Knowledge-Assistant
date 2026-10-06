---
title: "Customer Issues Prioritization Framework"
---

## Why This Framework Exists

Product teams at GitLab receive customer feedback through multiple channels—support tickets,
sales conversations, CSM interactions, and direct customer issues. Without a consistent
prioritization system, critical customer needs can get lost in the noise, and teams struggle
to align on what matters most for customer success.

This framework provides a shared language for GitLab team members to communicate customer
impact to product teams, ensuring that issues blocking sales, risking renewals, or representing
committed deliverables receive appropriate attention.

## Where to provide feedback

The preferred method for providing customer feedback on issues is to use an **internal comment** following the process [described below](#quick-start). Internal comments protect customer privacy and prevent sensitive business information from being publicly visible.

If a **public comment is necessary** (such as in Support workflows where the customer expects to see the comment), use the [Feedback template](/handbook/product/product-management/#feedback-template) instead.

## Quick Start

To prioritize a customer issue, add an **internal note** comment to the issue with the
appropriate label and context. Internal notes are made available only to GitLab Team Members
and help ensure customer sentiment is not unnecessarily exposed.

Here are the labels available:

- **Ultimate:** `~Ultimate::Blocker` or `~Ultimate::Retention` or `~Ultimate::Fast Follow`
- **Premium:** `~Premium::Blocker` or `~Premium::Retention` or `~Premium::Fast Follow`
- **DAP:** `~DAP::Blocker` or `~DAP::Retention` or `~DAP::Fast Follow`
- **Ultimate:** `~Ultimate::Blocker` or `~DAP::Retention` or `~DAP::Fast Follow`

Here are examples:

**Blocker Example:**

```markdown
~DAP::Blocker

Cannot close opportunity [internal link](https://gitlab.my.salesforce.com/0061234567890) without SAML group sync capability. Customer requires automatic provisioning based on IdP groups for their deployment. No workaround available that meets their security requirements.
```

**Retention Example:**

```markdown
~Ultimate::Retention

Customer ([internal link](https://gitlab.my.salesforce.com/0061234567891)) has flagged this as a renewal blocker renewing in July 2025. Performance degradation with large monorepos is preventing adoption across their engineering org. They are actively evaluating alternatives.

Customer has provided specific metrics showing 15+ minute wait times for pipeline starts.
```

**Fast Follow Example:**

```markdown
~Premium::Fast Follow

Committed to customer (SFDC: https://gitlab.my.salesforce.com/0061234567892) during renewal conversation that we would deliver enhanced audit log filtering by end of Q3-2025. Customer accepted renewal based on this commitment.

This capability allows them to meet compliance requirements without manual log exports. Current workaround is acceptable but creates operational overhead.
```

## How It Works

### Prioritization Labels

Customer-facing teams (Sales, Customer Success, Support, Solutions Architecture) add product-specific scoped labels **in their internal note comments** on issues that directly impact customers:

- **`ProductName::Blocker`** - Cannot sell customer the SKU without this capability
- **`ProductName::Retention`** - Cannot keep customer on this SKU that they've already purchased without this capability
- **`ProductName::Fast Follow`** - Yes we can sell or keep this customer, but they are expecting committed delivery on this capability

### Adding Labels to Comments

**Who can add labels:**

- Solutions Architects
- Customer Success Managers
- Support Engineers
- Account Executives
- Product team members

**When to add labels:**

- During technical evaluations when gaps are identified
- When customers report issues affecting their workflows
- During renewal conversations where specific capabilities are blocking expansion
- When commitments are made regarding future delivery

**How to add labels:**

1. Create an **internal note** comment (not a public comment)
2. Include the appropriate scoped label in your comment
3. Link to the customer record in Salesforce (or other external system)
4. Describe the business impact without including customer names or revenue figures

**Required context in your comment:**

- The prioritization label (e.g., `DAP::Blocker`)
- Link to customer account (Salesforce opportunity or account)
- Description of business impact
- Affected customer segment/tier when relevant

**Critical privacy requirements:**

- **Always use internal notes** - Do not post customer details in public comments
- **Never include customer names** in the issue comment
- **Never include Net ARR, contract values, or revenue figures** in the issue comment
- **All sensitive information must remain in the linked external system** (Salesforce, etc.)
- Reference customers generically (e.g., "Customer", "Strategic customer", "Enterprise prospect")

### What Each Label Means

#### Blocker

Cannot sell customer the SKU without this capability.

**Key question:** Is this capability a hard requirement to close the deal?

**Examples:**

- Customer requires specific compliance certification not available
- Integration with required enterprise system doesn't exist
- Security control is mandatory for customer's deployment model
- Missing API capability prevents customer's critical automation workflow

#### Retention

Cannot keep customer on this SKU that they've already purchased without this capability.

**Key question:** Will the customer churn or downgrade without this capability?

**Examples:**

- Customer explicitly raised issue as renewal blocker
- Competitive gap driving active evaluation of alternatives
- Missing functionality preventing adoption across purchased seats
- Performance or reliability issue causing business disruption

#### Fast Follow

Yes we can sell or keep this customer, but they are expecting committed delivery on this capability.

**Key question:** Did we make a commitment to deliver this capability to close or retain the customer?

**Examples:**

- Feature commitment made during sales process with expected timeline
- Roadmap item discussed in renewal conversation with delivery expectations
- Enhancement requested by customer with agreement on future delivery
- Capability gap where workaround exists but customer expects proper solution

## Product Team Responsibilities

Product teams use these labels as input to their planning processes, not as strict ordering mechanisms. Labels signal customer urgency and business impact, which teams balance against technical dependencies, strategic priorities, and overall product direction.

### Triage Expectations

A triage bot monitors issues with customer prioritization labels in comments. If an issue with a prioritization label remains without a milestone or planning label after 5 business days, relevant team members receive a reminder to ensure the issue receives proper consideration during planning.

This automation ensures customer-flagged issues receive timely review without mandating specific outcomes—product teams retain full autonomy in final prioritization decisions.

## Guidelines and Best Practices

**Always use internal notes.** Customer prioritization comments must be internal notes to protect customer privacy and sensitive business information.

**Protect customer information.** Never include customer names, revenue figures, or contract values in issue comments. All sensitive details should remain in linked external systems like Salesforce.

**Blocker means deal-blocking.** Reserve this label for situations where the sale genuinely cannot proceed without the capability. If a workaround exists that allows the customer to purchase, it's not a blocker.

**Retention means churn risk.** Use this label when a customer has explicitly indicated they cannot continue with the SKU, not just when they've requested a feature during a renewal conversation.

**Fast Follow means we made a commitment.** Only use this label when GitLab team members have set delivery expectations with the customer. General feature requests without commitments should not receive this label.

**Document business context clearly in your internal note.** Product teams need to understand customer impact to make informed decisions. Include account links, customer tier/segment, and specific details about commitments made—but keep names and revenue in external systems.

**One label per comment.** If an issue affects multiple products, choose the primary product area and add separate comments for each product if necessary. If customer impact is uncertain, discuss with product team before adding a label.

**Update as context changes.** If a workaround is identified, a deal closes without the capability, or customer priorities shift, add a new internal note comment with updated context or clarification.

## Feedback and Evolution

This framework will evolve based on team usage and product feedback. Submit questions or suggestions through:

- `#unified-gtm-product-feedback` Slack channel
- Create an issue in the [handbook project](https://gitlab.com/gitlab-com/content-sites/handbook) and assign `@poffey21`

*See also: [Product Development Flow](/handbook/product-development/how-we-work/product-development-flow/), [Working with Product](/handbook/product/product-processes/)*

## Resources

- [Issue Prioritization Framework Working Group](/handbook/company/working-groups/issue-prioritization-framework/)
- Slack channel: `#wg_issue_prioritization`
- [Top-level epic](https://gitlab.com/groups/gitlab-com/-/epics/928)
- [Unfiltered (private) playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0KrKoeXjf5Bdtapu9Cl3T7gI)
- [Case study on the "Cost of Delay / Duration" methodology](https://gitlab.com/gitlab-com/Product/uploads/fb6e33af006253cb7420689f83fcf644/black-swan-farming__3_.epub)
