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
|mute\_until|[int](../types/int.md) | Yes|Mute until|
|sound|[string](../types/string.md) | Yes|Sound|
|show\_previews|[Bool](../types/Bool.md) | Yes|Show previews?|
|events\_mask|[int](../types/int.md) | Yes|Events mask|



### Type: [PeerNotifySettings](../types/PeerNotifySettings.md)


### Example:

```php
$peerNotifySettings = ['_' => 'peerNotifySettings', 'mute_until' => int, 'sound' => 'string', 'show_previews' => Bool, 'events_mask' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "peerNotifySettings", "mute_until": int, "sound": "string", "show_previews": Bool, "events_mask": int}
```


Or, if you're into Lua:

```lua
peerNotifySettings={_='peerNotifySettings', mute_until=int, sound='string', show_previews=Bool, events_mask=int}

```


