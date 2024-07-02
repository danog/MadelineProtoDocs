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
|fullsize|[Bool](/API_docs/types/Bool.html) | Optional|
|query\_id|[long](/API_docs/types/long.html) | Optional|Webview session ID|
|url|[string](/API_docs/types/string.html) | Yes|Webview URL to open|



### Type: [WebViewResult](/API_docs/types/WebViewResult.html)


### Example:

```
$webViewResultUrl = ['_' => 'webViewResultUrl', 'fullsize' => Bool, 'query_id' => long, 'url' => 'string'];
```  
