---
title: messageService
description: Indicates a service message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageService  
[Back to constructors index](index.md)



Indicates a service message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|out|[Bool](../types/Bool.md) | Optional|Whether the message is outgoing|
|mentioned|[Bool](../types/Bool.md) | Optional|Whether we were mentioned in the message|
|media\_unread|[Bool](../types/Bool.md) | Optional|Whether the message contains unread media|
|silent|[Bool](../types/Bool.md) | Optional|Whether the message is silent|
|post|[Bool](../types/Bool.md) | Optional|Whether it's a channel post|
|legacy|[Bool](../types/Bool.md) | Optional|This is a legacy message: it has to be refetched with the new layer|
|id|[int](../types/int.md) | Yes|Message ID|
|from\_id|[int](../types/int.md) | Optional|
|to\_id|[Peer](../types/Peer.md) | Yes|
|reply\_to\_msg\_id|[int](../types/int.md) | Optional|
|date|[int](../types/int.md) | Yes|Message date|
|action|[MessageAction](../types/MessageAction.md) | Optional|Event connected with the service message|



### Type: [Message](../types/Message.md)


### Example:

```php
$messageService = ['_' => 'messageService', 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'silent' => Bool, 'post' => Bool, 'legacy' => Bool, 'id' => int, 'from_id' => int, 'to_id' => Peer, 'reply_to_msg_id' => int, 'date' => int, 'action' => MessageAction];
```  


Or, if you're into Lua:

```lua
messageService={_='messageService', out=Bool, mentioned=Bool, media_unread=Bool, silent=Bool, post=Bool, legacy=Bool, id=int, from_id=int, to_id=Peer, reply_to_msg_id=int, date=int, action=MessageAction}

```


