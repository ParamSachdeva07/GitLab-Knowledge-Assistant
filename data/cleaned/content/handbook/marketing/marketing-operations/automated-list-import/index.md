---
title: "Self-Service List Imports"
description: "Automated process developed by Marketing Operations to facilitate self-service list imports"
---

With the purpose of increasing efficiency through the use of automation, Marketing Operations has developed a self-service process for list imports, to be used by campaign managers when they have lists from events/other campaigns or to update the member status on field marketing events.

The objective of this process is to reduce the amount of time it takes to import a list, allowing leads to be followed up as soon as possible by SDR/BDR teams while minimising the busy work of the various teams involved.

### How it Works

1. A [google drive folder](https://drive.google.com/drive/folders/1SvDR2KW8_vtPZjJ7WWihA1iOgSJn0_fv?usp=share_link) has been created for list import uploads. This folder is listening for any new CSV that is created.
1. Once a CSV is created, it is processed through one of our systems and each record is individually validated to ensure data integrity. Certain corrections are applied like transforming country and state codes to country and state names, deleting white spaces, converting well known mistaken values to their correct form, etc.
1. The process will activate the `Interesting Moments` campaign in the Marketo program so that the Interesting Moment is correctly applied.
1. Each record is added to the Marketo program according to the [program status](/handbook/marketing/marketing-operations/campaigns-and-programs/#campaign-type--progression-status) specified in the import file.
1. At the end, a slack alert is sent on the #event_list_upload channel with a report containing information regarding created, updated and failed leads.
1. If you have a list size of over 1000 records, please open an [issue](/handbook/marketing/marketing-operations/list-import/) and assign to the marketing operations team. Please note that you will still need to clean the list, and add the relevant information (campaign member status, LIM) before handing over to Marketing Ops.

#### Video Explanation of list upload process

## How to use

### Step 1 - Before the import

Confirm you have access to the import folder, called `List Import Automation`. If you do not have access to the folder, open an AR request with the Marketing Operations team seeking access to both the `List Import Automation` and the `Report Folder`.

At time of upload, a program should already exist in `Marketo` . Campaigns are to be created by the campaign owner. For a running list of program templates, go [here](/handbook/marketing/marketing-operations/campaigns-and-programs/#how-to-clone-the-marketo-program).

Make sure that the campaign's `tokens` are filled in, which are found under the `My Tokens` tab in the main campaign. `Tokens` are used via `Smart Campaigns` to apply `Last Interesting Moments` to all leads whom appear in the campaign. The minimum `tokens` that should be used relate to the campaign's `Event Name`, `Event Date` and `Landing Page URL`. Without these filled out, `Last Interesting Moments` will fill in permanently `blank`. This does not mean your upload will fail or not complete. It just means in the LIM field you will see blank datapoints, for example: `Attended {{my.event name}}, which starts on {{my.event date}}. Location: {{my.event location}}` instead of `Attended Developer Conference, which starts on May 29, 2025, Location: San Francisco`.

Please note, the `Last Interesting Moments` and the `My Tokens` associated with them are separate from `Last Event Notes`. Tokens do not communicate with `Last Event Notes` and uploads from other columns in the list upload sheet. To ensure these are loaded correctly please make sure the SFDC campaign and the last event notes are filled out on your import sheet, Columns N and O. This will be explained more in the data cleaning steps below. Again, if this information is left blank it does not mean your import will fail, it will just be missing that information in the leads record.

### Step 2 - Add your lead data to the spreadsheet

Go to the import template [Google Sheet](https://docs.google.com/spreadsheets/d/143REaMQLyIy7to-CFktL45TTTLZxBQRJUDIOMCA3CVo/edit#gid=257616838) and make a copy of the document. This spreadsheet template allows for quick edits and faster data checks, refer to the [below instructions](#data-cleaning-instructions) for data cleanup advice. It is the responsibility of the person submitting the list to clean the list utilizing the import cleaning template.

Please review the [campaign member statuses](/handbook/marketing/marketing-operations/campaigns-and-programs/#campaign-type--progression-status) listed by campaign type - these statuses are CRITICAL to routing and follow up. Please do not use `Follow Up Requested` unless the prospect specifically asked for follow up. All member statuses correlate to scoring and automated follow up depending on the lead score, high priority status and/or white glove. If you have any quetions at all, please reach out to #mktgops and the team can help you.

<details>
  <summary markdown="span"> Click to expand screenshot</summary>

![ALT](/images/marketing/marketing-operations/automated-list-import/make-a-copy.png)

</details>

### Step 3 - Download the CSV

After you populated your spreadsheet with lead data, Download the leads tab as a `CSV`. Go to `File`>`Download`>`CSV`.

<details>
  <summary markdown="span">Click  to expand screenshot</summary>

![Download CSV](/images/marketing/marketing-operations/automated-list-import/download-csv.png)

</details>

### Step 4 - Drop the CSV in the Google Drive folder

1. Go to the [Google Drive folder](https://drive.google.com/drive/folders/1SvDR2KW8_vtPZjJ7WWihA1iOgSJn0_fv?usp=share_link) called `List Import Automation`.
1. Drop your CSV containing lead data into the folder
1. An automated process will pick up your CSV and start processing each record in your file, validating the data.

### Step 5 - Go to the `#event_list_upload` slack channel

**When the import finishes processing in Marketo, it will send a slack message with information about:**

1. Report link
1. Marketo program link
1. Records created
1. Records updated
1. Failed records

<details>
  <summary markdown="span"> Click to expand screenshot</summary>

![Slack alert](/images/marketing/marketing-operations/automated-list-import/slack-alert-import.png)

</details>

**If you want to receive these notifications you can subscribe to the import complete notification labels.**

Pubsec field marketers need to use `List Upload Complete - PubSec` label on either list import issue or another event related issue if no list upload issue is made. This is optional for private sector uploads, which use `List Upload Complete - Private Sector`. SDR/BDR/Sales can subscribe to this label to get notifications when the import is complete

### Step 6 - Review the report

1. Congrats! The import is complete. Review the information passed in the slack alert.
1. If there are failed records, review the report linked in the message. The first column, `Status`, contains useful information regarding the reason a specific lead failed to be imported.
1. If there are failed records, you can review the errors and correct them in the same report. You can then delete the first column, `Status` message, download the CSV again and reimport after correcting the errors.

<details>
  <summary markdown="span"> Click to expand screenshot</summary>

![Report status column](/images/marketing/marketing-operations/automated-list-import/report-status.png)

</details>

## Common errors

1. Country or State Failed Validation: We check the country and state values against a [strict picklist](/handbook/marketing/marketing-operations/marketo/#standardization-of-country-or-state-values). Having wrong values in those fields results in Salesforce refusing to accept to sync a new lead.
1. Missing email, last name, company, program status or marketo program name: Those fields are all required for a successful import. Missing any of them will result in an error.
1. Program status does not exist: The program status in the import file must match exactly the value in the Marketo Program. [See list here](/handbook/marketing/marketing-operations/campaigns-and-programs/#campaign-type--progression-status). We strive to catch and correct errors before the import happens but edge cases will result in an error.
1. Wrong value for `Opt-in`: This field only accepts TRUE/FALSE or YES/NO. Any other value will result in an error.
1. Missing CRM Partner ID: This field is required for joint partner or MDF Campaign type, and if missing, you'll be prompted with an error.

## Data Cleaning Instructions

{{% panel header="**Caution**" header-bg="danger" %}}
DO NOT MAKE CHANGES TO THE ORIGINAL SPREADSHEET OR INPUT DATA INTO IT. MAKE A COMPLETE COPY AS INDICATED IN THE LIST UPLOAD ISSUE TEMPLATE.

The list upload spreadsheet includes a protected range on the header. Changes to the header may break the bot. All spreadsheet changes need to be through Marketing Ops, with the following individuals having edit access: Bryce, Amy, Jameson, Rob and Jenny.
{{% /panel %}}

The following data cleanup is required for any list prior to upload or sending it to the Marketing Operations team for a manual upload. **If your spreadsheet/data does not meet these guidelines, it will error in the list upload.**

**Steps (also documented in _How it Works_ tab of the spreadsheet):**

1. Use the "Lead Data for upload" tab to drop your relevant data into the matching columns (i.e. copy the column in your file for "First Name" and paste it in the column "First Name").

1. Do not alter any rows or columns. These contain formulas that will reference your inputs and provide you with highighted errors (see clarifications below for more detail), as well as data entry that is acceptable for Marketo/Salesforce, and check the syntax of the email provided by your event organizer.

1. Check for any "warnings" highlighted in red and erroneous emails marked as `FALSE` - if there are none, you are good to go! (If there are highlighted cells, follow the instructions in the _Warning Handling_ steps below. Correct the errors and then proceed.)

1. Rename the spreadsheet to match the campaign tag name

**Error Handling:**

- **Email Syntax:** If the syntax of the email is not met (meaning it includes @ and a relevant ending such as .com or .co.uk or .io) it will be listed as FALSE under the green column headers and the email can be updated to make it ready for upload. Note that Google Sheets does not understand all email domains, such as `.mil` or `.us`, and those can be ignored

- **GitLab emails:** If the person has @gitlab in their email address, they will be highlighted in red under the blue column header and should be removed

- **Duplicate Records:** If the person is a duplicate based on email address, they will appear red under the blue column header, and should be removed from the list.

**Best Practices**

1. Member Statuses must match exactly to the program type and member status [listed](/handbook/marketing/marketing-operations/campaigns-and-programs/#campaign-type--progression-status). Definitions can also be found here. If you are updating the member status for an event where we collected registrations through a form, you must include both `No Show` and `Attended` records.

1. Remove inaccurate entries

     - `Job Title` **remove** "self", "me", "n/a", etc
     - `Phone` **remove** obvious junk numbers 0000000000, 1234567890, etc
     - `State` should be empty unless `country` equals `United States`, `Canada`, `Australia`. [Additional countries allow for state values](/handbook/marketing/marketing-operations/marketo/#standardization-of-country-or-state-values), but you must follow specific spellings for them, and state does not impact routing for them.
     - Internal GitLab employees, or hosts that we will not be following up with

1. `Washington DC` is a `State` value and is not to be split up between `City` `State`.

1. **Blank fields** are better than junk data. We have enrichment tools that are designed to write to blank fields. Also we can run reports on the blank fields to find where our data gaps are.

1. If you do not have a CONTACT `Phone` **do not** substitute the ACCOUNT `Phone` and vice versa. Leave it blank.

1. Be sure to include the country code for non-US phone numbers.

1. Sort spreadsheet by `Email Address` and remove duplicates.

1. Remove all [embargoed country](/handbook/legal/trade-compliance/) records.

1. `Zip Codes` contain five (5) numbers, States in US East may start with a `0`, make sure the `Zip/Postal Code` field is **plain text** and the leading `0` appears.

1. If list contains non-Latin characters (ex. Asian languages), it must be uploaded to Marketo using UTF-8 and UTF-16. [Marketo instructions here](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/email-marketing/email-programs/managing-people-in-email-programs/import-a-non-latin-characters-list). Salesforce Data Loader requires UTF-8 encoding, [instructions here](https://help.salesforce.com/s/articleView?id=sf.faq_import_dataloader_specialchars.htm&type=5).

1. If there are notes added to the `Last Event Notes` column, add the `SFDC campaign name` to the column titled `Last Event SFDC Campaign Name` for each lead that has notes. If there are no notes for that lead, do not add anything to either column. This column is used to automatically move notes to the `Qualification Notes` field found on lead and contact pages in Salesforce. That field is not overridden like the `Last Event Notes` field and it's where we can keep the notes for much longer.

1. If there are notes, the notes must be clear to someone who both was onsite and those who were not. Think to yourself, if someone was not there onsite, will they know what action to take as a result of these notes?

1. Format of the import file has to be CSV. Any other type of import will cause an error and a message tagging the file owner on slack will alert of this issue.

1. Record ownership will be assigned using established lead routing, which is [controlled by Traction Complete](/handbook/marketing/marketing-operations/traction-lead-complete/). For details on routing, visit the [Lead & Contact routing page](https://internal.gitlab.com/handbook/marketing/marketing-ops-and-analytics/marketing-operations/traction/).

1. `Preferred Language` must be listed as a language, not a location. See the table below for common languages.

**Opt-in information**

1. Only lead records from authorized sources -- meaning sources have legally obtained lead record data-- will be flagged as `Opted-in`. **No exceptions**

     - Pulling list of names out of LinkedIn and importing the records into SFDC **does not** qualify as compliant. In EMEA these lists _will not_ be uploaded
     - Field events that have not gained consent from the attendees that their name will be shared **are not** compliant.
     - Agreements to be contacted must explicitly state the individual has `opted-in` to receive communication and cannot leave room for nuance
     - Getting someone's name and/or business card from a meetup **does not** qualify as compliant.

1. In order to mark leads as `Opt-in = TRUE`, a record of the terms and conditions the leads agreed to upon having their data collected must be recorded. Check the `terms of service` wording has been recorded in the upload issue **before** opting in leads to receive marketing communications. No ToS, no `Opt-in`. Period. To find the appropriate language, refer to [Marketing Rules and Consent Language](https://internal.gitlab.com/handbook/legal-and-corporate-affairs/legal-privacy/#marketing-rules-and-consent-language/)

     - If there are any records who have opted out of contact for any reason, define that on the spreadsheet by selecting `Opt-in = FALSE`
     - Leave `Opt-In` empty if no other option is available

| Field Name             | Required                                  | Accepted Values                                                                                                                           | Notes                                                                                                                                                                                                                                                                   |
| ---------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Marketo Program Name   | Yes                                       | Exact name of program from Marketo                                                                                                        | This value is used to add records as campaign members in Marketo                                                                                                                                                                                                        |
| First Name             | No                                        |                                                                                                                                           |                                                                                                                                                                                                                                                                         |
| Last Name              | Yes                                       |                                                                                                                                           | Missing this value will result in an **error**                                                                                                                                                                                                                          |
| Email Address          | Yes                                       |                                                                                                                                           | Missing this value will result in an **error**                                                                                                                                                                                                                          |
| Company Name           | Yes                                       |                                                                                                                                           | Missing this value will result in an **error**                                                                                                                                                                                                                          |
| State/Province         | No but preferable for US/Canada/Australia | See values [here](#reference-values-for-picklists)                                                                                        | |
| Country                | Yes                                       | See values [here](#reference-values-for-picklists)                                                                                        | Missing this value will result in an **error**                                                                                                                                                                                                                          |
| Campaign Member Status | Yes                                       | See values and definitions for your campaign type [here](/handbook/marketing/marketing-operations/campaigns-and-programs/#campaign-type--progression-status)                     | This will determine the status in the Marketo Program                                                                                                                                                                                                                   |
| Label as Opt-In?       | No                                        | Yes/No or True/False                                                                                                                      | Leave blank if no option is provided. See details above related to marking leads as Opt-in=TRUE                                                                                                                                                                                                                                    |
| CRM Partner ID         | Required only for MDF Campaigns                                       | You can find setup instructions [here](/handbook/marketing/growth-marketing/partner-and-industry-marketing/#joint-gitlab-and-partner-campaigns) | If this import is a part of a joint event and MDF campaigns with partners, you must include the CRM Partner ID as a column in your list upload. You can find setup instructions [here](/handbook/marketing/growth-marketing/partner-and-industry-marketing/#joint-gitlab-and-partner-campaigns) |
| Preferred Language | No | Must be written exactly: French, German, Japanese, Italian, Korean, Spanish, Portuguese. Other languages available [here](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/8945). | Leave blank if value is English or unknown |
| High Priority Reason? | No | High Priority Campaign <br> White Glove  | Only used if leads [need to appear in front of SDRs quickly due to some high propensity to purchase reason](/handbook/sales/sales-development/#sdr-lead-views). More about [High Priority](/handbook/sales/sales-development/#high-priority-campaigns-and-leads). Familiarize yourself with the [white glove](/handbook/sales/sales-development/#white-glove-event-follow-up-sequences) process to determine if that dropdown should be used|

## Reference values for picklists

<details>

<summary  markdown="span"> Click to expand reference values table for Country, State, and other values </summary>

| Countries |
|-----------|
| Afghanistan |
| Aland Islands |
| Albania |
| Algeria |
| Andorra |
| Angola |
| Anguilla |
| Antigua and Barbuda |
| Argentina |
| Armenia |
| Aruba |
| Australia |
| Austria |
| Azerbaijan |
| Bahamas |
| Bahrain |
| Bangladesh |
| Barbados |
| Belarus |
| Belgium |
| Belize |
| Benin |
| Bermuda |
| Bhutan |
| Bolivia |
| Bonaire, Saint Eustatius and Saba |
| Bosnia and Herzegovina |
| Botswana |
| Bouvet Island |
| Brazil |
| British Indian Ocean Territory |
| Brunei Darussalam |
| Bulgaria |
| Burkina Faso |
| Burundi |
| Cambodia |
| Cameroon |
| Canada |
| Cape Verde |
| Cayman Islands |
| Central African Republic |
| Chad |
| Chile |
| China |
| Christmas Island |
| Cocos (Keeling) Islands |
| Colombia |
| Comoros |
| Congo |
| Congo, the Democratic Republic of the |
| Cook Islands |
| Costa Rica |
| Cote d'Ivoire |
| Croatia |
| Curaçao |
| Cyprus |
| Czech Republic |
| Denmark |
| Djibouti |
| Dominica |
| Dominican Republic |
| Ecuador |
| Egypt |
| El Salvador |
| Equatorial Guinea |
| Eritrea |
| Estonia |
| Ethiopia |
| Falkland Islands (Malvinas) |
| Faroe Islands |
| Fiji |
| Finland |
| France |
| French Guiana |
| French Polynesia |
| French Southern Territories |
| Gabon |
| Gambia |
| Georgia |
| Germany |
| Ghana |
| Gibraltar |
| Greece |
| Greenland |
| Grenada |
| Guadeloupe |
| Guatemala |
| Guernsey |
| Guinea |
| Guinea-Bissau |
| Guyana |
| Haiti |
| Heard Island and McDonald Islands |
| Holy See (Vatican City State) |
| Honduras |
| Hong Kong |
| Hungary |
| Iceland |
| India |
| Indonesia |
| Iran, Islamic Republic of |
| Iraq |
| Ireland |
| Isle of Man |
| Israel |
| Italy |
| Jamaica |
| Japan |
| Jersey |
| Jordan |
| Kazakhstan |
| Kenya |
| Kiribati |
| Korea, Democratic People's Republic of |
| Korea, Republic of |
| Kuwait |
| Kyrgyzstan |
| Lao People's Democratic Republic |
| Latvia |
| Lebanon |
| Lesotho |
| Liberia |
| Libyan Arab Jamahiriya |
| Liechtenstein |
| Lithuania |
| Macao |
| Macedonia, the former Yugoslav Republic of |
| Madagascar |
| Malawi |
| Malaysia |
| Maldives |
| Mali |
| Malta |
| Marshall Islands |
| Martinique |
| Mauritania |
| Mauritius |
| Mayotte |
| Mexico |
| Moldova, Republic of |
| Monaco |
| Mongolia |
| Montenegro |
| Montserrat |
| Morocco |
| Mozambique |
| Myanmar |
| Namibia |
| Nauru |
| Nepal |
| Netherlands |
| New Caledonia |
| New Zealand |
| Nicaragua |
| Niger |
| Nigeria |
| Niue |
| Norfolk Island |
| Norway |
| Oman |
| Pakistan |
| Palestinian Territory, Occupied |
| Panama |
| Papua New Guinea |
| Paraguay |
| Peru |
| Philippines |
| Pitcairn |
| Poland |
| Portugal |
| Qatar |
| Reunion |
| Romania |
| Russian Federation |
| Rwanda |
| Saint Barthélemy |
| Saint Helena, Ascension and Tristan da Cunha |
| Saint Kitts and Nevis |
| Saint Lucia |
| Saint Martin (French part) |
| Saint Pierre and Miquelon |
| Saint Vincent and the Grenadines |
| Samoa |
| San Marino |
| Sao Tome and Principe |
| Saudi Arabia |
| Senegal |
| Serbia |
| Seychelles |
| Sierra Leone |
| Singapore |
| Sint Maarten (Dutch part) |
| Slovakia |
| Slovenia |
| Solomon Islands |
| Somalia |
| South Africa |
| South Georgia and the South Sandwich Islands |
| South Sudan |
| Spain |
| Sri Lanka |
| Suriname |
| Svalbard and Jan Mayen |
| Swaziland |
| Sweden |
| Switzerland |
| Taiwan |
| Tajikistan |
| Tanzania, United Republic of |
| Thailand |
| Timor-Leste |
| Togo |
| Tokelau |
| Tonga |
| Trinidad and Tobago |
| Tunisia |
| Turkey |
| Turkmenistan |
| Turks and Caicos Islands |
| Tuvalu |
| Uganda |
| Ukraine |
| United Arab Emirates |
| United Kingdom |
| United States |
| Uruguay |
| Uzbekistan |
| Vanuatu |
| Venezuela |
| Viet Nam |
| Virgin Islands, British |
| Wallis and Futuna |
| Western Sahara |
| Yemen |
| Zambia |
| Zimbabwe |

**State Values**

| Country | States/Provinces |
|---------|------------------|
| Australia | New South Wales |
| | Queensland |
| | South Australia |
| | Tasmania |
| | Victoria |
| | Western Australia |
| | Australian Capital Territory |
| | Northern Territory |
| Canada | Alberta |
| | British Columbia |
| | Manitoba |
| | New Brunswick |
| | Newfoundland and Labrador |
| | Nova Scotia |
| | Northwest Territories |
| | Nunavut |
| | Ontario |
| | Prince Edward Island |
| | Quebec |
| | Saskatchewan |
| | Yukon |
| United States | Alabama |
| | Alaska |
| | American Samoa |
| | Arizona |
| | Arkansas |
| | Armed Forces Americas |
| | Armed Forces Europe |
| | Armed Forces Pacific |
| | California |
| | Colorado |
| | Connecticut |
| | Delaware |
| | Federated Micronesia |
| | Florida |
| | Georgia |
| | Guam |
| | Hawaii |
| | Idaho |
| | Illinois |
| | Indiana |
| | Iowa |
| | Kansas |
| | Kentucky |
| | Louisiana |
| | Maine |
| | Marshall Islands |
| | Maryland |
| | Massachusetts |
| | Michigan |
| | Minnesota |
| | Mississippi |
| | Missouri |
| | Montana |
| | Nebraska |
| | Nevada |
| | New Hampshire |
| | New Jersey |
| | New Mexico |
| | New York |
| | North Carolina |
| | North Dakota |
| | Northern Mariana Islands |
| | Ohio |
| | Oklahoma |
| | Oregon |
| | Palau |
| | Pennsylvania |
| | Puerto Rico |
| | Rhode Island |
| | South Carolina |
| | South Dakota |
| | Tennessee |
| | Texas |
| | United States Minor Outlying Islands |
| | US Virgin Islands |
| | Utah |
| | Vermont |
| | Virginia |
| | Washington |
| | Washington DC |
| | West Virginia |
| | Wisconsin |
| | Wyoming |

**Employees bucket (not required)**

Acceptable values:

- 1-99
- 100-499
- 500-1,999
- 2,000-9,999
- 10,000+

</details>

## FAQ

**Q: I made a mistake on my upload: Loaded to the wrong campaign, had field values in the wrong column, uploaded with the wrong status, etc. What do I do?**

A: Before re-uploading the correct list or trying to fix the error, please get in touch with MOps in the `#mktgops` Slack channel. Instructions will be provided. If you uploaded to the wrong program, we need to revert that prior to the new list being loaded, otherwise it will cause issues with lead scoring and be more challenging to correct.

**Q: Why do my interesting moments show Attended {{my.event name}}, which starts on {{my.event date}}. Location: {{my.event location}}?**

A: Your tokens were not filled out before the time of the import. A new batch campaign will need to be created to update this information.

**Q: I haven't received a notification that my import is complete, how can I check its status?**

A: If you have access to log into Marketo, navigate to the campaign and you can see the number of leads that have been loaded. Check these numbers against your CSV file to see its progress. Refresh this page periodically to see if those numbers continue to increase. If they seem to have stopped and don't match your final numbers you can notify mktgops and we can check for any failures.

**Q: Can I use this system to update information on a list that already exists? (Ex: I need to change their opt-in status or their employee bucket numbers.)**

A: Yes, you can create a CSV list with the members email and the column data you want to update and import the same way, this will update the records.

**Q: What's taking so long?!?**

A: Workato is running the leads through all the processing needed to add leads, update fields, and sync to SFDC. Due to Workato and Google Workspace's integration, there is a built-in delay to prevent the API from being over-taxed and canceling the job halfway through. With larger lists, the process can take some time but we do not expect the process to go over the 24 hour SLA. As an example; we have seen lists of non english leads of upwards of 800+ taking close to 14 hours to fully complete.

- Example: Uploaded at 1:20PM -> Progress check at 3:00PM: (467 members added so far out of the 807 total) ->
  Import Complete Message at 3:14AM.

**Q: Is there a size limit for lists?**

A: So far we have tested list sizes primarily around `1,000` leads in size. We have no reason to believe there is a limit but the list size does seem to affect processing time. If the list is 2,000 or more, consult MktgOps as this may affect processing time.

**Q: What happens after my list is loaded?**

A: Leads will be added with the requested program status to Marketo, then [scored](/handbook/marketing/marketing-operations/marketo/#mql-and-lead-scoring) and run through our operational processes in Marketo. Once that completes, they will be added to the SFDC campaign and the lead/contact is synced to SFDC. For details on routing, visit the [Lead & Contact routing page](https://internal.gitlab.com/handbook/marketing/marketing-ops-and-analytics/marketing-operations/traction/).

**Q: Tell me more about the `Follow up Requested` status.**

A: With a record marked as `Follow Up Requested`, this will score the record with 100pts, as [noted here](/handbook/marketing/marketing-operations/marketo/#auto-mql), which will then in turn show up in the [Sales Dev's team S1 (Priority 1) view](/handbook/sales/sales-development/#sdr-lead-views). Please only use this status if the lead has specifically requested follow up with sales post the event.
