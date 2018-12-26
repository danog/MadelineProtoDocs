---
title: geoChatMessage
description: Geo chat message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geoChatMessage  
[Back to constructors index](index.md)



Geo chat message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|id|[int](../types/int.md) | Yes|ID|
|from\_id|[int](../types/int.md) | Yes|From ID|
|date|[int](../types/int.md) | Yes|Date|
|message|[string](../types/string.md) | Yes|Message|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media|



### Type: [GeoChatMessage](../types/GeoChatMessage.md)


### Example:

```php
$geoChatMessage = ['_' => 'geoChatMessage', 'chat_id' => int, 'id' => int, 'from_id' => int, 'date' => int, 'message' => 'string', 'media' => MessageMedia];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "geoChatMessage", "chat_id": int, "id": int, "from_id": int, "date": int, "message": "string", "media": MessageMedia}
```


Or, if you're into Lua:

```lua
geoChatMessage={_='geoChatMessage', chat_id=int, id=int, from_id=int, date=int, message='string', media=MessageMedia}

```


