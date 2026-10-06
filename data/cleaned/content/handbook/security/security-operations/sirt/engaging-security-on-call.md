---
title: Engaging the Security Engineer On-Call
description: How to Engage the Security Engineer On-Call
---

## Overview

The [Security Incident Response Team (SIRT)](/handbook/security/security-operations/sirt/) is on-call [24/7/365](/handbook/engineering/infrastructure-platforms/incident-management/on-call/#security-team-on-call-rotation) to assist with any security incidents. This handbook provides guidance to help identify the scope and severity of a potential security incident, followed by instructions on how to engage the Security Engineer On-Call (SEOC) if needed.

Information about SIRT responsibilities and incident ownership is available in the [SIRT On-Call Guide](/handbook/security/security-operations/secops-oncall/).

## Incident Severity

Before engaging the SEOC, please review [our severity levels](/handbook/security/security-operations/sirt/severity-matrix/) to ensure that the incident has been assigned the appropriate level of response.

For phishing related issues, see the [phishing](#phishing) section below. For other non-urgent issues, see the [low severity issues](#low-severity-issues) section.

Note: Additional information on Recovery Time Objective (RTO) and Recovery Point Objective (RPO) is available on the [BCP Handbook page](/handbook/business-technology/entapps-documentation/policies/gitlab-business-continuity-plan/)

The following items are out of scope for SIRT and should be escalated to the respective teams mentioned below:

- **Vulnerability reports and HackerOne**: please escalate to [Application Security](/handbook/security/engaging-with-security/#vulnerability-reports-and-hackerone)
- **Abuse reports and DMCA notices**: please escalate to [Trust & Safety](/handbook/security/security-operations/trustandsafety/)
- **General Customer Inquiries**: please escalate to [Field Security](/handbook/security/security-assurance/field-security/)

## Low Severity Issues

For general Q&A, GitLab Security is available in the `#security_help` channel in GitLab Slack.

For low severity, non-urgent issues, [SIRT](/handbook/security/security-operations/sirt/) can be reached by using the `@sirt-members` handle in Slack, `@sirt-oncall` to specifically request the Security Engineer On-call (SEOC) or by requesting the incident form link, using the `/security` slash command in Slack. (Note: this command does not work inside Slack threads)

Please be advised the SLA for Slack mentions is **6 hours** on business days.

## Phishing

If you suspect you've received a phishing email and have not engaged with the sender, please see: [What to do if you suspect an email is a phishing attack](/handbook/security/security-assurance/governance/phishing/#what-to-do-if-you-suspect-an-email-is-a-phishing-attack).

If you have engaged a phisher by replying to an email, clicking on a link, have sent and received text messages, or have purchased goods requested by the phisher, please [engage the SEOC](#engage-the-security-engineer-on-call).

## Engage the Security Engineer On-Call

If you have identified a security incident or you need immediate assistance from the SIRT:

- **Slack**: use the `/security` slash command

The Slack command triggers SIRT's Escalation Workflow. You will be sent a link to file a security incident using a Tines webform. This form asks questions about the incident that help the SIRT automatically determine the *severity*. You can optionally choose to send a page (Severity 1 & 2).

For more information on how the form is processed and labels are assigned, consult SIRT's [Security Incident Severity Matrix](/handbook/security/security-operations/sirt/severity-matrix/).

The workflow uses your answers to create an investigation, where the SEOC will determine if it needs to be escalated into an incident. Please provide as many details as possible when answering the open questions to aid the SEOC in their investigation.

For small requests like an indication if something is a security issue, questions on ongoing incidents or SIRT FYIs, team members can use the Slack handle:

- `@sirt-oncall`

This tags the current on call engineer.

If the security incident prevents you from accessing Slack:

- **Email**: send an email with a brief description of the issue to `panic@gitlab.com`

If paged, the SEOC will typically respond within **15 minutes** and may have questions which require synchronous communication from the incident reporter. It is important when paging the SEOC that the incident reporter be prepared and available for this synchronous communication in the initial stage of the incident response.
