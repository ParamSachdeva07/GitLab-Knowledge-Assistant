---
title: Marketing Cookies
description: "Learn more about how Digital Experience uses browser cookies."
---

The Digital Experience team use the `gitlab_tier` cookie as a tool to customize content on the `about.gitlab.com` domain. This cookie is set when a user logs into GitLab.com. This cookie expires with the session(logging out), or after 2 weeks (whichever comes first).

* The `gitlab_tier` cookie contains information for which unique tiers a user belongs to (Free, Premium, and/or Ultimate). This is the only user data that is being passed. **No other user data is passed**.
  * `false`: for authenticated users product tried to find the existence of a tier, but it didn't find anything (could be for many reasons, browser blocking, privacy settings, etc)
  * `not set`: for unauthenticated users no cookie is set, and so no attempt to check was even started.
  * Mental note: Tiers are tied to namespaces and not users. Namespaces to user relationships are many to one, which mean that you will see unique namespace values such as `free&premium`.

This implementation is on the [GitLab product project](https://gitlab.com/gitlab-org/gitlab) for the Enterprise Edition of the product. Thus, it will exist in the `gitlab.com` domain, and it will propagate down to all project subdomains, including about.gitlab.com. The cookie _does not_ work in review apps for other projects such as within About or Blog, so keep that in mind when developing for personalization in the Digital Experience team. If you want to verify that features are being rolled out appropriately and that the user breakdown between authenticated and non-authenticated users looks correct, reach out to Marketing Analytics.

For more information, read the [docs on that](https://docs.gitlab.com/ee/user/profile/#cookies-used-for-sign-in).

Note that this cookie can sometimes not show up for GitLab team members. This is because the GitLab org uses the previous `Gold` tier in the product codebase. We made the decision to exclude `Silver` and `Gold` as most customers are not using these legacy plans. You can verify this behavior by creating a new namespace with a different tier plan.

## Related MRs

* `gitlab_tier` MVC 1 MR: <https://gitlab.com/gitlab-org/gitlab/-/merge_requests/151323>
* Setting marketing cookie for logged in users `about_gitlab_active_user`: <https://gitlab.com/gitlab-org/gitlab/-/merge_requests/113761>
* Add gitlab_tier cookie for marketing use: <https://gitlab.com/gitlab-org/gitlab/-/merge_requests/151323>

This contains an older video, but still holds some relevance in a simplier but previous `gitlab_user` cookie:

 <figure class="video_container">
   <iframe src="https://www.youtube.com/embed/Nm8wWtoBCTc" frameborder="0" allowfullscreen="true"> </iframe>
 </figure>

## How to use the cookie in the About repo

Then, you can use that function to update your component as follows:

```js
const { cookieValue } = getCookieValue('gitlab_tier')

// ...

if (cookieValue.value) {
  // Do something
}
```

Note that any of this logic is done client side, so we caution against doing extensive DOM manipulation in this manner. This is impacts web performance. Be sure to add reasonable failsafes if a user doesn't have a cookie we expect them to have (via progressive enhancement).
