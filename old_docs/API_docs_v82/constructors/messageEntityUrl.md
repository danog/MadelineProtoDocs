---
title: messageEntityUrl
description: Message entity URL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityUrl  
[Back to constructors index](index.md)



Message entity URL

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityUrl = ['_' => 'messageEntityUrl', 'offset' => int, 'length' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageEntityUrl", "offset": int, "length": int}
```


Or, if you're into Lua:

```lua
messageEntityUrl={_='messageEntityUrl', offset=int, length=int}

```


