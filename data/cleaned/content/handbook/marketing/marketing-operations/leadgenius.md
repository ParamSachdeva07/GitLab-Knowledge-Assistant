---
title: "LeadGenius"
description: "Global B2B Data & Buyer Intelligence for Revenue Teams"
---

## LeadGenius

LeadGenius is a **B2B data provider** used by **Marketing Operations & Sales Development Teams** to source and enrich and leads & contacts for the **APJ market**. It complements our existing enrichment stack (ZoomInfo, Cognism, etc.) by focusing specifically on **APJ data coverage and quality**.

LeadGenius is an **enrichment and sourcing tool only** – all production data from LeadGenius is written into **Salesforce (SFDC)** so that GTM teams can work entirely from SFDC.

---

## Access, Licensing, and Provisioning

### Who needs direct LeadGenius access

Most GTM users **do not** need a LeadGenius login. Direct platform access is limited to a small group of users who operationally run campaigns and enrichment:

- **Marketing Operations (MktgOps)** – tool owner, integration, data governance, and workflows
- Selected **APJ GTM ops / SDR/BDR stakeholders** – where hands-on list building or QA is required

Everyone else consumes LeadGenius data **through SFDC only**.

### How to request access (Lumos)

If your role requires direct tool access:

1. Go to **Okta** and open **Lumos**.
2. Search for **`LeadGenius`**.
3. Submit an access request including:
   - Your **role** (e.g., APJ BDR, APJ Field Marketing, MktgOps)
   - Your **region** and **use case** (e.g., "APJ outbound sourcing for Japan enterprise accounts")

Requests are reviewed by **MktgOps** and provisioned based on license availability and regional priorities.

### Who can see LeadGenius data

- All enrichment and net-new data from LeadGenius is stored in **SFDC** on **Lead**, **Contact** records.
- Any user with standard access to those objects in SFDC can see LeadGenius-enriched fields.
- There is **no production data that exists only inside LeadGenius**; SFDC is the SSOT for LeadGenius output.

---

## Where LeadGenius Data Lives in SFDC

LeadGenius enrichment is written directly into **standard and custom fields on the Lead and Contact layouts** so that reps can see and use the data without leaving SFDC.

On both **Lead** and **Contact** objects, LeadGenius data is grouped in the **`LeadGenius/OceanFrogs`** section. This section includes:

- **Person-level fields**
  - **First Name**, **Last Name**
  - **Email**
  - **Title**
  - **Seniority Level**
  - **Department**
  - **Mobile Phone**
  - **Person LinkedIn**
  - **Contact Country**, **Contact State**

- **Company-level fields**
  - **Company Name**
  - **Company Website**
  - **Company Domain**
  - **Company HQ Country**
  - **Company HQ State**
  - **Industry**
  - **Annual Revenue**
  - **Employee Count**
  - **Technologies Used**

- **Operational enrichment fields**
  - **Email Verification Status**
  - **Last Enrichment Date**
  - **Enrichment Source**

These fields are read-only for most users and are populated/updated by the LeadGenius integration. They are used by **routing, reporting, and GTM workflows**, and should be treated as the **system of record for APJ enrichment data** alongside our other enrichment providers.

---

## LeadGenius APJ Campaign Workflows

MktgOps & Sales Development Teams uses LeadGenius in **two core workflows**:

1. **ICP-based APJ sourcing and enrichment**
2. **Account-level `Nominate for Enrichment` workflow**

### 1. ICP-based APJ sourcing & enrichment

This workflow is used when we want to **proactively source net-new APJ contacts** that match our target ICP.

**High-level flow**

1. **Define ICP**
   MktgOps and APJ GTM stakeholders agree on an **APJ ICP spec** (segment, geo, employee band, industry, tech profile, etc.).

2. **LeadGenius sourcing**
   LeadGenius uses this ICP to:
   - Identify **net-new accounts** in the APJ region
   - Identify **key contacts** at those accounts (titles, buying groups, etc.)

3. **Load into SFDC**
   MktgOps:
   - Loads the results into **SFDC** using our standard **enrichment process**
   - Tags records with a consistent **Initial Source** (for example, an APJ-specific LeadGenius source value) so we can report on performance and data quality

4. **Downstream usage**
   - New and enriched records are used for **SDR/BDR prospecting**.
   - All subsequent ownership and routing follows **standard APJ rules** (see *Routing* section below).

### 2. Nominate for Enrichment (Account object)

