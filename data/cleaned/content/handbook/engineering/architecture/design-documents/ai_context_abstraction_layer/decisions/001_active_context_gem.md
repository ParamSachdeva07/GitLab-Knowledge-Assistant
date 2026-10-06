---
title: "AI Context Abstraction Layer ADR-001: Gem-Based Architecture"
description: "Decision record for implementing the AI Context Abstraction Layer as the ActiveContext Ruby gem."
toc_hide: true
---

## Status

Accepted

## Context

The AI Context Abstraction Layer is a critical component that provides a unified interface for semantic search across different vector stores (Elasticsearch, OpenSearch, PostgreSQL with pgvector). This layer needs to be:

1. Reusable across multiple GitLab services
2. Maintainable and testable in isolation
3. Clearly separated from GitLab-specific implementations
4. Extensible for future vector store backends

## Decision

We have decided to:

1. Implement the ActiveContext Abstraction Layer as a Ruby gem located in `gems/gitlab-active-context` within the GitLab Rails repository
2. Name the gem `ActiveContext`, thus all gem classes are namespaced under `ActiveContext::`
3. GitLab-specific implementations should be namespaced under `Ai::ActiveContext` (for example, `Ai::ActiveContext::Collections::Code`, `Ai::ActiveContext::References::Code`)

## References

- [ActiveContext Gem](https://gitlab.com/gitlab-org/gitlab/-/tree/master/gems/gitlab-active-context)
