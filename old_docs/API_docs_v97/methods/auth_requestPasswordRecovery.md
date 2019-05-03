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


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_PasswordRecovery = $MadelineProto->auth->requestPasswordRecovery();
```

Or, if you're into Lua:

```lua
auth_PasswordRecovery = auth.requestPasswordRecovery({})
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PASSWORD_EMPTY|The provided password is empty|


