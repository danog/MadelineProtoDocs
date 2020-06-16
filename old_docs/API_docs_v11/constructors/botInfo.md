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
|version|[int](../types/int.md) | Yes|
|share\_text|[string](../types/string.md) | Yes|
|description|[string](../types/string.md) | Yes|Description of the bot|
|commands|Array of [BotCommand](../types/BotCommand.md) | Yes|Bot commands that can be used in the chat|



### Type: [BotInfo](../types/BotInfo.md)


### Example:

```php
$botInfo = ['_' => 'botInfo', 'user_id' => int, 'version' => int, 'share_text' => 'string', 'description' => 'string', 'commands' => [BotCommand, BotCommand]];
```  


Or, if you're into Lua:

```lua
botInfo={_='botInfo', user_id=int, version=int, share_text='string', description='string', commands={BotCommand}}

```


