---
title: "inputPeerNotifySettings"
description: "Notification settings."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerNotifySettings  
[Back to constructors index](/API_docs/constructors/index.html)



Notification settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|show\_previews|[Bool](/API_docs/types/Bool.html) | Optional|If the text of the message shall be displayed in notification|
|silent|[Bool](/API_docs/types/Bool.html) | Optional|Peer was muted?|
|mute\_until|[int](/API_docs/types/int.html) | Optional|Date until which all notifications shall be switched off|
|sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|Name of an audio file for notification|
|stories\_muted|[Bool](/API_docs/types/Bool.html) | Optional|
|stories\_hide\_sender|[Bool](/API_docs/types/Bool.html) | Optional|
|stories\_sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|



### Type: [InputPeerNotifySettings](/API_docs/types/InputPeerNotifySettings.html)


### Example:

```
$inputPeerNotifySettings = ['_' => 'inputPeerNotifySettings', 'show_previews' => Bool, 'silent' => Bool, 'mute_until' => int, 'sound' => NotificationSound, 'stories_muted' => Bool, 'stories_hide_sender' => Bool, 'stories_sound' => NotificationSound];
```  
