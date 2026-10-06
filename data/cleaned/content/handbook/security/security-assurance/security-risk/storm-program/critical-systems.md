---
title: "Critical System Tiering Methodology"
summary: "The purpose of the Critical System Tiering Methodology is to support GitLab in identifying and understanding the specific systems utilized across the organization that are considered critical to serving GitLab's Customers."
controlled_document: true
---

{{< label name="Visibility: Audit" color="#E24329" >}}

## Purpose

The purpose of the Critical System Tiering Methodology is to support GitLab in categorizing systems based on their impact on GitLab's SaaS subscriptions (delivery of GitLab.com or GitLab Dedicated). By classifying systems into specific tiers, GitLab may appropriately prioritize risk mitigation activities and tailor internal controls.

## Scope

The Critical System Tiering methodology is applicable to all systems utilized across GitLab which are tracked within the [Tech Stack](https://app.serval.com/new-request) (internal only).

## Roles and Responsibilities

|Role|Responsibility|
|----------|------------------------------|
|[Security Risk Team](/handbook/security/security-assurance/security-risk/)|Owns the Critical System Tiering Methodology and designates Critical System Tiers for new systems through the [Business Impact Analysis](/handbook/security/security-assurance/security-risk/storm-program/business-impact-analysis/).|
|[IT Compliance](/handbook/business-technology/enterprise-applications/it-compliance/)|Supports defining of Critical System Tiers in conjunction with the Security Risk Team when new systems are added to the Tech Stack.|
|Business/Technical Owners of Systems|Provide complete and accurate data about the systems that they own so that an accurate tier is designated.|

## Critical System Tiering Procedure

Defining what a critical system means at GitLab can be complex given the nature of our environment and the number of integrations that exist across the many systems that are used to carry out business activities. GitLab's [Business Impact Analysis (BIA)](/handbook/security/security-assurance/security-risk/storm-program/business-impact-analysis/) procedure enables the designation of a Critical System Tier for a new system by the Security Risk Team. The BIA questions used to designate Critical System Tier are:

1. What is the impact of System disruption (System is unavailable)?
2. Please describe the potential impact of System disruption. Specify any GitLab team(s) affected.

The Security Risk Team judgmentally designates a Critical System Tier for the new system based on answers from the Business Owner and their own understanding of the services provided by the system. The guidelines used to distinguish each tier are described in the next section.

### Designating Critical System Tiers

Systems are designated a Critical System Tier based on the following matrix:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{border-color:black;border-style:solid;border-width:1px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-zqun{background-color:#ffffff;color:#000000;text-align:center;vertical-align:middle}
.tg .tg-knp3{background-color:#6e49cb;border-color:#000000;color:#ffffff !important;;
  text-align:center;vertical-align:middle}
.tg .tg-clye{background-color:#380d75;color:#ffffff;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-fecx{background-color:#cccccc;color:#000000;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-cc97{background-color:#380d75;color:#ffffff;text-align:center;vertical-align:middle}
.tg .tg-dxvi{background-color:#6e49cb;color:#ffffff;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-e02t{background-color:#ffffff;border-color:#000000;color:#000000 !important;;
  font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-9hzb{background-color:#FFF;font-weight:bold;text-align:center;vertical-align:top}
</style>
<table class="tg">
<tbody>
  <tr>
    <td class="tg-clye">Critical System Tier (CST) <sup style="color:#DB3B21;"><b>1</b></sup></td>
    <td class="tg-dxvi">CST Description</td>
    <td class="tg-dxvi">Examples</td>
  </tr>
  <tr>
    <td class="tg-e02t">Tier 1 Mission Critical<sup style="color:#DB3B21;"><b>2,3</b></sup></td>
    <td class="tg-zqun">Disruption or breach has an immediate and significant impact on the availability/security of GitLab SaaS subscriptions and Customer data (See <a href="/handbook/security/policies_and_standards/data-classification-standard/#data-classification-definitions">Data Classification Standard</a> for definitions).</td>
    <td class="tg-zqun">GitLab.com, Google Cloud Platform, Elastic</td>
  </tr>
  <tr>
    <td class="tg-e02t">Tier 2 Business Critical<sup style="color:#DB3B21;"><b>4</b></sup></td>
    <td class="tg-zqun">Disruption affects execution of major business functions or capabilities.</td>
    <td class="tg-zqun">Okta, Salesforce, Workday</td>
  </tr>
  <tr>
    <td class="tg-e02t">Tier 3 Business Operational</td>
    <td class="tg-zqun">Disruption affects efficiency or cost in completing standard business processes.</td>
    <td class="tg-zqun">DocuSign, Figma, Tableau</td>
  </tr>
  <tr>
    <td class="tg-e02t">Tier 4 Administrative</td>
    <td class="tg-zqun">Disruption affects productivity/well-being of individual GitLab Team Members.</td>
    <td class="tg-zqun">Vimeo, Donut</td>
  </tr>
</tbody>
</table>
<br/>

{{% panel header="**Notes**" header-bg="primary" %}}
{{% note %}}
<sup style="color:#DB3B21;"><b>1</b></sup> As an extension of tiering methodology, the [Data Classification Standard](/handbook/security/policies_and_standards/data-classification-standard/) prescribes **specific** [Security and Privacy](/handbook/security/policies_and_standards/data-classification-standard/) control requirements for each data classification level. These requirements should be followed based on a system's data classification, regardless of the system's tier.
{{% /note %}}
{{% note %}}
<sup style="color:#DB3B21;"><b>2</b></sup> Any system interacting with <b>RED Data</b> per the [Data Classification Standard](/handbook/security/policies_and_standards/data-classification-standard/#red) is considered **Tier 1 Mission Critical**, as the exposure or loss of RED data carries the highest business impact of any classification level.
{{% /note %}}
{{% note %}}
<sup style="color:#DB3B21;"><b>3</b></sup> Any system designated as a [Third Party Sub-Processor](https://about.gitlab.com/privacy/subprocessors/#third-party-sub-processors) is considered **Tier 1 Mission Critical**, as these providers process Customer data on GitLab's behalf under GitLab's Data Processing Agreements.
{{% /note %}}
{{% note %}}
<sup style="color:#DB3B21;"><b>4</b></sup> By default, any system in-scope for [SOX](https://internal.gitlab.com/handbook/internal-audit/sarbanes-oxley/) will be a **Tier 2 Business Critical** system, at minimum, as its disruption could impact GitLab's ability to execute or accurately report on major financial functions.
{{% /note %}}
{{% /panel %}}

{{% panel header="**Why do we differentiate between impact on SaaS subscriptions vs. major business functions or capabilities?**" header-bg="warning" %}}
Critical System Tiers help prioritize risk mitigation activities for systems critical to serving GitLab's Customers. GitLab's core service offerings are  SaaS.  Thus, the systems that have an immediate and significant impact on the availability/security of GitLab SaaS subscriptions and Customer data in the event of a disruption are priority.  These are *Tier 1 Mission Critical* systems.
{{% /panel %}}

### Why does GitLab need this methodology?

Tiering systems utilized across GitLab enables team members to make decisions on prioritizing work related to a specific system(s). For example, if multiple risks have been identified across many systems and require remediation, team members can leverage the designated Critical System Tiers to make decisions on how to prioritize remediation efforts. This methodology also provides GitLab with a mechanism to easily identify systems which are most critical across the organization so that teams can proactively protect and secure those systems.

### Maintaining Critical System Tiers

Critical System Tiers for existing systems are validated periodically. A system's designated tier can be found in the [tech stack](https://app.serval.com/new-request) (internal only) which is the Single Source of Truth for all systems used at GitLab.

## Exceptions

Exceptions to this procedure will be tracked as per the [Information Security Policy Exception Management Process](/handbook/security/controlled-document-procedure/#exceptions).

## References

- [Business Impact Analysis](/handbook/security/security-assurance/security-risk/storm-program/business-impact-analysis/)
- [Data Classification Standard](/handbook/security/policies_and_standards/data-classification-standard/)
