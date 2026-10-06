---
title: "Disaster Recovery of GitLab.com"
description: "This policy specifies requirements for Disaster Recovery of GitLab.com"
controlled_document: true
---

{{< label name="Visibility: Audit" color="#E24329" >}}

## Purpose

GitLab continually assesses ways to improve recovery capabilities across the full platform to ensure that should a disaster occur, normal operations can be restored as quickly and with as little disruption as possible.

This policy outlines the current capabilities for responding to disaster scenarios for GitLab.com, how [GitLab.com backups](/handbook/engineering/gitlab-com/policies/backup/) are validated and tested for restoration, and how GitLab tests service recovery procedures in the unlikely event of a large-scale service disruption.

## Disaster Recovery

### Scope

GitLab.com's disaster recovery strategy encompasses the following components:

1. Regular validation and testing of restore procedures
2. Automated restore and validation of backups
3. Deployment across multiple data centers in `us-east1` to provide tolerance against localized disruptions

### Validation and Testing of Restore Procedures

Mock disaster recovery (DR) events, called Game Days, are conducted quarterly to simulate incidents affecting one or more services.
These exercises validate DR processes and assess readiness for actual incidents.

During these [Game Days](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/disaster-recovery/gameday.md), RTO and RPO targets are validated by [recording measurements for each procedure](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/disaster-recovery/recovery-measurements.md).

### Regional Recovery

All [GitLab.com backups](/handbook/engineering/gitlab-com/policies/backup/) are stored in multi-region object storage to ensure the capability to recover customer data in the unlikely event of a regional disaster.
Recovery from regional backups is validated through automated recovery and data validation processes described below.

### Automated restore testing and data integrity validation of backups

GitLab employs automated mechanisms to ensure data integrity of backups.

#### PostgreSQL

Daily restoration testing is performed for GitLab.com application databases in [CI pipelines](https://ops.gitlab.net/gitlab-com/gl-infra/data-access/durability/gitlab-restore/postgres-gprd/-/pipelines) (internal) using the [PostgreSQL Database Restore Validation](https://gitlab.com/gitlab-com/gl-infra/data-access/durability/gitlab-restore/postgres-gprd) project.
This process performs a point-in-time recovery (PITR) restore into a new instance and verifies data integrity by running queries on the restored database.
The same process is used for CustomersDOT database in [scheduled pipeline runs](https://ops.gitlab.net/gitlab-com/gl-infra/data-access/durability/gitlab-restore/postgres-prdsub/-/pipelines) (internal) in the [postgres-prdsub](https://gitlab.com/gitlab-com/gl-infra/data-access/durability/gitlab-restore/postgres-prdsub) project.

#### Gitaly Disk Snapshots

Hourly restoration testing is performed for Git repositories using a randomly selected Gitaly disk in [CI pipelines](https://ops.gitlab.net/gitlab-com/gl-infra/data-access/durability/gitlab-restore/gitaly-snapshot-verification/-/pipelines) (internal) via the [Gitaly snapshot verification](https://gitlab.com/gitlab-com/gl-infra/data-access/durability/gitlab-restore/gitaly-snapshot-verification) project.
This process takes a random Gitaly snapshot, restores it to a new disk, and verifies data integrity by checking for recent commits after restoration.

#### Object Storage

Automated restore validation is not required for Object Storage due to its inherent protections through versioning and soft delete.

### Multiple zone deployments

GitLab.com is deployed across multiple GCP availability zones in the `us-east1` region.
During short-term outages affecting a single zone within `us-east1`, unaffected zones will scale up to restore service.
For the Gitaly service, backup recovery will be necessary if data loss occurs.

## Exceptions

Exceptions to this policy will be managed in accordance with the [Information Security Policy Exception Management Process](/handbook/security/controlled-document-procedure/#exceptions).

## References

- [Backups](/handbook/engineering/gitlab-com/policies/backup/)
- [PostgreSQL Database Restore Validation Project](https://gitlab.com/gitlab-com/gl-infra/data-access/durability/gitlab-restore/postgres-gprd)
- [PostgreSQL Database Restore Validation Pipeline Runs](https://ops.gitlab.net/gitlab-com/gl-infra/data-access/durability/gitlab-restore/postgres-gprd/-/pipelines)
- [Gitaly snapshot verification Project](https://gitlab.com/gitlab-com/gl-infra/data-access/durability/gitlab-restore/gitaly-snapshot-verification)
- [Gitaly snapshot verification Project Pipeline Runs](https://ops.gitlab.net/gitlab-com/gl-infra/data-access/durability/gitlab-restore/postgres-prdsub/-/pipelines)
- [Records Retention & Disposal](/handbook/security/policies_and_standards/records-retention-deletion/)
- [Disaster Recovery runbooks](https://runbooks.gitlab.com/disaster-recovery/recovery/)
- [GameDays](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/disaster-recovery/gameday.md)
