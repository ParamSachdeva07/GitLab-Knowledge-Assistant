---
title: 'Automated Dependency Updates ADR 003: Single service account model'
description: 'Decision to use a single service account per project for both the update job and merge request creation, instead of the originally proposed two-account model.'
---

## Context

The original proposal called for two separate accounts to limit the blast
radius of a compromised token:

- A **CI job account**, scoped to read the repository and write only to
  dependency-update branches, with no package registry tokens and no
  merge-request-creation rights.
- A separate **MR-creation account**, used only to open merge requests from
  branches the CI job account had already pushed to, with no ability to run
  arbitrary code.

The idea was that a compromised job token would never carry the `api` scope
needed to open merge requests, and a compromised MR-creation token would
never be able to run code.

## Decision

We provision a **single service account per project** and use it for both
steps.

`DependencyManagement::ProvisionServiceAccountService` creates one service
account named `GitLab Dependency Management` per project (idempotently, via
an exclusive lease keyed on the project), using
`Namespaces::ServiceAccounts::ProjectCreateService`, and adds it to the
project as a **Guest** member. Both `UpdateService` (which drives the update
job and pushes the branch) and `CreateMergeRequestService` (which opens the
resulting merge request) reuse this same account via
`project.dependency_management_service_account`.

### How the permissions actually work

The service account is passed as the current user to the ordinary application
services that create the branch, write the files, and open the merge request.
Every action goes through normal permission checks — nothing bypasses
authorization.

What grants those actions is a dedicated internal role,
[`config/authz/roles/dependency_management_service_account.yml`](https://gitlab.com/gitlab-org/gitlab/-/blob/master/config/authz/roles/dependency_management_service_account.yml).
The project policy enables that role only when the current user is both a
member of the project and *is* that project's designated dependency
management service account. The role is scoped to what the feature needs:
read the repository, push branches, create pipelines, and create, read, and
update merge requests. The Guest membership is what makes the account a
member at all; it is not what confers write access. The role file is the
authority on the exact permission set.

### What we gave up

The two-account design's core property does not survive: one identity now
both runs the update job and opens the merge request. A compromised service
account can push to any unprotected branch in that project and open merge
requests, where the original split meant a compromised job credential could
not open a merge request and a compromised merge-request credential could not
run code.

We accepted that in exchange for the following:

1. The permission set is narrow and declared in one reviewable file, rather
   than implied by two accounts' role assignments.
1. There is no long-lived API-scoped token to leak — authorization is
   policy-based rather than token-based, and the account is issued no package
   registry credentials.
1. Because the writes go through the ordinary file and branch services as a
   normal user, the project's existing repository controls apply to them
   rather than being bypassed.
1. Merge request creation rejects an update that would touch an unreasonable
   number of files, bounding the blast radius of any single automated commit.
1. One credential per project instead of two removes the provisioning,
   rotation, and cleanup overhead. Provisioning is idempotent, and a failed
   membership add cleans up the orphaned account.

If the separation of duties is wanted back later, the natural shape is a
second internal role rather than a second account.

## References

1. `ee/app/services/dependency_management/provision_service_account_service.rb`
1. `ee/app/services/dependency_management/security_update/create_merge_request_service.rb`
1. `ee/app/policies/ee/project_policy.rb`
1. `config/authz/roles/dependency_management_service_account.yml`
1. [001: Bounded, severity-prioritized remediation](./001_bounded_severity_prioritized_remediation.md)
