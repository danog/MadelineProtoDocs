---
title: "auth.recoverPassword"
description: "Reset the [2FA password](https://core.telegram.org/api/srp) using the recovery code sent using [auth.requestPasswordRecovery](../methods/auth.requestPasswordRecovery.html)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_recoverPassword.html
---
# Method: auth.recoverPassword
[Back to methods index](index.html)



Reset the [2FA password](https://core.telegram.org/api/srp) using the recovery code sent using [auth.requestPasswordRecovery](../methods/auth.requestPasswordRecovery.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|code|[string](/API_docs/types/string.html) | Code received via email | Yes|
|new\_settings|[account.PasswordInputSettings](/API_docs/types/account.PasswordInputSettings.html) | New password | Optional|


### Return type: [auth.Authorization](/API_docs/types/auth.Authorization.html)

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
$auth_Authorization = $MadelineProto->auth->recoverPassword(code: 'string', new_settings: account.PasswordInputSettings, );
```

