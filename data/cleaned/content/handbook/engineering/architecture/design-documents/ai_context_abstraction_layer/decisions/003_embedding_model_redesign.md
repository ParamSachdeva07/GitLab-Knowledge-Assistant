---
title: "AI Context Abstraction Layer ADR-003: Embedding model redesign"
description: "Decision record explaining a new embedding model design"
toc_hide: true
---

## Status

Accepted

## Context

The original ActiveContext design hard-coded embedding models as embedding version hashes:

```ruby
class Ai::ActiveContext::Collections::Code # class implementing an ActiveContext Collection
  embeddings_v1: { model: 'text_embedding_005_vertex', dimensions: 768 }
  embeddings_v2: { model: 'text_embedding_004_vertex', dimensions: 512 }
end
```

### Limitations of the previous design

- Model selection by the user cannot be supported, making it a blocker for Self-Managed instances with Duo Self-hosted, where the user must select their own models
- Adding new models requires updating the hard-coded version hashes and doing a manual backfill process, creating maintenance burden

### Existing Model Configuration feature

There is already an existing [Model Configuration functionality](https://docs.gitlab.com/administration/gitlab_duo/model_selection/) for other AI features. However, this cannot support the backfill process needed when switching embedding models.

## Decision

We have decided to redesign the embedding models to support flexible model selection with one-click model switching that triggers a backfill process in the background.

The main concepts of the redesign are:

- **Model Metadata** - embedding model configuration is persisted in `Ai::ActiveContext::Collection` record `metadata` rather than hard-coded
- **3 model configurations per Collection** - each Collection has a `current_indexing_embedding_model`, `next_indexing_embedding_model`, and `search_embedding_model`
- **Asynchronous switching process** - model switching triggers a series of background processes that leverages the [Active Context Tasks framework](../active_context_tasks.md)
- **Synced with [AIGW Model Switching framework](https://docs.gitlab.com/development/ai_features/model_switching/)** - each Collection has its corresponding Embeddings AI Feature key, supported in AI Gateway and synced with `Ai::FeatureSetting` records

For further details, please see the [Embedding Models design document](../embedding_models.md).
