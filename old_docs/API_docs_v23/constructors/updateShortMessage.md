---
title: updateShortMessage
description: Update short message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortMessage  
[Back to constructors index](index.md)



Update short message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|from\_id|[int](../types/int.md) | Yes|From ID|
|message|[string](../types/string.md) | Yes|Message|
|pts|[int](../types/int.md) | Yes|Pts|
|date|[int](../types/int.md) | Yes|Date|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortMessage = ['_' => 'updateShortMessage', 'id' => int, 'from_id' => int, 'message' => 'string', 'pts' => int, 'date' => int, 'seq' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateShortMessage", "id": int, "from_id": int, "message": "string", "pts": int, "date": int, "seq": int}
```


Or, if you're into Lua:

```lua
updateShortMessage={_='updateShortMessage', id=int, from_id=int, message='string', pts=int, date=int, seq=int}

```


