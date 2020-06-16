---
title: dialog
description: Chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialog  
[Back to constructors index](index.md)



Chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](../types/Bool.md) | Optional|Is the dialog pinned|
|peer|[Peer](../types/Peer.md) | Yes|The chat|
|top\_message|[int](../types/int.md) | Yes|The latest message ID|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Position up to which all incoming messages are read.|
|read\_outbox\_max\_id|[int](../types/int.md) | Yes|Position up to which all outgoing messages are read.|
|unread\_count|[int](../types/int.md) | Yes|Number of unread messages|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notification settings|
|pts|[int](../types/int.md) | Optional|[PTS](https://core.telegram.org/api/updates)|
|draft|[DraftMessage](../types/DraftMessage.md) | Optional|Message draft|



### Type: [Dialog](../types/Dialog.md)


### Example:

```php
$dialog = ['_' => 'dialog', 'pinned' => Bool, 'peer' => Peer, 'top_message' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'notify_settings' => PeerNotifySettings, 'pts' => int, 'draft' => DraftMessage];
```  


Or, if you're into Lua:

```lua
dialog={_='dialog', pinned=Bool, peer=Peer, top_message=int, read_inbox_max_id=int, read_outbox_max_id=int, unread_count=int, notify_settings=PeerNotifySettings, pts=int, draft=DraftMessage}

```


