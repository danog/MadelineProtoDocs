---
title: "topPeerCategoryPeers"
description: "Top peer category"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: topPeerCategoryPeers  
[Back to constructors index](/API_docs/constructors/index.md)



Top peer category

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|category|[TopPeerCategory](/API_docs/types/TopPeerCategory.md) | Yes|Top peer category of peers|
|count|[int](/API_docs/types/int.md) | Yes|Count of peers|
|peers|Array of [TopPeer](/API_docs/types/TopPeer.md) | Yes|Peers|



### Type: [TopPeerCategoryPeers](/API_docs/types/TopPeerCategoryPeers.md)


### Example:

```php
$topPeerCategoryPeers = ['_' => 'topPeerCategoryPeers', 'category' => TopPeerCategory, 'count' => int, 'peers' => [TopPeer, TopPeer]];
```  
