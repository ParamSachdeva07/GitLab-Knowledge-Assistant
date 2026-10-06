---
title: Investigate DB performance issues
description: This guide provides steps for working with our engineering team to investigate DB performance issues.
category: Self-managed
---

## When to use

Use this workflow when a customer reports performance symptoms that appear **database-driven**, for example:

- Slow page loads, API calls, or Sidekiq jobs with high `db_duration_s` / `db_count`
- Lock contention, blocked queries, or high database CPU / I/O
- Slow background migrations or maintenance tasks
- Repeated timeouts where traces show database bottlenecks

---

## Workflow

### 1. Initial triage and scoping

1. Clarify **what is slow** and **for whom**:

   - Specific endpoints, actions, or workflows (for example, MR load, pipeline view, API calls)
   - Scope and impact (for example, user / project / entire instance)

1. Capture **environment details** in the ticket:

   - GitLab version, deployment type (Omnibus / Helm / Dedicated), reference architecture size
   - Database engine/version, hosting (VM, managed DB, bare metal), HA/replica setup

1. Confirm it is likely **DB-related**:

   - Metrics or logs showing high DB time, high `db_count`, lock waits, or obvious slow queries

   An example JQ query to identify Sidekiq events with long DB durations:

```shell
cat current | jq -Rr 'fromjson? | select(.db_primary_duration_s != null and .db_primary_duration_s > 30) | [(.duration_s * 1000 | round / 1000), (.redis_duration_s * 1000 | round / 1000), (.db_primary_duration_s * 1000 | round / 1000), (.cpu_s * 1000 | round / 1000), ."meta.feature_category", .queue, .class, .correlation_id] | @tsv'
```

### 2. Collect concrete evidence

Gather enough to uniquely characterize the problem:

- **Minimal reproducible description** (if possible)
- **Representative examples**:
  - Request IDs, job IDs, or traces for slow operations
  - Sample slow queries or query fingerprints
- **Timeline and changes**:
  - When the issue started, recent upgrades, config changes, or traffic spikes
- **Key metrics / screenshots**:
  - DB CPU, I/O, connections, locks, slow query charts
    - You can use [GitLab PostgreSQL Connection Calculator](https://postgresql-connection-calculator-759014.gitlab.io/) to calculate the maximum database connections.

Keep these linked from the ticket for later use in issues/epics.

### 3. Cross-reference existing investigations

1. **Search GitLab.com / Dedicated logs for similar patterns** (if you have access or through Infra):

   - Same worker names or endpoints
   - Same query signature or error text
   - Similar symptom patterns: timeouts, N+1-like behavior, memory spikes, etc.
   - Example Elastic search: https://log.gprd.gitlab.net/app/r/s/0Bvmn

1. **Search GitLab issues** (`gitlab-org/gitlab` and relevant groups):

   - Search by:
     - Worker or service names (for example, specific background jobs)
     - Endpoint or feature names
     - Query patterns or error strings
   - Filter by labels where relevant, for example:
     - `performance`, `infradev`, `SLO::Missed`, `GitLab Dedicated`, `bug::availability`
   - Check any obvious related performance epics (for the affected area).

1. **Check infrastructure / Dedicated trackers**:

   - Look for GitLab.com / Dedicated incidents with similar:
     - Symptoms (timeouts, high DB load, lock contention)
     - Error messages or query patterns
     - Workers / features

1. **Consult owning development group if needed**:

   - Use the RFC process to avoid investigating in isolation.
   - When you see a likely match but are unsure, @-mention the relevant group on an existing issue and briefly summarize customer evidence.

### 4. Decide: existing issue vs new issue

#### 4.1 When you find a good match

If there is an existing GitLab issue that matches the customer symptoms:

- **Link the ticket** to the issue:
  - Add a short comment in the GitLab issue with:
    - Deployment type, GitLab version
    - Instance size / notable configuration
    - High-level impact (for example, "Ultimate, ~10k active users, many MRs per day")
- Ensure customer-related labels are present:
  - `customer` and relevant deployment-type/performance labels where appropriate
- Note **any mitigations** tried or known (from .com / Dedicated or docs) and whether they helped.

#### 4.2 When you **don't** find a match

1. If similar patterns **are** present on .com or Dedicated:

   - **Create a new issue** in `gitlab-org/gitlab` (or appropriate project) that:
     - Summarizes the problem
     - Includes evidence from both:
       - The customer environment, and
       - GitLab.com / Dedicated logs
   - Add labels such as:
     - `customer`, `performance`, `infradev`, and deployment-type labels
   - Tag the owning group and link to any related epics.
   - Link the customer ticket to this new issue.

1. If **no similar patterns** show up on .com / Dedicated:

   - Treat it as **potentially self-managed-specific**:
     - Configuration, scaling, or environment-specific behavior
   - If the issue is **significant and reproducible**, still **open a GitLab issue** with:
     - Clear reproduction notes
     - Customer impact
     - Any hypotheses (for example, schema, index, configuration, or workload characteristics)

### 5. Drive the database investigation

While the cross-reference work proceeds, continue driving the technical investigation:

- Use existing **Database Help / DB Support Pod** workflows for:
  - Query analysis and slow-query identification
  - Index / schema review and background migration checks
  - Lock / blocking analysis and connection saturation
- Loop in **Database Engineering / DBO** when:
  - The issue appears systemic or risky to change
  - You need deeper guidance on schema, partitioning, or background migrations

Document your findings in the ticket and, when relevant, in the linked GitLab issue.

### 6. Close the feedback loop

To make the work re-usable across deployments:

- **As new information appears** (from customer or Infra):
  - Add it to the linked GitLab issue as a comment.
- When a **fix or mitigation** is merged:
  - Record:
    - Version(s) containing the fix
    - Any backports or feature flags required
  - Help the customer apply and verify the fix.
- After validation:
  - Comment on the GitLab issue with:
    - Customer confirmation and any metrics before/after
    - Whether the same fix should be proactively considered for other deployment types.

---

## Related

- [Database Support Pod documentation](../../support/support-pods/database/)

---

## Reference

- [RFC: Process for Cross-Referencing Self-Managed Performance Issues with GitLab.com and GitLab Dedicated](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/7411)
