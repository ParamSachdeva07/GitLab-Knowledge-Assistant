---
title: "Work Item REST API endpoints"
description: "Endpoint reference for the Work Item REST API: routes, parameters, payloads, pagination, authorization, and feature flags."
toc_hide: true
---

This API is in active development and sits behind a feature flag, so it has no public `doc/api/` reference page yet. What follows is a draft of that future documentation.

All paths below are relative to `/api/v4`. Every logical endpoint exists in three variants:

- `/namespaces/:id/-/work_items...`
- `/projects/:id/-/work_items...`
- `/groups/:id/-/work_items...`

In all three, `:id` accepts either a numeric ID or an unescaped full path.

Availability is stated per license tier rather than per edition, because gitlab.com runs EE while its free namespaces behave like CE. **Free** means every tier on both CE and EE builds. **Premium** and **Ultimate** name the tier whose license unlocks the item. A few items ship only in EE builds but need no license; those say **EE builds**.

## Endpoint summary

| Verb | Path | Purpose | Availability |
|---|---|---|---|
| `GET` | — | List work items | Free |
| `GET` | `/:work_item_iid` | Get one work item | Free |
| `POST` | — | Create work item | Free |
| `PATCH` | `/:work_item_iid` | Update work item | Free |
| `DELETE` | `/:work_item_iid` | Delete work item | Free |
| `GET` | `/:work_item_iid/children` | List children | Free |
| `POST` | `/:work_item_iid/children/:child_id` | Attach child | Free |
| `DELETE` | `/:work_item_iid/children/:child_id` | Detach child | Free |
| `PUT` | `/:work_item_iid/children/:child_id` | Reorder child | Free |
| `GET` | `/:work_item_iid/notes` | List notes | Free |
| `GET` | `/:work_item_iid/discussions` | List discussions | Free |
| `GET` | `/:work_item_iid/discussions/:discussion_id` | Get one discussion | Free |
| `GET` | `/:work_item_iid/closing_merge_requests` | MRs that close the item | Free |
| `GET` | `/:work_item_iid/related_merge_requests` | MRs referencing the item | Free |
| `GET` | `/:work_item_iid/related_branches` | Branches referencing the item | Free |
| `GET` | `/:work_item_iid/feature_flags` | Feature flags on the item | EE builds |
| `GET` | `/:work_item_iid/linked_items` | List linked work items | Free |
| `GET` | `/:work_item_iid/linked_resources` | List linked resources (Zoom) | Free |
| `GET` | `/:work_item_iid/award_emoji` | List emoji reactions | Free |
| `GET` | `/:work_item_iid/current_user_todos` | List current user's to-dos | Free |
| `GET` | `/:work_item_iid/email_participants` | List Service Desk email participants | Free |

## Selecting fields and features

Every response always includes exactly four fields: `id`, `iid`, `global_id`, `title`. Everything else is opt-in and must be requested explicitly through `fields=`.

<details>
<summary markdown="span">All 25 `fields` values</summary>

| Field | Type | Example |
|---|---|---|
| `id` | integer | `1` |
| `global_id` | string | `gid://gitlab/WorkItem/1` |
| `iid` | integer | `1` |
| `title` | string | `Fix the bug` |
| `state` | string | `opened` |
| `confidential` | boolean | `false` |
| `imported` | boolean | `false` |
| `hidden` | boolean | `false` |
| `lock_version` | integer | `0` |
| `created_at` | datetime | `2022-08-17T12:46:35.053Z` |
| `updated_at` | datetime | `2022-11-14T17:22:01.470Z` |
| `closed_at` | datetime | `2022-11-15T08:30:55.232Z` |
| `title_html` | string | `<p>Fix the bug</p>` |
| `author` | object | an `Author` entity |
| `work_item_type` | object | a `Type` entity |
| `namespace` | object | a `NamespaceBasic` entity |
| `create_note_email` | string | `issue-1@example.com` |
| `duplicated_to_work_item_url` | string | `https://gitlab.example.com/groups/gitlab-org/-/work_items/2` |
| `moved_to_work_item_url` | string | `https://gitlab.example.com/groups/gitlab-org/-/work_items/3` |
| `reference` | string | `gitlab-org#1` |
| `web_url` | string | `https://gitlab.example.com/groups/gitlab-org/-/work_items/1` |
| `web_path` | string | `/groups/gitlab-org/-/work_items/1` |
| `user_permissions` | object | a `Permissions` entity |
| `user_discussions_count` | integer | `3` |
| `features` | object | keyed by feature name, see the next table |

