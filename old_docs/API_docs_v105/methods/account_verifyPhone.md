---
title: account.verifyPhone
description: Verify phone number
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.verifyPhone  
[Back to methods index](index.md)


Verify phone number

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | The phone number | Yes|
|phone\_code\_hash|[string](../types/string.md) | The phone code hash returned by account.sendVerifyPhoneCode | Yes|
|phone\_code|[string](../types/string.md) | The phone code type returned by account.sendVerifyPhoneCode | Yes|


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

