---
title: messageEntityHashtag
description: Message entity hashtag
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityHashtag  
[Back to constructors index](index.md)



Message entity hashtag

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityHashtag = ['_' => 'messageEntityHashtag', 'offset' => int, 'length' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageEntityHashtag", "offset": int, "length": int}
```


Or, if you're into Lua:

```lua
messageEntityHashtag={_='messageEntityHashtag', offset=int, length=int}

```


