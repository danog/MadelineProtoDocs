---
title: messageEntityPre
description: Message entity pre
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityPre  
[Back to constructors index](index.md)



Message entity pre

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|
|language|[string](../types/string.md) | Yes|Language|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityPre = ['_' => 'messageEntityPre', 'offset' => int, 'length' => int, 'language' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageEntityPre", "offset": int, "length": int, "language": "string"}
```


Or, if you're into Lua:

```lua
messageEntityPre={_='messageEntityPre', offset=int, length=int, language='string'}

```


