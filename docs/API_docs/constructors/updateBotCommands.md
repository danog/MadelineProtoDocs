---
title: "updateBotCommands"
description: "The command set of a certain bot in a certain chat has changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotCommands  
[Back to constructors index](/API_docs/constructors/index.html)



The [command set](https://core.telegram.org/bots/api#june-25-2021) of a certain bot in a certain chat has changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|The affected chat|
|bot\_id|[long](/API_docs/types/long.html) | Yes|ID of the bot that changed its command set|
|commands|Array of [BotCommand](/API_docs/types/BotCommand.html) | Yes|New bot commands|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotCommands = ['_' => 'updateBotCommands', 'peer' => Peer, 'bot_id' => long, 'commands' => [BotCommand, BotCommand]];
```  
