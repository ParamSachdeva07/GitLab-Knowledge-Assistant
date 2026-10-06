---
title: "Build Infrastructure"
---

GitLab's release artifact build pipeline uses mirrored repositories, each with a distinct role.
The current state of which services build where is documented here and updated as services migrate.

For the decision rationale behind this architecture, see [ADR 001: Build Mirror Separation](decisions/001_build_mirror_separation.md).

## Repository Mirrors

| Mirror | Location | Purpose |
|--------|----------|---------|
| Canonical | GitLab.com | Public development, merge request workflows, canonical source of truth |
| Security | GitLab.com | Private mirror for pre-disclosure security fixes; source for building and publishing release artifacts for new modular services |
| Build | dev.gitlab.org | Private mirror for building and publishing release artifacts for legacy processes |

## New components: Security mirror

New modular services build and publish release artifacts from the Security mirror on GitLab.com.

GitLab CI runners execute on compute that is separate from GitLab.com application servers.
This dedicated runner fleet, combined with the Security mirror's restricted access model, satisfies the logical separation between build infrastructure and production environments required by SOC 2, FedRAMP, and SLSA L2+.

The Security mirror's activity is independently auditable and its access is scoped separately from the Canonical project's maintainer pool.

## Existing processes: dev.gitlab.org

Legacy tooling and processes continue to run builds through [dev.gitlab.org](https://dev.gitlab.org), a separate GitLab instance.
As the build system evolves - particularly as GitLab moves toward a more modular release architecture - these processes will naturally migrate away from the separate instance.
This is a gradual transition rather than a discrete migration effort.

For operational details on dev.gitlab.org and the build machines, see the [Build team maintenance documentation](build/maintenance/).
