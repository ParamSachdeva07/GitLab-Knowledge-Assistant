---
title: "Work Item REST API"
description: "Design document for the Work Item REST API, a resource-oriented interface that aligns with GitLab REST conventions."
status: ongoing
creation-date: "2026-02-05"
authors: ["@nicolasdular", "@mdangelo6", "@msaleiko", "@daniyalAD", "@brytannia"]
coaches: ["ntepluhina", "@engwan"]
dris: []
owning-stage: "~devops::plan"
toc_hide: true
---

{{< engineering/design-document-header >}}

## Summary

The Work Item REST API extends the Work Items architecture with a first-class, resource-oriented interface that aligns with the broader GitLab REST conventions. It enables third-party integrations, automations, and CLI tooling to access Work Items without adopting GraphQL while maintaining a single Work Item domain model that powers issues, incidents, tasks, epics, and future types. This document proposes the foundational design for the REST surface, its evolution model, and the supporting backend components required to reach feature parity with the GraphQL API iteratively.

## Motivation

Work Items have become our preferred framework for representing planning entities across GitLab. The existing GraphQL endpoint offers breadth, but many users rely on or prefer a REST API. Establishing a documented and stable REST interface will unlock Work Item adoption, simplify migrations from legacy issue APIs, and reduce duplication of business logic between the existing REST APIs and the GraphQL API.

### Goals

- Provide a versioned REST surface for Work Items that aligns with existing GitLab REST patterns and authentication flows.
- Design for feature parity between the REST and GraphQL APIs.
- Provide flexibility when shaping responses to maximize client efficiency.
- Aim for parity in parameters and responses so switching between the GraphQL and REST APIs is straightforward.
- Deliver an excellent developer experience for our users and for us internally when we want to switch endpoints from GraphQL to REST.

### Non-Goals

- Replacing the Work Items GraphQL API.

## Proposal

We expose the Work Item REST API under the following endpoints:

1. `/namespaces/:full_path/-/work_items`.
    Notably, we only support `full_path` because the ID would need to be a `Namespace` ID, and we do not expose Namespace IDs of projects transparently in our APIs. This is a trade-off between developer experience and capabilities. I expect that this endpoint will be used mostly internally.
2. `/projects/:id_or_full_path/-/work_items` and `/groups/:id_or_full_path/-/work_items`
    For an easy migration from the existing issues endpoints, we also introduce endpoints for `/groups` and `/projects`. In this case, we allow the IDs as well, as we share the ID of a Group or Project in our APIs.

### Listing and returning single Work Items

#### Filtering and pagination

For filtering, we can either:

