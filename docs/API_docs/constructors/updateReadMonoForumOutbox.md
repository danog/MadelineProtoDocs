---
title: "updateReadMonoForumOutbox"
description: "Outgoing messages in a monoforum were read."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadMonoForumOutbox  
[Back to constructors index](/API_docs/constructors/index.html)



Outgoing messages in a [monoforum](https://core.telegram.org/api/monoforum) were read.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|ID of the monoforum.|
|saved\_peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|Topic ID.|
|read\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all outgoing messages are read.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateReadMonoForumOutbox = ['_' => 'updateReadMonoForumOutbox', 'channel_id' => long, 'saved_peer_id' => Peer, 'read_max_id' => int];
```  
