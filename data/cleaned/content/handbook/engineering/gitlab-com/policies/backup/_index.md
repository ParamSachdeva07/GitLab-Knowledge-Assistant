---
title: "Backups of GitLab.com"
description: "This policy specifies requirements for backups of GitLab.com"
controlled_document: true
tags:
  - security_policy
  - security_policy_caplscsi
---

{{< label name="Visibility: Audit" color="#E24329" >}}

## Purpose

This policy outlines how GitLab performs, monitors, and validates backups and restorations of GitLab.com.
These procedures are critical for ensuring data recovery and disaster recovery for customer data.

## Scope

GitLab.com's backup strategy includes both monitoring and restore validation.

Customer data is stored in the following locations:

1. All PostgreSQL databases for GitLab.com
1. Object storage for GitLab.com, including packages, LFS, uploads, and CI data
1. The CustomersDot database, which manages subscriptions and purchases
1. Git repositories

## Not in Scope

1. Customer Data stored in the Redis cache
   1. Data queued for processing
   1. Sessions and other cached data

## Roles & Responsibilities

| Role                      | Responsibility                                                                 |
|---------------------------|--------------------------------------------------------------------------------|
| GitLab Team Members       | Ensure adherence to the requirements outlined in this policy                   |
| Engineering (Code Owners) | Approve significant changes and exceptions to this policy                      |

## Procedure

GitLab defines:

- The services requiring backups
- The frequency of backups, data retention periods, and restoration processes
- The procedures for data restoration for Disaster Recovery scenarios

### Backup and Restore

#### PostgreSQL Databases

| Area                | Details                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Backup frequency    | A full backup is taken every hour, with continuous transaction log archival.                                      |
| Storage             | Stored in [GCS](https://cloud.google.com/storage)                                                                 |
| Encryption          | Backup data is encrypted in transit and at rest                                                                   |
| Retention           | 14 days (7 days for CustomersDot database)                                                                        |
| Loss prevention     | [Soft Delete](https://cloud.google.com/storage/docs/soft-delete) enabled, with 7 day retention                    |
| Location/redundancy | [Multi-region geo redundancy](https://cloud.google.com/storage/docs/availability-durability)                      |
| Monitoring          | All databases are continuously monitored to ensure successful backups, with alerts triggered for missing backups. |
| Restore validation  | Regular restoration from disk snapshots and replaying WAL segments                                                |

#### Git Repositories

| Area                | Details                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------- |
| Backup frequency    | Repositories are backed up hourly using block-level disk snapshots.                          |
| Storage             | Stored as GCP [Standard snapshots](https://cloud.google.com/compute/docs/disks/snapshots)    |
| Encryption          | Snapshots are encrypted at rest                                                              |
| Retention           | 14 days                                                                                      |
| Loss prevention     | Retained after source disk deletion                                                          |
| Location/redundancy | [Multi-region geo redundancy](https://cloud.google.com/storage/docs/availability-durability) |
| Monitoring          | All disks are monitored, with alerts triggered for missing snapshots                         |
| Restore validation  | Conducted by randomly sampling disks and restoring recent snapshots.                         |

#### Object Storage

Data stored in Object Storage (GCS) benefits from Google's [99.999999999% annual durability](https://cloud.google.com/storage/docs/storage-classes#descriptions) and multi-region bucket redundancy. To enhance data protection, [Object Versioning](https://cloud.google.com/storage/docs/object-versioning) and [Soft Delete](https://cloud.google.com/storage/docs/soft-delete) are enabled.

Automated restore validation is not required for Object Storage due to its inherent protections through versioning and soft delete.

## Exceptions

Exceptions to this policy will be managed in accordance with the [Information Security Policy Exception Management Process](/handbook/security/controlled-document-procedure/#exceptions).

## References

- [Records Retention & Disposal](/handbook/security/policies_and_standards/records-retention-deletion/)
- [Disaster Recovery runbooks](https://gitlab.com/gitlab-com/runbooks/-/tree/master/docs/disaster-recovery)
- [GameDays](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/disaster-recovery/gameday.md)
