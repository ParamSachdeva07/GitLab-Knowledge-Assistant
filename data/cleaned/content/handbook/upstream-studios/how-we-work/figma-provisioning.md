---
title: "Figma provisioning and deprovisioning"
description: "Guidance on how to provision/deprovision Figma"
---

Figma provisioners/deprovisioners are found in the [Tech Stack YAML file](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml#L1780).

While multiple departments have team members with [Editor](https://help.figma.com/hc/en-us/articles/360039960434-Roles-in-Figma#editor) roles as paid seats, the UX department is the business owner.

## Figma seats

### Seat types

Figma has four different seat types depending on your needs:

* **View:** Default seat type. Access is requested via Lumos but auto-approved.
* **Full:** Full access to all Figma products, including Figma Design, Figma Make, Dev Mode, Figma Draw, Figma Slides, and FigJam.
* **Dev:** Access to Dev Mode, Figma Slides, and FigJam. View and comment access in Figma Design files.
* **Collab:** Access to FigJam and Figma Slides. View and comment access in Figma Design files.

## Provisioning

### Access request issues

Every approved paid Figma seat must have a corresponding [Lumos access request](/handbook/security/corporate/systems/lumos/ar/) with budget approval. Seat upgrades can only happen with Okta access through Lumos and not by using the Figma admin or Figma's sharing tools.

Provisioners are automatically pinged when a Lumos access request is opened. As a provisioner, ensure:

* The team member's manager has approved access.
* The team member understands what seat option they need.
  * A **View** seat is often enough when a team member only needs to view and comment on files to collaborate. All team members start with a **View** role, so no action may be needed.
  * The difference between a **Full** and **Collab** seat can be confusing at first. Ensure the team member knows which seat they need in order to perform their role.
* There is budget approval. Billing group admins should work with their Finance partners to ensure seat counts are not going over the maximum spend allocated for the fiscal year.

### Quarterly audits

Our billing cycle includes quarterly true-ups. Each quarter, admins receive an email informing them of the upcoming invoice. This gives them an opportunity to review added seats before approving the new invoice.

To audit seats:

1. Review all new seats and ensure each team member (or [guest](https://help.figma.com/hc/en-us/articles/4420557314967-Members-versus-guests#guests)) has been assigned to a billing group.
1. Once all new users have a billing group, mark your group as `Reviewed`.

Once confirmed, the Figma business owner will:

1. Lock in the final invoice amount.
1. Reach out to our Figma rep to share total seat counts for R&D, Marketing, and Sales. These will be added to line items on the invoice.
1. Ensure the invoice is uploaded to Coupa and goes through our full Procurement process.

## Deprovisioning

* A user will automatically be fully deprovisioned when they are no longer with GitLab.
* A paid seat can be downgraded to an unpaid **View** seat by reaching out to IT.
* A paid seat that has been inactive for **90 days** will be automatically downgraded to a **View** seat.

* When a member is fully removed:
  * Anyone with 'can edit' access to the member's files will be able to continue editing and can move the files.
  * Their draft files stay within the organization and Figma admins can view and manage the files.

For more information, refer to Figma's [Remove people from an organization](https://help.figma.com/hc/en-us/articles/360040453453-Remove-people-from-an-organization) documentation.
