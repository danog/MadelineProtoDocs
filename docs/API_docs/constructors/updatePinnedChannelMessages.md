---
title: "updatePinnedChannelMessages"
description: "Messages were pinned/unpinned in a channel/supergroup"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedChannelMessages  
[Back to constructors index](index.md)



Messages were pinned/unpinned in a [channel/supergroup](https://core.telegram.org/api/channel)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](../types/Bool.md) | Optional|Whether the messages were pinned or unpinned|
|channel\_id|[long](../types/long.md) | Yes|
|messages|Array of [int](../types/int.md) | Yes|Messages|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePinnedChannelMessages = ['_' => 'updatePinnedChannelMessages', 'pinned' => Bool, 'channel_id' => long, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updatePinnedChannelMessages={_='updatePinnedChannelMessages', pinned=Bool, channel_id=long, messages={int}, pts=int, pts_count=int}

```


