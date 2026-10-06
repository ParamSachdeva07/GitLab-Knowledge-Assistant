---
title: "Beefree"
description: "Beefree email builder"
---
## About Beefree

Beefree is an email builder tool used for creating professional email templates and campaigns.

## Access

Beefree is primarily used by the Lifecycle Marketing team. We have limited seats, but we do assign to team members that need to build specialized emails.

To request access, complete a request in Lumos. If your access is approved, you will receive an email inviting you to our Beefree organization.

To login: Click on the Beefree tile in Okta, then select the "SSO" option on the login screen.

## When to use Beefree

Use Beefree when you need to create professional email templates that integrate with our marketing automation platforms.

## Training

* Hands*on training video

## Integrations

Beefree will be integrated with Marketo and Iterable. To follow along on the project status, please see [this](https://app.asana.com/1/306855239930259/project/1210465915628353/list/1210467082112980) Asana project.

## Using Tokens with BeeFree and Marketo

BeeFree uses the term "merge tags" for dynamic content, but since we're integrated with Marketo and Iterable, we use Marketo Tokens and Iterable Merge Parameters instead.

When building emails in BeeFree for Marketo, add tokens using the format `{{my.tokenName}}`. For UTM tracking in links, use `{{my.utm}}`.

## Quick best practices

1. Always build from a template, rather than from cloning

2. Utilize the saved modules from the folders, rather than building from scratch where possible. If you have a new module in mind, ask @aklatzkin or @cbaun for support.

3. Ensure you're using the right modules for footer & hero based on if you're using Marketo vs. Iterable:
   * The Iterable version will have `{{utm}}`, `{{email}}`, `{{unsubscribeUrl}}`, `{{viewInBrowserUrl}}`
   * The Marketo version will have `{{my.utm}}`, `{{my.email address}}`, `{{system.unsubscribeLink}}`, `{{system.viewasWebPageLink}}`

4. Always ensure you update the email details (subject line and preheader text only) within the email. This shows up in the title & preview text of the email

   ![Email details section](/handbook/marketing/marketing*operations/beefree/Screenshot_2025*10*06_at_5.19.51_PM.png "Email details section showing subject line and preheader text fields")

5. If you have one main CTA link in the email, use a token for the link (i.e. `https://{{my.LandingPageURL}}?lb_email={{lead.email address}}&{{my.utm}}` for marketo for scalability)

6. Ensure that any links are correct on both the desktop and mobile versions

7. If you're using arrows or checkmarks as bullet points, set these to bullets on the mobile version.

8. For events, tokenize as much of the email as you can for scalability.

9. Once you add the email to marketo or Iterable:
   * Update the text only version of the email
   * Ensure any tokens are copied over correctly, including:
     * Unsub links: `{{system.unsubscribeLink}}` for Marketo or `{{unsubscribeUrl}}` for Iterable
     * View as web page links `{{system.viewAsWebpageLink}}` for Marketo or `{{viewInBrowserUrl}}`
   * Ensure subject line and preheader text are reflected
     * For Marketo, ensure these details are filled out:

       ![Marketo email settings](/handbook/marketing/marketing*operations/beefree/Screenshot_2025*10*07_at_2.10.59_PM.png "Marketo email settings showing subject line and preheader configuration")

     * For Iterable: ensure these details are filled out:

       ![Iterable email settings](/handbook/marketing/marketing*operations/beefree/Screenshot_2025*10*07_at_2.12.59_PM.png "Iterable email settings showing subject line and preheader configuration")
