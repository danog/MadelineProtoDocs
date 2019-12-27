---
title: account.resetAuthorization
description: Log out an active [authorized session](https://core.telegram.org/api/auth) by its hash
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.resetAuthorization  
[Back to methods index](index.md)


Log out an active [authorized session](https://core.telegram.org/api/auth) by its hash

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|[long](../types/long.md) | Session hash | Yes|


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

$Bool = $MadelineProto->account->resetAuthorization(['hash' => long, ]);
```

Or, if you're into Lua:

```lua
Bool = account.resetAuthorization({hash=long, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|HASH_INVALID|The provided hash is invalid|
|406|FRESH_RESET_AUTHORISATION_FORBIDDEN|You can't logout other sessions if less than 24 hours have passed since you logged on the current session|


