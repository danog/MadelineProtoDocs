---
title: "peerNotifySettings"
description: "Notification settings."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerNotifySettings  
[Back to constructors index](/API_docs/constructors/index.html)



Notification settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|show\_previews|[Bool](/API_docs/types/Bool.html) | Optional|Display text in notifications|
|silent|[Bool](/API_docs/types/Bool.html) | Optional|Mute peer?|
|mute\_until|[int](/API_docs/types/int.html) | Optional|Mute all notifications until this date|
|ios\_sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|
|android\_sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|
|other\_sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|



### Type: [PeerNotifySettings](/API_docs/types/PeerNotifySettings.html)


### Example:

```
$peerNotifySettings = ['_' => 'peerNotifySettings', 'show_previews' => Bool, 'silent' => Bool, 'mute_until' => int, 'ios_sound' => NotificationSound, 'android_sound' => NotificationSound, 'other_sound' => NotificationSound];
```  
