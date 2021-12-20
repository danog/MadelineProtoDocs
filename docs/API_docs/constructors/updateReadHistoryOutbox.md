---
title: "updateReadHistoryOutbox"
description: "Outgoing messages were read"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadHistoryOutbox  
[Back to constructors index](index.md)



Outgoing messages were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|max\_id|[int](../types/int.md) | Yes|Maximum ID of read outgoing messages|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadHistoryOutbox = ['_' => 'updateReadHistoryOutbox', 'peer' => Peer, 'max_id' => int, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateReadHistoryOutbox={_='updateReadHistoryOutbox', peer=Peer, max_id=int, pts=int, pts_count=int}

```


