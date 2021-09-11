---
title: account.confirmPasswordEmail
description: Verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_confirmPasswordEmail.html
---
# Method: account.confirmPasswordEmail
[Back to methods index](index.md)



Verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|code|[string](../types/string.md) | The phone code that was received after [setting a recovery email](https://core.telegram.org/api/srp#email-verification) | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->confirmPasswordEmail(['code' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.confirmPasswordEmail({code='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CODE_INVALID|Code invalid|
|400|EMAIL_HASH_EXPIRED|Email hash expired|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|


