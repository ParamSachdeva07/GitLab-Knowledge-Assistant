---
title: 'Organization Data Migration ADR 003: Org Mover Control Plane'
description: 'Org Mover is a Runway-deployed control plane that orchestrates moves of GitLab.com organizations between Cells.'
status: proposed
creation-date: "2026-06-09"
authors: [ "@mkozono" ]
coaches: [ "@ayufan" ]
dris: [ "@mkozono" ]
owning-stage: "~devops::tenant scale"
participating-stages: ["~devops::tenant scale", "~devops::data stores", "~devops::systems"]
toc_hide: true
---

## Summary

**Org Mover** is a [Runway](https://docs.runway.gitlab.com/)-deployed control plane service that orchestrates
moves of GitLab.com organizations between Cells.

| | |
|---|---|
| **Problem** | No automation exists to migrate an organization from the legacy cell to a target cell. |
| **Approach** | Build Org Mover as a Runway-deployed control plane that any engineer can use to run each move as an ordered sequence of steps. Org Mover coordinates the systems that move data; it does not move data itself. The Org Mover exposes a REST API. |
| **Status** | Proposed |
| **Scope** | GitLab.com SaaS only: legacy cell to target cell. See [Scope](#scope) and [Non-goals](#non-goals). |
| **Decision needed** | Approval of the control-plane shape, scope, and non-goals from Tenant Scale, Geo, Siphon, and Infrastructure stakeholders. |
| **See also** | [ADR-002 rollback](002_rollback_strategy.md) · [ADR-010 Organization Maintenance Mode](../../organization/decisions/010_organization_maintenance_mode.md) · [Org data migration blueprint](../_index.md) |

### Why do we need to move organizations across Cells?

GitLab.com runs as a single monolithic deployment that is hitting hard scaling
ceilings, the database first.
[Cells](../../cells/)
address this by spreading [organizations](../../organization/) across independent, horizontally
scalable instances.

### Why this is hard

We cannot just take an organization offline and move it, for two reasons:

1. We must be capable of moving large organizations
2. We must do it with minimal customer impact.

#### Customer size

Many small organizations have little enough data that it could be transferred in
minutes, and many are inactive at night or on weekends. We could move those
organizations by relatively simple means, and with relatively simple
orchestration.

However, large organizations account for [a large proportion of database load (internal link)](https://gitlab.com/gitlab-com/gl-infra/tenant-scale/staff/lstaff/-/work_items/3), so fully relieving the legacy cell eventually requires moving them, not just small organizations.
They also account for [a large proportion of data volume (internal link)](https://gitlab.com/gitlab-com/gl-infra/tenant-scale/tenant-services/team/-/work_items/417).

#### Downtime

Relieving the legacy cell does not require emptying it, but it does require
moving a substantial fraction of its load and data, enough to restore
meaningful headroom rather than a marginal trim. And the cell keeps growing,
with that growth accelerating, so relief has to be sustained rather than a
one-time push. Meeting that target means running many moves continuously and in
parallel. Gating the migration rate on customers' off-hours windows would mean
it could not keep pace.

The largest organizations rule out downtime windows entirely. They span every
timezone, so they have no off-hours to schedule a read-only period in. Their
cost of lost development time scales with their user count, so a day of
disruption runs to millions of dollars. Scaling GitLab.com is GitLab's
responsibility, not the customer's, so we cannot push that cost onto them.

So we must minimize organization downtime, regardless of organization size. Yet
organizations hold too much data to transfer inside any acceptable read-only
window. This forces the central requirement for moving organizations: the bulk
of the data must already be on the target before the read-only window opens, so
that the window drains only a small delta rather than transferring everything.

## Decisions

We will build Org Mover as a Runway-deployed control plane service that orchestrates organization moves between GitLab.com Cells.

1. **The Org Mover service is a control plane.** It runs each move as an ordered
   sequence of steps, checks conditions before each transition, maintains state
   about all moves, exposes real-time status, and records an audit trail.
2. **Deployment model: a long-lived RunwayService.** Org Mover is a long-lived
   [RunwayService](https://docs.runway.gitlab.com/welcome/introduction/) backed
   by a persistent state database. It should avoid RunwayJobs; instead it
   should delegate heavy work to subsystems.
3. **A move runs as a sequence of saved steps.** Each move goes through ordered
   steps such as pre-flight checks, data replication, a final sync, and the
   routing switch. Org Mover saves progress after each step, so a move that is
   interrupted resumes where it left off instead of starting over.
4. **Never switch routing to incomplete data.** Org Mover does not send an
   organization's traffic to the target cell until it has checked that the
   target's data is complete and matches the source, using checksums, row
   counts, and spot checks. Routine replication failures along the way are
   expected and retried; they do not stop the move. Switching without that check
   would risk losing customer data.
5. **A person makes the go/no-go call, at first.** Cutover is the moment Org
   Mover sends an organization's traffic from the old cell to the new one, the
   point where the move goes live. Before cutover, an engineer reviews
   replication and verification status and authorizes the switch. As the
   metrics and our confidence grow, this decision can be automated.
6. **Pre-replicate each organization's data before the downtime window.** The
   bulk of an organization's data, across every data store, is replicated to the
   target while the source stays writable, leaving only a small delta to drain
   during a short read-only window.
7. **PostgreSQL replication is delegated to Siphon.** Org Mover configures
   the streams and starts replication; Siphon takes the initial snapshot and
   then streams CDC on its own. Org Mover watches lag, waits for every table to
   catch up, and drops replication slots on completion or abort.
8. **Non-PG replication reuses Geo as the baseline.** This includes Git
   repositories, object storage, container registry, and Secrets Manager. Org
   Mover configures both cells as needed to reuse Geo for replication. In the
   future, Geo may be replaced, in whole or part. The control-plane contract is
   identical regardless.
9. **Routing is delegated to the Topology Service.** Org Mover invokes the
   cutover through the Topology Service's two-phase claim update and verifies
   the route; the Topology Service is the routing authority.
10. **Rollback follows ADR-002.** There is no data rollback after cutover. The
    strategy relies on a pre-cutover go/no-go gate, the short
    [ADR-002](002_rollback_strategy.md) Stage 2 switchback window, and then
    fix-forward.
11. **One control plane orchestrates many concurrent moves.** A single Org
    Mover deployment runs many moves at once, each with its own saved state,
    and provides visibility and control across all of them. It is
    not one service per move.

### Alternatives considered

#### Dual-write

Instead of replicating data after it is committed to the source cell, the
application could write every change to both the source and target during a
transition, then cut over once the target is caught up. Dual-write would require
write-path changes across every data store an organization uses: PostgreSQL, Git
repositories, object storage, the container registry, and Secrets Manager. That
is a large, invasive change to the monolith for each store. In conjunction with
the urgency of Cells, we reject it for now.

#### Direct Transfer

Use GitLab's
[migration by direct transfer](https://docs.gitlab.com/user/group/import/)
to move an organization's groups and projects over the API. Rejected: it is a
slow, logical API-level migration with known coverage gaps. It rewrites record
IDs, which breaks references and rules it out on its own. It also offers no
pre-replicate path, so the whole transfer must happen inside the read-only
window, exactly what large organizations rule out.

#### File-based group and project export/import

Export each group and project to a file, then import the files on the target
cell. Rejected for the same reasons as Direct Transfer, and then some: it is the
older, file-based path with the same ID rewriting and coverage gaps, and it adds
an export, upload, and import round trip. Like Direct Transfer, it has no
pre-replicate path, so the whole transfer happens inside the read-only window.

#### Copy the whole cell, then clean up the destination after cutover

Replicate the entire legacy cell, cut over the moved organization, then delete
everything else. A more formal version of this,
[splitting a large cell](../../cells/impacted_features/data-migration/), clones
the cell into many replicas using whole-system physical replication (Geo,
PostgreSQL physical replication) and promotes each replica as authoritative for
the organizations it keeps. Rejected: either form still requires org-scoping,
now as a risky mass-delete on a live cell. It amplifies storage with full copies
that are immediately discarded, and it puts other tenants' data on a cell that
is not theirs.

#### Orchestrate from within the monolith

Build the orchestration as a Rails feature and Sidekiq jobs inside the monolith
instead of a standalone control-plane service. Rejected: the orchestrator would
live inside the cells it operates on, including the legacy cell it is meant to
relieve and eventually retire, and it would share those cells' deploys, scaling,
and failure domains. A standalone service keeps its own state database, runs
cluster-wide across all cells, and survives any single cell going read-only or
away. A cell-local control plane that the standalone service delegates to is a
[future direction](#boundary-contracts), not a replacement for it.

## Scope

This ADR targets the **GitLab.com SaaS** use case specifically: moving
organizations between GitLab.com Cells, **legacy cell to target cell**. The
design intentionally keeps broader use cases in view (see
[Non-goals](#non-goals)), but nothing beyond the GitLab.com legacy-to-target
case is promised here. Specifics Org Mover must handle:

- The legacy cell has multiple physical PostgreSQL databases, while the target
  cell uses one physical PostgreSQL with multiple logical databases.
- Legacy cell deployment infrastructure is custom; target cells use standardized
 cell deployment. Org Mover itself uses standardized Runway deployment,
  which is not yet available on self-managed. Org Mover's source-cell
  interactions reflect the legacy infrastructure.
- The legacy cell has many more Gitaly storages than the target cell. Org Mover
  must translate between them.

## Non-goals

These use cases are out of scope. Each may be revisited later:

- **Self-managed and GitLab Dedicated migration orchestration.** Org Mover
  targets GitLab.com Cells.
- **Cross-platform migration (self-managed to SaaS or vice versa).**
- **Any-cell to any-cell.** A future direction, not delivered by this design;
  a follow-on workstream once GitLab.com legacy-to-target is operational.
- **Migrating derived datastores (ClickHouse, Elasticsearch).** These are
  rebuilt on the target cell post-migration rather than replicated. For
  ClickHouse specifically, the existing
  [PostgreSQL-to-ClickHouse Siphon pipeline](https://docs.gitlab.com/development/database/clickhouse/clickhouse_table_design_with_siphon/#working-in-cells-environment)
  in the target cell handles this automatically.

## Engineering principles

These principles guide every implementation choice and review. They are
data-plane-independent: they hold whichever data-plane architecture the team
chooses. A change that violates one needs an explicit, recorded
justification.

1. **The Org Mover service is a control plane; data does not transit it.** Org
   Mover issues commands, reads progress, and decides. The systems it
   coordinates move the bytes.
2. **Make each step safe to retry.** A step that is interrupted or re-run
   should reach the same result, not double-apply or corrupt data. Prefer
   operations that can repeat safely, such as upserts over inserts and
   resume-from-checkpoint over restart-from-zero.
3. **Pre-replicate everything expensive before read-only.** Move bulk data while
   the source is writable, then drain only a small delta during the read-only
   window.
4. **Keep components orthogonal.** Org Mover coordinates each subsystem through
   a small, fixed contract: issue commands, read progress, verify, gate. Where a
   subsystem's semantics must leak through to gate correctly, make the coupling
   explicit in the contract rather than hiding it.

## Boundary contracts

Org Mover coordinates several systems. The high-level contracts are as follows:

Responsible for the following, per move and across the fleet:

- Providing interfaces for engineers to manage moves (likely a Slack bot and
  API first). Built for multiple operators to drive a move, hand off, and check
  status
- Tracking move state
- Pre-validating move transitions, such as checking for deploy freeze or active
  batched background migrations
- Verifying the target's data matches the source before cutover, using
  checksums, row counts, and spot checks across both source and target
- Toggling Organization Maintenance Mode
- Configuring and managing Siphon
- Configuring and managing Geo
- Tracking operator actions in Org Mover for auditing
- Coordinating pause, resume, abort
- When a
  [cell-local control plane (internal link)](https://gitlab.com/gitlab-com/gl-infra/delivery/-/work_items/22133)
  exists, Org Mover will interact with a cell (such as setting up the Siphon
  publisher and receiver) through it, rather than interacting directly with the
  cell's monolith API, services, or data stores

### Siphon (PostgreSQL replication)

[Siphon](https://gitlab.com/gitlab-com/gl-infra/tenant-scale/tenant-services/team/-/work_items/416#note_3339776621)
was chosen over [AWS DMS](../dms-blueprint.md), the original Cohort 0 plan.
DMS
[could not replicate PostgreSQL partitioned tables in an org-move context](https://gitlab.com/gitlab-com/gl-infra/tenant-scale/tenant-services/team/-/work_items/419).
Its only documented workaround for partitioned tables is to truncate the target
before loading, which is impossible when the target cell already holds other
organizations' data. Worse, `partition_id` values are local to each cell, so
leaf partitions need a translation step that DMS, a closed AWS service, does not
provide. Because Siphon is GitLab-owned, we can extend it to do that
translation.

Responsible for:

- PostgreSQL change data capture: the initial snapshot and CDC streaming
- Creating the replication slot on boot (Org Mover drops it)

Constraints the control plane must account for:

- Target schema must be backward compatible with the source schema during
  PostgreSQL replication
- Siphon creates the replication slot on boot but does not drop it. Org Mover
  must drop it, because an unconsumed slot fills the source primary disk
- Siphon keeps streaming until it is told to stop. Org Mover must stop Siphon at
  cutover

### Geo (Non-PG data replication)

Responsible for:

- Copying or replicating Git repositories, object storage, container registry,
  and Secrets Manager data to the target cell
- Verifying replication of non-PG data

Constraints the control plane must account for:

- Asynchronous replication never reaches 100% for an active org

### Monolith (application and org state)

Responsible for:

- Application maintenance mode (correctness is app-owned, see [ADR-010 Organization Maintenance Mode](../../organization/decisions/010_organization_maintenance_mode.md))
- Target-cell mode
- Schema and DDL

### Topology Service (routing)

Responsible for:

- Routing, as the routing authority
- The two-phase claim update Org Mover invokes for cutover, the point of no return

## References

- [ADR-002: Rollback strategy](002_rollback_strategy.md)
- [Organization Maintenance Mode (ADR-010)](../../organization/decisions/010_organization_maintenance_mode.md)
- [Organization data migration blueprint](../_index.md)
- [`gitlab-org/cells/org-mover` repository](https://gitlab.com/gitlab-org/cells/org-mover)
- [Topology Service](../../cells/topology_service.md)
- [Runway](https://docs.runway.gitlab.com/)
