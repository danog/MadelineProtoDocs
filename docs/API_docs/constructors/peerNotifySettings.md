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
|show\_previews|[Bool](/API_docs/types/Bool.html) | Optional|(Ternary value) If set, indicates whether or not to display previews of messages in notifications; otherwise the default behavior should be used.|
|silent|[Bool](/API_docs/types/Bool.html) | Optional|(Ternary value) If set, indicates whether to mute or unmute the peer; otherwise the default behavior should be used.|
|mute\_until|[int](/API_docs/types/int.html) | Optional|Mute all notifications until this date|
|ios\_sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|Notification sound for the official iOS application|
|android\_sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|Notification sound for the official android application|
|other\_sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Optional|Notification sound for other applications|



### Type: [PeerNotifySettings](/API_docs/types/PeerNotifySettings.html)


### Example:

```
$peerNotifySettings = ['_' => 'peerNotifySettings', 'show_previews' => Bool, 'silent' => Bool, 'mute_until' => int, 'ios_sound' => NotificationSound, 'android_sound' => NotificationSound, 'other_sound' => NotificationSound];
```  
