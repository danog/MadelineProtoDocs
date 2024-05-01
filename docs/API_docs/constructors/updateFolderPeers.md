---
title: "updateFolderPeers"
description: "The peer list of a peer folder was updated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateFolderPeers  
[Back to constructors index](/API_docs/constructors/index.html)



The peer list of a [peer folder](https://core.telegram.org/api/folders#peer-folders) was updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_peers|Array of [FolderPeer](/API_docs/types/FolderPeer.html) | Yes|New peer list|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateFolderPeers = ['_' => 'updateFolderPeers', 'folder_peers' => [FolderPeer, FolderPeer], 'pts' => int, 'pts_count' => int];
```  
