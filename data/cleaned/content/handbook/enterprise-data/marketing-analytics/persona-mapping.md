---
title: Marketing Persona Mapping
description: How Marketing categorizes titles in our Tableau Reporting  
---

<link rel="stylesheet" type="text/css" href="/stylesheets/biztech.css" />

## <i id="biz-tech-icons" class="far fa-newspaper"></i>Goal

## Marketing Persona Mapping

The Marketing Persona Mapping framework categorizes person data linked to touchpoints based on job titles to understand our audience composition and improve campaign targeting. This analysis uses self-reported titles from marketing touchpoints, form submissions primarily from Marketo & trials, to create standardized persona categories.

## How Persona Mapping Works

When prospects interact with GitLab marketing campaigns, they submit their job titles through forms. These titles are free-form text fields stored in Salesforce. Our persona mapping logic analyzes these titles to categorize each person into one of 14 defined personas using a prioritized matching system.

### Important Context for Campaign Managers

- **Self-Reported Data**: All titles are self-reported by form submitters. This means the data reflects how people describe their own roles, not verified organizational titles.
- **Free-Form Challenges**: Since title is a free-text field, expect variations in spelling, formatting, and completeness. The mapping logic handles common variations but some edge cases may be uncategorized.
- **Total Populate**: Before categorization, we exclude persons with missing, empty, or single-character titles.

## Persona Categories

Below are the 14 persona categories with their share of total touchpoints and descriptions:

### Technical Leadership

- **C Level**: Senior executives and C-suite leaders including CEOs, CTOs, CIOs, CISOs, and other chief officers. Also includes founders, owners, presidents, and entrepreneurs who make strategic technology decisions.
- **Info Security Management**: Information security leaders who also have management responsibilities, combining security expertise with team leadership roles.
- **Info Security**: Information security professionals focused on cybersecurity, including security officers, analysts, and engineers without direct management responsibilities.

### Management & Strategy

- **Upper Management**: Mid to senior level managers including directors, VPs, heads of departments, and team leads who oversee teams and budgets but aren't C level.
- **Program Management - Management**: Senior program managers, product managers, and consultants who lead strategic initiatives and manage other PMs.
- **Program Management**: Program managers, project managers, product managers, business analysts, and consultants focused on execution and delivery.

### Technical Contributors

- **IC Developer**: Individual contributor software engineers, developers, programmers, and technical engineers who build and maintain applications and systems.
- **Platform / Ops / Infrastructure Engineering**: Technical professionals managing infrastructure, systems administration, cloud operations, and platform engineering without direct reports.
- **Release & Change Mgmt**: Individual contributors in DevOps, QA, testing, release management, and site reliability engineering without management duties.
- **Release & Change Mgmt - Management**: Leaders who oversee software delivery, quality assurance, DevOps, and change management processes with management responsibilities.

### Other Categories

- **Education**: Students, professors, researchers, and academic professionals in educational institutions or research organizations.
- **Non-Development Back Office**: Business functions including marketing, sales, finance, HR, legal, operations, and administrative roles not directly involved in technology development.
- **Not Enough Info**: Titles too generic or vague to categorize accurately (e.g., "specialist," "staff," "consultant").
- **Uncategorized**: Titles that don't match any defined category patterns.

## Prioritization Logic

The mapping uses a priority scoring system to handle titles that could match multiple categories:

1. **Security + Management** titles get highest priority
2. **C-Level** titles (excluding VPs) come next
3. **Single category matches** follow in order of business impact
4. **Generic titles** fall to "Not Enough Info" category
5. **Unmatched titles** become "Uncategorized"

This ensures consistent categorization when titles contain multiple keywords (e.g., "DevOps Security Manager" maps to Info Security Management, not Platform/Ops).

## Data Quality Considerations

### Title Variations

The system handles multiple languages and common variations:

- English, Japanese, Korean, French, Spanish, Portuguese terms
- Common abbreviations (CEO, CTO, VP, PM, etc.)
- Regional differences in titles

### Exclusions

Certain keywords trigger exclusions to improve accuracy:

- Sales-related titles are excluded from technical categories
- Pure sales roles are categorized as "Non-Development Back Office"