</details>

`features` defaults to empty, so nothing feature-related is returned unless requested. Every feature is an object except `assignees`, which is an array. Twelve are available in every tier; the other ten depend on the license.

<details>
<summary markdown="span">All 22 `features` values with example payloads</summary>

| Feature | Availability | Example |
|---|---|---|
| `description` | Free | `{"description": "Fix the login bug", "description_html": "<p>Fix the login bug</p>", "edited": false, "last_edited_at": "2022-11-15T08:30:55.232Z", "last_edited_by": {…}, "task_completion_status": {…}}` |
| `assignees` | Free | `[{"id": 1, "username": "alice", …}]` |
| `labels` | Free | `{"allows_scoped_labels": true, "labels": [{…}]}` |
| `milestone` | Free | `{"id": 1, "iid": 1, "title": "19.2", …}` |
| `start_and_due_date` | Free | `{"start_date": "2022-08-17", "due_date": "2022-08-30", "roll_up": false}` |
| `designs` | Free | `{"design_collection": {"copy_state": "ready"}}` |
| `time_tracking` | Free | `{"time_estimate": 12600, "total_time_spent": 4500, "human_readable_attributes": {"time_estimate": "3h 30m", "total_time_spent": "1h 15m"}, "timelogs": […]}` |
| `error_tracking` | Free | `{"identifier": 12345}` |
| `hierarchy` | Free | `{"parent": {…}, "has_parent": true}` |
| `award_emoji` | Free | `{"upvotes": 5, "downvotes": 1, "new_custom_emoji_path": "/groups/gitlab-org/-/custom_emoji/new"}` |
| `development` | Free | `{"closing_merge_requests_count": 2, "will_auto_close_by_merge_request": false}` |
| `notifications` | Free | `{"subscribed": true}` |
| `color` | Premium | `{"color": "#A8DADC", "text_color": "#1D3557"}` |
| `progress` | Ultimate | `{"progress": 65, "current_value": 13, "start_value": 0, "end_value": 20, "updated_at": "2024-02-12T09:45:00Z"}` |
| `iteration` | Premium | `{"iteration": {…}}` |
| `health_status` | Ultimate | `{"health_status": "needs_attention"}` |
| `weight` | Premium | `{"weight": 3, "rolled_up_weight": 8, "rolled_up_completed_weight": 5}` |
| `requirement_legacy` | Ultimate | `{"legacy_iid": 1}` |
| `status` | Premium | `{"status": {"id": "gid://gitlab/WorkItems::Statuses::SystemDefined::Status/1", "name": "To do", "category": "to_do", "color": "#737278", …}}` |
| `verification_status` | Ultimate | `{"verification_status": "satisfied"}` |
| `linked_items` | EE builds | `{"blocking_count": 2, "blocked_by_count": 1}` |
| `custom_fields` | Premium | `{"custom_field_values": [{"custom_field": {"id": 1, "name": "Priority", "field_type": "single_select", …}, "value": "In progress", "selected_options": […]}]}` |

</details>

Both `fields` and `features` are comma-separated and downcased. A value that is not a known field or feature name returns `400` listing the unknown values, so a typo is caught rather than ignored. A feature that is valid but that the work item's type does not support, or that is not licensed for the namespace, is omitted from that item's response instead of erroring. This mirrors GraphQL: a list spans several work item types, and each item returns only the features it has. `hierarchy` is explicitly permitted on the list endpoint, it is preloaded there specifically.

## Pagination

Every collection endpoint uses keyset pagination, exposed to clients as an opaque cursor. Requests take `cursor` and `per_page`. Responses carry `X-Next-Cursor` and `X-Prev-Cursor`, plus a `Link` header with `rel="next"` and `rel="prev"`.

