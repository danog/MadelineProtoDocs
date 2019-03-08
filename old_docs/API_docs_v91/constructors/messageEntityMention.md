---
title: messageEntityMention
description: Message entity mention
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityMention  
[Back to constructors index](index.md)



Message entity mention

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|length|[int](../types/int.md) | Yes|Length|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityMention = ['_' => 'messageEntityMention', 'offset' => int, 'length' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageEntityMention", "offset": int, "length": int}
```


Or, if you're into Lua:

```lua
messageEntityMention={_='messageEntityMention', offset=int, length=int}

```


