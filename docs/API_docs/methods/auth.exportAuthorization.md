---
title: "auth.exportAuthorization"
description: "You cannot use this method directly, use $MadelineProto->exportAuthorization() instead, see https://docs.madelineproto.xyz/docs/LOGIN.html"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_exportAuthorization.html
---
# Method: auth.exportAuthorization
[Back to methods index](index.md)



You cannot use this method directly, use $MadelineProto->exportAuthorization() instead, see https://docs.madelineproto.xyz/docs/LOGIN.html

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|dc\_id|[int](../types/int.md) | Number of a target data-centre | Yes|


### Return type: [auth.ExportedAuthorization](../types/auth.ExportedAuthorization.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_ExportedAuthorization = $MadelineProto->auth->exportAuthorization(['dc_id' => int, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|DC_ID_INVALID|The provided DC ID is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-503|Timeout|Timeout while fetching data|


