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
|user|[User](../types/User.md) | Optional|Remaining user info|
|link|[contacts.Link](../constructors/contacts.Link.md) | Yes|Link|
|profile\_photo|[Photo](../types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notification settings|
|blocked|[Bool](../types/Bool.md) | Yes|Blocked?|
|bot\_info|[BotInfo](../types/BotInfo.md) | Optional|For bots, info about the bot (bot commands, etc)|



### Type: [UserFull](../types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'user' => User, 'link' => contacts.Link, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'blocked' => Bool, 'bot_info' => BotInfo];
```  


Or, if you're into Lua:

```lua
userFull={_='userFull', user=User, link=contacts.Link, profile_photo=Photo, notify_settings=PeerNotifySettings, blocked=Bool, bot_info=BotInfo}

```


