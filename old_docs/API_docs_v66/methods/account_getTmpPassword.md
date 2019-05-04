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
|password\_hash|[bytes](../types/bytes.md) | The password hash | Yes|
|period|[int](../types/int.md) | The validity period | Yes|


### Return type: [account\_TmpPassword](../types/account_TmpPassword.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_TmpPassword = $MadelineProto->account->getTmpPassword(['password_hash' => 'bytes', 'period' => int, ]);
```

Or, if you're into Lua:

```lua
account_TmpPassword = account.getTmpPassword({password_hash='bytes', period=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PASSWORD_HASH_INVALID|The provided password hash is invalid|
|TMP_PASSWORD_DISABLED|The temporary password is disabled|


