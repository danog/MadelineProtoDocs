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
|view\_forum\_as\_messages|[Bool](/API_docs/types/Bool.html) | Optional|Users may also choose to display messages from all topics of a [forum](https://core.telegram.org/api/forum) as if they were sent to a normal group, using a "View as messages" setting in the local client.  <br>This setting only affects the current account, and is synced to other logged in sessions using the [channels.toggleViewForumAsMessages](../methods/channels.toggleViewForumAsMessages.html) method; invoking this method will update the value of this flag.|
|peer|[long](/API_docs/types/long.html) | Yes|The chat|
|top\_message|[int](/API_docs/types/int.html) | Yes|The latest message ID|
|read\_inbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all incoming messages are read.|
|read\_outbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all outgoing messages are read.|
|unread\_count|[int](/API_docs/types/int.html) | Yes|Number of unread messages|
|unread\_mentions\_count|[int](/API_docs/types/int.html) | Yes|Number of [unread mentions](https://core.telegram.org/api/mentions)|
|unread\_reactions\_count|[int](/API_docs/types/int.html) | Yes|Number of unread reactions to messages you sent|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.html) | Yes|Notification settings|
|pts|[int](/API_docs/types/int.html) | Optional|[PTS](https://core.telegram.org/api/updates)|
|draft|[DraftMessage](/API_docs/types/DraftMessage.html) | Optional|Message [draft](https://core.telegram.org/api/drafts)|
|folder\_id|[int](/API_docs/types/int.html) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|ttl\_period|[int](/API_docs/types/int.html) | Optional|Time-to-live of all messages sent in this dialog|



### Type: [Dialog](/API_docs/types/Dialog.html)


### Example:

```
$dialog = ['_' => 'dialog', 'pinned' => Bool, 'unread_mark' => Bool, 'view_forum_as_messages' => Bool, 'peer' => long, 'top_message' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'unread_mentions_count' => int, 'unread_reactions_count' => int, 'notify_settings' => PeerNotifySettings, 'pts' => int, 'draft' => DraftMessage, 'folder_id' => int, 'ttl_period' => int];
```  
