---
title: messageEntityBotCommand
description: Message entity bot command
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityBotCommand  
[Back to constructors index](index.md)



Message entity bot command

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityBotCommand = ['_' => 'messageEntityBotCommand', 'offset' => int, 'length' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageEntityBotCommand", "offset": int, "length": int}
```


Or, if you're into Lua:

```lua
messageEntityBotCommand={_='messageEntityBotCommand', offset=int, length=int}

```


