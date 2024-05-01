---
title: "peerBlocked"
description: "Information about a blocked peer"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerBlocked  
[Back to constructors index](/API_docs/constructors/index.html)



Information about a blocked peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|Peer ID|
|date|[int](/API_docs/types/int.html) | Yes|When was the peer blocked|



### Type: [PeerBlocked](/API_docs/types/PeerBlocked.html)


### Example:

```
$peerBlocked = ['_' => 'peerBlocked', 'peer_id' => Peer, 'date' => int];
```  
