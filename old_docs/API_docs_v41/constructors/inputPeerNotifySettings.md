---
title: inputPeerNotifySettings
description: Notification settings.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerNotifySettings  
[Back to constructors index](index.md)



Notification settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|mute\_until|[int](../types/int.md) | Yes|Date until which all notifications shall be switched off|
|sound|[string](../types/string.md) | Yes|Name of an audio file for notification|
|show\_previews|[Bool](../types/Bool.md) | Yes|If the text of the message shall be displayed in notification|
|events\_mask|[int](../types/int.md) | Yes|Events mask|



### Type: [InputPeerNotifySettings](../types/InputPeerNotifySettings.md)


### Example:

```php
$inputPeerNotifySettings = ['_' => 'inputPeerNotifySettings', 'mute_until' => int, 'sound' => 'string', 'show_previews' => Bool, 'events_mask' => int];
```  


Or, if you're into Lua:

```lua
inputPeerNotifySettings={_='inputPeerNotifySettings', mute_until=int, sound='string', show_previews=Bool, events_mask=int}

```


