---
title: "Data Team CI Jobs"
description: "GitLab Data Team CI Jobs"
---

---

This page documents the CI jobs used by the data team in Merge Requests in both the [Data Tests](https://gitlab.com/gitlab-data/data-tests) and [Analytics](https://gitlab.com/gitlab-data/analytics) projects. For a quickstart guide on how to get started doing Merge Requests and using CI jobs, see [this practical guide](/handbook/enterprise-data/how-we-work/practical-guide/) in How We Work.

## What to do if a pipeline fails

- If a weekend has passed re-run any CLONE steps which were performed prior, every Sunday (5:00AMUTC) all old pipeline databases are [dropped](https://gitlab.com/gitlab-data/analytics/-/blob/master/orchestration/drop_snowflake_objects.py) from SnowFlake older than 14 days.
![ci-db-deletion-schema.png](/images/enterprise-data/platform/ci-jobs/ci-db-deletion-schema.png)
- Merge master branch. Due to how dbt handles packages pipelines can fail due to package failures which should always be handled in the latest branch.
- Confirm [model selection syntax](https://docs.getdbt.com/reference/node-selection/syntax). In general, it is easiest to simply use the file names of the models you are changing.
- If still uncertain or facing any issues, request assistance in the #data Slack channel

### Variable Name not found in the CI Pipeline job

This kind of error pops up in the pipeline like KeyError: 'GITLAB_COM_CI_DB_USER'. It means the variable is not defined in the variable section of CI/CD Settings. To resolve this, add the variable name to [CI/CD setting](https://gitlab.com/gitlab-data/analytics/-/settings/ci_cd) i.e. settings --> ci_cd --> variable, also provide the variable value.
**Notes:-** Turn off the Flags, so the variable is accessible from the CI pipeline.
The same applies to the variable value; if it is incorrect in the job, we can update it in the above link.

## Analytics pipelines

## Stages

CI jobs are grouped by stages.

### ❄️ Snowflake

These jobs are defined in [`.gitlab-ci.yml`](https://gitlab.com/gitlab-data/analytics/-/blob/master/.gitlab-ci.yml). All Snowflake objects created by a CI clone job will exist until dropped, either manually or by the [weekly clean up of Snowflake objects](/handbook/enterprise-data/platform/ci-jobs/#what-to-do-if-a-pipeline-fails).

#### `clone_prep_specific_schema`

Run this if you need a clone of any schema available in the prep database. Specify which schema to clone with the `SCHEMA_NAME` variable. If the clone already exists, this will do nothing.

#### `clone_prod_specific_schema`

Run this if you need a clone of any schema available in the prod database. Specify which schema to clone with the `SCHEMA_NAME` variable. If the clone already exists, this will do nothing.

#### `clone_prod`

Runs automatically when the MR opens to be able to run any dbt jobs. Subsequent runs of this job will be fast as it only verifies if the clone exists. This is an empty clone of the `prod` and `prep` databases.

#### `clone_prod_real`

Run this if you need to do a real clone of the `prod` and `prep` databases. This is a full clone both databases.

#### `clone_raw_full`

Run this if you need to run extract or freshness jobs. Subsequent runs of this job will be fast as it only verifies if the clone exists.

#### `clone_raw_postgres_pipeline`

Run this if you only need a clone of the raw `tap_postgres` schema in order to test changes to postgres pipeline or a manifest file.  If the raw clone already exists, this will do nothing.

#### `clone_raw_sheetload`

Run this if you only need a clone of the raw `sheetload` schema in order to test changes or additions to sheetload.  If the raw clone already exists, this will do nothing.

#### `clone_raw_specific_schema`

Run this if you need a clone of any other raw schema in order to test changes or additions. Specify which raw schema to clone with the `SCHEMA_NAME` variable. If the raw clone already exists, this will do nothing.

#### `clone_raw_by_schema`

Clones the entire RAW DB, created due to timeout issues when trying to clone the DB using SF commands.

**NB Due to the size of the DB created by running, only run this when you absolutely have to run through complete platform tests. Likely only applicable for infrastructure upgrades.**

#### `force_clone_both`

Run this if you want to force refresh raw, prod, and prep. This does a full clone of raw, but a shallow clone of `prep` and `prod`.

### 🚂 Extract

These jobs are defined in [`extract-ci.yml`](https://gitlab.com/gitlab-data/analytics/-/blob/master/extract/extract-ci.yml)

#### `boneyard_sheetload`

Run this if you want to test a new boneyard sheetload load. This requires the real `prod` and `prep` clones to be available.

#### `sheetload`

Run this if you want to test a new sheetload load. This jobs runs against the clone of `RAW`. Requires the `clone_raw_specific_schema` (parameter `SCHEMA_NAME=SHEETLOAD`) job to have been run.

#### `🛢 gitlab_saas_pgp_test`

Run this pipeline when making changes to any manifest file under `extract/gitlab_saas_postgres_pipeline/manifests`.

**Step 1:** Run `clone_raw_postgres_pipeline` CI job (part of `❄️ Snowflake` stage) to clone the `TAP_POSTGRES` schema.

**Step 2:** Run `gitlab_saas_pgp_test` CI job with the following `job_inputs`:

- `MANIFEST_NAME` (mandatory): Full manifest filename without extension, e.g. `el_gitlab_dotcom_db_manifest_main`
- `TASK_INSTANCE` (optional): Only required for **SCD** manifests with `advanced_metadata: true`. Use any unique value, e.g. `my_task_instance_123`

<details>
<summary>List of Manifest Files</summary>

| Manifest File | Type |
|---|---|
| `el_gitlab_dotcom_db_manifest_ci.yaml` | GitLab DB |
| `el_gitlab_dotcom_db_manifest_ci_scd.yaml` | GitLab DB (SCD) |
| `el_gitlab_dotcom_db_manifest_main.yaml` | GitLab DB |
| `el_gitlab_dotcom_db_manifest_main_scd.yaml` | GitLab DB (SCD) |
| `el_gitlab_dotcom_db_manifest_secure.yaml` | GitLab DB |
| `el_gitlab_dotcom_db_manifest_secure_scd.yaml` | GitLab DB (SCD) |
| `el_saas_customers_scd_db_manifest.yaml` | Customers DB (SCD) |

</details>

### ⚙️ dbt Run

These jobs are defined in [`snowflake-dbt-ci.yml`](https://gitlab.com/gitlab-data/analytics/-/blob/master/transform/snowflake-dbt/snowflake-dbt-ci.yml)

> As part of a dbt model change MR, you need to trigger a pipeline job to test that your changes won't break anything in production. We recommend using `build_changes` in the `dbt_run` stage.

These jobs are scoped to the `ci` target, which selects a subset of data for the snowplow and version datasets. Job artifacts, including compiled code and run results, are available for all dbt run jobs.

Most dbt run jobs can be parameterized with variables specifying the dbt model that requires testing along with other inputs.

**Note:** `build_changes` and `custom_invocation` parameters are defined using GitLab CI/CD [job inputs](https://docs.gitlab.com/ee/ci/inputs/). When triggering these jobs manually via **Run pipeline**, you'll see a typed input form instead of free-text variable key/value pairs.

#### DBT CI Job Warehouse size

If you want to run a dbt job via the `🏗️🏭build_changes` or `🎛️custom_invocation`, you have the possibility to choose the size of the Snowflake warehouse you want to use in the CI job. Available warehouse sizes are XS, M, L, and XL. This can be done by setting the `WAREHOUSE` variable when starting the CI job:

- Setting `WAREHOUSE` to `DEV_XS` is will use an `XS` warehouse.
- Setting `WAREHOUSE` to `DEV_M` will use an `M` warehouse.
- Setting `WAREHOUSE` to `DEV_L` is will use a `L` warehouse.
- Setting `WAREHOUSE` to `DEV_XL` is will use an `XL` warehouse.

Using a bigger warehouse will result in shorter run time (and prevents timing out of large models),
but also results in bigger costs for GitLab if the warehouse is running for less than a minute.
Reference your local development run times and model selection to aid in identifying what warehouse should be used.
If you are unsure or are unable to have a reasonable estimation of the run time start with a `L` warehouse.
Also its important to find parity between testing a model and how the model is executed in Production.
Of course there can be a good reason to use a bigger warehouse,
if there are complex transformations or lots of data to be processed more power is required.
But always also please check your model. Maybe the model can be adjusted to run more efficiently.
Running your test on a bigger warehouse will not only trigger increased costs for **this** CI Job,
but it also could run inefficiently in production and could have a much bigger impact for the long run.

#### `🏗️🏭build_changes`

This job is designed to work with most dbt changes without user configuration. It clones, runs, and tests all new and changed models, as well as any models between the changed models in the lineage. It also identifies models that depend on changed macros and includes them in the build process, ensuring comprehensive testing of all affected components.

It references the live databases (`PROD`, `PREP`, and `RAW`) for any tables not included in the selection, in accordance with the most recent version of the [dbt documentation](https://dbt.gitlabdata.com/). If the job fails, it should represent an issue within the code itself and should be addressed by the developer making the changes.

The job runs with default settings out of the box. To trigger it, simply press ▶️ next to the `build_changes` job.

![build-changes-screenshot](/images/enterprise-data/platform/ci-jobs/build-changes-screenshot.png)

Should you require a different configuration, it can be updated as follows:

- `WAREHOUSE`: Defaults to `DEV_M` and also accepts `DEV_XS`, `DEV_L`, and `DEV_XL`.
- `CONTIGUOUS`: Defaults to `true`. When true (default), runs all models in the contiguous subgraph between changed models using the `contiguous_list` selector. Set to `false` to run only the directly changed models. `DOWNSTREAM` and `EXCLUDE` only take effect when `CONTIGUOUS` is `false`; they're ignored when `CONTIGUOUS` is `true`.
- `SELECTION`: Defaults to a list of any changed SQL or CSV files but accepts any valid dbt selection statement. It overrides any other model selection. Available selectors can be found in the [selector.yml](https://gitlab.com/gitlab-data/analytics/-/blob/master/transform/snowflake-dbt/selectors.yml) file.
- `DOWNSTREAM`: Defaults to `None` but accepts the `plus` and `n-plus` operators. It's bypassed when `CONTIGUOUS` is `true` (the default), so you must set `CONTIGUOUS` to `false` to use it. `DOWNSTREAM` has no impact when overriding `SELECTION`. See the [documentation](https://docs.getdbt.com/reference/node-selection/graph-operators) on graph operators for details on what each does.
- `FAIL_FAST`: Defaults to `true` in the CI but accepts `false` to continue running even if a test fails or a model can't build. See the [documentation](https://docs.getdbt.com/reference/global-configs/failing-fast) for details. Locally, the default is `false`.
- `EXCLUDE`: Defaults to `None` but accepts any dbt node selection. It's bypassed when `CONTIGUOUS` is `true`. See the [documentation](https://docs.getdbt.com/reference/node-selection/exclude) for details.
- `FULL_REFRESH`: Defaults to `false` but accepts `true` to re-clone and rebuild any tables that would otherwise run incrementally. See the [documentation](https://docs.getdbt.com/reference/commands/run#refresh-incremental-models) for details.
- `VARS`: Defaults to `None` but accepts a comma-separated list of `key:value` pairs, e.g. `key1:value1, key2:value2`. For models using `only_force_full_refresh()`, set `VARS=full_refresh_force:true` along with `FULL_REFRESH=true`.
- `RAW_DB`: Defaults to `Live` but accepts `Dev`. Selecting `Dev` has the job use the branch-specific version of the live `RAW` database, so only explicitly loaded data will be present. This is needed when testing models built on extracts that are new in the same branch.

![build-changes-screenshot](/images/enterprise-data/platform/ci-jobs/build-changes-inputs.png)

Running this CI job in a merge request pipeline will produce an output report that is added directly to a merge request as a comment from a project bot. This report will summarize the results of the job showing total run time, model counts, what models were executed, and any models that run for more than one hour.  This report can be suppressed by adding the {{< label name="Supress Results Report" >}} label to the merge request.

<details markdown="1">
<summary>CI Job Reference</summary>

| Change Example | Recommended CI Job & Inputs |
| --- | --- |
| Add column to small table or view | <ol><li>🏗️🏭build_changes</li><ul><li>WAREHOUSE : DEV_XS</li></ul></ol> |
| Update column description | <ol><li>📚✏️generate_dbt_docs</li></ol> |
| Update or create a small dbt snapshot | <ol><li>🏗️🏭build_changes</li><ul><li>WAREHOUSE : DEV_XS</li></ul></ol> |
| Add or update a seed | <ol><li>🏗️🏭build_changes</li><ul><li>WAREHOUSE : DEV_XS</li><li>FULL_REFRESH : true</li></ul></ol> |
| Update a model and test downstream impact | <ol><li>🏗️🏭build_changes</li><ul><li>WAREHOUSE : DEV_XS</li><li>CONTIGUOUS : false</li><li>DOWNSTREAM : +</li></ul></ol> |
| Update a model and test specific models | <ol><li>🏗️🏭build_changes</li><ul><li>WAREHOUSE : DEV_XS</li><li>SELECTION : specific_models+1</li></ul></ol> |
| Make a change to an incremental model without full refresh | <ol><li>🏗️🏭build_changes</li></ol> |
| Make a change to an incremental model with full refresh | <ol><li>🏗️🏭build_changes</li><ul><li>FULL_REFRESH : true</li></ul></ol> |
| Update a model and test downstream impact, skipping specific model | <ol><li>🏗️🏭build_changes</li><ul><li>CONTIGUOUS : false</li><li>EXCLUDE : other_model</li><li>DOWNSTREAM : +</li></ul></ol> |
| Change a model that needs vars | <ol><li>🏗️🏭build_changes</li><ul><li>VARS : key1:value1,key2:value2</li></ul></ol> |
| Make a change and see all errors | <ol><li>🏗️🏭build_changes</li><ul><li>WAREHOUSE : DEV_XS</li><li>FAIL_FAST : false</li></ul></ol> |
| Make a change to or use a Selector | <ol><li>🎛️custom_invocation</li><ul><li>STATEMENT : build --selector customers_source_models</li></ul></ol> |
| Add a model built on a new Sheetload in the same MR | <ol><li>❄️ Snowflake: clone_raw_sheetload</li><li>Extract: sheetload</li><li>🏗️🏭build_changes</li><ul><li>RAW_DB : Dev</li></ul></ol> |

</details>

#### `🎛️custom_invocation`

This job is designed to be a way to resolve edge cases not fulfilled by other pre-configured jobs. The job will process the provided dbt command using the selected warehouse.

This job can be configured in the following ways:

- `WAREHOUSE`: Defaults to `DEV_M`, but can be updated to `DEV_XL`, `DEV_L`, or `DEV_XS`.
- `STATEMENT`: No default, any valid dbt command, excluding the 'dbt' prefix. For `run/build/test` commands, **recommended**: append `'--defer --state reference_state'` to resolve upstream refs from production rather than rebuilding them in your branch (i.e., `'run --select dim_date --defer --state reference_state'`). Available selectors can be found in the [selector.yml](https://gitlab.com/gitlab-data/analytics/-/blob/master/transform/snowflake-dbt/selectors.yml) file.
- `RAW_DB`: Defaults to `Live` but will accept `Dev`.  Selecting `Dev` will have the job use the branch specific version of the live `RAW` database, only the data that is explicitly loaded will be present.  This is needed when testing models build on extracts that are new in the same branch.

#### `📚📝generate_dbt_docs`

You should run this pipeline manually when either `*.md` or `.yml` files are changed under `transform/snowflake-dbt/` folder. The motivation for this pipeline is to check and validate changes in the `dbt` documentation as there is no check on how the documentation was created - errors are allowed and not validated, by default. There are no parameters for this pipeline.

### 🛠 dbt Misc

These jobs are defined in [`snowflake-dbt-ci.yml`](https://gitlab.com/gitlab-data/analytics/-/blob/master/transform/snowflake-dbt/snowflake-dbt-ci.yml)

#### `🔍ds_exposure_dependencies_query`

This CI job runs automatically whenever SQL files in the dbt project are updated. It checks if any modified models are tied to Data Science exposures and, if so, fails the job while notifying the user. It is then the MR creator’s responsibility to inform the Data Science team, ensuring they have the opportunity to review any potential impact.

By catching these updates early, the job helps maintain smooth Data Science workflows and prevents unintended disruptions from dbt model changes.

#### `🔍tableau_direct_dependencies_query`

This job runs automatically and only appears when `.sql` files are changed. In its simplest form, the job will check to see if any of the currently changed models are **directly** connected to tableau views, tableau data-extracts and/or tableau flows. If they are, the job will fail with a notification to check the relevant dependency. If it is not queried, the job will succeed.

Current caveats with the job are:

- It will not tell you which tableau workbook to check
- It will not tell indirectly connected downstream dependencies. This feature will be a part of upcoming iteration to this job.
- It does not find dependencies for tables that use a dbt alias. [We discourage the use of aliases](/handbook/enterprise-data/platform/dbt-guide/#general) in models, but there are legacy tables that use aliases, so caution should be exercised when working with aliased tables. Downstream dependencies can be checked manually in MonteCarlo using the alias.
- If there are any changes in Tableau, like adding or removing dependencies to a dashboard, it can take up to 8 days for Monte Carlo to reflect that change in lineage

##### Explanation

This section explains how the `tableau_direct_dependencies_query` works.

`git diff origin/$CI_MERGE_REQUEST_TARGET_BRANCH_NAME...HEAD --name-only | grep -iEo "(.*)\.sql" | sed -E 's/\.sql//' | awk -F '/' '{print tolower($NF)}' | sort | uniq`

This gets the list of files that have changed from the master branch (i.e. target branch) to the current commit (HEAD). It then finds (grep) only the sql files and substitutes (sed) the `.sql` with an empty string. Using `awk`, it then prints the lower-case of the last column of each line in a file (represented by $NF - which is the number of fields), using a slash (/) as a field separator. Since the output is directory/directory/filename and we make the assumption that most dbt models will write to a table named after its file name, this works as expected. It then sorts the results, gets the unique set and is then used by our script to check the downstream dependencies.

`orchestration/tableau_dependency_query/src/tableau_query.py`

We leverage [Monte Carlo](/handbook/enterprise-data/platform/monte-carlo/) to detect downstream dependencies which is also our data obeservability tool. Using [Monte carlo API](https://apidocs.getmontecarlo.com/) we detect directly connected downstream nodes of type `tableau-view`, `tableau-published-datasource-live`, `tableau-published-datasource-extract` using the [`GetTableLineage` GraphQL endpoint](https://apidocs.getmontecarlo.com/#query-getTableLineage).

If no dependencies are found for the model, then you would get an output in the CI jobs logs - `INFO:root:No dependencies returned for model <model_name>` and the job will be marked as successful.

And if dependencies were found for the model, then the job would fail with the value error `ValueError: Check these models before proceeding!`. The job logs will contain number of direct dependencies found for a given model, type of tableau object, tableau resource name and monte carlo asset link, in the below format:

```bash
Found <number of tableau dependencies> downstream dependencies in Tableau for the model <model name>
INFO:root: <tableau resource type> : <name of tableau resource> - : <monte_carlo_connection_asset_url>
ValueError: Check these models before proceeding!
ERROR: Job failed: command terminated with exit code 1
```

More implementation details can be found in the issue [here](https://gitlab.com/gitlab-data/analytics/-/issues/19885).

#### `🛃dbt_sqlfluff`

Runs the SQLFluff linter on all changed `sql` files within the `transform/snowflake-dbt/models` directory.  This is currently executed manually and is allowed to fail, but we encourage anyone developing dbt models to view the output and format according to the linters specifications as this format will become the standard.

#### `🚫safe_model_script`

In order to ensure that all [SAFE](/handbook/legal/safe-framework/) data is being stored in appropriate schemas all models that are downstream of [source models with MNPI data](/handbook/enterprise-data/how-we-work/new-data-source/#mnpi-data) must either have an exception tag or be in a restricted schema in `PROD`. This CI Job checks for compliance with this state.

This [video](https://www.youtube.com/watch?v=ICOuerPeAUU) provides an overview of the SAFE Data Program implementation on Snowflake.

<details><summary>how `safe_model_script` works - under the hood</summary>

The CI job is set-up in `snowflake-dbt-ci.yml` and these are the pertinent lines:

```sh
- dbt --quiet ls $CI_PROFILE_TARGET --models tag:mnpi+
  --exclude
    tag:mnpi_exception
    config.schema:restricted_safe_common_mapping
    config.schema:some_other_restricted_schema_etc
    ...
  --output json > safe_models.json
- python3 safe_model_check.py
```

The above has two parts, the `dbt ls` command (the main part), and the python script.

The`dbt ls` does the following:

- It first returns all models tagged with mnpi and all **downstream** models.
- Then, in the `--exclude` argument, we exclude any *valid* models. Models from the above step are excluded if they meet one of these conditions:
  - tagged with `mnpi_exception`
  - within a `restricted` schema
- Any models that are left need to be fixed by either being placed in a restricted schema, or tagged with 'mnpi_exception'

In the 2nd part, the python script reads in the output from the above 'dbt ls' command. If the output is NOT empty, an exception is raised with a list of failing models.

</details>

##### How to handle script failure

A failure indicates one of two things:

- your model has MNPI data (either directly or as a downstream model)
  - Fix: move your model to a restricted schema
- your model does NOT have MNPI data, but is downstream of a model that does have MNPI data
  - Fix: add `mnpi_exception` tag to the model

##### How to decide when to use the mnpi_exception tag

The MNPI exception tag `mnpi_exception` can be added to the model if it does not contain MNPI data. MNPI data would be columns containing information like Paid Licensed Users, ARR, Net_ARR, Revenue, Net Retention, Expenses etc. Essentially Financial Data that would allow a person to understand GitLab's publicly disclosed financial metrics on a trending basis and result in providing information that would be material to investment decisions. Once we financial data is surfaced in a data model, we take a conservative approach and put the model into the restricted schema and no tag is required in that case since it is in the restricted schema.

#### `🔍macro_name_check`

Automatically runs when making changes in the snowflake-dbt/macros folder and checks if the newly created macros match the correct name format.

#### `run_grants`

**Note:** `run_grants` parameters are defined using GitLab CI/CD [job inputs](https://docs.gitlab.com/ee/ci/inputs/). When triggering this job manually via **Run pipeline**, you'll see a typed input form instead of free-text variable key/value pairs.

Run this if you'd like to grant access to the copies or clones of `prep` and `prod` for your branch to your role or a role of a business partner. Specify the snowflake roles (see [roles.yml](https://gitlab.com/gitlab-data/analytics/-/blob/master/permissions/snowflake/roles.yml)) you'd like to grant access to using the `GRANT_TO_ROLES` CI variable. You can pass in a single role, or multiple separated by a space as in `role1 role2`. This job checks the git commit for the changed models and verifies that the submitted roles have adequate access in `PREP` and `PROD` to grant access in the clone. It does not create any future grants and so **all relevant objects must be built in the clone before you run this job if you want to ensure adequate object grants.**

If the submitted role does not have adequate access in `PREP` and `PROD` then in the job logs you will see the following entry:

`INFO:root::rotating_light: upstream objects in OBJECT_NAME did not match upstream grants for ROLE :rotating_light:`

There's a intermittent problem where the run grants job will be unable to compare existing grants in `PREP` and `PROD` because the source for querying existing grants in Snowflake is a table that has a derived state and intermittently can be missing grants.

In this case, verify that the submitted role has adequate access in `PREP` and `PROD`. If it does and this problem persists then re-running (sometimes this takes an hour or so) should fix the problem. ```

**Note:** The `run_grants` job can be run multiple times during the development process. If new models are created after the initial run, you can re-run the job to ensure that grants are applied to these new objects as well.

#### `run_grants_eval_harness`

**What it does:** Grants the `SQG_EVAL_CI` role `USAGE` + `SELECT` access on the
per-MR Snowflake zero-copy clone databases (`<BRANCH>_PROD` / `<BRANCH>_PREP`).
Clone databases do not inherit grants from their source, so the SQG evaluation
harness cannot read MR clone data without this step.

**When to run it:** Needed if you want to run the eval harness for conversational
analytics. Trigger manually after your MR clones have been built and before
running the SQG eval harness. Recommended sequence:

1. `clone_prod_real`
2. `🏗️🏭build_changes` (optional)
3. **`run_grants_eval_harness`** ← trigger manually here
4. Run the `sql-eval` job to test the harness

**How to trigger it:** Run without arguments — it always only grants
`SQG_EVAL_CI` role access.

### 🐍 Python

These jobs are defined in [`.gitlab-ci.yml`](https://gitlab.com/gitlab-data/analytics/-/blob/master/.gitlab-ci.yml).

There are several jobs that only appear when `.py` files have changed. All of them will run automatically on each new commit where `.py` files are present.

Pipelines running automatically are:

#### `⚫python_black`

We handle python code formatting using the [`black`](https://github.com/psf/black) library. The pipeline checks the entire `/analytics` repo (all `*.py` files).

#### `✏️python_mypy`

We use the [`mypy`](https://mypy.readthedocs.io/en/stable/) library to check code correctness. The pipeline checks the entire `/analytics` repo (all `*.py` files).

#### `🗒️python_pylint`

We use the [`pylint`](https://pylint.pycqa.org/en/latest/) library and check code linting for Python files. The pipeline checks only **changed** Python files (`*.py`) in `/analytics` repo.

#### `🌽python_flake8`

We use the [`flake8`](https://flake8.pycqa.org/en/latest/) library and check code linting for Python files. The pipeline checks only **changed** Python files (`*.py`) in `/analytics` repo.

#### `🦅python_vulture`

We use the [`vulture`](https://pypi.org/project/vulture/0.5/) library and check unused for Python files. `Vulture` finds unused classes, functions and variables in your code. This helps you cleanup and find errors in your programs.
The pipeline checks only **changed** Python files (`*.py`) in `/analytics` repo.

#### `🤔python_complexity`

We use the [`xenon`](https://pypi.org/project/xenon/) library and check code complexity for Python files. The pipeline checks the entire `/analytics` repo (all `*.py` files).

#### `✅python_pytest`

We ensure code quality by running the [`pytest`](https://docs.pytest.org/en/7.1.x/contents.html) library and test cases in `/analytics` repo. The pipeline all test files in the entire `/analytics` repo (all `*.py` files contains `pytest` library).

Manually running pipelines are:

#### 📈namespace_metrics_check

The pipeline runs only when the file [usage_ping_namespace_queries.json](https://gitlab.com/gitlab-data/analytics/-/blob/master/extract/saas_usage_ping/usage_ping_namespace_queries.json) is changed to ensure all rules are satisfied. The pipeline runs automatically.

### Permifrost

These are CI jobs to run Permifrost in [snowflake-permissions](https://gitlab.com/gitlab-data/snowflake-permissions) project.

#### `🧊⚙permifrost_run`

Manual job to do a dry run of [Permifrost](https://gitlab.com/gitlab-data/permifrost/).

#### `🧊 permifrost_spec_test`

Must be run at least once before any changes to `permissions/snowflake/roles.yml` are merged. Takes around 5 minutes to complete.

Runs the `spec-test` cli of [Permifrost](https://gitlab.com/gitlab-data/permifrost/) to verify changes have been correctly configured in the database.

#### `📁 yaml_validation`

Triggered when there is a change to `permissions/snowflake/roles.yml`. Validates that the YAML is correctly formatted.

#### `📚 roles_yaml_snowflake_provisioning`

Updates `roles.yml` automatically based on changes to `snowflake_users.yml`, then commits changes back to the repository.

CI arguments and their default values are all clearly visible as CI job inputs.

#### `👥 users_snowflake_provisioning_snowflake`

Adds/removes users and roles directly in Snowflake based on changes to `snowflake_users.yml`. For security, requires codeowner MR approval to run.

CI arguments and their default values are all clearly visible as CI job inputs.

### 🛑 Snowflake Stop

These jobs are defined in [`.gitlab-ci.yml`](https://gitlab.com/gitlab-data/analytics/-/blob/master/.gitlab-ci.yml).

#### `clone_stop`

Runs automatically when MR is merged or closed. In general, this should not be run manually but it can also be used to remove the MR development database. Once completed, starting a new pipeline or re-running the `clone_prod` job will then re-clone the empty database and you can start again

## Data Test Pipelines

All the below run against the Prod DB using the changes provided in the repo. No cloning is needed to run the below.

### `🧠 all_tests_prod`

Runs through all tests in the analytics & data tests repo.

### `💾 data_tests_prod`

Runs through all the data tests in the analytics & data tests repo's.

### `schema_tests_prod`

Runs through all the schema tests in the analytics & data tests repo's.

### `specify_tests_prod`

Runs specified model tests with the variable `DBT_MODELS`
