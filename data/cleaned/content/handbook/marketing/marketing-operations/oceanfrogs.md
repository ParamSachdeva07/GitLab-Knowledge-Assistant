---
title: "OceanFrogs"
description: "APJ (India) B2B Data & Buyer Intelligence for GCC Accounts"
---

## OceanFrogs

OceanFrogs is a **B2B data provider** focused on **APJ**, with a specific emphasis on **India-based Global Capability Center (GCC) accounts**. It is used by **Marketing Operations (MktgOps) & Sales Development Teams** to source and enrich contacts where traditional providers (e.g., ZoomInfo, Cognism) have coverage gaps.

OceanFrogs works alongside **LeadGenius** in the same **LeadGenius/OceanFrogs** section on SFDC Lead and Contact layouts. Both tools are dedicated to **APJ enrichment** and should be used as the **primary data sources for APJ**.

All production data from OceanFrogs is written into **Salesforce (SFDC)** so APJ teams can work entirely from SFDC.

---

## Access and Provisioning

### Platform access

There is **no standalone OceanFrogs UI login** for GTM users.

- OceanFrogs data is delivered to GitLab via a managed **Workato ↔ OceanFrogs integration**.
- Only **MktgOps and Systems** work directly with the integration.
- Reps and marketers consume OceanFrogs data **exclusively through SFDC records and fields**.

### Who uses OceanFrogs data

- **Primary users:** APJ GTM teams focused on **India GCC accounts** (AEs, BDRs/SDRs, field marketing).
- **Operational owner:** **Marketing Operations (MktgOps)** – integration, data governance, and workflows.

No Lumos request is required; access is inherited via normal SFDC object permissions.

---

## Where OceanFrogs Data Lives in SFDC

OceanFrogs enrichment is written directly into **standard and custom fields on the Lead and Contact layouts**.

On both **Lead** and **Contact** objects, OceanFrogs data appears in the shared **LeadGenius/OceanFrogs** section. This section includes:

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

These fields are populated/updated by the **Workato ↔ OceanFrogs integration** and **LeadGenius**, and are read-only for most users. They are used for **India GCC targeting, routing, reporting, and GTM workflows**.

---

## How OceanFrogs Data Flows Into SFDC

High-level flow:

1. **Target definition**
   - MktgOps and APJ stakeholders define **India GCC ICP criteria** (India HQ or GCC presence, segment, industry, employee band, etc.).

2. **OceanFrogs sourcing & enrichment**  
   - OceanFrogs identifies **India GCC accounts and contacts** that match the agreed ICP.
   - Data is passed to GitLab via the **OceanFrogs API → Workato integration**.

3. **Workato processing into SFDC**
   - Workato:
     - Matches to existing Accounts / Leads / Contacts where possible.
     - Creates **new Leads**.
     - Populates the **LeadGenius/OceanFrogs** section fields and enrichment metadata.

4. **APJ team activation**
   - The **APJ (India) team works these leads and contacts directly from SFDC** using standard lead views, dashboards, and Outreach sequences.

---

## Routing and Ownership (India / APJ)

OceanFrogs does **not** route records; it only supplies data. Routing is handled by our **standard APJ lead & contact routing logic** (Traction).

Key principles:

- **Lead Source & attribution**
  - Records created from OceanFrogs are tagged with a clear **initial source**.
  - This allows us to track **volume, data quality, and pipeline impact** from OceanFrogs separately from other providers.

- **Standard APJ routing**
  - **Leads** created via OceanFrogs follow the same **APJ routing rules** as other APJ leads (India-specific geo/segment rules in Traction).
  - There are **no OceanFrogs-specific exceptions** to RoE or routing; OceanFrogs data simply improves targeting.

---

## When to Use OceanFrogs vs. Other Enrichment Tools

From a MktgOps perspective:

- **Use OceanFrogs when**
  - You are targeting **India GCC accounts** or India-based decision makers.
  - You need **better India/APJ coverage** than what we get from other providers.
  - You are running **India-specific ABM or outbound programs** where GCC context matters.

- **Use LeadGenius when**
  - You are targeting **APJ outside India** (e.g., ANZ, ASEAN, Japan, Korea) or broader APJ segments.
  - You need net-new APJ accounts and contacts that aren't specific to India GCC.

- **Use ZoomInfo / Cognism when**
  - You are working outside APJ (e.g., **AMER, EMEA, LATAM**) or following existing global enrichment workflows.

If you are unsure which provider is correct for your use case, start a thread in `#mktgops` with:

- Region + segment (e.g., India GCC, enterprise)  
- Use case (e.g., India GCC ABM for top 200 accounts)  
- Whether you need **net-new sourcing**, **enrichment on existing accounts**, or both

---

## Data Quality, Compliance, and Best Practices

- **SFDC is the SSOT** for all OceanFrogs data
- Follow existing **DNC / consent / privacy** processes when using OceanFrogs-enriched records for email, calls, or ads.
- Do **not** manually overwrite OceanFrogs-enriched fields with guessed values. If data looks incorrect:
  - Log a **MktgOps issue**, or
  - Request that the account be revisited in a future OceanFrogs batch.

---

## How to Get Help

For questions or issues related to OceanFrogs:

- Start in **Slack** `#mktgops` and include:
  - Links to the **Account / Lead / Contact** in question
  - Whether you are asking about **data quality**, **routing**, **target lists**, or **integration behavior**
- For structural changes or new workflows, open a **MktgOps issue** using the standard templates and mention **OceanFrogs** in the title or description.
