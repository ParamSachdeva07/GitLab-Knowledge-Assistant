---
title: "ADR 003: Expose Semantic Code Search Outside of MCP"
description: "Decision record for making Semantic Code Search available via REST API and glab CLI"
toc_hide: true
---

## Context

Semantic Code Search was initially implemented as an MCP (Model Context Protocol) server tool, making it available exclusively to AI agents using MCP clients. However, this approach has significant limitations:

- Any workflow that doesn't go through an MCP client is completely excluded
- MCP requires a running server and compatible client, adding complexity
- CLI-first agents are becoming increasingly common and are preferred because of lower latency, easier reasoning (standard CLI invocation), better reliability, and lower cost ([see details](https://gitlab.com/groups/gitlab-org/-/work_items/21285#note_3159063685))

## Decision

We decided to:

1. Introduce a Semantic Code Search REST API ([design details](../semantic_code_search.md#semantic-code-search-on-the-rest-api))
2. Refactor the MCP tool to invoke the REST API ([design details](../semantic_code_search.md#semantic-code-search-on-the-gitlab-mcp-server))
3. Expose semantic code search natively in `glab` CLI as `glab search semantic` command which invokes the REST API under the hood ([design details](../semantic_code_search.md#semantic-code-search-on-glab-cli))

## Related Work Item

- [Make semantic code search available outside of MCP (Epic)](https://gitlab.com/groups/gitlab-org/-/work_items/21285)
