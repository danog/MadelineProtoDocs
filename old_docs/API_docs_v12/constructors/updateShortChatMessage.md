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
|unread|[Bool](../types/Bool.md) | Optional|
|out|[Bool](../types/Bool.md) | Optional|Whether the message is outgoing|
|mentioned|[Bool](../types/Bool.md) | Optional|Whether we were mentioned in this message|
|media\_unread|[Bool](../types/Bool.md) | Optional|Whether the message contains some **unread** mentions|
|silent|[Bool](../types/Bool.md) | Optional|If true, the message is a silent message, no notifications should be triggered|
|id|[int](../types/int.md) | Yes|ID of the message|
|from\_id|[int](../types/int.md) | Yes|ID of the sender of the message|
|chat\_id|[int](../types/int.md) | Yes|ID of the chat where the message was sent|
|message|[string](../types/string.md) | Yes|Message|
|pts|[int](../types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[PTS count](https://core.telegram.org/api/updates)|
|date|[int](../types/int.md) | Yes|[date](https://core.telegram.org/api/updates)|
|fwd\_from|[MessageFwdHeader](../types/MessageFwdHeader.md) | Optional|Info about a forwarded message|
|via\_bot\_id|[int](../types/int.md) | Optional|Info about the inline bot used to generate this message|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|[Entities](https://core.telegram.org/api/entities) for styled text|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortChatMessage = ['_' => 'updateShortChatMessage', 'unread' => Bool, 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'id' => int, 'from_id' => int, 'chat_id' => int, 'message' => 'string', 'pts' => int, 'pts_count' => int, 'date' => int, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => int, 'reply_to_msg_id' => int, 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
updateShortChatMessage={_='updateShortChatMessage', unread=Bool, out=Bool, mentioned=Bool, media_unread=Bool, silent=Bool, id=int, from_id=int, chat_id=int, message='string', pts=int, pts_count=int, date=int, fwd_from=MessageFwdHeader, via_bot_id=int, reply_to_msg_id=int, entities={MessageEntity}}

```


