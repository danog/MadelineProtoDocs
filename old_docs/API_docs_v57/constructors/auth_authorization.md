---
title: auth.authorization
description: Contains user authorization info.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.authorization  
[Back to constructors index](index.md)



Contains user authorization info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|tmp\_sessions|[int](../types/int.md) | Optional|Temporary [passport](https://core.telegram.org/passport) sessions|
|user|[User](../types/User.md) | Optional|Info on authorized user|



### Type: [auth\_Authorization](../types/auth_Authorization.md)


### Example:

```php
$auth_authorization = ['_' => 'auth.authorization', 'tmp_sessions' => int, 'user' => User];
```  


Or, if you're into Lua:

```lua
auth_authorization={_='auth.authorization', tmp_sessions=int, user=User}

```


