---
title: 'Automated Dependency Updates ADR 002: Trigger via SBOM-ingestion scan profile'
description: 'Decision to trigger automated dependency updates via SBOM ingestion through a post-processing scan profile, rather than Continuous Vulnerability Scanning.'
---

## Context

The original proposal had `IngestCvsSliceService`, part of
[Continuous Vulnerability Scanning](https://docs.gitlab.com/user/application_security/continuous_vulnerability_scanning/)
(CVS), forward vulnerable components to `UpdateDependencyService` whenever a
CVS scan completed. This tied automated dependency updates to CVS's
advisory-driven scanning model: updates would only be considered when CVS
re-evaluated a project against newly disclosed advisories.

In practice, remediation needed to be tied to the same signal that dependency
scanning already produces for every pipeline: a project's SBOM. Coupling
remediation to CVS specifically would have made it depend on CVS's own
scanning cadence, and would not have reused the generic mechanism GitLab
already has for reacting to scan-profile-configured triggers.

## Decision

Automated dependency updates are triggered by **SBOM ingestion**, through a
**post-processing scan profile**, not by Continuous Vulnerability Scanning.

### Post-processing scan profiles

GitLab's `Security::ScanProfile` model supports two trigger families:

- **Pipeline-related triggers** (`default_branch_pipeline`,
  `merge_request_pipeline`), used by profiles that run as part of a CI
  pipeline.
- **Post-processing triggers** (`sbom_ingested`), used by profiles that react
  to data already ingested by GitLab, independent of any specific pipeline.

`Security::ScanProfileTrigger` validates that `sbom_ingested` may only be
used on post-processing profiles, and vice versa.

### Wiring for auto-remediation

Automated dependency updates rely on a single pairing: a
`dependency_scanning_post_processing` profile carrying the `sbom_ingested`
trigger. `DependencyManagement::SecurityUpdate::Eligibility` owns that
definition and the lookup for a given project. Both the automatic
`SchedulerService` and the user-triggered single-vulnerability remediation
flow gate on the same lookup, so the two stay consistent about when
remediation may run.

This means remediation fires whenever a project's dependency scan produces a
new SBOM, rather than waiting on a separate CVS scan cycle.

## References

1. `ee/app/models/dependency_management/security_update/eligibility.rb`
1. `ee/app/models/security/scan_profile_trigger.rb`
1. [001: Bounded, severity-prioritized remediation](./001_bounded_severity_prioritized_remediation.md)
