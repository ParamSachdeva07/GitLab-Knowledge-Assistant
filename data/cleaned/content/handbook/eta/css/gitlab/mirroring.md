---
title: 'Project mirroring'
description: 'Documentation on project mirroring'
---

This guide covers GitLab repository mirroring setup for Customer Support Systems projects. Mirroring automatically synchronizes changes from source repositories to target repositories, enabling automated backups and multi-repo workflows.

## Understanding mirroring

### What is mirroring

This guide covers GitLab repository mirroring setup for Customer Support Systems projects. Mirroring automatically synchronizes changes from source repositories to target repositories, enabling automated backups and multi-repo workflows.

## Setup

For the Customer Support Systems team, we setup mirroring using these steps:

1. Login as the `gl-support-bot` user (as it is used as a service account for mirrors)
1. Navigate to the source project
1. Add a new mirror
   - Git repository URL: `ssh://gitlab.com/full/path/to/project.git`
   - Mirror direction: `Push`
   - Authentication method: `SSH public key`
   - Username: `git`
   - Keep divergent refs: unchecked
   - Mirror branches: `Mirror only protected branches`
1. Copy SSH public key from new mirror
1. Navigate to the target project
1. Add a new deploy key (under `Settings > Repository > Deploy Keys`)
   - Title: `full/path/to/project`
   - Key: The value copied in step 4
   - Grant write permissions to this key: checked
   - Expiration date (optional): leave it blank
1. Navigate to the source project
1. Force an update on the mirror (under `Settings > Repository > Mirroring repositories`)

## Common issues and troubleshooting

This is a living section that will have items added to it as needed.
