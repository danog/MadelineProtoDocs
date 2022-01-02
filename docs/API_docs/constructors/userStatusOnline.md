---
title: "userStatusOnline"
description: "Online status of the user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userStatusOnline  
[Back to constructors index](index.md)



Online status of the user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|Time to expiration of the current online status|



### Type: [UserStatus](../types/UserStatus.md)


### Example:

```php
$userStatusOnline = ['_' => 'userStatusOnline', 'expires' => int];
```  


Or, if you're into Lua:

```lua
userStatusOnline={_='userStatusOnline', expires=int}

```


