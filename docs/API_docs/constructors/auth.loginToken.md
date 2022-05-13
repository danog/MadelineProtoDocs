---
title: "auth.loginToken"
description: "Login token (for QR code login)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginToken.html
---
# Constructor: auth.loginToken  
[Back to constructors index](/API_docs/constructors/index.html)



Login token (for [QR code login](https://core.telegram.org/api/qr-login))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](/API_docs/types/int.html) | Yes|Expiry date of QR code|
|token|[bytes](/API_docs/types/bytes.html) | Yes|Token to render in QR code|



### Type: [auth.LoginToken](/API_docs/types/auth.LoginToken.html)


### Example:

```
$auth_loginToken = ['_' => 'auth.loginToken', 'expires' => int, 'token' => 'bytes'];
```  
