---
title: "Work item to merge request relationship"
description: "Design for the bidirectional link between work items and merge requests required by SDD."
status: ongoing
maturity: mature
creation-date: "2026-04-16"
authors: [ "@fredericcaplette" ]
owning-stage: "~devops::plan"
toc_hide: true
---

Read more about SDD in [Spec-Driven Development](_index.md).

**Maturity: Mature**

## Summary

SDD requires a first-class, bidirectional relationship between work items and merge requests. The Agent plan lives on the work item; Duo Developer and Duo Review operate on the MR. Without a strong link, downstream agents cannot reliably find the plan they should follow or validate against.

## Current state

Today the work item-to-MR link is loose:

- **Closing references** — an MR description containing `Closes #123` will add a closing reference.
- **Mentioned reference** - when a comment adds a link to an issue, it adds the `Mentioned` reference.
- **No programmatic lookup** — there is no reliable API to ask "given this MR, what is the originating work item and its Agent plan?"

## What SDD needs

1. **Duo Developer** starts a coding session from a work item. The resulting MR must be automatically linked back to that work item so the relationship is established without manual intervention.
2. **Duo Review** receives an MR and needs to fetch the originating Agent plan. It must be able to traverse MR -> linked work item -> Agent plan widget in a single, deterministic path.
3. **Merge checks** may eventually validate the MR against the plan. This requires the link to be queryable on the merge request page.

## Proposed approach

Strengthen the existing work item–MR association so it is:

- **Automatic** — when Duo Developer creates an MR from a work item, the link is created as part of the flow.
- **Explicit** - relationship can be established or destroyed via the API and or through the UI. This also adds a nice integration layer to allow more programatic updates.
- **Bidirectional** — queryable from both the work item side (`workItem.mergeRequests`) and the MR side (`mergeRequest.workItems`).
- **Typed** — distinguishable from other MR references (for example, "created by agent from this plan" vs "manually linked").

The exact data model (extending the existing `MergeRequestsClosingIssues` table, a new association table, or leveraging work item links) is TBD.

## Downstream impact

- [Downstream consumers](downstream_consumers.md) — Duo Developer handoff and Duo Review validation both depend on this link.
- [Merge check in MR](_index.md#3-plan-validation) — Validating the plan at merge time requires the link to be present and queryable.
