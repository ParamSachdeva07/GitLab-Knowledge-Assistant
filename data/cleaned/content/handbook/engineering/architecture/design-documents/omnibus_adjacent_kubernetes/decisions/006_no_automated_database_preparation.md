---
title: "GitLab Omnibus-Adjacent Kubernetes ADR 006: No automated database preparation for OAK components"
description: "Decision on database provisioning for OAK advanced components: Omnibus does not automatically create or configure databases for advanced components."
owning-stage: "~devops::gitlab delivery"
toc_hide: true
---

## Context

OAK advanced components (such as OpenBao) may require a PostgreSQL database to operate.
Omnibus GitLab already supports logical databases for non-Rails components through the
`postgresql['component_databases']` framework introduced in
[MR!9440](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/9440).
This framework allows operators to declare component databases in `gitlab.rb` and have
Omnibus create the required PostgreSQL roles, databases, schemas, and extensions during
`gitlab-ctl reconfigure`.

Should Omnibus automatically provision a database for an advanced component when the operator enables it via OAK settings, or should the operator configure the database explicitly? Two options exist:

1. **Option A — Automatic provisioning**: When an operator enables an OAK component that
   requires a database, Omnibus automatically creates the database objects (role, database,
   extensions) using the `postgresql['component_databases']` framework, without requiring
   the operator to add any database-specific settings to `gitlab.rb`.

1. **Option B — Explicit configuration**: The operator configures the database by adding
   the relevant entry to `postgresql['component_databases']` in `gitlab.rb` directly.
   Omnibus creates the database objects only when this entry is present and enabled.

## Decision

Omnibus does **not** automatically provision databases for OAK advanced components.
Operators must explicitly configure the database for each component that requires one
by adding an entry to `postgresql['component_databases']` in `gitlab.rb`.

## Rationale

1. **Password management complexity**: Automatic provisioning requires either auto-generating a database password (introducing a new secret-storage mechanism, rotation concerns, and migration paths) or requiring the operator to supply a password via an OAK-specific setting such as `oak['components']['<name>']['database']['password']`. The latter approach offers minimal UX benefit over direct use of `postgresql['component_databases']`, while the added indirection increases maintenance cost.
1. **Explicit intent reduces resource surprises**: When an operator enables an OAK component, they may not intend to collocate its database with the existing GitLab-managed PostgreSQL. Requiring an explicit `postgresql['component_databases']` entry forces a deliberate decision about database placement, connection limits, and resource impact — considerations that matter especially in constrained single-node deployments.
1. **Not all components are suitable for co-location**: Some advanced components could have resource or compatibility constraints that make co-location with the main PostgreSQL cluster undesirable. A single automatic rule cannot cover all cases; making automation a recommendation rather than a default avoids encoding an assumption that may not hold.
1. **Low marginal benefit**: The `postgresql['component_databases']` framework already handles the heavy lifting of database object creation. The cognitive overhead of adding a few lines to `gitlab.rb` is small, and clear documentation further reduces friction.
1. **Geo replication complexity**: Geo deployments introduce primary/secondary site roles and replication concerns — it is not safe to assume a component database should be automatically replicated, or that the component supports read-only replicas. Explicit configuration keeps the operator in control of these topology decisions.

## Consequences

1. Operators who enable an OAK advanced component that requires a database must add the corresponding entry to `postgresql['component_databases']` in `gitlab.rb`. OAK documentation must clearly describe this requirement and provide a copy-pasteable example for each component.
1. Component teams introducing a new OAK-compatible component that needs a database must document the required `postgresql['component_databases']` configuration in their component's setup guide.

## References

1. [Issue#9997 - Define design strategy for database preparation for Omnibus-Adjacent Kubernetes](https://gitlab.com/gitlab-org/omnibus-gitlab/-/work_items/9997)
1. [MR!9440 - Introduce a component database framework](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/9440)
1. [ADR-004: Multi-node Omnibus support in OAK - Data storage considerations](004_multi_node_omnibus_support.md)
