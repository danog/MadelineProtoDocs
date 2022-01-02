---
title: "updatePeerSettings"
description: "Settings of a certain peer have changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerSettings  
[Back to constructors index](index.md)



Settings of a certain peer have changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|The peer|
|settings|[PeerSettings](../types/PeerSettings.md) | Yes|Associated peer settings|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePeerSettings = ['_' => 'updatePeerSettings', 'peer' => Peer, 'settings' => PeerSettings];
```  


Or, if you're into Lua:

```lua
updatePeerSettings={_='updatePeerSettings', peer=Peer, settings=PeerSettings}

```


