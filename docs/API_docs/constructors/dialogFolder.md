---
title: dialogFolder
description: Dialog folder
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFolder  
[Back to constructors index](index.md)



Dialog folder

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](../types/Bool.md) | Optional|Pinned?|
|folder|[Folder](../types/Folder.md) | Yes|Folder|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|top\_message|[int](../types/int.md) | Yes|Top message|
|unread\_muted\_peers\_count|[int](../types/int.md) | Yes|Unread muted peers count|
|unread\_unmuted\_peers\_count|[int](../types/int.md) | Yes|Unread unmuted peer count|
|unread\_muted\_messages\_count|[int](../types/int.md) | Yes|Unread muted messages count|
|unread\_unmuted\_messages\_count|[int](../types/int.md) | Yes|Unread unmuted messages count|



### Type: [Dialog](../types/Dialog.md)


### Example:

```php
$dialogFolder = ['_' => 'dialogFolder', 'pinned' => Bool, 'folder' => Folder, 'peer' => Peer, 'top_message' => int, 'unread_muted_peers_count' => int, 'unread_unmuted_peers_count' => int, 'unread_muted_messages_count' => int, 'unread_unmuted_messages_count' => int];
```  


Or, if you're into Lua:

```lua
dialogFolder={_='dialogFolder', pinned=Bool, folder=Folder, peer=Peer, top_message=int, unread_muted_peers_count=int, unread_unmuted_peers_count=int, unread_muted_messages_count=int, unread_unmuted_messages_count=int}

```


