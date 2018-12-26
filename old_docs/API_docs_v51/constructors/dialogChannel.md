---
title: dialogChannel
description: Dialog channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogChannel  
[Back to constructors index](index.md)



Dialog channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|top\_message|[int](../types/int.md) | Yes|Top message|
|top\_important\_message|[int](../types/int.md) | Yes|Top important message|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Read inbox max ID|
|unread\_count|[int](../types/int.md) | Yes|Unread count|
|unread\_important\_count|[int](../types/int.md) | Yes|Unread important count|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notify settings|
|pts|[int](../types/int.md) | Yes|Pts|



### Type: [Dialog](../types/Dialog.md)


### Example:

```php
$dialogChannel = ['_' => 'dialogChannel', 'peer' => Peer, 'top_message' => int, 'top_important_message' => int, 'read_inbox_max_id' => int, 'unread_count' => int, 'unread_important_count' => int, 'notify_settings' => PeerNotifySettings, 'pts' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "dialogChannel", "peer": Peer, "top_message": int, "top_important_message": int, "read_inbox_max_id": int, "unread_count": int, "unread_important_count": int, "notify_settings": PeerNotifySettings, "pts": int}
```


Or, if you're into Lua:

```lua
dialogChannel={_='dialogChannel', peer=Peer, top_message=int, top_important_message=int, read_inbox_max_id=int, unread_count=int, unread_important_count=int, notify_settings=PeerNotifySettings, pts=int}

```


