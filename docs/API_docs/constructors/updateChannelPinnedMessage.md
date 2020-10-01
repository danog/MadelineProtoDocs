---
title: updateChannelPinnedMessage
description: A message was pinned in a [channel/supergroup](https://core.telegram.org/api/channel).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelPinnedMessage  
[Back to constructors index](index.md)



A message was pinned in a [channel/supergroup](https://core.telegram.org/api/channel).  
This update is also typically emitted as an [updateNewMessage](updateNewMessage.md) with [messageService](messageService.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel/supergroup ID|
|id|[int](../types/int.md) | Yes|ID of pinned message|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelPinnedMessage = ['_' => 'updateChannelPinnedMessage', 'channel_id' => int, 'id' => int];
```  


Or, if you're into Lua:

```lua
updateChannelPinnedMessage={_='updateChannelPinnedMessage', channel_id=int, id=int}

```


