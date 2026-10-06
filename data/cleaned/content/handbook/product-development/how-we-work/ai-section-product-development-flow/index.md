---
title: AI Section Product Development Flow
description: Cross-functional product development workflow process, ownership and labeling.
---

## Overview & philosophy

Engineering, Product, and Design in GitLab's AI organization work together to turn ideas into customer value. Three principles guide how we collaborate.

We ship fast without sacrificing quality by keeping teams small and cross-functional, running tight cycles, and holding a high bar on first drafts. Customer 0 and design partners validate quality before we roll out broadly.

We operate with an ownership mindset. The people closest to the work make the decisions, and the team that builds a feature stays accountable through rollout and into production.

We measure success by outcomes for the customer: adoption, retention, reliability and value measured through time saved and impact.

### Customer outcomes

Every team's work ladders to one of four customer outcomes. They define what GitLab AI delivers and guide prioritization and roadmap decisions.

1. Ship with higher quality and velocity: Developers are more productive in the tools they already use, and what they ship is better.
1. Automate with confidence: Users can launch long-running agentic workflows and trust them to complete reliably without supervision.
1. Expand capacity: AI takes on work teams couldn't get to before, including continuous analysis, comprehensive review, and routine tasks that previously required manual effort.
1. Build and compose: Customers and partners can build for their specific context and connect GitLab to their stack.
1. Trust and operate: Customers can trust what runs, understand what happened, and scale with predictable cost and quality.

### Value signals

We measure whether a customer outcome is being realized through four signals. A customer who is blocked will show up negatively across all of them

- Adoption: Customers pick up and use the capability we shipped.
- Retention: Customers keep using it over time.
- Time to value: Customers reach a successful outcome quickly.
- Reliability: The capability behaves predictably in production.

## Functional team composition

AI functional teams are small and narrowly scoped. Each team is a partnership between engineering, product, and design. 

- The PM owns the problem, the JTBD (Jobs-to-be-Done), the success criteria, and the customer relationship. 
- The EM owns the delivery date, dependencies and technical strategy and architecture.
- Design owns the experience. 

The PM, designer, and engineer align on the outcome up front, then move independently. Most decisions are made on the spot by whoever owns them. The three coordinate deliberately when a decision changes the shape of what we're building.

Team composition, slack channels and a link to the team's charter which outlines its mission, customer outcomes, success metric, scope, and current bets can be found on the [Product Categories Handbook page](/handbook/product/categories/).

## How we work together - the workflow

