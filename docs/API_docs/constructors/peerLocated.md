---
title: "peerLocated"
description: "Peer geolocated nearby"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerLocated  
[Back to constructors index](index.md)



Peer geolocated nearby

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|expires|[int](../types/int.md) | Yes|Validity period of current data|
|distance|[int](../types/int.md) | Yes|Distance from the peer in meters|



### Type: [PeerLocated](../types/PeerLocated.md)


### Example:

```php
$peerLocated = ['_' => 'peerLocated', 'peer' => Peer, 'expires' => int, 'distance' => int];
```  


Or, if you're into Lua:

```lua
peerLocated={_='peerLocated', peer=Peer, expires=int, distance=int}

```


