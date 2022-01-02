---
title: "botCommand"
description: "Describes a bot command that can be used in a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botCommand  
[Back to constructors index](index.md)



Describes a bot command that can be used in a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|command|[string](../types/string.md) | Yes|`/command` name|
|description|[string](../types/string.md) | Yes|Description of the command|



### Type: [BotCommand](../types/BotCommand.md)


### Example:

```php
$botCommand = ['_' => 'botCommand', 'command' => 'string', 'description' => 'string'];
```  


Or, if you're into Lua:

```lua
botCommand={_='botCommand', command='string', description='string'}

```


