# topPeerCategoryPeers

> Top peer category

[Back to constructors index](/API_docs/constructors/index.html)



Top peer category

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|category|[TopPeerCategory](/API_docs/types/TopPeerCategory.html) | Yes|Top peer category of peers|
|count|[int](/API_docs/types/int.html) | Yes|Count of peers|
|peers|Array of [TopPeer](/API_docs/types/TopPeer.html) | Yes|Peers|



### Type: [TopPeerCategoryPeers](/API_docs/types/TopPeerCategoryPeers.html)


### Example:

```
$topPeerCategoryPeers = ['_' => 'topPeerCategoryPeers', 'category' => TopPeerCategory, 'count' => int, 'peers' => [TopPeer, TopPeer]];
```
