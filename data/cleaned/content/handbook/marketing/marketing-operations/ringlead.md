---
title: "Ringlead"
description: "The Ringlead platform orchestrates Salesforce and Marketing Automation processes like managing duplicates, data normalization, segmentation, enrichment."
---

### About Ringlead

RingLead is a SaaS application designed to enable sales and marketing to become efficient and productive.

The Ringlead platform orchestrates Salesforce and Marketing Automation processes like managing duplicates, data normalization, segmentation, enrichment.

As an introduction, below are a few items that will help with using the platform and understand how their tools help us reach our data goals.

<table>
  <tr>
        <td style = "text-align: center;"> <b>Product</b> </td>
                 <td style = "text-align: center;"> <b>Overview</b> </td>
                         <td style = "text-align: center;"> <b>Feature</b> </td>
                                 <td style = "text-align: center;"> <b>Description </b> </td>
   </tr>
   <tr>
        <td rowspan = "4" style = "text-align: left; vertical-align: top;"> <b> Cleanse </b> </td>
          <td rowspan = "4" style = "text-align: left; vertical-align: top;">Cleanse your database by removing costly duplicates or hundreds of custom object records while creating data records that are standardized and easily update with Cleanse. </td>
              <td style= "text-align: left; vertical-align: top;"> <a href = "www.help.zoominfo.com/lightning/articles/help/Overview-of-Salesforce-Deduplication-Best-Practices"> Overview of Salesforce Deduplication Best Practices</a> </td>
                <td style= "text-align: left; vertical-align: top;"> Scan    your database for duplicates based on specific criteria                                             that you define. Once you've identified your duplicates, easily merge them saving you storage costs and time. </td>
   </tr>
     <tr>
         <td style= "text-align: left; vertical-align: top;"> <a href = "www.help.zoominfo.com/lightning/articles/help/Overview-of-Normalization-Rules-in-RingLead">Overview of Normalization Rules in RingLead</a> </td>
            <td style= "text-align: left; vertical-align: top;"> Standardize your    addresses, websites, phone numbers, and more to keep data easy to    navigate and search on </td>
  </tr>
     <tr>
          <td style= "text-align: left; vertical-align: top;"> <a href = "www.help.zoominfo.com/lightning/articles/help/How-to-Create-and-Run-a-Mass-Update-Task">How to Create and Run a Mass Update Task</a> </td>
            <td style= "text-align: left; vertical-align: top;"> Update fields on custom and standard objects after filtering and defining your new values </td>
   </tr>
     <tr>
          <td style= "text-align: left; vertical-align: top;"> <a href = "www.help.zoominfo.com/lightning/articles/help/How-to-Mass-Delete-Leads-with-Last-Activity-Greater-Than-2-Years">How to Mass Delete Leads with Last Activity Greater Than 2 Years</a> </td>
            <td style= "text-align: left; vertical-align: top;"> Clean out your Salesforce by deleting custom and standard objects </td>
  </tr>
     <tr>
         <td rowspan = "6" style= "text-align: left; vertical-align: top;"> <b>Enrichment </b> </td>
            <td rowspan = "6" style= "text-align: left; vertical-align: top;"> Make the most out of the data you have and fill in the gaps where you don't. Company firmographics and contact data can be completed and updated with this tool. Use your existing vendor, or let us help you find the best data from any vendor. </td>
            <td style= "text-align: left; vertical-align: top;"> <a href = "www.help.zoominfo.com/lightning/articles/help/How-to-Perform-Salesforce-Mass-Enrichment">How to Perform Salesforce Mass Enrichment</a> </td>
            <td style= "text-align: left; vertical-align: top;"> Enrich records directly from any data vendor. </td>
   </tr>
     <tr>
          <td style= "text-align: left; vertical-align: top;"> <a href = "https://university.zoominfo.com/formcomplete-made-easy"> FormComplete Made Easy </a> </td>
          <td style= "text-align: left; vertical-align: top;"> Allow web form users to spend less time entering data with a RingLead powered address search    right on your form </td>
   </tr>
     <tr>
          <td style= "text-align: left; vertical-align: top;"> <a href = "https://api-docs.zoominfo.com/#4d0c0007-bb7c-4eea-a2a0-53b01730713f">API Enrichment</a> </td>
            <td style= "text-align: left; vertical-align: top;"> Enable expanded data    such as addresses and company information to come in with your form submissions </td>
  </tr>
     <tr>
         <td style= "text-align: left; vertical-align: top;"> <a href = "www.help.zoominfo.com/lightning/articles/help/Instant-Enrich-Explained">Instant Enrich Explained</a> </td>
          <td style= "text-align: left; vertical-align: top;"> Enrich data directly within your Salesforce Lead, Contact, and Account objects </td>
  </tr>
  <tr>
        <td style= "text-align: left; vertical-align: top;"> <a href = "https://university.zoominfo.com/ringlead-multi-vendor-enrich-overview-for-admins-live-webinar"> RingLead Multi-Vendor Enrich Overview for Admins (Live Webinar)</a> </td>
          <td style= "text-align: left; vertical-align: top;"> Enrich data using a data vendor outside of RingLead. </td>
   </tr>
  <tr>
        <td style= "text-align: left; vertical-align: top;"> <a href = "www.help.zoominfo.com/lightning/articles/help/Package-Manage-Explained">Package Manage Explained</a> </td>
          <td style= "text-align: left; vertical-align: top;"> Having multiple vendors with multiple delivery mechanisms can be challenging and Package Management offers a way to consolidate these into an easy to use and codeless system. </td>
  </tr>
