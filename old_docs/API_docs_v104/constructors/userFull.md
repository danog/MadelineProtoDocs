---
title: userFull
description: User full
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userFull  
[Back to constructors index](index.md)



User full

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|[Bool](../types/Bool.md) | Optional|Blocked?|
|phone\_calls\_available|[Bool](../types/Bool.md) | Optional|Phone calls available?|
|phone\_calls\_private|[Bool](../types/Bool.md) | Optional|Phone calls private?|
|can\_pin\_message|[Bool](../types/Bool.md) | Optional|Can pin message?|
|user|[User](../types/User.md) | Optional|User|
|about|[string](../types/string.md) | Optional|About|
|settings|[PeerSettings](../types/PeerSettings.md) | Yes|Peer settings|
|profile\_photo|[Photo](../types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Yes|Notify settings|
|bot\_info|[BotInfo](../types/BotInfo.md) | Optional|Bot info|
|pinned\_msg\_id|[int](../types/int.md) | Optional|Pinned msg ID|
|common\_chats\_count|[int](../types/int.md) | Yes|Common chats count|
|folder\_id|[int](../types/int.md) | Optional|Folder ID|



### Type: [UserFull](../types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'blocked' => Bool, 'phone_calls_available' => Bool, 'phone_calls_private' => Bool, 'can_pin_message' => Bool, 'user' => User, 'about' => 'string', 'settings' => PeerSettings, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'bot_info' => BotInfo, 'pinned_msg_id' => int, 'common_chats_count' => int, 'folder_id' => int];
```  


Or, if you're into Lua:

```lua
userFull={_='userFull', blocked=Bool, phone_calls_available=Bool, phone_calls_private=Bool, can_pin_message=Bool, user=User, about='string', settings=PeerSettings, profile_photo=Photo, notify_settings=PeerNotifySettings, bot_info=BotInfo, pinned_msg_id=int, common_chats_count=int, folder_id=int}

```


