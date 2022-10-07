---
title: "notificationSoundRingtone"
description: "A specific previously uploaded notification sound should be used"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: notificationSoundRingtone  
[Back to constructors index](/API_docs/constructors/index.html)



A specific previously uploaded notification sound should be used

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Document ID of notification sound uploaded using [account.uploadRingtone](../methods/account.uploadRingtone.html)|



### Type: [NotificationSound](/API_docs/types/NotificationSound.html)


### Example:

```
$notificationSoundRingtone = ['_' => 'notificationSoundRingtone', 'id' => long];
```  
