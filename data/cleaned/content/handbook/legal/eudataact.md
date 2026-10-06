---
title: Navigating the EU Data Act with GitLab
---

## Important Notice

The information in this summary is intended as an overview and outline of certain [EU Data Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32023R2854) related matters and it does not provide legal advice and shall not be construed or used as such, nor does this document form part of, create or amend any agreement, representations, warranties or any other obligation between GitLab and its customers. Customers are advised to seek and rely only on independent legal advice on any EU Data Act related matter. GitLab shall have no liability arising from any errors, misstatements or omissions in the content of this summary.

## Regulatory Context

The EU Data Act entered into force on January 11, 2024, and is a key pillar of the European data strategy that will make a significant contribution to the Digital Decade's objective of advancing digital transformation. Most of the new rules will apply as of September 12, 2025.

The Data Act establishes harmonized rules on fair access to and use of data across the EU, with the primary goal of creating a fair distribution of value from data by establishing clear rules for accessing and using data within the European data economy.

The Data Act requires data processing service providers like GitLab to facilitate user data access, ensure fair sharing terms, remove switching barriers (commercial, technical, contractual, and organizational), respond to public sector data requests, and enable customer migration to other providers—obligations that apply to any provider serving EU customers regardless of their location.

## GitLab's Approach

This document helps customers understand how GitLab has prepared for and addresses EU Data Act compliance requirements, providing transparency into our approach as data service providers adapt their contractual frameworks and data governance strategies.

The information in this document was current as of August 2025.

## How GitLab addresses the key requirements of the EU Data Act

| Requirement | Description | Data Act Reference | GitLab's Implementation |
|-------------|-------------|-------------------|-------------------------|
| **Technical Protection Measures on Unauthorised Use or Disclosure of Data** | | Art. 11 | GitLab implements industry standard safeguards to protect data held on cloud infrastructures in the EU, and its single, unified [Trust Center](https://trust.gitlab.com/) provides access to customers to comprehensive security and privacy collateral and an interactive knowledge base. |
| **Provisions around facilitating switching between data processing service providers, transparency and pre-contractual information** | | Art. 23 & 25 | GitLab ensures no commercial, technical, contractual or organizational impediments to customer transitions, enables standardized [data exports](https://docs.gitlab.com/user/project/settings/import_export/) in machine-readable formats, with [GitLab's Subscription Agreement](https://about.gitlab.com/terms/) including appropriate measures supporting such transitions.<br><br>Through its [Privacy Statement](https://about.gitlab.com/privacy/), [documentation](https://docs.gitlab.com/) and [Data Processing Addendum](/handbook/legal/data-processing-agreement/), GitLab provides transparent information about our data processing activities, including what data we process, how it's stored, and how customers can access and control their data. |
| **Information on switching and porting methods and formats, as well as details of data structures, data formats and the relevant standards and open interoperability specifications of exportable data** | | Art. 26 | GitLab makes available current information regarding data porting procedures for our services, including available methods and formats. Users can access comprehensive porting procedures through our [Project Import/Export documentation](https://docs.gitlab.com/user/project/settings/import_export/) and [API documentation](https://docs.gitlab.com/api/project_import_export/). Our export functionality provides data in structured formats as detailed in our [development documentation](https://docs.gitlab.com/development/import_export/).<br><br>Our data structures and formats are documented through our [REST API](https://docs.gitlab.com/api/rest/) and [GraphQL API](https://docs.gitlab.com/api/graphql/reference/) documentation, which provide machine-readable specifications for all exportable data. Additional information about data portability rights and procedures is also available in our [Privacy Statement](https://about.gitlab.com/privacy/).<br><br>No exemption from exportable data exists due to risk of breach of trade secrets of GitLab, and all Customer Data remains owned by the customer at all times. |
| **Confirmation of erasure of all exportable data and digital assets generated directly by the customer, or relating to the customer directly, after the expiry of the retrieval period** | | Art. 25 | **SaaS Deployment:** Following the end of subscription to paid features, customers maintain access to their instance and all Customer Data in the free version of the Software, which they may maintain at their full discretion or delete their [namespace](https://docs.gitlab.com/user/namespace/) entirely if they wish to do so as set out in the relevant [documentation](https://docs.gitlab.com/user/group/). Upon deletion of the customer's group, all exportable data and digital assets generated directly by the customer or relating to the customer directly will be purged and deleted after such deletion.<br><br>**Self-Managed Deployment:** GitLab does not host or store data for or on behalf of customers in self-managed deployments. All Customer Content remains in the customer's environment and under their full control. Erasure of exportable data and digital assets is managed entirely by the customer within their own infrastructure.<br><br>**GitLab Dedicated:** GitLab provides customers with a 30-day period following their [Dedicated subscription expiration](https://docs.gitlab.com/subscriptions/gitlab_dedicated/#expired-subscriptions) to retrieve their data, after which all customer content is permanently deleted unless preservation is requested within 15 days of expiration. |
| **Jurisdiction to which the ICT infrastructure deployed for data processing of their individual services is subject** | | Art. 28 | GitLab makes available on its website current information regarding the jurisdiction to which the ICT infrastructure deployed for data processing of our individual services is subject, which can be found at https://about.gitlab.com/privacy/subprocessors/ |
| **Details of organisational and contractual measures to prevent international governmental access to or transfer of non-personal data** | | Art. 28 & 32 | GitLab applies all technical, legal and organizational measures described in Part 2 and Part 3 of our [Transfer Impact Guide for GitLab Customers](https://trust.gitlab.com/?itemName=data_privacy&source=click&itemUid=c6baf16e-0c50-44c4-accb-ff002acb78dd) equally between personal and non-personal data to prevent unlawful international and third-country governmental access and transfer of non-personal data held in the EU. |
| **Fair and reasonable pricing for switching services** | | Art. 29 | GitLab does not impose switching charges to customers. |
| **Interoperability** | | Art. 30 | GitLab uses APIs that are wide-spread and commonly used in the software industry, and comply with applicable interoperability specifications or harmonized standards for interoperability that may be published by the EU Commission. |

## Further Assistance

For customers requiring more specific, in-depth assistance or those interested in engaging GitLab's migration services, we encourage you to contact your Account Executive to scope your requirements, discuss pricing, and execute an appropriate Statement of Work tailored to your needs.

If you have any questions regarding the information published on this page or need clarification on GitLab's position and compliance with the EU Data Act, please reach out to your designated Account Executive for guidance.

## Implementation Timeline

The Data Act provisions apply from September 12, 2025, with specific implementation milestones:

- **September 12, 2025:** Most Data Act obligations become applicable
- **September 12, 2026:** Obligations for connected products placed on the market
- **January 12, 2027:** Free switching services requirement becomes effective
- **Ongoing:** Model Contractual Terms (MCTs) and Standard Contractual Clauses (SCCs) will be published by the European Commission before September 12, 2025

## Additional Resources

For more information about GitLab's security practices and compliance documentation, please visit:

- [GitLab Trust Center](https://about.gitlab.com/security/)
- [GitLab Documentation](https://docs.gitlab.com/)
- [GitLab Privacy Statement](https://about.gitlab.com/privacy/)
- [GitLab Data Processing Addendum](https://about.gitlab.com/privacy/privacy-management/)
- [GitLab Terms](https://about.gitlab.com/terms/)

---

*This document was last updated in August 2025 and reflects GitLab's current understanding and implementation of EU Data Act requirements.*