Some orderings have no keyset form, for example the list endpoint's `popularity` and `milestone_due` sorts. For those the server pages by offset behind the same opaque cursor, so the contract does not change with the sort or the endpoint.

Unreadable records are filtered out **after** the page is fetched, so a page can hold fewer than `per_page` items, or none at all, while `X-Next-Cursor` is still present. Clients must follow the cursor rather than treat a short or empty page as the end of the collection.

Discussions are paged by `Issuable::DiscussionsListService`, which REST shares with the GraphQL resolver and the Rails controller.

## Authorization

1. **Authentication.** Every endpoint calls `authenticate!` except the list endpoint, which is reachable anonymously against public projects and groups. There is no unauthenticated write path.
1. **Permission.** Each route declares the ability the caller must hold, evaluated against the work item's container.
1. **CI job token policies.** A narrower gate that only runs when the caller is a CI job token. It has no bearing on personal access tokens, OAuth, or session requests.

| Group | Authentication | Permission | CI job token |
|---|---|---|---|
| List | not required | `:read_work_item` | `read_work_items`, on the `namespaces` and `projects` variants |
| Show, all GET sub-resources | required | `:read_work_item` | `read_work_items`, on the `namespaces` and `projects` variants (see exception below) |
| Create | required | `:create_work_item` | not accepted |
| Update, children attach/detach/reorder | required | `:update_work_item` | not accepted |
| Delete | required | `:delete_work_item` | not accepted |

"Not accepted" in the last column is an active rejection, not a missing check. A route that declares no `job_token_policies` fails the job token gate with `403` and the message "This action is unauthorized for CI/CD job tokens." Those routes are still authenticated and still permission-checked in the usual way; the column only says that a CI job token is not a usable credential for them. The gate is bypassed in a handful of configurations, such as a token used against its own project or an allowlist entry still on default permissions, so it describes the route's declaration rather than a guarantee for every deployment.

Container boundaries: the `namespaces` variant resolves to either `group` or `project`, depending on what the id points at.

Exception: the `groups` variant of email_participants does declare job token policies, unlike the rest of the GET sub-resources.

A denied request returns `404`, not `403`, both when the container itself is invisible and when the specific item is unreadable. A feature flag being off is a separate case and returns `403`.

## Feature flags

