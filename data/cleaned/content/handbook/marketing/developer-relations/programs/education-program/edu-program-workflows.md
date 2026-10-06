---
title: "GitLab for Education Program Workflows"
description: "Details on program-specific workflows related to the GitLab for Education Program"
aliases:
  - /handbook/marketing/developer-relations/strategy-programs/education-program/edu-program-workflows/
---

## Overview

This page contains details regarding workflows specific to issuing complimentary GitLab Ultimate licenses through the [GitLab for Education Program](/handbook/marketing/developer-relations/programs/education-program/).
Program members apply directly through the [GitLab Customers Portal](https://customers.gitlab.com/subscriptions/community_program/coupons/new?program=EDU) and are verified through a third party, [Proxi.id](https://proxi.id/).
Successfully verified users receive an email sent via `education@gitlab.com` with a coupon code and instructions to claim the subscription.

## Application workflow

An interactive step-by-step walkthrough of the application process for GitLab for Education is available through [Navattic](https://gitlab.navattic.com/g3x05ub).

Users must login or register through the [GitLab Customers Portal](https://customers.gitlab.com/subscriptions/community_program/coupons/new?program=EDU) to begin the application process.

The GitLab Customers Portal creates a unique tracking ID each time a program member attempts to start their verification with Proxi.id.
Only the tracking ID is sent to Proxi.id and no other PII is exchanged from the Customers Portal.

### Proxi.id verification workflow

Proxi.id offers several methods for verifying user identity at the academic institution.

1. Single sign on (users can log into their institutions SSO for automatic verification)
1. Email domain check (users can enter their institution email address and then confirm through a link)
    * If the institution uses a shared domain for both students and faculty, further proof of employment is required
1. Submit proof of eligibility (users can fill out a form and upload a document proving their employment at the institution)

If applicants are not successful with the first 3 automated verification options above, the Proxi.id team will offer a manual review for the applicant.

Proxi.id will send a message to the email the user provided during the proof of eligibility form submission and ask the user to upload an additional document.
Proxi.id also instructs the user to reach out to the GitLab Education Program team for any additional support using `education@gitlab.com`.

### Checking verification status

GitLab team members can view whether or not an applicant has successfully verified from the [Proxi.id Verifications page](https://customers.gitlab.com/admin/community_program~proxy_id_verification) in the Customers Portal.

* A "succeeded" status indicates Proxi.id has returned a webhook to confirm back to the Customers Portal which automatically triggers the Customers Portal to email the coupon code and instructions to the applicant.
* An "initialized" status indicates the user has started the verification process but may or may not have submitted anything. It is worth noting that this status could mean that the user's submission is incomplete and has not entered any information in Proxi.id's website, **or** that they have submitted to Proxi.id's website but have not yet completed their verification.
* A "rejected" status indicates the user has had their submission rejected. The "Feedback" column provides the reason for this being either that a student applied and is not eligible, or that the institution does not meet the criteria for the program.

GitLab team members can follow up with the Proxi.id team by emailing gitlab-support@proxi.id with the user tracking ID to inquire about current status. Note that Proxi.id regularly deletes the user data submitted through their websites, so a submission that was made several weeks ago may have been removed.

### Proxi.id bypass codes

GitLab team members can email gitlab-support@proxi.id to ask the Proxi.id team for bypass codes which can be used in lieu of the SSO/email check for verification.
Bypass codes are valid for 7 days and contain a special email address and verification code to submit in the Proxi.id UI.

### Manual codes

The GitLab for Education Program team can additionally provide a manual GitLab Ultimate coupon code directly to a member at their discretion using a code available in the [internal coupon code spreadsheet](https://docs.google.com/spreadsheets/d/1kORpssdu28RS1GIeE5C-LVzrrKC1iLwEoC3x0_2OnwU/edit?usp=sharing). 

## Support queue workflows

This section describes workflows for team members handling the Education Program support queue.

### Support queue overview

When program members encounter problems during the application or renewal process, they email `education@gitlab.com`. Each email automatically creates an issue in the [Education Program Support project](https://gitlab.com/gitlab-com/marketing/developer-relations/strategy-programs/education-program/education-program-support/-/issues/?sort=created_date&state=opened&first_page_size=100).

Team members use a [GLQL dashboard](https://gitlab.com/gitlab-com/marketing/developer-relations/meta/-/issues/61) to monitor and triage support tickets. The dashboard displays:

* New issues
* Reply detected (issues where the program member has replied)
* Missing label / ongoing issues
* Sales assisted issues

### Labels

The following labels are used in the Education Support project:

| Label | Description |
|-------|-------------|
| `EDU Program Support::Intake` | New issues to triage (automatically removed when the Programs team replies) |
| `updated` | Issues where the program member has replied (automatically removed when the Programs team replies) |
| `EDU Program Support::Sales` | Issues waiting on Sales team assistance |

### Comment templates

Active comment templates are located in the [Education Program Support project](https://gitlab.com/gitlab-com/marketing/developer-relations/strategy-programs/education-program/education-program-support/-/comment_templates).

### Verification flow

When handling a support request, always complete the following verification steps:

1. Check the customer using their email in [customers.gitlab.com/admin/customer](https://customers.gitlab.com/admin/customer):
   * First/last name
   * GitLab groups (to confirm the namespace they are referencing)
   * Zuora subscriptions (check subscription type, plan, end date, owned seats)
1. If the customer reports being stuck in the verification process, check:
   * [Proxi.id Verifications page](https://customers.gitlab.com/admin/community_program~proxy_id_verification) in the Customers Portal, where the status can be seen as "initialized" or "succeeded"
   * Contact the Proxi.id support team with the Tracking Id to check the status of an application

### Renewal and application flow

Many customers assume that the team has full context about their situation without providing details. Treat each customer as a new applicant requiring confirmation of compliance with program rules. Additionally, during 2025 changes were made to renewals which means that all applications to the program, new or renewals, go through the same process and voucher codes are no longer issued. Some existing program members may need to be reminded about this change.

When a customer contacts support, first direct them to the automated application process:

> Hello [name],
>
> Thank you for your email and description of your situation. Could you please try to go through our automated process of application/renewal here - https://about.gitlab.com/solutions/education/join/?
>
> To do that you will need simply to fill the Application form and our system will send you renewal/application code for your subscription.
>
> In case if you encounter any issues during this process please let me know and I will help you with manual application/renewal.
>
> Best regards.

Note: Many customers are unaware that the renewal process uses the same application form at [about.gitlab.com/solutions/education/join/](https://about.gitlab.com/solutions/education/join/), even though this is mentioned in the renewal reminder emails they receive.

### Manual renewal workflow

When customers cannot complete the automated process, request additional information to verify their eligibility:

> Hello,
>
> I am sorry to hear that you encountered these issues during the renewal/application process. To proceed with manual application I will need to ensure that you are compliant with program rules. To do that could you please provide me the following information:
>
> 1. Link to official website / description of your institution
> 1. Description of how you currently use/intend to use GitLab
> 1. Who you will be teaching and their age?
> 1. (optional) Confirmation that you are a teacher/staff member of this institution (ID or any other valid proof)
>
> Thank you in advance!

#### Confirming intended usage

In some cases it is not clear if the customer intends to use GitLab for teaching purposes as required by the program. Ask customers to describe how they currently use or plan to use GitLab to confirm alignment with program goals.

### Providing renewal codes

When a customer has provided all needed information and their eligibility is confirmed:

1. Use the comment template called **Education program approval code**
1. Obtain a renewal code from the [renewal codes spreadsheet](https://docs.google.com/spreadsheets/d/1kORpssdu28RS1GIeE5C-LVzrrKC1iLwEoC3x0_2OnwU/edit) (EDU tab)
1. When using a code from the spreadsheet:
   * Mark "Yes" in the "Dispatched" column first, before copying the code
   * In the "Who?" column, provide information about the institution (name or link to their website)
   * In the "Support Ticket link" column, provide a link to the issue
   * Add notes if needed

### Adding more seats

This is a common request. Use the comment template called **Any program ask for additional seats**. The key points to communicate:

* Customers can add additional users to their namespace, even if it exceeds the registered seat count
* Automated messages about charges for additional seats can be safely ignored for program members
* At renewal time, customers should update the number of seats when completing the application form

### Multiple GitLab subscriptions

Program members may ask for multiple subscriptions so that they can run more than one instance of GitLab. This is unusual and requires approval from the Developer Relations Programs team. A clear justification for this should be requested from the program member and discussion on the #developer-relations-programs Slack channel to agree on the approval. If a decision is made to grant this, a manual process is required to provision the second instance. It is not possible for the member to add or renew a second instance through the customer account portal. Use the manual codes or renewal codes processes on this page so that the member can set up a second subscription. Use the message template "Manual Voucher Code" for the reply.

### Handling common issues

#### Students applying to the program

When students apply to the program, explain the available options:

1. Ask their teachers or university staff to apply to the program on behalf of the institution
1. Join the [GitLab Contributors program](https://contributors.gitlab.com/)
1. Start an open source project and apply for the [GitLab for Open Source Program](https://about.gitlab.com/solutions/open-source/)

Use the "Student Application Response" comment template to reply to this type of inquiry.

#### Wrong license type selected

Customers sometimes select Self-managed instead of SaaS (or vice versa) during renewal. When this happens:

1. Confirm that the customer is part of the Education program
1. Confirm they recently renewed (within the past week/month)
1. For SaaS licenses, confirm they are not a K-12 institution (K-12 institutions are only eligible for Self-managed)
1. Provide a new code for the correct license type

#### Not approved by verification system

When eligible customers are not approved by Proxi.id:

1. Check the [Proxi.id Verifications page](https://customers.gitlab.com/admin/community_program~proxy_id_verification) for their status
1. Contact gitlab-support@proxi.id with the tracking ID if needed
1. If verification cannot be completed through Proxi.id, proceed with manual verification and provide a code directly

#### Ownership confirmation

When someone other than the account owner sends a request:

1. Request confirmation of account ownership
1. Ask for a screenshot of the namespace showing they are the owner
1. If the email is not found in the system, request the GitLab account owner's email

#### Ownership transfer

If a member needs to transfer ownership of their account to another person, they can do this through the [GitLab Customers portal](https://customers.gitlab.com/) following the [instructions for changing profile owner information](https://docs.gitlab.com/subscriptions/billing_account/#change-profile-owner-information).

The "Change of account ownership" comment template can be used to respond to this type of inquiry.

### Upsell and add-on workflow

<!-- vale off -->
<!-- Upsell is a valid business term -->

Each renewal code email suggests add-ons like Duo. When customers express interest:

1. Start a Slack thread in `#developer-relations-programs` with:
   * Short description of the opportunity
   * Customer contact information
   * Support issue link
   * SFDC link
1. Mention the Account Executive and Business Development Representative responsible for the customer account

### Escalation workflow

For non-standard cases or when uncertain how to proceed, reach out to the `#developer-relations-eng-and-programs-confidential` Slack channel. Provide:

* What the case is about (brief summary)
* Link to support issue
* Link to customer in customer database
* Any additional relevant information (email, link to namespace, etc.)

### Handling nonprofit program members

Occasionally, nonprofit program members contact the Education team for renewal (Education and Nonprofit programs use the same SKU). In these cases:

1. Guide the customer to the [GitLab for Nonprofits program](https://about.gitlab.com/solutions/nonprofit/)
1. Explain that the Nonprofit team reviews applications within 2 working weeks

Use the "Nonprofit Submission Response" comment template to respond to this type of inquiry.

### Handling unrelated inquiries

For requests not related to the program (events, funding requests, etc.), follow the escalation workflow described above.

For spam, add an internal comment noting it as spam and close the ticket.

### Handling forwarded requests

The team uses the GitLab Service Desk to manage incoming support issues effectively. Sometimes GitLab Support forwards customer requests directly without including the customer in the thread. In these cases:

* Answer the question in the customer email if possible
* If the customer needs help with renewal, ask the person who forwarded the email to have the customer write directly to `education@gitlab.com`

Example response to the forwarder:

> Hello,
>
> Since the team uses the GitLab Service Desk to manage support issues, unfortunately I cannot write to customers directly. Could you please ask them to write to education@gitlab.com and the team will help resolve issues with renewal. Currently there is no request from them in our system.
>
> Best regards.
