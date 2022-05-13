---
title: "updateReadHistoryOutbox"
description: "Outgoing messages were read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadHistoryOutbox  
[Back to constructors index](/API_docs/constructors/index.html)



Outgoing messages were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|Peer|
|max\_id|[int](/API_docs/types/int.html) | Yes|Maximum ID of read outgoing messages|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateReadHistoryOutbox = ['_' => 'updateReadHistoryOutbox', 'peer' => Peer, 'max_id' => int, 'pts' => int, 'pts_count' => int];
```  
