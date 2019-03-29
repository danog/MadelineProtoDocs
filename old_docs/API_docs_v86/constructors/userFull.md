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
|user|[User](../types/User.md) | Optional|User|
|about|[string](../types/string.md) | Optional|About|
|link|[contacts\_Link](../types/contacts_Link.md) | Yes|Link|
|profile\_photo|[Photo](../types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Yes|Notify settings|
|bot\_info|[BotInfo](../types/BotInfo.md) | Optional|Bot info|
|common\_chats\_count|[int](../types/int.md) | Yes|Common chats count|



### Type: [UserFull](../types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'blocked' => Bool, 'phone_calls_available' => Bool, 'phone_calls_private' => Bool, 'user' => User, 'about' => 'string', 'link' => contacts_Link, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'bot_info' => BotInfo, 'common_chats_count' => int];
```  


Or, if you're into Lua:

```lua
userFull={_='userFull', blocked=Bool, phone_calls_available=Bool, phone_calls_private=Bool, user=User, about='string', link=contacts_Link, profile_photo=Photo, notify_settings=PeerNotifySettings, bot_info=BotInfo, common_chats_count=int}

```


