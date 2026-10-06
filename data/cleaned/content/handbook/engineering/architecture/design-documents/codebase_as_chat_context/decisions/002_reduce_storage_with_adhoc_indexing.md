---
title: "ADR 002: Reduce Storage Size for Semantic Code Search Clusters with Ad-hoc Indexing"
description: "Decision record for reducing vector storage requirements for Semantic Code Search"
toc_hide: true
---

## Context

When planning to scale Semantic Code Search from the `gitlab-org` namespace to all eligible namespaces on GitLab.com, we encountered significant storage challenges with the Elasticsearch cluster we are using for the vector store.

[Analysis](https://gitlab.com/gitlab-org/gitlab/-/work_items/551852#note_2796177006) of the index for `gitlab-org/gitlab` indicated that `gitlab-org` is estimated to require more than 100TB of storage.

A [storage distribution analysis](https://gitlab.com/gitlab-org/gitlab/-/work_items/562554#note_2709963740)
of `gitlab-org/gitlab` surfaced these percentages used up by each field of the index:

| Field | Percentage |
| --------- | ---------- |
| `_source` (raw documents) | 74.5% |
| `embeddings_v1` (vector index) | 22.0% |
| `content` (text index) | 1.3% |
| Other metadata | ~2% |

The storage requirement was deemed prohibitively expensive and operationally challenging.
Furthermore, the fields we needed to target for optimization are fields we need to keep or would require significant refactor and engineering effort to drop.

## Decision

We decided to introduce **Ad-hoc Indexing** for Semantic Code Search.

This is a lazy-loading mechanism that automatically triggers initial indexing when a user attempts to perform semantic code search on a project that hasn't been indexed yet. Instead of a pipeline that indexes all eligible projects upfront, ad-hoc indexing reduces required storage by only initiating indexing when needed.

For further details, please see the [Ad-hoc Indexing design document](../ad_hoc_indexing.md).

## Alternatives Considered

1. **Remove the `content` field**
   - Stop storing the actual code snippet content in the index to reduce storage.
   - Status: rejected
   - Reasons:
      - The `content` field is essential for Semantic Code Search functionality
      - Removing it would require a major refactor of both the indexing pipeline and the Duo Chat integration
      - Analysis showed that removing `content` only saved ~4% of storage, making the effort not worthwhile
2. **Quantize embeddings**
   - Convert 4-byte float embeddings to 1-byte integers using quantization.
   - Status: deferred as a future optimization
   - Reasons for deferral:
      - This would require changes to the embedding model and vector search implementation
      - Potential impact on search quality and relevance
3. **Dynamic Partitions**
   - Implement dynamic partition allocation based on actual storage needs.
   - Status: Deferred as a future optimization
   - Reason for deferral:
     - This would require significant engineering effort

## Related Work Items

1. [Cluster sizing](https://gitlab.com/gitlab-org/gitlab/-/issues/551852)
1. [Determine number_of_partitions](https://gitlab.com/gitlab-org/gitlab/-/work_items/562554)
1. [Ad-hoc indexing epic](https://gitlab.com/groups/gitlab-org/-/epics/19655)
