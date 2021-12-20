---
title: "dialogPeerFolder"
description: "Peer folder"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogPeerFolder  
[Back to constructors index](index.md)



[Peer folder](https://core.telegram.org/api/folders#peer-folders)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](../types/int.md) | Yes|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|



### Type: [DialogPeer](../types/DialogPeer.md)


### Example:

```php
$dialogPeerFolder = ['_' => 'dialogPeerFolder', 'folder_id' => int];
```  


Or, if you're into Lua:

```lua
dialogPeerFolder={_='dialogPeerFolder', folder_id=int}

```


