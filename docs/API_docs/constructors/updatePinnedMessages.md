---
title: "updatePinnedMessages"
description: "Some messages were pinned in a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedMessages  
[Back to constructors index](/API_docs/constructors/index.md)



Some messages were pinned in a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.md) | Optional|Whether the messages were pinned or unpinned|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|Peer|
|messages|Array of [int](/API_docs/types/int.md) | Yes|Message IDs|
|pts|[int](/API_docs/types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updatePinnedMessages = ['_' => 'updatePinnedMessages', 'pinned' => Bool, 'peer' => Peer, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  
