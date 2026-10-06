---
title: "Snowflake Guide"
description: "Snowflake Data Warehouse Guide"
---

## What and why

[Snowflake](https://www.snowflake.com/en/) is our Enterprise Data Warehouse (EDW) and is the core technology in our [Enterprise Data Platform](/handbook/enterprise-data/platform/#i-classfas-fa-cubes-fa-fw--text-orangeiour-data-stack).

## What does Snowflake Contain?

Snowflake contains all of our analytical data and [Data Sources](/handbook/enterprise-data/platform/#data-sources) defines the set of original/raw data available.

## Related Content

- [Access](/handbook/enterprise-data/platform/#warehouse-access)
- [Support Portal Access](/handbook/enterprise-data/platform/#snowflake-support-portal-access)
- [Compute Resources](/handbook/enterprise-data/platform/#compute-resources)
- [Data Masking](/handbook/enterprise-data/platform/#data-masking)
- [Backups](/handbook/enterprise-data/platform/#backups)
- [AI Function Guide](/handbook/enterprise-data/platform/snowflake/snowflake-ai-function/snowflake-ai-function.md)
- [Snowflake CLI](/handbook/enterprise-data/platform/snowflake/snowflake-cli/)

## Current access model

Snowflake access operates on a hybrid model depending on your account history and the level of access required.

### Current access architecture

Snowflake access at GitLab is split across multiple systems working together:

- **Lumos** serves as the request and approval solution for Snowflake access.
- **Okta SCIM** creates or updates Snowflake users when Lumos requests are approved, assigning (wrapper) roles:
  - `SNOWFLAKE_ANALYST_OKTA` (which inherits the underlying `SNOWFLAKE_ANALYST` role)
  - `SNOWFLAKE_ANALYST_SAFE_OKTA` (which inherits the underlying `SNOWFLAKE_ANALYST_SAFE` role)
- **Permifrost** remains the source of truth for all custom, team-specific, and extended Snowflake authorization beyond the baseline analyst roles. This includes functional roles (e.g., `analyst_marketing`) and dev database access. This can be requested either via Lumos (`Customer User`) or via an [Access Request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/).
- **Snowflake SSO**: provides the login tile and SSO access.

The Okta SCIM path is intended **only for the two access levels**: Analyst and Analyst SAFE. Anything beyond these two roles is managed through the [Permifrost](/handbook/enterprise-data/platform/permifrost/) process.

### Where Okta SCIM stops

The Okta SCIM provisioning path is designed for the two baseline access levels only: **Analyst** and **Analyst SAFE**.

1. **Pre-SCIM users**: If your Snowflake account existed before Okta SCIM was implemented, Okta SCIM will not provision your account.
2. **Custom or extended roles**: If you need team-specific roles (e.g., `analyst_marketing`), functional roles (e.g., `analyst_core`), or dev database access, those are managed separately through the Permifrost process.
3. **Mixed-role users**: Users who have both Lumos-managed baseline roles and Permifrost-managed custom roles exist in both systems. Lumos and Permifrost are separate layers and do not automatically mirror each other.

## Logging In

Login to Snowflake from Okta.

## Navigating the UI

The [Snowflake Quick Tour of the Web Interface](https://docs.snowflake.com/user-guide/ui-snowsight-quick-tour) provides comprehensive documentation for the UI.

## Snowflake account configuration

### ABORT_DETACHED_QUERY

[ABORT_DETACHED_QUERY](https://docs.snowflake.com/en/sql-reference/parameters#abort-detached-query) parameter is set on account level to `True`.

We often have cases where the connectivity was lost and the query keeps trying to run and still does not complete. It is meaningless for the query to keep running in these cases and adds no value. There is a grace period of 5 minutes. If the connectivity isn't fixed in 5 minutes, it stops the execution so the warehouses won't be running unnecessarily.

## Data Freshness

We leverage automatic monitors in `MonteCarlo` for monitoring the freshness of the data.

## Snowflake Warehouse Sizing Guide

### Key principles

1. **Start with `XS` by default** for all development work across all environments (Snowsight, Tableau, local dbt development, etc.). Only size up when a specific query or workflow requires it and subsequently size-down afterwards.

2. **Key signal for over-provisioning**: If your queries run on a warehouse larger than XS but complete in under 30 seconds, you're likely wasting credits.

### Warehouse Sizing Quick Reference

| Warehouse | Use Case | Partitions Scanned | Rough Row Count | Target Query Time |
|-----------|----------|-------------------|-----------------|-------------------|
| **XSmall (XS)** | Quick lookups, single row queries, small aggregations, dbt tests | <4,000 | 0-500M records | <2 minutes |
| **Small (S)** | Dashboard queries (pre-aggregated), light analytics, ad-hoc exploration | 2,000-8,000 | 250M-1B records | 30 sec - 2 min |
| **Medium (M)** | Standard analytics, moderate complexity joins, typical dbt models | 4,000-16,000 | 500M-3B records | 30 sec - 3 min |
| **Large (L)** | Heavy analytics, complex transformations, large table scans | 8,000-32,000 | 1B-5B records | 1-10 minutes |
| **XLarge (XL)** | Very large data processing, complex ETL, multi-table joins | 16,000-64,000 | 2B+ records | 2-30 minutes |
| **4XL+** | Massive transformations for production workloads (e.g., Snowplow backfills) | 128,000+ | 5B+ records | 10+ minutes |

**Note:**

- Row count ranges are **extremely rough guidelines that often overestimate** warehouse size. A 3B-row table filtered to 1 week may only need `XS`, not `M`. We provide them only as a quick starting reference.
- For more accurate sizing, use `partitions_scanned` (ranges provided by Snowflake Solutions Architects), visible via the [`explain` command](https://www.chaosgenius.io/blog/snowflake-explain-guide/), i.e `explain select * from my_table where my_filter;`

### Decision Framework: When to Size Up

For a more accurate warehouse selection, please consider the following 3 variables:

#### 1. Table Size (Starting Point)

<details>
<summary>Click to expand</summary>

Refer to the above markdown table for a starting warehouse size based on table record count.

**Always check your table size first:**

```sql
SELECT COUNT(*) FROM your_table;
```

</details>

#### 2. Filter Selectivity (Can You Stay Smaller?)

<details>
<summary>Click to expand</summary>

##### Time Range Filters (Most Powerful)

Time-based predicates are typically the most selective for time-series data:

- **1 day - 1 week**: Even massive tables can run on **XS**
- **2-4 weeks**: Consider **S** or **M** depending on base table size
- **Beyond 4 weeks**: Table size becomes the primary factor

##### Other Selective Filters

- **Highly selective** (e.g., `event_action`, `app_id`): Excellent for partition pruning; boolean flags can also be good for pruning
- **Weakly selective** (low cardinality fields like `user_id`, `event_id`): Minimal impact on scan size
- **Clustering key filters** (e.g., `behavior_at`): Most effective when aligned with table clustering

**Pro tip:** Add a `LIMIT` clause during development to avoid full result set materialization.

</details>

#### 3. Query Complexity (Need More Power?)

<details>
<summary>Click to expand</summary>

- **Simple scans**: Filters + aggregations → stay at recommended size
- **Heavy operations**: Large joins, window functions, complex aggregations → **size up one level**
- **Multi-table joins**: Especially with unfiltered dimensions → **size up 1-2 levels**

</details>

### Real Examples: `mart_behavior_structured_event`

These examples show that even for one of our largest tables, a `XS` can be sufficient:

<details>
<summary>Example 1: XS Suffices (With Narrow Time Range)</summary>

```sql
-- 51 seconds on DEV_XS
-- No LIMIT, but highly filtered time range (3 days)
SELECT *
FROM PROD.COMMON_MART.MART_BEHAVIOR_STRUCTURED_EVENT
WHERE BEHAVIOR_AT BETWEEN '2025-01-01' AND '2025-01-03'
  AND event_action = 'check_policy_scope_for_security_policy'
  AND app_id = 'gitlab';
```

**Why XS works:** 3-day time window + specific event_action = small scan

</details>

<details>
<summary>Example 2: XS is Acceptable (Aggregation, 2-Week Range)</summary>

```sql
-- 49 seconds on DEV_XS
-- Aggregation with moderate time range
SELECT
    event_action,
    COUNT(*) AS ct
FROM PROD.COMMON_MART.MART_BEHAVIOR_STRUCTURED_EVENT
WHERE BEHAVIOR_AT BETWEEN '2025-02-01' AND '2025-02-15'
GROUP BY ALL
HAVING ct > 50
ORDER BY ct DESC;
```

**Why XS works:** Aggregation reduces result set, 2-week window is manageable

</details>

<details>
<summary>Example 3: M Required (Large Join + Wider Range)</summary>

```sql
-- 71 seconds on DEV_M
-- Joins 2TB fact table (filtered) with 260GB dimension (unfiltered)
SELECT *
FROM prod.common.fct_behavior_website_page_view fct
JOIN prod.common.dim_behavior_website_page dim
  ON fct.dim_behavior_website_page_sk = dim.dim_behavior_website_page_sk
WHERE behavior_at >= CURRENT_DATE - 7
  AND dim.app_id = 'docs'
LIMIT 10000;
```

**Why M needed:** Large join + unfiltered dimension requires more memory

</details>

## VS Code Snowflake extension

To use Snowflake from VS Code, install the [Snowflake Extension for Visual Studio Code](https://docs.snowflake.com/en/user-guide/vscode-ext) from the Extensions pane.

**Setup:**

1. First, confirm you can log into the Snowflake UI via Okta in the browser.
2. Click the Snowflake icon in the VS Code left sidebar and sign in with the following:
   - **Account Identifier:** `gitlab`
   - **Auth Method:** Single sign-on
   - **Username:** your full GitLab email
3. Click **Sign in** — an Okta window will open. Complete SSO and return to VS Code.

Once connected, use the dropdowns in the Snowflake panel to set your role and warehouse.

From there, open any `.sql` file in VS Code and run queries directly without touching the web UI.
