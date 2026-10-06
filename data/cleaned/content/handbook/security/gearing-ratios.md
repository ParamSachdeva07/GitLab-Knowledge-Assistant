---
title: "Security Department Gearing Ratios"
description: Gearing ratios are used as [Business Drivers](/handbook/finance/financial-planning-and-analysis/) to forecast long term financial goals by function.
---

## Bug bounties

The gearing ratio for bug bounty expenditure is as follows:

- The cost of a compromise is estimated at 1% of company worth
- Bug Bounty budget is determined as 10% of a compromise
- Bug Bounty top reward is determined as 1% of budget

An illustration:
GitLab is worth 3.5 billion and a significant compromise can cost GitLab $35 million.
10% ratio = $3.5 million budget. Likewise, 1% of budget = $35,000 top reward

Approximate monthly budget should be set at total budget divided by 12. It should be understood that our bug bounty payouts are largely unpredictable and fluctuate based on the following:

- Number and severity of bugs produced by GitLab and pushed to production
- Participation of research community
- Reward ranges

This gearing ratio is owned by the [Product Security](/handbook/security/product-security/) Sub-department. The cost of a compromise should be re-evaluated at least annually based on the average market cap of GTLB over the previous 6 months.

## Security Incident Response Team (SIRT) size

SIRT is the sole carrier of the Security On-Call (SEOC) rotation, which ensures that there's a page-able Security Engineer 24/7/365. The baseline and gearing ratio for the size of the SIRT [have been agreed on](https://gitlab.com/gitlab-com/www-gitlab-com/-/issues/9711#note_450845141) as outlined below:

- Baseline:
  - 12 team members to cover 3 timezone in a 8 hour, follow-the-sun rotation:
    - 4 team members in JAPAC
    - 4 team members in EMEA
    - 4 team members in AMER

- Gearing ratio that triggers a review of team size:
  - If number of pages to SEOC per month exceeds +50% of monthly average of the last 12 months for 3 consecutive months
  - If number of pages to SEOC per year exceeds +100% of previous year
  - If number of total team members increases by +20% compared to previous year

This gearing ratio is owned by the [Security Operations](/handbook/security/security-operations/) Sub-department.

## Security Compliance Team Staffing

The weighted gearing ratio for Security Compliance team size accounts for
certification complexity:

**Certification Complexity Weighting:**

- High Complexity (2.0 FTE): FedRAMP, DoD
- Medium Complexity (1.0 FTE): ISO standards, PCI DSS, ISMAP, IRAP, CMMC  
- Standard Complexity (0.5 FTE): SOC 2, TISAX, Cyber Essentials

**Formula**: Required FTE = Σ(Active Certifications × Complexity Weight) +
1 Core Operations Staff

This ratio should be re-evaluated when:

- Adding certifications that introduce new geographic or regulatory domains
- Certification requirements significantly change
- Automation capabilities reduce manual effort by >30%

This gearing ratio is owned by the Security Compliance team and should be
re-evaluated annually during budget planning.

## Security Compliance External Audit Budget

Annual audit budget is tiered based on certification complexity and requirements:

**Budget Tiers:**

- Tier 1 ($200-300K): FedRAMP, DoD, ISMAP
- Tier 2 ($100-150K): ISO 27001, IRAP, CMMC
- Tier 3 ($50-75K): SOC 2, PCI SAQ, TISAX, ISO, Cyber Essentials

Budget should include 10% contingency for scope changes and remediation
validation audits.

This gearing ratio is owned by the Security Compliance team and should be
re-evaluated annually during budget planning.
