---
title: auth.loginToken
description: auth.loginToken attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginToken.html
---
# Constructor: auth.loginToken  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|expires|[int](../types/int.md) | Yes|
|token|[bytes](../types/bytes.md) | Yes|



### Type: [auth.LoginToken](../types/auth.LoginToken.md)


### Example:

```php
$auth.loginToken = ['_' => 'auth.loginToken', 'expires' => int, 'token' => 'bytes'];
```  


Or, if you're into Lua:

```lua
auth.loginToken={_='auth.loginToken', expires=int, token='bytes'}

```


