---
title: "updateFolderPeers"
description: "The peer list of a peer folder was updated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateFolderPeers  
[Back to constructors index](index.md)



The peer list of a [peer folder](https://core.telegram.org/api/folders#peer-folders) was updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_peers|Array of [FolderPeer](../types/FolderPeer.md) | Yes|New peer list|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateFolderPeers = ['_' => 'updateFolderPeers', 'folder_peers' => [FolderPeer, FolderPeer], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateFolderPeers={_='updateFolderPeers', folder_peers={FolderPeer}, pts=int, pts_count=int}

```


