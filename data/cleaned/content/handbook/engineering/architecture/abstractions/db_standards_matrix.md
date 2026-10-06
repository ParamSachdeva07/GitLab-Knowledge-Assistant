---
title: "Database Standards Matrix"
description: "Defines the approved database technology and procurement path for each GitLab deployment scenario, extending the PostgreSQL key abstraction."
---

## The Fundamental Question

What database technology and procurement path should a given GitLab application require, under which deployment scenarios?

This document answers that question across two axes:

1. **Database technology** — PostgreSQL, ClickHouse, and a small set of justified exceptions.
2. **Procurement path** — Self-hosted ↔ N managed services ↔ 1 managed service.

It is the matrix companion to the [PostgreSQL key abstraction](postgresql.md), which establishes PostgreSQL as GitLab's approved OLTP database. This document covers the operational and procurement model around that abstraction across all deployments.

## Standardization Principle

GitLab standardizes on **Community PostgreSQL** for OLTP. The standard is not "PostgreSQL the engine" alone — it is **Community-backed PostgreSQL wrapped by a Database-as-a-Service offering operated by the GitLab Database team**.

This framing has two consequences:

1. The same logical contract — Community PostgreSQL versions, extensions, migration tooling, observability, and backup/DR patterns — applies in every deployment context.
2. The *operational shape* of that DBaaS differs by deployment, but the *product-facing interface* does not. Services target the DBaaS, not a specific cloud provider's flavor of Postgres.

Engines that present a PostgreSQL wire protocol but diverge from Community PostgreSQL — Aurora, AlloyDB, Yugabyte, CockroachDB, EDB Postgres Distributed — are **non-standard**. They require an explicit, documented exception with a clear and durable justification; a requirement the standard cannot meet. The reasoning is captured in the [PostgreSQL key abstraction](postgresql.md): a single, community-backed engine keeps migration tooling, runbooks, and team expertise unified across products and the most broad set of deployment options.

### What the DB team ships in each deployment

| Deployment | Cloud | DBaaS shipped and supported by the DB team |
| ---------- | ----- | ------------------------------------------ |
| GitLab.com | GCP | GitLab Postgres stack (Patroni + PgBouncer + Consul) today. Cloud SQL under active evaluation — see benchmarking program below. |
| Dedicated | AWS | Amazon RDS (Multi-AZ), wrapped with the DB team's tooling, runbooks, and migration layer. |
| Self-Managed — Enterprise reference | Customer | **GitLab Postgres stack** — full Patroni + PgBouncer reference deployment, packaged and supported. |
| Self-Managed — Omnibus | Customer | Bundled PostgreSQL, with optional Patroni/PgBouncer for HA deployments. |

Products do not pick a database; products pick the DBaaS, and the DB team is responsible for the engine, the operational stack around it, and the migration path between providers.

A roadmap item for the DBaaS is **cross-cloud logical replication on Community PostgreSQL as a managed feature** — bidirectional or follower-style replication between GCP and AWS regions, operated by the DB team rather than by each consuming product. The intent is to close the gap that today justifies non-standard engines for global-distribution use cases, so the standard DBaaS contract eventually covers cross-cloud read fan-out without requiring an exception.

## The Matrix

|                          | **GitLab.com (GCP)**             |                                   | **Dedicated (AWS)**     | **Self-Managed**         |                  |
| ------------------------ | -------------------------------- | --------------------------------- | ----------------------- | ------------------------ | ---------------- |
| **Environment→**                | Dev / Stage                      | Load / Prod                       | All envs                | Enterprise               | Omnibus          |
| **PG-OLTP applications** | Cloud SQL or GitLab PG stack     | GitLab PG stack (→ Cloud SQL TBD) | RDS                     | GitLab PG stack          | Bundled PG       |
| **Analytics & events**   | GL ClickHouse                    | ClickHouse Cloud                  | ClickHouse Cloud → GL   | BYO ClickHouse           | CH-OAK appliance |
| *Exceptions*             |                                  |                                   |                         |                          |                  |
| **GLAZ (GATE)**          | Cloud SQL / Yugabyte             | Yugabyte (Aeon SaaS)              | RDS                     | GitLab PG stack          | Bundled PG       |
| **Protocells**           | Cloud SQL                        | Spanner (topology only)           | RDS                     | n/a                      | n/a              |

**PG-OLTP applications** include: the GitLab Rails monolith (Main, CI, Sec clusters), Container Registry, Artifact Registry, and future transaction-centric services.

## Benchmarking Program — Next Six Months

The matrix above commits today's defaults, but the long-term question is whether the GitLab Postgres stack remains the right default on .com at Cells scale, or whether a system-managed Postgres (Cloud SQL, AlloyDB) is cheaper, faster, and easier to operate.

The DB team is running a **standardized benchmarking program** that produces apples-to-apples comparisons across the providers we already use or might adopt: GitLab Postgres stack on VMs, RDS, Cloud SQL, AlloyDB, and Yugabyte (for cross-reference against the GATE workload). The goal is to retire the "we think" answers and replace them with measured ones.

Metrics in scope:

- **Cost to serve** — infrastructure $ per workload at a fixed performance envelope.
- **Cost to support** — ops and people cost (incident load, on-call burden, runbook churn, provisioning time) per cluster and per cell.
- **Cost per transaction** — normalized $/tx and latency at p50/p95/p99 for a representative GitLab workload.
- **Cells fit** — provisioning time, blast radius, per-cell COGS, and self-serve readiness.

The headline question: **can a system-managed PostgreSQL be cheaper, faster, and easier to operate than the GitLab Postgres stack at Cells scale?** If yes, it becomes the default for new modular services on .com. If no, the GitLab Postgres stack remains the default and we invest further in its self-serve provisioning. The choice will be made on the metrics — not on preference.

## Exceptions

### GLAZ — Yugabyte for GATE

GATE (Auth / Identity) has a requirement for **low-latency replication across cloud providers** — sub-second bounded staleness for L1 reads spanning GCP and AWS. No Community-PostgreSQL-backed offering meets that requirement today. We deploy Yugabyte (Aeon SaaS) for GATE's L0 control plane and L1 regional read replicas.

Scope and guardrails for this exception:

- **One service, one exception.** Yugabyte is approved for GATE only.
- **Standard PG surface area.** GATE code stays on standard `pgx`/Rails patterns and standard PG DDL/DML, so migration off Yugabyte remains feasible.
- **L2 (cell-local) stays on Community PG.** Only L0 and L1 are on Yugabyte; cell-local auth data continues to use the standard DBaaS.
- **Data ownership safety net.** Logical replication from L0 Yugabyte to a GitLab-managed Community PG instance ensures GitLab owns the data even while consuming managed Aeon.

### Protocells

Protocells use Cloud SQL for application data, with Spanner used **for topology metadata only** — not for application OLTP. As Cells matures, the topology service is re-evaluated against the benchmarking program above; the goal is to converge on the standard wherever possible.

## Related Documents

- [PostgreSQL key abstraction](postgresql.md) — the base OLTP standard this matrix extends
- [Key Abstractions index](_index.md)
