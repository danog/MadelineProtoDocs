---
title: messageEntityTextUrl
description: messageEntityTextUrl attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityTextUrl  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offset|[int](../types/int.md) | Yes|
|length|[int](../types/int.md) | Yes|
|url|[string](../types/string.md) | Yes|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityTextUrl = ['_' => 'messageEntityTextUrl', 'offset' => int, 'length' => int, 'url' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageEntityTextUrl", "offset": int, "length": int, "url": "string"}
```


Or, if you're into Lua:

```lua
messageEntityTextUrl={_='messageEntityTextUrl', offset=int, length=int, url='string'}

```


