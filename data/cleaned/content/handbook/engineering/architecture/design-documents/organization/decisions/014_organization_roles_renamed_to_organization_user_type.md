---
owning-stage: "~devops::tenant scale"
title: 'Organizations ADR 014: Organization roles renamed to Organization user types'
description: "ADR proposing to rename Organization roles to Organization user types to avoid confusion with feature-specific roles."
creation-date: "2026-06-11"
authors: [ "@peterhegman" ]
toc_hide: true
---

## Context

There is an `organization_users` table that holds the users that belong to an Organization. This table has an `access_level` column that defines the access the user has to the Organization. In the future we will be introducing roles that are specific to an Organization feature such as Artifact Registry. We want to avoid confusion between these feature roles and the access level of the Organization user.

### Current state

Currently in the UI we are referring to the `access_level` of an Organization user as their "Organization role". There are two options:

- Organization owner
- Organization user

A user that belongs to an Organization is called a "Member".

## Decision

The `access_level` of the Organization user will be referred to as "Organization user type". There will be two options:

- Organization Administrator
- Organization Regular User

This aligns with the current user types we have in the admin area (Administrator and Regular).

A user that belongs to an Organization is called an "Organization user".

## Consequences

- This could cause confusion between Instance Administrator and Organization Administrator.
