---
title: messageEntityMention
description: Message entity [mentioning](https://core.telegram.org/api/mentions) the current user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityMention  
[Back to constructors index](index.md)



Message entity [mentioning](https://core.telegram.org/api/mentions) the current user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityMention = ['_' => 'messageEntityMention', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityMention={_='messageEntityMention', offset=int, length=int}

```


