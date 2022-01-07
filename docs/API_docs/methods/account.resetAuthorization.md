---
title: "account.resetAuthorization"
description: "Log out an active [authorized session](https://core.telegram.org/api/auth) by its hash"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_resetAuthorization.html
---
# Method: account.resetAuthorization
[Back to methods index](index.md)



Log out an active [authorized session](https://core.telegram.org/api/auth) by its hash

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|[long](/API_docs/types/long.md) | Session hash | Yes|


### Return type: [Bool](/API_docs/types/Bool.md)

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

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|HASH_INVALID|The provided hash is invalid|
|406|FRESH_RESET_AUTHORISATION_FORBIDDEN|You can't logout other sessions if less than 24 hours have passed since you logged on the current session|
|-503|Timeout|Timeout while fetching data|


