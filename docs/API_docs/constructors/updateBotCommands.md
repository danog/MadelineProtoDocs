---
title: "updateBotCommands"
description: "updateBotCommands attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotCommands  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|
|bot\_id|[long](/API_docs/types/long.html) | Yes|
|commands|Array of [BotCommand](/API_docs/types/BotCommand.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```php
$updateBotCommands = ['_' => 'updateBotCommands', 'peer' => Peer, 'bot_id' => long, 'commands' => [BotCommand, BotCommand]];
```  
