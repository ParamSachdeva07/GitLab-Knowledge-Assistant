---
title: "Decision log"
description: "Design for the Decision log work item widget that captures structured decisions for SDD context gathering."
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

The Decision log is a new work item widget that captures structured decisions (pending and decided). It provides a reference point for humans and agents and is included as context whenever an Agent plan generation session starts.

Epic: [Workstream 3 — Decision log](https://gitlab.com/groups/gitlab-org/-/work_items/21552)

## Data model

A list of decision entries on the work item. Each entry has: description, status (pending/decided), author, date, and optionally an assignee. Storage format TBD — options are a JSON column on a widget table or individual records in a dedicated table. Most likely the issue table is too big and we'd want a separate table.

## Interactions

- Humans can add pending decisions manually.
- Agents can read the log as input context and write new entries through work item tools in AI Gateway.
- Resolving a comment thread with "Make a decision" stores the result in the log, bridging the Notes system with the Decision log widget.
- Assigning a pending decision to a user creates a to-do item through the existing to-do system.
- Raise any pending threads within the widget so that you can make decisions from the widget per thread and leave no threads unanswered.

## Consumption

Whenever a Duo Chat session starts on a work item, the Decision log is read through the work item tool.
