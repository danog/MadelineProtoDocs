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
|user|[User](../types/User.md) | Optional|



### Type: [auth\_Authorization](../types/auth_Authorization.md)


### Example:

```php
$auth_authorization = ['_' => 'auth.authorization', 'user' => User];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "auth.authorization", "user": User}
```


Or, if you're into Lua:

```lua
auth_authorization={_='auth.authorization', user=User}

```


