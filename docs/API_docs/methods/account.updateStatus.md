---
title: "account.updateStatus"
description: "Updates online user status."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateStatus.html
---
# Method: account.updateStatus
[Back to methods index](index.md)



Updates online user status.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offline|[Bool](../types/Bool.md) | If [(boolTrue)](../constructors/boolTrue.md) is transmitted, user status will change to [(userStatusOffline)](../constructors/userStatusOffline.md). | Yes|


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

$Bool = $MadelineProto->account->updateStatus(['offline' => Bool, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CONNECTION_LANG_PACK_INVALID|Language pack invalid|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|-3002|All workers are busy. Active_queries = X|All workers are busy. Active_queries = X|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-500|No workers running|Internal error|
|-503|Timeout|Timeout while fetching data|


