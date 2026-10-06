---
title: "GitLab Release Manifest"
description: "GitLab Release Manifest provides structured data about the versions of modular components of GitLab that are compatible with a given overarching GitLab version"
status: ongoing
creation-date: "2026-08-07"
owning-stage: "~devops::gitlab delivery"
authors: ["@siddharthkannan", "@rpereira2", "@jennykim-gitlab" ]
dris: ["@skarbek"]
coaches: ["@nolith", "@skarbek"]
toc_hide: false
---

## Summary

The GitLab Release Manifest provides structured data about the versions of modular components of GitLab that are compatible with a given overarching GitLab version. This information is intended to be used by internal and external installation tools that aim to provide GitLab environments containing modular components, such as [GitLab Orbit](/handbook/engineering/architecture/design-documents/orbit/) and [Artifact Registry](/handbook/engineering/architecture/design-documents/artifact_registry/). The release manifest is built with a particular focus on simplifying the initial installation of GitLab (with modular components) and the experience of upgrading GitLab automatically.

## Goals, Non-Goals, and Assumptions

### Goals

1. Communicate the versions of modular components which are compatible with a GitLab version
1. Ensure that the modular component release cycle is not tied to GitLab's current release schedule
1. Allow users to upgrade a single modular component while keeping most of their GitLab installation unchanged
1. Release manifest should be structured and machine readable
1. Release manifest should be immutable once a GitLab version has been published

### Non-Goals

