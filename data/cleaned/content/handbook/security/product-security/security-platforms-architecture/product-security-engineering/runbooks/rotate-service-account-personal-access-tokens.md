---
title: "Rotate Service Account Personal Access Tokens (PATs)"
---

## Rotate Service Account Personal Access Tokens (PATs) Runbook

This runbook is an approach to rotating a GitLab Service Accounts Personal Access Tokens (PATs). They can be configured as a legacy PAT (which uses broader scopes) or a fine-grained PAT (which scopes to specific boundaries and resources). From here on out we will refer to Personal Access Tokens as PATS and singular use of Personal Access Token as PAT.

### 1. Why is this important?

- Services Accounts can have their PATs expire and therefore preventing resources from being accessed. This blocks API access, Pipeline completion, and individual jobs from running properly and completing their work.
- This runbook is meant to be a structured way to help someone new to this problem, or as a reminder to those who have engaged this problem before but forgot specifics, to attempt to solve the issue with PAT rotations for the Service Accounts.

### 2. Pre-requisites?

- Find the affected Service Account, hopefully you or someone in the team will receive an email like the one in the screenshot below:

![GitLab Security Service - Architecture - Inventory PAT Email](/images/security/product-security/security-platforms-and-architecture/security-service-architecture-inventory.png)

- If not already completed, create an issue like [GitLab Security Service - Architecture - Inventory's PAT expired](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/product-security-engineering-team/-/issues/262).
- Check and see if you have access to the Service Accounts login credentials in 1Password like below:

![Service Account in 1Password](/images/security/product-security/security-platforms-and-architecture/service-account-1password.png)

- If you do not have access, submit an Access Request (AR) like this [issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/36630).

### 3. Steps to fix

1. Before rotating, check whether this token is a legacy PAT or a fine-grained PAT.
1. Make sure you are logged out of your personal account on GitLab.com.
1. Using the Service Accounts credentials in 1Password, login in to GitLab.com with them.
1. Use the `one-time password` parameter in 1Password for the MFA OTP.
1. You should land on the Service Account's Project page like below:

    ![Service Account Landing Page](/images/security/product-security/security-platforms-and-architecture/service-account-landing-page.png)

1. Select the Service Account's icon and click on `Edit Profile` like below:

    ![Service Account Edit Profile](/images/security/product-security/security-platforms-and-architecture/service-account-edit-profile.png)

1. Click on `Access tokens` in the `User settings`:
    - **If the existing token is a fine-grained PAT and you are not changing its boundaries or permissions:** next to the active token, select the vertical ellipsis (⋮) → **Duplicate**, which will bring you to the page with most of the same configurations pre-filled. You need to manually adjust the token name and expiration date per your project requirement. The standard token lifespan is 1 year. Continue with step 8.
    - **Otherwise** (legacy PAT, or you need to change a gPAT's scope): click the `Add new token` button and continue with step 8.

    ![Service Account Access Token Page](/images/security/product-security/security-platforms-and-architecture/service-account-access-token-page.png)

1. Add the `Token name` that matches the previous token that had expired, in this case it is `GitLab Security Service - Architecture - Inventory`. **For a fine-grained PAT**, select "Fine-grained token" from the Generate token dropdown.
1. Add a `Description` of what the token is used for.
1. For `Expiration Date` set it for 365 days in the future (the maximum expiration). If you do not set it, it is default to expire in 30 days for legacy PATs (gPATs default to 365).
1. Configure access:
    - **For a legacy PAT:** click the `Select scopes` permission level that best matches what access the Service account needs (in this case it is API only), like in the image below:

    ![Service Account Personal Access Token](/images/security/product-security/security-platforms-and-architecture/service-account-personal-access-token.png)

    - **For a fine-grained PAT:** select the **Boundary** (Group, Project, or User; pick the most restrictive that still lets the automation work) and then in the right panel select the minimum **permission** per resource.

1. Before you click `Create Token` make sure to scroll down the page and `Revoke` the old token, as shown in the image below. Skip if you used the in-place Rotate flow in step 7. GitLab already deactivated the old token.

    ![Service Account Revoke Old Personal Access Token](/images/security/product-security/security-platforms-and-architecture/service-account-revoke-old-personal-access-token.png)

1. Then click the `Create token` button and review the confirmation that the new token is in the PAT list on `Personal access tokens` page.

### 4. Steps to test

1. Logout of the Service Account and back in to an Account that has permissions to re-run any pipelines associated with the Service Accounts PAT.
1. For this particular Service Account, the GitLab Inventory Builder uses this Service Accounts PAT to access APIs.
1. So re-running a pipeline job for that repository that was previously failing due to token errors, demonstrated that the PAT rotation was successful as seen in the image below:

    ![GitLab Inventory Builder Weekly - Monday mornings Pipeline Build](/images/security/product-security/security-platforms-and-architecture/gitlab-inventory-builder-weekly-monday-mornings-pipeline-success.png)

1. If the pipeline passes, congratulations, update the issue with the success and notify any concerned parties of the successful PAT rotation, and finally, close the associated issue.
