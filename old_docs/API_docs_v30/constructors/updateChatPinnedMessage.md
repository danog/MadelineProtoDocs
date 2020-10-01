---
title: updateChatPinnedMessage
description: A message was pinned in a [legacy group](https://core.telegram.org/api/channel). This update is also typically emitted as an [updateNewChannelMessage](updateNewChannelMessage.md) with [messageService](messageService.md).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatPinnedMessage  
[Back to constructors index](index.md)



A message was pinned in a [legacy group](https://core.telegram.org/api/channel). This update is also typically emitted as an [updateNewChannelMessage](updateNewChannelMessage.md) with [messageService](messageService.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|[Legacy group](https://core.telegram.org/api/channel) ID|
|id|[int](../types/int.md) | Yes|ID of pinned message|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatPinnedMessage = ['_' => 'updateChatPinnedMessage', 'chat_id' => int, 'id' => int];
```  


Or, if you're into Lua:

```lua
updateChatPinnedMessage={_='updateChatPinnedMessage', chat_id=int, id=int}

```


