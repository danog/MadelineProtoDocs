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
|link|[contacts.Link](../constructors/contacts.Link.md) | Yes|
|profile\_photo|[Photo](../types/Photo.md) | Optional|Profile photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notification settings|
|blocked|[Bool](../types/Bool.md) | Yes|
|real\_first\_name|[string](../types/string.md) | Yes|
|real\_last\_name|[string](../types/string.md) | Yes|



### Type: [UserFull](../types/UserFull.md)


### Example:

```php
$userFull = ['_' => 'userFull', 'user' => User, 'link' => contacts.Link, 'profile_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'blocked' => Bool, 'real_first_name' => 'string', 'real_last_name' => 'string'];
```  


Or, if you're into Lua:

```lua
userFull={_='userFull', user=User, link=contacts.Link, profile_photo=Photo, notify_settings=PeerNotifySettings, blocked=Bool, real_first_name='string', real_last_name='string'}

```


