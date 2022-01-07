---
title: "updateNotifySettings"
description: "Changes in notification settings."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNotifySettings  
[Back to constructors index](/API_docs/constructors/index.md)



Changes in notification settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[NotifyPeer](/API_docs/types/NotifyPeer.md) | Yes|Nofication source|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.md) | Yes|New notification settings|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateNotifySettings = ['_' => 'updateNotifySettings', 'peer' => NotifyPeer, 'notify_settings' => PeerNotifySettings];
```  
