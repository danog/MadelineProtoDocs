---
title: auth.authorization
description: Authorization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.authorization  
[Back to constructors index](index.md)



Authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|Expiration date|
|user|[User](../types/User.md) | Optional|User|



### Type: [auth\_Authorization](../types/auth_Authorization.md)


### Example:

```php
$auth_authorization = ['_' => 'auth.authorization', 'expires' => int, 'user' => User];
```  


Or, if you're into Lua:

```lua
auth_authorization={_='auth.authorization', expires=int, user=User}

```


