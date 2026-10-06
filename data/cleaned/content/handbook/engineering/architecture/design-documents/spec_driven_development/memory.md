---
title: "Memory and context injection"
description: "Design for modeling, storing, and injecting project context and memory into Agent plan generation."
status: ongoing
maturity: not for now
creation-date: "2026-04-16"
authors: [ "@fredericcaplette" ]
owning-stage: "~devops::plan"
toc_hide: true
---

Read more about SDD in [Spec-Driven Development](_index.md).

**Maturity: Not for now**

## Summary

Agents generating or refining an Agent plan need context beyond the current work item: project conventions, past decisions, architectural patterns, team preferences. This page covers how that external context is modeled, stored, and injected.

Epic: [Workstream 2 — Memory loop](https://gitlab.com/groups/gitlab-org/-/work_items/21512)

## Memory layers

Context exists at multiple scopes: Project, Group, Instance, Organization. The model for retrieving and prioritizing layered context is TBD. A possible fifth scope (Product) has been discussed.

## Injection point

Where in the AI Gateway pipeline memory gets injected — before prompt assembly as system context, or as a tool the agent calls on demand — is TBD.

## Learning loop

When an agent completes work and the result is reviewed (approved/rejected), the outcome should be captured as a learning and fed back into memory for future plan generation. The mechanism for this feedback loop is TBD.

## Storage

Where memory lives — repository files (`.gitlab/memory/`), a database-backed store, or the Wiki — is TBD.
