---
title: "messages.botCallbackAnswer"
description: "Callback answer sent by the bot in response to a button press"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_botCallbackAnswer.html
---
# Constructor: messages.botCallbackAnswer  
[Back to constructors index](/API_docs/constructors/index.html)



Callback answer sent by the bot in response to a button press

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|alert|[Bool](/API_docs/types/Bool.html) | Optional|Whether an alert should be shown to the user instead of a toast notification|
|has\_url|[Bool](/API_docs/types/Bool.html) | Optional|Whether an URL is present|
|native\_ui|[Bool](/API_docs/types/Bool.html) | Optional|Whether to show games in WebView or in native UI.|
|message|[string](/API_docs/types/string.html) | Optional|Alert to show|
|url|[string](/API_docs/types/string.html) | Optional|URL to open|
|cache\_time|[int](/API_docs/types/int.html) | Yes|For how long should this answer be cached|



### Type: [messages.BotCallbackAnswer](/API_docs/types/messages.BotCallbackAnswer.html)


### Example:

```
$messages_botCallbackAnswer = ['_' => 'messages.botCallbackAnswer', 'alert' => Bool, 'has_url' => Bool, 'native_ui' => Bool, 'message' => 'string', 'url' => 'string', 'cache_time' => int];
```  
