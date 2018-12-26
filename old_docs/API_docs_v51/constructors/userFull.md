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
|user|[User](../types/User.md) | Optional|User|
|about|[string](../types/string.md) | Optional|About|
|link|[contacts\_Link](../types/contacts_Link.md) | Yes|Link|
|profile\_photo|[Photo](../types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notify settings|
|bot\_info|[BotInfo](../types/BotInfo.md) | Optional|Bot info|



### Type: [UserFull](../types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'blocked' => Bool, 'user' => User, 'about' => 'string', 'link' => contacts_Link, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'bot_info' => BotInfo];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "userFull", "blocked": Bool, "user": User, "about": "string", "link": contacts_Link, "profile_photo": Photo, "notify_settings": PeerNotifySettings, "bot_info": BotInfo}
```


Or, if you're into Lua:

```lua
userFull={_='userFull', blocked=Bool, user=User, about='string', link=contacts_Link, profile_photo=Photo, notify_settings=PeerNotifySettings, bot_info=BotInfo}

```


