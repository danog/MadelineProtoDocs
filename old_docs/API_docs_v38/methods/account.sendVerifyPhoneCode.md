---
title: account.sendVerifyPhoneCode
description: Send the verification phone code for telegram [passport](https://core.telegram.org/passport).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_sendVerifyPhoneCode.html
---
# Method: account.sendVerifyPhoneCode
[Back to methods index](index.md)



Send the verification phone code for telegram [passport](https://core.telegram.org/passport).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | The phone number to verify | Yes|
|settings|[CodeSettings](../types/CodeSettings.md) | Phone code settings | Yes|


### Return type: [auth.SentCode](../types/auth.SentCode.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_SentCode = $MadelineProto->account->sendVerifyPhoneCode(['phone_number' => 'string', 'settings' => CodeSettings, ]);
```

Or, if you're into Lua:

```lua
auth_SentCode = account.sendVerifyPhoneCode({phone_number='string', settings=CodeSettings, })
```

