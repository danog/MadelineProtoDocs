---
title: "auth.exportLoginToken"
description: "Generate a login token, for [login via QR code](https://core.telegram.org/api/qr-login).  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_exportLoginToken.html
---
# Method: auth.exportLoginToken
[Back to methods index](index.html)



Generate a login token, for [login via QR code](https://core.telegram.org/api/qr-login).  
The generated login token should be encoded using base64url, then shown as a `tg://login?token=base64encodedtoken` URL in the QR code.

For more info, see [login via QR code](https://core.telegram.org/api/qr-login).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|api\_id|[int](/API_docs/types/int.html) | Application identifier (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|api\_hash|[string](/API_docs/types/string.html) | Application identifier hash (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|except\_ids|Array of [long](/API_docs/types/long.html) | List of already logged-in user IDs, to prevent logging in twice with the same user | Yes|


### Return type: [auth.LoginToken](/API_docs/types/auth.LoginToken.html)

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
$auth_LoginToken = $MadelineProto->auth->exportLoginToken(api_id: int, api_hash: 'string', except_ids: [long, long], );
```

