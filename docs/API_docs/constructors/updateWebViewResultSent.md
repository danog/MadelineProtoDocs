---
title: "updateWebViewResultSent"
description: "Indicates to a bot that a webview was closed and an inline message was sent on behalf of the user using messages.sendWebViewResultMessage"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateWebViewResultSent  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates to a bot that a webview was closed and an inline message was sent on behalf of the user using [messages.sendWebViewResultMessage](../methods/messages.sendWebViewResultMessage.html)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.html) | Yes|Web app interaction ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateWebViewResultSent = ['_' => 'updateWebViewResultSent', 'query_id' => long];
```  
