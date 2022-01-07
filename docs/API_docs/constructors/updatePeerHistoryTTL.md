---
title: "updatePeerHistoryTTL"
description: "updatePeerHistoryTTL attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerHistoryTTL  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|
|ttl\_period|[int](/API_docs/types/int.md) | Optional|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updatePeerHistoryTTL = ['_' => 'updatePeerHistoryTTL', 'peer' => Peer, 'ttl_period' => int];
```  
