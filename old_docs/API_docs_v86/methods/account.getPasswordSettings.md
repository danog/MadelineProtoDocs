---
title: account.getPasswordSettings
description: Get private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info & so on)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getPasswordSettings  
[Back to methods index](index.md)


Get private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info & so on)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|password|[InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md) | The password (see [SRP](https://core.telegram.org/api/srp)) | Yes|


### Return type: [account\_PasswordSettings](../types/account_PasswordSettings.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_PasswordSettings = $MadelineProto->account->getPasswordSettings(['password' => InputCheckPasswordSRP, ]);
```

Or, if you're into Lua:

```lua
account_PasswordSettings = account.getPasswordSettings({password=InputCheckPasswordSRP, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PASSWORD_HASH_INVALID|The provided password hash is invalid|


