---
title: userFull
description: userFull attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userFull  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user|[User](../types/User.md) | Optional|
|link|[contacts\_Link](../types/contacts_Link.md) | Yes|
|profile\_photo|[Photo](../types/Photo.md) | Optional|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|
|blocked|[Bool](../types/Bool.md) | Yes|
|real\_first\_name|[string](../types/string.md) | Yes|
|real\_last\_name|[string](../types/string.md) | Yes|



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


