---
title: "auth.acceptLoginToken"
description: "Accept QR code login token, logging in the app that generated it."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_acceptLoginToken.html
---
# Method: auth.acceptLoginToken
[Back to methods index](index.html)



Accept QR code login token, logging in the app that generated it.

Returns info about the new session.

For more info, see [login via QR code](https://core.telegram.org/api/qr-login).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|token|[bytes](/API_docs/types/bytes.html) | Login token embedded in QR code, for more info, see [login via QR code](https://core.telegram.org/api/qr-login). | Yes|


### Return type: [Authorization](/API_docs/types/Authorization.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Authorization = $MadelineProto->auth->acceptLoginToken(token: 'bytes', );
```

