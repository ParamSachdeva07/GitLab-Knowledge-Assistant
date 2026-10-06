---
title: "Blog Handbook"
description: "Everything you need to know about suggesting and publishing a post on the GitLab Blog."
---

Welcome to the GitLab Blog handbook! The [GitLab Blog](https://about.gitlab.com/blog/) is managed by the Content Marketing team. The managing editor of the blog is Sandra Gittlen (@sgittlen).

## What is a blog post?

At GitLab, blog posts largely focus on sharing helpful information with the audience ([DevSecOps professionals](/handbook/marketing/product-and-technical-marketing/product-and-solution-marketing/roles-personas/user-personas/)). When you suggest or write a blog post, always consider what it offers the reader. If the post is more internal-focused or a personal essay of sorts, it is likely not a fit for the blog (but could go on your personal LinkedIn page).

Blogs fall into the following categories:

- Technical tutorials/how-tos
- Point of view/thought leadership
- Introduction to features and capabilities
- Open source community
- Customer case studies/interviews
- Company announcement (done in partnership with Executive comms team)
- Feature/change/etc. announcement
- Guest blog to highlight partnerships/alliances

## Who can publish content to the GitLab Blog?

[Everyone can contribute at GitLab](/handbook/company/mission/#mission). For the blog, this means we welcome your blog suggestions, ideas, and drafts. However, the [main blog](https://about.gitlab.com/blog/) is one of the many official voices of GitLab – meaning content that is published there must be carefully vetted to ensure we are accurately representing GitLab – both the company and the product. The Blog Managing Editor and the Director of Global Content Marketing are the [directly responsible individuals (DRIs) for the official GitLab blog](/handbook/people-group/directly-responsible-individuals/) and are tasked with this responsibility.

If you have questions about the GitLab Blog, please reach out to [sgittlen@gitlab.com](mailto:sgittlen@gitlab.com).

## How to suggest a blog idea - NEW PROCESS {#how-to-suggest-a-blog-post}

To suggest a blog idea, create an issue using the [blog submission template](https://gitlab.com/gitlab-com/marketing/brand-product-marketing/content-strategy-and-ops/blog/-/issues/new?issuable_template=blog-post-submission).

When submitting your idea:

- Answer all the questions in the template. They help us provide feedback on your idea.
- Submit your idea at least two weeks before your targeted publication date.
- For corporate/comms requests or blogs on a tight turnaround, submit the issue and reach out to @sgittlen directly.

**Note:** You can also notify the Blog team of a typo or request a change via the [blog submission template](https://gitlab.com/gitlab-com/marketing/brand-product-marketing/content-strategy-and-ops/blog/-/issues/new?issuable_template=blog-post-submission).

The blog editor will review your pitch and either a) approve the post, b) offer suggestions for improvements, or c) explain why the idea might not be a fit for the blog and offer other ideas for getting the message out.

**For newsletter content requests:** Add your request to [this issue](https://gitlab.com/gitlab-com/marketing/brand-product-marketing/content-strategy-and-ops/content-ops/-/issues/902).

### External contributions

**Note:** GitLab does not accept unsolicited blog submissions. If you are a GitLab partner and would like to pitch a blog post idea for consideration, please [email sgittlen@gitlab.com](mailto:sgittlen@gitlab.com). If you are a GitLab community member and would like to pitch a blog post idea for consideration, please [email contributors@gitlab.com](mailto:contributors@gitlab.com). Please DO NOT SEND drafts of your blogs with your pitch.

Pitch ideas must be relevant to the GitLab Blog and our readers and include the following information:

- What will your blog be about? Please be as specific as possible.
- Which of the following best describes your blog? (Please check at least one box.)

- [ ] tutorial/how-to on how best to use a feature/capability
- [ ] best practices for how to use the GitLab platform
- [ ] the open source community and GitLab
- [ ] partner/alliance integration
- [ ] other - please explain

**All blog pitch ideas and submissions will be vetted and reviewed by GitLab team members.**

Blog editors, please add the following two sentences at the beginning of contributed articles:

***Editor's note: From time to time, we invite members of the community to contribute to the GitLab Blog. Thanks to [entity name] for co-creating with us.***

External contributions are subject to the [External Blog Submissions Terms](https://about.gitlab.com/externalblogsubmissionsterms/). Please read this document and agree to terms before submitting material to GitLab.

## How to submit a blog draft once your idea is approved

**Once a blog pitch is approved,** the author will use one of the following options to submit their draft:

- Submit via a merge request in GitLab. To do this, [please follow these steps to do so from the repo](/handbook/marketing/digital-experience/decap-cms/#creating-a-blog-post-in-the-aboutgitlabcom-repository) or [for the IDE](/handbook/marketing/digital-experience/decap-cms/#creating-a-blog-post-using-the-web-ide). Please follow them CAREFULLY! Reach out to @sgittlen with any questions.

- Submit via Decap, our basic content management system, [using these steps](/handbook/marketing/digital-experience/decap-cms/#creating-a-blog-post-using-decap-cms). Please follow them CAREFULLY! Reach out to @sgittlen with any questions.

- Submit via Google Docs using the [Blog Submission template](https://docs.google.com/document/d/1iWk0a5T14dG5fvIxvG4doqqRxx0pyv3ej_aMDqYXjgA/template/preview) (Google Doc) to write the blog, ensuring the Google Doc is linked in the issue. **All fields in the template will have to be completed for the blog team to accept the submission.** The author will tag @sgittlen in the issue, put the doc link in a comment, and share the Google Doc once it is ready to be edited (after all necessary approvals and reviews have been completed). **Note:** All images must be included inline in the Google Doc.

**Note:** All blog submissions now require a **call to action** or CTA and you will be asked to provide one in the blog draft template. A CTA is what you want the reader to do next after reading your blog. Do you want them to go to another page and learn more, sign up for a trial, register for a webinar, view a demo, etc.? We will be able to track the CTA as part of our overall blog metrics.

Whatever way you choose to submit your blog, please ensure that @sgittlen is tagged.

**BLOGS CANNOT BE PUBLISHED WITHOUT REVIEW/APPROVAL FROM THE BLOG TEAM.**

## Guide to the frontmatter in the MR

The MR will include the following frontmatter. Please see the comments after each section

```text
seo:
  title: the blog post title
  description: the blog post description
  <!-- Blog team will fill this area in -->
config:
  slug: blog-post-slug
  featured: false
  template: BlogPost
  <!-- blog team will fill this in -->
content:
  title: the blog post title
  <!-- ideal length - 55-60 characters -->
  description: the blog post description
  <!-- ideal length - no more than 155 characters -->
  authors:
    - Blog post author
  <!-- Format: Sandra Gittlen (if this is your first time contributing, leave blank, and if there are multiple authors, add a comma no space between)-->
  heroImage: images/blog/hero-images/logoforblogpost.jpg
  <!-- blog team will fill this in -->
  date: '2021-03-31'
  category: engineering
  <!-- blog team will fill this in -->
  tags:
    - community
  <!-- blog team will fill this in -->
  body: |
    add the blog post body text in markdown
```

## The blog edit process

The blog team will communicate initial edits/questions for the author using the issue and Google Doc. The blog team will then put the blog into the CMS and, if necessary, share a preview link with the author/DRI. Note: The blog will be published from Contentful.

If changes are needed post-publication, the author will reach out to the blog team via Slack and explain the change or submit an MR by going to the bottom of the published page and clicking on edit this page, which will kick off an MR.

The blog team will share the blog's URL with the author once it is published.

Publishing of blog posts occurs according to an editorial calendar. However, that is subject to change based on blogs that are urgent. The blog team will update authors as to their expected publish dates.

### Legal review process

Some blog posts must be reviewed by legal, in accordance with our [Materials Legal Review Process/SAFE program](/handbook/legal/materials-legal-review-process/). Authors are responsible for reviewing SAFE guidelines and getting Legal approval before sharing the Google Doc with the blog team. This process can take time, so please plan target publication dates accordingly.

GitLab has a bias for action, and the Blog team is no different. However, the GitLab Blog is a public-facing asset and represents the company. If the Blog team has concerns or questions about the information contained in the blog post, the Blog team has the authority to hold a blog post until Legal, Corporate Commmunications, Partner Marketing, the CMO, etc., can review the blog post to mitigate any potential risk for the company.

Learn more about the [SAFE Guidelines by reading the handbook page](/handbook/legal/safe-framework/) and following the [Materials Legal Review Process](/handbook/legal/materials-legal-review-process/).

## How to suggest a change to a published blog

- If you are internal to GitLab and want to suggest a change to a published GitLab blog, please post the change you need in detail with the URl in the `#content` Slack channel and tag @sgittlen or ping @sgittlen directly in Slack or create an MR with the change needed by going to the bottom of the published page and clicking on "Edit this page," which will kick off an MR.

- If you are external to GitLab, please email Sandra Gittlen at  `sgittlen@gitlab.com` with the details of your suggested change or create an MR with the change needed by going to the bottom of the published page and clicking on "Edit this page," which will kick off an MR.

## Communication with Blog team

Chat channels:

- Use `#content` for questions (also tag @sgittlen)
- Use `#content-updates` to see updates on recently published articles
- Slack @sgittlen directly

## Other related pages

- [Editorial style guide](/handbook/marketing/product-and-technical-marketing/content/editorial-team/)
- [Brand guidelines](https://design.gitlab.com/)
- [Monthly release post](https://docs.gitlab.com/development/documentation/release_notes/)

## Considerations when drafting a blog

### Diversity, Inclusion, and Belonging (DIB) checklist for blog writers

It is important that our blog content represents our company values of diversity, inclusion, and belonging. Not all of these points will be relevant to your blog post, but they are important values and practices to be mindful of throughout the writing process. The blog editorial team tries to check for these things, but it is better if all content is created with these values and practices in mind. Tag us or a member of the [DIB team](/handbook/company/culture/inclusion/) if you have questions!

#### Inclusive writing

- Write short and concise sentences. Clear writing with short sentences makes it easier for the reader to follow along.
- Limit your use of jargon, and if you must use a jargon-y term, define it on the first instance.
- GitLab is a global team with a global community, so you want to write for a global audience. This means limiting your use of regional metaphors and not writing in a manner that is United States-centric.
- Does the post use [inclusive language](/handbook/company/culture/inclusion/#inclusive-language)?
- Is every individual in the blog post quoted using their [preferred pronoun](/handbook/people-group/orientation-identity/#how-do-i-know-which-pronouns-to-use)? Tip: If you don't know someone's preferred pronoun, just ask them. They should also be included on the [team page profile](https://gitlab.com/close-modal) and Slack profile.

#### More DIB writing tips

- Is your blog post biased? We all have unconscious biases. Check the [list of unconscious biases in our DIB handbook page](/handbook/company/culture/inclusion/unconscious-bias) and practice strategies for recognizing and managing yours.
- If you still have questions, don't hesitate to tag the editorial team lead @sgittlen, leads of the appropriate [team member resource group (TMRG)](/handbook/company/culture/inclusion/tmrg-tmag/) in your blog issue, or email diversityinclusionandbelonging@gitlab.com with your questions.

### Blog categories and tags

#### Categories

Use only **one** of the following categories per post.
**Do not** change the capitalization, spelling, or anything else,
otherwise you'll create another category, which is something we don't want to do accidentally.

If you're not sure which category your post belongs in, just put a placeholder in your MR and leave a comment for your reviewer noting that.

- `agile planning` - posts about AgiLe planning
- `ai-ml` – posts that focus directly on AI/ML in the platform or in the industry as a whole
- `customer stories` - posts about how our customers are using GitLab DevSecOps platform
- `bulletin board` - where shorter blogs/announcements go
- `DevSecOps` - posts more generally about DevSecOps
- `engineering` – technical, actionable content. Anything covering how to do something, use something, or solve a problem should fall under this category
- `open source` – stories from or about our community, users, or the wider open source community
- `product` - details about features, roadmaps, and strategy
- `news` – company or product announcements (including policy changes, operational announcements, and breaking changes), news, or events
- `security` – security-related posts
- `releases` - release posts, security and patch releases. Posts in the `releases` category need to be in the `sites/uncategorized/source/releases/posts` directory, not `sites/uncategorized/source/blog/blog-posts`. Please see the [Release Post handbook](https://docs.gitlab.com/development/documentation/release_notes/) for more.

#### Tags

These are included to help readers find similar posts if they are interested in a particular subject. Tags appear at the top of each blog post, and clicking on a tag takes you to the specific `/blog/tags/specific-tag` where you can view all posts with the specified tag.

You can include as many tags as you like, separated by commas. Please only include tags from the following list, and note that they are case sensitive.

- agile
- AI/ML
- automotive
- AWS
- bug bounty
- careers
- CI/CD
- cloud native
- code review
- collaboration
- community
- contributors
- customers
- demo
- design
- developer survey
- DevSecOps
- DevSecOps platform
- embedded development
- education (articles about the education sector)
- events
- features
- financial services
- frontend
- git
- GitOps
- GKE
- google
- growth
- inside GitLab
- integrations
- kubernetes
- news
- open source
- partners
- patch releases
- performance
- product
- production
- public sector
- releases
- remote work
- research
- security
- security releases
- security research
- solutions architecture
- startups
- testing
- tutorial
- UI
- user stories
- UX
- webcast
- workflow
- zero trust

### Media embeds

[Instructions for including video](/handbook/marketing/digital-experience/decap-cms/#creating-a-blog-post-using-the-web-ide).

### Adding code blocks

[Instructions for adding code blocks](/handbook/marketing/digital-experience/decap-cms/#creating-a-blog-post-using-the-web-ide).

#### Mermaid charts

[How to embed mermaid charts into MR](https://gitlab.com/gitlab-com/marketing/digital-experience/gitlab-blog/-/merge_requests/211#usage-notes). Please read as there are nuances that might prevent your chart from rendering properly.

#### Preparing images

- If creating an original cover image, the dimensions should be 1800px x 945px for optimal quality on all displays.
- All images should aim to be less than 1MB. JPEGs tend to be smaller than PNGs so use JPEGs when possible.
- To resize in Preview go to `Tools`, `Adjust size` and adjust the entry in the `Resolution` field. Preview will estimate what the resulting image size will be before you click `OK` to confirm.
- Keep all the images the same width.

#### Screenshots

For technical/tutorial posts, please illustrate your examples with [code blocks](#adding-code-blocks) or screenshots. Be consistent with your examples. E.g., if you are using a generic URL
to exemplify your steps `domain.com`, be consistent and keep it `domain.com`, throughout the post.

- Static images should be used to illustrate concepts, provide diagrams, elements of the UI or orient the reader.
- Images should not be used to render commands or configuration which would prevent someone being able to copy and paste.
- Animated GIFs can be used sparingly where you need to show a process or some event happening over the course of time or several actions, though they should not replace text descriptions or instructions.
- Use screenshots to identify and localize specific parts of the screen. There are great tools for doing so. For example, Nimbus Screenshot (browser extension), Mac screenshot, Snipping Tool for Windows, and Screenshot Tool for Ubuntu.

**Important security point:** Do not expose your personal details by using your real tokens or security credentials. Use placeholders such as `[project's CI token]` stub instead. Or blur them if displayed on screenshots.

#### Embedding tweets or Instagram posts

Please see the [Markdown guide for instructions for embedding posts from social media](https://about.gitlab.com/community/markdown-guide-middleman/#embed-tweets).

#### Creating GIFs

Animated GIFs are very useful to illustrate short dynamic processes, which might be easier to understand with this kind of resource.
There are a few ways to create animated GIFs, one of them is using [Giphy Capture], a light-weight app for Mac.

Avoid GIFs with a huge file size, they will be difficult to load for users with bad internet connection. In those cases, you can either cut the GIFs in smaller pieces, or record a video, or use a sequential image.

### Creating `Author` entries in the CMS

Here's a set of recommendations **when creating** an `Author` entry in the CMS (Decap).

- `Name` field
    This is a required field. It is also a unique field.

    1. Author's name should be a combination of first and last name only, including composed names. Please avoid adding a job description (use the `Role` field for this task) or alpha-numeric combinations into this field.
    1. No double authors (eg. `/authors/<author1>-<author2>`). We can add multiple single authors to blog posts. We should create individual authors and then add them all to other content types as a one-to-many relationship.
    1. Same as above, no multiple authors for a single blog post (eg. `/authors/<author1>-<author2>-<author3>-and-<author4>`).

- `Role` field

    Current working position or job description.

- `Bio` field

    Biography of the Author.

- `GitLab handle` field

    It corresponds to Author's GitLab username in lowercase format. This field has to be unique.

- `Social media handles` fields

    Optional fields for social media handles.

## Localizing blog posts in the CMS

We can publish blog posts in languages other than English. We currently support the following languages:

| Language | URL structure|
|---------|----------|
| French |`/fr-fr/blog/YEAR/MONTH/DAY/Title/` |
| German |`/de-de/blog/YEAR/MONTH/DAY/Title/` |
| Japanese |`/ja-jp/blog/YEAR/MONTH/DAY/Title/` |

Please contact the GitLab localization team for more information.

### How to kick off translations

Starting the process of getting a blog post translated is easy. Follow these steps:

1. Create a translation request issue in the Localization project. Pro tip - add the URL for the blog post and a direct link to the Contentful entry. It will be super helpful to you as you track the project.
2. Argo will export the English blog post as JSON and import the translated JSON back into Contentful. Then you'll be pinged in the issue when it's ready for review.
3. Hop into the entry for the blog post and review the translated content.
4. Coordinate with @sgittlen on publishing the translated post.
5. Once published, always verify that it's working as expected on about.gitlab.com/blog/.
6. Celebrate your translated blog post by posting it in Slack.

Here's a video walkthrough of the full process from creating the translation request to publishing on production.

- Video recording comming soon that demonstrates the following
- Create issue
- Argo roundtrip
- Translation show up in Contentful
- Review the translations
- Live previews/changing languages
- Publish

### Gotchas When localizing an EN blog post

Things to be careful about when localizing an EN blog post.

- Don't change the slug!

### Tags to keep organized

- If a post in process of being translating, put the "translation-in-progress" label on it. This enables the team to easily find all blog posts in Contentful that are in progress of being translated and reviewed.
- Remove and apply local label to languages the post is translated into.
| Tag | Definition | How to use |
|----|----|----|
| translation-in-progress | Notes when a blog post is currently be translated and reviewed | Apply when translation request is opened. Remove when post is published |
| language_de-DE | Marks entry that is in German | Apply to blog post that is translated into German |
| language_fr-FR | Marks entry that is in French | Apply to blog post that is translated into French |
| language_ja-JP | Marks entry that is in Japanese | Apply to blog post that is translated into Japanese |
