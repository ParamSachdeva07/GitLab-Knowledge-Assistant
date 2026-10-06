---
title: "VAT ID and Legal Entity Name Validation"
description: "How GitLab captures and validates the sold-to customer's VAT ID and legal entity name on net-new international prospect accounts before an opportunity can be booked."
---

## Overview

As of **7 October 2026**, an opportunity on a net-new international prospect account cannot be submitted for approval until the account's Value-Added Tax Identification ("VAT ID") number and legal entity name have been validated.

**What we mean by "VAT ID".** Throughout this page, "VAT ID" and "VAT ID validation" refer to any tax identification number used to identify a business for indirect tax purposes. This includes:

- VAT numbers (for example, in the EU and UK)
- GST numbers (for example, in Australia, India, and Singapore)
- Other Tax Identification Numbers (TINs) used in the customer's country

A validation is performed via an API call from Salesforce to Fonoa, a third-party tax identification service. Fonoa checks the VAT ID against the official government database for that country and returns the registered company name and the registered address. Fonoa also returns a validation result based on the accuracy of the data sent to Fonoa in the API call. Salesforce stores the Fonoa results on the Account and compares the registered name Fonoa returns against the Salesforce Account Name.

The Salesforce Account is the system of record for the customer's legal entity. The validated Account Name and VAT ID appears on the order form and flows into the Zuora billing account when the deal is booked.

### Why this exists

GitLab validates the customer's VAT ID and registered legal entity name at the point of capture, so that the invoice applies the correct VAT. As a result, both GitLab as well as our customers are not confronted with incorrect (non-recoverable) VAT.

**Why is a valid VAT ID number of the Sold To legal entity important?**

- For GitLab: an invalid or mismatched VAT ID means VAT should have been charged but wasn't. That becomes GitLab's liability, with interest and penalties, and is rarely recoverable from the customer afterwards.
- For the customer: an invoice with an incorrect VAT ID or address is not a valid tax invoice in most jurisdictions, so they cannot reclaim the input VAT; the invoiced VAT becomes an additional cost.

Validating at the point of capture — while the Account Executive (AE) is still in conversation with the customer — prevents incorrect data reaching booking and invoicing, and removes the manual post-invoice correction cycle.

## Phase 1: criteria for when VAT validation applies

In this early roll-out of a larger implementation plan, the requirement applies to an opportunity when **both** of the following are true of its Account:

| Condition | Value |
| --- | --- |
| Account Type | Prospect |
| Account billing country | Anything other than the United States or Canada |

If either condition is not met, no banner appears and no validation is required.

Two consequences worth understanding:

- This requirement is not driven by the opportunity's Subscription Type, but rather by Account status (Prospect vs. Customer). In the future, we intend to expand this requirement to existing customers.
- **Domestic deals are unaffected.** US and Canada accounts are excluded outright.

### Out of scope for the early implementation phase ("Phase 1")

- Web direct and self-service purchases (later phase TBD)
- Renewals, amendments and add-on business (planned for Phase 2)
- Partner and reseller accounts (later phase TBD)
- US and Canada address validation
- Translation of registered names returned in a non-Latin script (planned for Phase 2)

## The VAT validation banner process

### Step 1 — The prompt appears at Stage 3

Nothing appears at Stages 1 or 2, so early-stage qualification stays frictionless.

From **Stage 3 – Technical Evaluation** onward, a persistent banner appears on the Opportunity for as long as validation is outstanding:

> Please validate the VAT ID and Legal Entity Name. You cannot book the deal until this validation is complete.

Note that booking blockage can be overridden by the Account Executive in this Phase 1; Phase 1 is implemented to understand why the override is occurring. The banner carries a **Validate VAT ID | Legal Entity Name** button and remains visible through Stages 4, 5 and 6 until validation succeeds. It disappears once the account reaches a validated state.

![Validation banner on a Stage 3 opportunity](/images/sales/field-operations/vat-id-validation/stage-3-banner.png)

### Step 2 — Run the validation

Selecting the button opens the **VAT ID Validator**. It shows the account name, the ISO country code, the address on file and the current VAT/Tax ID, and has three tabs.

![The VAT ID Validator on its TIN Validation tab](/images/sales/field-operations/vat-id-validation/validator-tin-validation.png)

