---
title: account.resetPassword
description: account.resetPassword parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_resetPassword.html
---
# Method: account.resetPassword
[Back to methods index](index.md)





### Return type: [account.ResetPasswordResult](../types/account.ResetPasswordResult.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_ResetPasswordResult = $MadelineProto->account->resetPassword();
```

Or, if you're into Lua:

```lua
account_ResetPasswordResult = account.resetPassword({})
```

