---
title: "Interactive builder"
description: "Design for the Interactive builder, a reusable Duo Chat and live preview UI framework for iterating on LLM output."
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

The Interactive builder is a generic, reusable UI framework for iterating on LLM output. The left side is a Duo Chat conversation, the center pane shows a live preview of the artifact being produced. SDD (Agent plan generation) is the first use case, but the framework is feature-agnostic.

Epic: [Interactive builder](https://gitlab.com/groups/gitlab-org/-/work_items/21653)

[PoC video](https://www.youtube.com/watch?v=UjZ-yHNg6Ic)

## Relationship to AI Panel

The Interactive builder lives inside the existing [AI Panel architecture](../ai_panel/_index.md) as a new sub-application. It follows the same component agnosticism, props passthrough, and event-driven communication patterns described there.

## Live preview

As the agent updates the Agent plan through tool calls, the preview pane reactively reflects the change. The propagation mechanism (Apollo cache write on tool completion vs subscription) is TBD.

## Generality

The framework exposes a plugin contract so other features can register their own artifact type and preview component. The specifics of this contract are TBD.

## Scope

The Interactive builder is a refinement on top of the base Agent plan + Duo Chat experience. For v1 the widget and chat are sufficient; the builder is a follow-up iteration.

This workstream is **on ice** until we validate that the Agent plan itself adds value through the base Duo Chat flow. Investing in a richer builder UI before confirming the core artifact is useful would be premature.
