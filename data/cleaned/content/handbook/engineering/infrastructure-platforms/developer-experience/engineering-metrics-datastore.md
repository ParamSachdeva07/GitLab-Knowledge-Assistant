---
title: "Engineering Metrics Datastore"
description: "Overview of the engineering metrics datastore used by the Developer Experience section, covering CI execution, test execution, code coverage, performance tests, issues, and merge requests data"
---

## Instance

The Developer Experience section uses a [ClickHouse](https://clickhouse.com/) instance for storing and querying large-scale engineering metrics data. ClickHouse is a column-oriented database optimized for analytical workloads, making it well-suited for the data it holds: CI execution, test execution, code coverage, performance tests, issues, and merge requests.

For technical documentation on databases, tables, materialized views, and schemas, see the [Developer Experience ClickHouse databases catalog (internal only)](https://gitlab.com/gitlab-org/quality/engineering-productivity-infrastructure/-/blob/main/docs/clickhouse/databases.md).

### Instance Details

| Property | Value |
|----------|-------|
| **Hosting** | ClickHouse Cloud |
| **Instance Name** | CI_AND_TEST_METRICS |

### Data Retention

Most data is retained for **1 year**. Some datasets, such as code coverage, are retained for **3 months**.

## Dashboards

Dashboards powered by this datastore are listed on the [Developer Experience Dashboards](./dashboards) page.

## Access

The ClickHouse instance is internal and accessible to GitLab team members. To request access, submit an [Access Request](/handbook/eta/corporate-it/end-user-services/access-requests/).
