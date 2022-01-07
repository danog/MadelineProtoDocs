---
title: "userFull"
description: "Extended user info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userFull  
[Back to constructors index](/API_docs/constructors/index.md)



Extended user info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|[Bool](/API_docs/types/Bool.md) | Optional|Whether you have blocked this user|
|phone\_calls\_available|[Bool](/API_docs/types/Bool.md) | Optional|Whether this user can make VoIP calls|
|phone\_calls\_private|[Bool](/API_docs/types/Bool.md) | Optional|Whether this user's privacy settings allow you to call him|
|can\_pin\_message|[Bool](/API_docs/types/Bool.md) | Optional|Whether you can pin messages in the chat with this user, you can do this only for a chat with yourself|
|has\_scheduled|[Bool](/API_docs/types/Bool.md) | Optional|Whether [scheduled messages](https://core.telegram.org/api/scheduled-messages) are available|
|video\_calls\_available|[Bool](/API_docs/types/Bool.md) | Optional|Whether the user can receive video calls|
|id|[long](/API_docs/types/long.md) | Yes|
|about|[string](/API_docs/types/string.md) | Optional|Bio of the user|
|settings|[PeerSettings](/API_docs/types/PeerSettings.md) | Yes|Peer settings|
|profile\_photo|[Photo](/API_docs/types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.md) | Yes|Notification settings|
|bot\_info|[BotInfo](/API_docs/types/BotInfo.md) | Optional|For bots, info about the bot (bot commands, etc)|
|pinned\_msg\_id|[int](/API_docs/types/int.md) | Optional|Message ID of the last [pinned message](https://core.telegram.org/api/pin)|
|common\_chats\_count|[int](/API_docs/types/int.md) | Yes|Chats in common with this user|
|folder\_id|[int](/API_docs/types/int.md) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|ttl\_period|[int](/API_docs/types/int.md) | Optional|
|theme\_emoticon|[string](/API_docs/types/string.md) | Optional|
|private\_forward\_name|[string](/API_docs/types/string.md) | Optional|



### Type: [UserFull](/API_docs/types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'blocked' => Bool, 'phone_calls_available' => Bool, 'phone_calls_private' => Bool, 'can_pin_message' => Bool, 'has_scheduled' => Bool, 'video_calls_available' => Bool, 'id' => long, 'about' => 'string', 'settings' => PeerSettings, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'bot_info' => BotInfo, 'pinned_msg_id' => int, 'common_chats_count' => int, 'folder_id' => int, 'ttl_period' => int, 'theme_emoticon' => 'string', 'private_forward_name' => 'string'];
```  
