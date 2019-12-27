---
title: peerNotifySettings
description: Notification settings.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerNotifySettings  
[Back to constructors index](index.md)



Notification settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|mute\_until|[int](../types/int.md) | Yes|Mute all notifications until this date|
|sound|[string](../types/string.md) | Yes|Audio file name for notifications|
|show\_previews|[Bool](../types/Bool.md) | Yes|Display text in notifications|
|events\_mask|[int](../types/int.md) | Yes|Events mask|



### Type: [PeerNotifySettings](../types/PeerNotifySettings.md)


### Example:

```php
$peerNotifySettings = ['_' => 'peerNotifySettings', 'mute_until' => int, 'sound' => 'string', 'show_previews' => Bool, 'events_mask' => int];
```  


Or, if you're into Lua:

```lua
peerNotifySettings={_='peerNotifySettings', mute_until=int, sound='string', show_previews=Bool, events_mask=int}

```


