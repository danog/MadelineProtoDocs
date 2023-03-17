---
title: "messageActionBotAllowed"
description: "The domain name of the website on which the user has logged in. More about Telegram Login »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionBotAllowed  
[Back to constructors index](/API_docs/constructors/index.html)



The domain name of the website on which the user has logged in. [More about Telegram Login »](https://core.telegram.org/widgets/login)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|attach\_menu|[Bool](/API_docs/types/Bool.html) | Optional|
|domain|[string](/API_docs/types/string.html) | Optional|The domain name of the website on which the user has logged in.|
|app|[BotApp](/API_docs/types/BotApp.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionBotAllowed = ['_' => 'messageActionBotAllowed', 'attach_menu' => Bool, 'domain' => 'string', 'app' => BotApp];
```  
