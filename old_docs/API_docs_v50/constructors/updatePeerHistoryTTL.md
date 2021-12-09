---
title: updatePeerHistoryTTL
description: updatePeerHistoryTTL attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerHistoryTTL  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](../types/Peer.md) | Yes|
|ttl\_period|[int](../types/int.md) | Optional|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePeerHistoryTTL = ['_' => 'updatePeerHistoryTTL', 'peer' => Peer, 'ttl_period' => int];
```  


Or, if you're into Lua:

```lua
updatePeerHistoryTTL={_='updatePeerHistoryTTL', peer=Peer, ttl_period=int}

```


