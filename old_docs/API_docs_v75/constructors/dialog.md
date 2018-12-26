---
title: dialog
description: Dialog
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialog  
[Back to constructors index](index.md)



Dialog

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](../types/Bool.md) | Optional|Pinned?|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|top\_message|[int](../types/int.md) | Yes|Top message|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Read inbox max ID|
|read\_outbox\_max\_id|[int](../types/int.md) | Yes|Read outbox max ID|
|unread\_count|[int](../types/int.md) | Yes|Unread count|
|unread\_mentions\_count|[int](../types/int.md) | Yes|Unread mentions count|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notify settings|
|pts|[int](../types/int.md) | Optional|Pts|
|draft|[DraftMessage](../types/DraftMessage.md) | Optional|Draft|



### Type: [Dialog](../types/Dialog.md)


### Example:

```php
$dialog = ['_' => 'dialog', 'pinned' => Bool, 'peer' => Peer, 'top_message' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'unread_mentions_count' => int, 'notify_settings' => PeerNotifySettings, 'pts' => int, 'draft' => DraftMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "dialog", "pinned": Bool, "peer": Peer, "top_message": int, "read_inbox_max_id": int, "read_outbox_max_id": int, "unread_count": int, "unread_mentions_count": int, "notify_settings": PeerNotifySettings, "pts": int, "draft": DraftMessage}
```


Or, if you're into Lua:

```lua
dialog={_='dialog', pinned=Bool, peer=Peer, top_message=int, read_inbox_max_id=int, read_outbox_max_id=int, unread_count=int, unread_mentions_count=int, notify_settings=PeerNotifySettings, pts=int, draft=DraftMessage}

```


