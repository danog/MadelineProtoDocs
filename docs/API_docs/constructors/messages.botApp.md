---
title: "messages.botApp"
description: "messages.botApp attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_botApp.html
---
# Constructor: messages.botApp  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|inactive|[Bool](/API_docs/types/Bool.html) | Optional|
|request\_write\_access|[Bool](/API_docs/types/Bool.html) | Optional|
|app|[BotApp](/API_docs/types/BotApp.html) | Yes|



### Type: [messages.BotApp](/API_docs/types/messages.BotApp.html)


### Example:

```
$messages_botApp = ['_' => 'messages.botApp', 'inactive' => Bool, 'request_write_access' => Bool, 'app' => BotApp];
```  
