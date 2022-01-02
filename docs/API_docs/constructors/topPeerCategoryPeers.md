---
title: "topPeerCategoryPeers"
description: "Top peer category"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: topPeerCategoryPeers  
[Back to constructors index](index.md)



Top peer category

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|category|[TopPeerCategory](../types/TopPeerCategory.md) | Yes|Top peer category of peers|
|count|[int](../types/int.md) | Yes|Count of peers|
|peers|Array of [TopPeer](../types/TopPeer.md) | Yes|Peers|



### Type: [TopPeerCategoryPeers](../types/TopPeerCategoryPeers.md)


### Example:

```php
$topPeerCategoryPeers = ['_' => 'topPeerCategoryPeers', 'category' => TopPeerCategory, 'count' => int, 'peers' => [TopPeer, TopPeer]];
```  


Or, if you're into Lua:

```lua
topPeerCategoryPeers={_='topPeerCategoryPeers', category=TopPeerCategory, count=int, peers={TopPeer}}

```


