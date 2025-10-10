---
title: "updateBotBusinessConnect"
description: "Connecting or disconnecting a business bot or changing the connection settings will emit an updateBotBusinessConnect update to the bot, with the new settings and a connection_id that will be used by the bot to handle updates from and send messages as the user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotBusinessConnect  
[Back to constructors index](/API_docs/constructors/index.html)



Connecting or disconnecting a [business bot](https://core.telegram.org/api/bots/connected-business-bots) or changing the connection settings will emit an [updateBotBusinessConnect](../constructors/updateBotBusinessConnect.html) update to the bot, with the new settings and a `connection_id` that will be used by the bot to handle updates from and send messages as the user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|connection|[BotBusinessConnection](/API_docs/types/BotBusinessConnection.html) | Yes|Business connection settings|
|qts|[int](/API_docs/types/int.html) | Yes|New **qts** value, see [updates »](https://core.telegram.org/api/updates) for more info.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotBusinessConnect = ['_' => 'updateBotBusinessConnect', 'connection' => BotBusinessConnection, 'qts' => int];
```  
