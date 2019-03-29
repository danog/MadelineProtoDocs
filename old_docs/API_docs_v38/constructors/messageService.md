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
|id|[int](../types/int.md) | Yes|ID|
|from\_id|[int](../types/int.md) | Optional|From ID|
|to\_id|[Peer](../types/Peer.md) | Yes|To ID|
|date|[int](../types/int.md) | Yes|Date|
|action|[MessageAction](../types/MessageAction.md) | Optional|Action|



### Type: [Message](../types/Message.md)


### Example:

```php
$messageService = ['_' => 'messageService', 'id' => int, 'from_id' => int, 'to_id' => Peer, 'date' => int, 'action' => MessageAction];
```  


Or, if you're into Lua:

```lua
messageService={_='messageService', id=int, from_id=int, to_id=Peer, date=int, action=MessageAction}

```


