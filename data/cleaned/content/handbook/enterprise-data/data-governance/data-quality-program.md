---
title: "Data Quality Program"
description: "GitLab Data Quality Program framework, standards, and procedures for ensuring trusted data across the enterprise"
---

## Overview

The Data Quality Program establishes comprehensive standards and procedures to enhance trust in GitLab's data assets, enabling accurate insights and effective decision-making while reducing manual data correction efforts. This program is led by the Data Governance & Quality team and covers all enterprise data domains.

### Program Objectives

- **Measure** data quality objectives across all dimensions
- **Track** progress against specific, measurable targets
- **Report** on program effectiveness at multiple levels
- **Improve** continuously through data-driven insights

## Data Quality Framework

### Six Dimensions of Data Quality

The GitLab Data Quality Program measures quality across six key dimensions:

|Dimension|Definition
|-----------|----------
|**Accuracy**|Data correctly represents real-world entities and values
|**Completeness**|All required data fields are populated
|**Consistency**|Data aligns across different systems and over time
|**Timeliness**|Data is available within expected timeframes
|**Validity**|Data conforms to defined formats and business rules
|**Uniqueness**|No inappropriate duplicate records exist

*Note: Specific target thresholds will be established through baseline measurements and domain-specific requirements.*

### Implementation Approach

The Data Quality Program will be implemented through close partnership with domain stakeholders and functional data stewards. Each domain's unique requirements and challenges will be addressed through:

- Collaborative baseline assessments with domain teams
- Co-development of domain-specific quality thresholds
- Joint ownership of improvement initiatives
- Regular touchpoints with domain stewards for continuous refinement

**Timeline:**

- **FY27**: Pilot implementation for Product domain to establish frameworks, processes, and best practices
- **FY27-28**: Expand program to additional domains based on pilot learnings and domain readiness

## Reporting and Managing Data Quality Issues

### When to Open a Data Quality Issue

Open a Data Quality issue when you discover:

- **Inaccurate Data** - Values that don't match reality (e.g., incorrect revenue amounts)
- **Missing Data** - NULL or empty fields that should exist (e.g., missing customer IDs)
- **Inconsistent Data** - Conflicting information across systems (e.g., different customer counts in Salesforce vs. Snowflake)
- **Untimely Data** - Outdated, stale, or delayed data updates (e.g., dashboards not refreshing)
- **Invalid Data** - Format violations or business rule breaches (e.g., future dates for historical events)
- **Duplicate Data** - Repeated records where uniqueness is expected (e.g., duplicate customer records)

### How to Report a Data Quality Issue

<details>
<summary><b>Step 1: Create the Data Quality Issue</b></summary>

