---
title: Traction Lead Complete
description: Traction Lead Complete Overview
twitter_image: /images/tweets/handbook-marketing.png
twitter_site: '@gitlab'
twitter_creator: '@gitlab'
---

- Overview
- Lead Routing Workflow
- Partner lead management
- Contact routing workflow
- Account routing workflow
- Lead routing request or question?
- How to Reassign a lead
- Traction Lead Flow update process

## Overview

Traction Lead Complete is an application within Salesforce to process and assign lead records, L2A matching and contact routing.

Traction assigns each MQL (Marketing Qualified Lead) to the member of the Sales Development organization who is responsible for engagement and qualification of that individual dependant on the workflow.

## Lead Routing Workflow

To read in more detail how our lead routing logic is set up, please visit the internal handbook page on [Traction](https://internal.gitlab.com/handbook/marketing/marketing-ops-and-analytics/marketing-operations/traction/).

## Partner Lead Assignment

In the first stage of the main lead assignment flow, Traction runs through its assignment rules to filter for Channel Partner and Distributor leads. They are assigned using campaign member based routing and primarily fields on the campaign member object. Most Channel related records are assigned to `Partner Queue` and passed to Channel Partners via [Impartner](/handbook/marketing/marketing-operations/impartner/), where they can accept, assign and qualify the leads.

Note: Alliance partner leads will be assigned to members of the Sales Development team for qualification.

GitLab collaborates with Channel Partners to develop co-marketing campaigns including Partner sponsored, MDF funded, free trial and joint partner campaigns.

### Partner Sponsored Event

GitLab allows Channel Partners to sponsor our owned events. Traction completes the following steps when it recognizes a new campaign member is associated with a [partner sponsored event](/handbook/marketing/growth-marketing/partner-and-industry-marketing/#partner-sponsored-events):

1. Reviews the lead fields for  `Lead Acquisition Source` = `Partner Sponsored Event` and `Impartner Partner Account` is not empty
1. Checks the lead fields for  `Partner Recalled Date` is empty and `Partner Recalled` equals `False`
1. Updates `Partner Share Status` = `Pending` and `Partner Lead Status` = `Qualifying` which enables the lead to be synced into the Impartner Prospects (Lead Sharing).
1. Assigns the lead to `Partner Queue`.

### MDF and Free Trial Campaign

Traction completes the following steps when it recognizes a new campaign member is associated with a [MDF campaign](/handbook/marketing/growth-marketing/partner-and-industry-marketing/#mdf-campaigns) and trial campaign:

1. Reviews the campaign field for `Will there be MDF funding` = `Yes`, campaign name if it starts with  `Partner - Trial`and lead field for `Impartner Partner Account` is not empty.
1. Checks the lead fields for  `Partner Recalled Date` is empty and `Partner Recalled` equals `False`
1. Updates `Prospect Share Status` = `Sending to Partner` and `Partner Prospect Status` = `Qualifying` which enables the lead to be synced into Impartner.
1. Assigns the lead to `Partner Queue`.

### Joint Partner Campaign

Traction completes the following steps when it recognizes a new campaign member is associated with a [joint partner campaign](/handbook/marketing/growth-marketing/partner-and-industry-marketing/#joint-gitlab-and-partner-campaigns):

1. Reviews the campaign fields for `Is a Channel Partner Involved?` = `Yes` and  `Campaign Member Status` with regards to partner engagement, and the lead field for `Impartner Partner Account` is not empty.
1. Verifies the campaign member is not actively worked by GitLab, thus `Person Status` is not `Accepted`, `Qualifying` nor `Qualified`, or `Actively Being Sequenced` = `False`. <br>
If all above is
   1. True, then Traction updates the `Partner Prospect Status` to `Qualifying`, `Prospect Share Status` = `Sending to Partner`, then assigns the lead to `Partner Queue`
   1. False, then Traction assigns to appropriate SDR.

### Exceptions to This Rule

When a lead/contact engages with GitLab in any shape or form, for example, via an inbound marketing request, the lead/contact owner is responsible for following up with the partner lead, regardless of their stage within the partner lead lifecycle.

## Contact Routing

To read in more detail how our contact routing logic is set up, please visit the internal handbook page on [Traction](https://internal.gitlab.com/handbook/marketing/marketing-ops-and-analytics/marketing-operations/traction/)

Traction works to ensure all regional SMB Sales owned accounts and their associated contacts are owned by AMER/EMEA/APJ SMB Sales. When leads are converted, contact ownership consistently update to the appropriate regional SMB Sales owner. We implemented a change in October of 2025 to fix contact ownership reassignment; If there's an open opportunity, Traction will now update all contacts associated to the Account (not just Primary Owner) to the SMB account owner (rather than the opportunity owner).

All other [SFDC contact ownership rules](/handbook/sales/field-operations/gtm-resources/#changing-contact-ownership-in-salesforce) are maintained through [Traction](/handbook/marketing/marketing-operations/traction-lead-complete/#contact-routing). If you have questions or concerns about contact routing outside of partner record management processes, please reach out to [Sales Systems](/handbook/sales/field-operations/sales-systems/).

## Account Routing

All account routing is handled by Enterprise Territory Management (ETM). If you wish to learn more about this, please visit the sales operation handbook.

## Traction Complete view on the account object

We have custoized the lead section of the Traction Complete view on the account object. To navigate to this section in Salesforce Lightning, click `Traction Complete` on the top of the account page (same row you find `Details`). This will open the view where you can see all leads matched to the account with useful information like Full Name, Title, Email, Last Activity, Last Flow Name, and Active Flows Count. This information can be valuable to Sales Development and Sales to collaborate on reaching out to high value leads associated with their accounts.

### How to reassign a lead step by step

1. Update `[Admin] Company Address Country`. You will need to update the `[Admin] Company Address Source` field before the country field will save.
2. Check the box for Re-run Traction Complete. Save the lead.
3. Refresh - the lead should now be reassigned.

Notes:

- The lead will be assigned based on round robins for that region.
- This will only work for MQL reassignment- it will not work for HP leads.
- This will not work if the lead is matched to an account where there is a BDR assigned (in APJ) and marked as Actively Working (EMEA & AMER).
- Remember that the `[Admin] Company Address Country` also affects account and opportunity routing so don't update the country unless you are sure of where it is.

## Schedule Routing Jobs

There are a number of scheduled and/or clean up jobs on the lead and contact object to help ensure records are in the proper ownership.

1. `Daily lead ownership to Queues`: This job runs nightly on leads in Inquiry, Ineligible, and Disqualified status to the corresponding status queue. Other filters include: Lead is not actively being sequenced, Matched account is not Actively Working, Lead is not converted, AI Email in Progress is false, Owner Profile is Sales Development Rep OR Marketo Integration with a Last Interesting Moment Date greater than May 1, 2025

2. `Weekly lead ownership to Queues`: This job runs weekly on Saturday on leads in Raw and Recycle status. Other filters include: Lead created date is greater than 7 days ago, High Priority is false, AI Email in Progress is false, Actively Being Sequenced is false, Matched Account is not Actively Working, Is Converted is false, Owner Profile is Sales Development Rep OR Marketo Integration with LIM Date after May 1, 2025.

3. `Daily Recycle, No Action flow`: This job moves leads that have been in MQL status for more than 30 days to Recycle, No Action.

4. `BDR Actively Working Reassignment`: This job moves leads matched to an account that has been marked as Actively Working to the BDR Assigned on the account. The leads must be in Recycle, Raw, or Inquiry status. The job is scheduled to look at BDR Prospecting Status changes that occurred the previous day.

5. `Inactive User Lead Assignment`: When the owner of a lead goes inactive in Salesforce, the lead will be reassigned based on our routing rules.

6. `Account Owner/BDR Assigned Change Contacts Assignment`: When the Owner or BDR Assigned on an account is changed, contacts associated with that account will run based on our contact assignment rules.

## Lead routing request or question?

### Request an update to Routing

 If requesting a proactive update to the lead routing workflow, open an issue using the [Routing change request issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/blob/mktgops-template-updates-nov2025/.gitlab/issue_templates/Routing_Change_Request.md).

### Experiencing a lead routing problem?

Lead volume low? Receiving leads from an account or territory you're not assigned to? If you think you've found a bug :bug: in existing lead routing logic, open an issue using the [bug request issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new?issuable_template=bug_request).

### General questions

Open a [Marketing Operations issue](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new) following the format in the issue template.

## Traction Update Governance Process

### Process Workflow

#### 1. Request Submission

Who: Any stakeholder requesting a change

- [Action: Open a GitLab issue with the following template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/blob/master/.gitlab/issue_templates/lead_routing_approvals.md)

Required Issue Template Fields:

- Change Title: Brief, descriptive title
- Requester: Name and team
- Change Type:
  - Permanent routing change
  - One-off campaign routing
- Business Justification: Why is this change needed?
- Detailed Description: What specifically needs to change?
- Campaign Duration (if one-off): Start and end dates for temporary routing
- Affected Teams/Users: Who will be impacted by this change?
- Priority Level: Critical / High / Medium / Low
- Target Timeline: When is this needed by?
- Success Criteria: How will we know this change is successful?
- Issue Labels: Traction, MktgOps::00: Triage, and appropriate priority label

#### 2. Team Notification

Who: Issue creator

- Action: Tag all related teams in the GitLab issue comments with the following details
  - Provide a brief summary of the change and why they're being notified
  - Request feedback or concerns by a specific date (suggest 3-5 business days)
  - Issue Labels: Add Traction::Stakeholder-Review

#### 3. Development & Testing

Who: Bryce Weatherford & Gill Murphy

Development Phase:

- MKTGOPs will assign the issue to a team member
- Develop the change in the Traction Sandbox Environment
- Document the technical changes made
- Add implementation notes to the GitLab issue

Testing Phase:

- Conduct thorough testing in sandbox:
- Functional testing
- Integration testing with dependent systems
- User acceptance testing (if applicable)
- Document test results in the issue
  - Capture screenshots/videos of the change if helpful
- Confirm all success criteria are met

Issue Labels: Update to MktgOps::04: In Progress then Traction::Testing

#### 4. Approval Process

Who: Gill Murphy or Amy Waller if Gill on leave

- Action: Review the GitLab issue for approval

Approval Checklist:

- All required fields completed
- Change type clearly identified (permanent vs. one-off)
- For one-off campaigns: Duration and reversion plan documented
- Related teams have been informed
- Development completed in sandbox
- Testing completed with documented results
- No major concerns raised by stakeholders
- Business justification is sound
- Change aligns with Traction roadmap/strategy

How to Approve:

- Comment "Approved"
- Tag the builder to proceed

Issue Labels: Update to MktgOps::05: Business Owner Review

#### 5. Production Implementation

Who: Bryce Weatherford or Gill Murphy

- Actions: Build the requested logic

Pre-Deployment Requirements:

- Deployment Window: Schedule for Early to Mid Week. No Friday Deployments
- Build Monitoring Report: Create a report to track the change impact
- Define key metrics to monitor (e.g., routing accuracy, volume changes, error rates)
- Set up dashboards or queries to track these metrics
- Document baseline metrics before deployment
- Attach report specifications to the GitLab issue

Update Handbook Documentation:

- Document the change in the Traction handbook/documentation
- Include what changed, why it changed, and how it works now
- Update any relevant workflow diagrams or process maps
- Update user guides or training materials if applicable
- Add screenshots or examples if helpful
- Link the handbook update to the GitLab issue

Deployment Process:

1. Download from Sandbox:

   - Export/download the configuration file from the Traction sandbox environment
   - Verify file integrity and completeness
   - Document the file version/timestamp

2. Pre-Deployment Checklist:

   - Deployment scheduled for Tuesday or Wednesday
   - Monitoring report built and tested
   - Configuration file downloaded from sandbox
   - Affected teams notified of deployment time
   - Rollback plan documented
   - Backup of current production configuration taken

3. Upload to Production:

   - Upload the configuration file to Traction production environment
   - Verify successful upload
   - Perform smoke testing (basic functionality check)

4. Post-Deployment Monitoring:

   - Run the monitoring report immediately after deployment
   - Monitor for 24-48 hours using the created report
   - Check for unexpected behaviors or errors
   - Document any issues in the GitLab issue

5. Update GitLab Issue:

   - Timestamp of deployment
   - Initial monitoring report results
   - Link to handbook documentation updates
   - Any immediate observations or concerns

Issue Labels: Update to MktgOps::06: Ready to Deploy then Traction::Monitoring after deployment

#### 6. Closure

Who: Mktgops team

Actions:

1. Review monitoring report results after 24-48 hours
2. Confirm change is working as expected in production
3. Compare post-deployment metrics to baseline
4. Verify handbook documentation is complete and accurate
5. For one-off campaign routing: Schedule and document the reversion plan
6. Gather feedback from affected teams
7. Document lessons learned and any adjustments made
8. Archive the sandbox configuration file and monitoring report
9. Close the GitLab issue with a summary including:
   - Deployment success confirmation
   - Monitoring report summary
   - Handbook documentation confirmation
   - Reversion schedule (if one-off campaign)
   - Any unexpected findings
   - Recommendations for future changes

Issue Labels: Update to MktgOps::08: Completed and close issue.

#### 7. One-Off Campaign Reversion (When Applicable)

Who: Bryce Weatherford or Gill Murphy

When: After the campaign end date specified in the original request

Actions:

1. Schedule Reversion:

   - Set calendar reminder for campaign end date
   - Assign team member to perform reversion
   - Notify affected teams of upcoming reversion

2. Perform Reversion:

   - Download original (pre-campaign) configuration from backup
   - Upload to production mid week only.
   - Follow same deployment process as initial change

3. Verify Reversion:

   - Confirm routing has returned to normal
   - Run monitoring report to ensure expected behavior
   - Update original GitLab issue with reversion details

4. Document:

   - Update handbook if temporary routing had been documented
   - Note reversion completion in GitLab issue
   - Archive campaign routing configuration

Note: One-off campaign routing changes should be clearly marked in the monitoring report and handbook updates as temporary changes with documented end dates.

## Recommended Label Workflow for Traction Changes

| Stage | Labels to Use |
|-------|---------------|
| 1. Request Submitted | Traction + MktgOps::00: Triage + Priority label + Traction::One-Off-Campaign (if applicable) |
| 2. Stakeholder Notification | Traction + Traction::Stakeholder-Review + Priority label + Traction::One-Off-Campaign (if applicable) |
| 3. Development | Traction + MktgOps::04: In Progress + Priority label + Traction::One-Off-Campaign (if applicable) |
| 4. Testing in Sandbox | Traction + Traction::Testing + Priority label + Traction::One-Off-Campaign (if applicable) |
| 5. Business Owner Review | Traction + MktgOps::05: Business Owner Review + Priority label + Traction::One-Off-Campaign (if applicable) |
| 6. Approved, Ready to Deploy | Traction + MktgOps::06: Ready to Deploy + Priority label + Traction::One-Off-Campaign (if applicable) |
| 7. Deployed to Production | Traction + Traction::Monitoring + Priority label + Traction::One-Off-Campaign (if applicable) |
| 8. Complete | Traction + MktgOps::08: Completed + Priority label + Traction::One-Off-Campaign (if applicable) |
| 9. One-Off Reversion Complete | Traction + MktgOps::08: Completed + Priority label + Traction::One-Off-Campaign + Close issue |

**If Blocked at Any Stage:** Add `~MktgOps::07: Blocked`

**If More Info Needed:** Use `~MktgOps::01: Needs More Information`

**Note:** Keep the Traction::One-Off-Campaign label throughout the entire lifecycle if the change is temporary. This makes it easy to filter and track all campaign routing that needs reversion.

## SLA Guidelines

| Stage | Target Timeline |
|-------|-----------------|
| Stakeholder Notification | Within 1 business day of submission |
| Stakeholder Feedback Period | 3-5 business days |
| Development (varies by complexity) | To be estimated per request |
| Testing (varies by complexity) | 2-5 business days |
| Approval Review | 2 business days |
| Monitoring Report Creation | 1-2 business days before deployment |
| Production Deployment | Early or Mid Week - No Friday deployments. |
| Post-Deployment Monitoring | 24-48 hours |
