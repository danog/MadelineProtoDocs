---
title: updatePinnedChannelMessages
description: updatePinnedChannelMessages attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedChannelMessages  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pinned|[Bool](../types/Bool.md) | Optional|
|channel\_id|[int](../types/int.md) | Yes|
|messages|Array of [int](../types/int.md) | Yes|
|pts|[int](../types/int.md) | Yes|
|pts\_count|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePinnedChannelMessages = ['_' => 'updatePinnedChannelMessages', 'pinned' => Bool, 'channel_id' => int, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updatePinnedChannelMessages={_='updatePinnedChannelMessages', pinned=Bool, channel_id=int, messages={int}, pts=int, pts_count=int}

```


