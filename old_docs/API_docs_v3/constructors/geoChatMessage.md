---
title: geoChatMessage
description: geoChatMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geoChatMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|
|id|[int](../types/int.md) | Yes|
|from\_id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|
|message|[string](../types/string.md) | Yes|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|



### Type: [GeoChatMessage](../types/GeoChatMessage.md)


### Example:

```php
$geoChatMessage = ['_' => 'geoChatMessage', 'chat_id' => int, 'id' => int, 'from_id' => int, 'date' => int, 'message' => 'string', 'media' => MessageMedia];
```  


Or, if you're into Lua:

```lua
geoChatMessage={_='geoChatMessage', chat_id=int, id=int, from_id=int, date=int, message='string', media=MessageMedia}

```


