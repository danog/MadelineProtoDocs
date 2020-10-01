---
title: updateChatPinnedMessage
description: A message was pinned in a [legacy group](https://core.telegram.org/api/channel)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatPinnedMessage  
[Back to constructors index](index.md)



A message was pinned in a [legacy group](https://core.telegram.org/api/channel)  
This update is also typically emitted as an [updateNewMessage](updateNewMessage.md) with [messageService](messageService.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|[Legacy group](https://core.telegram.org/api/channel) ID|
|id|[int](../types/int.md) | Yes|ID of pinned message|
|version|[int](../types/int.md) | Yes|Used to reorder updates in legacy groups|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatPinnedMessage = ['_' => 'updateChatPinnedMessage', 'chat_id' => int, 'id' => int, 'version' => int];
```  


Or, if you're into Lua:

```lua
updateChatPinnedMessage={_='updateChatPinnedMessage', chat_id=int, id=int, version=int}

```


