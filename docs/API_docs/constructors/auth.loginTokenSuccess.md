---
title: "auth.loginTokenSuccess"
description: "Login via token (QR code) succeded!"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginTokenSuccess.html
---
# Constructor: auth.loginTokenSuccess  
[Back to constructors index](/API_docs/constructors/index.md)



Login via token (QR code) succeded!

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorization|[auth.Authorization](/API_docs/constructors/auth.Authorization.md) | Yes|Authorization info|



### Type: [auth.LoginToken](/API_docs/types/auth.LoginToken.md)


### Example:

```php
$auth_loginTokenSuccess = ['_' => 'auth.loginTokenSuccess', 'authorization' => auth.Authorization];
```  
