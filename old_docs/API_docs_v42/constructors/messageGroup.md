---
title: messageGroup
description: Message group
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageGroup  
[Back to constructors index](index.md)



Message group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min\_id|[int](../types/int.md) | Yes|Min ID|
|max\_id|[int](../types/int.md) | Yes|Max ID|
|count|[int](../types/int.md) | Yes|Count|
|date|[int](../types/int.md) | Yes|Date|



### Type: [MessageGroup](../types/MessageGroup.md)


### Example:

```php
$messageGroup = ['_' => 'messageGroup', 'min_id' => int, 'max_id' => int, 'count' => int, 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageGroup", "min_id": int, "max_id": int, "count": int, "date": int}
```


Or, if you're into Lua:

```lua
messageGroup={_='messageGroup', min_id=int, max_id=int, count=int, date=int}

```


