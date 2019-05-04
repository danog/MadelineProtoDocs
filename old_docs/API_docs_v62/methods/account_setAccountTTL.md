---
title: account.setAccountTTL
description: Set account TTL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.setAccountTTL  
[Back to methods index](index.md)


Set account TTL

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|ttl|[AccountDaysTTL](../types/AccountDaysTTL.md) | Time To Live of account | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->setAccountTTL(['ttl' => AccountDaysTTL, ]);
```

Or, if you're into Lua:

```lua
Bool = account.setAccountTTL({ttl=AccountDaysTTL, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|TTL_DAYS_INVALID|The provided TTL is invalid|


