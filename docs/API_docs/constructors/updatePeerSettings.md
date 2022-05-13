---
title: "updatePeerSettings"
description: "Settings of a certain peer have changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Settings of a certain peer have changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|The peer|
|settings|[PeerSettings](/API_docs/types/PeerSettings.html) | Yes|Associated peer settings|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePeerSettings = ['_' => 'updatePeerSettings', 'peer' => Peer, 'settings' => PeerSettings];
```  
