---
title: Tier 2 Path to Tier 1
description: A repeatable plan for teams to transition from Tier 2 to Tier 1 on-call ownership.
---

## Tier 2 Path to Tier 1

*A repeatable plan for handing the pager to a team that already carries real operational ownership.*

### The premise

Production Engineering doesn't fully know what access the team needs, and the team may not either. We shouldn't guess. Assume the team already has what it needs, since it's already responding to these incidents in practice via Tier 2 escalations. All that changes is who gets paged first, and we have an easy feedback loop to provide needed access when it is identified.

**Flipping the pager** means: instead of the Tier 1 SRE on-call engineer (EOC) getting paged and escalating to the team when help is needed, the team gets paged directly and escalates to EOC when SRE help is needed. EOC is always a fallback when the team misses a page or has a gap in coverage.

Keep it simple.

### The access feedback loop

When the team hits something it can't do mid-incident that the EOC can:

1. Page the EOC.
2. Resolve the incident together.
3. Following the incident, the team opens a corrective action to:
   1. Open an access request to grant the missing access to the team.
   2. Add it to the team's baseline entitlements and/or onboarding.
   3. Update the relevant runbook, or write a new one for the team's own use.

### The rollout

Three stages, roughly a week apiece:

**Week 1 — Visibility.** Alerts start posting to the team's channel - this shows when the team would be getting paged and allows them to proactively join incidents before being paged. In parallel, the team reviews what it means to be incident lead (a reading checklist will be provided). Anyone can lead an incident: in S1/S2 it's the incident manager (IMOC); in S3/S4 it's usually whoever received the page.

**Week 2 — Dual paging.** Both the team and EOC are paged on these alerts, side by side.

**Week 3 — Ownership.** EOC paging turns off. EOC is the fallback on the escalation path. EOC is paged only if the team doesn't acknowledge within 5 minutes. The team is effectively on call. Any schedule gaps also route straight to EOC with no 5 minute delay. This allows teams to go on call without having to wait for full 24x7 coverage.

### Timeline

Treat the rollout as a map, not a deadline. Any stage can stretch if alerts aren't firing often enough to give a signal, or if a real gap turns up that needs filling before moving on.

### Where this fits

This isn't the final DevOps enablement process that enables every team to go on call immediately. It's a fast path for teams that already carry Tier 2 ownership. Each run of this plan surfaces the access gaps and edge cases that eventually shape the more complete enablement process.
