---
title: updates.getDifference
description: Get new [updates](https://core.telegram.org/api/updates).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getDifference.html
---
# Method: updates.getDifference
[Back to methods index](index.md)



Get new [updates](https://core.telegram.org/api/updates).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|pts|[int](../types/int.md) | PTS, see [updates](https://core.telegram.org/api/updates). | Yes|
|date|[int](../types/int.md) | date, see [updates](https://core.telegram.org/api/updates). | Yes|
|qts|[int](../types/int.md) | QTS, see [updates](https://core.telegram.org/api/updates). | Yes|


### Return type: [updates.Difference](../types/updates.Difference.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$updates_Difference = $MadelineProto->updates->getDifference(['pts' => int, 'date' => int, 'qts' => int, ]);
```

Or, if you're into Lua:

```lua
updates_Difference = updates.getDifference({pts=int, date=int, qts=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CDN_METHOD_INVALID|You can't call this method in a CDN DC|
|400|CONNECTION_DEVICE_MODEL_EMPTY|Device model empty|
|400|DATE_EMPTY|Date empty|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PERSISTENT_TIMESTAMP_EMPTY|Persistent timestamp empty|
|400|PERSISTENT_TIMESTAMP_INVALID|Persistent timestamp invalid|
|-3002|All workers are busy. Active_queries = X|All workers are busy. Active_queries = X|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-500|No workers running|Internal error|
|-504|memory limit exit|Internal error|
|-504|memory limit(?)|Internal error|
|-503|Timeout|Timeout while fetching data|


