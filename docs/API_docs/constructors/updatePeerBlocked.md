---
title: "updatePeerBlocked"
description: "We blocked a peer, see here » for more info on blocklists."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerBlocked  
[Back to constructors index](/API_docs/constructors/index.html)



We blocked a peer, see [here »](https://core.telegram.org/api/block) for more info on blocklists.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|[Bool](/API_docs/types/Bool.html) | Optional|Whether the peer was blocked or unblocked|
|blocked\_my\_stories\_from|[Bool](/API_docs/types/Bool.html) | Optional|Whether the peer was added/removed to/from the story blocklist; if not set, this update affects the main blocklist, see [here »](https://core.telegram.org/api/block) for more info.|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|The (un)blocked peer|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePeerBlocked = ['_' => 'updatePeerBlocked', 'blocked' => Bool, 'blocked_my_stories_from' => Bool, 'peer_id' => Peer];
```  
