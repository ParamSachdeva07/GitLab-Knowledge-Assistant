---
title: "Evaluating if data pipeline can be deprecated"
---

When a pipeline fails, ask: **"Should this pipeline be fixed, or can it be deprecated?"**

## Evaluation Process

### Step 1: Check dbt Model Usage

**Tool:** MonteCarlo

1. Find the **most downstream models** from the failed pipeline
2. Locate the asset and check its **Table Lineage**
3. **Review query activity**: Check if ANY table in the lineage has been queried in the last **60 days**
   - ✅ **Recent queries found** → Pipeline is actively used
   - ❌ **No queries in 60 days** → Flag for potential deprecation

### Step 2: Find Connected Dashboards

**Tool:** MonteCarlo

1. Navigate from table lineage to **Downstream Reports**
2. Filter for Tableau content:
   - `Tableau Workbook`
   - `Tableau Live Data Source`

### Step 3: Analyze Dashboard Usage

**Tool:** [Tableau Dashboard Viewership Dashboard](https://10az.online.tableau.com/#/site/gitlab/views/DashboardViewershipandUsage/BusinessUsers-DashboardViewership?:iid=2)

**Quick checks:**

1. **Location check**: Is the dashboard already in the `Admin Archive` folder?
   - ✅ **Yes** → Already deprecated, safe to remove pipeline
2. **Filter by dashboard name** (top left input)
3. **Check recent usage** in `Workbook - Dashboard Views per Month` chart (bottom left)
4. **Interpret results**:
   - **Rightmost month** = most recent usage
   - **Missing current month** = no usage this month

### Step 4: Make the Decision

**Deprecate if ALL conditions are met:**

- ❌ No dbt model queries in last 60 days
- ❌ No dashboard views in last 60 days
- ❌ No other downstream usage identified

**Before deprecating:**

- ✋ **Confirm with stakeholders** (data owners, business users)
- 📋 **Document the decision**

### Step 5: Execute Deprecation

**Actions:**

1. **Remove the data pipeline** which includes all code and data
2. **Archive Tableau content**: Contact BI team in `#data-tableau` Slack channel

---

## Quick Decision Tree

```shell
Pipeline Failed
    ↓
Models queried in 60 days? ──→ YES ──→ Fix the pipeline
    ↓ NO
Dashboards viewed in 60 days? ──→ YES ──→ Fix the pipeline
    ↓ NO
Stakeholder confirmation? ──→ NO ──→ Keep pipeline
    ↓ YES
Deprecate pipeline + Archive dashboards
```
