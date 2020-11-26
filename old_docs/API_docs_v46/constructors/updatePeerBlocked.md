---
title: updatePeerBlocked
description: updatePeerBlocked attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerBlocked  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer\_id|[Peer](../types/Peer.md) | Yes|
|blocked|[Bool](../types/Bool.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePeerBlocked = ['_' => 'updatePeerBlocked', 'peer_id' => Peer, 'blocked' => Bool];
```  


Or, if you're into Lua:

```lua
updatePeerBlocked={_='updatePeerBlocked', peer_id=Peer, blocked=Bool}

```


