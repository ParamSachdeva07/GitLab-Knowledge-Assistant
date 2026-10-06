---
title: "Data Platform Triage Guide"
---

## Overview

The Data Platform team rotate weekly through triage duties. While the rotation is assigned by week, the triager is responsible for **daily monitoring**, **issue processing**, and **communication** throughout their shift. This guide outlines what needs to happen each day, how to handle issues, and what to complete at the end of the rotation

## Responsibilities

The Data Platform triager is responsible for resolving problems with our data platform, which will either be in the **#data-pipelines** and **#data-prom-alerts** slack channels, on the [DE - Triage Errors board](https://gitlab.com/groups/gitlab-data/-/boards/1917859) and on the [MonteCarlo Incident page](https://getmontecarlo.com/incidents?include-normalized=false&types=freshness_anomaly%2Cvolume_anomaly%2Cdimension_anomaly%2Cfield_metrics_anomaly%2CDBT_ERRORS%2Cfreshness_sli_rule_breach%2Cvolume_sli_rule_breach%2Csql_rule_breach) (make sure to filter on the `Data Platform` domain in MonteCarlo). Issues created from these errors should use the [DE Triage Errors issue template](https://gitlab.com/gitlab-data/analytics/issues/new?issuable_template=Triage%20Errors%20DE).

