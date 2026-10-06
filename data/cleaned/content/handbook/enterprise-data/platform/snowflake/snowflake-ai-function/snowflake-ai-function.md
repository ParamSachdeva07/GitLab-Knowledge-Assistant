---
title: "Snowflake AI Functions: Usage and Cost Management Guide"
description: "How to use Snowflake AI Functions effectively while managing costs and token consumption in GitLab's Enterprise Data Platform"
---

## Table of Contents

- [What is Snowflake AI Functions?](#what-is-snowflake-ai-functions)
- [Purpose](#purpose)
- [Prerequisites](#prerequisites)
- [Understanding Tokens and Credits](#understanding-tokens-and-credits)
- [Available AI Functions](#available-ai-functions)
- [Snowflake AI Functions: Fixed vs Variable Pricing](#snowflake-ai-functions-fixed-vs-variable-pricing)
- [⚡ Quick Start Checklist](#-quick-start-checklist)
- [Getting Started: 3-Step Approach](#getting-started-3-step-approach)
- [Is My Token Usage Reasonable?](#is-my-token-usage-reasonable)
- [Advanced Usage & Optimization](#advanced-usage--optimization)
- [Monitoring & Support](#monitoring--support)
- [Emergency Access Control Procedures - Data Platform Team](#emergency-access-control-procedures---data-platform-team)
- [AI Functions Access Management - Standard Operations](#ai-functions-access-management---standard-operations)
- [Related Resources](#related-resources)

## What is Snowflake AI Functions?

Snowflake AI Functions are built-in machine learning capabilities that enable data analysts and engineers to perform advanced analytics directly within our [Enterprise Data Warehouse](/handbook/enterprise-data/platform/snowflake/). These functions leverage Snowflake's native AI/ML capabilities to provide insights without requiring external tools or complex model deployments.

### AI Functions in Snowflake allow GitLab team members to

- Perform sentiment analysis on text data
- Extract insights from unstructured data
- Generate predictions and classifications
- Enhance data quality through intelligent data processing
- Accelerate time-to-insight for business decisions

⚠️ Important Cost Consideration: AI Functions use token-based billing separate from standard warehouse credits. Always estimate costs before processing large datasets.

## Purpose

This guide provides comprehensive guidance on using Snowflake AI Functions effectively while maintaining cost control. Given the token-based billing model, understanding cost implications is crucial for responsible usage within GitLab's data platform.

⚠️ Tableau and BI Tools: Do Not Call AI Functions Directly

Snowflake Cortex AI functions must not be called directly from Tableau or any other BI tool. Doing so causes AI functions to rerun on every query execution, which generates unpredictable costs and inconsistent results. Specific risks include:

- **Runaway credit consumption**: Every dashboard load, filter change, and scheduled refresh reruns the AI function, meaning a single popular dashboard can silently generate thousands of AI calls per day across all viewers.
- **No cost visibility**: Credit consumption accumulates per execution with no warning until it appears on your usage report, making it nearly impossible to budget or forecast.
- **Non-deterministic output**: Generative functions like `COMPLETE` return different results on each execution, so the same row will display different values across sessions, users, and refreshes.
- **No auditability**: Results computed at query time cannot be reviewed, validated, or reused downstream.

**Correct approach:** Run AI functions once in a controlled pipeline and persist the results to a Snowflake table. Connect your BI tool to that pre-computed table instead. Use a dbt model, Airflow pipeline, or Snowflake task to populate and incrementally refresh the output table as new source rows arrive. This ensures credits are consumed in a single predictable batch, results are stable and consistent for all users, and the output is reusable across multiple workbooks or downstream models.

## Prerequisites

Before using Snowflake AI Functions, ensure you have:

- **Snowflake Access**: Follow the [Warehouse Access](/handbook/enterprise-data/platform/#warehouse-access) process
- **Required Roles**: `CORTEX_FUNCTIONS` account role — see [How to Get Cortex AI Access](/handbook/enterprise-data/platform/snowflake/snowflake-ai-function/snowflake-ai-credits-alert/#how-to-get-cortex-ai-access)
- **Warehouse Access**: Access to appropriate compute warehouses (`dev_xs`, `dev_m`, or `reporting`)
- **Cost Awareness**: Understanding of token-based billing implications

## Understanding Tokens and Credits

### What is a Token?

A token is the smallest unit of text that AI models process, roughly equivalent to 4 characters or 3/4 of an English/text word.
Examples:

- "Hello" = ~1 token
- "Analyze this text" = ~3 tokens
- A typical email (200 words) = ~270 tokens
- A GitLab issue description (500 words) = ~670 tokens

### What are Credits?

Credits are Snowflake's billing unit for AI services and compute resources

<b>Credit Rates:</b> Snowflake bills Cortex AI credits at two distinct rates depending on the service type:

| Service Type | Relative Credit Rate | What It Covers |
|---|---|---|
| **AI_INFERENCE** | 1x (base rate) | Single-purpose, stateless AI SQL function calls — `COMPLETE()`, `SENTIMENT()`, `SUMMARIZE()`, `TRANSLATE()`, `EMBED_TEXT()`, `AI_CLASSIFY()`, `AI_FILTER()`, etc. |
| **AI_SERVICES** | ~10x | Higher-level orchestrated services (multiple LLM calls per request) — Cortex Analyst, Cortex Agent, Cortex Code (CoCo), Cortex Search |

> **Note**: For exact rates, query your account's `SNOWFLAKE.ORGANIZATION_USAGE.RATE_SHEET_DAILY`.

<b>Conversion:</b> Different models charge different rates per million tokens

<b>[Current Model Rates](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf) (Credits per million tokens):</b>

- `mistral-7b:`     0.12 credits/million tokens
- `mixtral-8x7b:`    0.22 credits/million tokens
- `llama3.1-70b:`    1.21 credits/million tokens
- `llama3.3-70b:`     1.21 credits/million tokens
- `claude-4-sonnet:`  2.55 credits/million tokens
- `deepseek-r1:`      1.03 credits/million tokens
- `snowflake-arctic:` 0.84 credits/million tokens

<b>Credit Usage Examples</b>

| Model | Credits per Million Tokens | Credits for 10M Tokens |
|-------|---------------------------|------------------------|
| mistral-7b | 0.12 | 1.2 |
| llama3.1-70b | 1.21 | 12.1 |
| claude-4-sonnet | 2.55 | 25.5 |

*AI_SERVICES (Cortex Agent, Analyst, Code) consume credits at ~10x the AI_INFERENCE rate. Query `RATE_SHEET_DAILY` for exact rates.

### Understanding Token-Based Billing

Snowflake AI services use token-based billing, distinct from standard warehouse credit billing:

- **AI Credits**: Depend on token usage (input + output tokens)
- **Warehouse Credits**: Separate billing based on runtime and warehouse size  
- **Token Calculation**: Based on the specific model used and text length processed
- **Cost Variability**: Different models have different token consumption rates

**Example**: Running a 1-hour query on a Large warehouse costs the same warehouse credits whether you process 100 or 100,000 records. However, AI function costs scale directly with the amount of text processed

## Available AI Functions

Snowflake provides several AI functions through the CORTEX namespace:

### Text Analysis Functions

| Function | Purpose | Cost (Credits/M Tokens) | Typical GitLab Use Cases |
|----------|---------|-------------------------|--------------------------|
| `SNOWFLAKE.CORTEX.SENTIMENT` | Analyze sentiment of text | 0.08 | Customer feedback, support ticket mood |
| `SNOWFLAKE.CORTEX.EXTRACT_ANSWER` | Extract answers from text | 0.08 | Issue root cause extraction, feature requirements |
| `SNOWFLAKE.CORTEX.SUMMARIZE` | Generate text summaries | 0.10 | MR summaries, release note generation |
| `SNOWFLAKE.CORTEX.TRANSLATE` | Translate between languages | 1.50 | Internationalization analysis |
| [`SNOWFLAKE.CORTEX.COMPLETE`](https://internal.gitlab.com/handbook/enterprise-data/platform/ai_to_data/technical_documentation_ai_to_data/#snowflake-cortex-complete) | Text completion/generation | 0.05-12.00* | Content generation, categorization |

*Varies by model selected

### Available Models for COMPLETE Function

| Model Tier | Examples | Cost Range | Best For |
|------------|----------|------------|----------|
| **Budget** | `mistral-7b`, `llama3.1-8b` | 0.05-0.12 | High-volume simple tasks, categorization |
| **Balanced** | `mixtral-8x7b`, `llama3.1-70b` | 0.22-1.21 | Most general-purpose tasks |
| **Performance** | `llama3.3-70b`, `snowflake-arctic` | 0.84-1.21 | Complex analysis, nuanced reasoning |
| **Premium** | `claude-4-sonnet`, `mistral-large2` | 1.95-2.55 | Customer-facing content, highest quality |

💡 **Cost Tip**: Use specialized functions (SENTIMENT, SUMMARIZE, EXTRACT_ANSWER) whenever possible - they're 3-30x cheaper than using COMPLETE for the same tasks!

## Snowflake AI Functions: Fixed vs Variable Pricing

### Fixed-Price Functions

These functions have **fixed costs** - no model selection required, consistent pricing:

**Basic Functions**  

| Function | Cost (Credits/M Tokens) | Purpose |
|----------|-------------------------|---------|
| `SNOWFLAKE.CORTEX.SENTIMENT` | 0.08 | Sentiment analysis |
| `SNOWFLAKE.CORTEX.EXTRACT_ANSWER` | 0.08 | Q&A extraction from text |
| `SNOWFLAKE.CORTEX.SUMMARIZE` | 0.10 | Text summarization |
| `SNOWFLAKE.CORTEX.GUARD` | 0.25 | Content safety filtering |

 **Advanced Functions**

| Function | Cost (Credits/M Tokens) | Purpose |
|----------|-------------------------|---------|
| `SNOWFLAKE.CORTEX.AI_TRANSCRIBE` | 1.30 | Speech to text conversion |
| `SNOWFLAKE.CORTEX.AI_CLASSIFY` | 1.39 | Advanced classification |
| `SNOWFLAKE.CORTEX.AI_FILTER` | 1.39 | Intelligent data filtering |
| `SNOWFLAKE.CORTEX.TRANSLATE` | 1.50 | Language translation |
| `SNOWFLAKE.CORTEX.AI_AGG` | 1.60 | AI-powered aggregation |
| `SNOWFLAKE.CORTEX.AI_SENTIMENT` | 1.60 | Enhanced sentiment analysis |
| `SNOWFLAKE.CORTEX.AI_SUMMARIZE_AGG` | 1.60 | Aggregated summarization |
| `SNOWFLAKE.CORTEX.ENTITY_SENTIMENT` | 1.60 | Entity-level sentiment |
| `SNOWFLAKE.CORTEX.AI_EXTRACT` | 2.55 | Advanced data extraction |

## Variable-Price Functions (Model Selection Required)

These functions require **model selection** and costs vary based on your choice:

| Function Category | Price Range (Credits/M Tokens) | Purpose |
|-------------------|--------------------------------|---------|
| `SNOWFLAKE.CORTEX.COMPLETE` | 0.05 - 12.00 | Text generation, completion, custom tasks |
| `SNOWFLAKE.CORTEX.EMBED_TEXT_768` | 0.03 | Basic text embeddings (768 dimensions) |
| `SNOWFLAKE.CORTEX.EMBED_TEXT_1024` | 0.05 - 0.07 | Advanced text embeddings (1024 dimensions) |
| `SNOWFLAKE.CORTEX.EMBED_IMAGE_1024` | 0.06 | Image and text embeddings |

## ⚡ Quick Start Checklist

Before using any AI functions:

- [ ] **Check your daily credit usage** (see monitoring query below)
- [ ] **Start with specialized functions** (SENTIMENT, SUMMARIZE) when possible - they're 3-30x cheaper
- [ ] **Use budget models** (mistral-7b) for initial testing
- [ ] **Always test on small samples** before processing full datasets

## Getting Started: 3-Step Approach

### Step 1: Test on Sample Data First

Always start with a small sample to understand function behavior and token consumption:

```sql
-- Test sentiment analysis on sample data
SELECT 
    email,
    SNOWFLAKE.CORTEX.SENTIMENT(email) as sentiment_score,
    SNOWFLAKE.CORTEX.COUNT_TOKENS('mistral-7b', email) as tokens_used
FROM RAW.AIRFLOW_STITCH.AB_USER
SAMPLE (10 ROWS)
ORDER BY tokens_used DESC;
```

- Note: For SENTIMENT, no token counting needed (fixed cost function)
- Token counting mainly applies to COMPLETE function

### Step 2: Estimate Costs Before Full Run

Calculate estimated costs before processing your entire dataset:

```sql
-- Calculate estimated cost before processing full table
WITH sample_estimate AS (
    SELECT 
        COUNT(*) as sample_rows,
        SUM(SNOWFLAKE.CORTEX.COUNT_TOKENS(
            'mistral-7b',
            'Your prompt here: ' || your_column
        )) as sample_tokens
    FROM your_table
    SAMPLE (100 ROWS)  -- Sample 100 rows
),
cost_projection AS (
    SELECT 
        sample_tokens,
        sample_rows,
        (SELECT COUNT(*) FROM your_table) as total_rows,
        sample_tokens * total_rows / sample_rows as estimated_total_tokens
    FROM sample_estimate
)
SELECT
    estimated_total_tokens / 1000000 as estimated_million_tokens,
    estimated_million_tokens * 0.12 as estimated_credits  -- Check current rates
FROM cost_projection;
```

### Step 3: Process in Controlled Batches

For large datasets, process data in manageable batches:

```sql
-- Process data in daily batches
SELECT
    date_day,
    issue_id,
    SNOWFLAKE.CORTEX.COMPLETE(
        'mistral-7b',
        'Categorize this GitLab issue: ' || title || '. Categories: bug, feature, documentation'
    ) as issue_category
FROM RAW.AIRFLOW_STITCH.AB_USER
WHERE date_day = '2024-01-01'  -- Process one day at a time
ORDER BY issue_id;
```

## Is My Token Usage Reasonable?

### Daily Usage Planning: How Much Can I Process Today?

To control costs, each user with Cortex AI access has a daily credit budget enforced by the [Cortex AI Credit Monitoring System](/handbook/enterprise-data/platform/snowflake/snowflake-ai-function/snowflake-ai-credits-alert/). These hard budgets are a safety net because Snowflake Cortex costs can escalate quickly and unintentionally. Limits can be adjusted by the Data Platform Team upon request.

**Your Daily Budget: 50 Credits (default)** | **Resets at 00:00 UTC**

**DAILY LIMIT ENFORCEMENT (Automated)**

The monitoring system checks usage every 30 minutes and takes action automatically:

- **DIRECT users** (granted `CORTEX_FUNCTIONS` via Permifrost): Access is **automatically revoked** when you exceed 100%. Restored on the next Permifrost run.
- **INHERITED users** (access via `SNOWFLAKE_DB` role): Access **cannot be auto-revoked**. The triager is notified for manual intervention.

| Zone | Credits Used | What Happens |
|------|--------------|--------------|
| **Safe** | 0–24 credits (< 50%) | No action |
| **Monitor** | 25–37 credits (50–74%) | Logged only — no email |
| **Warning** | 37–44 credits (75–89%) | Email notification sent to you |
| **Urgent** | 45–49 credits (90–99%) | Urgent email sent to you |
| **Critical** | 50+ credits (100%+) | Access revoked (DIRECT) or triager escalation (INHERITED) |

For full details on thresholds, cost impact, and escalation procedures, see the [Cortex AI Credit Monitoring System](/handbook/enterprise-data/platform/snowflake/snowflake-ai-function/snowflake-ai-credits-alert/) handbook.

Quick check: How many credits do I have left today?

```sql
SELECT USER_NAME, STATUS, CREDITS_USED_TODAY, DAILY_HARD_LIMIT,
       CREDITS_REMAINING, PERCENTAGE_USED, CREDIT_SOURCES
FROM RAW.CORTEX_MONITORING.CURRENT_USAGE_MONITOR
WHERE USER_NAME = CURRENT_USER();
```

## Advanced Usage & Optimization

### Token Counting Best Practices

- Always validate token estimates using Snowflake’s built-in functions (SNOWFLAKE.CORTEX.COUNT_TOKENS).

- Concatenate prompts and data per row to precisely calculate token usage:

```sql
SELECT
    SUM(
        SNOWFLAKE.CORTEX.COUNT_TOKENS(
            'llama3.1-70b',
            'fixed prompt text here ' || data_column
        )
    ) AS total_token_usage
FROM your_table;
```

**Critical Rule:** Count tokens on the complete concatenated string (prompt + data), not separately. This avoids ±5% estimation errors due to token boundaries, delimiters, or encoding differences.

Count tokens on this combined string per row and sum across all rows:

```sql
SELECT
    SUM(
        SNOWFLAKE.CORTEX.COUNT_TOKENS(
            'llama3.1-70b',
            'your prompt here ' || your_column
        )
    ) AS precise_token_estimation
FROM your_table;
```

### Cost Optimization Strategies

**1. Function Selection Priority**

- First choice: Use specialized functions (SENTIMENT, SUMMARIZE, EXTRACT_ANSWER) when possible
- Second choice: Budget models for COMPLETE function (mistral-7b, llama3.1-8b)
Use shorter prompts and limit input data size wherever possible.

**2. Data Preprocessing**

- Apply WHERE clauses before AI functions to reduce data volume
- Process only meaningful content (filter out empty or very short text)

**3. Smart Batching**

- Process similar data together for consistency
- Use daily batches rather than real-time processing
- Store and reuse results to avoid reprocessing

### Token Usage Comparison

Token usage varies significantly between models. Here's a practical comparison:

```sql
-- Compare token usage across models for the same text
WITH sample_text AS (
    SELECT 'Analyze customer feedback for product improvement opportunities' as text
)
SELECT 
    'mistral-7b' as model,
    SNOWFLAKE.CORTEX.COUNT_TOKENS('mistral-7b', text) as token_count
FROM sample_text
UNION ALL
SELECT 
    'llama3.1-70b' as model,
    SNOWFLAKE.CORTEX.COUNT_TOKENS('llama3.1-70b', text) as token_count
FROM sample_text
UNION ALL
SELECT 
    'mixtral-8x7b' as model,
    SNOWFLAKE.CORTEX.COUNT_TOKENS('mixtral-8x7b', text) as token_count
FROM sample_text;
```

![Token Usage Comparison](/images/enterprise-data/snowflake-ai-function/model_comparison.png)

**Selection Strategy:** Start with mistral-7b for initial testing, then upgrade only when accuracy requirements justify the additional cost.

## Monitoring & Support

### Daily Usage Tracking

Monitor your daily credit consumption against your daily limit (default: 50 credits). Use the monitoring view for a real-time snapshot:

```sql
SELECT USER_NAME, STATUS, CREDITS_USED_TODAY, DAILY_HARD_LIMIT,
       CREDITS_REMAINING, PERCENTAGE_USED, CREDIT_SOURCES
FROM RAW.CORTEX_MONITORING.CURRENT_USAGE_MONITOR
WHERE USER_NAME = CURRENT_USER();
```

For the full monitoring system, thresholds, and triager procedures, see the [Cortex AI Credit Monitoring System](/handbook/enterprise-data/platform/snowflake/snowflake-ai-function/snowflake-ai-credits-alert/) handbook.

### High-Cost Query Identification

```sql
SELECT
    u.NAME AS USER_NAME,
    DATE(cai.USAGE_TIME) AS USAGE_DATE,
    cai.MODEL_NAME,
    SUM(cai.TOKEN_CREDITS) AS TOTAL_CREDITS,
    SUM(cai.TOKENS) AS TOTAL_TOKENS,
    COUNT(*) AS REQUEST_COUNT
FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_AISQL_USAGE_HISTORY cai
JOIN SNOWFLAKE.ACCOUNT_USAGE.USERS u ON cai.USER_ID = u.USER_ID
WHERE u.NAME = CURRENT_USER()
  AND cai.USAGE_TIME >= DATEADD('day', -30, CURRENT_TIMESTAMP())
GROUP BY u.NAME, DATE(cai.USAGE_TIME), cai.MODEL_NAME
ORDER BY TOTAL_CREDITS DESC
LIMIT 10;
```

### Troubleshooting Common Issues

#### High Token Consumption

**Problem: Approaching or exceeding daily credit limits**

**Diagnostic Steps:**

- Check which functions consumed the most credits
- Review prompt efficiency
- Verify model selection appropriateness

Solutions:

- Switch to specialized functions when possible
- Use budget models (mistral-7b, llama3.1-8b) for initial analysis
- Implement more aggressive data filtering
- Process in smaller, controlled batches

#### Function Timeouts

**Problem: AI function queries failing or timing out**

Solutions:

- Use larger compute warehouses (dev_m instead of dev_xs)
- Reduce batch sizes (process 1,000 records instead of 10,000)
- Simplify prompts to reduce processing complexity
- Split complex queries into multiple steps

#### Inconsistent Results

**Problem: AI functions returning variable or unexpected outputs**

Solutions:

- Use more specific, structured prompts
- Include examples in prompts for better consistency
- Consider upgrading to higher-accuracy models
- Implement result validation and retry logic

## Emergency Access Control Procedures - Data Platform Team

**Audience**: Data Platform Team administrators only.
**Purpose**: Emergency lockdown of all Cortex AI functions account-wide.
**Warning**: These procedures will disable AI functions for **every user** in the account.

### RED BUTTON: Immediate Account-Wide Cortex Shutdown

<div style="border: 3px solid red; background-color: #fff0f0; padding: 15px; border-radius: 5px; margin-bottom: 15px;">

<p style="color: red; font-weight: bold; font-size: 1.2em;">If Cortex AI credit consumption is out of control and you need to shut it down for the entire account immediately, run this single command as ACCOUNTADMIN:</p>

```sql
USE ROLE ACCOUNTADMIN;
ALTER ACCOUNT SET CORTEX_MODELS_ALLOWLIST = 'None';
```

<p>This instantly blocks <b>all</b> Cortex AI model invocations for every user and role in the account. No Cortex function (<code>COMPLETE</code>, <code>SENTIMENT</code>, <code>SUMMARIZE</code>, Cortex Agents, Cortex Analyst, Cortex Code, etc.) will work until the allowlist is restored.</p>

</div>

> **Why this is the primary control:** SNOWFLAKE is an APPLICATION, and database role revokes are unreliable — legacy grants from pre-2020 cannot be individually revoked, and `SNOWFLAKE_DB` provides broad inherited access that cannot be surgically restricted. The `CORTEX_MODELS_ALLOWLIST` parameter is the **only** control that universally blocks all Cortex model invocations regardless of access path (DIRECT, INHERITED, or LEGACY). See [Cortex Access Architecture](#cortex-access-architecture) for details.

**Verify the kill switch took effect:**

```sql
SHOW PARAMETERS LIKE 'CORTEX_MODELS_ALLOWLIST' IN ACCOUNT;
-- Should show 'None'
```

### When to Use the RED BUTTON

- Runaway cost: total account Cortex spend is accelerating beyond acceptable thresholds
- Security incident involving AI functions
- Compliance or legal requirement for immediate cessation
- Automated per-user monitoring is insufficient (e.g., many users spiking simultaneously)

### Restoration (After Incident Resolution)

**Business approval required** before restoring access.

#### Step 1: Re-enable the Model Allowlist

```sql
USE ROLE ACCOUNTADMIN;
ALTER ACCOUNT SET CORTEX_MODELS_ALLOWLIST =
    'claude-4-sonnet,snowflake-arctic,snowflake-arctic-embed-m-v1.5,llama3.1-8b,llama3.1-70b,llama3.3-70b,mistral-7b,arctic-translate,arctic-extract,arctic-sentiment,arctic-parse-document,arctic-extract-answer,arctic-summarize';

SHOW PARAMETERS LIKE 'CORTEX_MODELS_ALLOWLIST' IN ACCOUNT;
```

> **Allowlist model tiers:**
>
> | Tier | Models | Rationale |
> |------|--------|-----------|
> | **Production** | `claude-4-sonnet`, `snowflake-arctic`, `snowflake-arctic-embed-m-v1.5` | Actively used by AIRFLOW pipelines and embedding workflows |
> | **Cost-effective** | `llama3.1-8b`, `llama3.1-70b`, `llama3.3-70b`, `mistral-7b` | Low-cost open models for general development use |
> | **Managed function aliases** | `arctic-translate`, `arctic-extract`, `arctic-sentiment`, `arctic-parse-document`, `arctic-extract-answer`, `arctic-summarize` | Required by [BCR-2220](https://docs.snowflake.com/en/release-notes/bcr-bundles/2026_02/bcr-2220) — managed AI functions will enforce the allowlist |

If you want to allow **all** models (return to pre-lockdown state):

```sql
ALTER ACCOUNT UNSET CORTEX_MODELS_ALLOWLIST;
```

#### Step 2: Resume Monitoring Tasks

```sql
ALTER TASK RAW.CORTEX_MONITORING.MONITOR_CORTEX_USAGE_TASK RESUME;
ALTER TASK RAW.CORTEX_MONITORING.RESTORE_DAILY_ACCESS_TASK RESUME;
```

#### Step 3: Verify Restoration

```sql
SELECT SNOWFLAKE.CORTEX.COMPLETE('llama3.1-8b', 'Restoration test');
-- Should succeed

SELECT COUNT(*) AS monitored_users
FROM RAW.CORTEX_MONITORING.USER_THRESHOLDS
WHERE IS_ACTIVE = TRUE;
```

### Post-Incident

1. **Document**: Record all actions taken, timeline, and root cause in a triage issue
2. **Notify stakeholders**: Confirm lockdown/restoration status
3. **Review thresholds**: Consider lowering per-user limits if the incident was cost-driven
4. **Update runbook**: Add any new learnings to the [triager runbook](/handbook/enterprise-data/platform/snowflake/snowflake-ai-function/snowflake-ai-credits-alert/)

## AI Functions Access Management - Standard Operations

### Cortex Access Architecture

Snowflake's `SNOWFLAKE` object is an **APPLICATION** (not a regular database). This has critical implications for how Cortex database roles are granted, inherited, and revoked. There are three distinct access paths:

| Path | Role | Mechanism | Revocable? | Monitoring Enforcement |
|------|------|-----------|------------|----------------------|
| **DIRECT** | `CORTEX_FUNCTIONS` | Permifrost grants 6 Cortex database roles individually | Yes — per-user revoke/restore | Auto-revoke on limit breach |
| **INHERITED** | `SNOWFLAKE_DB` | `USAGE ON APPLICATION SNOWFLAKE` → all 37+ database roles | Only by revoking `SNOWFLAKE_DB` from the user (breaks all SNOWFLAKE access) | Triager notification (cannot auto-revoke) |
| **LEGACY** | Various group roles | Pre-2020 `USAGE ON DATABASE SNOWFLAKE` grants that became APPLICATION-managed metadata | **No** — `REVOKE` returns success but has no effect | N/A — these are metadata artifacts, not effective access |

**Roles with current `USAGE ON APPLICATION SNOWFLAKE`** (the only roles with effective inherited Cortex access):

| Role | Granted | Purpose |
|------|---------|---------|
| `SYSADMIN` | 2019-05-08 | Top-level admin |
| `SNOWFLAKE_DB` | 2020-03-09 | Consolidated SNOWFLAKE access for user roles |
| `READ_ALL` | 2020-06-11 | Read-only access role |
| `SNOWFLAKE_ACCOUNT_USAGE` | 2022-11-01 | Account usage views |
| `DATA_OBSERVABILITY` | 2025-10-09 | Data observability tooling |

**Legacy grants (non-revocable):** `SHOW GRANTS OF DATABASE ROLE SNOWFLAKE.CORTEX_USER` shows ANALYST_PEOPLE, ANALYST_SALES, DATA_MANAGER, ENGINEER, PRODUCT_MANAGER, REPORTER_SENSITIVE, and TRANSFORMER with timestamps from 2019. These are APPLICATION-managed metadata from when these roles had direct `USAGE ON DATABASE SNOWFLAKE` (revoked in March 2020 during the SNOWFLAKE_DB consolidation). Individual `REVOKE DATABASE ROLE` commands return success but do not remove these entries. They do **not** represent effective access — these roles only have Cortex access if they inherit from one of the 5 roles listed above.

> **Key takeaway:** The `CORTEX_MODELS_ALLOWLIST` account parameter is the **only** control that universally blocks Cortex across all access paths. Database role revokes are unreliable for the SNOWFLAKE APPLICATION.

### Access Provisioning

Cortex AI access is managed through two paths:

**Path 1: DIRECT — `CORTEX_FUNCTIONS` via Permifrost (recommended)**

This is the governed, per-user controllable path. The monitoring system can auto-revoke and restore access for users on this path.

1. Open a merge request in the [`snowflake-permissions`](https://gitlab.com/gitlab-data/snowflake-permissions) repository
2. Add `CORTEX_FUNCTIONS` to the user's role in `roles.yml` under `member_of:`
3. Merge — Permifrost applies the grant automatically

**Path 2: INHERITED — via `SNOWFLAKE_DB`**

Roles that are members of `SNOWFLAKE_DB` inherit all SNOWFLAKE database roles, including all Cortex roles. This path **cannot** be surgically restricted — revoking Cortex would require removing `SNOWFLAKE_DB` entirely, which breaks access to ACCOUNT_USAGE views and other SNOWFLAKE objects. The monitoring system handles these users via triager escalation rather than auto-revoke.

For full details, see [How to Get Cortex AI Access](/handbook/enterprise-data/platform/snowflake/snowflake-ai-function/snowflake-ai-credits-alert/#how-to-get-cortex-ai-access).

### Model-Level Access Control (Allowlist Governance)

The `CORTEX_MODELS_ALLOWLIST` account parameter controls which Cortex AI models can be invoked. Only `ACCOUNTADMIN` can modify it.

**Current status:** `ALL` (no restrictions). **Recommendation:** Enforce the allowlist below to control costs and prevent unauthorized model usage.

```sql
USE ROLE ACCOUNTADMIN;

-- Enforce the approved model allowlist
ALTER ACCOUNT SET CORTEX_MODELS_ALLOWLIST =
    'claude-4-sonnet,snowflake-arctic,snowflake-arctic-embed-m-v1.5,llama3.1-8b,llama3.1-70b,llama3.3-70b,mistral-7b,arctic-translate,arctic-extract,arctic-sentiment,arctic-parse-document,arctic-extract-answer,arctic-summarize';

-- Verify
SHOW PARAMETERS LIKE 'CORTEX_MODELS_ALLOWLIST' IN ACCOUNT;
```

| Tier | Models | Rationale |
|------|--------|-----------|
| **Production** | `claude-4-sonnet`, `snowflake-arctic`, `snowflake-arctic-embed-m-v1.5` | Actively used by AIRFLOW pipelines and embedding workflows |
| **Cost-effective** | `llama3.1-8b`, `llama3.1-70b`, `llama3.3-70b`, `mistral-7b` | Low-cost open models for general development use |
| **Managed function aliases** | `arctic-translate`, `arctic-extract`, `arctic-sentiment`, `arctic-parse-document`, `arctic-extract-answer`, `arctic-summarize` | Required by [BCR-2220](https://docs.snowflake.com/en/release-notes/bcr-bundles/2026_02/bcr-2220) — managed AI functions will enforce the allowlist |

**Blocked models** (not in allowlist): `claude-3-5-sonnet`, `claude-3-7-sonnet`, `claude-sonnet-4-5`, `claude-sonnet-4-6`, `mixtral-8x7b`, `mistral-large2`, `deepseek-r1`. These are either higher-cost Claude variants or unused models.

**How it works:**

- `ALL` (default) — all models allowed (no restriction)
- `None` — all models blocked ([RED BUTTON](#red-button-immediate-account-wide-cortex-shutdown))
- Comma-separated list — only listed models and aliases are permitted

To allow all models (remove restrictions):

```sql
ALTER ACCOUNT UNSET CORTEX_MODELS_ALLOWLIST;
```

**When to update:** Review quarterly or when onboarding new Cortex use cases. Add models only after cost-impact assessment.

### Test Access

```sql
USE ROLE <username>;
SELECT SNOWFLAKE.CORTEX.COMPLETE('llama3.1-8b', 'Hello, world!');
-- Should succeed if user has CORTEX_FUNCTIONS
```

### Getting Help

1. **Data Team Support**: Create an issue in the [analytics project](https://gitlab.com/gitlab-data/analytics/-/issues)
2. **Slack Channels**:
   - `#data-team` for general questions and usage help
   - `#data-engineering` for technical issues
   - `@dataplatformtriage` for urgent monitoring alerts
3. **Cost Concerns**: Contact the Data Platform Team for cost optimization guidance or limit adjustments
4. **Monitoring System**: See the [Cortex AI Credit Monitoring System](/handbook/enterprise-data/platform/snowflake/snowflake-ai-function/snowflake-ai-credits-alert/) for thresholds, procedures, and runbook

## Related Resources

### Internal GitLab Resources

- [Snowflake Guide](/handbook/enterprise-data/platform/snowflake/) - Main Snowflake documentation
- [dbt Guide](/handbook/enterprise-data/platform/dbt-guide/) - Data transformation best practices
- [SQL Style Guide](/handbook/enterprise-data/platform/sql-style-guide/) - SQL coding standards
- [Data Platform Overview](/handbook/enterprise-data/platform/) - Enterprise Data Platform architecture
- [Interacting with Data Using AI](https://internal.gitlab.com/handbook/enterprise-data/platform/ai_to_data/)

### External Documentation

- [Snowflake Cortex AI Functions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions)
- [Snowflake AI Function Pricing](https://docs.snowflake.com/en/user-guide/cost-understanding-ai-features)
- [Snowflake Performance Optimization](https://docs.snowflake.com/en/user-guide/performance-query)

By consistently applying these guidelines, teams can effectively leverage Snowflake AI capabilities while maintaining control over expenses.
