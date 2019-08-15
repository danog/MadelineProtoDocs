---
title: peerLocated
description: Located peer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerLocated  
[Back to constructors index](index.md)



Located peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|expires|[int](../types/int.md) | Yes|Expiry date|
|distance|[int](../types/int.md) | Yes|Distance|



### Type: [PeerLocated](../types/PeerLocated.md)


### Example:

```php
$peerLocated = ['_' => 'peerLocated', 'peer' => Peer, 'expires' => int, 'distance' => int];
```  


Or, if you're into Lua:

```lua
peerLocated={_='peerLocated', peer=Peer, expires=int, distance=int}

```


