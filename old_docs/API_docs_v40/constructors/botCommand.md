---
title: botCommand
description: Bot command
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botCommand  
[Back to constructors index](index.md)



Bot command

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|command|[string](../types/string.md) | Yes|Command|
|description|[string](../types/string.md) | Yes|Description|



### Type: [BotCommand](../types/BotCommand.md)


### Example:

```php
$botCommand = ['_' => 'botCommand', 'command' => 'string', 'description' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "botCommand", "command": "string", "description": "string"}
```


Or, if you're into Lua:

```lua
botCommand={_='botCommand', command='string', description='string'}

```


