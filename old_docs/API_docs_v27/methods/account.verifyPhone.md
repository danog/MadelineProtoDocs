---
title: account.verifyPhone
description: Verify a phone number for telegram [passport](https://core.telegram.org/passport).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_verifyPhone.html
---
# Method: account.verifyPhone
[Back to methods index](index.md)



Verify a phone number for telegram [passport](https://core.telegram.org/passport).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | Phone number | Yes|
|phone\_code\_hash|[string](../types/string.md) | Phone code hash received from the call to [account.sendVerifyPhoneCode](../methods/account.sendVerifyPhoneCode.md) | Yes|
|phone\_code|[string](../types/string.md) | Code received after the call to [account.sendVerifyPhoneCode](../methods/account.sendVerifyPhoneCode.md) | Yes|


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

$Bool = $MadelineProto->account->verifyPhone(['phone_number' => 'string', 'phone_code_hash' => 'string', 'phone_code' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.verifyPhone({phone_number='string', phone_code_hash='string', phone_code='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PHONE_CODE_EXPIRED|The phone code you provided has expired, this may happen if it was sent to any chat on telegram (if the code is sent through a telegram chat (not the official account) to avoid it append or prepend to the code some chars)|


