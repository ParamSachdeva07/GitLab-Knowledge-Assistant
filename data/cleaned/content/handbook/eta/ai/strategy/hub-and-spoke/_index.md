---
title: "Hub & Spoke & Hub"
description: "GitLab's operating model for scaling AI across every function: one platform Hub, one ATO spoke per function, one Champion community per function."
---

## Why we work this way

- **Pre-AI governance applied to AI-era tooling.** The volume and velocity of AI work outpace the review cadence that was designed for traditional capabilities. The fix is not less governance; it is governance that scales, delivered through a central interface for CorpSec, Legal, and Privacy rather than reviewer-by-reviewer across the whole company.

- **Uneven AI capability across functions.** Some functions are pulling ahead while others fall behind, and the gap widens every week. Without coordination we miss the deeper opportunity, which is to reimagine how work gets done rather than simply inject AI into existing flows.

- **Centralised teams too far from business context.** Centralised AI delivery, interpreted in isolation, produces solutions that miss the mark, often months after the request landed. Embedded delivery, sitting close to the work, is faster and produces better answers.

- **Siloed individual experimentation with no clear arbiter.** Team members building AI tools independently leads to duplicated effort, inconsistent approaches, and competing P1 requests with no single point of prioritisation. The energy is right; the channel is missing.

## The model in one paragraph

Two hubs joined by a spoke. The platform Hub (Enterprise AI) owns the AI capability: platform, engineering, governance, and standards. Each function has an embedded spoke, the AI Transformation Owner (ATO), paired with an AI Engineer from Enterprise AI. The in-function Hub is the Champion community: a peer network of practitioners inside the function. The ATO is the connective tissue between the platform Hub and the in-function Hub.

## The model in one picture

![Hub, Spoke, Hub: Enterprise AI as the platform Hub on the left (Platform, AI Engineering, Governance and Security); the AI Transformation Owner as the single accountable bridge in the middle; and Champions as the in-function Hub on the right, organised by sub-function. Build and standards flow from the platform Hub to the ATO. Use cases and priorities flow from Champions through the ATO back to the platform Hub. A feedback loop runs across all three for bugs, security issues and platform feedback.](/images/eta/ai/strategy/hub-spoke-hub.png)

One platform Hub at the centre, one ATO spoke per function, one Champion community inside each function.

## The three roles

### Enterprise AI (the platform Hub)

Owns the AI platform, engineering capacity, governance, security review, and cross-function standards. Builds skills, agents, and integrations that any function can pick up. Does not own use cases inside any single function. It does, however, own the *how*: partnering with the ATO to shape the technical approach and the best practice each solution should follow, regardless of which team ultimately builds it.

### ATO, AI Transformation Owner (the spoke)

A senior role embedded inside a function. Owns the AI roadmap for that function, qualifies use cases, partners with the assigned AI Engineer to deliver them, and reports value back to the function's exec sponsor. The ATO is the single accountable bridge between Enterprise AI and the function. The split is right-hand / left-hand: the ATO owns the *what* and *why* (which problems to solve, in what order) and brings those problem statements to Enterprise AI, who own the *how*. The ATO also gates work built inside the function, by Champions or individual contributors, keeping it aligned to centralised strategy and standards. See the [AI Transformation Owner](ato/) page for the full role.

### Champions (the in-function Hub)

A peer community inside the function, one per sub-team, at 5 to 10% time. Champions surface use cases from the front line, pilot solutions in their teams, coach teammates, and feed friction back to the ATO. They are not direct reports to the ATO; they are a community of practice.

## How work flows

1. **Raise.** Team members surface ideas through their function rather than building independently.
2. **Triage.** The ATO prioritises against business outcomes and executive guidance.
3. **Scout.** The embedded AI Engineer explores, prototypes, and proves what works.
4. **Deliver.** A small, focused team takes proven concepts to production. Depending on complexity and the expertise required, the build runs through the assigned AI Engineer, the function's own engineering capacity, or Champions and builders inside the function. Enterprise AI owns the *how* throughout, and the ATO gates in-function builds for alignment.
5. **Share.** Successful solutions, patterns, and lessons feed back through the Hub for reuse across other functions.

