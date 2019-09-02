---
title: account.getTmpPassword
description: Get temporary password for buying products through bots
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getTmpPassword  
[Back to methods index](index.md)


Get temporary password for buying products through bots

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|password|[InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md) | Password | Yes|
|period|[int](../types/int.md) | The validity period | Yes|


### Return type: [account\_TmpPassword](../types/account_TmpPassword.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_TmpPassword = $MadelineProto->account->getTmpPassword(['password' => InputCheckPasswordSRP, 'period' => int, ]);
```

Or, if you're into Lua:

```lua
account_TmpPassword = account.getTmpPassword({password=InputCheckPasswordSRP, period=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PASSWORD_HASH_INVALID|The provided password hash is invalid|
|400|TMP_PASSWORD_DISABLED|The temporary password is disabled|


