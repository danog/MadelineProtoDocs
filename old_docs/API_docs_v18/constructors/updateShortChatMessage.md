---
title: updateShortChatMessage
description: updateShortChatMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortChatMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[int](../types/int.md) | Yes|
|from\_id|[int](../types/int.md) | Yes|
|chat\_id|[int](../types/int.md) | Yes|
|message|[string](../types/string.md) | Yes|
|pts|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|
|seq|[int](../types/int.md) | Yes|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortChatMessage = ['_' => 'updateShortChatMessage', 'id' => int, 'from_id' => int, 'chat_id' => int, 'message' => 'string', 'pts' => int, 'date' => int, 'seq' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateShortChatMessage", "id": int, "from_id": int, "chat_id": int, "message": "string", "pts": int, "date": int, "seq": int}
```


Or, if you're into Lua:

```lua
updateShortChatMessage={_='updateShortChatMessage', id=int, from_id=int, chat_id=int, message='string', pts=int, date=int, seq=int}

```


