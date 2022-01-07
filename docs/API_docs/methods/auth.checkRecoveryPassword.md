---
title: "auth.checkRecoveryPassword"
description: "auth.checkRecoveryPassword parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_checkRecoveryPassword.html
---
# Method: auth.checkRecoveryPassword
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|code|[string](/API_docs/types/string.md) | Yes|


### Return type: [Bool](/API_docs/types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->auth->checkRecoveryPassword(['code' => 'string', ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PASSWORD_RECOVERY_EXPIRED|The recovery code has expired|


