---
title: "updateShortChatMessage"
description: "Shortened constructor containing info on one new incoming text message from a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortChatMessage  
[Back to constructors index](index.md)



Shortened constructor containing info on one new incoming text message from a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](../types/Bool.md) | Optional|Whether the message is outgoing|
|mentioned|[Bool](../types/Bool.md) | Optional|Whether we were mentioned in this message|
|media\_unread|[Bool](../types/Bool.md) | Optional|Whether the message contains some **unread** mentions|
|silent|[Bool](../types/Bool.md) | Optional|If true, the message is a silent message, no notifications should be triggered|
|id|[int](../types/int.md) | Yes|ID of the message|
|from\_id|[long](../types/long.md) | Yes|
|chat\_id|[long](../types/long.md) | Yes|
|message|[string](../types/string.md) | Yes|Message|
|pts|[int](../types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](../types/int.md) | Yes|[date](https://core.telegram.org/api/updates)|
|fwd\_from|[MessageFwdHeader](../types/MessageFwdHeader.md) | Optional|Info about a forwarded message|
|via\_bot\_id|[long](../types/long.md) | Optional|
|reply\_to|[MessageReplyHeader](../types/MessageReplyHeader.md) | Optional|Reply (thread) information|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|[Entities](https://core.telegram.org/api/entities) for styled text|
|ttl\_period|[int](../types/int.md) | Optional|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortChatMessage = ['_' => 'updateShortChatMessage', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'id' => int, 'from_id' => long, 'chat_id' => long, 'message' => 'string', 'pts' => int, 'pts_count' => int, 'date' => int, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => long, 'reply_to' => MessageReplyHeader, 'entities' => [MessageEntity, MessageEntity], 'ttl_period' => int];
```  
