---
title: "auth.loginTokenSuccess"
description: "Login via token (QR code) succeeded!"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginTokenSuccess.html
---
# Constructor: auth.loginTokenSuccess  
[Back to constructors index](/API_docs/constructors/index.html)



Login via token (QR code) succeeded!

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorization|[auth.Authorization](/API_docs/constructors/auth.Authorization.html) | Yes|Authorization info|



### Type: [auth.LoginToken](/API_docs/types/auth.LoginToken.html)


### Example:

```
$auth_loginTokenSuccess = ['_' => 'auth.loginTokenSuccess', 'authorization' => auth.Authorization];
```  
