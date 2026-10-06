---
title: Creating SCIM Applications
---

## Overview

This guide outlines best practices for creating SCIM applications in Okta.

## Application Type Preference

When creating a new application in Okta, follow this order of preference:

### 1. Use OIN App Where Possible

Always check the Okta Integration Network (OIN) first for a pre-built integration. OIN applications provide:

- Pre-configured SAML/SCIM settings
- Tested and maintained integrations
- Simplified setup process

If an OIN application is available for your vendor, use it.

### 2. SWA App (If OIN Not Available)

If an OIN application is not available, create a Secure Web Authentication (SWA) application.

## SWA Application Configuration

### Sign-On Settings

When configuring the SWA application, use the following sign-on settings:

- **App Sign-On URL**: `https://localhost`
- **App visibility**: Enable: `Do not display application icon to users`

### Credential Management

Use the correct SWA credential setting:

- **Setting**: `Administrator sets username & password`

This setting ensures proper credential management and security.

### Provisioning

Once the app has been created, navigate to the "General" tab and select "Edit".

- **Provisioning**: `SCIM`

## Assignment and Password Security

When assigning SWA applications to users using the recommended configuration, both assignment methods minimize the risk of password exposure in Okta.

### Group-Level Assignment

At the group level, there is no risk of password exposure because:

- The password field is not available when assigning at the group level
- Passwords cannot be set or stored in Okta through group assignments
- This is how most access is assigned

### Individual Assignment

At the individual level, there is no risk of password exposure when you:

- Leave the password field blank during assignment
- This leaves the password unset in Okta
- No credentials are stored in Okta

Both assignment methods result in no password storage in Okta, ensuring credential security.
