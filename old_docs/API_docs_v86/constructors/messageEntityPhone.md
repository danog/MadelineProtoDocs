---
title: messageEntityPhone
description: Message entity phone
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityPhone  
[Back to constructors index](index.md)



Message entity phone

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityPhone = ['_' => 'messageEntityPhone', 'offset' => int, 'length' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageEntityPhone", "offset": int, "length": int}
```


Or, if you're into Lua:

```lua
messageEntityPhone={_='messageEntityPhone', offset=int, length=int}

```


