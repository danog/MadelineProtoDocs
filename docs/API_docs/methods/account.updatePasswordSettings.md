---
title: "account.updatePasswordSettings"
description: "You cannot use this method directly; use $MadelineProto->update2fa($params), instead (see https://docs.madelineproto.xyz for more info)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updatePasswordSettings.html
---
# Method: account.updatePasswordSettings
[Back to methods index](index.md)



You cannot use this method directly; use $MadelineProto->update2fa($params), instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|password|[InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md) | The old password (see [SRP](https://core.telegram.org/api/srp)) | Yes|
|new\_settings|[account.PasswordInputSettings](../types/account.PasswordInputSettings.md) | The new password (see [SRP](https://core.telegram.org/api/srp)) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->updatePasswordSettings(['password' => InputCheckPasswordSRP, 'new_settings' => account.PasswordInputSettings, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|EMAIL_UNCONFIRMED|Email unconfirmed|
|400|EMAIL_UNCONFIRMED_X|The provided email isn't confirmed, X is the length of the verification code that was just sent to the email.|
|400|INPUT_REQUEST_TOO_LONG|The request is too big|
|400|NEW_SALT_INVALID|The new salt is invalid|
|400|NEW_SETTINGS_INVALID|The new settings are invalid|
|400|PASSWORD_HASH_INVALID|The provided password hash is invalid|
|400|SRP_ID_INVALID|Invalid SRP ID provided|
|400|SRP_PASSWORD_CHANGED|Password has changed|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


