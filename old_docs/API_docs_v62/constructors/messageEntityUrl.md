---
title: messageEntityUrl
description: messageEntityUrl attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityUrl  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offset|[int](../types/int.md) | Yes|
|length|[int](../types/int.md) | Yes|



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


