---
title: userFull
description: Extended user info
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
|user|[User](../types/User.md) | Optional|Remaining user info|
|about|[string](../types/string.md) | Optional|Bio of the user|
|link|[contacts\_Link](../types/contacts_Link.md) | Yes|Link|
|profile\_photo|[Photo](../types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Yes|Notification settings|
|bot\_info|[BotInfo](../types/BotInfo.md) | Optional|For bots, info about the bot (bot commands, etc)|
|common\_chats\_count|[int](../types/int.md) | Yes|Chats in common with this user|



### Type: [UserFull](../types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'blocked' => Bool, 'phone_calls_available' => Bool, 'phone_calls_private' => Bool, 'user' => User, 'about' => 'string', 'link' => contacts_Link, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'bot_info' => BotInfo, 'common_chats_count' => int];
```  


Or, if you're into Lua:

```lua
userFull={_='userFull', blocked=Bool, phone_calls_available=Bool, phone_calls_private=Bool, user=User, about='string', link=contacts_Link, profile_photo=Photo, notify_settings=PeerNotifySettings, bot_info=BotInfo, common_chats_count=int}

```


