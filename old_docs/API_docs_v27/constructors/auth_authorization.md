---
title: auth.authorization
description: auth_authorization attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.authorization  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|expires|[int](../types/int.md) | Yes|
|user|[User](../types/User.md) | Optional|



### Type: [auth\_Authorization](../types/auth_Authorization.md)


### Example:

```php
$auth_authorization = ['_' => 'auth.authorization', 'expires' => int, 'user' => User];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "auth.authorization", "expires": int, "user": User}
```


Or, if you're into Lua:

```lua
auth_authorization={_='auth.authorization', expires=int, user=User}

```


