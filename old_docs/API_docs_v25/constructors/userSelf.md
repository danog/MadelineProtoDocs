---
title: userSelf
description: User self
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userSelf  
[Back to constructors index](index.md)



User self

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|
|username|[string](../types/string.md) | Yes|Username|
|phone|[string](../types/string.md) | Yes|Phone|
|photo|[UserProfilePhoto](../types/UserProfilePhoto.md) | Optional|Photo|
|status|[UserStatus](../types/UserStatus.md) | Optional|Status|



### Type: [User](../types/User.md)


### Example:

```php
$userSelf = ['_' => 'userSelf', 'id' => int, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string', 'phone' => 'string', 'photo' => UserProfilePhoto, 'status' => UserStatus];
```  


Or, if you're into Lua:

```lua
userSelf={_='userSelf', id=int, first_name='string', last_name='string', username='string', phone='string', photo=UserProfilePhoto, status=UserStatus}

```


