---
title: "Success Plans"
description: "A success plan is a roadmap that connects a customer's desired business outcomes to GitLab solutions. It is a living document, developed by the CSM."
---

View the [CSM Handbook homepage](/handbook/customer-experience/csm/) for additional CSM-related handbook pages.

---

## New to success plans? Start here

A success plan is the roadmap for achieving a customer's business objectives using GitLab. It is the foundation of every CSM engagement — built with the customer, and maintained throughout the relationship.

There are three things to understand before you build one:

| Concept | What it is |
|---|---|
| **Objective** | A customer business outcome — with a clear goal, measurable success criteria, owners, and a timeline. |
| **Initiative** | An action plan that supports an objective. Focused on the "how." |
| **Verifiable Outcome (VO)** | An objective that is formally tracked, customer-validated, and reported quarterly. Must be [SMART](#what-makes-a-good-vo). |

**Ready to build?** Jump to [Building your success plan](#building-your-success-plan).

Want the full conceptual introduction to Verifiable Outcomes first? See the video below (GitLab Unfiltered account required):

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/i3n4cMMIJz8" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

---

## Building your success plan

Success plans live in a GitLab customer collaboration group shared with your customer. Objectives are epics. Initiatives are issues. The [Success Plan Viewer](https://success-plan-viewer-c27524.gitlab.io/group) reads directly from this group — no additional tooling or pipeline setup required.

> **Where to create your group:** Customer collaboration groups live in the [account-management](https://gitlab.com/gitlab-com/account-management) group under your region: **Western North America**, **Eastern North America**, **EMEA**, or **APAC**. Ask your CSM manager if you are unsure.

---

### Step 1 — Create an objective epic

Each customer objective is a **GitLab epic** in the customer collaboration group. Use the [objective epic template](#objective-epic-template) to get started quickly.

If you are starting a new objective from scratch, create a new epic directly in the customer collaboration group.

If you already have an existing issue that should be tracked as a VO, promote it to an epic using one of two methods:

**Option A — UI:**

1. Open the issue
2. In the top-right, click **More actions (…)** → **Change type**
3. Under **Type**, select **Epic**
4. Click **Change type**

**Option B — Quick action:**

In a comment on the issue, type the following and submit:

```text
/promote_to Epic
```

Either method creates an epic in the issue's parent group and carries over the title, description, comments, participants, and relevant group labels.

> **Note:** After promotion, verify that all three required labels are present — they may not transfer if they were not already applied to the original issue.

Every objective epic requires:

**Three labels — all must be present or the epic will not appear in reporting:**

| Label | What to set |
|---|---|
| `~SP Objective` | Always required — no value needed |
| `~SP Objective::Status::` | `Not Started` · `On Track` · `Watchpoint` · `Concern` · `Closed Success` |
| `~Verifiable Outcome::` | `Proposed` · `Accepted` · `Delivered` · `Verified` |

**One use case label:**
`~UseCase::` — pick one: `AI` · `CD` · `CI` · `Dedicated` · `Developer Experience` · `Infrastructure` · `Other` · `Plan` · `SCM` · `Security`

**Optional labels:**
`~Priority::` (`Low` · `Medium` · `High`) · `~Success Accelerator` (for Success Tier adoption accelerators)

**A due date** — treated as the target completion date in reporting.

**Two required description sections** — use exact headers, as they are parsed by the Success Plan Viewer:

- `## Summary` — What the customer is trying to achieve and why it matters to their business. Write for a stakeholder audience. Optionally add `### Successes` and `### Risks` subsections.
- `## Success Criteria` — Measurable bullet points that define completion.

#### Objective epic template

Copy this into your epic description to start from the right structure:

```markdown
## Summary

[What is the customer trying to achieve, and why does it matter to their business?
Write for an executive stakeholder — focus on business impact, not GitLab features.]

## Success Criteria

- [Specific, measurable condition #1 — include baseline, target, and date]
- [Specific, measurable condition #2]

## Updates

- [Status updates, close objective reason]
```

---

### Step 2 — Add initiative issues

Each initiative is a **GitLab issue** inside the objective's epic. Every initiative issue should have:

- An `## Update` section — current status, progress against success criteria, next steps
- A due date
- At least one assignee (GitLab DRI; add customer-side DRI where applicable)
- A status label: `~SP Initiative::Status::` `Not Started` · `On Track` · `Watchpoint` · `Concern`

For Enablement Plan initiatives, also add `~EP Initiative::Status::` `On Track` · `Watchpoint` · `Concern` · `Proposal`.

---

### Step 3 — Advance the VO lifecycle

Update the `~Verifiable Outcome::` label as work progresses. The SPV dashboard is live data — do not batch updates at quarter-end.

| Stage | Label | When to apply |
|---|---|---|
| **Proposed** | `~Verifiable Outcome::Proposed` | VO identified; drafting internally before customer presentation |
| **Accepted** | `~Verifiable Outcome::Accepted` | Customer aligned on objective, baseline, success criteria, and timeline |
| **Delivered** | `~Verifiable Outcome::Delivered` | Work complete on GitLab's side |
| **Verified** | `~Verifiable Outcome::Verified` | Customer has explicitly confirmed successful completion *(preferred)* |

---

### Step 4 — Close out a completed VO

All three steps are required, in order. Skipping any step causes reporting errors.

1. Set `~SP Objective::Status::Closed Success`
2. Set `~Verifiable Outcome::Verified` (or `::Delivered` if customer confirmation is not available)
3. **Close the epic**

---

## Quarterly VO tracking

VO completion is reported quarterly through the [Success Plan Viewer](https://success-plan-viewer-c27524.gitlab.io/group), which reads live from your customer collaboration group.

**Each quarter, you are responsible for:**

- All active VO epics have the three required labels applied
- Initiative `## Update` sections are kept current — the dashboard is live, not a snapshot
- Lifecycle labels are advanced in real time as work progresses
- Completed VOs are fully closed out before the quarterly reporting deadline

**Add the SPV link to these three places for easy stakeholder access:**

- Gainsight Success Plan Link field (Plan info tab)
- Your internal customer Slack channel topic
- Your customer collaboration project README (customer view version)

---

## What makes a good VO?

A VO must be **SMART**: Specific, Measurable, Attainable, Relevant, Time-bound.

Every VO needs: a **baseline** (where you are today), **success criteria** (how you'll know you're done), **business impact** (in the customer's language), and a **timeline**.

**Within-quarter VO examples:**

| VO | Baseline | Success Criteria | Timeframe | Business Impact |
|---|---|---|---|---|
| Security and engineering leads are equipped to enforce compliance policies in their pipelines | Team has not used Compliance Pipelines; no enforced policy framework in place | Security and engineering leads attend compliance policies workshop; customer confirms understanding of the policy enforcement model and identifies at least one policy to implement | Within the quarter | Gives the team a concrete starting point for enforcing standards; reduces reliance on individual developer behavior for compliance |
| Platform team is actively using DAP capabilities they already own | DAP capabilities are not in use; available promotional credits are undeployed | Top 5 DAP use cases reviewed with the platform team; promotional credits applied or a deployment plan confirmed | Within the quarter | Turns an underutilized purchase into active value; reduces time to first meaningful DAP adoption |
| New development team has their first pipelines running in GitLab | New team of 12 developers has no CI/CD pipelines in GitLab | All 12 developers have at least one pipeline running in their project; team can build and troubleshoot basic pipelines without CSM support | Within the quarter | Unblocks the team from manual deployment steps; establishes the foundation for broader CI/CD adoption |
| Pilot group has hands-on experience with GitLab Duo and a clear next step | No Duo usage in the account; pilot group identified but not yet enabled | Pilot group enabled and has completed at least one use case walkthrough; customer has provided feedback and confirmed whether to expand, pause, or adjust the rollout | Within the quarter | Converts an unknown into a decision; gives the customer a concrete basis for their next Duo investment choice |
| Customer's main branch pipeline failure rate is no longer blocking releases | ~30% failure rate on main branch causing release delays | Pipeline failure rate reduced to under 5%; root cause documented and shared with customer engineering lead | Within the quarter | Restores release velocity; eliminates a recurring source of developer frustration and lost time |

**Discovery tips:**

- Ask open-ended TED questions: *"Tell me about your team's priorities... Explain how... Describe what..."*
- Reference investor reports, press releases, and GitLab case studies to frame business impact
- Use GitLab Duo to test whether your criteria are truly SMART
- The [continuous triage bot](https://gitlab.com/gitlab-com/account-management/continuous-planning-triage/) reviews open objectives weekly and suggests SMART criteria when draft success criteria exist

For additional discovery questions and techniques, see [Questions & Techniques for Success Plan Discovery](/handbook/customer-experience/csm/success-plans/questions-techniques/).

---

## Troubleshooting

### VO not appearing in reports?

| Symptom | Fix |
|---|---|
| Work item is an issue, not an epic | Promote it to an epic |
| Missing `~SP Objective` label | Add it to the epic |
| Missing `~SP Objective::Status::` label | Add the appropriate status value |
| Missing `~Verifiable Outcome::` label | Add the appropriate stage value |
| Epic not closed | Complete all three closeout steps |
| Labels updated but epic still open, or epic closed but labels not updated | Ensure all three closeout steps are done in order |

---

## Success plan lifecycle

Success plans span the full customer journey. Here is where the CSM's role fits in:

| Phase | Who leads | What happens |
|---|---|---|
| **Pre-sales** | SA + AE | Customer objectives are documented and used to demonstrate GitLab value. See the [mutual customer success plan process](/handbook/solutions-architects/processes/customer-success-plan/). |
| **Post-sales / Onboarding** | CSM | CSM reviews objectives, validates accuracy, and adds initiatives for enablement and implementation. Full alignment on what comes next and who owns it. |
| **Ongoing engagement** | CSM | Success plan anchors every [cadence call](/handbook/customer-experience/csm/cadence-calls/) and [business review](/handbook/customer-experience/csm/ebr/). Cadence calls drive week-to-week progress; business reviews assess strategy and surface new objectives. |

---

## Gainsight

GitLab.com is the source of truth for success plans. Gainsight reflects it and enables pattern analysis across the full book of business.

Key customer interactions — calls, meetings, milestone updates — are logged in Gainsight timeline. Objectives created in GitLab are reflected in Gainsight; when closed, they are updated in both.

For detailed guidance on Gainsight workflows, see [Using Gainsight as a CSM](/handbook/customer-experience/csm/gainsight/).

**Phase 1 — Success Plan Viewer (current):** Quarterly VO tracking is available now via the [Success Plan Viewer](https://success-plan-viewer-c27524.gitlab.io/group). No manual Gainsight data entry is required for VO tracking.

**Phase 2 — Gainsight integration (planned):** Full VO reporting within Gainsight is in development. This page will be updated when available.
