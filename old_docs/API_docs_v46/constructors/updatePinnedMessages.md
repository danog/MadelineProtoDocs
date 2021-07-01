---
title: updatePinnedMessages
description: Some messages were pinned in a chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedMessages  
[Back to constructors index](index.md)



Some messages were pinned in a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](../types/Bool.md) | Optional|Whether the messages were pinned or unpinned|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|messages|Array of [int](../types/int.md) | Yes|Message IDs|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePinnedMessages = ['_' => 'updatePinnedMessages', 'pinned' => Bool, 'peer' => Peer, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updatePinnedMessages={_='updatePinnedMessages', pinned=Bool, peer=Peer, messages={int}, pts=int, pts_count=int}

```


