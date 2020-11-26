---
title: auth.loginToken
description: Login token (for [QR code login](https://core.telegram.org/api/qr-login))
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginToken.html
---
# Constructor: auth.loginToken  
[Back to constructors index](index.md)



Login token (for [QR code login](https://core.telegram.org/api/qr-login))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|Expiry date of QR code|
|token|[bytes](../types/bytes.md) | Yes|Token to render in QR code|



### Type: [auth.LoginToken](../types/auth.LoginToken.md)


### Example:

```php
$auth.loginToken = ['_' => 'auth.loginToken', 'expires' => int, 'token' => 'bytes'];
```  


Or, if you're into Lua:

```lua
auth.loginToken={_='auth.loginToken', expires=int, token='bytes'}

```


