---
title: "Okta"
---

## What is Okta?

From the Okta website

> Okta is the foundation for secure connections between people and technology.
> It's a service that gives employees, customers, and partners secure access to the tools they need to do their most important work.

In practice - Okta is an Identity and Single Sign On solution for applications and Cloud entities.
It allows GitLab to consolidate authentication and authorisation to applications we use daily through a single dashboard and ensure a consistent, secure and auditable login experience for all our GitLab team members.

### How is GitLab using Okta?

GitLab is using Okta for a few key goals:

- We can use Okta to enable Zero-Trust based authentication controls upon our assets, so that we can allow authorised connections to key assets with a greater degree of certainty.
- We can better manage the login process to the 80+ and growing cloud applications that we use within our tech stack.
- We can better manage the provisioning and deprovisioning process for our users to access these application, by use of automation and integration into our HRIS system.
- We can make trust and risk based decisions on authentication requirements to key assets, and adapt these to ensure a consistent user experience.

### What are the benefits to me using Okta as a user?

- A single Dashboard that is provided to all users, with all the applications you need in a single place.
- Managed SSO and Multi-Factor Authentication that learns and adapts to your login patterns, making life simpler to access the assets you need.
- Transparent Security controls with a friendly user experience.

### What are the benefits to me as an application administrator to using Okta?

- Automated provisioning and group management
- Ability to transparently manage shared credentials to web applications without disclosing the credentials to users
- Centralised access for users, making it easy to add, remove and change the application profile without the need to update all users.

## How do I get my Okta account set up?

All GitLab team members will have an Okta account set up during onboarding. You should receive an activation email in your personal email account before your start date. Please follow the steps in the email to activate your Okta account.

Once you’ve signed in to Okta, access your work Gmail and look for a 1Password activation email titled "Welcome to 1Password!" to set up your account.

<div class="w3-panel w3-yellow">
  <h3>Important:</h3>
  <p>Follow our [IT Onboarding Guide](/handbook/eta/corporate-it/end-user-services/onboarding101/) closely to ensure that your Okta account is configured correctly</p>
</div>

GitLab requires all team members to use either Biometrics or a YubiKey as your [Okta authentication](/handbook/eta/corporate-it/end-user-services/onboarding101/onboarding-mobile-devices/#mobile-passkey-and-yubikey-setup)

## Device Trust

Okta Device Trust ensures that team members are acccessing Okta applications from a managed device. For additional details and timelines, please see the [internal handbook](https://internal.gitlab.com/handbook/it/okta-device-trust/).

## Adding New Applications to Okta

Create a [new CorpSec issue](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?description_template=okta_app_change) and tag `@gitlab-com/gl-security/corp/identity`

Okta is currently configured with assigned groups/roles based on a team member's role/group.
Refer to the [Access Change Request](/handbook/eta/corporate-it/end-user-services/access-requests/) section of the handbook for additional information on why an application may not be available in Okta.

### How do I get my application set up within Okta?

If you are an application owner please submit an [Okta app change issue](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?description_template=okta_app_change) on the Okta project page for your application.
We will work with you to verify details and provide setup instructions.

### I have an application that uses a shared password for my team, can I move this to Okta?

Yes you can!
Submit a [new application setup issue](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new?description_template=okta_app_change) on the Okta project page for your application.
We will work with you to verify details and provide setup instructions.

If you are having problems with being asked for multiple MFA authentications during the day, please [log an issue](https://gitlab.com/gitlab-com/gl-security/corp/issue-tracker/-/issues/new), tag `gitlab-com/gl-security/corp/identity`, and we can look into it.

### Why does GitLab.com ask for an additional MFA when I login via Okta?

Your gitlab.com account will have 2FA installed as required by our policy.
Note that the 2FA for GitLab.com is different to the MFA you use to log into Okta.
[This issue](https://gitlab.com/gitlab-com/gl-infra/infrastructure/issues/7397) has been opened to propose a solution.

## Where do I go if I have any questions?

- For Okta help, setup and integration questions: Please contact IT via the Compass app in Slack (type "Compass" in the top search bar to find it) or it-help@gitlab.com.