**Consume before build.** Before building anything new, the ATO and the builders they pull in check what Enterprise AI, other ATOs, and other teams have already shipped, and build new only when nothing fits or the existing thing is genuinely wrong for the use case. In a federated model the largest risk is every function quietly rebuilding the same capability. Reaching for existing patterns first is what makes the shared library compound rather than fragment.

## A worked example

A Champion in a function notices that her teammates are spending roughly six hours a week reformatting the same kind of customer-facing email into different formats for different briefs. Some of the friction is raised with her directly; some she picks up by being close to the work. She raises it at the next Champion sync with the function's ATO.

The ATO has already aligned with the function's exec sponsor on the priorities that matter this quarter, so she can see immediately that this use case is on-strategy. For a small, clearly aligned ask like this, she does not need a separate approval meeting; she prioritises the work and surfaces it to the exec sponsor in their next standing sync. Larger or cross-functional asks would go to the exec sponsor before any resource is committed.

The ATO brings the function's AI Engineer in early. Their first job is not to start building; it is to agree the shape of the solution. In this case: a Claude skill, bounded and prompt-driven, shipped inside the function's role-based plugin so every team member gets it without an install step. The ATO leads the first pass, drafting the input/output contract and the first cut of the prompt. The AI Engineer then refines, applies the harder prompt engineering, sets up an eval harness, and tunes for edge cases. The Champion validates in real flow, catches a tone issue, the AI Engineer tunes again. Two iterations in a week.

The skill ships into the role-based plugin. Every team member in the function gets it the next morning. Because the skill lives in a plugin, not in 200 personal prompts spread across the function, the next iteration is cheap: update once, and everyone benefits the same day. One Champion's recurring annoyance becomes a function-wide capability that improves every quarter.

## Decision rights at a glance

| Decision | Owner |
|---|---|
| Use-case prioritisation in a function | ATO, guided by the exec sponsor's org priorities and company objectives. Larger or cross-functional calls escalate to the Exec Sponsor. |
| How a solution is built (technical approach and best practice) | Enterprise AI, partnering with the ATO. |
| Platform and tooling choices | Enterprise AI |
| Security, data, and governance review | Enterprise AI (accountable platform reviewer with published SLAs) |
| Success metrics in a function | The function's own business metrics. The ATO is responsible for moving them. The Hub aggregates across spokes. |
| Replatforming bespoke tools onto the standard stack | Enterprise AI |
| In-function builds (Champion or individual contributor) | ATO gates for alignment to centralised strategy and standards |
| Champion selection in a function | ATO, with sub-team manager sign-off |
| ATO hiring | Five-step loop; see [AI Transformation Owner](ato/) |

## Function vs division

Large, complex functions with distinct sub-orgs may need spokes at the sub-function level. A single ATO across a multi-sub-org function would be too far from the business context in each area to make credible prioritisation calls, and the ATO would quickly become another layer of abstraction rather than the connective tissue the role is meant to be.

Smaller or more unified functions can work with a single spoke at the functional level. The pilot phase tests both approaches so the data, not the org chart, determines where the right level sits. The principle is the same in both cases: the ATO has to be close enough to the work to qualify use cases credibly.

## The bigger picture

AI has fundamentally changed the output-per-person ratio. A small, well-composed team with AI tooling and clear ownership can now deliver what previously required a department. The Hub and Spoke model is not just about delivering AI solutions more efficiently; it is about enabling every function to aim dramatically higher with the people they already have, in a way that is governed, coordinated, and builds capability that compounds over time rather than fragmenting into silos.

## Related

- [Guiding Principles](../guiding-principles/): the five principles that shape every AI initiative we run.
- [Operating Rhythm](./operating-rhythm/): channels, cadence, decision rights, escalation.
- [Prompts are Process](../prompts-are-process/): why every agent needs an owner.
