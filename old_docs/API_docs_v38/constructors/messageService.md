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
|id|[int](../types/int.md) | Yes|Message ID|
|from\_id|[int](../types/int.md) | Optional|Id of te sender of the message|
|to\_id|[Peer](../types/Peer.md) | Yes|ID of the destination of the message|
|date|[int](../types/int.md) | Yes|Message date|
|action|[MessageAction](../types/MessageAction.md) | Optional|Event connected with the service message|



### Type: [Message](../types/Message.md)


### Example:

```php
$messageService = ['_' => 'messageService', 'id' => int, 'from_id' => int, 'to_id' => Peer, 'date' => int, 'action' => MessageAction];
```  


Or, if you're into Lua:

```lua
messageService={_='messageService', id=int, from_id=int, to_id=Peer, date=int, action=MessageAction}

```


