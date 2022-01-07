---
title: "auth.requestPasswordRecovery"
description: "Request recovery code of a [2FA password](https://core.telegram.org/api/srp), only for accounts with a [recovery email configured](https://core.telegram.org/api/srp#email-verification)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_requestPasswordRecovery.html
---
# Method: auth.requestPasswordRecovery
[Back to methods index](index.md)



Request recovery code of a [2FA password](https://core.telegram.org/api/srp), only for accounts with a [recovery email configured](https://core.telegram.org/api/srp#email-verification).



### Return type: [auth.PasswordRecovery](../types/auth.PasswordRecovery.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_PasswordRecovery = $MadelineProto->auth->requestPasswordRecovery();
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PASSWORD_EMPTY|The provided password is empty|
|400|PASSWORD_RECOVERY_NA|No email was set, can't recover password via email.|


