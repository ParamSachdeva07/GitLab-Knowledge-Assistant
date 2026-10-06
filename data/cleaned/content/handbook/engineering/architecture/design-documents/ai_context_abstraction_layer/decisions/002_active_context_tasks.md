---
title: "AI Context Abstraction Layer ADR-002: ActiveContext Task framework"
description: "Decision record for the introduction of a framework for complex long-running operations"
toc_hide: true
---

## Status

Accepted

## Context

The ActiveContext framework needs to support long-running, asynchronous operations that may span multiple steps and require careful orchestration.

For example, switching from one embedding model to another requires:

1. Creating a new vector field
1. Backfilling embeddings for all documents
1. Updating collection metadata
1. Syncing feature settings
1. Cleaning up old fields

### Challenges with Existing Approaches

**Simple Sidekiq Workers:**

- No built-in support for task dependencies
- Difficult to handle cascading failures
- No visibility into multi-step workflows
- Hard to retry individual steps in a chain

**Orchestration Services:**

- Complex state management
- Difficult to recover from crashes
- No persistence of workflow state
- Hard to debug long-running operations

## Decision

We have decided to introduce the [**ActiveContext Task Framework**](../active_context_tasks.md) for managing long-running, asynchronous operations. It provides a structured way to define, execute, and track complex workflows that may involve multiple sequential or dependent steps.
