---
title: auth.recoverPassword
description: Use the code that was emailed to you after running $MadelineProto->auth->requestPasswordRecovery to login to your account
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: auth.recoverPassword  
[Back to methods index](index.md)


Use the code that was emailed to you after running $MadelineProto->auth->requestPasswordRecovery to login to your account

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|code|[string](../types/string.md) | The code that was emailed to you | Yes|


### Return type: [auth\_Authorization](../types/auth_Authorization.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_Authorization = $MadelineProto->auth->recoverPassword(['code' => 'string', ]);
```

Or, if you're into Lua:

```lua
auth_Authorization = auth.recoverPassword({code='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CODE_EMPTY|The provided code is empty|


