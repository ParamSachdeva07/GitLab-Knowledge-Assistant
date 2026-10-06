---
title: 'Account merges'
description: 'Documentation on Salesforce account merges'
---

This page is intended to provide guidance for when you must review a Salesforce (SFDC) customer account merge request. To ensure that Zendesk is kept up to date with the correct details about our customers and to ensure that we provide a consistent support experience even when changes are being made to customer accounts by Sales, we have created a process to review these requests. An example of such a request can be found [here](https://gitlab.com/gitlab-com/sales-team/field-operations/sales-operations/-/issues/4026).

## Reviewing SFDC Account Merge Requests

1. Initial Review of Organizations in Zendesk
   - Check Support Entitlement:
     - Review the target organization to ensure they have support entitlement. Ensure that the target organization is neither a prospect nor in a Support Hold state.
     - Note: If the target organization does not meet this criteria, we should not proceed with the account merge until the customer is eligible for support. Instead, respond back to the original account merge request issue informing Sales Ops that the target organization is not currently eligible for support and that they should resolve this before proceeding with the account merge.
   - Check for any special configurations:
     - Check if the source organization has a Contact Management Project (CMP) or if it's a shared organization.
     - Action: If either condition is true, we can proceed with the account merge. However, Customer Support Systems should inform Sales Ops in the issue that the target organization will not automatically have the same configuration. The customer will need to raise a ticket with Customer Support Systems to explicitly request that the target organization is updated after the account merge has taken place.
   - Once eligibility for the Account Merge has been confirmed:
     - Customer Support Systems should reply back to the original issue, providing their approval and sign off on the account merge.
1. Post-Merge Actions
   - Communication:
     - Once the account merge is complete, Sales Ops should notify Customer Support Systems about the successful merge.
