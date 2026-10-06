---
title: Security Factory Stage
description: >-
  The Security Factory stage builds the scanning, detection, and remediation
  engines of the GitLab security portfolio, from analyzers through vulnerability
  management and threat research.
---

The Security Factory engineering stage owns the engines that find, explain, and help fix
security problems in customer code: the analyzers, the detection rules, the vulnerability
management surface, and the research that feeds them.

This stage was formed in the FY27 Sec reorg from the former Application Security Testing
stage plus the Security Insights and Security Infrastructure groups.

## Leadership

| Role | Person |
| --- | --- |
| Stage lead | Maw Wildpaner (`@maw`, interim) |
| Principal Engineer | Isaac Dawson (`@idawson`) |
| Principal Engineer | Lucas Charles (`@theoretick`) |
| Principal Engineer | Meir Benayoun (`@mbenayoun`) |

## Teams

| Group | Engineering Manager | Tech Lead | Label |
| --- | --- | --- | --- |
| [Secret Detection](secret-detection/) | Amar Patel (`@amarpatel`) | Ahmed Hemdan (`@ahmed.hemdan`) | `group::secret detection` |
| [Composition Analysis](composition-analysis/) | Ethan Feller (`@efeller`) | Nick Ilieskou (`@nilieskou`) | `group::composition analysis` |
| [Code Scanning](code-scanning/) | Ethan Feller (`@efeller`) | Yoric Teller (`@yteller`) | `group::code scanning` |
| [Code Security](code-security/) | Ethan Feller (`@efeller`) | Philip Cunningham (`@philipcunningham`) | `group::code security` |
| [AI Security](ai-security/) | To be determined | Mher Tolpin (`@mtolpin`) | `group::ai security` |
| [Vulnerability Management](vulnerability-management/) | AJ Biton (`@ajbiton`) | Lorenz van Herwaarden (`@lorenzvanherwaarden`) | `group::vulnerability management` |
| [Agentic Security Flows](agentic-security-flows/) | AJ Biton (`@ajbiton`) | Savas Vedova (`@svedova`) | `group::agentic security flows` |
| [Threat Research](threat-research/) | Daniel Abeles (`@dabeles`) | Dinesh Bolkensteyn (`@dbolkensteyn`) | `group::threat research` |
| [Security Foundations](security-foundations/) | Ryan Wells (`@ryaanwells`) | Gregory Havenga (`@ghavenga`) | `group::security foundations` |

Group membership is sourced from Workday and published on the
[product categories page](/handbook/product/categories/#sec-section).

## Labels

Work in this stage carries the `devops::security factory` stage label plus the owning
group's `group::` label. Both are scoped labels and exist in the `gitlab-org` and
`gitlab-com` top-level groups.

## Slack

- [`#sec-security-factory-eng`](https://gitlab.enterprise.slack.com/archives/C07QX7Y63HQ) - stage engineering channel.

Per-group channels are listed on each group page. Several channel renames are still in
progress, tracked in
[Sec reorg issue 2](https://gitlab.com/gitlab-org/software-supply-chain-security/reorg-act2-2026-06/-/issues/2).

## Stage resources

1. [Planning](planning/)
1. [QA process](qa_process/)
1. [Products and metrics](products/)
1. [Technical documentation](tech-docs/)
1. [Tutorial: add observability metrics to a CI-based analyzer](analyzer-observability-metrics/)
