---
title: messageEntityBotCommand
description: Message entity representing a bot /command
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityBotCommand  
[Back to constructors index](index.md)



Message entity representing a bot /command

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityBotCommand = ['_' => 'messageEntityBotCommand', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityBotCommand={_='messageEntityBotCommand', offset=int, length=int}

```


