---
title: GitLab University Panorama
description: Complete workflow for requesting, setting up, and managing GitLab University Panorama dedicated learning portals for customers with Signature Success Tier.
---

## What is a GitLab University Panorama?

[GitLab University](https://university.gitlab.com/) is free and open to all customers for self-serve learning. **GitLab University Enterprise** is a dedicated, managed portal included with the **Signature Success Tier** or available for separate purchase through Education Services. Internally, we refer to each customer-dedicated portal as a **GitLab University Panorama**. The course content is the same as the public catalog. The key differences are:

- SSO configuration for customer users (optional)
- Custom content hosting alongside GitLab University materials
- Customer-specific reporting
- Elevated platform permissions for designated individuals

Each panorama is provisioned and managed by the CX Platform Engineering team and must be requested via the [CX intake request form](https://cx-requests-c0b2c7.gitlab.io/) (see workflow below).

## Who can request a Panorama?

Any CX team member working with the customer can submit the request.

## Who qualifies?

Customers on the Signature Success tier are eligible for GitLab University Enterprise / Panorama.

## Pre-requisite information to gather from the customer

Before opening a request, the requesting team member should gather:

1. **Authentication preference**
   - Do they want SSO login or site registration code?
   - Default: site registration code and customer account creation — simpler and faster, no IT dependency.
   - SSO:
     - Requires customer IT involvement
     - Customer must provide an IT contact name who can join a 30-minute configuration call with the GitLab University team
     - Capture which SSO provider they use (Okta, Microsoft Entra, other)
     - SSO scheduling can extend the overall setup timeline, depending on customer IT availability.
2. **Certification vouchers**
   - How many certification vouchers did the customer purchase (if any)?
   - Do you have the registration code(s)?
3. **Customization preferences**
   - Content exclusions: Any content from the public GitLab University catalog to be excluded?
   - Custom content uploads: Any customer-provided content to upload?
4. **Reporting needs**
   - Customer's GLUE Admin email (required): To access reporting dashboards (e.g., user enrollments, course completions, active users, adoption activity), the customer needs an admin account. Collect the email address(es) of customer stakeholders who should have reporting access and include them in the request issue.

## How to request a Panorama

1. **Gather customer details**
   Collect all pre-requisite information listed above.

2. **Submit your request using the intake form**
   Go to [CX intake request form](https://cx-requests-c0b2c7.gitlab.io/) and:
   - Sign in with your GitLab account
   - Enter your request summary using this format: `GitLab University Enterprise Request - <Customer Name>`
   - The form will automatically detect your Panorama request and populate the template based on your title
   - You'll see in the right panel:
     - **Suggested destination:** CX-Platform-Engineering
     - **Routing confidence:** How confident the system is in the routing
     - **Matched keywords:** What triggered the Panorama detection
     - **Pre-selected labels:** GitLab-University and Panorama
     - **Issue template preview:** A 4-step form to guide your request

3. **Complete the 4-step template**
   You'll fill out:
   - **Step 1:** Your details and customer information
   - **Step 2:** Portal creation rationale
   - **Step 3:** Customization preferences:
     - Content to exclude from the public catalog
     - Custom content to upload
     - Reporting dashboard access (provide email addresses for customer stakeholders who need access to usage analytics such as enrollments, completions, and adoption activity)
     - Authentication method (SSO or site registration code)
   - **Step 4:** Admin checklist (completed by GitLab University team after approval)

4. **Select urgency level**
   Choose the appropriate urgency for your request:
   - **Standard:** SLA 2 weeks — Normal priority, queued with other requests
   - **Expedited:** SLA 1 week — Higher priority, moved to front of queue
   - **Critical:** SLA 48 hours — Business-critical issue requiring immediate attention

   *SLA times are estimates for initial response from the team. Complex requests may require additional time to fully resolve.*

5. **Submit and track progress**
   - Click submit to create the issue in the CX-Platform-Engineering project
   - Use the issue as your system of record
   - Keep the issue updated with:
     - Status updates from the GitLab University team
     - Links to the live Panorama once provisioned
     - Notes from any SSO configuration calls

6. **Document for ongoing account management**
   - Add the Panorama URL and key details (authentication method, main learning paths, reporting owner) to:
     - The customer's Gainsight C360, and/or
     - The customer collaboration project on GitLab

## After the customer gains access

### Initial rollout

- Share the customer-specific welcome one-pager (provided by the GitLab University team)
- Remind them of certification vouchers and how to redeem them
- Recommend learning paths aligned to their goals

### Ongoing engagement (at least quarterly)

Review Panorama usage with the customer to:

- Track adoption, course completions, and certification progress
- Identify unused vouchers and highlight expiration dates
- Suggest new learning paths based on current initiatives or product updates

## Getting support

### For GitLab team members

- **For Panorama-related requests** (new portals, content changes, configuration updates, reporting access), use the [CX intake request form](https://cx-requests-c0b2c7.gitlab.io/). This ensures your request is routed and tracked correctly.
- **For platform bugs or feature requests** not specific to a customer Panorama, open an issue in the GitLab University project:
  [GitLab University issues](https://gitlab.com/gitlab-com/customer-success/digital-success/platform/gitlab-university/-/work_items?type=ISSUE&initialCreationContext=list-route)

### For customers

- Customers can email university@gitlab.com to contact the GitLab University team directly for help with the Panorama

## Requesting custom content uploads

To upload customer-specific content into an existing Panorama:

1. Submit a request via the [CX intake request form](https://cx-requests-c0b2c7.gitlab.io/)
2. Include in your request:
   - Customer name and Panorama name
   - Title of the content
   - Short description (audience, purpose, where it should appear)
   - The file to upload (or link, if appropriate)

**Target SLA**: 3 business days from receipt of complete information

**Note:** The GitLab University team will upload customer-specific content but will not create custom learning paths due to maintenance overhead when courses are updated.

## Adding admins to an existing Panorama

To add a customer as a reporting admin after the initial Panorama setup:

1. Submit a request via the [CX intake request form](https://cx-requests-c0b2c7.gitlab.io/)
2. Include in your request:
   - Customer name and Panorama name
   - Email address(es) of customer stakeholders who need reporting access
3. The GitLab University team will provision admin access within 5 business days

Admins can view usage reports and dashboards in GitLab University Enterprise, including user enrollments, course completions, active users, and adoption activity.

## The value of GitLab University for customers

- Scalable, self-serve learning for teams at any size
- Access to GitLab University content organized by focus area like DevOps and CI/CD, Security, and AI Duo
- A mix of short courses, hands-on labs, and certifications
- Customer-specific reporting on usage and completion
- Ability to include customer-owned content in the same portal
- One centralized hub for all GitLab education used across the organization

## Escalation path (internal)

If you encounter blockers or critical issues:

1. **Open a GitLab issue** in the GitLab University project and tag:
   - `@khokanson`
   - `@p_luong`
2. **Escalate in Slack**:
   - Post in `#digital-success` with:
     - A link to the issue
     - A short summary of the blocker
   - Tag:
     - `@khokanson`
     - `@p_luong`
     - `@nfrye`
