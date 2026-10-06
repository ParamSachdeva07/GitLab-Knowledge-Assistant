---
title: "Semantic Code Search"
description: "Design document for Semantic Code Search"
status: implemented
creation-date: "2026-06-29"
authors: [ "@partiaga" ]
coaches: []
dris: [ "@wortschi" ]
owning-stage: "~devops::ai platform"
toc_hide: true
---

<!--

The canonical place for the latest set of instructions (and the likely source
of this file) is
[content/handbook/engineering/architecture/design-documents/_template.md](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/main/content/handbook/engineering/architecture/design-documents/_template.md).

Document statuses you can use:

- "proposed"
- "accepted"
- "ongoing"
- "implemented"
- "postponed"
- "rejected"

-->

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

<!-- This renders the design document header on the detail page, so don't remove it-->
{{< engineering/design-document-header >}}

## Overview

The [Codebase as Chat Context](_index.md) functionality, which was initially implemented for Classic Duo Chat, is made available to other systems (such as Agentic Duo Chat) as the **Semantic Code Search** feature.

## Using the ActiveContext Query

Semantic Code Search is backed by `Ai::ActiveContext::Queries::Code` class, which makes use of the [Active Context framework](https://gitlab.com/gitlab-org/gitlab/-/tree/master/gems/gitlab-active-context) to:

1. Generate vector embeddings out of natural language queries using the configured [search embedding model](../ai_context_abstraction_layer/embedding_models.md#embedding-model-metadata)
1. Perform a distance-based search (k-nearest neighbors) with the generated embeddings over the configured vector storage

A project is indexed the first time a Semantic Code Search is performed on it.
For further details, please see the [Ad-hoc Indexing document](ad_hoc_indexing.md).

## Semantic Code Search on the REST API

Semantic Code Search is exposed on a REST API endpoint which invokes the `Ai::ActiveContext::Queries::Code` class.

### Endpoint details

- **Request URL:** `/api/v4/projects/:id/(-/)search/semantic`
- **Parameters**:
  - `id` (required): Project ID or URL-encoded path
  - `q` (required): Natural language search query
  - `directory_path` (optional): Restrict search to specific directory
  - `knn` (optional): Number of nearest neighbors for retrieval (default: 64)
  - `limit` (optional): Maximum results to return (default: 20)

### Post-processing

After query execution, results undergo three transformations:

1. **Duo Context Exclusion Filtering:** Removes results matching the project's context exclusion rules (sensitive files, passwords, configs)
2. **File Grouping:** Groups results by file path, merging overlapping line ranges:
   - Each file includes: path, blob_id, file_url, score, and snippet_ranges
   - Snippet ranges contain: start_line, end_line, content, and individual score
3. **Confidence Calculation:** Computes an overall confidence level (high/medium/low/unknown) based on score distribution across results

### Event Tracking

The `search_code_with_semantic_search` internal event is tracked for analytics with:

```ruby
::Gitlab::InternalEvents.track_event(
  'search_code_with_semantic_search',
  user: current_user,
  project: user_project,
  namespace: user_project.root_namespace
)
```

### Response Structure

```json
{
  "confidence": "high|medium|low|unknown",
  "results": [
    {
      "path": "app/models/user.rb",
      "blob_id": "abc123def456",
      "file_url": "https://gitlab.com/group/project/-/blob/main/user.rb",
      "score": 0.92,
      "snippet_ranges": [
        {
          "start_line": 42,
          "end_line": 44,
          "content": "def authenticate\n  ...\nend",
          "score": 0.85
        }
      ]
    }
  ]
}
```

## Semantic Code Search on the GitLab MCP Server

In order to make Semantic Code Search available to Agentic Duo Chat, it is provided as the `semantic_code_search` tool on the GitLab MCP Server. This tool is backed by the [REST API endpoint](#semantic-code-search-on-the-rest-api), which means that we avoid code duplication.

### MCP Tool Registration

The Semantic Code Search API endpoint is registered as a read-only MCP tool through Grape route settings:

```ruby
class EE::API::Search::SemanticCodeSearch
  resource :projects do
    route_setting :mcp,
      tool_name: :semantic_code_search,
      params: [:id, :q, :directory_path, :knn, :limit],
      annotations: { readOnlyHint: true },
      resource_name: "project"
    get ':id/(-/)search/semantic' do
      # endpoint implementation
    end
  end
end
```

### MCP Tool Discovery

1. The MCP client calls `list_tools` on the MCP Server
1. The MCP `list_tools` handler invokes the MCP Tool Manager to get all available MCP tools
1. For API-backed tools including `semantic_code_search`, the MCP Tool Manager discovers all routes with `route_setting :mcp`
1. The `Mcp::Tools::ApiTool` class dynamically generates the following schema for `semantic_code_search`:

    ```json
    {
      "type": "object",
      "properties": {
        "id": { "type": "string", "description": "The ID or URL-encoded path of the project" },
        "q": { "type": "string", "description": "Natural language search query" },
        "directory_path": { "type": "string", "description": "Restrict search to files under this directory path" },
        "knn": { "type": "integer", "description": "Number of nearest neighbours to retrieve" },
        "limit": { "type": "integer", "description": "Maximum number of results to return" }
      },
      "required": ["id", "q"],
      "additionalProperties": false
    }
    ```

1. The MCP Tool Manager returns the list of tools, with description and schema, to the `list_tools` handler
1. The `list_tools` handler returns the list of tools, with description and schema, to the MCP client

### MCP Tool Execution

1. The MCP Client invokes `call_tool` tool, specifying `tool: "semantic_code_search"` and providing arguments based on the schema returned by `list_tools`:

    ```json
    {
      "tool": "semantic_code_search",
      "arguments": {
        "id": "gitlab-org/gitlab",
        "q": "authentication middleware",
        "directory_path": "app/services/",
        "limit": 10
      }
    }
    ```

1. The MCP `call_tool` handler fetches the `semantic_code_search` tool through the MCP Tool Manager
1. The MCP Tool Manager returns an `Mcp::Tools::ApiTool` object that routes to the Semantic Code Search REST API endpoint
1. The `call_tool` handler invokes `Mcp::Tools::ApiTool` object, which in turn sends a request to the Semantic Code Search REST API
1. The `call_tool` handler returns the REST API's results to the MCP Client

### Integration with Agents

AI agents connected to the GitLab MCP Server can use semantic code search as part of their reasoning loop:

1. **Context Gathering**: When an agent needs to understand code structure or find relevant implementations, it formulates a natural language query describing what it's looking for
2. **Semantic Retrieval**: The MCP tool returns ranked results with file paths and line numbers, providing precise locations without requiring the agent to parse entire repositories
3. **Focused Analysis**: Agents can then fetch specific files or sections using the returned locations, reducing token usage and improving response quality
4. **Iterative Refinement**: Agents can refine queries based on initial results, progressively narrowing down to the exact code they need

## Semantic Code Search on `glab` CLI

Semantic Code Search is exposed as a native `glab` command to enable CLI-first agents, CI/CD pipelines, and scripts to access semantic search without requiring an MCP client or server.

Under the hood, the `glab search semantic` command invokes the [REST API endpoint](#semantic-code-search-on-the-rest-api).

### Command Interface

```shell
glab search semantic [flags]
```

The `flags` map to the parameters accepted by the REST API endpoint, detailed in full in the [`glab` CLI documentation](https://docs.gitlab.com/cli/search/semantic/).

### Architecture

The `glab` CLI implementation consists of a Command layer and an API Client layer:

1. **Command Layer** (`internal/commands/search/semantic/semantic.go`):
   - Parses command-line arguments and flags
   - Resolves project from git remote
   - Constructs request URL segment for semantic code search `/projects/:id/search/semantic`
   - Delegates request to the API client layer
   - Formats output based on `--output` flag
2. **API Client Layer** (`internal/api/client.go`):
   - Handles actual request invocation to the full API endpoint (`/api/v4/<api_endpoint_url>`)
   - Handles authentication via glab's configured credentials (personal access tokens, OAuth, gPAT)
   - Parses JSON response from REST API

### Use Cases

- **CLI-first Agents**: Agents like Claude Code and DAP agents can invoke semantic search with lower overhead
- **CI/CD Pipelines and Scripts**: Any workflow that doesn't have an MCP client available
- **Ad-hoc Developer Queries**: Analysts running semantic searches without IDE/MCP setup

### Integration with Agents

Agents using `glab` for semantic code search follow this pattern:

1. **Query Formulation**: Agent constructs a natural language query describing what it needs to find
2. **CLI Invocation**: Agent executes `glab search semantic <query> --project <id> --output json`
3. **Result Parsing**: Agent parses JSON response to extract file paths and line numbers
4. **Code Fetching**: Agent uses `glab repo view` or `glab api` to fetch specific file contents
5. **Analysis**: Agent analyzes fetched code to inform its reasoning and response