This workflow lets APJ GTM teams flag **specific accounts** where deeper or refreshed data would unlock better prospecting.

**High-level flow**

1. **Nomination in SFDC**
   - On the **Account** object, APJ reps (AEs, SDRs/BDRs, or MktgOps) can set a dedicated field such as **“Nominate for Enrichment”** to indicate that the account should be enriched via LeadGenius.
   - Reps should only nominate accounts that:
     - Are **in the APJ region**
     - Are **legitimate target or customer accounts** (not personal or test records)
     - Have a clear business need (e.g., missing buying group, outdated firmographics)

2. **Batch extraction by MktgOps**
   - On a regular cadence (e.g., **weekly**), MktgOps pulls **all APJ accounts** where *Nominate for Enrichment = True*.
   - The account list is provided to LeadGenius for enrichment.

3. **Enrichment + import back to SFDC**
   - LeadGenius returns **additional contacts** for those accounts.
   - MktgOps loads the results back into SFDC using the same controlled import process:
     - Creates new leads for those accounts
     - Updates operational metadata (e.g., last enrichment date / source)

4. **Post-enrichment hygiene**
   - After the batch has been processed, MktgOps (or automation) clears or updates the **Nominate for Enrichment** field so it reflects current status.
   - APJ reps can then work the newly enriched contacts using standard SFDC views and sequences.

---

## Routing and Ownership (APJ)

LeadGenius itself does **not** own routing logic; it simply populates data and creates records. Routing takes place in Traction and remains fully aligned with our **standard APJ lead & contact routing**.

Key principles:

- **Lead Source & attribution**
  - Records created via LeadGenius should be tagged with a clear **source / source detail** that identifies LeadGenius as the origin.
  - This allows us to measure **volume, quality, and pipeline impact** from LeadGenius specifically.

- **Standard APJ routing**
  - **Leads** created from LeadGenius imports follow the **same Traction / routing rules** as any other APJ lead:
    - Routing is based on **segment, geo, and routing rules** defined in our APJ lead & contact routing configuration.
    - Ownership (BDR vs SDR vs AE vs queues) is not special-cased for LeadGenius; it is determined by the standard routing logic.

- **No bypass of RoE**
  - LeadGenius-sourced records are still subject to our **Rules of Engagement (RoE)** and **Do Not Contact / consent** policies.
  - Reps should treat LeadGenius as **one more data source**, not as a reason to bypass routing or RoE.

---

## When to Use LeadGenius vs. Other Enrichment Tools

From a MktgOps perspective:

- **Use LeadGenius when**
  - The **target audience is in APJ** (either net-new sourcing or deeper enrichment on APJ accounts).
  - You need targeted **APJ campaigns** (e.g., vertical, region, or cluster plays) and existing data providers have gaps.
  - An APJ rep or marketer has explicitly **nominated an APJ account for enrichment**.

- **Use ZoomInfo / Cognism when**
  - You are working outside APJ (e.g., **AMER, EMEA, LATAM**).
  - You’re following established workflows documented on the **ZoomInfo** and **Cognism** handbook pages or the **lead & contact enrichment** internal page.

If you are unsure which provider is appropriate for your campaign, start a thread in `#mktgops` with:

- Region + segment
- Use case (e.g., "APJ ABM for strategic accounts in Japan")
- Whether you need **net-new sourcing**, **enrichment on existing accounts**, or both

---

## Data Quality, Compliance, and Best Practices

- **SFDC is the SSOT** for all LeadGenius data.
- Follow existing **DNC / consent / privacy** processes when using LeadGenius-enriched records in emails, calls, or campaigns.
- Do **not** manually overwrite LeadGenius-enriched fields with guessed values; instead:
  - Log a **MktgOps issue** or
  - Nominate the account again for enrichment or correction.

### Job-change handling (APJ)

When LeadGenius identifies that an APJ **contact** has changed jobs, Marketing Operations automatically sets the Salesforce **Contact Status** to `Disqualified – No longer at company`. This prevents APJ teams from continuing to work stale people while still preserving historical activity and attribution for reporting.

---

## How to Get Help

For questions or issues related to LeadGenius:

- Start in **Slack** `#mktgops` and include:
  - A link to the **Account / Lead / Contact** in question
  - Whether you are asking about **access**, **data quality**, **routing**, or **campaign setup**
- For structural changes or new workflows, open a **MktgOps issue** using the standard templates and mention LeadGenius in the title or description.
