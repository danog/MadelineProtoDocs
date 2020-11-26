---
title: peerBlocked
description: peerBlocked attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerBlocked  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer\_id|[Peer](../types/Peer.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [PeerBlocked](../types/PeerBlocked.md)


### Example:

```php
$peerBlocked = ['_' => 'peerBlocked', 'peer_id' => Peer, 'date' => int];
```  


Or, if you're into Lua:

```lua
peerBlocked={_='peerBlocked', peer_id=Peer, date=int}

```


