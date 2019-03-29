---
title: peerNotifySettings
description: Peer notify settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerNotifySettings  
[Back to constructors index](index.md)



Peer notify settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|show\_previews|[Bool](../types/Bool.md) | Optional|Show previews?|
|silent|[Bool](../types/Bool.md) | Optional|Silent?|
|mute\_until|[int](../types/int.md) | Yes|Mute until|
|sound|[string](../types/string.md) | Yes|Sound|



### Type: [PeerNotifySettings](../types/PeerNotifySettings.md)


### Example:

```php
$peerNotifySettings = ['_' => 'peerNotifySettings', 'show_previews' => Bool, 'silent' => Bool, 'mute_until' => int, 'sound' => 'string'];
```  


Or, if you're into Lua:

```lua
peerNotifySettings={_='peerNotifySettings', show_previews=Bool, silent=Bool, mute_until=int, sound='string'}

```


