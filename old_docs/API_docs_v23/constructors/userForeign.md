---
title: userForeign
description: User foreign
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userForeign  
[Back to constructors index](index.md)



User foreign

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|
|username|[string](../types/string.md) | Yes|Username|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|photo|[UserProfilePhoto](../types/UserProfilePhoto.md) | Optional|Photo|
|status|[UserStatus](../types/UserStatus.md) | Optional|Status|



### Type: [User](../types/User.md)


### Example:

```php
$userForeign = ['_' => 'userForeign', 'id' => int, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string', 'access_hash' => long, 'photo' => UserProfilePhoto, 'status' => UserStatus];
```  


Or, if you're into Lua:

```lua
userForeign={_='userForeign', id=int, first_name='string', last_name='string', username='string', access_hash=long, photo=UserProfilePhoto, status=UserStatus}

```


