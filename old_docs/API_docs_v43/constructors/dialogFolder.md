---
title: dialogFolder
description: Dialog in folder
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFolder  
[Back to constructors index](index.md)



Dialog in folder

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](../types/Bool.md) | Optional|Is this folder pinned|
|folder|[Folder](../types/Folder.md) | Yes|The folder|
|peer|[Peer](../types/Peer.md) | Yes|Peer in folder|
|top\_message|[int](../types/int.md) | Yes|Latest message ID of dialog|
|unread\_muted\_peers\_count|[int](../types/int.md) | Yes|Number of unread muted peers in folder|
|unread\_unmuted\_peers\_count|[int](../types/int.md) | Yes|Number of unread unmuted peers in folder|
|unread\_muted\_messages\_count|[int](../types/int.md) | Yes|Number of unread messages from muted peers in folder|
|unread\_unmuted\_messages\_count|[int](../types/int.md) | Yes|Number of unread messages from unmuted peers in folder|



### Type: [Dialog](../types/Dialog.md)


### Example:

```php
$dialogFolder = ['_' => 'dialogFolder', 'pinned' => Bool, 'folder' => Folder, 'peer' => Peer, 'top_message' => int, 'unread_muted_peers_count' => int, 'unread_unmuted_peers_count' => int, 'unread_muted_messages_count' => int, 'unread_unmuted_messages_count' => int];
```  


Or, if you're into Lua:

```lua
dialogFolder={_='dialogFolder', pinned=Bool, folder=Folder, peer=Peer, top_message=int, unread_muted_peers_count=int, unread_unmuted_peers_count=int, unread_muted_messages_count=int, unread_unmuted_messages_count=int}

```


