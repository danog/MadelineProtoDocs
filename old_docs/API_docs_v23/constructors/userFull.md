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
|user|[User](../types/User.md) | Optional|User|
|link|[contacts\_Link](../types/contacts_Link.md) | Yes|Link|
|profile\_photo|[Photo](../types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notify settings|
|blocked|[Bool](../types/Bool.md) | Yes|Blocked?|
|real\_first\_name|[string](../types/string.md) | Yes|Real first name|
|real\_last\_name|[string](../types/string.md) | Yes|Real last name|



### Type: [UserFull](../types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'user' => User, 'link' => contacts_Link, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'blocked' => Bool, 'real_first_name' => 'string', 'real_last_name' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "userFull", "user": User, "link": contacts_Link, "profile_photo": Photo, "notify_settings": PeerNotifySettings, "blocked": Bool, "real_first_name": "string", "real_last_name": "string"}
```


Or, if you're into Lua:

```lua
userFull={_='userFull', user=User, link=contacts_Link, profile_photo=Photo, notify_settings=PeerNotifySettings, blocked=Bool, real_first_name='string', real_last_name='string'}

```


