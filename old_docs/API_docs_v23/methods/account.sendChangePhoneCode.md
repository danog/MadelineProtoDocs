---
title: account.sendChangePhoneCode
description: Verify a new phone number to associate to the current account
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.sendChangePhoneCode  
[Back to methods index](index.md)


Verify a new phone number to associate to the current account

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | New phone number | Yes|


### Return type: [account.SentChangePhoneCode](../types/account.SentChangePhoneCode.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account.SentChangePhoneCode = $MadelineProto->account->sendChangePhoneCode(['phone_number' => 'string', ]);
```

Or, if you're into Lua:

```lua
account.SentChangePhoneCode = account.sendChangePhoneCode({phone_number='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PHONE_NUMBER_INVALID|The phone number is invalid|


