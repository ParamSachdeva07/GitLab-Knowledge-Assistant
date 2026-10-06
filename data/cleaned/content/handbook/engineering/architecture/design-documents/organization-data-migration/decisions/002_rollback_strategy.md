---
title: 'Rollback strategy for organization data migrations to Protocells'
status: proposed
creation-date: "2026-03-09"
authors: [ "@luciezhao" ]
dris: [ "@luciezhao" ]
owning-stage: "~devops::tenant scale"
participating-stages: ["~devops::tenant scale", "~group::geo"]
toc_hide: true
---

## Definitions

- **Data rollback**: Moving an Organization's data from the target cell back to the source cell, including any recent changes made on the target cell after the topology routing switch.
- **Topology routing switch**: The Topology Service controls routing of an Organization's traffic to the relevant cell. At the end of a successful data migration, the Topology Service switches the routing of traffic from the source cell to the target cell.
- **Fix-forward**: Resolving issues discovered on the target cell in place, rather than attempting to reverse the migration. This is the standard operational posture for production systems.
- **Go/No-Go gate**: A formal validation checkpoint that must be cleared *before* the topology routing switch is executed. If the gate is not cleared, the switch does not happen and the Organization remains on the source cell.

## Context

GitLab is migrating customer Organizations from the Legacy Cell to Protocells as part of the transition to a [Cell-based architecture](/handbook/engineering/architecture/design-documents/cells/). The migration tooling copies organization data (PostgreSQL, Git repositories, object storage, Container Registry) from the source cell to the target cell. Only after the migration is validated does the Topology Service execute a routing switch to direct traffic to the target cell.

A key question raised by Product and Engineering is: **if we discover issues after migrating an Organization to a Protocell, should we build the capability to move the data back?**

