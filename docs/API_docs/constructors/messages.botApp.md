---
title: "messages.botApp"
description: "Contains information about a direct link Mini App"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_botApp.html
---
# Constructor: messages.botApp  
[Back to constructors index](/API_docs/constructors/index.html)



Contains information about a [direct link Mini App](https://core.telegram.org/api/bots/webapps#direct-link-mini-apps)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inactive|[Bool](/API_docs/types/Bool.html) | Optional|Whether the web app was never used by the user, and confirmation must be asked from the user before opening it.|
|request\_write\_access|[Bool](/API_docs/types/Bool.html) | Optional|The bot is asking permission to send messages to the user: if the user agrees, set the `write_allowed` flag when invoking [messages.requestAppWebView](../methods/messages.requestAppWebView.html).|
|has\_settings|[Bool](/API_docs/types/Bool.html) | Optional|Deprecated flag, can be ignored.|
|app|[BotApp](/API_docs/types/BotApp.html) | Yes|Bot app information|



### Type: [messages.BotApp](/API_docs/types/messages.BotApp.html)


### Example:

```
$messages_botApp = ['_' => 'messages.botApp', 'inactive' => Bool, 'request_write_access' => Bool, 'has_settings' => Bool, 'app' => BotApp];
```  
