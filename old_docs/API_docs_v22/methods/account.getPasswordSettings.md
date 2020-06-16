---
title: account.getPasswordSettings
description: Get private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info &amp; so on)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getPasswordSettings.html
---
# Method: account.getPasswordSettings
[Back to methods index](index.md)



Get private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info &amp; so on)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|current\_password\_hash|[bytes](../types/bytes.md) |  | Yes|


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

$account.PasswordSettings = $MadelineProto->account->getPasswordSettings(['current_password_hash' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
account.PasswordSettings = account.getPasswordSettings({current_password_hash='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PASSWORD_HASH_INVALID|The provided password hash is invalid|


