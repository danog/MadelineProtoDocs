---
title: "peerNotifySettings"
description: "Notification settings."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerNotifySettings  
[Back to constructors index](index.md)



Notification settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|show\_previews|[Bool](../types/Bool.md) | Optional|Display text in notifications|
|silent|[Bool](../types/Bool.md) | Optional|Mute peer?|
|mute\_until|[int](../types/int.md) | Optional|Mute all notifications until this date|
|sound|[string](../types/string.md) | Optional|Audio file name for notifications|



### Type: [PeerNotifySettings](../types/PeerNotifySettings.md)


### Example:

```php
$peerNotifySettings = ['_' => 'peerNotifySettings', 'show_previews' => Bool, 'silent' => Bool, 'mute_until' => int, 'sound' => 'string'];
```  


Or, if you're into Lua:

```lua
peerNotifySettings={_='peerNotifySettings', show_previews=Bool, silent=Bool, mute_until=int, sound='string'}

```


