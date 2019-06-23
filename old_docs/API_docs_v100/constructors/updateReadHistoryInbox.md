---
title: updateReadHistoryInbox
description: Update read history inbox
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadHistoryInbox  
[Back to constructors index](index.md)



Update read history inbox

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](../types/int.md) | Optional|Folder ID|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|max\_id|[int](../types/int.md) | Yes|Max ID|
|still\_unread\_count|[int](../types/int.md) | Yes|Still unread count|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadHistoryInbox = ['_' => 'updateReadHistoryInbox', 'folder_id' => int, 'peer' => Peer, 'max_id' => int, 'still_unread_count' => int, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateReadHistoryInbox={_='updateReadHistoryInbox', folder_id=int, peer=Peer, max_id=int, still_unread_count=int, pts=int, pts_count=int}

```