This question was extensively discussed across [Rollback Options (#581028)](https://gitlab.com/gitlab-org/gitlab/-/issues/581028), the [Protocells Steerco](https://gitlab.slack.com/archives/C09DFJTRNFJ/p1767791138987269), and the [Cells Migration Rollback capabilities call](https://docs.google.com/document/d/1sVISTctnx1RtimBpaDPV_jCBE9olsFFSHViYVsq5uDg). Four rollback options were evaluated: Topology Flip, Full Migration Back, Direct Transfer, and Congregate.

## Important

This ADR addresses migration rollback only. It does **not** replace the need for standard backup and disaster recovery procedures. Organization data must be backed up on both the source cell and the target cell independently of the migration process. Rollback is not a data protection mechanism — it is a migration recovery concept, and one we have decided not to support.

## Decision

**We will not support data rollback for organization data migrations.**

The topology routing switch will only be executed after the migration clears the go/no-go gate. This means we will never be in a position where traffic is routed to a target cell with incomplete data or unsupported features. If the gate is not cleared, the Organization remains on the source cell — no switch happens, and no rollback is required.

After the topology routing switch, we adopt a **fix-forward** posture for any issues discovered on the target cell.

### The go/no-go gate

The go/no-go gate is the primary risk mitigation mechanism. The topology routing switch will not be executed unless both of the following criteria are satisfied:

1. **Replicated data completeness** — All organization data on the target cell has been verified as complete and consistent with the source cell. This includes PostgreSQL data, Git repositories, object storage, and Container Registry data. Verification is performed through checksums, row counts, and spot checks against the source cell.

2. **Feature compatibility and supportability** — The target cell supports all features that the Organization requires. This includes confirming that the Organization does not depend on features that are unavailable or unsupported on the target cell (e.g., hosted runners, specific integrations, CI/CD capabilities). The Organization is not a candidate for migration if the target cell cannot fully support its workload.

If either criterion is not met, the topology routing switch does not happen. The Organization stays on the source cell, the migration is treated as a failed attempt, and the tooling or cell configuration is iterated upon before retrying.

#### Stage 1: Cutover validation (pre-user traffic)

This stage occurs **after data migration completes** and **before** any customer traffic is allowed to write to the target cell. The source cell remains the active production system.

**Minimum checks before proceeding:**

- **Routing and connectivity**
  - Topology Service correctly routes the org to the target cell.
  - SSH/HTTP access to repos from the target cell is working for representative users.
- **Authentication and session flows**
  - Primary auth flows (username/password, SAML/OmniAuth where applicable) succeed end-to-end for test accounts.
- **Data completeness**
  - Checksums and row counts for PostgreSQL data match the source cell.
  - Git repository checksums match.
  - Object storage and Container Registry data is present and accessible.
- **Basic functional smoke tests**
  - Read/write operations on key data types (projects, issues, pipelines) succeed for the migrated org.
  - No obvious data corruption or major gaps in migrated datasets.

If any of these checks fail, the topology routing switch does not happen. The migration is treated as a failed attempt ("go-around"), tooling and process are refined, and a new cutover window is scheduled.

After Stage 1 passes, controlled customer access is enabled with a **topology routing switch** on the target cell for **customer-facing final checks**:

- **Auth and sessions** — Customers can sign in via their expected auth methods (e.g., SAML/SSO where applicable).
- **Runners** — Representative CI jobs run successfully on the org's configured runners (or shared runners where applicable).
- **Integrations** — A curated set of critical integrations (SCM hooks, key webhooks, external issue trackers) are exercised and succeed.
- **Git operations** — Users can push code to key repos successfully and see expected behaviour in pipelines and MR flows.

### Switchback during Stage 2 only

A switchback — reversing the topology routing switch to re-route traffic back to the source cell without moving data — is only available during **Stage 2** of the go/no-go gate, while customer smoke testing is in progress.

If a customer-facing check fails during Stage 2 (e.g., runners don't work, a critical integration fails, git push behaves unexpectedly), we execute a switchback to the source cell and treat the migration as a failed attempt. The Organization resumes operating on the source cell, and the migration is retried after the issue is resolved.

**It is understood that any data created on the target cell during the Stage 2 smoke test window will be lost.** This is acceptable because the smoke test window is short, the data volume is minimal (limited to validation activity), and the customer is aware they are participating in a controlled validation.

Switchback is **not** available after Stage 2 completes and the migration is committed. Once the go/no-go gate is fully cleared and the topology routing switch is finalised, we adopt a fix-forward posture.

### Post-switch: fix-forward

After the topology routing switch, the Organization is live on the target cell. Any issues discovered at this point are resolved in place:

- **Minor data gaps** (e.g., a background job that didn't complete) are patched forward on the target cell.
- **Feature issues** are treated as production bugs and fixed with the same urgency as any GitLab.com incident.
- **Performance issues** are addressed through standard infrastructure tuning and scaling.

### Cohort-specific behaviour

| Cohort | Description | Pre-switch | Post-switch |
|--------|-------------|------------|-------------|
| Cohort 0 | Internal test organizations | Go/no-go gate; can discard and recreate | Fix-forward; no customer impact |
| Cohort A | Subset of inactive free users | Go/no-go gate | Fix-forward |
| Cohort B | Active opt-in beta (up to 1,000 orgs) | Go/no-go gate; feature parity required | Fix-forward |
| Cohort C | Top 1,000 orgs by database time | Go/no-go gate; feature parity required | Fix-forward |

### Source data retention

Organization data on the source cell is retained (read-only) for a defined retention period after the topology routing switch:

- **Cohorts 0/A**: Retained indefinitely while processes are hardened.
- **Cohorts B/C**: Retained for a defined window (to be determined by Product in consultation with DBREs and Tenant Scale), then pruned.

This retained data serves as a reference for investigation and data reconciliation, but is not intended to be "switched back to".

## Motivation

### Why data rollback is not viable

**The cost of rollback exceeds the cost of fix-forward.** Consider an Organization that is 95% functional on the target cell after the topology routing switch — perhaps a minor integration is misbehaving or a background job didn't complete. Data rollback would require:

- Placing the Organization into maintenance mode on the target cell (downtime begins).
- Migrating all data — including any new data created on the target cell — back to the source cell. This is the same order of complexity as the forward migration.
- Reconciling data that now exists on both cells, with potential conflicts.
- Executing another topology routing switch back to the source cell.
- Validating the rollback itself (introducing its own go/no-go gate).
- Total downtime: hours to days, depending on data volume.

By contrast, fixing forward on a 95% functional Organization means identifying and patching the specific issue in place, with the Organization remaining operational throughout. The customer impact of a targeted fix-forward is a fraction of the downtime that a full data rollback would impose.

**Data divergence makes rollback operationally intractable.** Once customers write data to the target cell — new projects, issues, merge requests, pipeline runs — that data exists only on the target cell. A data rollback must either discard this post-migration work (unacceptable for active customers) or merge it back into the source cell (technically complex and error-prone with no existing tooling).

**Geo is one-directional.** The current migration process reuses [Geo](https://docs.gitlab.com/ee/administration/geo/) to replicate data from the source cell to the target cell. Reversing this relationship would require both cells to simultaneously act as primary and secondary — a configuration that has never been built or tested, and would require significant infrastructure investment.

**Feature parity eliminates the primary rollback driver.** The principal reason a customer would want to "go back" is missing features on the target cell. By requiring feature compatibility as part of the go/no-go gate, we eliminate this driver before the topology routing switch ever happens.

**Engineering effort is better spent on forward migration quality.** The effort required to build, test, and validate a full reverse migration capability is substantial and unknown. This effort directly competes with hardening the forward migration tooling, improving go/no-go validation, and building fix-forward capabilities — all of which reduce the likelihood that rollback would ever be needed.

### Precedent: GitLab Dedicated migrations

While the Protocells migration architecture is distinct from GitLab Dedicated, the operational pattern is instructive. Across all Dedicated customer migrations to date, we have never needed to perform a data rollback. Migrations have either been aborted before the cutover (equivalent to not clearing the go/no-go gate) or issues have been fixed forward on the destination environment. This track record supports the viability of a no-rollback, gate-based approach.

## Consequences

- **The go/no-go gate must be rigorous.** Since there is no fallback after the topology routing switch, the validation criteria must be comprehensive and well-tested. Investment in checksumming, automated verification, and game days is critical.
- **Feature parity becomes a hard gate for active cohorts.** Cohorts B and C cannot be migrated until feature compatibility is confirmed. This creates a dependency between the Organizations product team and the Cells infrastructure team.
- **Fix-forward capability must be robust.** Strong observability, incident response, and patching capabilities on Protocells are required to handle post-migration issues without the option of data rollback.
- **Source data retention delays scaling benefits.** Retaining organization data on the source cell delays the database headroom benefits that motivate migration. Retention windows must be kept deliberately short for later cohorts.
- **Customer communication must be clear.** Customers opting into migration (Cohorts B/C) must understand that migration is irreversible after the topology routing switch, and that any issues will be resolved fix-forward.
- **Future Org Mover may revisit.** A future, fully-featured Org Mover capable of moving organizations between any cells in any direction could revisit this decision. However, this is not on the near-term roadmap and should not be conflated with the Protocells migration programme.

## Alternatives considered

### Option 1: Full data rollback (reverse migration)

Build a full data migration process to move an Organization's data back from the target cell to the source cell, equivalent in complexity to the forward migration.

- **Pros**: Preserves all post-migration data; provides a permanent safety net.
- **Cons**: Unknown but substantial engineering effort; delays first migration indefinitely; doubles testing and validation surface; requires bi-directional Geo or equivalent (never built); imposes significant customer downtime during the rollback itself.
- **Verdict**: Rejected. The downtime and complexity of a rollback exceed the cost of fixing forward. Engineering effort is better invested in go/no-go gate quality.

### Option 2: Post-commitment topology switchback (routing-only revert after go/no-go)

After the go/no-go gate is fully cleared and the migration is committed, revert routing back to the source cell without moving data.

- **Pros**: Fast to execute (minutes); no data migration required.
- **Cons**: Discards all production data created on the target cell after the migration is committed; the longer the org operates on the target cell, the more data is lost; does not address the root cause; creates a false sense of safety that weakens investment in fix-forward capability.
- **Verdict**: Rejected as a post-commitment mechanism. Switchback is supported only during the Stage 2 smoke test window (see above), where the data loss is limited to validation activity. After the migration is committed, we fix-forward.

### Option 3: Direct Transfer (reverse)

Use GitLab's native bulk import mechanism to migrate data back from the target cell to the source cell.

- **Pros**: Leverages existing tooling; lower effort than full reverse migration.
- **Cons**: Requires a complete data copy from scratch (not incremental), imposing significant downtime comparable to the original forward migration; mutates resource IDs (groups, projects), breaking external integrations and bookmarks; excludes certain data types (CI/CD variables, deploy tokens, webhooks); does not verify data integrity; not yet viable on Cells.
- **Verdict**: Rejected. The downtime of a full re-copy negates the benefit of reverting, and ID mutation is unacceptable for active customers.

### Option 4: Congregate (reverse)

Use Congregate (an enhanced wrapper around Direct Transfer) to migrate data back with broader data type coverage.

- **Pros**: Better data type coverage than Direct Transfer; handles CI/CD variables, webhooks, registries.
- **Cons**: Same as Direct Transfer — requires a complete data copy from scratch with comparable downtime; still mutates resource IDs; requires running a separate container with network access to both cells; some data types remain unsupported; does not verify data integrity.
- **Verdict**: Rejected for the same downtime and ID-mutation reasons as Direct Transfer.

### Option 5: Bi-directional Geo replication

Extend Geo to support bi-directional replication between source and target cells, keeping both cells in sync post-migration.

- **Pros**: Would enable seamless switchback at any time with no data loss.
- **Cons**: Geo has never supported bi-directional replication; this is a net-new capability requiring fundamental changes to a core system; significant risk of data conflicts; would require all requests and background jobs to be Cells-aware and Org Migration-aware; massive engineering investment.
- **Verdict**: Rejected. Disproportionate effort and risk for a capability that a rigorous go/no-go gate and fix-forward make unnecessary.

## Related

- [Organization Data Migration design document](/handbook/engineering/architecture/design-documents/organization-data-migration/)
- [Rollback Options issue (#581028)](https://gitlab.com/gitlab-org/gitlab/-/issues/581028)
- [Document rollback decisions in ADR (#592983)](https://gitlab.com/gitlab-org/gitlab/-/work_items/592983)
- [Org data migration end-to-end](https://docs.google.com/document/d/1XFI9uB3dRTgMON62DkH6SnUmVXcZDWsFDY2XiNzY0Ck)
- [Existing draft MR (!18887)](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/18887)
- Epic: [Organization Data Migration: Support Cohort 0 Organization move (#17308)](https://gitlab.com/groups/gitlab-org/-/work_items/17308)
