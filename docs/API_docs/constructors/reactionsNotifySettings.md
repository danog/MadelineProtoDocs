---
title: "reactionsNotifySettings"
description: "Reaction notification settings, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: reactionsNotifySettings  
[Back to constructors index](/API_docs/constructors/index.html)



Reaction notification settings, see [here »](https://core.telegram.org/api/reactions#notifications-about-reactions) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages\_notify\_from|[ReactionNotificationsFrom](/API_docs/types/ReactionNotificationsFrom.html) | Optional|Message reaction notification settings, if not set completely disables notifications/updates about message reactions.|
|stories\_notify\_from|[ReactionNotificationsFrom](/API_docs/types/ReactionNotificationsFrom.html) | Optional|Story reaction notification settings, if not set completely disables notifications/updates about reactions to stories.|
|sound|[NotificationSound](/API_docs/types/NotificationSound.html) | Yes|[Notification sound for reactions »](https://core.telegram.org/api/ringtones)|
|show\_previews|[Bool](/API_docs/types/Bool.html) | Yes|If false, [push notifications »](https://core.telegram.org/api/push-updates) about message/story reactions will only be of type `REACT_HIDDEN`/`REACT_STORY_HIDDEN`, without any information about the reacted-to story or the reaction itself.|



### Type: [ReactionsNotifySettings](/API_docs/types/ReactionsNotifySettings.html)


### Example:

```
$reactionsNotifySettings = ['_' => 'reactionsNotifySettings', 'messages_notify_from' => ReactionNotificationsFrom, 'stories_notify_from' => ReactionNotificationsFrom, 'sound' => NotificationSound, 'show_previews' => Bool];
```  
