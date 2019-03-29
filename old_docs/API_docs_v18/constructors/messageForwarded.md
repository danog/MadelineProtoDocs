---
title: messageForwarded
description: Message forwarded
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageForwarded  
[Back to constructors index](index.md)



Message forwarded

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|fwd\_from\_id|[int](../types/int.md) | Yes|Forwarded from ID|
|fwd\_date|[int](../types/int.md) | Yes|Forwarded date|
|from\_id|[int](../types/int.md) | Yes|From ID|
|to\_id|[Peer](../types/Peer.md) | Yes|To ID|
|date|[int](../types/int.md) | Yes|Date|
|message|[string](../types/string.md) | Yes|Message|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|Media|



### Type: [Message](../types/Message.md)


### Example:

```php
$messageForwarded = ['_' => 'messageForwarded', 'id' => int, 'fwd_from_id' => int, 'fwd_date' => int, 'from_id' => int, 'to_id' => Peer, 'date' => int, 'message' => 'string', 'media' => MessageMedia];
```  


Or, if you're into Lua:

```lua
messageForwarded={_='messageForwarded', id=int, fwd_from_id=int, fwd_date=int, from_id=int, to_id=Peer, date=int, message='string', media=MessageMedia}

```


