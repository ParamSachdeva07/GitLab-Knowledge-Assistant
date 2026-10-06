---
title: "Downstream consumers"
description: "How Duo Developer and Duo Review consume the Agent plan for execution and validation."
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

The Agent plan's value comes from being consumed by downstream systems. This page covers how Duo Developer and Duo Review read and use the plan.

## Duo Developer handoff

When a user triggers Duo Developer from a work item, the agent needs to read the Agent plan. Two options:

1. The Flow's first step fetches the plan through the work item GraphQL API.
2. The plan is injected into the agent's context at session creation.

The chosen approach and its implementation are TBD.

## Duo Review validation

The Duo Review agent validates MR changes against the originating Agent plan. The link between MR and plan is established through the [work item–MR relationship](wi_mr_relationship.md). The review agent fetches the plan from the linked work item and uses it as evaluation criteria.

Epic: [Workstream 1 — MR spec enforcement](https://gitlab.com/groups/gitlab-org/-/work_items/21514)

## Merge check in MR

Validating the Agent plan at merge time (as a merge check) is still being defined. This may be covered by the [Code Review Lifecycle Transformation](https://docs.google.com/document/d/1BsdLonLqNyB0QSdEiUaJJ5GNQLkr-gKx_uQNTApdfCA/edit?tab=t.0) initiative workstream rather than built within SDD directly.

## API surface

The Agent plan is exposed through the standard work item widget GraphQL/REST API. External tools (`curl`, `glab`, IDE extensions) can read and write plans using this surface.

## Structured vs raw Markdown

Downstream agents consume the plan as raw Markdown text today. If the plan evolves to a richer structure (sections, acceptance criteria, test cases), serialization and backward compatibility will need to be addressed.

## Decisions

| Date | Decision | Who |
|------|----------|-----|
| 2026-04-17 | Agent plan format consumed by downstream agents is **Markdown** (not YAML or structured JSON). Markdown is human-readable, already the common format of GitLab descriptions, and avoids serialization overhead for consumers. | @fredericcaplette |
