---
title: "connectedBot"
description: "Contains info about a connected business bot »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: connectedBot  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [connected business bot »](https://core.telegram.org/api/business#connected-bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_reply|[Bool](/API_docs/types/Bool.html) | Optional|Whether the the bot can reply to messages it receives through the connection|
|bot\_id|[long](/API_docs/types/long.html) | Yes|ID of the connected bot|
|recipients|[BusinessBotRecipients](/API_docs/types/BusinessBotRecipients.html) | Yes|Specifies the private chats that a [connected business bot »](https://core.telegram.org/api/business#connected-bots) may receive messages and interact with.<br>|



### Type: [ConnectedBot](/API_docs/types/ConnectedBot.html)


### Example:

```
$connectedBot = ['_' => 'connectedBot', 'can_reply' => Bool, 'bot_id' => long, 'recipients' => BusinessBotRecipients];
```  
