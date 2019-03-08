---
title: messages.affectedHistory
description: Affected history
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.affectedHistory  
[Back to constructors index](index.md)



Affected history

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|
|offset|[int](../types/int.md) | Yes|Offset|



### Type: [messages\_AffectedHistory](../types/messages_AffectedHistory.md)


### Example:

```php
$messages_affectedHistory = ['_' => 'messages.affectedHistory', 'pts' => int, 'pts_count' => int, 'offset' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.affectedHistory", "pts": int, "pts_count": int, "offset": int}
```


Or, if you're into Lua:

```lua
messages_affectedHistory={_='messages.affectedHistory', pts=int, pts_count=int, offset=int}

```


