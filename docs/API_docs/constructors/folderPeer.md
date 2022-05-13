---
title: "folderPeer"
description: "Peer in a folder"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: folderPeer  
[Back to constructors index](/API_docs/constructors/index.html)



Peer in a folder

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|Folder peer info|
|folder\_id|[int](/API_docs/types/int.html) | Yes|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|



### Type: [FolderPeer](/API_docs/types/FolderPeer.html)


### Example:

```
$folderPeer = ['_' => 'folderPeer', 'peer' => Peer, 'folder_id' => int];
```  
