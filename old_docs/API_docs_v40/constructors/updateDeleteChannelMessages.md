---
title: updateDeleteChannelMessages
description: Some messages in a [supergroup/channel](https://core.telegram.org/api/channel) were deleted
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteChannelMessages  
[Back to constructors index](index.md)



Some messages in a [supergroup/channel](https://core.telegram.org/api/channel) were deleted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|messages|Array of [int](../types/int.md) | Yes|Messages|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDeleteChannelMessages = ['_' => 'updateDeleteChannelMessages', 'peer' => Peer, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateDeleteChannelMessages={_='updateDeleteChannelMessages', peer=Peer, messages={int}, pts=int, pts_count=int}

```


