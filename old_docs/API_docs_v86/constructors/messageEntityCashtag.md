---
title: messageEntityCashtag
description: Message entity cashtag
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityCashtag  
[Back to constructors index](index.md)



Message entity cashtag

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityCashtag = ['_' => 'messageEntityCashtag', 'offset' => int, 'length' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageEntityCashtag", "offset": int, "length": int}
```


Or, if you're into Lua:

```lua
messageEntityCashtag={_='messageEntityCashtag', offset=int, length=int}

```


