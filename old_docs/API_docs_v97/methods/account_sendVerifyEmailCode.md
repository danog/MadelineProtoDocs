---
title: account.sendVerifyEmailCode
description: Send email verification code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.sendVerifyEmailCode  
[Back to methods index](index.md)


Send email verification code

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|email|[string](../types/string.md) | Email | Yes|


### Return type: [account\_SentEmailCode](../types/account_SentEmailCode.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_SentEmailCode = $MadelineProto->account->sendVerifyEmailCode(['email' => 'string', ]);
```

Or, if you're into Lua:

```lua
account_SentEmailCode = account.sendVerifyEmailCode({email='string', })
```

