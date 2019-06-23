---
title: folderPeer
description: Peer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: folderPeer  
[Back to constructors index](index.md)



Peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|folder\_id|[int](../types/int.md) | Yes|Folder ID|



### Type: [FolderPeer](../types/FolderPeer.md)


### Example:

```php
$folderPeer = ['_' => 'folderPeer', 'peer' => Peer, 'folder_id' => int];
```  


Or, if you're into Lua:

```lua
folderPeer={_='folderPeer', peer=Peer, folder_id=int}

```


