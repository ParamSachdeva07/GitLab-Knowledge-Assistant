---
title: 'App development'
description: 'Documentation on Zendesk app development'
---

This guide covers the development of Zendesk apps at GitLab.

{{% alert title="Note" color="primary" %}}

- This is generalized information we have found helpful in the course of app development. It is not a single source of truth.
- It is expected you have a solid understanding in programming HTML, CSS, and JavaScript to develop a Zendesk app.

{{% /alert %}}

## Understanding Zendesk Apps

Before you can start creating and editing apps in Zendesk, it is important to understand the ins and outs of both Zendesk Apps and [Zendesk Apps framework](https://developer.zendesk.com/documentation/apps/app-developer-guide/using-the-apps-framework/).

There is a lot to this, so the Zendesk documentation is the best resource you have to learn the various ins and outs. This training documentation will cover what is viewed at “the most important” parts, but it is highly recommended you read and reference the [Zendesk developer documentation](https://developer.zendesk.com/documentation/apps/app-developer-guide/getting_started/) as often as possible.

## ZAT

ZAT, or Zendesk App Tools, is a ruby gem that makes working with Zendesk Apps locally considerably easier. It is highly recommended you install it on your computer:

```bash
gem install rake
gem install zendesk_apps_tools
```

To update it:

```bash
gem update rake
gem update zendesk_apps_tools
```

Sometimes on Mac terminal, you will get write permission error. You may use:

```bash
sudo gem update rake
sudo gem update zendesk_apps_tools
```

## manifest.json

This file is used to configure you application. As such, it is very important and vital it is accurate.

The common configuration settings are:

| Setting | What it does | Required? |
|---------|--------------|:---------:|
| name | Specifies the name of the app | Y |
| author | Specifies the author of the app | Y |
| version | Specifies the app version | Y |
| frameworkVersion | Specifies the framework version to use | Y |
| location | Specifies where the app appears | Y |
| defaultLocale | Specifies the locale (language) of the app | Y |
| parameters | The parameters to pass to the app during installation | N |
| domainWhitelist  | The domains to allow use of secure parameters | N |
| private | Specifies whether the app can be only be installed in the app developer's account or not | N |

## Location

This setting determines where the app will appear and run. This is a very important setting. The first setting determines the product type location, and within that setting you can specify many other configurations, including the physical location the app will appear in. For the product type location, we always use `support`.

The physical locations are as follows:

| String | Location/Purpose |
|--------|------------------|
| `ticket_sidebar` | The right side of all ticket view pages |
| `new_ticket_sidebar` | The right side of the new ticket creation page |
| `ticket_editor` | A button on the ticket editor box |
| `nav_bar` | An icon on the left-side navigation bar |
| `top_bar` | An icon on the right side of the top menu |
| `user_sidebar` | The right side of all user view pages |
| `organization_sidebar` | The right side of all organization view pages |
| `background` | The app runs in the background without displaying a UI. Use for apps that only need to listen to events or run scheduled tasks |
| `modal` | Used when the app creates modals |

Within the physical location settings, you can include more configuration settings, with the most common being:

| String | What it does | Variable type |
|--------|--------------|---------------|
| `autoHide` | Tells the app to auto-collapse on first load | Boolean |
| `autoLoad` | Tells the app to automatically load (defaults to true) | Boolean |
| `signed` | Specifies whether or not to use signed URLs | Boolean |
| `url` | The URL of the page to display in the iframe of the app | String |
| `size` | The initial app size (configure this in the app instead) | JSON |

As an example, to have an app load `https://google.com` automatically in the ticket sidebar with a starting height of 200px, your configuration block would look like this:

```json
"location": {
  "support": {
    "ticket_sidebar": {
      "autoLoad": true,
      "url": "https://google.com/",
      "size": {
        "height": "200px"
      }
    }
  }
}
```

As another example, to have your app load in both the user and organization pages, rendering the local `assets/iframe.html` file, you would do this:

```json
"location": {
  "support": {
    "user_sidebar": "assets/iframe.html",
    "organization_sidebar": "assets/iframe.html"
  }
}
```

## Parameters

This is where you would define variables you want the app to use during installation.

### Domain whitelists

If your app is using secure parameters and you plan to make requests outside of Zendesk, you must whitelist the domains in question. An example of doing this would look like:

```json
{
  "domainWhitelist": [
    "gitlab.com",
    "google.com"
  ]
}
```

### Entries

Each parameter entry is a hash that contains the following:

- `name`: the name of the parameter
- `type`: the type of parameter
- `secure`: ensures users cannot see the variable value when making HTTP requests (you should *always* use this)
- `required`: specifies if the parameter is required for installation

As an example, to use two required parameters (`param1` and `param2`), both of which are text parameters in a secure way, you would do the following:

```json
{
  "parameters": [
    {
      "name": "param1",
      "type": "text",
      "secure": true,
      "required": true
    },
    {
      "name": "param2",
      "type": "text",
      "secure": true,
      "required": true
    }
  ]
}
```

During the installation of the app, Zendesk will ask you to give the values for these parameters. To utilize this in the code of your app, you will use this:

`{{setting.NAME_OF_PARAMETER}}`

Where `NAME_OF_PARAMETER` is the name you gave the parameter in the manifest.json file.

## Required JavaScript library

To utilize the ZAT, you must include the following javascript in your app's HTML file(s):

```html
<script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
```

### init

To create a client instance of the ZAF (Zendesk App Framework) client, you need to ensure the following is present in the javascript of your app:

```javascript
var zafclient = ZAFClient.init();
```

### App resizing

To resize the app during runtime, you would use the `invoke` class, specifying you wish to invoke the `resize` function. This is done like so:

```javascript
var zafclient = ZAFClient.init();
zafclient.invoke('resize', { width: '100%', height: '100px' });
```

### Getting metadata

To get metadata and use it in your app, you need to use the ZAF client's `get` function. This takes an array of values to get from the ticket metadata, which you use in a function.

As an example, to get the ticket requester's name and the ticket's organization, and then log them to the console, you would do the following:

```javascript
var zafclient = ZAFClient.init();
zafclient.get(['ticket.requester.name', 'ticket.organization']).then(function(data) {
  console.log("Ticket requester name: " + data['ticket.requester.name']);
  console.log("Ticket organization: " + data['ticket.organization.name']);
});
```

As another example, to get the ticket's due date and the due date notes (a custom ticket field) and then log them to the console, you would do the following:

```javascript
var zafclient = ZAFClient.init();
zafclient.get(['ticket.customField:due_date', 'ticket.customField:custom_field_360017383799']).then(function(data) {
  console.log("Due date": + data['ticket.customField:due_date']);
  console.log("Due date notes:" + data['ticket.customField:custom_field_360017383799']);
});
```

### Making requests

Your app might need to make requests, whether they be "internal" (i.e. within Zendesk itself) or external. To do this, we use the `request` function of the client object.

The format of this is *very* close to that of making [AJAX requests](https://api.jquery.com/jquery.ajax/) in jQuery. The format you will normally use is:

```javascript
var zafclient = ZAFClient.init();
zafclient.request({
  method: 'REQUEST_TYPE',
  url: 'URL_TO_USE',
  contentType: 'CONTENT_MEDIA_TO_SEND',
  data: DATA_OBJECT,
  secure: BOOLEAN,
  headers: HEADERS_OBJECT
}).then(function(data) {
  // do stuff
}).catch(function(error) {
  console.error('Request failed:', error);
});
```

The exact parameters in the request will vary from request to request.

As an example, if you wanted to update the due date of a ticket, you might do:

```javascript
var zafclient = ZAFClient.init();
zafclient.request({
  method: 'PUT',
  url: '/api/v2/tickets/123456.json',
  contentType: 'application/json',
  data: JSON.stringify({
    due_at: new Date('2021-01-01').toISOString()
  }),
  secure: BOOLEAN,
  headers: HEADERS_OBJECT
}).then(function(data) {
  console.log('Due date updated to 2021-01-01');
});
```

As another example, if you wanted to make a GET request to gitlab.com to find information about user ID 987654, using a secure parameter from app installation, you might do:

```javascript
var zafclient = ZAFClient.init();
zafclient.request({
  method: "GET",
  url: 'https://gitlab.com/api/v4/users/987654?private_token={{setting.GitLab_token}}',
  secure: true
}).then(function(data) {
  console.log('User email: ' + data.email);
});
```

## Human readable replacements

Currently, the sync repo can perform replacements of various items from a human readable item to the "Zendesk" equivalent item in JavaScript and HTML files. This includes:

| Human readable item | Zendesk field item | Notes |
|---------------------|--------------------|-------|
| `[[Field: XXX]]` | A ticket field ID | Replace `XXX` with the ticket field's title |
| `[[Form: XXX]]` | A ticket form ID | Replace `XXX` with the ticket form's name |

As an example, if you wanted to reference the ID of the ticket form `Support Ops`, you would do:

```javascript
var support_ops_form_id = [[Form: Support Ops]]
```

Likewise, to reference the ID fo the ticket field `Customer Priority`, you would do:

```html
<div data-field-id='[[Field: Customer Priority]]'>
  <!-- Stuff goes here -->
</div>
```

Keep in mind this is technically "invalid" code in Javascript, so if using `zat` to run it locally, it will cause errors. Only the `sync` style scripts do the conversion itself.

## Testing an app

There are two ways to test a Zendesk app before you put it into production.

### Locally

{{% alert title="Note" color="primary" %}}

This cannot be done if your app is using secure parameters. Instead, you would need to install the app into the Sandbox and test from there.

{{% /alert %}}

To test your app locally, cd into the app directory on your local computer and then run the `zat server` command. This will start up a ZAT server on your computer. Once it has booted up, go to a Zendesk URL and put `?zat=true` at the end. This will now load the apps from your local computer, allowing you to test out the app locally.

### Via the Sandbox

If your app is using secure parameters, you will need to test via the Sandbox instead. This would mean deploying it to the sandbox. See [Zendesk Apps](../apps/) for more information.
