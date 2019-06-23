---
title: messageService
description: Message service
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageService  
[Back to constructors index](index.md)



Message service

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](../types/Bool.md) | Optional|Out?|
|mentioned|[Bool](../types/Bool.md) | Optional|Mentioned?|
|media\_unread|[Bool](../types/Bool.md) | Optional|Media unread?|
|silent|[Bool](../types/Bool.md) | Optional|Silent?|
|post|[Bool](../types/Bool.md) | Optional|Post?|
|legacy|[Bool](../types/Bool.md) | Optional|Legacy message|
|id|[int](../types/int.md) | Yes|ID|
|from\_id|[int](../types/int.md) | Optional|From ID|
|to\_id|[Peer](../types/Peer.md) | Yes|To ID|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|Reply to msg ID|
|date|[int](../types/int.md) | Yes|Date|
|action|[MessageAction](../types/MessageAction.md) | Optional|Action|



### Type: [Message](../types/Message.md)


### Example:

```php
$messageService = ['_' => 'messageService', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'post' => Bool, 'legacy' => Bool, 'id' => int, 'from_id' => int, 'to_id' => Peer, 'reply_to_msg_id' => int, 'date' => int, 'action' => MessageAction];
```  


Or, if you're into Lua:

```lua
messageService={_='messageService', out=Bool, mentioned=Bool, media_unread=Bool, silent=Bool, post=Bool, legacy=Bool, id=int, from_id=int, to_id=Peer, reply_to_msg_id=int, date=int, action=MessageAction}

```


