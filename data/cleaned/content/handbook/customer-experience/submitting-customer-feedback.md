---
title: "DAP Customer Feedback Framework"
---

## DAP Customer Feedback Framework

The **DAP Customer Feedback** platform is GitLab's [centralized tool](https://dap-customer-feedback-6c19a4.gitlab.io/) for collecting feature requests and enhancement ideas about the Duo Agentic Platform (DAP) from customers and GitLab team members. Each submission automatically becomes a GitLab Issue, gets routed to the right team, and can be tracked as it moves through the development process.

> **Important:** This system is for **feature requests and enhancements only**. Bug reports should be submitted through Support Channels.

---

### Who Should Use This?

| Role | How to Contribute |
|------|-------------------|
| **Customer Success Managers** | Submit feature requests on behalf of customers to ensure their ideas are heard in product planning. |
| **Solutions Architects** | Share capability gaps and desired enhancements discovered during customer implementations. |
| **Sales Team Members** | Submit feature requirements and enhancement ideas that come up during sales conversations. |
| **Support Engineers** | Consolidate and submit customer enhancement requests (not bugs) so product and engineering teams can see patterns. |
| **Internal Users** | Submit feature requests and enhancement ideas based on your own experience using DAP. |

---

### Bugs vs. Feature Requests

#### Submit Bugs Through Support Channels

If you've found a bug or issue with DAP functionality, do **not** use this form. Instead:

1. Submit the bug through Support Channels

2. Follow the support team's escalation process

#### Submit Feature Requests Here

Use [this form](https://dap-customer-feedback-6c19a4.gitlab.io/) for new capabilities and enhancements.

---

### How It Works

#### Step 1 — Share Your Feature Request

Complete the [feedback form](https://dap-customer-feedback-6c19a4.gitlab.io/) with details about the feature you'd like to see, the use case it solves, and why it matters. Include relevant context so the team can fully understand the impact.

#### Step 2 — Route to the Right Team

Your feature request gets routed to the appropriate GitLab Group based on the category you select during submission.

#### Step 3 — Track Progress

Your request is automatically converted into a GitLab Issue. You'll receive a link where you can follow discussions, add comments, and stay updated as the team evaluates it. You can also view all [open submissions here](https://gitlab.com/groups/gitlab-org/-/work_items?sort=created_date&state=opened&label_name%5B%5D=customer_feedback_form&first_page_size=20).

---

### Key Features

| Feature | Description |
|---------|-------------|
| **GitLab Login Required** | Secure authentication ensures requests are trackable and linked to a real person. |
| **Attachments & Context** | Upload screenshots, mockups, links, or other documentation to provide context. |
| **Structured Forms** | Consistent questions ensure we capture the information needed to understand your request. |
| **Collaborative Feedback** | Discuss details with the team directly on the resulting GitLab Issue. |

---

### Tips for Good Feature Requests

- **Be specific about the outcome** — Instead of "improve reporting," say "Add ability to schedule daily email reports with custom charts"

- **Explain the problem it solves** — What pain point or limitation does this address?

- **Provide context** — Explain why this matters and how it impacts your workflow

- **Include examples** — Screenshots, mockups, or step-by-step descriptions help clarify the idea

- **Link related items** — Reference GitLab issues, documentation, or customer conversations where relevant

- **Think about the user** — Consider how customers would use this feature and what benefits it provides

---

### Frequently Asked Questions

**What counts as a feature request?**

- Any new capability, product improvement, expanded functionality, better workflow, documentation enhancement, or idea for how DAP could solve problems more effectively. Do *not* submit bug reports or issues where existing features don't work correctly — those go through Support Channels.

**Is this guaranteed to be implemented?**

- No, but your request is valued and will be considered during product planning. Prioritization depends on customer needs, technical feasibility, strategic alignment, and roadmap planning.

**What if I need to submit sensitive information?**

- All submissions become GitLab Issues visible to the relevant team. Avoid sharing customer identifiable information, API keys, or highly confidential details. If your request involves sensitive information, discuss it separately with your Customer Success Manager or directly with the team.

---

### Customer Feedback Triage Process

When feature requests are submitted, Product Managers triage them using labels to create transparency about what's being built, what's being declined, and why.

#### Triage Labels

##### Customer Feedback Label

The `customer_feedback::new` label is automatically assigned on submission. Product Managers then update it to one of the following:

| Label | Meaning |
|-------|---------|
| `customer_feedback::new` | Just received (auto-assigned) |
| `customer_feedback::accepted` | Approved as a feature to build |
| `customer_feedback::wont-do` | Decided not to pursue |

##### Managing Duplicate Issues

We manage duplicates through a daily job that identifies and merges duplicate issues into a primary issue.

| Label | Meaning |
|-------|---------|
| `duplicate::primary` | The issue being kept and tracked |
| `duplicate::merged` | The issue that was closed and consolidated into the primary |

The merge process works as follows:

- Copy the duplicate issue's URL into the internal notes of the primary issue.

- Add any labels from the duplicate that are not already on the primary issue.

- If the primary issue is closed, reopen it and reset the customer feedback label to "new."

- Label the duplicate issue `duplicate::merged` and close it.

##### Priority & Status

For accepted requests, Product Managers assign a `priority::` label (starting at `priority::1`) to indicate urgency, and update the **Status field** on the issue to reflect progress through the development workflow.

In addition, for accepted requests:

- If the `DAP Key Account` **or** a `priority::1` or `priority::2` label is used, Product Managers **will also add** a `quarter::` label and a `milestone::` label.

- For all other accepted requests, Product Managers are advised to add either a `Milestone Backlog` label or another milestone label if they are confident of which milestone the change will go to.

##### Won't-Do Labels

When a request is declined, one of the following labels is added to explain why:

| Label | Meaning |
|-------|---------|
| `wont_do::out-of-scope` | Outside the scope of our product |
| `wont_do::not-core-product` | Doesn't align with our core product vision |
| `wont_do::low-priority` | Low customer demand or niche use case |
| `wont_do::better-alternatives` | Customers can accomplish this with external tools |
| `wont_do::security-risk` | Would weaken our security |
| `wont_do::design-risk` | Would create architectural problems |
| `wont_do::platform-limitation` | Technical constraints make implementation infeasible |
| `wont_do::vendor-dependency` | Requires external service reliance |
| `wont_do::maintenance-burden` | Support costs outweigh benefit |
| `wont_do::backwards-incompatible` | Would break existing functionality |
| `wont_do::technical-debt` | Solving this creates more problems than it solves |
| `wont_do::duplicate-feature` | Functionality exists elsewhere in product |
| `wont_do::product-vision` | Misaligned with roadmap and product direction |
| `wont_do::performance-concern` | Negative impact on performance |
| `wont_do::regulatory-blocker` | Legal or compliance reasons prevent implementation |

#### Triage Examples

| Scenario | Labels & Fields |
|----------|--------|
| Accept the feature request | `customer_feedback::accepted`, `priority::1`, Status: Validation Backlog, `milestone::backlog` |
| Accept a key account or high-priority request | `customer_feedback::accepted`, `DAP Key Account` or `priority::1`/`priority::2`, `quarter::`, `milestone::` |
| Decline the feature request | `customer_feedback::wont-do`, `wont_do::low-priority` |
| Feature currently in development | `customer_feedback::accepted`, `priority::1`, Status: In Dev, `milestone::` |
| Feature shipped | `customer_feedback::accepted`, `priority::1`, Status: Complete, `milestone::` |
