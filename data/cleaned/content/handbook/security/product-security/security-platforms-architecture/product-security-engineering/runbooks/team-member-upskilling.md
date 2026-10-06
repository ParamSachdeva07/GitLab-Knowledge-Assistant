---
title: "Team Member Upskilling"
---

## Team Member Upskilling Runbook

This runbook is a collection of resources for new or existing Product Security Engineers, or for those looking to build a body of work to enhance their skills and knowledge in product security. This runbook is designed to provide guidance and resources for continuous learning and professional development.

### 1. Core Competencies

Team members should work to become proficient in the following core competencies:

- Web application security
- Secure coding practices
- Threat modeling
- Risk assessment and management
- Internal security team functions and their purposes, such as Vulnerability Management and Product Security Incident Response

Team members should also have 'good' knowledge of the following areas; enough to know how to go and learn more should the need arise:

- Cloud / network security
- Cryptography

### 2. Learning Paths

These learning paths are designed to help new team members in Product Security Engineering get up to speed and make meaningful contributions. They provide a balance of quick wins and longer-term skill development, focusing on core competencies essential to our mission. Choose one or more paths that align with your interests and the team's current priorities.

#### 1. "Paved Road & Defense-in-Depth" Learning Path

Essential:

- [ ] Analyze a historic GitLab vulnerability (from release posts or our [internal](https://internal.gitlab.com/handbook/security/product_security/application_security/reproducible-vulnerabilities/) or [public Reproducible Vulnerabilities page](/handbook/security/product-security/security-platforms-architecture/application-security/reproducible-vulnerabilities/))
- [ ] Design a solution that makes it easier for developers to avoid this class of bug ("paved road"), and/or prevents or mitigates the class of bug (defense-in-depth)
- [ ] Document your solution design in an [issue](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/product-security-engineering-team/-/issues/new) (and/or epic & child items)
  - Have the solution peer reviewed by a teammate
  - Iteratively [refine it](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/detailed-workflow/#refinement-and-planning) until it's in the `~workflow::ready for development` state

Recommended:

- [ ] [Add it to a milestone](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/detailed-workflow/#milestone-planning) and implement your solution
- [ ] Reproduce a historic vulnerability on a local version of GitLab
- [ ] [Create a threat model](/handbook/security/product-security/security-platforms-architecture/application-security/threat-modeling/) that encompasses the vulnerability you chose
- [ ] Compare your designed solution to our actual patches and defense-in-depth measures

#### 2. "Secure GitLab with GitLab" Learning Path

Essential:

- [ ] Identify an existing issue off our issue board or select a ~ProdSecEngCandidate issue which will help one of the Product Security teams better secure GitLab (the org) _with_ GitLab (the product)
- [ ] Document your solution design in an [issue](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/product-security-engineering-team/-/issues/new) (and/or epic & child items)
  - Have the solution peer reviewed by a teammate
  - Iteratively [refine it](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/detailed-workflow/#refinement-and-planning) until it's in the `~workflow::ready for development` state

Recommended:

- [ ] [Add it to a milestone](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/detailed-workflow/#milestone-planning) and implement your solution
- [ ] Conduct a post-implementation review and propose improvements
- [ ] Collaborate with the Application Security team to identify other high-impact automation opportunities

#### 3. "Security Upskilling and Collaboration" Learning Path

Essential:

- [ ] Review the following and identify areas that you want to learn more about:
  - [ ] GitLab's [Secure Code Guidelines](https://docs.gitlab.com/ee/development/secure_coding_guidelines.html)
  - [ ] GitLab's [Security Risk Quarterly](/handbook/security/security-assurance/security-risk/storm-program/#risk-tracking-and-reporting)
- [ ] Create an issue or epic to track your learning efforts. Include:
  - [ ] Type of training / URL(s)
  - [ ] Your goal, estimated effort, & milestone
  - [ ] Links to G&D issues if you need to apply for budget (certifications, online courses, etc)

Recommended:

- [ ] Update this page with resources or processes you found helpful!

#### 4. "Understanding Internal Security Team Functions" Learning Path

ProdSecEng builds tools, automation, and paved roads for other Product Security teams. To make good engineering decisions (what to build, how to scope it, what trade-offs matter) you need to understand what these teams do day-to-day, what processes they follow, and why. 

The goal of this path is to build enough fluency that you can ask good clarifying questions when one of these teams brings ProdSecEng a tooling request.

**Essential:**

- [ ] Read the [Product Security overview](/handbook/security/product-security/) to see how the teams in the department fit together
- [ ] Read the [Product Security Engineering](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/) team charter to understand ProdSecEng's mission, scope, and operating model
- [ ] Skim each of the following team pages and note what kinds of work they do:
  - [ ] [Application Security (AppSec)](/handbook/security/product-security/security-platforms-architecture/application-security/) - reviews code, threat-models features, and triages vulnerabilities reported through HackerOne
  - [ ] [PSIRT](/handbook/security/product-security/psirt/) - handles vulnerability reports, coordinates remediation, and runs the security release process
  - [ ] [Vulnerability Management](/handbook/security/product-security/vulnerability-management/) - tracks vulnerabilities across GitLab's products and infrastructure to closure
  - [ ] [Security Platforms & Architecture (SPA)](/handbook/security/product-security/security-platforms-architecture/) - ProdSecEng's own sub-department
  - [ ] [Infrastructure Security](/handbook/security/product-security/infrastructure-security/) - secures GitLab's production infrastructure
  - [ ] [Data Security](/handbook/security/product-security/data-security/) - protects customer and corporate data
  - [ ] [Supply Chain Risk Management](/handbook/security/product-security/supply-chain-risk-management/) - addresses risks from third-party dependencies and the software supply chain
- [ ] For each team above, identify a ProdSecEng-maintained tool that may support their work (the [tooling inventory in the internal handbook](https://internal.gitlab.com/handbook/security/product_security/product_security_engineering/) lists each tool's stakeholder)
- [ ] Read the [ProdSec-to-Product workflow](/handbook/security/product-security/security-platforms-architecture/security-interlock/prodsec-to-product-workflow/) to see how ProdSecEng turns requests from these teams into product features

**Recommended:**

- [ ] Sit in on a meeting from one of the teams ProdSecEng builds for (e.g., AppSec triage, PSIRT sync) to see how they actually use the tooling
- [ ] Pick one ProdSecEng-maintained tool and trace it end-to-end: read the project README, look at recent issues, and see which stakeholder team filed them
