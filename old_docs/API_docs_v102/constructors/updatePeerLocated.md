---
title: updatePeerLocated
description: Peer location updated
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerLocated  
[Back to constructors index](index.md)



Peer location updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peers|Array of [PeerLocated](../types/PeerLocated.md) | Yes|Peers|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePeerLocated = ['_' => 'updatePeerLocated', 'peers' => [PeerLocated, PeerLocated]];
```  


Or, if you're into Lua:

```lua
updatePeerLocated={_='updatePeerLocated', peers={PeerLocated}}

```


