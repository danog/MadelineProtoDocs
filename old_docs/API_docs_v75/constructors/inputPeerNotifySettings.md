---
title: inputPeerNotifySettings
description: Peer notify settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerNotifySettings  
[Back to constructors index](index.md)



Peer notify settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|show\_previews|[Bool](../types/Bool.md) | Optional|Show previews?|
|silent|[Bool](../types/Bool.md) | Optional|Silent?|
|mute\_until|[int](../types/int.md) | Yes|Mute until|
|sound|[string](../types/string.md) | Yes|Sound|



### Type: [InputPeerNotifySettings](../types/InputPeerNotifySettings.md)


### Example:

```php
$inputPeerNotifySettings = ['_' => 'inputPeerNotifySettings', 'show_previews' => Bool, 'silent' => Bool, 'mute_until' => int, 'sound' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPeerNotifySettings", "show_previews": Bool, "silent": Bool, "mute_until": int, "sound": "string"}
```


Or, if you're into Lua:

```lua
inputPeerNotifySettings={_='inputPeerNotifySettings', show_previews=Bool, silent=Bool, mute_until=int, sound='string'}

```


