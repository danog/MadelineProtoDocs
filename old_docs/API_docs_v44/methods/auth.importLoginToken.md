---
title: auth.importLoginToken
description: Login using a redirected login token, generated in case of DC mismatch during [QR code login](https://core.telegram.org/api/qr-login).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_importLoginToken.html
---
# Method: auth.importLoginToken
[Back to methods index](index.md)



Login using a redirected login token, generated in case of DC mismatch during [QR code login](https://core.telegram.org/api/qr-login).

For more info, see [login via QR code](https://core.telegram.org/api/qr-login).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token|[bytes](../types/bytes.md) | Login token | Yes|


### Return type: [auth.LoginToken](../types/auth.LoginToken.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth.LoginToken = $MadelineProto->auth->importLoginToken(['token' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
auth.LoginToken = auth.importLoginToken({token='bytes', })
```

