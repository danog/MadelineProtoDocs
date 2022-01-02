---
title: "updateBotCommands"
description: "updateBotCommands attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotCommands  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](../types/Peer.md) | Yes|
|bot\_id|[long](../types/long.md) | Yes|
|commands|Array of [BotCommand](../types/BotCommand.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotCommands = ['_' => 'updateBotCommands', 'peer' => Peer, 'bot_id' => long, 'commands' => [BotCommand, BotCommand]];
```  


Or, if you're into Lua:

```lua
updateBotCommands={_='updateBotCommands', peer=Peer, bot_id=long, commands={BotCommand}}

```


