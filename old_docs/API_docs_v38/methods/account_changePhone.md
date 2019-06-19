---
title: account.changePhone
description: Change the phone number associated to this account
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.changePhone  
[Back to methods index](index.md)


Change the phone number associated to this account

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | Phone number | Yes|
|phone\_code\_hash|[string](../types/string.md) | Phone code hash returned by account.sendChangePhoneCode | Yes|
|phone\_code|[string](../types/string.md) | The phone code sent by account.sendChangePhoneCode | Yes|


### Return type: [User](../types/User.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$User = $MadelineProto->account->changePhone(['phone_number' => 'string', 'phone_code_hash' => 'string', 'phone_code' => 'string', ]);
```

Or, if you're into Lua:

```lua
User = account.changePhone({phone_number='string', phone_code_hash='string', phone_code='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PHONE_NUMBER_INVALID|The phone number is invalid|


