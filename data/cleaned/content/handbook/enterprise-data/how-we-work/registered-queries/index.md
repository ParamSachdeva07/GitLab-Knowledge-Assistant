---
title: "Registered Queries"
---

## Overview

Registered Queries are a data team service that gives GitLab team members a low-overhead path to get a reusable SQL query into the data warehouse as a documented, tested view. Instead of maintaining ad-hoc queries locally or requesting a full data model, you can register a query and have it reliably available in the warehouse, typically within 24 hours of submitting a request.

See the [Enterprise Data Warehouse](/handbook/enterprise-data/platform/edw/#registered-queries) page for how Registered Queries fit into the broader warehouse architecture.

{{< note >}}
The registration workflow is currently being automated. During this transition, please expect variability in request turnaround times.
{{< /note >}}

## Prerequisites

Before submitting a Registered Query request, the target schema for your function must already exist in the data warehouse. Creating a new function-specific schema and setting up its permissions falls outside of this workflow and must be arranged separately. If your team does not yet have a schema, contact the data team to have one created before submitting a request. A general schema is available as a default for teams that do not yet have a dedicated function schema.

## Benefits

- **Reliability**: Registered queries are monitored by the data team. If something upstream breaks, the data team will know and be able to fix it. Treating a query as a known model also makes the data team less likely to inadvertently break it with internal changes.
- **Testability**: Being a model allows basic tests to be applied, providing an early indicator when data changes in unexpected ways.
- **Scalability**: If other team members need the same query, having it as a documented view in the warehouse is the easiest way to share it.

## When to Use This Service

Use Registered Queries when:

- You have a query you run repeatedly and want it to be reliable and available to others.
- A view provides sufficient performance for your use case.
- You want the data team to monitor the query for upstream breakage.
- You want basic data quality tests applied to the results.

## When Not to Use This Service

- **Performance needs beyond a view**: If query performance requires a materialized table, engage other data team services such as creating workspace or modeled tables.
- **Building other models on top of it**: Registered queries cannot be referenced (`ref()`) by other dbt models. If you need to build downstream models, the full data model development process should be used instead.

## How to Request

1. Open an issue using the Registered Query issue template *(forthcoming)*.
2. Include the following in the issue:
   - The SQL query text you want registered.
   - Whether the results contain SAFE data (required — this determines which schema the query is placed in).
   - Optionally, whether you want to be listed as a code owner (you will then be required to approve any future changes).
   - Optionally, a column or list of columns to use for uniqueness testing.
3. Assign the issue to a data team developer.
4. When the data team notifies you in the issue that the MR is ready, review and approve it.

## What Happens After You Request

Once you submit the issue, the data team developer will:

1. Read your query and check your configuration against the existing schema and directory structure. If the configuration does not align with an existing directory, they will report back to you in the issue.
2. Check existing queries and models for significant overlap with your request. If your query closely matches something that already exists, they will report back with alternatives.
3. Open a merge request on a new branch using a standard naming format.
4. Add or update the SQL file using a standard `rq_<name>.sql` naming format, then format, lint, and compile the code, resolving any errors.
5. Generate documentation for the query.
6. Run CI jobs and request a bot review, resolving any feedback.
7. Assign a code owner (if configured) and a maintainer for final review.
8. Notify you in the issue that the MR is ready for your review.

After maintainer merge, a CI job automatically rebuilds all registered queries in production, making your query immediately available.

## Configuration Options

### Required

| Option | Description |
|--------|-------------|
| SAFE Data | Whether the query results contain SAFE data. This determines the schema the query is placed in. Every registered query must declare this. |

### Optional

| Option | Description |
|--------|-------------|
| Code Ownership | If selected, the identified team member(s) are registered as code owners and **must** approve any future changes after the initial merge. |
| Uniqueness Testing | If selected, a target column or list of columns will be used to test the uniqueness of query results. The data team may need to limit or remove the test if it does not meet performance standards. |

## Constraints

- All registered queries are materialized as **views**. This allows for continuous deployment without interrupting production dbt runs.
- All files use an `rq_` prefix (e.g. `rq_my_query.sql`). This aids in audits and signals to users the potential limitations of these objects.
- Registered queries are placed in an **independent schema** separate from the rest of the warehouse. The schema used depends on whether the query is SAFE or not. A general schema is provided as a default for teams that do not yet have a dedicated workspace.
- Registered queries **cannot be referenced** (`ref()`) by other dbt models. They exist in a private dbt group specifically to prevent this.
- Queries that have not been used for more than **90 days** are subject to removal during quarterly audits.
- Expected turnaround for new requests is **approximately 24 hours**. Note: the workflow is in the process of being automated and the manual process may not yet consistently meet this target.

## Repository Structure

Registered query files are organized under a `query_registry` directory by function and SAFE status:

```plaintext
query_registry/
  <function>/
    restricted_safe/
      rq_<name>.sql
    rq_<name>.sql
```

SAFE queries are placed under `restricted_safe/` within the appropriate function directory. Non-SAFE queries sit directly in the function directory.
