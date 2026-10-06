---
title: "GitLab for Open Source Program Workflows"
description: "Details on program-specific workflows related to the GitLab for Open Source Program"
---

## Overview

This page contains details regarding workflows specific to the [GitLab for Open Source Program](https://about.gitlab.com/solutions/open-source/).
Because the GitLab for Open Source Program is part of GitLab's [Developer Relations Programs](/handbook/marketing/developer-relations/programs/), team members verify applications by using the team's standard, seven-step application workflow.
See [the handbook page](/handbook/marketing/developer-relations/programs/program-resources/#automated-application-workflow) on that workflow for details that pertain to all GitLab community programs.

## Program application form

GitLab Customers Portal contains the application form to request a GitLab for Open Source license.
The workflow in this form is divided into two types of submission:

### An open source project is located on GitLab.com

Applicants select a namespace that contains the project and check the program agreement. After pressing the submit button, namespace verification starts to make sure that it meets basic program requirements:

* Each project inside the namespace includes an [OSI-approved open source license](https://opensource.org/licenses).
* Namespace includes at least 1 public project.
* Namespace includes at most 1 private project.

Once the check is passed, the customer receives an email with further instructions.
For more information about the check for an OSI-approved license [see GitLab Docs](https://docs.gitlab.com/ee/subscriptions/community_programs.html#gitlab-for-open-source).

### An open source project is located on a Self-managed instance

Applicants **must explain why they need a self-managed solution** instead of using GitLab.com. They must also provide basic information about their project and a publicly accessible link to the namespace. Applicants receive a response within five business days.

The form also includes the following statement, added with help from the GitLab Legal team:

> I certify that the project maintainers are not seeking to make profit from this project by, for example, selling services or higher tiers. Make sure your use case qualifies.

For reasons relating to trade controls, we are unable to accept applicants from Cuba, Iran, Syria, North Korea, Russia, Belarus, or Ukraine.

## Verifying applicants

Eligibility requirements for the GitLab for Open Source Program are listed in the [program's handbook page](/handbook/marketing/developer-relations/programs/open-source-program/).
The application form performs basic alignment checks for program applications.

Verification flow for projects located on GitLab.com (SaaS) is fully automated. However, the team still needs to process the [Verification phase](/handbook/marketing/developer-relations/programs/program-resources/#verification) for Self-managed applications manually.
The Self-managed workflow requires an application processing team until further automation is implemented.

If the namespace does not qualify for the program, the team will send the applicant a rejection email that follows [the team's correspondence template](https://gitlab.com/gitlab-com/marketing/developer-relations/strategy-programs/operations/-/tree/main/support-macros/opensource).
Applicants can then contact `opensource@gitlab.com` if they believe the rejection was sent in error, or if they have additional questions about eligibility.

## Verification limit

Any individual can apply and reapply through the GitLab Customers Portal form until verification succeeds. For the Self-managed use case, an applicant can send a request once per day.
This limit provides room for error and allows a single individual to apply for licenses on behalf of multiple open source projects.
It can be changed at any time.
