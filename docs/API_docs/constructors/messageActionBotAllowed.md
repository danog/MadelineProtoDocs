---
title: "messageActionBotAllowed"
description: "We have given the bot permission to send us direct messages."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionBotAllowed  
[Back to constructors index](/API_docs/constructors/index.html)



We have given the bot permission to send us direct messages.

The optional fields specify how did we authorize the bot to send us messages.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|attach\_menu|[Bool](/API_docs/types/Bool.html) | Optional|We have authorized the bot to send us messages by installing the bot's [attachment menu](https://core.telegram.org/api/bots/attach).|
|domain|[string](/API_docs/types/string.html) | Optional|We have authorized the bot to send us messages by logging into a website via [Telegram Login »](https://core.telegram.org/widgets/login); this field contains the domain name of the website on which the user has logged in.|
|app|[BotApp](/API_docs/types/BotApp.html) | Optional|We have authorized the bot to send us messages by opening the specified [bot web app](https://core.telegram.org/api/bots/webapps).|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionBotAllowed = ['_' => 'messageActionBotAllowed', 'attach_menu' => Bool, 'domain' => 'string', 'app' => BotApp];
```  
