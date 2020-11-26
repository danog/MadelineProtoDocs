---
title: updatePinnedMessages
description: updatePinnedMessages attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedMessages  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pinned|[Bool](../types/Bool.md) | Optional|
|peer|[Peer](../types/Peer.md) | Yes|
|messages|Array of [int](../types/int.md) | Yes|
|pts|[int](../types/int.md) | Yes|
|pts\_count|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePinnedMessages = ['_' => 'updatePinnedMessages', 'pinned' => Bool, 'peer' => Peer, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updatePinnedMessages={_='updatePinnedMessages', pinned=Bool, peer=Peer, messages={int}, pts=int, pts_count=int}

```


