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
|id|[int](../types/int.md) | Yes|ID|
|from\_id|[int](../types/int.md) | Yes|From ID|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|message|[string](../types/string.md) | Yes|Message|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|
|date|[int](../types/int.md) | Yes|Date|
|fwd\_from\_id|[int](../types/int.md) | Optional|Fwd from ID|
|fwd\_date|[int](../types/int.md) | Optional|Fwd date|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|Reply to msg ID|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updateShortChatMessage = ['_' => 'updateShortChatMessage', 'id' => int, 'from_id' => int, 'chat_id' => int, 'message' => 'string', 'pts' => int, 'pts_count' => int, 'date' => int, 'fwd_from_id' => int, 'fwd_date' => int, 'reply_to_msg_id' => int, 'entities' => [MessageEntity, MessageEntity]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateShortChatMessage", "id": int, "from_id": int, "chat_id": int, "message": "string", "pts": int, "pts_count": int, "date": int, "fwd_from_id": int, "fwd_date": int, "reply_to_msg_id": int, "entities": [MessageEntity]}
```


Or, if you're into Lua:

```lua
updateShortChatMessage={_='updateShortChatMessage', id=int, from_id=int, chat_id=int, message='string', pts=int, pts_count=int, date=int, fwd_from_id=int, fwd_date=int, reply_to_msg_id=int, entities={MessageEntity}}

```