#### TIN Validation tab

The default tab, and the one used in most cases.

1. Enter or confirm the **VAT / Tax ID** using information provided by the Prospect.
1. Select the **TIN Type** — Business or Individual. This determines which format and checksum rules Fonoa applies.
1. Select **Validate VAT ID**.

Fonoa runs a country-specific format pre-check first. If the format fails, the request never reaches the database and the status is set to Invalid - Format immediately.

If the format passes, Salesforce stamps the status "Pending", calls Fonoa with the ISO country code and the VAT ID, and updates the record automatically when the response arrives. There is no need to refresh the page.

#### Country-specific requirements

Certain countries have additional requirements, such as Registered Business Name, UIN, Registered Address Zip Code, etc. Please request this information from the Prospect. Such countries include:

- China
- Croatia
- Egypt
- India
- Indonesia
- Lithuania
- Malaysia
- Mexico
- Philippines
- Poland
- Spain
- Turkey

#### Response time

Depending on the country, the time required to validate varies. For the majority of countries, validation occurs within seconds. For some countries, the validation may take up to 3 minutes. In such scenarios, the user is advised to close the validation pop up and return to the opportunity after a few minutes. The validation continues to run in the background and updates the VAT ID or legal entity name validation status fields with the response received from Fonoa.

#### TIN Search tab, or "Reverse Lookup"

An alternative approach is to search for a company by **name and address** to find its tax ID. This feature should be used when the customer cannot supply the VAT ID.

TIN Search is not available in every country. Fonoa supports format validation in around 120 countries but reverse search in roughly 40. In an unsupported country the search returns an explicit error naming the country, and the AE should obtain the VAT ID from the customer instead.

![The TIN Search tab](/images/sales/field-operations/vat-id-validation/tin-search.png)

The TIN Search passes the Salesforce Account Name and Address as search filters to Fonoa, which queries the relevant government database and returns one or more results. Each result displays fuzzy match percentages for the Name and Address alongside other key attributes. The user reviews these results, selects the best match, and clicks Use this TIN.

![TIN Search results showing fuzzy match percentages](/images/sales/field-operations/vat-id-validation/tin-search-results.png)

#### Request Support tab

Opens a case with Sales Operations. See Step 4.

### Step 3 — Read the result

Two statuses are written to the Account, and both must be satisfied before the deal can be booked.

#### VAT Validation Status

| Status | Meaning | Booking |
| --- | --- | --- |
| Valid | Format is valid, the ID was found in the official database, the business is not inactive, and it is tax-registered. | Passes |
| Pending | Stamped immediately before the Fonoa call. A temporary state. | Blocks |
| Invalid - Format | Failed the country-specific format check. Evaluated before any other rule, so the call never reaches Fonoa. | Blocks |
| Invalid - Not Found | The VAT ID is presented in the correct format, but the VAT ID is not present in the official database. | Blocks |
| Invalid - Not Tax Registered | Found in the database, but not registered for tax. | Blocks |
| Invalid - Inactive | The business status is inactive. | Blocks |
| Inconclusive | Fonoa responded but the result did not match any of the above — for example, tax-registered or business status returned as unknown. | Blocks |
| Validation Error | The call itself failed, or returned no validation detail. | Blocks |

An invalid or inconclusive result is not a dead end. Correct the VAT ID and validate again — each attempt is logged separately and the previous result is not overwritten in the audit history.

Valid result:

![A valid result, with the legal entity status set to Tool Verified](/images/sales/field-operations/vat-id-validation/result-valid.png)

Invalid result:

![An invalid result](/images/sales/field-operations/vat-id-validation/result-invalid.png)

#### Legal Entity Validation Status

Once a VAT ID is successfully validated, a legal entity validation status is generated by comparing the registered name returned by Fonoa with the Salesforce Account Name.

| Status | How it is set | Booking |
| --- | --- | --- |
| Tool-Verified | Automatic. Fonoa's registered name matches the Account Name. | Passes |
| Sales Rep-Verified | Manual. The AE selects **Mark as Verified** after confirming the name directly with the customer. | Passes |
| Sales Ops-Verified | Set when Sales Operations closes the Account Name Change/M&A case. | Passes |
| Pending Review | Automatic. The VAT ID is valid but Fonoa returned no registered name, so there is nothing to compare against. | Blocks |
| Pending Sales Ops Update | Automatic. Fonoa returned a registered name associated with the VAT ID, but the name does not match the Account Name. | Blocks |

