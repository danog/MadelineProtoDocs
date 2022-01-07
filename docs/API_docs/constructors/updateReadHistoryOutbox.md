---
title: "updateReadHistoryOutbox"
description: "Outgoing messages were read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadHistoryOutbox  
[Back to constructors index](/API_docs/constructors/index.md)



Outgoing messages were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|Peer|
|max\_id|[int](/API_docs/types/int.md) | Yes|Maximum ID of read outgoing messages|
|pts|[int](/API_docs/types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateReadHistoryOutbox = ['_' => 'updateReadHistoryOutbox', 'peer' => Peer, 'max_id' => int, 'pts' => int, 'pts_count' => int];
```  
