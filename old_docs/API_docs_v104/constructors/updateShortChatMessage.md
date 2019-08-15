---
title: updateShortChatMessage
description: Update short chat message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShortChatMessage  
[Back to constructors index](index.md)



Update short chat message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](../types/Bool.md) | Optional|Out?|
|mentioned|[Bool](../types/Bool.md) | Optional|Mentioned?|
|media\_unread|[Bool](../types/Bool.md) | Optional|Media unread?|
|silent|[Bool](../types/Bool.md) | Optional|Silent?|
|id|[int](../types/int.md) | Yes|ID|
|from\_id|[int](../types/int.md) | Yes|From ID|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|message|[string](../types/string.md) | Yes|Message|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|
|date|[int](../types/int.md) | Yes|Date|
|fwd\_from|[MessageFwdHeader](../types/MessageFwdHeader.md) | Optional|Fwd from|
|via\_bot\_id|[int](../types/int.md) | Optional|Via bot ID|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|Reply to msg ID|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortChatMessage = ['_' => 'updateShortChatMessage', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'id' => int, 'from_id' => int, 'chat_id' => int, 'message' => 'string', 'pts' => int, 'pts_count' => int, 'date' => int, 'fwd_from' => MessageFwdHeader, 'via_bot_id' => int, 'reply_to_msg_id' => int, 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
updateShortChatMessage={_='updateShortChatMessage', out=Bool, mentioned=Bool, media_unread=Bool, silent=Bool, id=int, from_id=int, chat_id=int, message='string', pts=int, pts_count=int, date=int, fwd_from=MessageFwdHeader, via_bot_id=int, reply_to_msg_id=int, entities={MessageEntity}}

```