**The name comparison is exact.** The two possible outcomes are:

- **Names do not match.** Differences in capitalization, punctuation, legal suffix, or trailing spaces result in a mismatch, even if the names appear to refer to the same company. The Legal Entity Validation Status is set to *Pending Sales Ops Update*. See Step 4 for next steps.
- **No registered name returned.** If Fonoa does not return a registered name, there is nothing to compare against. The Legal Entity Validation Status is set to *Pending Review*, and the validator displays: *"Fonoa did not return a Registered Business Name for this validation. Click the button 'Mark as Verified' to confirm the Registered Business Name has been verified with the Customer."*

In both situations, use **Mark as Verified** only after **confirming the legal entity name with the customer**. This is an assertion on the record, and it is what permits the deal to be booked.

![Pending Review, with the Mark as Verified button](/images/sales/field-operations/vat-id-validation/pending-review.png)

### Step 4 — Name mismatch: raise a Sales Operations case

Where Fonoa's registered name does not match the Account Name, the validator shows the two names side by side:

> Legal Entity Name Validation: Fonoa's registered company name [registered name] does not match the Account name [account name]. Please click Request Support to open a case with Sales Ops to change the name of this account.

Selecting **Request Support** creates an **Account Name Change/M&A** case in a single step. The team, request type and details are pre-filled; the mandatory reason/notes field is pre-populated with the detail of the mismatch:

> Fonoa's database lookup returned legal entity name "[legal entity name returned by Fonoa]" which does not match the Salesforce Account name "[Salesforce account name]". Please, update the Salesforce account name to match the legal entity name.

The text above is generated automatically. Please review it, edit as needed, and submit. The case is owned by the **Sales Ops Team** queue — no manual routing is required.

Mismatch banner:

![The legal entity name mismatch](/images/sales/field-operations/vat-id-validation/name-mismatch.png)

Account Name Change/M&A case:

![The pre-filled Account Name Change and M&A case](/images/sales/field-operations/vat-id-validation/sales-ops-case.png)

**The opportunity is not blocked while the case is open.** Quoting and order form generation continue as normal. Only submission for approval is gated.

When the case is created, the Legal Entity Validation Status is set to Pending Sales Ops Update, so the account does not sit on Pending Review while the case is in flight. This happens even if the popup is dismissed early.

#### Tasks performed by the Sales Operations team

Sales Operations reviews the case and corrects whichever of the Account Name, VAT ID or sold-to country is shown by Fonoa to be in conflict. Closing the case sets the Legal Entity Validation Status to Sales Ops Verified and no further prompts appear for that account.

Requests of this kind are automatically routed to Sales Operations under [Requesting Internal Support in Salesforce](/handbook/sales/field-operations/requesting-internal-support/) → Customer Account → Account Name Changes. This process uses the same case type and the same queue; only the method of flagging the mismatch has changed.

### Step 5 — Sold-to country mismatch on the quote

Tax is determined from the Account's country. Where the Sold-To Contact's **country** differs from the Sold-To Account's country, a warning appears on the quote:

> WARNING: Sold To Country Mismatch: The Sold To Contact's country [contact country] is different from the Account's country [account country]. VAT will be calculated incorrectly. Please escalate to the Sales Ops/Deal Desk team.

This warning does not block the quote, but ignoring it produces incorrect tax on the invoice. Please escalate this to the Sales Ops/Deal Desk team for support.

![The sold-to country mismatch warning on a quote](/images/sales/field-operations/vat-id-validation/quote-country-mismatch.png)

### Step 6 — Submitting for approval

The submission is ready for **Submit for Approval**. The submission passes when:

- VAT Validation Status is Valid, **and**
- Legal Entity Validation Status is Tool-Verified, Sales Rep-Verified or Sales Ops-Verified

With both satisfied, the submission proceeds with no additional prompt.

![The account fields once validation is complete](/images/sales/field-operations/vat-id-validation/account-fields-complete.png)

