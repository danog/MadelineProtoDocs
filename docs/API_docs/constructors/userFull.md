---
title: "userFull"
description: "Extended user info"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userFull  
[Back to constructors index](index.md)



Extended user info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|[Bool](../types/Bool.md) | Optional|Whether you have blocked this user|
|phone\_calls\_available|[Bool](../types/Bool.md) | Optional|Whether this user can make VoIP calls|
|phone\_calls\_private|[Bool](../types/Bool.md) | Optional|Whether this user's privacy settings allow you to call him|
|can\_pin\_message|[Bool](../types/Bool.md) | Optional|Whether you can pin messages in the chat with this user, you can do this only for a chat with yourself|
|has\_scheduled|[Bool](../types/Bool.md) | Optional|Whether [scheduled messages](https://core.telegram.org/api/scheduled-messages) are available|
|video\_calls\_available|[Bool](../types/Bool.md) | Optional|Whether the user can receive video calls|
|id|[long](../types/long.md) | Yes|
|about|[string](../types/string.md) | Optional|Bio of the user|
|settings|[PeerSettings](../types/PeerSettings.md) | Yes|Peer settings|
|profile\_photo|[Photo](../types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Yes|Notification settings|
|bot\_info|[BotInfo](../types/BotInfo.md) | Optional|For bots, info about the bot (bot commands, etc)|
|pinned\_msg\_id|[int](../types/int.md) | Optional|Message ID of the last [pinned message](https://core.telegram.org/api/pin)|
|common\_chats\_count|[int](../types/int.md) | Yes|Chats in common with this user|
|folder\_id|[int](../types/int.md) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|ttl\_period|[int](../types/int.md) | Optional|
|theme\_emoticon|[string](../types/string.md) | Optional|
|private\_forward\_name|[string](../types/string.md) | Optional|



### Type: [UserFull](../types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'blocked' => Bool, 'phone_calls_available' => Bool, 'phone_calls_private' => Bool, 'can_pin_message' => Bool, 'has_scheduled' => Bool, 'video_calls_available' => Bool, 'id' => long, 'about' => 'string', 'settings' => PeerSettings, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'bot_info' => BotInfo, 'pinned_msg_id' => int, 'common_chats_count' => int, 'folder_id' => int, 'ttl_period' => int, 'theme_emoticon' => 'string', 'private_forward_name' => 'string'];
```  


Or, if you're into Lua:

```lua
userFull={_='userFull', blocked=Bool, phone_calls_available=Bool, phone_calls_private=Bool, can_pin_message=Bool, has_scheduled=Bool, video_calls_available=Bool, id=long, about='string', settings=PeerSettings, profile_photo=Photo, notify_settings=PeerNotifySettings, bot_info=BotInfo, pinned_msg_id=int, common_chats_count=int, folder_id=int, ttl_period=int, theme_emoticon='string', private_forward_name='string'}

```


