---
title: account.confirmPhone
description: Confirm a phone number to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.confirmPhone  
[Back to methods index](index.md)


Confirm a phone number to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_code\_hash|[string](../types/string.md) | Phone code hash, for more info [click here »](https://core.telegram.org/api/account-deletion) | Yes|
|phone\_code|[string](../types/string.md) | SMS code, for more info [click here »](https://core.telegram.org/api/account-deletion) | Yes|


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

$Bool = $MadelineProto->account->confirmPhone(['phone_code_hash' => 'string', 'phone_code' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = account.confirmPhone({phone_code_hash='string', phone_code='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CODE_HASH_INVALID|Code hash invalid|
|400|PHONE_CODE_EMPTY|phone_code is missing|


