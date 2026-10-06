---
title: "ADR-001: Semantic Code Search"
description: "Decision record for introducing a Semantic Code Search tool for Agentic Duo Chat"
toc_hide: true
---

## Context

The "Codebase as Chat Context" functionality, which provides a way to semantically search through a codebase, was tightly coupled with Classic Duo Chat. We needed a way to make this available on Agentic Duo Chat.

## Decision

1. We decided to expose the semantic code searching feature as a tool on the **GitLab MCP (Model Context Protocol) Server**.

   Exposing Semantic Code Search through MCP decouples it from the Agentic Duo Chat implementation, allowing for independent evolution of both systems. In addition, other tools and agents can leverage the same MCP interface to access Semantic Code Search, promoting code reuse and consistency.

1. We decided to call the tool **Semantic Code Search**, and moving forward we will refer to this feature as such.

   Using the "Semantic Code Search" name for the tool makes its functionality self-explanatory.

For further details, please refer to the [Semantic Code Search design document](../semantic_code_search.md).

## Alternative considered: native Agentic Duo Chat tool

Implement Semantic Code Search as a native tool directly within the Agentic Duo Chat system, without exposing it through the MCP Server.

We decided against this approach because it would create unnecessary coupling and limit the extensibility of the system.

## Related Work Item

- [Semantic Code Search - Agentic Chat Integration](https://gitlab.com/groups/gitlab-org/-/work_items/18193)
