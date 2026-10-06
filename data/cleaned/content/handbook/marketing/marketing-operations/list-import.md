---
title: "List Imports"
description: "Processes for importing records into Marketo"
---

**For event or other lead generation campaign list uploads, please use the instructions for [self-service uploads](/handbook/marketing/marketing-operations/automated-list-import/)**.

The following information is for manual list uploads only. If you are unable to use the self-service import for an event/campaign upload, please [open an issue](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new?type=ISSUE&description_template=event-clean-upload-list) with Marketing Operations for assistance.

## Import Methods and their SLA

For non-event/campaign list uploads, there are a couple of ways to get leads into our systems.

| Import Method | SLA | Submission Instructions | Operations Instructions |
| :------------ | :-- | :---------- | :-------- |
| Zoominfo w/in SFDC | self-managed | [Instruction video how to do this can be found in the handbook](/handbook/marketing/marketing-operations/zoominfo/) | Not applicable |
| csv file | **Accepted by OPS** - 24 business hours<br><br>**Upload to SFDC** - up to 5 business days | Use [MktgOPS **general** list import request template](https://gitlab.com/gitlab-com/marketing/marketing-operations/issues/new?issuable_template=general-list-import-request), format as a Google Sheet (Gsheet) & place **link to Gsheet in issue**<br><br>Written Instructions how to use template | Ad Hoc Upload |

The SLA for each import method has been decided based on the perceived optimal response time. If a list of prospects cannot be considered "warm", please expect a turnaround time of the listed 5 day SLA and use the appropriate template.

**If a last minute request, please indicate the rush request in your issue or ping OPS in `#mktgops` slack channel to discuss options**

## Import Cleaning Template - Info for Pre-MktgOps Hand-off

Please find detailed data cleaning, formatting, and required data instructions on the [self-service page, under Data Cleaning Instructions](/handbook/marketing/marketing-operations/automated-list-import/#data-cleaning-instructions). The process is the same for both types of imports.

If your list load is being completed by MOps, please complete the additional following steps after cleaning your data file.

1. Give `edit access` of the spreadsheet to the relevant MktgOps member
1. Post a link to the spreadsheet in the list upload issue. Provide as Google Sheet in the upload issue. In order to protect data, **DO NOT** upload the file directly on the issue, always provide a link.
1. Apply the ~"List Upload: Ready" label to the issue

### MOps instructions for manual uploads

At time of upload, a campaign should already exist in `Marketo` . Campaigns are to be created by the campaign owner. For a running list of campaign templates, go [here](/handbook/marketing/marketing-operations/campaigns-and-programs/#how-to-clone-the-marketo-program).

### Upload Process

#### Operational uploads

In the event that a manual upload needs to occur for operational or transactional email needs. Note that this process can be variable depending on the purpose of the upload, so please use your discretion when selecting and building programs/smart campaigns.

- Use a current or create a new program or smart list within the [Non-Event List Loads](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/MF4394A1) folder or the appropriate [email program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/MF4267A1).
- For transactional emails, clone the appropriate program template. For other operational list loads, you can clone [this program](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG4420A1) to get started.
- Some notable `Operational` programs already in place are listed below with links. This section will be updated on a needed basis:
  - [Opt-Outs](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/PG6625A1)
- For transactional email list processing for security or other related notifications, be sure to run a campaign that accomplishes the flow steps outlined in the [List Processing smart campaign](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/SC24593C3ZN19).
- Preferred format for Marketo upload is .csv, but will accept an .xls, or .xlsx.

#### Campaign uploads

Campaign-related uploads. These should use the self-service import process, but in rare cases where that is not possible, the following instructions apply.

In order to assure proper attribution of `MQL Scoring` and `Last Interesting Moments`, perform the following checks before any uploads occur:

- If a campaign does not exist, tag the `Campaign Owner` on the `campaign epic` or `upload issue` to ask for campaign creation and token completion.
- Check that the campaign's `tokens` are filled in, which are found under the `My Tokens` tab in the main campaign.
  - `Tokens` are used via `Smart Campaigns` to apply `Last Interesting Moments` to all leads whom appear in the campaign. The minimum `tokens` that should be used relate to the campaign's `Event Name`, `Event Date` and `Landing Page URL`. Without these filled out, `Last Interesting Moments` will fill in permanently `blank`
- Review the components of the campaign. The needed components include:
  - `Static List(s)` in which to load lead list(s). The `static list(s)` should be renamed to resemble the program name. Depending on the campaign template, there may be more than one `static list` available. Some templates have been automated in a way that will fully launch relevant `Smart Campaigns` to append all relevant data, including `Campaign Member Statuses` and other important fields
  - `Smart Campaign` that triggers a `flow` when leads are added to the campaign's static list(s). This flow should set the following fields **if the fields are empty ONLY**: `Acquisition Program` and `Person Source` (same as `Initial Source` in SFDC), and `Change Program Status: to relevant status`. If updating no shows, you will need to add a flow step for `Registered > No Show`. On most program templates, we have a Manual List Upload Smart Campaign to help with this.
  - For campaign related uploads only: `Smart Campaign` to add an `Interesting Moment`. Check there are enough `triggers` and `flows` to activate for each `Campaign Member Status` that appears on the list. Usually these include, but are not limited to: `Attended`, `Attended On-Demand`, `Visited Booth` and `No Show`. A general rule is to not include `Registered`, `Sales Nominated` or `Marketing Nominated`. The previously mentioned `tokens` will be used to apply the full event data of the `Interesting Moments` to the leads. Depending on the template, sometimes this `Smart Campaign` and the previously mentioned campaign are one and the same

#### Best Practices and Procedure

1. Remove all unecessary data from `Job Title`, `Company`, `Names` and `Locations` columns, such as punctuation, `self`, etc, from the Google sheet before uploading. Check for any remaining duplicates and missing `Required Data`, pinging the `campaign owner` to fix, as needed
1. Only allow `Opt-in=TRUE` if the agreement to be contacted has been recorded in the list upload issue. Leave blank otherwise
1. Sort list by `Campaign Member Status` and then divide the whole list into separate tabs for the different statuses, eg. `Attended`, `Registered/No Show`, etc
1. Download the .csv file of the tabs to desktop
1. Load the corresponding .csv file to the corresponding `static list` and match up the fields on upload. These fields should mostly match automatically
     - If there is only `one static list` for the program, change the `Campaign Member Statuses` for each uploaded list before uploading the next. If all leads were uploaded at once and this is not possible, create a `Smart List` and filter by `Email Address` as a way to distinguish and change to the correct statuses
1. Always load `No Show` leads as `Registered` before setting them to `No Show`. Otherwise, they will not receive MQL scores. Check if a `Smart Campaign` changes the status to `No Show` before finalizing and if not, switch status from `Registered` to `No Show`
1. Depending on how the template has been set up, the remaining steps of appending data could be automated. If it is not, be sure to append the data listed above to the proper fields
1. After all steps of the needed `Smart Campaigns` have ran, including the often automated `Program Status: Registered -> No Show`, turn off the activated `Smart Campaigns` by "unscheduling" them
1. Check the `Loading Errors` smart list for any potential lead loading errors.
     - Check the `Person Details` on any leads that show up on the smart list and correct the error. If Marketo indicates a `duplicate`, change the name on the lead by adding random but easily identifiable characters to the last name and manually force the lead to sync with SFDC. Find the lead in SFDC and merge it with the pre-existing duplicate. If there is a differing `email address` between the records, add the new `email address` as a secondary email. Add to SFDC campaign with the appropriate `Campaign Member Status`, if necessary
1. Once the Marketo --> Salesforce sync has completed, use the [Upload checking template - do not erase](https://gitlab.my.salesforce.com/00Q?fcf=00B4M000004tTvd) lead view to check data has been applied correctly, scoring has occurred and leads have routed.  Plug the `campaign tag`, or Marketo program name, into the lead view's `campaign name` field to view leads as a list
1. Ensure the number of leads present in the Salesforce campaign matches the total number of leads from the original spreadsheet
1. Announce the upload in either the `event_list_upload` or `pub-sector-isr` Slack channels, depending on the campaign's intended `Sub-Region`. Include `Region` labels for private sector posts
1. After verified completion of all tasks, remove ~"List Upload: Ready" label and notify in the issue of upload completion. Adjust the "MktgOps" label and apply a milestone
1. Close list upload issue

### Trusted vs Non-Trusted Imports

In Marketo there is a an option to choose trusted or non-trusted sources. Non-trusted sources are for list uploads that we are not confident in the data points given to us. For example, if we are loading a list with inferred country data from IP, we do not want it to overwrite our current location data that is more accurate. Blocking updates allows for a field to be updated if blank, but will not overwrite a field that already has a value.

Here is the list of fields that are blocked during a non-trusted import. If you would like to add more fields, please file an issue with the mops team.

- First Name
- Last Name
- Job title
- Company
- Country
- City
- State
- Postal Code
