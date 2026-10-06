---
title: "Plan readiness scoring"
description: "Design for the readiness score that signals whether an Agent plan is prepared for agent execution."
status: ongoing
maturity: still defining
creation-date: "2026-04-16"
authors: [ "@fredericcaplette" ]
owning-stage: "~devops::plan"
toc_hide: true
---

Read more about SDD in [Spec-Driven Development](_index.md).

**Maturity: Still defining**

## Summary

A readiness score communicates how prepared an Agent plan is for agent execution. It acts as a lightweight quality gate before Duo Developer handoff.

Issue: [Workstream 0.5 — Agent plan score and approval flow](https://gitlab.com/gitlab-org/gitlab/-/work_items/596916)

## Scoring model

What signals contribute to the score — completeness of template sections, presence of acceptance criteria, resolved vs pending decisions, token efficiency — is TBD.

## Computation

Whether the score is computed client-side (heuristic on the Markdown), server-side (background job), or by an LLM call is TBD.

## Display

How and where the score is shown (on the widget, as a badge, as a blocking gate) is TBD.

## Approval flow

Eventually the score may gate automated execution. Work item approvals do not exist yet, so this is a future concern.
