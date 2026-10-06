---
title: "GitLab for Startups Program Workflows"
description: "This page explains at a high level how **GitLab for Startups** applications move through **Marketo, Salesforce, and Traction**, and how applicants are routed to the Community team and Sales Dev."
---

## Systems and roles

- **Marketo**: Captures Startup applications, manages program membership, Interesting Moments, and scoring.
- **Salesforce (SFDC)**: Stores leads/contacts, Startup Program fields, Total Funding, and campaign membership.
- **Traction**: Routes MQLs and high‑priority leads to Sales Dev and AEs.

**Primary DRIs**

- **Community / Startups Program** – reviews applications and sets program decisions.
- **Marketing Operations** – owns Marketo program, forms, sync to SFDC, and Traction routing rules.
- **Sales Dev** – works qualified but **rejected** Startup applicants.

---

## Key fields and values

### Shared Marketo/SFDC fields

- **Source**: `Startup Application`  
  - Set for all Startup application form fills.  
  - Used in Traction to branch into the Startup‑specific routing path.

- **Startup Program Status** (on lead/contact) – main statuses:
  - **Under Review** – application submitted and being reviewed by Community.
  - **Qualified for Seed Y1** – approved with Seed‑level Startup pricing.
  - **Qualified for Early Y1** – approved with Early‑stage Startup pricing.
  - **Denied from Startups Program** – not a fit and no Sales Dev follow‑up.
  - **Rejected Startup Lead Re‑engage** – not approved for the program but should be routed to Sales Dev.

- **Total Startups Funding** (SFDC) / **Total Funding** (Marketo)  
  - Captures company funding band on the application.  
  - Drives reporting and potential future segmentation.

---

## End-to-end Workflow

### 1. Application submitted

1. Prospect fills out a **Startup application form** (Marketo).
2. Marketo:
   - Creates/updates the person.
   - Adds them to the **Startup Application** program.
   - Logs an **Interesting Moment** for the form fill.
3. Marketo syncs the record to SFDC:
   - **Source = Startup Application**
   - **Startup Program Status = Under Review**
   - **Total Startups Funding** populated.

---

### 2. Program decision

The Community / Startups Program team reviews the application and updates **Startup Program Status**:

- **Approved**  
  - **Qualified for Seed Y1** or **Qualified for Early Y1**  
  - Startup pricing is granted; opportunities and owner/AE workflows follow the Startups Program’s standard process (documented on the broader Startups Program page).

- **Denied**  
  - **Denied from Startups Program**  
  - Leads remain visible for reporting but do **not** intentionally feed Sales Dev follow‑up via this workflow.

---

### 3. Rejected but good fit for Sales Dev

If an applicant is **not** approved for Startup pricing but is still a good fit for GitLab:

- Status is set to **Rejected Startup Lead Re‑engage** (replaces legacy “Denied – Sales Dev to re‑engage”).
- A Marketo smart campaign:
  - Watches for this status.
  - Ensures the lead **MQLs via scoring** (no direct status jump).
  - Logs an **Interesting Moment** to give Sales Dev context.

Once the lead reaches **MQL**:

- Marketo updates Lead Status per global lifecycle.
- Lead enters **standard Traction MQL routing** (same FY27 rules as other MQLs).
- Ownership is assigned based on territory and account coverage (BDR/SDR/AEs), while **Startup Program Status = Rejected Startup Lead Re‑engage** preserves context.
