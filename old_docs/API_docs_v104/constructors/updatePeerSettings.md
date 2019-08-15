---
title: updatePeerSettings
description: Peer settings updated
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerSettings  
[Back to constructors index](index.md)



Peer settings updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|settings|[PeerSettings](../types/PeerSettings.md) | Yes|Settings|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePeerSettings = ['_' => 'updatePeerSettings', 'peer' => Peer, 'settings' => PeerSettings];
```  


Or, if you're into Lua:

```lua
updatePeerSettings={_='updatePeerSettings', peer=Peer, settings=PeerSettings}

```


