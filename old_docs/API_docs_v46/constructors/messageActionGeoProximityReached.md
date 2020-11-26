---
title: messageActionGeoProximityReached
description: messageActionGeoProximityReached attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGeoProximityReached  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|from\_id|[Peer](../types/Peer.md) | Yes|
|to\_id|[Peer](../types/Peer.md) | Yes|
|distance|[int](../types/int.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionGeoProximityReached = ['_' => 'messageActionGeoProximityReached', 'from_id' => Peer, 'to_id' => Peer, 'distance' => int];
```  


Or, if you're into Lua:

```lua
messageActionGeoProximityReached={_='messageActionGeoProximityReached', from_id=Peer, to_id=Peer, distance=int}

```