1. `work_item_rest_api` (type `wip`, default off, per-user, introduced in 18.9) gates show, create, update, delete, and the GET sub-resources. They return `403` while it is off. It does **not** gate the list endpoint. [Rollout issue](https://gitlab.com/gitlab-org/gitlab/-/work_items/588874).
1. `work_item_rest_api_index` (type `wip`, introduced in 19.1, since removed) previously gated the list endpoint on its own. [Rollout issue](https://gitlab.com/gitlab-org/gitlab/-/work_items/601895).
1. `work_item_rest_api_frontend_users` (type `wip`, default off, introduced in 19.0) does not gate any endpoint. It only controls whether the Vue list and board views fetch work items through REST instead of GraphQL. [Rollout issue](https://gitlab.com/gitlab-org/gitlab/-/work_items/596882).

One further flag changes what an endpoint returns without being ours to roll out: `explicit_mr_work_item_relations`, owned by group::work items, widens the related merge requests response. It is described with [that endpoint](#related-merge-requests) rather than listed here.

## Core endpoints

Each endpoint below shows its verb, path, and purpose. Parameters and response details are collapsed, expand an endpoint to see them.

### List

`GET /-/work_items`

Lists work items visible to the current user (or anonymously, see [Authorization](#authorization)) in the given container.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `per_page` | integer | no | items per page, default `20` |
| `cursor` | string | no | keyset pagination cursor |
| `order_by` | string | no | default `created_at` |
| `sort` | string | no | default `desc` |
| `fields` | string | no | comma-separated field list, see [Selecting fields and features](#selecting-fields-and-features) |
| `features` | string | no | comma-separated feature list, default empty |

Filters (all optional, array-type params accept comma-separated values):

| Group | Filters |
|---|---|
| Basic | `ids`, `iids`, `state` (`opened`/`closed`/`all`), `work_item_type_ids` XOR `work_item_type_names`, `author_username`, `assignee_usernames` XOR `assignee_wildcard_id` (`None`/`Any`/`Me`), `label_name`, `milestone_title` XOR `milestone_wildcard_id` (`None`/`Any`/`Upcoming`/`Started`), `my_reaction_emoji`, `created_before`/`created_after`, `updated_before`/`updated_after`, `closed_before`/`closed_after`, `due_before`/`due_after`, `search`, `in` (`title`,`description`), `timeframe[start]`/`timeframe[end]`, `confidential`, `subscribed`, `parent_ids` XOR `parent_wildcard_id`, `include_descendant_work_items`, `release_tag` XOR `release_tag_wildcard_id`, `crm_contact_id`, `crm_organization_id` |
| `not[...]` | `assignee_usernames`, `author_username`, `label_name`, `milestone_title` XOR `milestone_wildcard_id`, `my_reaction_emoji`, `parent_ids`, `release_tag`, `work_item_type_ids` XOR `work_item_type_names` |
| `not[...]` (licensed) | `iteration_id` XOR `iteration_wildcard_id` (Premium), `health_status_filter` (Ultimate), `weight` (Premium). Negated `health_status_filter` takes an array of health status values, unlike the top-level filter, which is a single string that also accepts `none` and `any`. |
| `or[...]` | `assignee_usernames`, `author_usernames`, `label_names` |
| Licensed | `iteration_id` XOR `iteration_wildcard_id`, `iteration_cadence_id` (Premium), `health_status_filter` (Ultimate), `weight` XOR `weight_wildcard_id` (Premium), `custom_field[]` (Premium), `status[id]` XOR `status[name]` (Premium), `verification_status_widget[verification_status]` (Ultimate) |
| Group/namespace-only (not accepted by the `projects` variant) | `include_ancestors`, `include_descendants`, `include_archived` (default `false`) |

Response: an array of `WorkItemBasic`.

</details>

### Get

`GET /-/work_items/:work_item_iid`

Returns a single work item.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the work item, path parameter |
| `fields` | string | no | comma-separated field list |
| `features` | string | no | comma-separated feature list |

Response: `WorkItemDetail`, whose root fields are identical to `WorkItemBasic`. With Ultimate, the `health_status` feature carries extra detail (`count`, `rolled_up_health_status`). This is the only endpoint reachable with an `ai_workflows`-scoped token.

</details>

### Create

`POST /-/work_items` returns `201`.

Creates a work item.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `title` | string | yes | — |
| `work_item_type_name` / `work_item_type_id` | string / integer | at least one required | selects the work item type |
| `confidential` | boolean | no | — |
| `created_at` | datetime | no | admins/owners only |
| `fields` | string | no | fields to include in the response |
| `features` | object | no | feature payloads keyed by feature name, see [Feature payloads](#feature-payloads) |

Response: `WorkItemBasic`.

</details>

### Update

`PATCH /-/work_items/:work_item_iid` returns `200`.

Updates a work item. This is `PATCH` only, there is no `PUT` on the work item resource itself (the only `PUT` in the API is child reorder).

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the work item, path parameter |
| `title` | string | no | — |
| `confidential` | boolean | no | — |
| `state_event` | string | no | `close` or `reopen` |
| `fields` | string | no | fields to include in the response |
| `features` | object | no | feature payloads keyed by feature name, see [Feature payloads](#feature-payloads) |

The `features` keys submitted in the request also select which feature payloads come back in the response. A widget the work item's type does not support returns `400` with an `unsupported_widgets` list; a widget the type supports but that is disabled for the container is silently dropped instead of erroring.

Response: `WorkItemBasic`.

</details>

### Delete

`DELETE /-/work_items/:work_item_iid` returns `204`, no body.

### Feature payloads

`features` is an object keyed by feature name, and each feature has its own payload. Create and update accept different sets, and a few features take different keys on each, so both are shown side by side below. "Not accepted" means the feature is rejected on that verb.

| Feature | Availability | Create payload | Update payload |
|---|---|---|---|
| `description` | Free | `description` <strong class="text-danger">required</strong> | `description` <strong class="text-danger">required</strong> |
| `assignees` | Free | `assignee_ids` <strong class="text-danger">required, max 30</strong> | `assignee_ids` <strong class="text-danger">required, max 30</strong> |
| `labels` | Free | `label_ids` <strong class="text-danger">required, max 30</strong> | `add_label_ids`, `remove_label_ids` <strong class="text-danger">max 30 each</strong> |
| `milestone` | Free | `milestone_id`, send `null` to clear it | same as create |
| `hierarchy` | Free | `parent_id` | `parent_id`, `null` removes the parent |
| `start_and_due_date` | Free | `start_date`, `due_date` | same as create |
| `linked_items` | Free | `work_items_ids` <strong class="text-danger">required, max 30</strong>, `link_type` (only `relates_to`, the default) | not accepted |
| `crm_contacts` | Free | `contact_ids` <strong class="text-danger">required</strong> | `contact_ids` <strong class="text-danger">required</strong>, `operation_mode` (`REPLACE` default, `APPEND`, `REMOVE`) |
| `notes` | Free | not accepted | `discussion_locked` <strong class="text-danger">required</strong> |
| `notifications` | Free | not accepted | `subscribed` <strong class="text-danger">required</strong> |
| `current_user_todos` | Free | not accepted | `action` <strong class="text-danger">required</strong> (`mark_as_done` or `add`), `todo_id` (omit to update every to-do on the item) |
| `award_emoji` | Free | not accepted | `action` <strong class="text-danger">required</strong> (`add`, `remove`, or `toggle`), `name` <strong class="text-danger">required</strong> |
| `time_tracking` | Free | not accepted | `time_estimate` in human-readable form such as `1h 30m`, and `timelog` with `time_spent` <strong class="text-danger">required</strong>, `spent_at`, `summary` |
| `color` | Premium | `color` <strong class="text-danger">required</strong>, hex code such as `#e24329` | same as create |
| `health_status` | Ultimate | `health_status` (`on_track`, `needs_attention`, `at_risk`) | same as create |
| `iteration` | Premium | `iteration_id`, send `null` to clear it | same as create |
| `weight` | Premium | `weight`, send `null` to clear it | same as create |
| `status` | Premium | `status_id`, resolved against the namespace as either a custom or a system-defined status | same as create |
| `custom_fields` | Premium | array of entries, each carrying `custom_field_id` and whichever of `text_value`, `number_value`, `date_value`, or `selected_option_ids` matches the field's type | same as create, <strong class="text-danger">max 30 entries</strong> |
| `progress` | Ultimate | not accepted | `current_value` <strong class="text-danger">required</strong>, `start_value`, `end_value` |
| `verification_status` | Ultimate | not accepted | `verification_status` <strong class="text-danger">required</strong> |

`labels` is worth calling out: it takes `label_ids` on create but `add_label_ids`/`remove_label_ids` on update, so the same feature name means "set these" on one verb and "change these" on the other.

## Sub-resource endpoints

The remaining endpoints all hang off a single work item. Every one of them takes `work_item_iid` in the path, requires `:read_work_item`, and is gated by the `work_item_rest_api` flag. All are `GET` unless stated otherwise. They are grouped below by the concept they expose.

## Hierarchy endpoints

These cover a work item's children. The three write operations all return an identical generic `404` when the child cannot be found, whatever the reason, so existence cannot be probed.

### List children

`GET /-/work_items/:work_item_iid/children`

Lists a work item's children.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the parent work item, path parameter |
| `state` | string | no | `opened` or `closed`, omitted returns both |
| `fields` | string | no | comma-separated field list |
| `features` | string | no | comma-separated feature list |
| `cursor` | string | no | keyset pagination cursor |
| `per_page` | integer | no | items per page, default `20` |

Response: an array of `WorkItemBasic`.

</details>

### Attach a child

`POST /-/work_items/:work_item_iid/children/:child_id` returns `201`.

Attaches an existing work item as a child.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the parent work item, path parameter |
| `child_id` | integer | yes | numeric ID of the work item to attach, path parameter |

`child_id` is the child's numeric ID, not its iid, because a child can live in another namespace. It is not the `gid://` value returned in the `global_id` field.

Response: the child as `WorkItemBasic`. Returns `409` when the work item is already a child of this parent, and `422` for an invalid hierarchy.

</details>

### Detach a child

`DELETE /-/work_items/:work_item_iid/children/:child_id` returns `204`, no body.

Removes the parent/child link.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the parent work item, path parameter |
| `child_id` | integer | yes | numeric ID of the child, path parameter |

Returns `422` when the link cannot be removed.

</details>

### Reorder a child

`PUT /-/work_items/:work_item_iid/children/:child_id` returns `200`.

Moves a child within its siblings.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the parent work item, path parameter |
| `child_id` | integer | yes | numeric ID of the child to move, path parameter |
| `move_before_id` | integer | no | numeric ID of the sibling to move before |
| `move_after_id` | integer | no | numeric ID of the sibling to move after |

At least one of `move_before_id` or `move_after_id` is required, and the anchor sibling must be readable by the caller.

Response: the child as `WorkItemBasic`. Returns `422` when the move is invalid.

</details>

## Notes endpoints

Notes are the individual comments and system-generated activity entries on a work item. Listing is the only note operation available today, with more on the way.

### List notes

`GET /-/work_items/:work_item_iid/notes`

Lists notes on the work item.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the work item, path parameter |
| `order_by` | string | no | default `created_at`, or `updated_at` |
| `sort` | string | no | default `asc`, or `desc` |
| `activity_filter` | string | no | default `all_notes`, or `only_comments`, `only_activity` |
| `cursor` | string | no | keyset pagination cursor |
| `per_page` | integer | no | items per page, default `20` |

Requires `:read_note` in addition to `:read_work_item`.

Response: an array of `Note`.

</details>

## Discussion endpoints

A discussion is a thread of notes. Both endpoints require `:read_note` in addition to `:read_work_item`.

### List discussions

`GET /-/work_items/:work_item_iid/discussions`

Lists the discussions on the work item.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the work item, path parameter |
| `sort` | string | no | default `asc`, or `desc` |
| `activity_filter` | string | no | default `all_notes`, or `only_comments`, `only_activity` |
| `cursor` | string | no | keyset pagination cursor |
| `per_page` | integer | no | default `20`, maximum `100` |

Response: an array of `Discussion`.

</details>

### Get a discussion

`GET /-/work_items/:work_item_iid/discussions/:discussion_id`

Returns a single discussion.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the work item, path parameter |
| `discussion_id` | string | yes | ID of the discussion, path parameter |

Response: a single `Discussion`. Discussions generated from resource events, such as label or state changes, have no rows in `notes` and cannot be fetched here, so an id taken from the list response can return `404`. GraphQL behaves the same way.

</details>

## Development widget endpoints

These four back the development widget, which links a work item to the merge requests, branches, and feature flags related to it. All of them describe project-scoped concepts, so a group-level work item returns an empty collection from each.

### Closing merge requests

`GET /-/work_items/:work_item_iid/closing_merge_requests`

Lists the merge requests that close the work item.

<details>
<summary markdown="span">Parameters and response</summary>

Takes `work_item_iid` in the path, plus `cursor` and `per_page`.

Response: an array of `ClosingMergeRequest`, which exposes `id`, `from_mr_description`, and a nested `merge_request`.

The query is not scoped to the work item's project, because a merge request in another project can close it. Visibility is enforced in SQL, so pages are never short.

</details>

### Related merge requests

`GET /-/work_items/:work_item_iid/related_merge_requests`

Lists the merge requests that reference the work item.

<details>
<summary markdown="span">Parameters and response</summary>

Takes `work_item_iid` in the path, plus `cursor` and `per_page`.

Response: an array of `MergeRequestBasic`.

The set is derived by the same service that backs the GraphQL development widget, so REST tracks GraphQL rather than deriving the set a second way. Results are ordered by `iid` with `id` as a tiebreak, which keeps pagination stable across pages. When the `explicit_mr_work_item_relations` flag is enabled, the response also includes merge requests explicitly related to the work item, not only those that reference it in a note. A merge request that is both is returned once.

</details>

### Related branches

`GET /-/work_items/:work_item_iid/related_branches`

Lists the branches whose name references the work item.

<details>
<summary markdown="span">Parameters and response</summary>

Takes `work_item_iid` in the path, plus `cursor` and `per_page`.

Response: an array of `RelatedBranch` with `name`, `compare_path`, and `pipeline_status`.

Branches come from Gitaly rather than the database, so they are sorted by name and paginated in memory. A user without `read_code` gets an empty array.

</details>

### Feature flags

`GET /-/work_items/:work_item_iid/feature_flags`

Lists the feature flags linked to the work item. EE builds only, no license required.

<details>
<summary markdown="span">Parameters and response</summary>

Takes `work_item_iid` in the path, plus `cursor` and `per_page`.

Response: an array of `FeatureFlag` with `id`, `name`, `active`, `path`, and `reference`.

Unreadable flags are filtered out before pagination runs, so pages are never short, unlike the endpoints described in [Pagination](#pagination) that filter afterwards.

</details>

## Other sub-resource endpoints

These expose one concept each and share nothing beyond the conventions described above.

### Linked items

`GET /-/work_items/:work_item_iid/linked_items`

Lists work items linked to this one.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the work item, path parameter |
| `state` | string | no | `opened` or `closed` |
| `link_type` | string | no | `relates_to`; `blocks` and `is_blocked_by` with Premium |
| `fields` | string | no | comma-separated field list |
| `features` | string | no | comma-separated feature list |
| `cursor` | string | no | keyset pagination cursor |
| `per_page` | integer | no | items per page, default `20` |

Response: an array of `LinkedWorkItem`, which is `WorkItemBasic` plus `link_id`, `link_type`, `link_created_at`, and `link_updated_at`.

</details>

### Linked resources

`GET /-/work_items/:work_item_iid/linked_resources`

Lists linked external resources, currently Zoom links only.

<details>
<summary markdown="span">Parameters and response</summary>

Takes `work_item_iid` in the path, plus `cursor` and `per_page`.

Response: an array of `LinkedResource`, which exposes a single `url` field.

</details>

### Emoji reactions

`GET /-/work_items/:work_item_iid/award_emoji`

Lists emoji reactions on the work item.

<details>
<summary markdown="span">Parameters and response</summary>

Takes `work_item_iid` in the path, plus `cursor` and `per_page`.

Response: an array of `AwardEmoji`.

</details>

### Current user to-dos

`GET /-/work_items/:work_item_iid/current_user_todos`

Lists the calling user's to-dos on the work item. It is always scoped to that user, there is no way to read another user's to-dos.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the work item, path parameter |
| `state` | string | no | `pending` or `done`, omitted returns both |
| `cursor` | string | no | keyset pagination cursor |
| `per_page` | integer | no | items per page, default `20` |

Response: an array of `Todo`.

</details>

### Email participants

`GET /-/work_items/:work_item_iid/email_participants`

Lists the Service Desk email participants on the work item.

<details>
<summary markdown="span">Parameters and response</summary>

| Parameter | Type | Required | Description |
|---|---|---|---|
| `work_item_iid` | integer | yes | IID of the work item, path parameter |
| `fields` | string | no | comma-separated field list, see below |
| `cursor` | string | no | keyset pagination cursor |
| `per_page` | integer | no | items per page, default `20` |

This endpoint has its own `fields` vocabulary, unrelated to the work item field list: `id` and `email` by default, plus `created_at` and `updated_at`. Email addresses are masked according to the caller's permissions.

Response: an array of `EmailParticipant`. Returns `404` when the work item type has no email participants widget.

Two things set this endpoint apart from every other route in the API: its feature category is `service_desk` rather than `portfolio_management`, and it is the only group-scoped route that declares job token policies.

</details>
