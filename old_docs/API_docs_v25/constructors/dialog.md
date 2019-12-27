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
|peer|[Peer](../types/Peer.md) | Yes|The chat|
|top\_message|[int](../types/int.md) | Yes|The latest message ID|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Position up to which all incoming messages are read.|
|unread\_count|[int](../types/int.md) | Yes|Number of unread messages|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notification settings|



### Type: [Dialog](../types/Dialog.md)


### Example:

```php
$dialog = ['_' => 'dialog', 'peer' => Peer, 'top_message' => int, 'read_inbox_max_id' => int, 'unread_count' => int, 'notify_settings' => PeerNotifySettings];
```  


Or, if you're into Lua:

```lua
dialog={_='dialog', peer=Peer, top_message=int, read_inbox_max_id=int, unread_count=int, notify_settings=PeerNotifySettings}

```


