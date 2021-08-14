---
title: account.setAccountTTL
description: Set account self-destruction period
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_setAccountTTL.html
---
# Method: account.setAccountTTL
[Back to methods index](index.md)



Set account self-destruction period

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|ttl|[AccountDaysTTL](../types/AccountDaysTTL.md) | Time to live in days | Yes|


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

$Bool = $MadelineProto->account->setAccountTTL(['ttl' => AccountDaysTTL, ]);
```

Or, if you're into Lua:

```lua
Bool = account.setAccountTTL({ttl=AccountDaysTTL, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|TTL_DAYS_INVALID|The provided TTL is invalid|


