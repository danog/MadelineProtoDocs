---
title: "account.updatePasswordSettings"
description: "You cannot use this method directly; use $MadelineProto->update2fa($params), instead (see https://docs.madelineproto.xyz for more info)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updatePasswordSettings.html
---
# Method: account.updatePasswordSettings
[Back to methods index](index.html)



You cannot use this method directly; use $MadelineProto->update2fa($params), instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|password|[InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html) | The old password (see [SRP](https://core.telegram.org/api/srp)) | Yes|
|new\_settings|[account.PasswordInputSettings](/API_docs/types/account.PasswordInputSettings.html) | The new password (see [SRP](https://core.telegram.org/api/srp)) | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->account->updatePasswordSettings(password: InputCheckPasswordSRP, new_settings: account.PasswordInputSettings, );
```