1. Navigate to the [Analytics project](https://gitlab.com/gitlab-data/analytics/-/issues) in GitLab
2. Click "New Issue", select and apply the **[Report] Data Quality Issue**
3. If converting an existing issue, use `/label ~"Data Quality Issue"`

</details>

<details>
<summary><b>Step 2: Complete Required Information</b></summary>

#### Issue Classification & Severity

Select the appropriate severity level (Sev1-4) based on business impact as defined in the issue template.

**⚠️ For Sev1/Sev2 issues:** Immediately notify #data-team Slack channel and tag `@data-governance`

For more details on Incident management and Severity Levels, kindly refer the [Data Team Incident Management](/handbook/enterprise-data/data-governance/incident-management/) Handbook Page.

##### Problem Description

Provide comprehensive details in all required fields of the template, including technical evidence.

**Technical Evidence:**

Complete the evidence section in the issue template with relevant SQL queries, screenshots, and data samples.

##### Impact Assessment

Complete all impact fields in the template (Customer, ARR, Records, Strategic Impact).

##### Systems Information

Complete the systems and domain checkboxes provided in the issue template:

- **Primary Affected System** - Select all systems where the issue occurs
- **Data Domain Affected** - Identify which business domain is impacted

</details>

<details>
<summary><b>Step 3: Apply Labels</b></summary>

Use the quick label command:

```bash
/label ~"Data Quality Issue" ~"Sev[1-4]" ~"Champion: [Domain]" ~"Team: [TeamName]" ~"DQ-[Dimension]" ~"RC::[Category]" ~"workflow::1 - triage & validation"
```

**Example:**

```bash
/label ~"Data Quality Issue" ~"Sev2" ~"Champion: Sales" ~"Team: Analytics Engineering" ~"DQ-Accuracy" ~"RC::Data-Integration" ~"workflow::1 - triage & validation"
```

</details>

<details>
<summary><b>Step 4: Link Related Issues</b></summary>

- Search existing Data Quality issues for similar problems
- Link to related epics if they exist
- Note any patterns or recurring issues

</details>

### Data Quality Issue Workflow

**Detection → Triage & Validation → Investigation → Resolution → Prevention → Closed**

<details>
<summary><b>Triage Process</b></summary>

**For Issue Triagers:**

1. **Validate Severity** - Confirm it matches business impact
2. **Check for Duplicates** - Search for similar existing issues
3. **Apply DQ Dimension Label** - Use appropriate `DQ-[Dimension]` label
4. **Assign DRI** based on issue type
5. **Set Workflow State** - Move to appropriate stage
6. **Communicate** - Notify via Slack if Sev1/Sev2

</details>

### Data Quality Issue Management Workflow

**Detailed Workflow Diagram - Coming Soon**

A comprehensive workflow diagram detailing decision points, escalation paths, and automated triggers for data quality issue management is currently being developed and will be added to this handbook page.

*For current procedures, please follow the steps outlined in the sections above.*

### Root Cause Analysis

All resolved issues require root cause classification:

|Label|Category|Description|Examples
|---|---|---|---
|`RC::Technical-Implementation`|Technical|Code logic errors, implementation issues, technical debt|Join logic errors, optimization issues
|`RC::Data-Integration`|Integration|Cross-system issues, pipeline failures|ETL failures, sync errors
|`RC::Quality-Assurance`|Testing|Testing gaps, validation misses, monitoring failures|Missing dbt tests, no alerts
|`RC::Process-Business-Rules`|Process|Documentation gaps, business rules, training needs|Unclear requirements, process gaps
|`RC::Source-System`|External|Source system configurations, refresh timing|Vendor issues, API changes

### Prevention Framework

<details>
<summary><b>Prevention Scoring</b></summary>

Assign a prevention score (1-5) to each resolved issue:

|Score|Definition|Required Action
|---|---|---
|**5**|Highly Preventable - Basic checks should have caught|Document prevention measures
|**4**|Easily Preventable - Simple validation would help|Add monitoring/tests
|**3**|Moderately Preventable - Requires process changes|Consider improvements
|**2**|Difficult to Prevent - Complex dependencies|Monitor for patterns
|**1**|Not Preventable - External factors|Document for awareness

**For scores 4-5:** Specify prevention measures in the issue

#### Prevention Guidelines by Root Cause

|Root Cause Category|Typical Score|Common Prevention Measures
|---|---|---
|RC::Quality-Assurance|4-5|Add dbt tests, Monte Carlo monitors
|RC::Process-Business-Rules|3-4|Update documentation, training
|RC::Technical-Implementation|3-4|Code reviews, refactoring
|RC::Data-Integration|2-3|Cross-system validation
|RC::Source-System|1-2|External monitoring, vendor communication

</details>

<details>
<summary><b>Resolution Checklist</b></summary>

Complete all items in the resolution checklist provided in the issue template, ensuring:

- Root cause is documented with appropriate RC label
- Prevention score (1-5) is assigned
- For scores 4-5: Prevention measures are specified
- All validation steps are completed
- Stakeholders are notified

*Refer to the Data Quality issue template for the complete checklist.*

</details>

### Escalation to Incident

If a DQ issue requires immediate intervention:

1. Check if it meets [incident criteria](/handbook/enterprise-data/data-governance/incident-management/#1-incident-definition):
   - SLO breach
   - Immediate business impact
   - Requires urgent action
2. If yes, convert using `/type incident`
3. Follow [Incident Management procedures](/handbook/enterprise-data/data-governance/incident-management/)

## Quarterly Data Quality Retrospective

### Purpose

The quarterly retrospective drives continuous improvement by:

- Identifying patterns across individual issues
- Understanding root causes beyond symptoms
- Sharing knowledge across teams
- Shifting from reactive to proactive quality management

### Owners

-- Data Governance Team will performing activities as mentioned in the process.

### Process

#### 1. Data Collection

- Compile all DQ issues from the quarter
- Include Monte Carlo alerts and Tableau monitoring
- Document: Issue details, root cause, impact, resolution

#### 2. Analysis

- Categorize by dimension, severity, and root cause
- Calculate metrics:
  - Issue volume by domain
  - Mean Time to Resolution (MTTR)
  - Recurrence rates
  - Prevention score distribution

#### 3. Sharing the Findings from Retrospective

**Content:**

- DQ metrics and trends
- Celebrate wins and improvements
- Recurring pattern analysis
- Suggest prevention strategies
- Prioritize improvement actions

#### 4. Action Planning

- Assign owners to improvements
- Set implementation timelines
- Update documentation
- Schedule follow-ups

#### 5. Progress Tracking

- Monitor improvement effectiveness
- Adjust strategies based on outcomes
- Report to Data Extended Leadership and Data Team

## Roles & Responsibilities (RACI Matrix)

|Activity|Data Governance|Functional Analytics|Data/Engineering|Business Stakeholders
|---|---|---|---|---
|**Program Strategy**|R, A|C|C|I
|**Issue Detection**|I|R|R|R
|**Issue Triage**|A|C|C|I
|**Issue Remediation**|C|R|R|I
|**Metric Definitions**|R|A|C|C
|**Quality Monitoring**|A|R|R|C
|**Prevention Measures**|R|C|R|I
|**Retrospectives**|R, A|C|C|I
|**Communication**|A|R|C|I

*R = Responsible (does the work), A = Accountable (decision maker), C = Consulted (input), I = Informed (updated)*

### Key Responsibilities by Role

#### Data Governance Team

- Lead program strategy and implementation
- Design and maintain quality frameworks
- Conduct stakeholder assessments
- Facilitate quarterly retrospectives
- Maintain handbook documentation
- Report to Data Extended Leadership

#### Functional Analytics Teams

- Maintain accurate metric definitions
- Define quality monitoring metrics for owned domains
- Lead remediation for domain-specific issues related to business logic within out data/analytics models
- Participate in retrospectives
- Contribute to data catalog (Atlan)

#### Analytics/Data Engineering Teams

- Implement high-quality data products
- Establish proactive monitoring
- Expand Monte Carlo coverage
- Execute technical remediation
- Participate in retrospectives

## Platform & Monitoring Strategy

### Current Tools

|Tool|Purpose|Current Use
|---|---|---
|**Snowflake**|Data Platform|Native quality testing, data profiling
|**dbt**|Transformation|Quality tests in pipelines
|**Tableau**|Visualization|Quality metrics dashboards, trend reporting
|**GitLab**|Issue Tracking|DQ issue management

### Planned Enhancements

#### Monte Carlo Implementation

- Add/Modify alerts as needed for issue identification including Data freshness and volume monitoring for models/tables

#### Atlan Integration

- Expand usage as centralized source for metric definitions
- Data lineage tracking for impact analysis
- Business glossary maintenance

#### Enhanced dbt Testing

- Increase test coverage across critical data models
- Custom business rule validation
- Improved test documentation

#### Tableau Quality Scorecards

- Build domain-specific quality dashboards
- Track DQ metrics and trends
- Executive summary views

## Additional Resources

### Documentation

- [Data Quality Issue Template](https://gitlab.com/gitlab-data/analytics/-/issues/new?issuable_template=data_quality_issue)
- [Incident Management](/handbook/enterprise-data/data-governance/incident-management/)
- [Data Governance](/handbook/enterprise-data/data-governance/)
- [Data Team Workflow](/handbook/enterprise-data/how-we-work/)
- [Data Platform](/handbook/enterprise-data/platform/)
- [Data Sources & SLOs](/handbook/enterprise-data/platform/#data-sources)

### Quick Links

- **Report Issue:** [New DQ Issue](https://gitlab.com/gitlab-data/analytics/-/issues/new?issuable_template=data_quality_issue)
- **View Issues:** [Open DQ Issues](https://gitlab.com/gitlab-data/analytics/-/issues?label_name%5B%5D=Data+Quality+Issue)
- **Slack:** #data-team, #data-governance-quality
- **Office Hours:** [Data Team Calendar](/handbook/enterprise-data/how-we-work/calendar/)

---

*This page is maintained by the Data Governance & Quality team. For questions or suggestions, please reach out in #data-team or open an issue.*
