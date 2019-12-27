---
title: botInfo
description: Info about bots (available bot commands, etc)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInfo  
[Back to constructors index](index.md)



Info about bots (available bot commands, etc)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|ID of the bot|
|description|[string](../types/string.md) | Yes|Description of the bot|
|commands|Array of [BotCommand](../types/BotCommand.md) | Yes|Commands|



### Type: [BotInfo](../types/BotInfo.md)


### Example:

```php
$botInfo = ['_' => 'botInfo', 'user_id' => int, 'description' => 'string', 'commands' => [BotCommand, BotCommand]];
```  


Or, if you're into Lua:

```lua
botInfo={_='botInfo', user_id=int, description='string', commands={BotCommand}}

```


