---
title: "updateBotCommands"
description: "updateBotCommands attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotCommands  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|
|bot\_id|[long](/API_docs/types/long.md) | Yes|
|commands|Array of [BotCommand](/API_docs/types/BotCommand.md) | Yes|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateBotCommands = ['_' => 'updateBotCommands', 'peer' => Peer, 'bot_id' => long, 'commands' => [BotCommand, BotCommand]];
```  
