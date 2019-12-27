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
|user|[User](../types/User.md) | Optional|Remaining user info|
|about|[string](../types/string.md) | Optional|Bio of the user|
|link|[contacts\_Link](../types/contacts_Link.md) | Yes|Link|
|profile\_photo|[Photo](../types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notification settings|
|bot\_info|[BotInfo](../types/BotInfo.md) | Optional|For bots, info about the bot (bot commands, etc)|



### Type: [UserFull](../types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'blocked' => Bool, 'user' => User, 'about' => 'string', 'link' => contacts_Link, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'bot_info' => BotInfo];
```  


Or, if you're into Lua:

```lua
userFull={_='userFull', blocked=Bool, user=User, about='string', link=contacts_Link, profile_photo=Photo, notify_settings=PeerNotifySettings, bot_info=BotInfo}

```


