---
title: "reactionsNotifySettings"
description: "reactionsNotifySettings attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: reactionsNotifySettings  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|messages\_notify\_from|[ReactionNotificationsFrom](/API_docs/types/ReactionNotificationsFrom.html) | Optional|
|stories\_notify\_from|[ReactionNotificationsFrom](/API_docs/types/ReactionNotificationsFrom.html) | Optional|
|sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Yes|
|show\_previews|[Bool](/API_docs/types/Bool.html) | Yes|



### Type: [ReactionsNotifySettings](/API_docs/types/ReactionsNotifySettings.html)


### Example:

```
$reactionsNotifySettings = ['_' => 'reactionsNotifySettings', 'messages_notify_from' => ReactionNotificationsFrom, 'stories_notify_from' => ReactionNotificationsFrom, 'sound' => NotificationSound, 'show_previews' => Bool];
```  
