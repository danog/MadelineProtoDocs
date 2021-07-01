---
title: message
description: A message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: message  
[Back to constructors index](index.md)



A message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID of the message|
|from\_id|[int](../types/int.md) | Yes|
|to\_id|[Peer](../types/Peer.md) | Yes|
|date|[int](../types/int.md) | Yes|Date of the message|
|message|[string](../types/string.md) | Yes|The message|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media attachment|



### Type: [Message](../types/Message.md)


### Example:

```php
$message = ['_' => 'message', 'id' => int, 'from_id' => int, 'to_id' => Peer, 'date' => int, 'message' => 'string', 'media' => MessageMedia];
```  


Or, if you're into Lua:

```lua
message={_='message', id=int, from_id=int, to_id=Peer, date=int, message='string', media=MessageMedia}

```


