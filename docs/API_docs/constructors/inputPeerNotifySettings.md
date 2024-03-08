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
|sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|Identifier of an audio file to play for notifications.|
|stories\_muted|[Bool](/API_docs/types/Bool.html) | Optional|Whether story notifications should be disabled.|
|stories\_hide\_sender|[Bool](/API_docs/types/Bool.html) | Optional|Whether the sender name should be displayed in story notifications.|
|stories\_sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|Identifier of an audio file to play for story notifications.|



### Type: [InputPeerNotifySettings](/API_docs/types/InputPeerNotifySettings.html)


### Example:

```
$inputPeerNotifySettings = ['_' => 'inputPeerNotifySettings', 'show_previews' => Bool, 'silent' => Bool, 'mute_until' => int, 'sound' => NotificationSound, 'stories_muted' => Bool, 'stories_hide_sender' => Bool, 'stories_sound' => NotificationSound];
```  
