---
title: "dialog"
description: "Chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialog  
[Back to constructors index](/API_docs/constructors/index.html)



Chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|Is the dialog pinned|
|unread\_mark|[Bool](/API_docs/types/Bool.html) | Optional|Whether the chat was manually marked as unread|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|The chat|
|top\_message|[int](/API_docs/types/int.html) | Yes|The latest message ID|
|read\_inbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all incoming messages are read.|
|read\_outbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all outgoing messages are read.|
|unread\_count|[int](/API_docs/types/int.html) | Yes|Number of unread messages|
|unread\_mentions\_count|[int](/API_docs/types/int.html) | Yes|Number of [unread mentions](https://core.telegram.org/api/mentions)|
|unread\_reactions\_count|[int](/API_docs/types/int.html) | Yes|Number of unread reactions to messages you sent|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.html) | Yes|Notification settings|
|pts|[int](/API_docs/types/int.html) | Optional|[PTS](https://core.telegram.org/api/updates)|
|draft|[DraftMessage](/API_docs/types/DraftMessage.html) | Optional|Message draft|
|folder\_id|[int](/API_docs/types/int.html) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|



### Type: [Dialog](/API_docs/types/Dialog.html)


### Example:

```
$dialog = ['_' => 'dialog', 'pinned' => Bool, 'unread_mark' => Bool, 'peer' => Peer, 'top_message' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'unread_mentions_count' => int, 'unread_reactions_count' => int, 'notify_settings' => PeerNotifySettings, 'pts' => int, 'draft' => DraftMessage, 'folder_id' => int];
```  
