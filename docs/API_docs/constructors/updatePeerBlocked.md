---
title: "updatePeerBlocked"
description: "A peer was blocked"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerBlocked  
[Back to constructors index](index.md)



A peer was blocked

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer\_id|[Peer](../types/Peer.md) | Yes|The blocked peer|
|blocked|[Bool](../types/Bool.md) | Yes|Whether the peer was blocked or unblocked|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePeerBlocked = ['_' => 'updatePeerBlocked', 'peer_id' => Peer, 'blocked' => Bool];
```  


Or, if you're into Lua:

```lua
updatePeerBlocked={_='updatePeerBlocked', peer_id=Peer, blocked=Bool}

```


