---
title: "Theseus ADR 004: Independent per-component deploys for GitLab.com; bundled releases for Self-Managed"
owning-stage: ""
description: "Decision that GitLab.com SAAS migrates incrementally to independent per-component deploys via the Release Framework, while Self-Managed retains bundled monthly meta-packages by design."
toc_hide: true
---

<!-- Design Documents often contain forward-looking statements -->
<!-- vale gitlab.FutureTense = NO -->

## Status

**Proposed.**

## Context

GitLab.com today ships a single meta-package
containing changes from many components.
The SREs operating GitLab.com want the opposite shape:
independent rollback,
per-component cadence,
small blast radius per change.

Self-Managed customers operate their own GitLab installations,
on their own schedule,
with their own change-management processes.
A bundled monthly release is what they ask for:
one upgrade, one version, one set of release notes.
N component versions to track is not a feature — it's a burden.

The [Release Framework](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/release-platform/) aims to make both models possible.

## Decision

**GitLab.com SAAS** migrates to independent per-component deploys via the Release Framework.
The migration is incremental:
components onboard one at a time,
starting with Artifact Registry,
ending with the Rails monolith.
Until the monolith onboards,
GitLab.com retains the train-style cadence as the fallback for everything else.

**GitLab Cells** follows the same release model as GitLab.com SAAS —
independent per-component deploys via the Release Framework —
but the deployment mechanism is Instrumentor.

**Self-Managed** retains bundled monthly meta-packages.
Components are pinned to a release version
and ship together indefinitely.

**GitLab Dedicated** is a special case:
deployments use the newer rollout architecture
(potentially [Argo Rollouts](https://argoproj.github.io/rollouts/))
but the updates are bundled during the maintenance window.

## Consequences

### Positive

1. GitLab.com gains independent rollback.
1. Self-Managed keeps operational simplicity.

### Negative

1. **Two release models maintained in parallel, indefinitely.**
   Tooling, docs, release notes, and CI all carry the dual shape.
1. **Components must work in both shapes.**
   A component shipping independently on GitLab.com
   must also ship as part of the bundle on Self-Managed,
   with version compatibility maintained across both.

## References

- [Section 7.3 — The GitLab.com meta-package transition](../#73-open-tensions) —
  the tension this ADR resolves.
- [Release Framework design doc](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/release-platform/) —
  the mechanism enabling per-component deploys on GitLab.com.
- [Section 5.5 — Deployment: Fairway and the Release Framework](../#55-deployment--fairway-and-the-release-framework) —
  the platform integration point.
- [Argo Rollouts](https://argoproj.github.io/rollouts/) —
  the candidate rollout machinery for GitLab Dedicated's bundled-but-modern path.
