---
title: "auth.loginTokenSuccess"
description: "Login via token (QR code) succeded!"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginTokenSuccess.html
---
# Constructor: auth.loginTokenSuccess  
[Back to constructors index](index.md)



Login via token (QR code) succeded!

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorization|[auth.Authorization](../constructors/auth.Authorization.md) | Yes|Authorization info|



### Type: [auth.LoginToken](../types/auth.LoginToken.md)


### Example:

```php
$auth_loginTokenSuccess = ['_' => 'auth.loginTokenSuccess', 'authorization' => auth.Authorization];
```  


Or, if you're into Lua:

```lua
auth_loginTokenSuccess={_='auth.loginTokenSuccess', authorization=auth.Authorization}

```