1. Replace [Managed versioning](https://gitlab-org.gitlab.io/release/docs/components/managed-versioning/#components-under-managed-versioning)
1. Replace `*_VERSION` files in the GitLab Rails codebase (such as [GITLAB_KAS_VERSION](https://gitlab.com/gitlab-org/gitlab/-/blob/master/GITLAB_KAS_VERSION?ref_type=heads), [GITALY_SERVER_VERSION](https://gitlab.com/gitlab-org/gitlab/-/blob/master/GITALY_SERVER_VERSION?ref_type=heads), etc.)
1. Build or bundle the binaries, docker images, Helm charts for modular components into the existing GitLab Helm chart, CNG images, or Omnibus package

### Assumptions

1. Modular components follow semantic versioning and produce semantic releases using the [Release Framework](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/release-platform/)
1. Modular components build their own build artifacts such as binaries, container images, Helm charts, etc.
1. Modular components tag and publish releases at their own pace

## Present State

Each GitLab version consists of many components apart from the Rails codebase. The commonly used method to store the versions of these components is to add a **`*_VERSION` file in the Rails codebase.** This method is currently used for Gitaly, KAS, Pages, Shell, Zoekt, OpenBao, among others.

This version file is updated using various methods: The file is updated manually for [OpenBao](https://gitlab.com/gitlab-org/gitlab/-/commits/master/GITLAB_OPENBAO_VERSION?ref_type=heads), using Renovate Bot for [Zoekt](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/239781), and using [release tooling](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/245784) for components under [Managed Versioning](https://gitlab-org.gitlab.io/release/docs/components/managed-versioning/#components-under-managed-versioning) (Gitaly and KAS).

We expect the rapid addition of 10s of new modular components, which will be built and released from their own repository using the [Release Framework](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/release-platform/). In this scenario, it will no longer be practical to introduce and maintain a `*_VERSION` file in the Rails codebase for each new modular component. Release manifest proposes the simplification of version management by building on the standardization provided by the [Release Framework](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/release-platform/).

## Proposed Solution

The release manifest will **take a snapshot of the compatible versions for each modular component** whenever a GitLab release is published, and store this in a machine-readable format for other tools to consume. It will provide a mapping from a given GitLab version to compatible versions for all modular components that work with that version of GitLab.

``` mermaid
flowchart LR
    MCR[Modular Component - Release published] -->|Component entry updated in the Mutable catalog| RMMut[(Mutable Catalog)]

    GRS[GitLab Release Schedule] -->|GitLab monthly or weekly scheduled release published| GRP[GitLab Release Published]

    GRP ==> |Release manifest frozen for the current milestone| RMMut
    GRP ==> |Release manifest initialized for the next milestone| RMMut

    subgraph RM[Release Manifest]
        direction TD
        RMMut

        RMMut ==>|Release manifest frozen for the current milestone| RMImmut[(Immutable Record)]

        RMImmut
    end

    linkStyle 2 stroke:red
    linkStyle 3 stroke:blue
    linkStyle 4 stroke:red
```

It will contain two pieces:

1. **Mutable Catalog** of compatible versions for the future GitLab releases: This catalog will be updated automatically using CI jobs inside [Release Framework](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/release-platform/), requiring no intervention from the teams developing the modular component. Release framework requires components to follow semantic versioning, so all release framework components will be included in the Mutable catalog by default.
1. **Immutable Record** of compatible versions for past GitLab releases: When a GitLab release is published to users, the catalog entry for that release will be copied to an immutable store. This will serve as a reference for all tooling that intends to install this version at any point in time.

## Data Model

{{% alert %}}
The data model below is published as a [JSON Schema](https://gitlab.com/gitlab-org/release/manifests/schema/-/blob/main/json-schemas/release-manifest.schema.json). Both manifest projects validate every file against it in CI. See [Storage](#storage) for the projects.
{{% /alert %}}

### Mutable Catalog

The release manifest entry for [`artifact-registry`](https://gitlab.com/gitlab-com/gl-infra/infra-mgmt/-/blob/f3439969fdf44ddc0d76fcd197a9c5787897e379/data/projects/release-platform/repos.yaml#L137) for the upcoming GitLab release 19.5.0 will live inside the file `19/5/0/artifact-registry.json`. The string `artifact-registry` is the module's ID within the [Release Framework](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/release-platform/); we use that as an identifier in the release manifest.

The entry's content will be in this format:

``` json
{
  "version": "1.275.1",
  "sha": "6cdaf83c809b7d02c794d5db2dea9e101c662ac7",
  "ref": "v1.275.1",
  "source": {
    "url": "https://gitlab.com/gitlab-org/ops/artifact-registry"
  }
}
```

Similarly, the entry for [`knowledge-graph`](https://gitlab.com/gitlab-com/gl-infra/infra-mgmt/-/blob/f3439969fdf44ddc0d76fcd197a9c5787897e379/data/projects/release-platform/repos.yaml#L213) (GitLab Orbit) will be in the file `19/5/0/knowledge-graph.json` and have this content:

``` json
{
  "version": "0.95.3",
  "sha": "51aab3662a8764f47616acefdff8163312bd2bc6",
  "ref": "v0.95.3",
  "source": {
    "url": "https://gitlab.com/gitlab-org/orbit/knowledge-graph"
  }
}
```

Such entries will exist for all [components](https://gitlab.com/gitlab-com/gl-infra/infra-mgmt/-/blob/main/data/projects/release-platform/repos.yaml) which are being managed using the [Release Framework](https://internal.gitlab.com/handbook/engineering/architecture/design-documents/release-platform/).

The mutable catalog will be updated only **once** a version of the modular component is published to users. This allows the modular component team to control when their component version will be included in the overarching GitLab version.

### Immutable Record

Once the release 19.5.0 is published to users, we will combine the version information for multiple components into a single file `19/5/0.json`. This file's content will follow this format:

``` json
{
  "version": "19.5.0",
  "modules": {
    "artifact-registry": {
      "version": "1.275.1",
      "sha": "6cdaf83c809b7d02c794d5db2dea9e101c662ac7",
      "ref": "v1.275.1",
      "source": {
        "url": "https://gitlab.com/gitlab-org/ops/artifact-registry"
      }
    },
    "knowledge-graph": {
      "version": "0.95.3",
      "sha": "51aab3662a8764f47616acefdff8163312bd2bc6",
      "ref": "v0.95.3",
      "source": {
        "url": "https://gitlab.com/gitlab-org/orbit/knowledge-graph"
      }
    }
  }
}

```

## Storage

The release manifest lives in three dedicated projects under `gitlab-org/release/manifests`. Module authors and consumers start here.

| Project | Contents | Visibility |
| --- | --- | --- |
| [`manifests/unreleased`](https://gitlab.com/gitlab-org/release/manifests/unreleased) | Mutable catalog. One file per component, at `{major}/{minor}/{patch}/{module-id}.json` | Private. Internal consumers ask the Delivery: Release and Deploy team for a group share with the Reporter role |
| [`manifests/released`](https://gitlab.com/gitlab-org/release/manifests/released) | Immutable record. One file per published GitLab release, at `{major}/{minor}/{patch}.json` | Public |
| [`manifests/schema`](https://gitlab.com/gitlab-org/release/manifests/schema) | The [JSON Schema](https://gitlab.com/gitlab-org/release/manifests/schema/-/blob/main/json-schemas/release-manifest.schema.json) that both tiers validate against | Public |

Nobody pushes to `main` in either data project directly: the push allow-list on `main` holds only the release automation bots. A human change has to go through a merge request, where the CI checks gate it. Both projects validate every file against the schema. The record project also fails any merge request that changes a record file which already exists, enforcing the "immutable once published" goal (see [Goals](#goals)) by mechanism rather than by convention. A deliberate corrective change is still possible: it needs the `record-change-approved` label, and the job then passes and posts an audit comment naming the changed files.

### How Entries Are Written

Two separate events write to the release manifest, and each one writes to a different project.

**A module publishes a version.** [release-tools](https://gitlab.com/gitlab-org/release-tools) adds that module's entry to the [mutable catalog](https://gitlab.com/gitlab-org/release/manifests/unreleased), for each GitLab version that is still upcoming. The write does not wait for a GitLab release, and it does not touch any other module. This keeps the module release cycle independent of the GitLab release schedule (see [Goals](#goals)).

**A GitLab version publishes.** release-tools freezes the catalog entries for that version into one file in the [immutable record](https://gitlab.com/gitlab-org/release/manifests/released), then carries the same entries forward into the catalog for the next versions. The frozen file is the answer for that GitLab version from then on, and it never changes.

Carrying entries forward keeps the last published version of a module in the catalog until the module publishes again. A module that releases rarely still appears in later records, and a module that publishes during the cycle replaces the entry.

## Related Documents

1. [GitLab R&D Summit 2026 - Release Manifest Demo (GitLab Delivery) - Google Slides](https://docs.google.com/presentation/d/1jLXML2-2vIdtJ9TflasVgZtaoAs02WFS4M5oQ8c9dg4/edit?slide=id.g12b319f6181_0_0#slide=id.g12b319f6181_0_0)
1. Repositories and content used during the demo, replaced by the production projects in [Storage](#storage)
   1. [Mutable catalog](https://gitlab.com/gitlab-org/release/demo-release-manifests/unreleased/-/blob/main/19/0/5/gitaly.json)
   1. [Immutable record](https://gitlab.com/gitlab-org/release/demo-release-manifests/released/-/blob/main/releases/19/1/1.json)
1. [Implementation details and component changes](https://gitlab.com/groups/gitlab-com/gl-infra/software-delivery/-/work_items/39#note_3587819537)
