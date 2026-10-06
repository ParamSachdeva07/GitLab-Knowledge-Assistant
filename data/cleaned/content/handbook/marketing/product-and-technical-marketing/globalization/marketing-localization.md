---
title: "Marketing Localization"
description: Overview of GitLab's marketing localization proccesses and infrastructure that enmable about.gitlab.com to be available in multiple languages.
---

## Marketing Localization

Our website is now available in 6 languages. The translated content of our website pages is stored across the [about-gitlab-com](https://gitlab.com/gitlab-com/marketing/digital-experience/about-gitlab-com/-/tree/main/content) project. For further technical details on localizing marketing content, go to the [Digital Experience's Localization best practices team Handbook page](/handbook/marketing/digital-experience/engineering/localization/)

### List of localized websites

| Language | Localized Landing Page | Status |
| ------ | ------------ | ------ |
| French | https://about.gitlab.com/fr-fr/ | Live |
| Japanese | https://about.gitlab.com/ja-jp/ | Live |
| German | https://about.gitlab.com/de-de/ | Live |
| Italian | https://about.gitlab.com/it-it/ | Live |
| Brazilian Portuguese | https://about.gitlab.com/pt-br/ | Live |
| Spanish | https://about.gitlab.com/es/ | Live |

### International Blogs

GitLab's blog is available in Japanese, French and German, with a dedicated content manager:

| Language | URL | Content Manager |
| ------ | ------------ | ------ |
| JA | https://about.gitlab.com/ja-jp/blog/ | [Megumi Uchikawa](https://gitlab.com/muchikawa) |
| FR | https://about.gitlab.com/fr-fr/blog/ | [Maud Leuenberger](https://gitlab.com/maud-L) |
| DE | https://about.gitlab.com/de-de/blog/ | [Hendrik Breuer](https://gitlab.com/hbreuer-ext) |

### Translating content for campaigns

The Integrated Marketing team typically drives which translations are required, based on current campaigns and regional need. Localized campaigns currently follow the [integrated campaign process](/handbook/marketing/campaigns/#campaign-planning). The Integrated Marketing team is responsible for content localization for integrated campaigns.

### Language preference segmentation

In order to offer content and events in preferred languages where available, we have a `Language Preference` Segmentation created in Marketo. Only Marketing Ops can edit these segments. Available languages for this segmentation can be found on the [Marketo page](/handbook/marketing/marketing-operations/marketo/#segmentations). A person will be added to a `Language Preference` segment if they complete a form on our website or respond to a campaign that was offered in one of the available languages.

### Translated URL structure

All translated pages live in a sub-folder dedicated to a specific language. These sub-folders use [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

### hreflang tagging

Search engines use the `hreflang` tag to determine a canonical version for translated pages. We'll use `hreflang` on our translated pages.

`hreflang` tags start with declaration `<link rel="alternate"`, adds URL `href={{url}}`, and ends with `hreflang={{language ISO}}`

Example of a hreflang tag for a URL translated to German.

`<link rel="alternate" href="https://about.gitlab.com/de-de/warum/nutze-continuous-integration-fuer-schnelleres-bauen-und-testen/" hreflang="de" />`

The canonical version of our site will the United States English version on `about.gitlab.com`. We need to add all versions of a page under the page title and link to each one with the appropriate language noted. [Google provides this example](https://developers.google.com/search/docs/advanced/crawling/localized-versions?visit_id=637504000817145606-3833240924&rd=1):

```html
<head>
 <title>Widgets, Inc</title>
  <link rel="alternate" hreflang="en-gb"
       href="https://en-gb.example.com/page.html" />
  <link rel="alternate" hreflang="en-us"
       href="https://en-us.example.com/page.html" />
  <link rel="alternate" hreflang="en"
       href="https://en.example.com/page.html" />
  <link rel="alternate" hreflang="de"
       href="https://de.example.com/page.html" />
 <link rel="alternate" hreflang="x-default"
       href="https://www.example.com/" />
</head>
```

It's important to note we need to declare the default page from our repository as the canonical version to avoid penalties across Google properties.

Aleyda Solis maintains a great [tool to build `hreflang` tags](https://www.aleydasolis.com/english/international-seo-tools/hreflang-tags-generator/) we can use for reference as well.