### Step 7 — Exceptions

Where validation is incomplete, the Account Executive is asked whether to proceed with an exception:

> Would you like to submit this Opportunity with an exception reason?

Selecting **No** aborts the submission and the opportunity stays where it is. Selecting **Yes** requires an exception reason:

| Exception reason | Use when |
| --- | --- |
| Customer acknowledged that they don't have a valid VAT ID | The customer has confirmed they are not VAT-registered. |
| Customer has provided VAT exemption certificate | An exemption certificate has been received. Attach it to the opportunity. |
| Case Pending with Sales Ops | An Account Name Change/M&A case is open and unresolved. |
| Validation Tool Issue | The validator or Fonoa is not returning a usable result. |
| Other | Anything else. Additional detail is mandatory. |

The reason is written to the validation log against the account and opportunity, which will become part of the record for the opportunity and customer information. Every exception is visible to Tax, Finance and Sales Operations, so choose the reason that is actually true.

An exception does not mark the account as validated. The account continues to report as pending validation until the underlying VAT ID and legal entity name are resolved.

### Step 8 — Order form and downstream systems

The order form displays the sold-to legal entity name and the VAT ID from the Account.

On "Closed Won" and "Send to Zuora" attributes in Salesforce, the Account Name populates the Zuora billing account name. The validated VAT ID flows to the Zuora VAT ID field. Tax rules read the VAT ID at billing-account level, which is why the Account must be correct before the quote is sent.

The billing account is created within Zuora at the end of the Salesforce validation sequence, illustrated as follows:

Account → Opportunity → Quote → Quote Approval → Opportunity Approval → Closed Won → Quote Sent to Zuora → Billing Account

## Field reference

The following fields are retained in the Account, under **Other Account Info**, beside the existing VAT/Tax ID field.

| Field | Populated by | Notes |
| --- | --- | --- |
| VAT/Tax ID | You | The customer's VAT or tax identification number. |
| VAT Validation Status | System | Result of the Fonoa check. See Step 3. |
| VAT Last Validated Date | System | Timestamp of the most recent validation attempt. |
| Legal Entity Validation Status | System, or the AE via Mark as Verified | Result of the name comparison. See Step 3. |
| Legal Entity Validation Date | System | Timestamp of the most recent legal entity determination. |

Both status fields are **read-only for Sales**. Edit access is limited to Sales Operations, Finance User and System Administrator. Reps change these values through the validator, not by editing the field.

Every validation attempt also writes an append-only log record capturing the VAT ID submitted, the Fonoa response, the registered name and address, the resulting status, and any exception reason. Attempts are never overwritten.

## Who does what

| Role | Responsibility |
| --- | --- |
| Account Executive (AE) / opportunity owner | Obtains the VAT ID and legal entity name from the customer. Runs validation from Stage 3. Raises a Sales Ops case on mismatches. Selects an exception reason for valid exceptions. |
| Sales Operations | Owns the Account Name Change/M&A queue. Corrects the Account Name, VAT ID or sold-to country and closes the case. |
| Deal Desk | Supports AEs on quote-level sold-to country mismatches and on deals held up by validation. |
| Tax and Finance | Monitors exception volumes and reasons; owns the VAT compliance and reporting. |

## Things to watch

- **Validate before you quote.** Tax determination and the Zuora billing account both read from the Account. Creating a quote before validation completes can leave the VAT ID off the billing account.
- **Exact match means exact.** A legal suffix, a comma or a capital letter is enough to produce a mismatch. Check the registered name Fonoa returned before assuming the data is wrong.
- **The Account Name is the Sold-To legal entity name.** The Account Name is not the trading name, the brand name, or the ultimate parent name.
- **Mark as Verified is an assertion.** Only use it after you have actually confirmed the name with the customer.
- **Exceptions are visible.** Every exception reason is reported on. It is a documented path, not a workaround.

## Getting help

For a validation result you believe is wrong, or a deal held up by validation, post in `#sales-support`.

For an Account Name, VAT ID or sold-to country correction, use **Request Support** in the validator, or raise a case in Salesforce under Customer Account → Account Name Changes per [Requesting Internal Support](/handbook/sales/field-operations/requesting-internal-support/).
