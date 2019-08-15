---
title: updateFolderPeers
description: Folder update
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateFolderPeers  
[Back to constructors index](index.md)



Folder update

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_peers|Array of [FolderPeer](../types/FolderPeer.md) | Yes|New folder peers|
|pts|[int](../types/int.md) | Yes|PTS|
|pts\_count|[int](../types/int.md) | Yes|PTS|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateFolderPeers = ['_' => 'updateFolderPeers', 'folder_peers' => [FolderPeer, FolderPeer], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateFolderPeers={_='updateFolderPeers', folder_peers={FolderPeer}, pts=int, pts_count=int}

```


