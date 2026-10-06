---
title: "GitLab University"
description: "An overview of GitLab University, the free on-demand learning platform for customers, partners, and team members — including what it offers, who owns it at GitLab, and where to get help."
---

## Overview

GitLab University (GLU) is GitLab's learning platform for customers, partners, community members, and GitLab team members to access self-paced, on-demand training and certifications. It helps scale customer enablement, reduce repetitive support questions, and drive product adoption through structured learning paths, hands-on labs, and assessments.

GLU offers content ranging from short videos and one-page guides to curated multi-course learning paths. The majority of content is free, with paid options for certifications and instructor-led training. 

**Platform:** GitLab University is powered by [Thought Industries (TI)](https://www.thoughtindustries.com), GitLab's learning management system (LMS).

There are two ways customers access GitLab University:

- **Public GitLab University** — free, open to anyone with an email address at [university.gitlab.com](https://university.gitlab.com).
- **GitLab University Enterprise / Panoramas** — a dedicated portal for a specific customer's organization, included with the Signature Success tier. See [GitLab University Enterprise](#gitlab-university-enterprise) below.

For CSM enablement resources and talk tracks, see the [GitLab University Hub on Highspot](https://gitlab.highspot.com/items/6989f5ddcf54691b21cef407?lfrm=srp.5).

---

## What GitLab University Offers

| Format | Description | Cost |
|---|---|---|
| Self-paced courses & learning paths | On-demand content covering the full DevSecOps lifecycle; anyone can register with an email address | Free |
| Events & webinars | Live sessions on curated topics hosted by GitLab customer success team members | Free |
| Certifications | 50-question exam + digital Credly badge; prep resources included. See [university.gitlab.com/pages/certifications](https://university.gitlab.com/pages/certifications) for current offerings | $150 each |
| Public instructor-led training | Scheduled live sessions delivered over two days with hands-on labs. See [university.gitlab.com/pages/public-training](https://university.gitlab.com/pages/public-training) | $750/seat |

**GitLab team members** access GLU via the GitLab University tile in Okta. All certifications are free for team members.

**Partners** access GLU through the Impartner portal.

---

## Ownership & Operating Model

### Platform & Tooling

| Role | Owner | Scope |
|---|---|---|
| DRI — Platform & Tooling | Neil Frye, Senior Manager, CX Platform Engineering | GLU platform roadmap, integrations, Panorama / Enterprise portal architecture |
| GLU Platform Manager | Kim Hokanson | Day-to-day platform operations, vendor relationship with Thought Industries, GLU roadmap inputs from CS and Education Services |
| Frontend Engineer | Priscilla Luong | Frontend engineering and panorama deployment tooling alongside CX Platform Engineering |

### Content & Curriculum

**Education Services / Curriculum Development** owns the course catalog, certifications, and learning paths on GLU. They partner with CX Platform Engineering on platform capabilities such as new content types, reporting, and attribution.

### Customer-Facing Adoption & Enablement

**CSMs / CSAs / Digital Success** are responsible for positioning GLU as the primary self-paced enablement channel in customer journeys — across onboarding, expansion, and success plans. They identify panorama opportunities for Signature Success customers, submit intake requests, and own the business relationship through rollout.

---

## Where to Ask Questions

| Channel | Use For |
|---|---|
| Slack `#education_services` | Panorama / Enterprise questions, SSO configuration, customer-specific enablement workflows |
| Slack `#learninganddevelopment` | Internal L&D questions, LevelUp vs. GLU, general learning programs |
| Slack `#gitlab-university-internal` | Field feedback, experiences, and suggestions |
| `university@gitlab.com` | Customer-facing support — GLU platform issues and learner help |

---

## GitLab University Enterprise

### What It Is

GitLab University Enterprise is a dedicated, managed portal included with the Signature Success tier. Internally, each customer-dedicated portal is referred to as a **GitLab University panorama**.

Panoramas draw from the same content available on the public platform. Customers can also upload their own learning materials to be hosted alongside GitLab University content. The key differences from the public platform are:

- **SSO integration** (optional) — the portal can be connected to an identity provider the customer already uses, such as Okta or Microsoft. By default, users join via a registration code.
- **Customer content hosting** — customers can upload their own learning assets alongside standard GitLab University courses.
- **Customer-specific reporting** — reports covering enrollments, completions, active users, and certification utilization for the organization accessible to designated individuals.
- **Elevated permissions** — designated customer members can be granted portal admin rights to manage users, or reporting-only access to view completion and engagement data.

**Entitlement:** Panoramas are included with the Signature Success tier. 

### How to Request a Panorama

All Panorama requests must be submitted via the CX intake request form. The full workflow is documented on the [GLU Panorama handbook page](/handbook/customer-experience/success-services/glu-panorama/).

At a high level, the process is:

1. **Confirm the customer is on Signature Success** 
2. **Align with the customer on scope** — SSO vs. registration codes, any customer-specific content to host, which members need admin or reporting access, and their internal rollout plan.
3. **Submit the CX intake request form** — follow the [GLU Panorama handbook workflow](/handbook/customer-experience/success-services/glu-panorama/) for the full steps.
4. **The GitLab University team provisions the portal** — they create it in Thought Industries and, if SSO is needed, coordinate a ~30-minute configuration call with the customer's IT contact.
5. **Permissions are configured** — admin and reporting access is assigned to the appropriate customer members. The CSM owns the business relationship and rollout with the customer.

### Who Does What

**CSM / CSA responsibilities:**

1. Confirm the customer is on Signature Success before beginning the panorama request process.
2. Submit the CX intake request form, following the [GLU Panorama handbook workflow](/handbook/customer-experience/success-services/glu-panorama/).
3. Own the business conversation, set expectations, and manage the customer's internal rollout plan.
4. Use the [GitLab University Hub on Highspot](https://gitlab.highspot.com/items/6989f5ddcf54691b21cef407?lfrm=srp.5) for positioning guidance.

**CX Platform Engineering & Education Services responsibilities:**

1. Provision the Panorama — review intake request, validate entitlement, create in Thought Industries.
2. Configure SSO — coordinate a 30-minute config call with the customer's IT contact.
3. Set up reporting & admin access — assign portal admin roles, confirm dashboard access.
4. Load customer-specific content (optional) — upload customer-provided learning assets.
5. Ongoing platform support — manage escalations to Thought Industries, coordinate resolution via `university@gitlab.com`.

**Customer admin responsibilities:**

1. Own internal rollout and communications — who should enroll, when, and how.
2. Manage user invitations and any SSO communication within their organization.
3. Monitor engagement and completion reports inside the portal.

---
