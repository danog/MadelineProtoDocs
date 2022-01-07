---
title: "dialogFolder"
description: "Dialog in folder"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFolder  
[Back to constructors index](/API_docs/constructors/index.md)



Dialog in folder

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.md) | Optional|Is this folder pinned|
|folder|[Folder](/API_docs/types/Folder.md) | Yes|The folder|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|Peer in folder|
|top\_message|[int](/API_docs/types/int.md) | Yes|Latest message ID of dialog|
|unread\_muted\_peers\_count|[int](/API_docs/types/int.md) | Yes|Number of unread muted peers in folder|
|unread\_unmuted\_peers\_count|[int](/API_docs/types/int.md) | Yes|Number of unread unmuted peers in folder|
|unread\_muted\_messages\_count|[int](/API_docs/types/int.md) | Yes|Number of unread messages from muted peers in folder|
|unread\_unmuted\_messages\_count|[int](/API_docs/types/int.md) | Yes|Number of unread messages from unmuted peers in folder|



### Type: [Dialog](/API_docs/types/Dialog.md)


### Example:

```php
$dialogFolder = ['_' => 'dialogFolder', 'pinned' => Bool, 'folder' => Folder, 'peer' => Peer, 'top_message' => int, 'unread_muted_peers_count' => int, 'unread_unmuted_peers_count' => int, 'unread_muted_messages_count' => int, 'unread_unmuted_messages_count' => int];
```  
