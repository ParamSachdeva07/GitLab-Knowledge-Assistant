---
title: 'Automated Dependency Updates ADR 004: Package release cooldown'
description: 'Decision to add a configurable cooldown period before automated dependency updates will propose a newly published package version, to reduce supply-chain risk.'
---

## Context

Automatically bumping a dependency to the newest available version as soon
as it's published carries supply-chain risk: a just-published package
version has had the least time for the community to notice if it's
malicious, compromised, or simply broken. The original design doc didn't
address this; it focused on bounding *how many* MRs get opened and in what
order ([001](./001_bounded_severity_prioritized_remediation.md)), not on
*which* versions are safe to propose.

## Decision

We added a **cooldown period**: a minimum number of days a package version
must have been publicly available before automated dependency updates will
propose it.

The cooldown is a field on the `auto_remediation` section of a project's
remediation scan profile configuration, defaulting to seven days, and is
customer-configurable within a validated range.

The monolith does not act on the cooldown itself. It passes the configured
value through to the update orchestrator as part of the job payload, and the
orchestrator is responsible for excluding any package version
younger than the cooldown window when resolving the target version for an
update.

This is a sibling safeguard to the open-MR rate limit: the rate limit caps
*volume*, the cooldown constrains *freshness*. Both exist to reduce risk
introduced by the automation itself, rather than risk already present in the
dependency tree.

## References

1. `ee/app/services/dependency_management/security_update/job_builder.rb`
1. `ee/app/models/security/scan_profiles/configuration/defaults/dependency_scanning_post_processing.rb`
1. [001: Bounded, severity-prioritized remediation](./001_bounded_severity_prioritized_remediation.md)
1. [005: Refresh open merge requests instead of rebasing them](./005_refresh_instead_of_rebase.md)
