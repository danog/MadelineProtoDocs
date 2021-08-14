---
title: peerBlocked
description: Information about a blocked peer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerBlocked  
[Back to constructors index](index.md)



Information about a blocked peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer\_id|[Peer](../types/Peer.md) | Yes|Peer ID|
|date|[int](../types/int.md) | Yes|When was the peer blocked|



### Type: [PeerBlocked](../types/PeerBlocked.md)


### Example:

```php
$peerBlocked = ['_' => 'peerBlocked', 'peer_id' => Peer, 'date' => int];
```  


Or, if you're into Lua:

```lua
peerBlocked={_='peerBlocked', peer_id=Peer, date=int}

```