1. Generate the filter params from the GraphQL definitions, so new filters stay in sync automatically (see [POC](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/221749/diffs#diff-content-99fa4134f164348eb12207e36f4f325203311e1c))
    The advantage is to have it generated automatically. The disadvantage is that GraphQL is the source of truth of the REST API, and we have a different deprecation policy for GraphQL APIs.
2. Add tests to ensure that the filters are the same on both the GraphQL and the REST API
    The advantag is to ensure this in tests, but we still need to add them manually.

Regardless of what we use, we want parity by design and never ship updates to either the REST or GraphQL exclusively.

Pagination is keyset-based on every endpoint. The mechanics are in the [endpoint reference](endpoints.md#pagination).

#### Flexible response

We retain some of the GraphQL flexibility by adapting some of the JSON:API concept of [sparse fieldsets](https://jsonapi.org/format/#fetching-sparse-fieldsets).

1. Only `id`, `global_id`, `iid`, and `title` are always returned. Other fields need to be requested explicitly.
2. By default, no feature or widget is added as part of the response.
3. Other top-level fields must be requested specifically via a `fields` param.
4. For the features/widgets, we add a separate `features` param.
5. We don't allow to select nested fields within `features`.

Responses use `snake_case` for field names, consistent with the rest of the GitLab REST API. This applies to top-level fields, the `features` keys, and the nested fields within each feature.

`features` is the flattened representation we recently added to GraphQL; once all consumers switch over, we plan to drop the old `widgets` array for parity.

The reasons for supporting sparse fields are:

1. It avoids serializing unnecessary fields.
2. It reduces payload for clients, which can be especially important for agents that need to minimize context size.
3. It gives us insights into how fields are used within our API.

Every `features` value is available on the listing endpoint. `hierarchy` preloads parent visibility there so it does not cause N+1 queries. Where a feature is too expensive for a list response we split it into a separate list entity or a sub-resource endpoint rather than rejecting the request.

#### Example requests

- **List Work Items within a namespace**

  ```shell
  curl --request GET \
    --header "PRIVATE-TOKEN: <your_access_token>" \
    "https://gitlab.example.com/api/v4/namespaces/gitlab-org%2Fplan/-/work_items?fields=title,state,confidential&features=labels,assignees&work_item_type_id=task"
  ```

  This call lists Work Items of type `task`, requesting the `title`, `state`, and `confidential` fields, plus the `labels` and `assignees` features.

- **Retrieve a single Work Item**

  ```shell
  curl --request GET \
    --header "PRIVATE-TOKEN: <your_access_token>" \
    "https://gitlab.example.com/api/v4/projects/gitlab-org%2Fplan/-/work_items/42?features=labels,hierarchy"
  ```

  This call returns Work Item `42` with only `id`, `iid`, `global_id`, and `title`, and includes the `labels` and `hierarchy` features in the response.

### Creating Work Items

Creating Work Items should remain straightforward while still translating into the existing feature service layer we use for GraphQL. The REST contract flattens feature inputs into a single `features` object whose nested keys mirror the GraphQL widget inputs.

#### Example create request

```shell
curl --request POST \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --header "Content-Type: application/json" \
  --data '{
    "title": "Draft Work Item REST API ADR",
    "work_item_type_id": 1,
    "features": {
      "description": { "description": "Capture the architectural decisions about the REST API." },
      "labels":   { "label_ids": [23, 47] },
      "assignees": { "assignee_ids": [42] }
    }
  }' \
  "https://gitlab.example.com/api/v4/namespaces/gitlab-org%2Fplan/-/work_items"
```

This example creates a Work Item using a flattened `features` object whose nested structures align with the existing GraphQL widget inputs. The REST API accepts integer IDs and translates them to the same service-layer payloads currently produced by the GraphQL prepare hooks.

### Updating Work Items

Today, updates go through a single `PATCH` endpoint that mirrors how the GraphQL update mutation handles changes: core fields are set at the top level, and feature changes flow through a flattened `features` object whose nested keys align with the GraphQL widget inputs. This keeps translation to the service layer minimal and the REST and GraphQL contracts close to each other.

#### Example update request

```shell
curl --request PATCH \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --header "Content-Type: application/json" \
  --data '{
    "title": "Work Item REST API rollout",
    "state_event": "close",
    "features": {
      "description": { "description": "Track the rollout milestones and metrics." },
      "labels": { "add_label_ids": [81], "remove_label_ids": [23, 47] }
    }
  }' \
  "https://gitlab.example.com/api/v4/namespaces/gitlab-org%2Fplan/-/work_items/42"
```

This call:

- updates the title of Work Item `42`
- closes it through `state_event`
- refreshes the description
- adjusts labels through the flattened `features` object

#### Per-feature endpoints (future consideration)

Before GA, we may introduce dedicated per-feature endpoints so clients can update a single feature without rebuilding the whole `features` payload. This is a more typical REST shape, but it is not implemented today and remains an open option rather than a commitment. An example of the shape we have in mind:

```shell
curl --request PATCH \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  --header "Content-Type: application/json" \
  --data '{ "add_label_ids": [81], "remove_label_ids": [23, 47] }' \
  "https://gitlab.example.com/api/v4/groups/gitlab-org/-/work_items/42/labels"
```

Such feature-specific routes would avoid large, multi-purpose payloads while reusing the same field names as the GraphQL inputs. If introduced, they would complement — not replace — the flattened `features` object on the main update endpoint.

### Deleting Work Items

Deleting a Work Item follows the standard REST pattern by issuing a `DELETE` request to the Work Item resource. The endpoint returns `204 No Content` on success when the Work Item is removed.

#### Example delete request

```shell
curl --request DELETE \
  --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/projects/gitlab-org%2Fplan/-/work_items/42"
```

## Implemented endpoints

The endpoint reference, covering every route, parameter, payload, pagination style, and feature flag, lives on its own page: [Work Item REST API endpoints](endpoints.md). It stands in for the public `doc/api/` page until the API leaves its feature flag, at which point it moves there.

## Rollout plan

The API is marked as `experimental` and every route is `hidden`, so none of it appears in the public API reference yet. Since it is crucial to get the REST API right and we cannot introduce breaking changes once it is public, we will remove the `experimental` tag only after we are certain that the API meets our expectations.

Flag coverage is not uniform, and the difference matters when judging what we can still change:

1. The single Work Item, create, update, delete and sub-resource endpoints are controlled by the `work_item_rest_api` flag (default off, with the user as actor). They return `403` when it is disabled.
1. The listing endpoint has completed its rollout and is no longer behind a flag. It was gated by `work_item_rest_api_index` while it rolled out, and once that flag had been enabled globally for a week without issues we removed it. The endpoint also does not require authentication, so anonymous requests succeed for work items in public projects and groups, matching the GraphQL API. Its protection against breaking changes is now the `hidden` and `experimental` status alone.
1. `work_item_rest_api_frontend_users` does not gate any endpoint. It only controls whether the Work Items list and board frontend reads the list from REST instead of GraphQL.

## Decision registry

1. [Build a dedicated Work Items REST API instead of extending the Issues REST API](https://gitlab.com/gitlab-org/gitlab/-/issues/368055#note_1227097586), with the long-term intent of deprecating the Issues API.

   Other work item types (requirement, test case, objective, key result) share Task's widget set and would hit the same parity gaps; a dedicated API gives the flexibility Work Items need.

1. [Hand-write the REST API rather than auto-generate it from GraphQL](https://gitlab.com/gitlab-org/gitlab/-/issues/368055#note_1304000657).

   The API Vision Working Group's REST-wrapper PoCs targeted REST v5 and would take far too long to become feature-complete. Two blockers were never solved: API versioning, and the divergent deprecation policies of GraphQL versus REST.

1. [Postpone the REST API until the Work Items GraphQL API left Alpha and the data model stabilized](https://gitlab.com/gitlab-org/gitlab/-/issues/368055#note_1243016134).

   Defining REST earlier would have forced breaking changes, which are far harder to make on REST than on an Alpha GraphQL API. This is the origin of the experiment-behind-a-flag posture that shows up again in the rollout decisions below.

1. [Do not deprecate the Epics REST API as part of this work](https://gitlab.com/gitlab-org/gitlab/-/issues/368055#note_1917379056).

1. [Aim for parity with GraphQL by design, with GraphQL as the source of truth for filters and response schema](https://gitlab.com/groups/gitlab-org/-/work_items/9673#note_3052544341).

1. [Design the REST API for customer needs rather than frontend parity, so only the list query moves to REST](https://gitlab.com/groups/gitlab-org/-/work_items/22398#note_3517626531).

   The frontend migrates the list query alone, purely for performance. An unstated assumption that the whole frontend would migrate had been driving endpoints to mirror GraphQL mutations; once corrected, reshaping those endpoints cost the frontend nothing, and this unlocked the linked-items and hierarchy carve-outs described below.

1. [Do not omit widgets that already exist in GraphQL or the legacy issue and epic REST APIs, even where demand is unclear](https://gitlab.com/groups/gitlab-org/-/work_items/22398#note_3514528434).

   There is no way to know which attributes third parties depend on. Omitting them risks breaking existing workflows and blocks migration off the legacy endpoints.

1. [Use the generic `PATCH` with a flattened `features` object for most widgets, and add a dedicated sub-endpoint only when a widget is a collection of separately addressable entities](https://gitlab.com/groups/gitlab-org/-/work_items/22398#note_3517626531).

   If a client needs to reference an entity by its own id, or unlink or reorder it, it is a child collection and cannot be folded into a scalar PATCH. The `fields` and `features` design already solves the fat-response problem for reads, so it is specifically the write side of collections that needs splitting out. See also [the rubric for splitting collection writes](https://gitlab.com/groups/gitlab-org/-/work_items/22398#note_3521914109).

1. [Remove `features.linked_items` from create and update, keep it read-only on show, and manage links through `POST` and `DELETE /-/work_items/:iid/linked_items`](https://gitlab.com/groups/gitlab-org/-/work_items/22398#note_3516168878).

   The field was additive only. It could not unlink or reorder, and a link has its own id and per-link authorization.

1. [Remove `features.hierarchy.children_ids` from create and update while keeping `features.hierarchy.parent_id`, and manage children through dedicated endpoints](https://gitlab.com/groups/gitlab-org/-/work_items/22398#note_3516168878).

   `children_ids` had the same additive-only problem, and unlinking previously required patching each child's `parent_id` to null, which is backwards and unsafe under concurrent tree changes. `parent_id` is a genuine scalar property of the item and stays inline. The children write endpoints (`POST`/`DELETE`/`PUT .../children/:child_id`) have since shipped.

1. [Build Work Item native notes and discussions CRUD endpoints rather than leaving writes on the legacy `/issues/:iid/notes` API](https://gitlab.com/groups/gitlab-org/-/work_items/21728#note_3490998470).

   `features.notes` on PATCH only accepts `discussion_locked`. More importantly, the legacy endpoint routes through Issues services and silently drops work-item-only quick actions such as `/status`, so the behavior differs, not just the URL. See also [the discussion on quick actions dropped by the legacy notes API](https://gitlab.com/groups/gitlab-org/-/work_items/21728#note_3521919684).

1. [Allow a single feature name to resolve to two entity shapes, a basic one on the list endpoint and a detail one on show, selected by endpoint rather than by a client parameter](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/228670).

   This keeps listing fast where a feature is N+1 prone or carries data a list view never shows.

1. [Expose any feature that needs its own pagination as a separate sub-endpoint rather than as a `features` key](https://gitlab.com/groups/gitlab-org/-/work_items/21728).

   GraphQL supports nested connection pagination and REST does not. This is the principle behind the notes, discussions, children and linked items endpoints.

1. [Declare `work_item_type_ids` as a first-class `Array[Integer]` filter and remove the base type `types` filter before GA](https://gitlab.com/gitlab-org/gitlab/-/work_items/605888#note_3552897024).

   `work_item_type_ids` previously worked only as an undeclared parameter leaking through the raw params hash. Base types are an internal detail that is actively misleading with custom types, since `types=issue` also returns every custom type built on the issue base type. See also [the merge request removing the `types` filter](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/245936).

1. [Add `work_item_type_names` as a REST-only filter, case-insensitive, where unknown names match nothing rather than raising](https://gitlab.com/gitlab-org/gitlab/-/work_items/605888#note_3571780518).

   Integer type ids are unusable for custom types created per namespace, and universal tooling such as gitlab-triage writes type names in YAML and cannot know ids ahead of time. Matching nothing on an unknown name is consistent with how an unknown id already behaves.

1. [Do not bring `exclude_group_work_items` and `exclude_projects` to parity; record them as intentional exclusions in the parity spec](https://gitlab.com/gitlab-org/gitlab/-/issues/595010).

   They were a temporary GraphQL workaround from before the `traversal_ids` optimization, so replicating them would cement a workaround as API surface.

1. [Authorize `:read_work_item` against the work item itself on the single item endpoint, not only against its container, and return 404 rather than 403 when access is denied](https://gitlab.com/gitlab-org/gitlab/-/issues/603898).

   Authorizing only the parent leaks individual work items, such as confidential ones, to anyone who can read the container. 404 matches the list endpoint and avoids confirming existence.

1. [Run the beta on GitLab.com only, enabled per group by feature flag, without committing to the design, so breaking changes remain possible](https://gitlab.com/gitlab-org/gitlab/-/issues/599248#note_3461368353).

1. [Defer the `participants` widget out of Beta and GA and track it in a dedicated out-of-scope epic rather than dropping it silently](https://gitlab.com/groups/gitlab-org/-/work_items/22398#note_3514528434).

   Participants was historically a performance bottleneck. Closing the work as "won't do" in a tracked epic keeps the exclusion auditable and reversible, and open to community contribution. See also [the issue closing the participants widget](https://gitlab.com/gitlab-org/gitlab/-/issues/601069#note_3516576976).
1. [Use keyset pagination on every endpoint, exposed as an opaque cursor](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/20950#note_3788496964).
   A client should not have to inspect response headers to learn which mechanism a given sort uses, and a uniform cursor contract leaves the implementation free to change. Where an ordering has no keyset form, the server pages by offset behind the same cursor. Implementation is tracked in [gitlab-org/gitlab#628176](https://gitlab.com/gitlab-org/gitlab/-/work_items/628176).
1. [Return `400` for unknown `fields` and `features` values, and omit features an item's type does not support or that are unlicensed](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/20950#note_3788728139).
   A `200` should mean the request was understood in full, so an unrecognized name is rejected rather than dropped, as GraphQL does at query validation. A valid feature that an individual item cannot have is left out of that item instead, also mirroring GraphQL, because a list response spans several work item types and a single `400` would make mixed-type lists unusable. See also [the discussion on failing loudly](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/20950#note_3822228190). Implementation is tracked in [gitlab-org/gitlab#629477](https://gitlab.com/gitlab-org/gitlab/-/work_items/629477).