</table>

Currently, GitLab, uses Ringlead's Cleanse capabilities, specifically Deduplication, while the enrichment is done through [Zoominfo](/handbook/marketing/marketing-operations/zoominfo/), our SSOT when it comes to lead/contact enrichment.

### Set Up & Access

Currently, Sales & Marketing Operations have access to Ringlead. To request access [please follow the access request process](/handbook/eta/corporate-it/end-user-services/access-requests/access-requests/) as outlined in the business operations handbook.

### Ways to access Ringlead & Help

Once you have access you can follow [this link](https://dms.ringlead.com/auth/login/?next=/) to login. For more information about Ringlead and it's capabilities please visit the [Ringlead Overview](https://help.zoominfo.com/s/article/Overview-of-RingLead).

## Current Process & Order of Operations

Deduplication and cleaning up a CRM database requires some thought on the processes needed to be successful.  It will depend a lot on what our urgent problems are and our final goals. Below you will see the best practices, using Salesforce as the example, recommendations which Ringlead customers can use to help achieve their goal of clean, efficient and usable data by starting with their main object. Your main object is your ultimate parent (Accounts frequently in Salesforce as an example). That object should be cleaned first of duplicates then move down to the next level and so on. Please see below for our basic Salesforce Recommendations.

Finding and merging duplicate records is easy with RingLead while preventing valuable data from being lost. When merging duplicates, Surviving Field Value Rules can be set for each field resulting in the chosen Master record having the best, most recent and most valuable data. Since you will have complete, precise control over the values that survive in the Master, you can safely merge large numbers of duplicate record groups automatically.

Marketing Operations works with the tool in order to deduplicate the existing leads and contact records, as well as any other custom objects that need deduplication.

Lead and Contact objects are being worked by Marketing Operations while the Account object, by Sales Operations.

Increasing the database cleanliness through deduplication is important and there are good ways and bad ways to go about it. Organizations need to make sure they follow the correct order of operations in order to achieve a clean database. In the current process, MOps and SOps are using the Ringlead's guidance for proper deduplication of our database.

## ⚠️ Before You Execute: RingLead Merge Timing & False MQL Stamps

When RingLead merges duplicate records in Salesforce, a timing-dependent race condition in Marketo can result in false MQL stamps.

**Critical configuration requirement**: The `RingLead Merge Date/Time` field must be set to populate with datetime on merge to support the [Rescoring Automation](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC22871A1ZN19).

The issue occurs because when activities from both records merge, the Person Score inflates and may trigger the [MQL Stamp campaign](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC13588C3ZN19) before the `RingLead Merge Date/Time` field syncs from SFDC to Marketo. Due to SFDC-to-Marketo sync latency (typically 5 minutes, longer during backlogs), the merge field may not populate within the campaign's 2-minute wait step. This means the MQL stamp fires before the Rescoring Automation can properly recalculate the score, resulting in false MQLs that need to be manually reversed.

### Dedupe Guidance

Marketing Operations should monitor `RingLead Merge Date/Time` field reliability and for MQL volume spikes during merge periods. When building score-based campaigns, always include `RingLead Merge Date/Time` removal logic in triggers with minimum 2-minute wait steps, and consider additional filters like recent activity or "not merged" status for extra protection.

For deduplication projects, plan merges during low-traffic hours in smaller batches of 100-500 records, run a test batch of 50 records first to validate timing, monitor the sync queue throughout execution, and communicate with Sales Dev and Analytics about potential false MQLs. Build in time for post-project MQL audit and cleanup, and for large-scale projects (10,000+ records), consider temporarily pausing/excluding the record so they aren't picked up by the MQL Stamp campaign during execution.

**Note:** There's no way to remove SLA data from affected leads. Managers can exclude specific lead IDs from reporting if they're skewing team averages.

### Recommended order of operations

1. Lead Deduplication (Completed & Automated - runs weekly on Saturdays)
2. Account Deduplication (Taking place using Openprise as the tool of choice and is run by Sales Operations)
3. Converting Leads to New Contacts (This step is skipped in our case since it would impact sales workflow considerably. We will re-evaluate if the sales team is not as heavily focused on leads as we are now.)
4. Contact Deduplication (Completed & Automated - runs weekly on Saturdays)
5. Lead to Contact Deduplication (Completed and working on Scheduled Task)
6. Deduplication of Custom Objects (only if needed)

### Account Deduplication

Account deduplication is currently being managed by Sales Ops. The deduplication job applies for Prospect Accounts w/o ZI Company ID and runs weekly every Saturday at 12:00 PDT.

### Lead to Lead Deduplication

Lead to Lead deduplication is managed by Marketing Ops and is taking place on a weekly basis on Saturdays. From the deduplication job certain lead records are excluded, as follows:

- Records that have a value in the Impartner Partner Account field;
- Records that are actively being sequenced;
- Records which status is Qualifying or Qualified;
- Records for which either the Last Name or Company Name is `[[unknown]]`

### Contact to Contact Deduplication

Contact to Contact deduplicaion, as the lead to lead deduplication, is managed by Marketing Ops and is taking place on a weekly basis on Saturdays. From the deduplication job certain contact records are excluded, as follows:

- Records that have Account Type = `Partner`;
- Records that are actively being sequenced;
- Records which status is Qualifying or Qualified;
- Records for which either the Last Name or Account Name is `[[unknown]]`
- Records that are flagged as being on an open quote using the **On Open Quote** checkbox;
- Records that are marked as current customers with the **Current Customer** checkbox;

### Lead to Contact Deduplication

Lead to Contact deduplicaion is managed by Marketing Ops and the first batch of deduplication is completed for FY25Q4. Marketing Ops is looking into resolving the MQL stamp/Rescoring automation to turn on the scheduled job. From the deduplication job certain Leads and contacts records are excluded, as follows:

**Lead Record Filters**

- Records that have a value in the Impartner Partner Account field;
- Records that are actively being sequenced;
- Records which status is Qualifying or Qualified;
- Records for which either the Last Name or Company Name is `[[unknown]]`;
- Records which Lead Source doesn't start with UserGems

**Contact Record Filters**

- Records that have a value in the Impartner Partner Account field;
- Records that have Account Type = `Partner`;
- Records that are actively being sequenced;
- Records which status is Qualifying or Qualified;
- Records for which either the Last Name or Account Name is `[[unknown]]`
- Records that are flagged as being on an open quote using the **On Open Quote** checkbox;
- Records that are marked as current customers with the **Current Customer** checkbox;
- Records which Lead Source doesn't start with UserGems

### Custom Object Deduplication

Once all the standard fields have been deduplicated in the correct order of operations, we can move to custom object deduplication to make sure all our custom objects are clean and duplicate free as well.

## Enrichment (RingLead Enrich Premium)
 
GitLab uses RingLead Enrich Premium to enrich Salesforce Lead and Contact records via ZoomInfo. There are 10 active enrichment jobs covering approximately 719,456 records across daily, weekly, and monthly cadences.
 
There are a few active issues to be aware of:

1. Many records are being reprocessed even when no new enrichment data is available, which still updates enrichment dates and fields and inflates the volume of data changes in Salesforce unnecessarily. 
2. Monthly enrichment job dates also require manual updates each month, as RingLead only supports scheduling on a specific calendar day rather than a relative week (e.g., "2nd Thursday").
 
### Enrichment Summary
 
| Job | Object | Cadence (PT) | 
|---|---|---|
| [Leads Created in the Last 7 Days](https://gitlab.ringlead.com/enrichment/152606/general/) | Lead | Daily – 7 PM | 
| [Lead Enrichment w/ Company Unknown](https://gitlab.ringlead.com/enrichment/154809/general/) | Lead | Weekly – Thu 7 PM | 
| [Lead State Enrichment](https://gitlab.ringlead.com/enrichment/154997/general/) | Lead | Weekly – Sat 12 AM | 
| [Contact State Enrichment](https://gitlab.ringlead.com/enrichment/154998/general/) | Contact | Weekly – Wed 12 AM | 
| [Inquiry Leads – This FY](https://gitlab.ringlead.com/enrichment/154970/general/) | Lead | Monthly – 1st Friday 2 PM | 
| [MQL / Accepted / Qualifying Leads](https://gitlab.ringlead.com/enrichment/155047/general/) | Lead | Monthly – 2nd Thursday 5 PM | 
| [Inquiry Leads – Last FY](https://gitlab.ringlead.com/enrichment/155031/general/) | Lead | Monthly – 2nd Friday 2 PM | 
| [MQL / Accepted / Qualifying Contacts](https://gitlab.ringlead.com/enrichment/155047/general/) | Contact | Monthly – 3rd Thursday 7 PM | 
| [Raw Leads](https://gitlab.ringlead.com/enrichment/154973/general/) | Lead | Monthly – 3rd Friday 5 PM | 
| [Raw / Inquiry Contacts](https://gitlab.ringlead.com/enrichment/155046/general/) | Contact | Monthly – 4th Friday 7 PM | 
 
### Enrichment Jobs 
 
#### Leads Created in the Last 7 Days
 
Enrichment is managed by Marketing Ops and runs daily at 7 PM PT. Record filters — records are enriched when:
 
- Do Not Call - Direct Phone OR Do Not Call - Mobile Phone ≠ Yes
- Created Date = last 7 days
- Zoominfo Enrich Status  ≠ Enriched, No-Match
 
#### Lead Enrichment w/ Company Unknown
 
Enrichment is managed by Marketing Ops and runs weekly on Thursdays at 7 PM PT. Record filters — records are enriched when:
 
- Company contains `unknown`

**Notes:** Simple filter, no advanced logic.
 
#### Lead State Enrichment
 
Enrichment is managed by Marketing Ops and runs weekly on Saturdays at 12 AM PT. Record filters — records are enriched when:
 
- Do Not Call - Direct Phone OR Do Not Call - Mobile Phone ≠ Yes
- Person Address: Country = Canada, US
- Person Address: State is null
- Zoominfo Enrich Status = Enriched
- [Admin] Exclude from Enrichment = False
- Status ≠ Disqualified, Recycle, Ineligible

#### Contact State Enrichment
 
Enrichment is managed by Marketing Ops and runs weekly on Wednesdays at 12 AM PT. Record filters — records are enriched when:
 
- Do Not Call - Direct Phone OR Do Not Call - Mobile Phone ≠ Yes
- Person Address: Country = Canada, US
- Person Address: State is null
- Zoominfo Enrich Status = Enriched
- [Admin] Exclude from Enrichment = False

#### Inquiry Leads – This FY
 
Enrichment is managed by Marketing Ops and runs monthly on the 1st Friday at 2 PM PT. Record filters — records are enriched when:
 
- Do Not Call - Direct Phone OR Do Not Call - Mobile Phone ≠ Yes
- Inquiry Date/Time = This FY
- Status = Inquiry
- [Admin] Exclude from Enrichment = False
 
#### MQL / Accepted / Qualifying Leads
 
Enrichment is managed by Marketing Ops and runs monthly on the 2nd Thursday at 5 PM PT. Record filters — records are enriched when:
 
- Do Not Call - Direct Phone OR Do Not Call - Mobile Phone ≠ Yes
- Created Date after 2024-04-01
- Status = Accepted, MQL, Qualifying, Qualified
- [Admin] Exclude from Enrichment = False

#### Inquiry Leads – Last FY
 
Enrichment is managed by Marketing Ops and runs monthly on the 2nd Friday at 2 PM PT. Record filters — records are enriched when:
 
- Do Not Call - Direct Phone OR Do Not Call - Mobile Phone ≠ Yes
- Inquiry Date/Time = Last FY
- Status = Inquiry
- [Admin] Exclude from Enrichment = False

**Notes:** High volume. Runs the same week as MQL Leads — monitor for system load.
 
#### MQL / Accepted / Qualifying Contacts
 
Enrichment is managed by Marketing Ops and runs monthly on the 3rd Thursday at 7 PM PT. Record filters — records are enriched when:
 
- Do Not Call - Direct Phone OR Do Not Call - Mobile Phone ≠ Yes
- [Admin] Exclude from Enrichment = False
- Contact Status ∈ MQL, Accepted, Qualifying, Qualified

#### Raw Leads
 
Enrichment is managed by Marketing Ops and runs monthly on the 3rd Friday at 5 PM PT. Record filters — records are enriched when:
 
- Do Not Call - Direct Phone OR Do Not Call - Mobile Phone ≠ Yes
- Created Date after 2024-04-01
- Status = Raw
- [Admin] Exclude from Enrichment = False
 
#### Raw / Inquiry Contacts
 
Enrichment is managed by Marketing Ops and runs monthly on the 4th Friday at 7 PM PT. Record filters — records are enriched when:
 
- Do Not Call - Direct Phone OR Do Not Call - Mobile Phone ≠ Yes
- [Admin] Exclude from Enrichment = False
- Contact Status = Raw, Inquiry

### Mass Enrich Guidelines

#### Validate Picklist Values

1. Standardize Country - If Country values do not align with SFDC, standardize them in RingLead before the data reaches Salesforce.
    - In the Transform tab:
      - Add an active segment named `[Active] Country Standardization`
        - Map the vendor output values to the SFDC-accepted Country values
    - Use this instead of Salesforce automation or corrective Mass Update jobs after launch.
2. Handle State/Province Separately - Do not treat State/Province as a global mapping layer across all countries.
    - Only apply State/Province mapping for:
      - United States
      - Canada
      - Australia
    - Create individual enrichment jobs for state enrichment by supported country and limit each job to the correct audience.
3. Do not map Country Code - The returned format is not compatible with the format Salesforce expects, so mapping this field can introduce validation errors instead of improving enrichment quality.

#### Country Block List

Apply blocked-country filters at job creation rather than after launch. This prevents unnecessary credit usage and avoids enriching records from countries we do not do business in.

GitLab's blocked-country list currently includes:

- Cuba
- Iran
- North Korea
- Syria
- Russia
- Belarus
- The Crimea, Donetsk, and Luhansk regions of Ukraine

#### Scheduling and Monitoring

Stagger heavier weekly and monthly jobs where possible. Spreading job execution across different windows reduces unnecessary load on the SFDC ↔ Marketo sync and makes monitoring easier during launch and stabilization periods.

Credit usage should also be reviewed on a recurring basis. RingLead does not provide a clean in-platform view of Mass Enrich credit consumption, so usage reporting may need to be requested directly from the vendor.
