---
title: auth.loginTokenSuccess
description: auth.loginTokenSuccess attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginTokenSuccess.html
---
# Constructor: auth.loginTokenSuccess  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|authorization|[auth.Authorization](../constructors/auth.Authorization.md) | Yes|



### Type: [auth.LoginToken](../types/auth.LoginToken.md)


### Example:

```php
$auth.loginTokenSuccess = ['_' => 'auth.loginTokenSuccess', 'authorization' => auth.Authorization];
```  


Or, if you're into Lua:

```lua
auth.loginTokenSuccess={_='auth.loginTokenSuccess', authorization=auth.Authorization}

```


