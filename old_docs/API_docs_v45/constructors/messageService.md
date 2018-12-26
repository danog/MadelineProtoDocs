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
|unread|[Bool](../types/Bool.md) | Optional|Unread?|
|out|[Bool](../types/Bool.md) | Optional|Out?|
|mentioned|[Bool](../types/Bool.md) | Optional|Mentioned?|
|media\_unread|[Bool](../types/Bool.md) | Optional|Media unread?|
|id|[int](../types/int.md) | Yes|ID|
|from\_id|[int](../types/int.md) | Optional|From ID|
|to\_id|[Peer](../types/Peer.md) | Yes|To ID|
|date|[int](../types/int.md) | Yes|Date|
|action|[MessageAction](../types/MessageAction.md) | Optional|Action|



### Type: [Message](../types/Message.md)


### Example:

```php
$messageService = ['_' => 'messageService', 'unread' => Bool, 'out' => Bool, 'mentioned' => Bool, 'media_unread' => Bool, 'id' => int, 'from_id' => int, 'to_id' => Peer, 'date' => int, 'action' => MessageAction];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageService", "unread": Bool, "out": Bool, "mentioned": Bool, "media_unread": Bool, "id": int, "from_id": int, "to_id": Peer, "date": int, "action": MessageAction}
```


Or, if you're into Lua:

```lua
messageService={_='messageService', unread=Bool, out=Bool, mentioned=Bool, media_unread=Bool, id=int, from_id=int, to_id=Peer, date=int, action=MessageAction}

```


