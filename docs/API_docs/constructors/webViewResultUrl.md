---
title: "webViewResultUrl"
description: "Contains the webview URL with appropriate theme and user info parameters added"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webViewResultUrl  
[Back to constructors index](/API_docs/constructors/index.html)



Contains the webview URL with appropriate theme and user info parameters added

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|fullsize|[Bool](/API_docs/types/Bool.html) | Optional|If set, the app must be opened in fullsize mode instead of compact mode.|
|fullscreen|[Bool](/API_docs/types/Bool.html) | Optional|If set, the app must be opened in fullscreen|
|query\_id|[long](/API_docs/types/long.html) | Optional|Webview session ID (only returned by [inline button mini apps](https://core.telegram.org/api/bots/webapps#inline-button-mini-apps), [menu button mini apps](https://core.telegram.org/api/bots/webapps#menu-button-mini-apps), [attachment menu mini apps](https://core.telegram.org/api/bots/webapps#attachment-menu-mini-apps)).|
|url|[string](/API_docs/types/string.html) | Yes|Webview URL to open|



### Type: [WebViewResult](/API_docs/types/WebViewResult.html)


### Example:

```
$webViewResultUrl = ['_' => 'webViewResultUrl', 'fullsize' => Bool, 'fullscreen' => Bool, 'query_id' => long, 'url' => 'string'];
```  
