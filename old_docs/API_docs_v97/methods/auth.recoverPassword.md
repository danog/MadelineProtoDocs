---
title: auth.recoverPassword
description: Reset the [2FA password](https://core.telegram.org/api/srp) using the recovery code sent using [auth.requestPasswordRecovery](../methods/auth.requestPasswordRecovery.md).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: auth.recoverPassword  
[Back to methods index](index.md)


Reset the [2FA password](https://core.telegram.org/api/srp) using the recovery code sent using [auth.requestPasswordRecovery](../methods/auth.requestPasswordRecovery.md).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|code|[string](../types/string.md) | Code received via email | Yes|


### Return type: [auth.Authorization](../types/auth.Authorization.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth.Authorization = $MadelineProto->auth->recoverPassword(['code' => 'string', ]);
```

Or, if you're into Lua:

```lua
auth.Authorization = auth.recoverPassword({code='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CODE_EMPTY|The provided code is empty|


