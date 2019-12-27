---
title: auth.resendCode
description: Resend the login code via another medium, the phone code type is determined by the return value of the previous auth.sendCode/auth.resendCode: see [login](https://core.telegram.org/api/auth) for more info.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: auth.resendCode  
[Back to methods index](index.md)


Resend the login code via another medium, the phone code type is determined by the return value of the previous auth.sendCode/auth.resendCode: see [login](https://core.telegram.org/api/auth) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | The phone number | Yes|
|phone\_code\_hash|[string](../types/string.md) | The phone code hash obtained from [auth.sendCode](../methods/auth.sendCode.md) | Yes|


### Return type: [auth\_SentCode](../types/auth_SentCode.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_SentCode = $MadelineProto->auth->resendCode(['phone_number' => 'string', 'phone_code_hash' => 'string', ]);
```

Or, if you're into Lua:

```lua
auth_SentCode = auth.resendCode({phone_number='string', phone_code_hash='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PHONE_CODE_EXPIRED|The phone code you provided has expired, this may happen if it was sent to any chat on telegram (if the code is sent through a telegram chat (not the official account) to avoid it append or prepend to the code some chars)|
|400|PHONE_CODE_HASH_EMPTY|phone_code_hash is missing|
|400|PHONE_NUMBER_INVALID|The phone number is invalid|


