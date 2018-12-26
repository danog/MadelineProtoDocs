---
title: updateReadHistoryOutbox
description: Update read history outbox
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadHistoryOutbox  
[Back to constructors index](index.md)



Update read history outbox

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|max\_id|[int](../types/int.md) | Yes|Max ID|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadHistoryOutbox = ['_' => 'updateReadHistoryOutbox', 'peer' => Peer, 'max_id' => int, 'pts' => int, 'pts_count' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateReadHistoryOutbox", "peer": Peer, "max_id": int, "pts": int, "pts_count": int}
```


Or, if you're into Lua:

```lua
updateReadHistoryOutbox={_='updateReadHistoryOutbox', peer=Peer, max_id=int, pts=int, pts_count=int}

```


