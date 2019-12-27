---
title: account.getPasswordSettings
description: You cannot use this method directly; use $MadelineProto->update_2fa($params), instead (see https://docs.madelineproto.xyz for more info)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getPasswordSettings  
[Back to methods index](index.md)


You cannot use this method directly; use $MadelineProto->update_2fa($params), instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|password|[InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md) | You cannot use this method directly; use $MadelineProto->update_2fa($params), instead (see https://docs.madelineproto.xyz for more info) | Yes|


### Return type: [account.PasswordSettings](../types/account.PasswordSettings.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account.PasswordSettings = $MadelineProto->account->getPasswordSettings(['password' => InputCheckPasswordSRP, ]);
```

Or, if you're into Lua:

```lua
account.PasswordSettings = account.getPasswordSettings({password=InputCheckPasswordSRP, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PASSWORD_HASH_INVALID|The provided password hash is invalid|


