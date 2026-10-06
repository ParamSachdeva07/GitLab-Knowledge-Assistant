---
title: "Data Team Incident Management"
description: "Incident Management covers incident definitions, creation, resolution and communication procedures. The goal is to establish a structured process for rapidly detecting, responding to, and resolving unplanned disruptions to business operations in order to minimize impact and restore normal service as quickly as possible. content around managing, securing, and governing the Enterprise Data Platform and related activities."
---

## Why Incident Management Matters

* **Consistency and Reliability in Data Operations** - As the GitLab Data team manages critical analytics infrastructure and data pipelines that support business decision-making across the organization, having standardized incident management processes ensures consistent response times and resolution quality. Without clear guidelines, incidents may be handled differently by various team members, leading to inconsistent outcomes and potentially prolonged downtime that impacts data availability for stakeholders.
* **Improved Response Times and Accountability** - Standardized incident management creates clear escalation paths, defined roles and responsibilities, and established communication protocols. This structure eliminates confusion during high-pressure situations, ensuring that the right people are notified quickly and that response efforts are coordinated effectively. When everyone knows their role and the expected procedures, incidents can be resolved faster with less organizational friction.
* **Knowledge Preservation and Continuous Improvement** - Formal incident management processes include documentation requirements that capture what went wrong, how it was resolved, and what can be improved. This creates an institutional knowledge base that helps prevent similar incidents in the future and enables new team members to learn from past experiences. The structured approach also facilitates post-incident reviews that drive systematic improvements to data infrastructure and processes.
* **Stakeholder Communication and Trust** - Clear incident management standards ensure that affected stakeholders receive timely, accurate updates about data availability issues. This transparency builds trust with business users who depend on data for their operations and helps manage expectations during outages. Consistent communication also demonstrates the Data team's professionalism and commitment to service reliability.
* **Compliance and Risk Management** - For a data team handling sensitive business information, having documented incident response procedures helps meet compliance requirements and reduces organizational risk. Standardized processes ensure that security considerations are consistently addressed during incidents and that appropriate stakeholders are notified when data integrity or confidentiality may be compromised.

## Outcome of Incident Management Mechanism

Faster Problem Resolution

* **Reduced downtime** for critical data pipelines, ETL/ELT processes, and analytics dashboards
* **Clear escalation paths** when data quality issues, pipeline failures, or performance degradation occur
* **Documented troubleshooting procedures** for common issues like failed data loads, schema changes, or API rate limits

Better Data Quality & Reliability

* **Proactive monitoring** catches data anomalies, missing data, or drift before downstream users are affected
* **Root cause analysis** helps identify systemic issues in data infrastructure (e.g., recurring transformation failures, source system instabilities)
* **Service level objectives (SLOs)** for data freshness, completeness, and accuracy become measurable and enforceable

Improved Collaboration

* **Clear ownership** of data assets and pipelines - knowing exactly who to contact when specific data sources or models break
* **Cross-functional** coordination between data teams and stakeholders during outages (e.g., notifying analysts when marts are unavailable)
* **Shared knowledge base** of past incidents helps new team members understand common failure patterns

## I. Incident Definition, Severity and Creation

### 1. Incident Definition

An incident is any anomalous condition that results in—or may lead to—service degradation, data quality issues, or system outages that require immediate human intervention to prevent disruptions or restore operational status.

Incidents may manifest through:

* **Availability Issues**: Data, dashboards, or analytics tools becoming inaccessible or unavailable to users
* **Quality Degradation**: Data inaccuracy, corruption, validation failures, or unexpected schema changes
* **Timeliness Violations**: Data not refreshing within expected timeframes, stale metrics, or delayed reporting
* **Processing Failures**: Pipeline breakages, ETL/ELT job failures, model errors, or instrumentation logic failures that impact downstream processes
* **Security Concerns**: Unauthorized data exposure, access control breaches, or data leakage
* **Collection Disruptions**: Interruption to event tracking, data capture mechanisms, or source system failures

**Incident Criteria** - not all issues qualify as incidents. An incident must meet one or more of these criteria:

* Whether there is immediate impact on downstream models or dependencies, business operations or data consumers
* Whether there is an SLO breach
* Whether there is immediate action required
* Whether there is potential for permanent data loss or corruption if not addressed immediately

### 2. Incident Severity

Incident severity is determined by evaluating three key dimensions:

* Business disruption and impact
* Data criticality and impact
* Downstream dependencies

Based on the factors above, we formulate the severity levels below:

* Sev1: Production data pipelines failed, customer-facing teams blocked, critical business decisions cannot be made, data breach/exposure, impending or actual data loss affecting multiple systems/metrics, or moderate to severe degradation in business-critical metrics.
* Sev2: Significant workflow disruption requiring manual workarounds, data pipeline delays impacting downstream consumers, potential security vulnerability/compliance issues, or partial system/service degradation.
* Sev3: Inconvenience but work continues with minimal impact, non-critical data pipeline delays, internal-only data inappropriately accessed, performance degradation in development/staging environments, or minor data quality issues with known workarounds.
* Sev4: Nice-to-have features/improvements missing, cosmetic issues, documentation updates needed, or technical debt items with no immediate operational impact.

When in doubt between two severity levels, choose the higher one initially. Severity can be downgraded or re-classified as more information becomes available and understanding improves.

### 3. Incident Creation

Once you decide to create an incident, you can follow the following steps:

1. Use the incident template in the appropriate project folder
2. Document all essential information
3. Add `incident` and `sev` labels
4. Assign to the right DRI and tag relevant team members
5. Communicate via Slack

Incident VS Issue: Use `/type incident` to convert issues to incidents when escalation is needed.

**Tooling**:

Depending on the types of incidents:

* If you have to collaborate with SREs on-call (i.e. in case of Postgres pipeline issues), then use [incident.io](https://incident.io/) to log and track incidents. However, there should always be a corresponding Incident within GitLab in our Analytics project (created by data team members).
* For all other types of incidents, create a brand new issue or incident on GitLab [here](https://gitlab.com/gitlab-data/analytics/-/issues/new?type=ISSUE) with `incident` label. You can use `/type incident` to convert the issue to incident.

Note: For cases when there is minimal impact on data and manual steps or correction is needed, please raise a bug rather than an incident.

## II. Incident Resolution

Immediate Response

* All incidents require immediate attention upon detection.
* Every incident must have a DRI assigned. The triager or creator serves as interim DRI until another team member actively engages in resolution.

Resolution Approach

* Prioritize implementing a fix, even a temporary workaround, before pursuing long-term solutions.
* Managers review severity assessments (determined by the detection DRI) and prioritize work accordingly.

For data incidents, we distinguish clearly between **mitigation** and **resolution**:

An incident should be treated as **resolved** only when all of the following are true:

* The underlying cause has been fixed and validated (for example, pipelines are stable, infrastructure is no longer degraded).
* Impacted data has been fully backfilled, re‑processed, or otherwise corrected so that downstream models, dashboards, and reports are accurate and meet our timeliness SLOs.
* Affected stakeholders are unblocked and can rely on the data again. Incidents should **not** be closed purely when the part of the work is complete, if the data downstream remains stale or incorrect. The incident stays open until the data is fully refreshed and accurate (owning the outcome).

This ensures our “time to resolve” matches the period during which users experienced degraded or unreliable data, not just the time until code or infrastructure changes were deployed.

If multiple teams are involved, i.e. of a data pipeline failure (the Data Platform Team resolves the pipeline outage) and downstream dbt models are impacted (The Analytics Engineering team has to perform backfills), it could be that 2 separate incidents are opened (1 by Data Platform Team, 1 by Analytics Engineering team), in this case you _can_ create an overarching incident that links to these 2 child incidents. The overarching incident stays open until both incidents are resolved (to indicate the time to resolve) where the 2 child incidents are independently closed.

Communication

* DRIs must provide regular status updates in the incident channel, including expected resolution timelines once available.

Closure
Close incidents promptly **after** verifying that:

* the fix is working as intended, **and**  
* the affected data has been fully refreshed and validated against our SLOs, **and**  
* downstream consumers (for example, key dashboards or recurring reports) are no longer relying on temporary workarounds.

If part of the work is completed but data backfills or re‑computations are still in progress, keep the incident open and document this explicitly in the timeline and status updates. The incident is closed only when both the technical fix and the data state are back to normal.

* Conduct a retrospective for each incident to identify preventive measures and avoid future occurrences

Incident SLOs

| Severity | TTR (time to response) | TTM (time to mitigate) | TTR (time to resolve) |
| :-- | :-- | :-- | :-- |
| Sev1 | 2 hours | 1 day | 7 days |
| Sev2 | 4 hours | 3 days | 30 days |
| Sev3 | 24 hours | 7 days | 60 days |
| Sev4 | 48 hours | 30 days | 90 days |

* Mitigation: A temporary band-aid fix aimed at reducing further impact by quickly investigating and addressing the immediate cause
* Resolution: A long-term, permanent solution that follows standard work processes to completely eliminate the root cause

Resources

* To find the right DRI for assigning the incident, you can refer to this [codeownerfile](https://gitlab.com/gitlab-data/analytics/-/blob/master/CODEOWNERS) for code ownership.
* For members from Analytics Instrumentation org, you can check [monitoring and troubleshooting guide](/handbook/engineering/data-engineering/analytics/analytics-instrumentation/monitoring_troubleshooting/) as a reference.
