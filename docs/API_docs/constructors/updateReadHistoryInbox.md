---
title: "updateReadHistoryInbox"
description: "Incoming messages were read"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadHistoryInbox  
[Back to constructors index](index.md)



Incoming messages were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](../types/int.md) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|max\_id|[int](../types/int.md) | Yes|Maximum ID of messages read|
|still\_unread\_count|[int](../types/int.md) | Yes|Number of messages that are still unread|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadHistoryInbox = ['_' => 'updateReadHistoryInbox', 'folder_id' => int, 'peer' => Peer, 'max_id' => int, 'still_unread_count' => int, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateReadHistoryInbox={_='updateReadHistoryInbox', folder_id=int, peer=Peer, max_id=int, still_unread_count=int, pts=int, pts_count=int}

```