| Step | Owner | Description |
|---|---|---|
| **1. Vision and planning** | Product, curated with the trio | Each team maintains a single source of truth for the problems it is solving, each mapped to one of the four customer outcomes. When a team picks up work, it should be clear what is happening and how it ladders to an outcome. Although flexibility to be reactive matters we hold ourselves accountable to ensuring we're always delivering on these customer outcomes. |
| **2. Prioritization** | Product, with trio inputs | Design and engineering each bring their own backlogs into prioritization alongside feature work. Before each planning cycle, Design maps quality gaps to customer outcomes and brings that list into planning. Engineering does the same for maintenance and tech debt. A fixed 15% of each milestone is reserved for each, so neither backlog compounds over time. Bugs are prioritized by severity per the org-wide [Issue Triage SLO guidelines](/handbook/product-development/how-we-work/issue-triage/#severity-slos). `~severity::1` and `~severity::2` bugs follow their SLO timelines regardless of the 15% allocation, given their active risk. Lower-severity bugs (`~severity::3` and `~severity::4`) without an SLO breach may be planned within the 15% maintenance/tech-debt pool. Both Design and Engineering own the input, not the roadmap. |
| **3. Design cycle** | Design, with the trio as collaborators | At the start of each planned feature the trio runs a design session: one PM, one designer, and engineering. This is a 30 minute working meeting to align on experience direction before work begins. PM brings the spec or brief, written and thought through beforehand. Design leads, owns the experience direction, and is responsible for the desirability and craft of what ships. Engineering and PM are collaborators who bring technical and product input. The output is a plan the trio has agreed to, often followed by a prototype to pressure test it before building. Engineering input happens here, at the start of the cycle, not at review. <br><br> Two kinds of work skip the design session: reversible low-risk changes, and exploratory POCs or feasibility spikes. If a POC graduates into a prioritized feature, it enters the design session at that point. Each team defines what qualifies as reversible or low-risk in their team charter. |
| **4. Milestone planning** | Product and EM | Prior to milestone kickoff the trio agrees on committed scope, the reversible and irreversible calls for the work (see Step 6), success criteria, and features which require design before development. Engineering commits to what they intend to ship in the milestone before the milestone begins. PM agrees to protect that scope. Issues intended to ship will use the `~Deliverable` label. Work can only enter the milestone when the trio has signed off on "readiness".|
| **5. Development** | Engineering | Work moves in small increments that are easy to deploy and roll back, shipping behind feature flags so the team can dogfood as it builds. Nothing ships to customers until PM confirms it meets the Minimum Lovable Product bar and Design has signed off. MLP is the quality bar that defines what we commit to customers. Increasingly AI handles code generation, tests, and first-pass review. Engineers engage where human judgment is required. |
| **6. Reviews and the decision protocol** | Shared across the trio | Every consequential decision is classified as reversible or irreversible before a review window opens. We bias toward speed and optimize for a decision, not consensus. <br><br> **Reversible** - ships with a notification on the MR, tagging relevant reviewers. No channel post or fixed deadline required. <br><br> **Irreversible**<br> - the DRI classifies it into one of two tiers before opening a review window: <br> - Tier 1 (lower risk): 48 hour window. DRI incorporates what they agree with, documents what they are not taking, and ships. <br> - Tier 2 (legal, compliance, executive visibility, or large user impact): 3 day window. Required reviewers are notified directly. DRI ships with a sign-off record capturing any unresolved dissents. <br> <br> When in doubt, default to Tier 2. Each team's tier definitions and decision authority live in their team charter. |
| **7. Delivery accountability** | EM owns delivery, PM protects scope | Deliverables are agreed and documented during milestone planning. The EM is accountable for shipping committed work, communicating early if something is at risk, and driving urgency rather than waiting for work to finish itself. We track say/do, the ratio of what we commit to what we ship, as our measure of predictability. Changes to scope, escalations, and ad hoc requests are documented on the milestone issue so the cost of direction changes is visible and available for retrospectives. |
| **8. Customer validation** | Product led, trio invited | Customer validation is a constant flywheel feeding into multiple steps throughout the SDLC.<br><br>- PMs target engaging with at least 10 customers per month, inviting designers and engineers to inform first-hand insights.<br>- New features are rolled out to Customer Zero before broader rollout to validate assumptions, user experience and fit for purpose. Customer Zero comms are Product led, similar to a release post. Feedback issues are created to capture Customer Zero feedback and we may choose not to invest in wider rollout if the lovable bar is not achieved. |
| **9. Sharing status** | IC Engineering for status, Product for sharing usage and feedback | Status lives on the issue, updated weekly, and is summarized into Slack for visibility. Leaders and PMM utilizes the [AI org execution dashboard](/handbook/product-development/how-we-work/ai-section-product-development-flow/#ai-org-status-dashboard) to view real time status of workstreams. Usage data and customer feedback flow back to the trio to inform the next planning cycle. |

## Prototyping

{{% alert title="Note" color="primary" %}}
Anyone can build a prototype. Each one starts with a named question and a named DRI who calls the test complete when the question has an answer. The goal is a decision, not a perfect artifact. Details are clarified as work moves from idea to functional prototype.
{{% /alert %}}

There are two flavors of prototype, with different promotion paths:

- Concept prototype: built outside the GitLab codebase (e.g. Figma, Claude artifacts). These are cheap and fast but they cannot ship as-is. Validated concepts get rebuilt as real features before broad rollout.
- Working prototype: built on a branch inside the relevant GitLab repo, using real APIs and data. This is a heavier lift and typically driven by engineering. While it can ship as-is if it clears the production bars (tests, conventions, security review), more often it gets refined first.

The type to use depends on the test. Surface decisions, early concept validation, and most usability tests are well-served by concept prototypes. Technical feasibility and high-fidelity customer testing need in-tree prototypes.

| Test | Exit criteria | DRI |
|---|---|---|
| **Usability test:** does the interaction hold up in real use? | The team has a clear yes/no on whether the interaction works. | Design |
| **Surface decision:** which pattern moves forward? | A single pattern is selected, with stated reasoning. | Design |
| **Customer validation:** does this concept solve the customer's problem when tested with Customer Zero? | Customer Zero confirms or rejects the concept. | Trio |
| **Assumption test:** does our hypothesis hold true? | The idea is proven or falsified. | Trio |
| **Technical feasibility:** can we build this within a reasonable scope of effort? | Engineering confirms or denies feasibility with a rough effort estimate. | Engineering |

A "yes" on prototype validation does not mean the code is production-ready. If the concept is validated, the team rebuilds it as a real feature before broad rollout.

Larger prototypes (more than a few days of effort) get coordinated with the trio when the test is named, so they don't quietly consume committed milestone capacity.

## Cadence

We value synchronous time and limit our standing ceremonies to:

- Weekly 30 minute sync per functional team attended by engineering, design and product. EM leads the call, but all team members contribute. We cover what shipped in the last week, what is blocked, and any change in scope. We leave room for discussion, ideation, demos, and information sharing.
- Monthly milestone kickoff, 45 minutes to align the team on scope commitment, reversibility calls, success criteria, work entering the design cycle. Call is led by PM or EM, but all functional team members contribute.
- Monthly retrospective is a 45 minute functional team sync, driven by the EM. Product, engineering and design all contribute. Actionable outcomes of the retro are documented in the async retro issue and rolled up to the group level for process improvement identification across teams.

{{% alert title="Sync best practices" color="primary" %}}

- We expect all team members to contribute to the agenda at least 12 hours prior to the call, giving time for the team to pre-read agenda topics and references so our sync time is used efficiently.
- We record the calls and use AI to take notes. 
- AI generated summaries including call outcomes are posted to the functional team's Slack channel.

{{% /alert %}}

## Measuring effectiveness of the process

The workflow above is meant to makes us faster, more aligned, and more accountable to customers. To be sure we're meeting this objective, we watch a small set of signals and revise when patterns emerge.

- Qualitative: cross team retrospectives, customer feedback loops, and functional team member feedback.
- Quantitative: the team metric, say/do attainment, and reduced silent slippage of work from one milestone to the next.

## Translating org structure to GitLab labels

The AI section's org structure is documented [here](/handbook/engineering/ai/#organizational-structure). This section explains the labels that map to each level of that structure, so issues and MRs land in the right team's view.

| Org level | Label convention | Example |
|---|---|---|
| Section | `~section::ai` | `~section::ai` |
| Stage | `~devops::<slug>` | `~devops::agent foundations` |
| Group | `~group::<slug>` | `~group::agent execution` |
| Functional team | `~Category:<name>` | `~Category:Agent Tools` |

## AI org status dashboard

The [AI org status dashboard](https://ai-org-status-dashboard-105018.gitlab.io) is the source of truth for what the AI section is shipping and how it's tracking. Leadership uses it as a pre-read before weekly business reviews and cross-functional syncs.

### How your epic gets on the dashboard

An epic appears on the dashboard when it carries **both**:

1. **One of the recognized AI-org labels** (any of the below). The current list lives in [`ORG_LABELS` in the dashboard fetcher](https://gitlab.com/gitlab-org/ai-powered/ai-org-status-dashboard/-/blob/main/fetcher/fetch_epics.py) and includes:
   - `section::ai`
   - `devops::agent foundations`
   - `devops::ai clients`
   - `devops::ai coding`
   - `devops::ai platform`

2. **A quarterly planning label**: `FY27-Q3`, `FY27-Q4`, `FY28-Q1`, `FY28-Q2`.

{{% alert title="Troubleshooting tip" color="primary" %}}
If your epic is only tagged with a `group::*` or `category:*` label and no `section::` or `devops::`, it won't show up. If a workstream is missing from the dashboard the first thing to check is whether it has one of the labels above.
{{% /alert %}}

### Key epic metadata

1. **Description summary.** The dashboard parses your epic description and uses it in the status dashboard to provide viewers with an overview of the workstream. The job is looking for any of the following headers:
   - `## Summary`
   - `## Release notes` / `## Release notes summary`
   - `## Release post` / `## Release post summary`
   - `## Overview`
   - `## Problem` / `## Problem to solve`

2. **Release milestone.** Add a GitLab milestone to your epic to signal the intended delivery date of the workstream. (tip: do use a specific milestone like 19.5, 19.6, don't use general timing like "next 1-3 milestones")

3. **Health status.** For workstreams in progress, set the epic's health via GitLab's native health-status widget (On track / Needs attention / At risk). Without a health status, your epic falls into "Health unavailable" on the KPI bar, even if a Weekly Status comment is posted.

4. **Weekly Status comment.** Weekly Status comments are the source of the "AI weekly synthesis" section shown in the drawer for each epic on the dashboard. These are normally AI-generated, posted weekly as an **internal note** on the epic using the [Weekly Status comment template](https://gitlab.com/gitlab-org/ai-powered/ai-org-status-dashboard/-/blob/main/scripts/prompts/workstream-weekly-status.md#weekly-status--yyyy-mm-dd--on-track--needs-attention--at-risk--no-status--complete). You can also post or edit one by hand using the same header format — see [How the dashboard picks up your changes](#how-the-dashboard-picks-up-your-changes) for how manual edits reach the dashboard.

5. **CXO Interest.** This optional label is used to filter epics being followed by CPMO+. These epics require the highest metadata fidelity for workstreams in progress.

6. **PMM Shipping.** The optional `pmm-ai-whats-shipping` label is applied to create a curated release narrative for the Product Marketing team. The same metadata hygiene expected as CXO for work in progress.

7. **Release Target.** Add the appropriate release target label to indicate how the work will be released, options include `~release target::customer zero`, `~release target::experimental`, `~release target::beta`, and `~release target::GA`.

### How the dashboard picks up your changes

1. **Data refresh** runs automatically on an hourly CI schedule, plus on-demand via the dashboard's **↻ Refresh now** button. This refreshes epic, issue, and MR metadata — milestones, health-status widget value, labels, hierarchy — but it does **not** re-read Weekly Status comments; see the next point.
1. **Weekly Status comments** are picked up on two separate cadences from the data refresh above:
   - **Weekly** (Mondays ~12:00 UTC): a scheduled job generates a new AI-written Weekly Status comment per in-progress epic and posts it, and updates the health-status widget.
   - **Daily** (00:00 UTC): a lighter ad-hoc rescan re-reads whichever Weekly Status / Status / Async Status Update comment is already posted on the epic — one you posted or edited by hand, or last Monday's AI synthesis — and merges it into the dashboard's cache. It makes no AI call and posts nothing; it only catches the dashboard up to what's already on GitLab, so a hand-posted or edited status shows up within a day instead of waiting for the next Monday.

   Either way, the comment reaches the dashboard itself at the next hourly data refresh.
1. **Milestone slip capture**: any epic whose milestone changes (slip, advance, schedule, deschedule) is recorded in a forward-only snapshot log. Slips surface in the drawer's "Milestone history" section, a `(N×)` badge next to the milestone in the table, and the "Items slipped" KPI tile.

### Questions & feedback

Ping @amandarueda in Slack for general questions, leave feedback in the [feedback issue](https://gitlab.com/gitlab-org/ai-powered/ai-org-status-dashboard/-/work_items/1) and open bugs in the [source project](https://gitlab.com/gitlab-org/ai-powered/ai-org-status-dashboard/-/work_items).
