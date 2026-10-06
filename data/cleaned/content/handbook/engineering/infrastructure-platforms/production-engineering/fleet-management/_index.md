---
title: "Fleet Management Team"
description: "The Fleet Management team provisions, secures, and maintains the foundational infrastructure—including core Kubernetes clusters, VMs, standardized OS images, and primary Infrastructure-as-Code platforms that power GitLab's production environments."
---

Within Production Engineering, the Fleet Management team serves as GitLab's core infrastructure management unit. We provision, scale, and secure the foundational bedrock—encompassing core Kubernetes clusters, virtual machines, standardized OS images, and secrets management. By owning the low-level compute layer, we free our internal customers to focus entirely on building and deploying their services without friction.

## Mission

Our mission is to empower GitLab's teams to confidently build and deploy their services by providing a secure, smooth, and scalable core infrastructure.

## Ownership and Responsibilities

The Fleet Management team focuses on:

1. **Core Kubernetes Infrastructure:** Provisioning, scaling, and managing the health of GitLab's core GKE clusters.
2. **Kubernetes Workload Management:** Managing the tooling and platforms required to deploy workloads to our clusters (e.g., ArgoCD, Helmfile, Helm charts).
3. **Virtual Machine & OS Image Management:** Designing and maintaining the fleet-wide OS baselines, OS image systems, and managing large-scale VM migrations.
4. **Ops Infrastructure:** Owning and maintaining [ops.gitlab.net](https://ops.gitlab.net/) and its associated Ops runners.
5. **Secrets Management:** Owning and operating the foundational infrastructure for GitLab's secrets management (Vault).
6. **Infrastructure-as-Code (IaC) & Shared Tooling:** Maintaining the primary configuration repositories (e.g., `infra-mgmt`, core Chef, Terraform scaffolding) and shared CI templates (e.g., Common CI Tasks) to ensure standardized deployments.
7. **Cloud Vendors Engagement Management:** Managing relationships and engagements with cloud vendors to support our core fleet and infrastructure needs.

## Getting Assistance

- **Slack:** `[#g_fleet_management](https://gitlab.enterprise.slack.com/archives/C0ACE4T2R6W)`

## Common Links

| | |
|--------------------------------|---------------------------------------------------------------------------------------------------|
| **Workflow**                   | [Infrastructure Platforms Project Management](/handbook/engineering/infrastructure-platforms/project-management/) |
| **GitLab.com**                 | `@gitlab-org/production-engineering/fleet-management` |
| **Team Slack Channels**        | `[#g_fleet_management](https://gitlab.enterprise.slack.com/archives/C0ACE4T2R6W)` - Team channel |

## Team Members

{{< team-by-manager-slug manager="galon3" department="Production Engineering Fleet Management Team" >}}

## How We Work

We default to working inline with the [GitLab values](/handbook/values/), by following the processes of the wider [Infrastructure Platforms section](/handbook/engineering/infrastructure-platforms/project-management/). As a newly defined team, we are actively establishing and iterating on our workflows.

### Labels

- `~"Fleet::Requests"` - For incoming requests coming from outside the team.
- `~"Fleet::KTLO"` - For keeping the lights on (KTLO) issues and routine maintenance.
- `~"Fleet::Project Work"` - For issues that are part of planned epics and roadmap initiatives.
- `~"Fleet::Meta"` - For issues related to team processes (retrospectives, planning, etc.).

### Meetings and Rituals

- **Weekly Team Sync:** We follow a 3-week rotating schedule to accommodate our globally distributed team across APAC, EMEA, and AMER. Each week, two regions overlap for a 45-minute sync covering team connection, async catch-up from the missing region, process iteration, and a Show & Tell session. Members who cannot attend are encouraged to participate asynchronously via a shared agenda doc.
- **Group Reviews:** We review project status asynchronously every Wednesday to ensure alignment ahead of the Production Engineering group review.
- **Retrospectives:** A team-level retrospective issue is created regularly to reflect on our processes and encourage a culture of continuous improvement.
- **On-Call:** Most team members participate in the on-call rotation as part of our commitment to the reliability of the infrastructure we own.

### Infradev Workflow

We use the following workflow to triage [infradev](/handbook/engineering/workflow/#infradev) issues assigned to Fleet Management. This workflow is proposed and we expect to iterate on it as we learn what works.

1. **Auto-assignment in triage state:** When a new infradev issue is routed to our team, [triage-ops](https://gitlab.com/gitlab-org/quality/triage-ops) automatically assigns every team member to the issue, signaling it is in the triage state.
2. **Collaborative triage:** Anyone on the team can triage the issue. The goal is to confirm:
   1. The issue makes sense and has enough context to act on.
   1. Fleet Management is the right team to own it.
   1. The priority label is appropriate.
   1. The due date is realistic.
3. **Ready for work:** Once the issue passes triage, we unassign all team members and apply the `~"workflow-infra::ready"` label to move it into the ready queue.
4. **Pulling from the ready queue:** Team members pull from the ready queue as capacity allows. When a due date is approaching, a bot may randomly assign an issue to a team member to ensure nothing slips.