- During the assigned triage week the Data Platform Team member will focused on (in priority order):
  - Incoming incidents
  - [Open incidents](https://gitlab.com/gitlab-data/analytics/-/incidents)
  - New issues: Every issue that comes in during a team member's triage week must be [resolved](/handbook/enterprise-data/how-we-work/triage/data-platform-triage/#issue-assignment-and-processing).
    - A new issue is defined as an issue with no assignee and the workflow label `triage & validation`. [This issue list](https://gitlab.com/groups/gitlab-data/-/issues/?sort=updated_desc&state=opened&assignee_id=None&label_name%5B%5D=Team%3A%3AData%20Platform&label_name%5B%5D=workflow%3A%3A1%20-%20triage%20%26%20validation&not%5Blabel_name%5D%5B%5D=Triage&first_page_size=100) tracks these items.
  - Open issues on the [Data Platform - Triage Errors board](https://gitlab.com/groups/gitlab-data/-/boards/1917859).
    - If an open incident or issue is already assigned it is still the triager responsibility to either take that issue or ensure progress is made.
    - If there is no work to be performed on incidents or issues on the [board](https://gitlab.com/groups/gitlab-data/-/boards/1917859) the triager will work on their regular work assignments.
- Involvement from Data Platform Team members who do **not** carry triage responsibilities that week is likely still needed in some cases like:
  - A standing issue or incident could not be solved by the triager and triager need help from other Data Platform Team members.
  - Monitoring #data-prom-alerts:
    - The #data-prom-alerts slack channel is used for the most urgent breaking events, which requires **immediate** action. It is the responsibility of all Data Platform Team members to ensure action is taken in time after office hours of the triager.
  - Assistance from the Data Platform Team is needed by other GitLab Team members and this is outside of the office hours of the triager.
- Monte Carlo incidents are posted in the `#data-pipelines` Slack channel (except schema changes). Because Monte Carlo only initially notifies an incident, checking the Monte Carlo Incident page is needed to avoid missing any incidents. **Schema changes** are filtered out using [this link](https://getmontecarlo.com/incidents?include-normalized=false&types=freshness_anomaly%2Cvolume_anomaly%2Cdimension_anomaly%2Cfield_metrics_anomaly%2CDBT_ERRORS%2Cfreshness_sli_rule_breach%2Cvolume_sli_rule_breach%2Csql_rule_breach), because these don't require action (and are also not reported in the Slack channel). **All Monte Carlo incidents need to be given an appropriate resolution status or linked to an assigned GitLab issue end of day.**
  - Note: Currently there is a large backlog of unclassified incidents in MonteCarlo. We currently focus only on the last 7 days.

## Issue Assignment and Processing

Every issue that comes in during a Data Platform Team member's triage week must be resolved as follows:

1. All issues are assigned to triager as starting point.
1. All issues are processed through the combined `triage & validation` stage, where the triager determines both the clarity of the problem statement and whether the work warrants development, then moved to `waiting for prioritization` - following the defined [workflow (criteria)](/handbook/enterprise-data/how-we-work/#workflow-summary). If the triager cannot prepare it adequately:
   - **If missing information**: Engage in iterative communication with the stakeholder to clarify requirements and gather needed details. Triaging is a collaborative process that often requires back-and-forth discussion. Label as `workflow::blocked` if the issue is truly blocked and triage cannot continue despite attempts to gather information. When blocked, comment with specific information needed and assign to both the issue reporter and keep the triager assigned to create shared accountability.
   - **If lacking domain expertise**: Assign to a team member with domain expertise, OR assign to Director Data Platform if appropriate expertise is unknown
1. If an issue is **1-2** [issue points](/handbook/enterprise-data/how-we-work/#issue-pointing) they will fully implement the solution. This means moving through all workflow stages up until `workflow::6 - review`.
1. If an issue is **3 or more** issue points, the issue will be labelled as `workflow::2 - waiting for prioritization`.
   - If an issue is not urgent. Triager unassigns themselves and issue has been placed in the backlog.
   - If an issue is urgent. Triager aligns with a team member on assignment or assigns to Director Data Platform.

**Ownership continuity**: Any `workflow::1 - triage & validation` issues open during your triage week **remain assigned to you until resolved**, even if your triage week ends before they're complete. This preserves context and avoids unnecessary handoffs.

- **Exceptions:** blocked issues, capacity constraints, domain expertise gaps requiring delegation, or issues opened after the triager's final business hours of their triage week (these fall to the incoming triager).

**Note on blocked issues**: Blocked issues are an exception to ownership continuity. If an issue has been blocked for more than **five business days** with insufficient information to proceed, unassign yourself and relabel it to `workflow::blocked` so it drops off the triage board. Notify the stakeholder that when they provide the needed information, they should relabel it as `workflow::1 - triage & validation` for the next triager to pick up. If there is no stakeholder activity for two weeks+, consider closing the issue.

```mermaid
flowchart TD
    N[New Issue]
    A[Assign to triager]
    T[workflow::1 - triage & validation]
    C{Can triager complete?}
    B[workflow::blocked - assign to reporter & keep triager assigned]
    R[Assign to expert/director]
    W[workflow::2 - waiting for prioritization]
    D[workflow::3 - refinement]
    V[workflow::6 - review]
    U[Unassign]
    UB{Issue unblocked?}
    Close[Close issue]

    N-->A
    A-->T
    T-->C
    C-->|Missing info|B
    B-->UB
    UB-->|Yes|T
    UB-->|No, extended period|Close
    C-->|Need expertise|R
    R-->U
    C-->|No, not urgent|W
    W-->U
    C-->|No, urgent|R
    C-->|Yes 1-2 pts|D
    D-->V
    V-->U
```

### Follow up

- Incidents are always given immediate attention.
- Every incident has a DRI assigned. This is not necessarily the triager/creator of the incident. Due to the nature of asynchronous working at GitLab, the triager/creator is the DRI until another GitLab Team Member is actively contacted/involved.
  - The [codeownerfile](https://gitlab.com/gitlab-data/analytics/-/blob/master/CODEOWNERS) is the right future*source to find the right DRI for assigning the incident.* Currently the code ownership is not well defined. As part of FY23-Q1 we are planning to have a more strict ownership.
- Every raised incident will be communicated in the `#data` Slack channel, followed by a short description, ETA and link to the incident. The right GitLab Team Members are tagged.
  - A regular (depending on the severity) update is posted in Slack. Sometimes there isn't a new status, don't hesitate to communicate this as well.
  - Timelines should be documented in the [timeline section](https://docs.gitlab.com/ee/operations/incident_management/incident_timeline_events.html) under the incident Subject/Header for use in retrospectives and other investigations.
  - When the incident is solved, an update is posted in Slack

### End of week wrap-up

The Data Platform Team follows a weekly rotation schedule which means that by the end of the triage week the triager will hand over the triage responsibilities.

- Even though we still use the [triage issue](https://gitlab.com/gitlab-data/analytics/-/blob/master/.gitlab/issue_templates/Triage%3A%20Data%20Triage.md) on a daily basis, the triager will only write up the week a-sync in the central data team triage issue on Friday end of day.
- The triager will report/verbalize in the Weekly Data Platform Team meeting any notable things happened on triage on Tuesday in the next week.

Although running a weekly rotation, we expect the triager to post an EOD announcement in the applicable Slack channels.

## Triage common issues

In this section we state down common issues and resolutions

### GitLab.com databases structure changes

GitLab.com databases do regularly change. In order not to break the daily operation, changes to the database needs to be tracked and checked. Any change to the GitLab.com database and CustomerDot database is tracked by the Danger Bot. The Data Team gets notified, by applying labels to the MR, if a change to the db/structure\.sql is made.

A label `Data Warehouse::Impact Check` is added by the Danger Bot as call to action for the data team.

- On triage, the Triager will [check](https://gitlab.com/groups/gitlab-org/-/merge_requests?scope=all&state=opened&label_name[]=Data%20Warehouse%3A%3AImpact%20Check&draft=no&approved_by_usernames[]=Any) for MRs with label `Data Warehouse::Impact Check`.

The following actions are performed by Data Team Triager:

- Every merge request (`MR`) will be judged
  - If `MR` contains the label `group::product intelligence` along with `Data Warehouse::Impact Check`, there are a couple of checks that need to do:
    - Because a new metric is added or the existing one is altered, the `Data team` should ensure the change will not break the `Service ping` extraction process
    - Check new metric `SQL` statement from the original `MR` *(a typical example is [gitlab-org/gitlab/merge_requests/75504](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/75504/diffs#78300240169ab9f44b4dc25f6b6dcb56b3b629c7))* and execute it on `Snowflake` - usually, it is just a `SELECT` `SQL` statement
  - If the changes to the `SQL` file are not causing a break in the operation, the label will be changed to `Data Warehouse::Not Impacted`.
  - If the changes to the `SQL` file causing a break in the operation:
    - The Label will be changed to `Data Warehouse::Impacted`
    - A new issue is opened in the `GitLab Data Team project`, assigned to the correct DRI and linked to the original MR.
    - Impact will be determined in the issue.
    - Any MRs will be created to overcome loading issues, downstream dbt processing and Tableau usage.
      - If impact is beyond data loading, this means the data is used downstream, an Analytics Engineer **must** be included to also determine the business impact of the upstream change.
    - According to the Merge of the GitLab.com MR, merge will be planned.
  - If the `MR` does not contains the label `group::product intelligence` and it concerns changes to `SQL` structure:
    - Check if it will break the operation / data pipeline, following the Determination matrix below.

  - If any `MR` will cause a break in the operation, the label will be changed to `Data Warehouse::Not Impacted`.
  - If any `MR` will cause a break in the operation:
    - The Label will be changed to `Data Warehouse::Impacted`
    - A new issue is opened in the `GitLab Data Team project`, assigned to the correct DRI and linked to the original MR.
    - Impact will be determined in the issue.
    - Any MRs will be created to overcome loading issues, downstream dbt processing and Tableau usage.
      - If impact is beyond data loading, this means the data is used downstream, an Analytics Engineer **must** be included to also determine the business impact of the upstream change.
    - According to the Merge of the GitLab.com MR, merge will be planned.
    - All stakeholders will be informed.

#### Graphical representation of the process

<details><summary>Click to expand graphical representation of the process</summary>

```mermaid
flowchart TD
    subgraph "Original MR"
       CHECK_BOARD
       ADDITIONAL_LABEL
       CLABEL
       CHANGE_LABEL_I
       CHECK_DDL
    end
    CHECK_BOARD(Check MRs on the board) --> ADDITIONAL_LABEL{Does MR has a label: `group::product intelligence`}
    ADDITIONAL_LABEL --Yes--> CHECK_ORIGINAL_ISSUE_PI{{Check code in the original MR}}
    ADDITIONAL_LABEL --No--> CHECK_DDL{Will DDL break in the operation}
    CHECK_DDL --Yes--> CHANGE_LABEL_I(Change label to `Data Warehouse::Impacted`)
    CHECK_DDL --No-->CLABEL(Changed label to `Data Warehouse::Not Impacted`)
    CHANGE_LABEL_I-->OI(Open an new issue is opened in the `GitLab Data Team project`)
    subgraph "Data team project"
       OI-->IM(Impact will be determined in the issue)
       IM-->CHECK(Check downstream dbt processing and Tableau usage)
       CHECK-->PL(Plan MR)
       PL-->INFORM(Inform stakeholders)
    end
    INFORM-->END((End))
    CLABEL-->END
    OK_SQL--Yes-->CLABEL
    OK_SQL--No-->CHANGE_LABEL_I
    subgraph "group::product intelligence"
        CHECK_ORIGINAL_ISSUE_PI -->SQL[(Find and execute SQL statement)]
        SQL--Execute-->OK_SQL{Is SQL executed properly}

    end
```

</details>

Determination matrix: **

| Change | Call to action needed* |
| ------ | ------ |
| New table created | :x: |
| Table deleted | :white_check_mark: |
| Table renamed | :white_check_mark: |
| Field added | :x: |
| Field removed | :white_check_mark: |
| Field name altered | :white_check_mark: |
| Field datatype altered | :question:|
| Constraints changed | :question: |

*We are not loading all the tables and columns by default. Thus if new tables or columns are added, we only will load these tables if there is a specific business request. Any change to the current structure that causes a potential break of operation needs to be determined.

** Determination matrix is not extensive. Every MR should be checked carefully.

### GitLab Postgres Database not accessible

In a situation when gitlab_dotcom postgres replica snapshot is not built correctly, the task `check_replica_snapshot` inside the extract DAG's fail for MAIN and/or CI db, which indicates either that the replica snapshot is not rebuilt/accessible or the `pg_last_xact_replay_timestamp` value was not present.The error message generated from task failure would indicate errors with the replica database connectivity or database system starting up and the error in the task would look something similar like this:

```console
[2023-07-15 13:04:48,022] INFO - b'psycopg2.OperationalError: could not connect to server: Connection refused\n'
[2023-07-15 13:04:48,022] INFO - b'\tIs the server running on host "{db_instance_ip}" and accepting\n'
[2023-07-15 13:04:48,022] INFO - b'\tTCP/IP connections on port {port}?
```

Follow the [runbook](https://gitlab.com/gitlab-data/runbooks/-/blob/main/Gitlab_dotcom/Gitlab_DB_recreation_failure.md) for the steps to perform, including communication.

### Automated service ping issue

In a situation when [Service ping](https://internal.gitlab.com/handbook/enterprise-data/data-governance/data-catalog/saas-service-ping-automation/#service-ping-overview) fail while it generates metrics, we should be informed either via `Trusted data dashboard` or `Airflow` log - generally, the error log is stored in `RAW.SAAS_USAGE_PING.INSTANCE_SQL_ERRORS` table. Follow the instructions from the link [error-handling-for-sql-based-service-ping](https://internal.gitlab.com/handbook/enterprise-data/data-governance/data-catalog/saas-service-ping-automation/#error-handling-for-sql-based-service-ping) in order to fix the issue.

### Zuora Stitch Integration single or set of table-level reset

It could happen, in any case, to [reset the table](https://www.stitchdata.com/docs/troubleshooting/destinations/destination-loading-error-reference#snowflake-error-reference) in Stitch for the Zuora data pipeline, in order to backfill a table completely (i.e. new columns added to in the source, technical error etc).
Currently, Zuora Stitch integration does not provide [table level reset](https://www.stitchdata.com/docs/integrations/saas/zuora#zuora-feature-snapshot), and thus we have to perform a reset of all the tables in the integration. This will result in extra costs and risks.

To this below steps can be followed using which we have successfully done the table level reset.
In this example, we have used Zuora `subscription` table, but this could be applied to any other table in the Stitch Zuora data pipeline.

#### Step 1:- Rename existing table with the date suffix to identity the backup, recommended format YYYYMMDD

```sql
    ALTER TABLE "RAW"."ZUORA_STITCH"."SUBSCRIPTION" RENAME TO "RAW"."ZUORA_STITCH"."SUBSCRIPTION_20210903";
```

#### Step 2:- Pause the regular integration

![Pause Regular integration](/images/Stitch_table_reset/Stitch_2.png "Stitch_int_2")

#### Step 3:- Create a new integration Zuora-Subscription in Stitch

While setting it up setup the extraction frequency to 30 minutes and date from extraction to 1st Jan 2012 to ensure all data gets pulled through.

![With only the subscription table to replicate](/images/Stitch_table_reset/Stitch_1.png "Stitch_int_1")

#### Step 4:- Run the newly created integration

Try running the newly created integration manually and wait for it to complete. Once completed then and it shows on the home page successfully. Once done Pause the newly integration task because we don't want any misaligned data while we follow the next steps.

#### Step 5:- Check for the records

In the newly created table `"RAW"."ZUORASUBSCRIPTION"."SUBSCRIPTION"` cross-check the number of rows showing as loaded in the integration UI in stitch and loaded in the table is same.

#### Step 6:- Create the table in the main schema

Move the newly loaded data to `ZUORA_STITCH` schema because the new integration will create the table in the `ZUORASUBSCRIPTION` as stated above in the image.

```sql
    CREATE TABLE "RAW"."ZUORA_STITCH"."SUBSCRIPTION" CLONE  "RAW"."ZUORASUBSCRIPTION"."SUBSCRIPTION";
**Note:** Check for the primary key present in the table post clone or not if not check for the primary key in the [link](https://www.stitchdata.com/docs/integrations/saas/zuora#subscription) and add the constraints on those columns.
```

#### Step 7:- Make records count check to ensure we don't have fewer records in the new table

```sql
    select count(*) from "RAW"."ZUORA_STITCH"."SUBSCRIPTION_20210903" where deleted = 'FALSE';
    select count(*) from "RAW"."ZUORA_STITCH"."SUBSCRIPTION" ;
```

#### Step 8:- Drop the new schema

```sql
    DROP SCHEMA "RAW"."ZUORASUBSCRIPTION"  CASCADE ;
```

#### Step 9:- Delete temp Zuora-Subscription integration and enable regular integration

#### Step 10:- Run regular integration and validate

This is to ensure that error observed previously to the table is gone and data is getting populated in the table.
Check on duplicate ids due to 2 different extractors, to ensure the data is getting populated in the table correctly.

```sql
    select id, count(*) from "RAW"."ZUORA_STITCH"."SUBSCRIPTION"
    group by id
    having count(*) > 1
**Note** Refer to the [MR (internal link)](https://gitlab.com/gitlab-data/analytics/-/issues/10065#note_668365681) for more information.
```

### Source freshness errors

See the [source contact spreadsheet](https://docs.google.com/spreadsheets/d/1VKvqyn7wy6HqpWS9T3MdPnE6qbfH2kGPQDFg2qPcp6U/edit) for who to contact if there are external errors related to a source.

### Airflow Task failure

|   |
| ------------------------- |
| DAG `gitlab_com_db_extract` <br> Task `gitlab-com-dbt-incremental-source-freshness`  <br> |
| Background: This extract relies on a copy (replication) database of the GitLab.com environment. Its high likely that this is the root cause of a high replication [lag](https://prometheus-db.gprd.gitlab.net/graph?g0.expr=(pg_replication_lag)%20and%20on(instance)%20(pg_replication_is_replica%7Btype%3D~%22postgres-(archive)%22%7D%20%3D%3D%201)&g0.tab=0&g0.stacked=0&g0.range_input=1w&g1.expr=pg_long_running_transactions_age_in_seconds%7Btype%3D~%22postgres-(archive)%22%7D&g1.tab=0&g1.stacked=0&g1.range_input=6h). |
| More information of the setup [here (internal link)](https://gitlab.com/gitlab-data/analytics/-/issues/8283#note_537332709).  |
| Possible steps, resolution and actions: - Check for replication lag <br> - Pause the DAG if needed <br> - Check for data gaps <br> - Perform backfilling <br> - Reschedule the DAG  |
| Note: The GitLab.com data source is a very important data source and commonly used. Please inform an update business stakeholders accordingly. |

### Sheetload - Column '#REF!' is not recognised

|   |
| ------------------------- |
| DAG `sheetload` <br> Task `dbt-sheetload`  <br> |
| Background: This is an issue with Google sheets when data is being imported from a second sheet using Google sheets' import function. Occasionally the connections between the sheets stop working and the sheet needs to be refreshed. |
| More information of the setup [here](https://internal.gitlab.com/handbook/enterprise-data/platform/pipelines/#sheetload).  |
| Possible steps, resolution and actions: <br> - In general you should just need to open the Google sheet which is failing and confirm the data has been re-populated. <br> - If you do not have access to the sheet contact @gitlab-data/engineers and confirm if anyone else does. |

### Model version_usage_data_unpacked stale

When got an error for model `version_usage_data_unpacked` and error looks like:

```console
[2022-01-26 11:56:32,233] INFO - b'\x1b[33mDatabase Error in model version_usage_data_unpacked (models/legacy/version/xf/version_usage_data_unpacked.sql)\x1b[0m\n'
[2022-01-26 11:56:32,233] INFO - b' 000904 (42000): SQL compilation error: error line 241 at position 12\n'
[2022-01-26 11:56:32,233] INFO - b" invalid identifier '{metrics_name}'\n"
[2022-01-26 11:56:32,233] INFO - b' compiled SQL at target/compiled/gitlab_snowflake/models/legacy/version/xf/version_usage_data_unpacked.sql\n'
[2022-01-26 11:56:32,234] INFO - b'\n'
```

The root cause of this issue is when new metrics are introduced in an upstream model - and this model (along with model `version_usage_data_unpacked_intermediate`) try to pivot values to columns. Without full refresh, this will not happen under the pipeline.

Full refresh required as per instructions from [dbt models full refresh - internal handbook](https://internal.gitlab.com/handbook/enterprise-data/platform/infrastructure/#dbt-full-refresh).

An example for this failure is the issue: **[#11524 (internal link)](https://gitlab.com/gitlab-data/analytics/-/issues/11524)**

### Zuora Revenue Source and Target Column Mismatch

Sometimes Zuora Revenue source system as part of a certain release modify the source table definition by adding/removing column(In a year once or twice). Whenever this type of change happens it triggers failure in the loading task in DAG `zuora_revenue_load_snow`.

For example, there was 3 additional column added to table `BI3_RC_POB` which lead to the below error message.

```console
[2022-03-21, 13:26:48 UTC] INFO - sqlalchemy.exc.ProgrammingError: (snowflake.connector.errors.ProgrammingError) 100080 (22000): 01a31326-0403-d02c-0000-289d37f10d4e: Number of columns in file (102) does not match that of the corresponding table (99), use file format option error_on_column_count_mismatch=false to ignore this error
[2022-03-21, 13:26:48 UTC] INFO -   File 'RAW_DB/staging/BI3_RC_POB/BI3_RC_POB_12.csv', line 3, character 1
[2022-03-21, 13:26:48 UTC] INFO -   Row 1 starts at line 2, column "BI3_RC_POB"[102]
[2022-03-21, 13:26:48 UTC] INFO -   If you would like to continue loading when an error is encountered, use other values such as 'SKIP_FILE' or 'CONTINUE' for the ON_ERROR option. For more information on loading options, please run 'info loading_data' in a SQL client.
```

When this kind of failure happens we need to alter/create or replace the target table and add the additional column to the table definition in RAW.ZUORA_REVENUE schema. It is good to practise creating or replacing because it requires doing the full refresh of the data because of the addition of a new column.

Below are set of steps that will guide you to resolve this.

**Step 1:-**  Download the first file from the storage to local to view the additional column. For any file, only the file name and folder name should be modified.

```console
gsutil cp  gs://zuora_revpro_gitlab/RAW_DB/staging/BI3_RC_POB/BI3_RC_POB_1.csv .
```

For any other file, only the file name and folder name should be modified. For example table, `BI3_RC_BILL` above command will change to `gsutil cp gs://zuora_revpro_gitlab/RAW_DB/staging/BI3_RC_BILL/BI3_RC_BILL_1.csv .`

**Step 2:-** Once the file is downloaded look for the header of the file using the below command

```console
head -1 BI3_RC_POB_1.csv
```

**Step 3:-** Pull out the current table definition from snowflake using the below query

```sql
USE ROLE LOADER;
USE DATABASE RAW;
USE SCHEMA ZUORA_REVENUE;
select get_ddl('table','BI3_RC_POB');
```

Prepare the CREATE OR REPLACE TABLE query by comparing the missing column from the header and the table definition and adding them to the new table. The missing column should be at the end and the data type should be varchar.
Deploy the modified SQL.

**Note:-** If the table doesn't exist then create the table with all the column named present in header with datatype as Varchar.

**Step 4:-** Move the log file from the process folder to the staging folder of the table.

```console
gsutil cp gs://zuora_revpro_gitlab/RAW_DB/processed/22-03-2022/BI3_RC_POB/BI3_RC_POB_22-03-2022.log  gs://zuora_revpro_gitlab/RAW_DB/staging/BI3_RC_POB/
```

The point to consider in this command is the date in the path and the log file name. If the failure happened on `23-03-2022` then it will become `gs://zuora_revpro_gitlab/RAW_DB/processed/23-03-2022/BI3_RC_POB/BI3_RC_POB_23-03-2022.log`

Validate in [GCS storage](https://console.cloud.google.com/storage/browser/zuora_revpro_gitlab/RAW_DB/staging?project=gitlab-analysis&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&prefix=&forceOnObjectsSortingFiltering=false) that the log file is present for the respective table.

**Step 5:-** Re-run the task from the airflow by clearing the task.

## Useful regex

### Match lines where these terms do not exist

`^(?!.*(<First term to find>|<Second term to find>)).*$`

e.g. For cleaning up Airflow logs:

`^(?!.*(Failure in test|Database error)).*$`
