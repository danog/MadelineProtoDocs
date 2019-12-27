---
title: updateShortChatMessage
description: Shortened constructor containing info on one new incoming text message from a chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortChatMessage  
[Back to constructors index](index.md)



Shortened constructor containing info on one new incoming text message from a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID of the message|
|from\_id|[int](../types/int.md) | Yes|ID of the sender of the message|
|chat\_id|[int](../types/int.md) | Yes|ID of the chat where the message was sent|
|message|[string](../types/string.md) | Yes|Message|
|pts|[int](../types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](../types/int.md) | Yes|[date](https://core.telegram.org/api/updates)|
|fwd\_from\_id|[Peer](../types/Peer.md) | Optional|Fwd from ID|
|fwd\_date|[int](../types/int.md) | Optional|Fwd date|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|ID of the message this message replies to|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortChatMessage = ['_' => 'updateShortChatMessage', 'id' => int, 'from_id' => int, 'chat_id' => int, 'message' => 'string', 'pts' => int, 'pts_count' => int, 'date' => int, 'fwd_from_id' => Peer, 'fwd_date' => int, 'reply_to_msg_id' => int, 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
updateShortChatMessage={_='updateShortChatMessage', id=int, from_id=int, chat_id=int, message='string', pts=int, pts_count=int, date=int, fwd_from_id=Peer, fwd_date=int, reply_to_msg_id=int, entities={MessageEntity}}

```


