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
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|top\_message|[int](../types/int.md) | Yes|Top message|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Read inbox max ID|
|unread\_count|[int](../types/int.md) | Yes|Unread count|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notify settings|



### Type: [Dialog](../types/Dialog.md)


### Example:

```php
$dialog = ['_' => 'dialog', 'peer' => Peer, 'top_message' => int, 'read_inbox_max_id' => int, 'unread_count' => int, 'notify_settings' => PeerNotifySettings];
```  


Or, if you're into Lua:

```lua
dialog={_='dialog', peer=Peer, top_message=int, read_inbox_max_id=int, unread_count=int, notify_settings=PeerNotifySettings}

```


