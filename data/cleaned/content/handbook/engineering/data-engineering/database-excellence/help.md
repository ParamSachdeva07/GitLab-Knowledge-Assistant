---
title: Getting Help with Database Issues
description: "A decision tree for finding the right help for database-related issues"
---

This guide walks you through finding the right help for any database-related issue. Start at Step 1 and follow the path that matches your situation.

## Step 1: What kind of help do you need?

* **There is an active S1/S2 incident on GitLab.com or Dedicated** -> Go to [Step 3: GitLab.com or Dedicated incident](#step-3-gitlabcom-or-dedicated-incident)
* **A self-managed customer is having a database problem** -> Go to [Step 2: Customer database issue](#step-2-customer-database-issue)
* **I need to file or route a non-urgent issue** -> Go to [Step 6: File a non-emergency issue](#step-6-file-a-non-emergency-issue)

## Step 2: Customer database issue

**Start by reaching out to our support stable counterparts** — they have context on common customer database issues and can help triage before escalating to engineering.

**First**: Post in `#spt_pod_database` and reach out to the [Database Pod team](https://gitlab.com/gitlab-com/support/support-pods/-/tree/main/Database?ref_type=heads) (database support stable counterparts). They can help determine the right path and whether engineering involvement is needed.

Then, determine what kind of issue this is:

**Is the issue related to a specific feature, migration, query, or endpoint?**

* **Yes** -> The feature team is the best first point of contact, even when the symptom looks database-related. Go to [Step 5: Identify the responsible team](#step-5-identify-the-responsible-team) to find them.

**Is the issue related to backups or restore?**

* **Yes** -> Backup and Restore are managed by the team that owns the [feature category `backup_and_restore`](/handbook/product/categories/lookup/).

**Is the issue related to Postgres packaging or configuration in Omnibus or Charts?**

* **Yes** -> Reach out to the [GitLab Delivery section](/handbook/engineering/infrastructure-platforms/gitlab-delivery/) in `#s_gitlab_delivery` who manages self-managed packaging and configuration.

**Is this a general database issue** (performance degradation not limited to a single feature, operational questions, upgrade failures, configuration guidance)?

* **Yes** -> File a support Request for Help:
  1. Confirm the issue has already been raised in `#spt_pod_database` with the stable counterparts
  2. File a [Request for Help issue](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-DatabaseFrameworks) using the database support template
  3. Request a [database SOS dump](https://docs.gitlab.com/administration/raketasks/maintenance/#collect-information-and-statistics-about-the-database) from the customer if possible
  4. Mention `@gitlab-org/database-team/triage` on the issue

  Include in the RFH:

  * Customer installation size and architecture information
  * PostgreSQL version, number of replicas, pgbouncer configuration, hosting details (managed service vs VM, cloud provider)
  * Add a db:sos dump if possible
  * Steps to reproduce
  * Relevant logs and observed monitoring metrics
  * Customer impact (deal pending, escalated, show stopper, etc.)

**Is the customer issue urgent and you need a faster response?**

* **Yes** -> After filing the RFH, go to [Step 4: Escalate to Database Excellence](#step-4-escalate-to-database-excellence).

## Step 3: GitLab.com or Dedicated incident

**Is the application (or a major component like Sidekiq) down or broadly unresponsive due to a database issue?**

* **Yes, widespread outage** -> This is an all-hands situation.
  1. Post in `#s_database_excellence` and tag `@db-team` and `@dbo-oncall`
  2. Ensure `/inc escalate` has been used in the incident channel to page the on-call database engineer via [incident.io](https://app.incident.io/gitlab/on-call/schedules/01JXJ7MN4T14008GQKWYYNT6E8)

**Is the incident related to database configuration or operations** (e.g., connection errors, replication errors, SSL errors, Postgres operations)?

* **Yes** -> Use `/inc escalate` in the incident Slack channel to page the on-call database engineer. See the [incident escalation process](/handbook/engineering/data-engineering/database-excellence/#incident-escalation) for full details.

**Is the incident related to application behavior** (e.g., PG timeout errors, slow queries, long-running transactions, failing migrations)?

* **Yes** -> First try to identify the responsible feature team. Go to [Step 5: Identify the responsible team](#step-5-identify-the-responsible-team). If you cannot identify the source or need database expertise urgently, go to [Step 4: Escalate to Database Excellence](#step-4-escalate-to-database-excellence).

## Step 4: Escalate to Database Excellence

When escalating, be as specific as possible. Per [communication guidelines](/handbook/communication/#writing-style-guidelines), avoid acronyms whenever possible. Always include:

* A link to the issue, Sentry error, incident, or Zendesk ticket
* The text of any error messages
* Links to any applicable charts or dashboards
* Details about the query, migration, or issue

**For ongoing GitLab.com or Dedicated incidents:**

1. Post in `#s_database_excellence`
2. If there is no response within 15 minutes, or the request is urgent, tag `@db-team` and `@dbo-oncall` in a thread on the original message
3. If there is still no response after another 15 minutes and the request is urgent, use Slack to find the phone number of the Database Excellence stage lead and text or call them

**For emergency self-managed escalations:**

1. Post in `#s_database_excellence` with details, a link to the Zendesk ticket and RFH issue
2. Tag the `@db-team` in the thread

### Incident escalation details

Database incident escalations use [incident.io](https://app.incident.io/gitlab/on-call/schedules/01JXJ7MN4T14008GQKWYYNT6E8) for on-call routing.

* **Scope**: GitLab.com S1 and S2 production incidents raised by the Incident Manager On Call, Engineer On Call, and Security teams. GitLab Dedicated support is consultative. Self-managed support is discretionary and evaluated case-by-case.
* **How to escalate**: Use `/inc escalate` in the incident Slack channel. For non-urgent issues, use the [triage rotation](/handbook/engineering/data-engineering/database-excellence/#triage-rotations) or post in `#s_database_excellence`.
* **Response**: Best effort, local timezone, weekday coverage only (24/5). The on-call engineer joins as a subject matter expert in a consultative capacity. There should be no expectation that the on-call engineer is solely responsible for resolving the escalation — they may need to bring in other subject matter experts.
* **Warm handoffs**: The on-call engineer is responsible for coordinating warm handoffs during shift changes, especially when there is an ongoing active incident.

### Escalation process

1. EOC/IM, Development, or Security pages the on-call database engineer via `/inc escalate`
1. On-call engineer acknowledges the page and joins the incident channel and Zoom
1. On-call engineer triages the issue and works towards a solution
1. If necessary, on-call engineer reaches out for further help or domain experts as needed
1. If on-call does not respond, the escalation path defined within incident.io takes effect

### For on-call responders

#### Responding guidelines

When responding to an incident:

1. Join the incident Zoom — this can be found bookmarked in the relevant incident Slack channel
1. Join the appropriate incident Slack channel for all text-based communications (normally `#inc-<INCIDENT NUMBER>`)
1. Work with the EOC to determine if a known code path is problematic
   * If the issue is in your domain, continue working with the EOC to troubleshoot
   * If the issue is unfamiliar, attempt to determine code ownership by team — this enables bringing an engineer from that team into the incident
1. Work with the Incident Manager to ensure the incident issue is assigned to the appropriate Engineering Manager

#### Shadowing

* **Shadowing an incident**: Watch for active incidents in `#incidents-dotcom` and join the Situation Room Zoom call for synchronous troubleshooting. See [this blog post](https://about.gitlab.com/blog/2020/04/13/lm-sre-shadow/) about the shadowing experience.
* **Shadowing a shift**: Contact the current on-call engineer to let them know you'll be shadowing, then monitor `#incidents-dotcom` during the shift.
* **Replaying previous incidents**: Situation Room recordings from previous incidents are available in the [Google Drive folder](https://drive.google.com/drive/u/1/folders/1wtGTU10-sybbCv1LiHIj2AFEbxizlcks) (internal).

#### Troubleshooting resources

1. [How to Investigate a 500 error using Sentry and Kibana](https://www.youtube.com/watch?v=o02t3V3vHMs&feature=youtu.be)
1. [Walkthrough of GitLab.com's SLO Framework](https://www.youtube.com/watch?v=QULzN7QrAjY)
1. [Scalability documentation](https://gitlab.com/gitlab-org/gitlab/merge_requests/18976)
1. [Use Grafana and Kibana to look at PostgreSQL data to find the root cause](https://youtu.be/XxXhCsuXWFQ)
1. [Use Grafana and Prometheus to troubleshoot API slowdown](https://www.youtube.com/watch?v=DtP4ZcuXT_8)

#### Dashboards

1. [Saturation Component Alert](https://dashboards.gitlab.net/d/alerts-saturation_component/alerts-saturation-component-alert?orgId=1)
1. [Service Platform Metrics](https://dashboards.gitlab.net/d/general-service/general-service-platform-metrics?orgId=1)
1. [SLAs](https://dashboards.gitlab.net/d/general-slas/general-slas?orgId=1)
1. [Web Overview](https://dashboards.gitlab.net/d/web-main/web-overview?orgId=1)

## Step 5: Identify the responsible team

Most database application issues are best handled by the team that owns the related feature. Even if the error has "database" in it, the feature team is typically best suited to resolve it because they understand the involved data patterns.

**Does the error include a feature category** (from Sentry, a Rails controller, Sidekiq worker, API endpoint, or background migration)?

* **Yes** -> Look up the team in the [feature category lookup](/handbook/product/categories/lookup/). Reach out in that team's Slack channel and `@mention` the team's manager. If they don't respond, go to [Step 4: Escalate to Database Excellence](#step-4-escalate-to-database-excellence).

**Is the issue related to a migration?**

* **Yes** -> From the [GitLab repository](https://gitlab.com/gitlab-org/gitlab), run:

  ```sh
  git log --first-parent {path/to/migration.rb}
  ```

  The migration file path can be found in the backtrace. Migration files start with a date-time stamp and are in [db/migrate/](https://gitlab.com/gitlab-org/gitlab/-/tree/master/db/migrate) or [db/post_migrate/](https://gitlab.com/gitlab-org/gitlab/-/tree/master/db/post_migrate). If you can find the timestamp (e.g., `20240113071052`) in the customer's log output, it will uniquely match a migration filename.

  The `git log` output should include a link to the merge request, which will identify the responsible team. If it does, contact that team. If not, try identifying the team by table name (next option).

**Can you identify a database table involved in the issue?**

* **Yes** -> Look for `{table_name}.yml` in [the database dictionary](https://gitlab.com/gitlab-org/gitlab/-/tree/master/db/docs). The file lists `feature_categories` which you can use to find the team via the [feature category lookup](/handbook/product/categories/lookup/). If there is more than one category, pick one and start with that team.

**Is the issue related to a query but you don't have a feature category?**

* **Yes** -> If the query comes from a Rails controller, Sidekiq worker, API endpoint, or background migration, determine the feature category using the [feature categorization guide](https://docs.gitlab.com/ee/development/feature_categorization/), then look up the team as described above. If you cannot determine the source, try identifying the team by table name using the tables referenced in the query.

**I can't identify the source or the owning team isn't responding.**

* Go to [Step 4: Escalate to Database Excellence](#step-4-escalate-to-database-excellence)

## Step 6: File a non-emergency issue

**Do you need something from the Database Excellence team** (consultation, infrastructure change, stable counterpart, project work)?

* **Yes** -> Submit a [work request](https://gitlab.com/gitlab-org/database-team/team-tasks/-/work_items/new?description_template=work_request) in `database-team/team-tasks`. This is the single intake point for all external requests. See the [Database Excellence stage page](/handbook/engineering/data-engineering/database-excellence/) for routing details.

**Is this an existing issue in `gitlab-org/gitlab` that needs database team attention?**

* **Yes** -> Add the `~database` label. The Database Excellence [triage rotation](/handbook/engineering/data-engineering/database-excellence/#triage-rotations) will pick it up.

**Is this an application issue where you know the responsible feature team?**

* **Yes** -> Label the issue with that team's group label. The feature team is the best first point of contact.

**Is this related to the packaged Postgres in Omnibus or Charts?**

* **Yes** -> Label the issue `~"group::distribution"`

**Is the issue blocking and you need to escalate?**

* **Yes** -> Go to [Step 4: Escalate to Database Excellence](#step-4-escalate-to-database-excellence)
