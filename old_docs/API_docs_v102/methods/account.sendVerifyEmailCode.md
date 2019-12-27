---
title: account.sendVerifyEmailCode
description: Send the verification email code for telegram [passport](https://core.telegram.org/passport).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.sendVerifyEmailCode  
[Back to methods index](index.md)


Send the verification email code for telegram [passport](https://core.telegram.org/passport).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|email|[string](../types/string.md) | The email where to send the code | Yes|


### Return type: [account\_SentEmailCode](../types/account_SentEmailCode.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_SentEmailCode = $MadelineProto->account->sendVerifyEmailCode(['email' => 'string', ]);
```

Or, if you're into Lua:

```lua
account_SentEmailCode = account.sendVerifyEmailCode({email='string', })
```

