---
title: "inputPeerNotifySettings"
description: "Notification settings."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerNotifySettings  
[Back to constructors index](index.md)



Notification settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|show\_previews|[Bool](../types/Bool.md) | Optional|If the text of the message shall be displayed in notification|
|silent|[Bool](../types/Bool.md) | Optional|Peer was muted?|
|mute\_until|[int](../types/int.md) | Optional|Date until which all notifications shall be switched off|
|sound|[string](../types/string.md) | Optional|Name of an audio file for notification|



### Type: [InputPeerNotifySettings](../types/InputPeerNotifySettings.md)


### Example:

```php
$inputPeerNotifySettings = ['_' => 'inputPeerNotifySettings', 'show_previews' => Bool, 'silent' => Bool, 'mute_until' => int, 'sound' => 'string'];
```  


Or, if you're into Lua:

```lua
inputPeerNotifySettings={_='inputPeerNotifySettings', show_previews=Bool, silent=Bool, mute_until=int, sound='string'}

```


