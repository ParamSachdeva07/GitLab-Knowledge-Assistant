---
title: "Marketing Metrics"
description: "We use Tableau to view and analyze our marketing metrics from multiple data sources."
---

## Marketing Metrics

Below are the definitions of our primary Marketing Metrics.

### Inquiry

An inquiry is a stage of the lead/contact objects in SFDC. GitLab defines inquiry as an Inbound request or response to [an outbound marketing effort](/handbook/marketing/marketing-operations/#lead-and-contact-statuses).

#### First Order Inquiries

Inquiries that are part of a parent account that has not made an order through GitLab are classified as first order inquiries. To find them, we join the account table to the person table on the inquiry's account ID. If the field `has_first_order_available` is true on the corresponding account object, the inquiry is first order. If the inquiry does not have an account associated with it, it is also first order.

#### Date of Inquiry

Finding when a person became an inquiry requires accounting for person records who skipped the inquiry stage. To do this take the lesser of `inquiry_date` and `inquiry_inferred_date`.

The logic for finding when a person became an inquiry is captured in the `true_inquiry_date` field. It should always be used to report inquiries unless you are looking for something specific.

#### Technical Definition

Any lead or contact with `Status != to Raw` and the first date between Inquiry Date and Inquiry Inferred.
Any lead or contact from the fct_crm_person table where `Status != to Raw` and `inquiry_date` or `inquiry_inferred_date` is not null.

Example Query, this will return a list of inquiries with the date they became an inquiry:

```sql
  SELECT
  dim_crm_person_id,
  sfdc_record_id,
  email_hash,
  inquiry_reporting_date
  FROM common_mart_marketing.mart_crm_person
  where
  lower(Status) != 'raw`
  and true_inquiry_date is not null
```

#### Source & Metric

An Inquiry is defined by records in the [Person Mart](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.mart_crm_person). To find the number of inquiries, take the unique count of `email_hash`

### MQL

A Marketing Qualified Lead (MQL) is a stage of the lead/contact objects in SFDC. GitLab defines an MQL as a person who is [Marketing Qualified through systematic means](/handbook/marketing/marketing-operations/#lead-and-contact-statuses).

#### First Order MQLs

MQLs that are part of a parent account that has not made an order through GitLab are classified as first-order MQLs. To find them, we join the account table to the person table on the MQL account ID. If the field `has_first_order_available` is true on the account, the MQL is first order. If the MQL does not have an account associated with it, it is also first order.

There is a set of fields that show information regarding the First Order (FO) status of a MQL:

1. `Is First Order Person` - this shows whether or not the record is currently a FO record
1. `FO Intial MQL` - this shows whether or not, at the time of the `Intitial MQL DateTime` (the first time the record MQL'd), the record was a FO record
1. `FO MQL` - this shows whether or not, at the time of the `MQL DateTime` (the most recent time the record MQL'd), the record was a FO record

#### Date of MQL

To find the date of when someone became an MQL, we use the date field from Marketo (`Marketo MQL DateTime` in SFDC). While this field is not stampted and can change if someone re-MQLs, it makes our reporting easier to understand, matches what Sales Development uses, and matches the data in Marketo.

#### Technical Definition

Any lead or contact from the [fct_crm_person](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.fct_crm_person) table where the MQL is not null.

This is captured in the [fct_crm_person](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.fct_crm_person) table by the `is_mql = TRUE`.

Example Query, this will return a list of MQLs with the date they became an MQL:

```sql
  SELECT
  dim_crm_person.dim_crm_person_id,
  dim_crm_person.sfdc_record_id,
  Dim_crm_person.email_hash,
  collate(mql_date_latest_pt, inferred_mql_date_latest) as mql_date
  FROM mart_crm_person
  where
  is_mql = TRUE
```

#### Source

An MQL is defined by records in the [Person Mart](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.mart_crm_person).

### SAO

A Sales Accepted Opportunity (SAO) is an Opportunity that has reached the accepted stage, the criteria to accept or reject an opportunity is set by sales and defined in [their handbook](/handbook/sales/field-operations/gtm-resources/).

#### First Order SAOs

SFDC stamps the order type on each SAO when it is created, meaning that each SAO knows its order type. The `order_type` field stores this information.
The logic for first-order SAOs is captured in the `is_new_logo_first_order` flag. It should always be used when querying for FO SAOs.

#### Date of SAO

To find the date the opportunity became an SAO, use the `sales_accepted_date` field.

#### Technical Definition

Any opportunity from the [fct_crm_opportunity](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.fct_crm_opportunity#description) table where the stage_name is not `10-Duplicate` and `is_edu_oss` is 0, and the sales_accepted_date is not null.
These conditions are captured in the `is_sao` field on the fct_crm_opportunity table.

Example Query

```sql
SELECT
sales_accepted_date,
dim_crm_opportunity_id
FROM mart_crm_opportunity
WHERE
is_sao = TRUE
and is_new_logo_first_order = TRUE
```

#### Source

An SAO is defined by records in the [Opportunity Mart](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.mart_crm_opportunity).

### Closed Won Opportunity

A Closed Won Opportunity (CW) is an opportunity where the sales team won the deal.

#### First Order CW Opportunities

Because a closed-won deal is an opportunity, the order_type field stores the first order information.
When querying for First Order Closed Won, it's best to use the `is_new_logo_first_order` flag, this ensures that all our dashboards are using the same logic to find FO CW.

#### Date of Closed Deal

To find the date the opportunity closed, use the `close_date` field.

#### Finding Net ARR for an Opportunity

When reporting on the [Net ARR](/handbook/sales/sales-term-glossary/arr-in-practice/) of a closed deal, we need to ensure the deal will contribute to the company's Net ARR. To this, add the `is_net_arr_closed_deal` flag as true to the query.

#### Technical Definition

Any opportunity from the [fct_crm_opportunity](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.fct_crm_opportunity#description) table where the stage_name is not `10-Duplicate` and `is_edu_oss` is 0, and the `is_won` is true, and `is_closed` is true.

These conditions are captured in the `is_closed_won` field on the fct_crm_opportunity table. The `is_closed_won` field should always be used when querying for closed-won deals.

Example Query

```sql
SELECT
sales_accepted_date,
dim_crm_opportunity_id
FROM mart_crm_opportunity
WHERE
is_closed_won = TRUE
and is_new_logo_first_order = TRUE
and is_net_arr_closed_deal = TRUE
```

#### Source

A CW Opportunity is defined by records in the [Opportunity Mart](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.mart_crm_opportunity).

### Marketing trial sign up flow

We use a variety of methods and systems to collect leads and understand how people discover GitLab. This is a basic overview of these visitors move through marketing systems.
Note: The time delay between a record being added to SFDC and the time it takes to process in Marketo, get a score, and get pushed back to SFDC as a MQL causes a discrepancy between Inquiries and MQLs for trials on a given day or in a given month (when the trial occurs on the first/last day of the month) when viewed on the [Marketing Metrics Dashboard](https://app.periscopedata.com/app/gitlab/431555/Marketing-Metrics).

![Trial sign up flow](/images/handbook/marketing/marketing-operations/trial-sign-up-flow.png)

## Lead Source Buckets

To give executives a better view of lead sources and showing where leads and contact are sourced from we created a bucketed feild. Its often refered to as `lead source buckets` in Tableau.

Below is the table mapping for each lead source and its Source Bucket.

| Initial Source                                                                                                         | Source Bucket      |
|------------------------------------------------------------------------------------------------------------------------|--------------------|
| Advertisement                                                                                                          | paid demand gen    |
| AE Generated                                                                                                           | AE Generated       |
| CE Download                                                                                                            | product            |
| CE Usage Ping                                                                                                          | product            |
| Channel Qualified Lead                                                                                                 | partner marketing  |
| Clearbit                                                                                                               | SDR prospecting    |
| Conference                                                                                                             | paid demand gen    |
| CORE Check-Up                                                                                                          | product            |
| Datanyze                                                                                                               | SDR prospecting    |
| Demo                                                                                                                   | organic inbound    |
| DiscoverOrg                                                                                                            | SDR prospecting    |
| Drift                                                                                                                  | organic inbound    |
| Education                                                                                                              | organic inbound    |
| Email Request                                                                                                          | organic inbound    |
| Email Subscription                                                                                                     | organic inbound    |
| Employee Referral                                                                                                      | other              |
| Event Partner                                                                                                          | partner marketing  |
| Executive Roundtable                                                                                                   | paid demand gen    |
| Existing Client                                                                                                        | product            |
| External Referral                                                                                                      | product            |
| Field Event                                                                                                            | paid demand gen    |
| Gainsight                                                                                                              | product            |
| Gated Content                                                                                                          | organic inbound    |
| Gated Content -                                                                                                        | organic inbound    |
| Gated Content - Demo                                                                                                   | organic inbound    |
| Gated Content - eBook                                                                                                  | organic inbound    |
| Gated Content - General                                                                                                | organic inbound    |
| Gated Content - Report                                                                                                 | organic inbound    |
| Gated Content - Reports                                                                                                | organic inbound    |
| Gated Content - select one (you may NOT choose from an option other than these): whitepaper,report,video,eBook,general | organic inbound    |
| Gated Content - study                                                                                                  | organic inbound    |
| Gated Content - Video                                                                                                  | organic inbound    |
| Gated Content - webcast                                                                                                | organic inbound    |
| Gated Content - Whitepaper                                                                                             | organic inbound    |
| GitLab DataMart                                                                                                        | product            |
| GitLab Subscription Portal                                                                                             | product            |
| GitLab.com                                                                                                             | product            |
| hopin                                                                                                                  | paid demand gen    |
| Impartner                                                                                                              | partner marketing  |
| Investor                                                                                                               | organic inbound    |
| Leadware                                                                                                               | SDR prospecting    |
| LinkedIn                                                                                                               | SDR prospecting    |
| List - DB - GACoreUpsert - 20200706                                                                                    | SDR prospecting    |
| List - Demandbase - GACoreInsert - 20200706                                                                            | SDR prospecting    |
| List-2HCentric-DB-20200914                                                                                             | SDR prospecting    |
| Newsletter                                                                                                             | product            |
| OSS                                                                                                                    | organic inbound    |
| Other                                                                                                                  | other              |
| Owned Event                                                                                                            | paid demand gen    |
| Partner                                                                                                                | partner marketing  |
| Prof Serv Request                                                                                                      | organic inbound    |
| Promotion                                                                                                              | paid demand gen    |
| Prospecting                                                                                                            | SDR prospecting    |
| Prospecting - General                                                                                                  | SDR prospecting    |
| Prospecting - LeadIQ                                                                                                   | SDR prospecting    |
| Public Relations                                                                                                       | organic inbound    |
| Purchased List                                                                                                         | SDR prospecting    |
| Registered                                                                                                             | organic inbound    |
| Request - Contact                                                                                                      | organic inbound    |
| Request - Professional Services                                                                                        | organic inbound    |
| Request - Public Sector                                                                                                | organic inbound    |
| SDR Generated                                                                                                          | SDR prospecting    |
| Security Newsletter                                                                                                    | product            |
| Startup Application                                                                                                    | product            |
| Trial - Enterprise                                                                                                     | Trial - Enterprise |
| Trial - GitLab.com                                                                                                     | Trial - GitLab.com |
| Virtual Sponsorship                                                                                                    | paid demand gen    |
| Web                                                                                                                    | organic inbound    |
| Web Chat                                                                                                               | organic inbound    |
| Web Direct                                                                                                             | Web Direct         |
| Webcast                                                                                                                | paid demand gen    |
| Word of mouth                                                                                                          | organic inbound    |
| Workshop                                                                                                               | paid demand gen    |
| ZI-EMEA-MM-OutboundQ4-2020.08.19                                                                                       | SDR prospecting    |
| Zoominfo                                                                                                               | SDR prospecting    |

## Reporting Fields Source of Truth

This section captures and links the most often used fields in reporting so that anyone pulling a Salesforce report can and is using the correct fields and the same fields that are being used in Periscope reports/dashboards.

Note: There is a current transition to move towards the [Territory Success Planning fields](/handbook/sales/field-operations/sales-systems/gtm-technical-documentation/)

### Lead

1. [Lead Source](https://gitlab.my.salesforce.com/_ui/common/config/field/StandardFieldAttributes/d?id=LeadSource&type=Lead&retURL=%2Fp%2Fsetup%2Flayout%2FLayoutFieldList%3Ftype%3DLead%26setupid%3DLeadFields%26retURL%3D%252Fui%252Fsetup%252FSetup%253Fsetupid%253DLead&setupid=LeadFields)
1. [MQL Date](https://gitlab.my.salesforce.com/00N6100000CJuLB?setupid=LeadFields) - if this is blank, the record is *not* counted as a `MQL`
1. [Sales Segment](https://gitlab.my.salesforce.com/00N6100000HHdoa?setupid=LeadFields)

### Contact

1. [Lead Source](https://gitlab.my.salesforce.com/_ui/common/config/field/StandardFieldAttributes/d?id=LeadSource&type=Contact&retURL=%2Fp%2Fsetup%2Flayout%2FLayoutFieldList%3Ftype%3DContact%26setupid%3DContactFields%26retURL%3D%252Fui%252Fsetup%252FSetup%253Fsetupid%253DContact&setupid=ContactFields)
1. [MQL Date](https://gitlab.my.salesforce.com/00N4M00000IW0Jx?setupid=ContactFields) - if this is blank, the record is *not* counted as a `MQL`
1. Sales Segment - See the Account `Sales Segment` field.

### Account

1. `Sales Segment` - Using the [Account Owner's](https://gitlab.my.salesforce.com/_ui/common/config/field/StandardFieldAttributes/d?id=Owner&type=Account&retURL=%2Fp%2Fsetup%2Flayout%2FLayoutFieldList%3Ftype%3DAccount%26setupid%3DAccountFields%26retURL%3D%252Fui%252Fsetup%252FSetup%253Fsetupid%253DAccount&_CONFIRMATIONTOKEN=VmpFPSxNakF5TVMwd05DMHhOMVF4TlRveE5qb3dOaTQzTnpOYSxURnIyR3gyTDhNSWx5dWJmTW1ObUxGLFl6UTNNekF5&setupid=AccountFields) - `User Segment`

### Opportunity

1. [SDR/BDR](https://gitlab.my.salesforce.com/00N6100000I1Y02?setupid=OpportunityFields)
1. [Closed Date](https://gitlab.my.salesforce.com/_ui/common/config/field/StandardFieldAttributes/d?id=CloseDate&type=Opportunity&retURL=%2Fp%2Fsetup%2Flayout%2FLayoutFieldList%3Ftype%3DOpportunity%26setupid%3DOpportunityFields&setupid=OpportunityFields)
1. [Net ARR](https://gitlab.my.salesforce.com/00N4M00000Ib5n8?setupid=OpportunityFields)
1. [Lead Source](https://gitlab.my.salesforce.com/_ui/common/config/field/StandardFieldAttributes/d?id=LeadSource&type=Opportunity&retURL=%2Fp%2Fsetup%2Flayout%2FLayoutFieldList%3Ftype%3DOpportunity%26setupid%3DOpportunityFields%26retURL%3D%252Fui%252Fsetup%252FSetup%253Fsetupid%253DOpportunity&setupid=OpportunityFields)
1. [Sales Accepted Date](https://gitlab.my.salesforce.com/00N6100000HmPaK?setupid=OpportunityFields)
1. [Sales Qualified Source](https://gitlab.my.salesforce.com/00N6100000HZPjd?setupid=OpportunityFields)
1. [Stage Name](https://gitlab.my.salesforce.com/_ui/common/config/field/StandardFieldAttributes/d?id=StageName&type=Opportunity&retURL=%2Fp%2Fsetup%2Flayout%2FLayoutFieldList%3Ftype%3DOpportunity%26setupid%3DOpportunityFields%26retURL%3D%252Fui%252Fsetup%252FSetup%253Fsetupid%253DOpportunity&setupid=OpportunityFields)
1. [Order Type](https://gitlab.my.salesforce.com/00N4M00000Ib8Ok?setupid=OpportunityFields)

## Useful things to know when it comes to Tableau vs. SFDC data

Given the way that our systems are connected and synched, you may see a discrepancy in the data within Tableau vs. Sales Force.com. A few things to note:

1. Opportunity amount will be updated immediately within sales force, but will NOT show up in Tableau until the next day, as our data synchs overnight.
1. There is about a 7 hour time difference between Tableau and SFDC, so this time lag can also create discrepancies as well.

## Field Marketing Metrics

This section will go into specifics on the workflow for a Field Marketer to check their results.

At the highest level, Field Marketing is responsible for helping to progress MQLs and influencing pipeline. Those MQLs will ultimately create [Sales Accepted Opportunities](/handbook/sales/field-operations/gtm-resources/#opportunities) by the Sales Development team.

### How to track the ROI of your Digital Tactics

#### 3rd Party digital agency

In order to track engagement for any work we do with on the digital side of the house, a campaign UTM code will be created. For more information on UTM's at GitLab [can be found here](/handbook/marketing/growth-marketing/digital-agency/digital-strategy-management/#utm-tracking).

You will follow this process when you are working with our 3rd party digital agency to serve your target audience ads/LinkedIn InMails.

At the highest level, it's interesting to see the spend, clicks, impressions, CPC (cost per click), inquiries, and CPI (cost per inquiry). This is done by going to the Field Marketing Specific digital spend Dashboard via our digital team, linked in the `Useful Links` section and searching for your campaign using the campaigns UTM code. Here is the report as well, because we know sometimes you just want the link in the exact place you are looking for it in ;) . [WW SFDC Field Marketing Digital Report](https://gitlab.my.salesforce.com/00O4M000004aA0V)

Inquiries (people who end up registering for your event or engaging with your ad) are the most important to look into and really the status of them attending your event or interacting with your campaign, eventually leading to an SAO and then pipeline!

If you were driving people to register for something, then hop over to your SFDC campaign. Then go down to the `Custom Links` section and click on the `View All Campaign Members` report.

You'll then want to sort by `Ad Campaign Name (FT)`, which answers the question "What was the 1st touch ad this record interacted with?" and also the `Ad Campaign Name (LC)`, which answers the question "What ad created this lead?".

If you did not have a specific SFDC Campaign you were driving to, and you wanted to see the success of your campaign, then you would still refer to the [WW SFDC Field Marketing Digital Report](https://gitlab.my.salesforce.com/00O4M000004aA0V), add in your campaigns UTM there, using the filter `Ad Campaign Name` [contains] and add your UTM.

Please note that whilst you can track leads via SFDC campaigns or UTM reports, pipeline generated should be viewed in [Tableau](https://10az.online.tableau.com/#/site/gitlab/views/DraftTDCampaigns-L2RInteractions/Overview?:iid=2) only, as SFDCs last touch model is different from our multi touch attribution model.

## Partner Marketing Reporting

We track marketing influence on channel opportunies as well as deal regisiration impact from [Market Development Funds](/handbook/resellers/channel-program-guide/mdf/).

| Report Name                                    | Platform   | Description                                                                                                                                                                                                                                  | Link                                                                                                                                  |
| ---------------------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Partner Lead Status                            | Tableau   | This dashboard shows the overview of the leads shared with partners via [Impartner](/handbook/marketing/marketing-operations/impartner/). This includes the Share Status by partners, partner leads, campaign and geo. | [🖇️](https://10az.online.tableau.com/#/site/gitlab/views/DraftPartnerMarketingv2/PartnerLeadsContacts?:iid=1)                             |
| Partner Sourced Opportunities                  | Tableau    | This dashboard shows the opportunities generated by Marketing campaigns.                                                                                                                                                                     | [🖇️](https://10az.online.tableau.com/#/site/gitlab/views/DraftPartnerMarketingv2/PartnerSourcedOpps?:iid=1)                  |
| Focus Partner Tech Capabilities                | Salesforce | This report shows all the focus partner and an overview of their company information.                                                                                                                                                        | [🖇️](https://gitlab.my.salesforce.com/00O8X00000963VI)                                                                               |
| Partner Marketing Trials Funnel - SaaS & Self Managed        | Tableau    | This dashboard shows an overview of all the SaaS & Self Managed free trial submissions by partners.                                                                                                                                                         | [🖇️](https://10az.online.tableau.com/#/site/gitlab/views/DraftPartnerMarketingv2/PartnerTrials?:iid=1) |
| Channel Partner Participation                  | Salesforce | This report captures an overview of [partner program offerings](/handbook/marketing/growth-marketing/partner-and-industry-marketing/) that partners are actively enrolled in.                       | [🖇️](https://gitlab.my.salesforce.com/00O8X00000963dq)                                                                               |
| Partner Recall Leads  & Contacts                        | Salesforce | This report captures the partner leads that have been recalled in the current FY.                                                                                                                                                            | [🖇️ Leads](https://gitlab.my.salesforce.com/00O8X000008muTH)  [🖇️ Contacts](https://gitlab.my.salesforce.com/00O8X000008muWG)                                                                        |
| MDF Funds Request with Funds Claim                       | Salesforce | This report captures a list of the current FY Funds Requests received and their respected. claims                                                                                                                                                            | [🖇️](https://gitlab.my.salesforce.com/00OPL0000002ILp)                                                                               |
| MDF Funds Request with Partner Account                       | Salesforce | This report captures a list of the current FY Funds Requests with Partner Account name filtered by status.                                                                                                                                                            | [🖇️](https://gitlab.my.salesforce.com/00OPL0000002IP3)                                                                               |
| Instant Marketing Campaigns Asset Report                       | Impartner | This report captures views, downloads, shares and cobrands of our Instant Marketing Campaigns and assets.                                                                                                                                                             | [🖇️](https://prod.impartner.live/en/s/channel-intel/dashboard/65e60883f43d1e0033b33d6e)                                                                               |

### SFDC Report Template - Records Passed to Partners

These reports are used as template for your reference. Please clone and modify the reports based on the campaign name you are wanting to dig into. Reminder that SFDC treats leads and contacts separetely, so you'll need both a leads and a contacts report to see full picture.

Note: You need to change the campaign name to the actual name of the campaign you're wanting this report for.

1. [Campaigns with Leads](https://gitlab.my.salesforce.com/00O4M000004enu7)
1. [Campaigns with Contacts](https://gitlab.my.salesforce.com/00O4M000004enuC)

- [Records passed to partners](https://gitlab.my.salesforce.com/00O8X000008RSHg) - As part of our [campaigns we run jointly with channel partners](/handbook/marketing/marketing-operations/campaigns-and-programs/#joint-gitlabpartner-campaign), we would like to understand the status of records we've passed to partners, this report give us that insight.
