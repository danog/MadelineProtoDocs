---
title: "updatePeerBlocked"
description: "A peer was blocked"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerBlocked  
[Back to constructors index](/API_docs/constructors/index.html)



A peer was blocked

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|The blocked peer|
|blocked|[Bool](/API_docs/types/Bool.html) | Yes|Whether the peer was blocked or unblocked|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePeerBlocked = ['_' => 'updatePeerBlocked', 'peer_id' => Peer, 'blocked' => Bool];
```  
