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
|blocked|[Bool](/API_docs/types/Bool.html) | Optional|
|blocked\_my\_stories\_from|[Bool](/API_docs/types/Bool.html) | Optional|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|The blocked peer|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePeerBlocked = ['_' => 'updatePeerBlocked', 'blocked' => Bool, 'blocked_my_stories_from' => Bool, 'peer_id' => Peer];
```  
