---
title: "Feature Store"
description: "GitLab's Snowflake-native feature store for ML feature management, serving, and retrieval."
---

## Feature Store

The Feature Store is GitLab's centralized system for managing, computing, and serving machine learning features. It is built on Snowflake's native Feature Store capabilities and uses parameterized SQL User-Defined Functions (UDFs) to generate features on demand for any date and lookback window — without pre-computing all historical data.

The source code lives in the [snowflake-feature-store](https://gitlab.com/gitlab-data/data-science-projects/snowflake-feature-store) project.

### How It Works

Features are defined as SQL UDFs that accept three parameters: `FEATURE_DATE`, `LOOKBACK_WINDOW_VALUE`, and `LOOKBACK_WINDOW_UNIT`. When a UDF is deployed, the system creates a dynamic view based on the values of the passed parameters and registers that view as a Feature View in Snowflake's Feature Store. Data scientists retrieve features by specifying which feature views they need, a spine query defining their modeling population, and the date/lookback parameters for their use case.

The data flow is: `Existing dbt tables → UDFs (parameterized SQL) → Dynamic Views → Feature Views → Feature Store API → Python / Jupyter`

### Key Concepts

#### Entities

An entity is the primary key (join key) of a feature view. The feature store currently supports two entities:

- `dim_namespace_id` — GitLab namespace identifier
- `dim_crm_account_id` — Account identifier

Entities are defined in `entities/entities.yaml` and registered in Snowflake during deployment. All feature views sharing the same entity can be joined together when serving.

#### Feature Views

A feature view is a named collection of related features, backed by a single UDF. Each feature view is configured in a domain-specific `feature_views.yaml` file with:

```yaml
feature_views:
  namespace_product_stage:
    version: "1.0"
    udf_name: "NAMESPACE_PRODUCT_METRICS_UDF"
    entity: "dim_namespace_id"
    timestamp_col: "feature_date"
    description: "Monthly product adoption metrics for namespaces"
    updated_by: "kdietz"
    updated_at: "2026-04-15"
```

#### UDFs (User-Defined Functions)

UDFs are SQL functions that contain the feature computation logic. Every UDF follows a standard signature with three parameters:

```sql
CREATE OR REPLACE FUNCTION MY_FEATURE_UDF(
    FEATURE_DATE DATE DEFAULT CURRENT_DATE() - 1,
    LOOKBACK_WINDOW_VALUE INT DEFAULT 1,
    LOOKBACK_WINDOW_UNIT VARCHAR DEFAULT 'month'
)
RETURNS TABLE(
    dim_namespace_id VARCHAR,
    feature_date DATE,
    ...
)
LANGUAGE SQL
AS $$ ... $$;
```

All three parameters are required in every UDF signature, even if not all are used in the SQL body. Entity columns must always be cast to `VARCHAR` for consistency across feature views.

#### Feature Descriptions

Each feature view has a companion YAML file that documents every output column. These descriptions are automatically attached to the feature view in Snowflake:

```yaml
descriptions:
  feature_A: "Description of Feature A"
  feature_B: "Description of Feature B"
```

## Feature Domains

Features are organized by business domain for maintainability and discoverability. For example:

| Domain | Description | Example Feature Views |
|--------|-------------|----------------------|
| `product` | Product usage, adoption | `namespace_product_usage`, `namespace_duo_saas_usage` |
| `sales` | Opportunities, activities, billing | `account_sales_activities` |
| `customer_success` | Customer health and engagement | `account_health_scores` |
| `support` | Support ticket metrics | `account_support_tickets` |
| `marketing` | Marketing attribution | `account_marketing_touchpoints` |

Each domain directory follows this structure:

```console
features/{domain}/
├── feature_views.yaml               # Feature view definitions
├── descriptions/                    # Per-feature-view documentation
│   └── {feature_view_name}.yaml
└── udfs/                            # SQL UDFs
    └── {feature_view_name}.sql
```

### Repository Structure

```console
snowflake-feature-store/
├── notebooks/
│   ├── update_feature_store.ipynb   # Deploy features (dev workflow)
│   └── serving_features.ipynb       # Retrieve features for ML models
├── src/
│   ├── feature_store_manager.py     # Core orchestrator
│   ├── update_features.py           # CLI entrypoint for deployment
│   ├── detect_changes.py            # Git-based change detection
│   ├── ci_deploy.py                 # CI/CD wrapper
│   └── utils/
│       ├── config_loader.py         # YAML configuration management
│       └── udf_type_validator.py    # UDF return type validation
├── features/{domain}/               # Domain-organized features
├── entities/entities.yaml           # Entity definitions
├── config/snowflake_config.yaml     # Environment configuration
├── .gitlab-ci.yml                   # CI/CD pipeline
├── Dockerfile                       # Container for CI
└── pyproject.toml                   # Python dependencies
```

### Environments

The feature store uses three environments:

| Environment | Database | Purpose | Workflow |
|-------------|----------|---------|----------|
| **Dev** | `{ROLE}_PROD` (e.g., `KDIETZ_PROD`) | Personal development and testing | Use `notebooks/update_feature_store.ipynb` |
| **Staging** | Shared CI environment | Pre-production validation | Triggered via MR CI pipeline |
| **Production** | `FEATURE_STORE.SF_FEATURE_STORE` | Production feature serving | Deployed automatically on merge to `main` |

### Getting Started

#### Prerequisites

- Python 3.12+
- JupyterLab, Jupyter Notebook, or VSCode
- Snowflake account with appropriate permissions
- dbt profile configured for Snowflake connection

#### Installation

```bash
git clone https://gitlab.com/gitlab-data/data-science-projects/snowflake-feature-store.git
cd snowflake-feature-store
uv sync
./.venv/bin/jupyter lab build --minimize=False
./.venv/bin/jupyter lab --port=8888
```

#### Snowflake Connection

Add entries to your `~/.dbt/profiles.yml` depending on your use case.

**To serve features (read-only access to production):**

```yaml
gitlab-snowflake:
  outputs:
    feature_store_serve:
      type: snowflake
      threads: 8
      account: gitlab
      user: YOUR_EMAIL@GITLAB.COM
      role: YOUR_ROLE
      database: FEATURE_STORE
      warehouse: DEV_XS
      schema: SF_FEATURE_STORE
      authenticator: externalbrowser
```

**To develop or modify features (personal dev database):**

```yaml
gitlab-snowflake:
  outputs:
    feature_store_dev:
      type: snowflake
      threads: 8
      account: gitlab
      user: YOUR_EMAIL@GITLAB.COM
      role: YOUR_ROLE
      database: {ROLE}_PROD
      warehouse: DEV_XS
      schema: SF_FEATURE_STORE
      authenticator: externalbrowser
```

### Development Workflow

Adding or modifying features follows a three-stage process: develop locally, validate in staging, and deploy to production.

#### Step 1: Local Development

All feature development starts locally using your personal Snowflake database and the `update_feature_store.ipynb` notebook. This lets you iterate on UDFs and test against real data without affecting anyone else.

**Create or modify your feature files:**

1. **UDF** — Add or edit a SQL file in the appropriate domain's `udfs/` directory. The UDF must include all three standard parameters with defaults:

    ```sql
    -- features/product/udfs/my_new_feature.sql
    CREATE OR REPLACE FUNCTION MY_NEW_FEATURE_UDF(
        FEATURE_DATE DATE DEFAULT CURRENT_DATE() - 1,
        LOOKBACK_WINDOW_VALUE INT DEFAULT 1,
        LOOKBACK_WINDOW_UNIT VARCHAR DEFAULT 'month'
    )
    RETURNS TABLE(
        dim_namespace_id VARCHAR,
        feature_date DATE,
        my_feature_column NUMBER
    )
    LANGUAGE SQL
    AS
    $$
    SELECT
        CAST(dim_namespace_id AS VARCHAR) AS dim_namespace_id,
        FEATURE_DATE AS feature_date,
        COUNT(*) AS my_feature_column
    FROM some_dbt_table
    WHERE event_date BETWEEN
        DATEADD(LOOKBACK_WINDOW_UNIT, -LOOKBACK_WINDOW_VALUE, FEATURE_DATE::DATE)
        AND FEATURE_DATE::DATE
    GROUP BY 1
    $$;
    ```

2. **Feature view config** — Add an entry to `features/{domain}/feature_views.yaml`:

    ```yaml
    feature_views:
      my_new_feature:
        version: "1.0"
        udf_name: "MY_NEW_FEATURE_UDF"
        entity: "dim_namespace_id"
        timestamp_col: "feature_date"
        description: "Description of what this feature view captures"
        updated_by: "your_name"
        updated_at: "2026-04-15"
    ```

3. **Feature descriptions** — Create `features/{domain}/descriptions/my_new_feature.yaml`:

    ```yaml
    descriptions:
      my_feature_column: "Description of this specific feature column"
    ```

4. **Entity** (if needed) — If your feature uses a new entity, add it to `entities/entities.yaml`:

    ```yaml
    entities:
      my_new_entity:
        name: "my_new_entity"
        join_keys: ["my_new_entity"]
        description: "Description of this entity"
    ```

**Deploy to your dev database:**

Open `notebooks/update_feature_store.ipynb` and set `PROFILE_TARGET = "feature_store_dev"`. This connects to your personal database (e.g., `KDIETZ_PROD.SF_FEATURE_STORE`). Then set the `DEPLOY_MODE`:

- `"incremental"` — auto-detects changes vs. `origin/main` using git diff and deploys only affected views
- `"full_refresh"` — deploys all feature views from scratch
- `"manual"` — deploys only the views listed in `MANUAL_FEATURE_VIEWS`

Run all cells. The notebook will:

1. Resolve which feature views to deploy based on your deploy mode
2. Validate UDF return types (and optionally auto-fix mismatches)
3. Register entities, deploy UDFs, and create feature views
4. Test feature serving with a sample spine query
5. Run comprehensive validation (entity counts, feature view counts, config checks)

Iterate on your UDF SQL and re-run until everything validates successfully.

#### Step 2: Staging Validation

Once your changes are working locally, push your branch and open a merge request. The MR pipeline provides two manual staging jobs:

- **`staging-feature-store-changes-incremental`** — detects which feature views changed in your MR (comparing against the target branch) and deploys only those to the staging schema. This is the typical way to test.
- **`staging-feature-store-changes-full-refresh`** — deploys all feature views to staging from scratch. Use this if you need to validate the entire feature store state, not just your changes.

Both jobs run against a shared staging schema (configured via `SNOWFLAKE_FEATURE_STORE_STAGING_SCHEMA`) and are triggered manually from the MR pipeline. Review the job logs to confirm your UDFs deployed without errors and validation passed.

#### Step 3: Production Deployment

When your MR is merged to `main`, the production pipeline runs automatically:

- **`deploy-feature_store-incremental`** — runs automatically on every merge. It compares the merge commit against the previous commit, detects affected and deleted feature views, and deploys only the changes to `FEATURE_STORE.SF_FEATURE_STORE`.
- **`deploy-feature-store-full-refresh`** — available as a manual job if a full redeployment is needed.

Deleted feature views are automatically cleaned up — the pipeline removes the dynamic view, the UDF, and the feature store registration. Production deletions are logged with warnings for visibility.

### Serving Features

To retrieve features for ML model training or inference, use `notebooks/serving_features.ipynb`. The workflow has four steps:

#### 1. Define Feature Views

Specify which feature views and versions you need. Feature views must share the same entity to be joined together:

```python
feature_views_dict = {
    "namespace_product_stage": "1.0",
    "namespace_information": "1.0"
}
```

#### 2. Define a Spine Query

The spine query defines your modeling population — the set of entity IDs and timestamps you want features for:

```python
spine_query = """
SELECT CAST(dim_namespace_id AS VARCHAR) AS dim_namespace_id,
       '2025-05-27'::TIMESTAMP AS snapshot_date
FROM PROD.common_prep.prep_namespace_order_trial
WHERE order_start_date BETWEEN '2024-03-17' AND '2025-05-27'
  AND trial_type IN (1, 4, 5, 7)
"""
```

#### 3. Configure Lookback Windows

Lookback windows control how far back each UDF looks when computing features. Three configuration options are available:

**Global (same for all feature views):**

```python
lookback_window_value = 6
lookback_window_unit = "month"
```

**Per-feature-view:**

```python
lookback_window_value = {
    "namespace_product_stage": 2,
    "namespace_information": 6
}
lookback_window_unit = {
    "namespace_product_stage": "week",
    "namespace_information": "month"
}
```

**Mixed (per-feature-view overrides with a global default):**

```python
lookback_window_value = {"namespace_product_stage": 2}
lookback_window_unit = "month"
```

#### 4. Call `serve_features`

```python
from gitlabds import serve_features

combined_features = serve_features(
    session=session,
    feature_store=fs,
    feature_views_dict=feature_views_dict,
    spine_df=spine_query,
    feature_date=snapshot_date,
    lookback_window_value=lookback_window_value,
    lookback_window_unit=lookback_window_unit,
    spine_timestamp_col="snapshot_date",
    include_feature_view_timestamp_col=False
)
```

This returns a pandas DataFrame with all requested features joined to your spine population.

### CI/CD Pipeline

The `.gitlab-ci.yml` defines a four-stage pipeline: `build` → `staging` → `deploy` → `security`. See the [Development Workflow](#development-workflow) section above for how staging and production jobs fit into the development process.

#### Change Detection

The CI pipeline uses `src/detect_changes.py` to compare git SHAs and determine exactly which feature views changed. Only affected views are deployed, and deleted views are automatically cleaned up (dynamic views, UDFs, and feature store registrations are all removed).

Changes are detected at the granular level: modifying a single entry in `feature_views.yaml` only triggers deployment of that specific view, not all views in the file. File renames and moves are handled correctly — moved views are deployed, not deleted.

#### Docker Image Management

The pipeline avoids unnecessary Docker rebuilds. On MRs, a `clone-image` job reuses the latest image unless `Dockerfile` or `pyproject.toml` changed, in which case `build-image` builds a fresh one. On `main`, `deploy-build-image` only runs when dependencies change.

### Troubleshooting

#### UDF Type Mismatches

If a UDF's declared return types don't match the actual output types, the deployment will catch this during validation. The `udf_type_validator.py` utility can auto-fix mismatches by comparing declared vs. actual types and updating the SQL file.

#### Permissions

The feature store uses the `FEATURE_STORE_PRODUCER` role for production deployments. If you encounter permission errors, verify that:

- `USAGE` grants exist on your UDFs for the consumer role
- `FUTURE GRANTS` are configured for new objects (note: future grants are not retroactive and only apply to objects created after the grant)

#### Common Issues

- **Entity ID type errors**: Always cast entity columns to `VARCHAR` in your UDF — Snowflake Feature Store requires consistent types across feature views sharing the same entity.
- **Missing parameters**: All three UDF parameters (`FEATURE_DATE`, `LOOKBACK_WINDOW_VALUE`, `LOOKBACK_WINDOW_UNIT`) must be present in every UDF signature, even if not all are used.
- **Cross-entity joins**: Feature views can only be joined during serving if they share the same entity. You cannot combine `dim_namespace_id` and `dim_crm_account_id` features in a single `serve_features` call.
