---
title: "Operating Rhythm"
description: "How Enterprise AI, ATOs, and Champions work together: channels, cadence, decision rights, and escalation path."
---

## Operating model in one paragraph

Enterprise AI is the platform Hub: it builds, governs and supports the AI capability. The ATO is the spoke, a senior role inside the function that owns delivery and bridges Enterprise AI to the function. Champions form the second Hub inside the function, a peer community across sub-teams who drive adoption, pilot agents and surface use cases. The ATO connects the two hubs. Use-case work flows through the ATO. Bugs, security issues and platform feedback flow up directly so the platform learns fast.

## Slack channels

| Channel | Visibility | Members | Purpose |
|---|---|---|---|
| [**#enterprise-ai-collab**](https://gitlab.enterprise.slack.com/archives/C0AE5DX6SQJ) | Public | All GitLab team members | Team-member engagement channel. Questions, FAQs, intake support. |
| `#enterprise-ai` | Private | Enterprise AI team | Internal Hub working channel. Roadmap, platform issues, governance, escalation routing. |
| `#ent-ai-ato` | Public | Enterprise AI plus all ATOs | Daily working channel for Hub-ATO collaboration. Default mode for async. |
| `#ent-ai-champions` | Public | Champions across all spokes plus ATOs plus Hub | Cross-spoke Champion community. Learning and consistency, not work intake. |

## Cadence

The cadence is deliberately stepped: lighter while we are small, heavier as we scale. Async-first throughout, with formal forums kept slim.

![Enterprise AI operating cadence at a glance: Daily, async-first in #ent-ai-ato with no mandatory standups. Weekly, ATO Council and AI Engineer to ATO sync. Every two weeks, ATO to exec sponsor, Champion to ATO sync, and function AI office hours. Monthly, Champion demo or share-out across the function. Quarterly, Business Review plus cross-spoke Champion show-and-tell.](/images/eta/ai/strategy/operating-cadence.png)

### Daily

Async-first in `#ent-ai-ato`. No mandatory standups across the cohort.

### Weekly

- **ATO Council.** All ATOs plus Enterprise AI representation. 60 minutes. Mandatory. Show-and-tell, platform updates, shared problems, cross-spoke learnings. This is the de-siloing forum, and it naturally grows in scope and value as more ATOs join.
- **AI Engineer to ATO sync.** Minimum once weekly between each ATO and their assigned AI Engineer. More during the launch of a new spoke or an active build (typically two to three times a week), daily during a production push. Async in Slack between syncs. Assignments are reviewed quarterly.
- **ATO to function leadership team.** The ATO joins their function's leadership meeting where appropriate, with a standing agenda slot, so AI work surfaces to the wider function exec team alongside the exec sponsor.

### Every two weeks

- **ATO to exec sponsor.** Updates and reactive prioritisation as priorities evolve.
- **Champion to ATO sync.** 30 minutes. In-function intake and coaching. Daily async happens in `#ent-ai-champions` between syncs.
- **Function AI office hours.** 45 minutes. Mandatory: every ATO runs them. Open to everyone in the function, not just Champions. Hosted by the ATO with the AI Engineer present, so technical questions get answered in the room rather than becoming a ticket. Drop-in and unstructured: no agenda, no attendance expectation, no preparation asked of anyone who turns up. Scheduled on the alternate week to the Champion to ATO sync, so there is something open in the function's diary every week.

  This is the front door for the majority of the function who are not Champions. It is also the ATO's cheapest source of signal: the questions people bring are unqualified use cases, and the ones that recur are the ones worth taking to the roadmap.

### Monthly

- **Champion demo or share-out** across the function, hosted by the ATO with Champions presenting.
- Otherwise reserved. Things move too fast in AI for monthly reviews to be the primary lever.

### Quarterly

- **Quarterly Business Review.** Director, Enterprise AI plus ATO plus exec sponsor. 30 minutes, two or three slides:
  - Backwards: use cases shipped, adoption, value delivered.
  - Forwards: planned use cases, dependencies, resourcing.
  - Other: process improvements, feedback, asks.

  Slim and punchy. No death by slides.

## Champion model

**Why Champions.** ATOs cannot personally drive every use case in a 200+ person function. The Champions Hub extends reach into sub-teams and creates a peer community of practice inside the function.

**Nature.** Champions are not direct reports to the ATO. They are a peer community within the function. The ATO is their bridge to Enterprise AI, not their manager.

**Selection.** The ATO selects Champions with sub-team manager sign-off. One per sub-team or squad. 5 to 10% time, formally agreed with the manager.

**What they do.**

- Identify and qualify use cases in their team.
- Pilot agents and workflows.
- Coach teammates inside their sub-team.
- Surface friction and feedback back to the ATO.

**Cadence.** See the [Cadence](#cadence) section above for the full schedule. In short: ATO to Champion sync every two weeks with daily async in `#ent-ai-champions`, a monthly Champion demo across the function, and a quarterly cross-spoke Champion show-and-tell run by Enterprise AI.

**Champions are not the only route in.** The Champion network extends the ATO's reach, but a function member should never have to find their Champion before they can ask a question. Fortnightly office hours are open to the whole function for exactly that reason. Champions are welcome there too, but it is not their forum.

**Routing rules.**

- Use-case requests, ideas and project work: **Champion to ATO**. Never direct to Hub.
- Bugs, security issues and platform feedback: **Champion to Hub** directly (via `#ent-ai-champions` or Serval).
- Anyone else in the function: **office hours, `#enterprise-ai-collab`, or their Champion**. All three land with the ATO for use-case work. The routing rule is about where work is triaged, not about who is allowed to raise it.

## Decision rights

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
| ATO hiring | Five-step loop; see [AI Transformation Owner](../ato/) |

## Escalation path

When something is on fire (broken use case in production, security incident, platform outage affecting a spoke):

1. ATO (or Champion if the ATO is unavailable) raises via **Serval**.
2. Serval routing triggers a notification in `#enterprise-ai`.
3. Hub on-call acknowledges and triages.
4. Hub feeds back into the originating channel (`#ent-ai-ato` or `#ent-ai-champions`).

For non-urgent issues, default to async in `#ent-ai-ato` first.

## Resourcing target

Each AI Engineer pairs with up to two ATOs (a 1:2 ceiling). During the early phase of a spoke (typically the first quarter) we pair closer to 1:1 to accelerate ramp-up. As a spoke matures and a delivery rhythm sets in, the same AI Engineer can support a second one without losing depth.

## Related

- [Hub & Spoke & Hub](../) - the strategic narrative.
