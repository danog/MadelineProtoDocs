---
title: botInfo
description: Bot info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInfo  
[Back to constructors index](index.md)



Bot info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|description|[string](../types/string.md) | Yes|Description|
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


