---
title: "auth.checkPassword"
description: "You cannot use this method directly, use the complete2falogin method instead (see https://docs.madelineproto.xyz for more info)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_checkPassword.html
---
# Method: auth.checkPassword
[Back to methods index](index.md)



You cannot use this method directly, use the complete2falogin method instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|password|[InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md) | The account's password (see [SRP](https://core.telegram.org/api/srp)) | Yes|


### Return type: [auth.Authorization](../types/auth.Authorization.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_Authorization = $MadelineProto->auth->checkPassword(['password' => InputCheckPasswordSRP, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PASSWORD_HASH_INVALID|The provided password hash is invalid|
|400|SRP_ID_INVALID|Invalid SRP ID provided|
|400|SRP_PASSWORD_CHANGED|Password has changed|
|-503|Timeout|Timeout while fetching data|


