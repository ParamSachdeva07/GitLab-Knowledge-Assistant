---
title: "Availability Measurement for GitLab SaaS Services"
description: "This policy specifies how availability is measured for GitLab.com, GitLab Dedicated and GitLab Dedicated for Government"
controlled_document: true
---

## GitLab Service Level Agreement - Availability Definition

The following service level agreement applies to SaaS Software purchased or renewed as Ultimate tier on or after 2026-01-01.

### Service Availability Commitment

GitLab commits to make the [Covered Experiences](#covered-experiences)
available with a Monthly Uptime Percentage of at least **99.9%** during each calendar month.

### Covered Experiences

The following GitLab features and services are covered under this SLA ("Covered Experiences"):

1. Issues and Merge Requests
1. Git Operations (push, pull, clone via HTTPS and SSH)
1. Container Registry operations
1. Package Registry operations
1. API Requests (limited to the above Covered Experiences only)

### Downtime Minute Definition

A **"Downtime Minute"** occurs when:

The Service experiences degraded availability, meaning **5% or more** of [Valid Customer Requests](#valid-request-definition)
to [Covered Experiences](#covered-experiences) in a given minute result in server errors
(defined as HTTP `5xx` status codes or connection timeouts exceeding 30 seconds)
as determined by GitLab's internal and external monitoring systems.

Downtime Minutes do not include any [Excluded Minutes](#excluded-minutes) as defined in this document.

### Valid Request Definition

**"Valid Request"** means a request that meets all of the following criteria:

1. **Properly authenticated and authorized** - The request includes valid authentication
   credentials and the user has appropriate permissions for the requested operation

1. **Correctly formed** - The request:
   1. Uses documented API endpoints, parameters, and methods
   1. Follows GitLab's published API specifications and documentation
   1. Contains syntactically correct Git commands (for Git operations)
   1. Includes required headers and properly formatted request bodies

1. **Within usage limits** - The request:
   1. Does not exceed documented rate limits
   1. Does not exceed size limits (e.g., file size, repository size, payload size)
   1. Originates from non-blocked IP addresses or users
   1. Complies with fair use policies

1. **Non-malicious** - The request:
   1. Does not attempt to exploit security vulnerabilities
   1. Does not contain malicious code or payloads
   1. Is not part of a DDoS or other attack pattern
   1. Does not attempt to circumvent access controls

1. **Supported operations** - The request:
   1. Targets features included in the customer's subscription tier
   1. Uses generally available features (not experimental/beta)

The following are excluded from Valid Requests:

1. Requests that receive HTTP `4xx` errors due to client-side issues
1. Requests to deprecated API endpoints after the deprecation date
1. Requests from automated testing or monitoring tools not operated by GitLab
1. Preflight/OPTIONS requests
1. Health check or status endpoint requests

### Excluded Minutes

The following minutes are excluded from being counted as Downtime Minutes:

1. Scheduled Maintenance windows
1. Emergency maintenance necessary to address critical security or data integrity issues
1. Force Majeure events or general Internet connectivity issues
1. Issues caused by Customer's use of the Service in violation of the Terms of Service
1. Issues caused by equipment, software, or services not provided or controlled by GitLab
1. Features or services explicitly labeled as Alpha, Beta, or Preview

### Calculating Monthly Uptime Percentage

**"Monthly Uptime Percentage"** is calculated as:

```math
\text{Monthly Uptime Percentage} = \frac{\text{Total Minutes in Month} - \text{Downtime Minutes}}{\text{Total Minutes in Month}} \times 100
```

Where:

- **"Total Minutes in Month"** = Total number of minutes in the calendar month
- **"Downtime Minutes"** = Total number of minutes in a calendar month when
  Covered Experiences met the Downtime Minute definition,
  excluding any Excluded Minutes

### Service Credits

If the Monthly Uptime Percentage falls below 99.9%, GitLab Ultimate tier Customers may request (defined below) Service Credits according to:

| Monthly Uptime Percentage | Service Credit |
| ---- | ---- |
| 99.5% - <99.9% | 5% of monthly fees |
| < 99.5% | 10% of monthly fees |

### Credit Request Process

To receive a Service Credit, an eligible customer must:

- Submit a Support request at [support.gitlab.com](https://support.gitlab.com) within thirty (30) days after the end of the affected month;
- Include all relevant information about when the SaaS Service was unavailable; and
- Provide reasonable detail about the attempted access to Covered Experiences

Once received, GitLab will then verify the claim against its own internal monitoring data and, if validated, issue Service Credits against Customer’s next issued invoice. In no event shall an issued Service Credit result in a refund of Fees to Customer.

### Credit eligibility

Raise a request through [support.GitLab.com](https://support.gitlab.com) to check if you are eligible for credits caused by downtime.

## Hosted Runners for GitLab Dedicated Service Level Agreement - Availability Definition

This service level agreement applies only to eligible customers using hosted runners for GitLab Dedicated.
It does not apply to GitLab-hosted runners on GitLab.com or to GitLab Dedicated for Government.

This service level agreement is separate from the service level agreement for a customer's GitLab
Dedicated instance.
Downtime for hosted runners for GitLab Dedicated does not count as downtime for the GitLab Dedicated instance.

### Service Availability Commitment for Hosted Runners

GitLab commits to make hosted runners for GitLab Dedicated available with a Monthly Uptime Percentage of at least
**99.9%** during each calendar month.
Monthly Uptime Percentage is calculated separately for each GitLab Dedicated tenant and includes all stacks of
hosted runners for GitLab Dedicated deployed for that tenant.

### Downtime Minute Definition for Hosted Runners

A **"Downtime Minute"** occurs when hosted runners for GitLab Dedicated experience degraded availability, meaning
**5% or more** of [Valid Jobs](#valid-job-definition-for-hosted-runners) that enter the pending state during that
minute do not enter the running state on a hosted runner for GitLab Dedicated within five minutes.

Jobs for a runner stack are excluded from the SLA calculation when the stack meets or exceeds the documented
[runner stack concurrency limit](https://docs.gitlab.com/administration/dedicated/hosted_runners/#plan-runner-stack-concurrency).

Downtime Minutes do not include any [Excluded Minutes](#excluded-minutes-for-hosted-runners) as defined in this
document.

### Valid Job Definition for Hosted Runners

A **"Valid Job"** is a CI/CD job that meets all of the following criteria:

1. The job is submitted by an authorized user or process in the GitLab Dedicated tenant.
1. The job is eligible to run on at least one stack of hosted runners for GitLab Dedicated deployed for the tenant,
   including matching supported runner tags and capabilities.
1. The job complies with documented usage limits.
1. The GitLab Dedicated tenant has enough allocated compute minutes for the job.
1. The job uses features of hosted runners for GitLab Dedicated that are generally available.
1. The job is not malicious and does not attempt to circumvent access controls or exploit security
   vulnerabilities.

### Excluded Minutes for Hosted Runners

The following minutes are excluded from being counted as Downtime Minutes:

1. Scheduled maintenance windows that affect hosted runners for GitLab Dedicated.
1. Emergency maintenance necessary to address critical security or data integrity issues.
1. Force Majeure events or general Internet connectivity issues.
1. Issues caused by the customer's use of hosted runners for GitLab Dedicated in violation of the Terms of Service.
1. Issues caused by equipment, software, services, or configurations not provided or controlled by GitLab.
1. Features or services explicitly labeled as Alpha, Beta, or Preview.

### Calculating Monthly Uptime Percentage for Hosted Runners

**"Monthly Uptime Percentage"** is calculated as:

```math
\text{Monthly Uptime Percentage} = \frac{\text{Total Minutes in Month} - \text{Downtime Minutes}}{\text{Total Minutes in Month}} \times 100
```

Where:

1. **"Total Minutes in Month"** = Total number of minutes in the calendar month.
1. **"Downtime Minutes"** = Total number of minutes in a calendar month when hosted runners for GitLab Dedicated
   met the Downtime Minute definition, excluding any Excluded Minutes.

### Service Credits for Hosted Runners

If the Monthly Uptime Percentage falls below 99.9%, eligible customers may request Service Credits according to:

| Monthly Uptime Percentage | Service Credit |
| --- | --- |
| 99.5% - <99.9% | 5% of the monthly commitment for hosted runners for GitLab Dedicated |
| <99.5% | 10% of the monthly commitment for hosted runners for GitLab Dedicated |

### Credit Request Process for Hosted Runners

To receive a Service Credit, an eligible customer must:

1. Submit a Support request at [support.gitlab.com](https://support.gitlab.com) within thirty (30) days
   after the end of the affected month.
1. Include all relevant information about when hosted runners for GitLab Dedicated were unavailable.
1. Provide reasonable detail about the attempted use of hosted runners for GitLab Dedicated.

Once received, GitLab will verify the claim against its internal monitoring data and, if validated,
issue Service Credits against the customer's next issued invoice.
In no event shall an issued Service Credit result in a refund of fees to the customer.

### Credit Eligibility for Hosted Runners

Raise a request through [support.gitlab.com](https://support.gitlab.com) to check if you are eligible for
credits caused by downtime.
