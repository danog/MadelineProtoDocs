---
title: auth.requestPasswordRecovery
description: Send an email to recover the 2FA password
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: auth.requestPasswordRecovery  
[Back to methods index](index.md)


Send an email to recover the 2FA password



### Return type: [auth\_PasswordRecovery](../types/auth_PasswordRecovery.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_PasswordRecovery = $MadelineProto->auth->requestPasswordRecovery();
```

Or, if you're into Lua:

```lua
auth_PasswordRecovery = auth.requestPasswordRecovery({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PASSWORD_EMPTY|The provided password is empty|


