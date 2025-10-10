---
title: "botBusinessConnection"
description: "Contains info about a bot business connection."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botBusinessConnection  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [bot business connection](https://core.telegram.org/api/bots/connected-business-bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|disabled|[Bool](/API_docs/types/Bool.html) | Optional|Whether this business connection is currently disabled|
|connection\_id|[string](/API_docs/types/string.html) | Yes|Business connection ID, used to identify messages coming from the connection and to reply to them as specified [here »](https://core.telegram.org/api/bots/connected-business-bots).|
|user\_id|[long](/API_docs/types/long.html) | Yes|ID of the user that the bot is connected to via this connection.|
|dc\_id|[int](/API_docs/types/int.html) | Yes|ID of the datacenter where to send queries wrapped in a [invokeWithBusinessConnection](../methods/invokeWithBusinessConnection.html) as specified [here »](https://core.telegram.org/api/bots/connected-business-bots).|
|date|[int](/API_docs/types/int.html) | Yes|When was the connection created.|
|rights|[BusinessBotRights](/API_docs/types/BusinessBotRights.html) | Optional|Business bot rights.|



### Type: [BotBusinessConnection](/API_docs/types/BotBusinessConnection.html)


### Example:

```
$botBusinessConnection = ['_' => 'botBusinessConnection', 'disabled' => Bool, 'connection_id' => 'string', 'user_id' => long, 'dc_id' => int, 'date' => int, 'rights' => BusinessBotRights];
```  
