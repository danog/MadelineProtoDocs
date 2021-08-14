---
title: invokeWithLayer
description: Invoke the specified query using the specified API [layer](https://core.telegram.org/api/invoking#layers)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: invokeWithLayer
[Back to methods index](index.md)



Invoke the specified query using the specified API [layer](https://core.telegram.org/api/invoking#layers)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|layer|[int](../types/int.md) | The layer to use | Yes|
|query|[!X](../types/!X.md) | The query | Yes|


### Return type: [X](../types/X.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$X = $MadelineProto->invokeWithLayer(['layer' => int, 'query' => !X, ]);
```

Or, if you're into Lua:

```lua
X = invokeWithLayer({layer=int, query=!X, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|AUTH_BYTES_INVALID|The provided authorization is invalid|
|400|CDN_METHOD_INVALID|You can't call this method in a CDN DC|
|400|CONNECTION_API_ID_INVALID|The provided API id is invalid|
|400|CONNECTION_DEVICE_MODEL_EMPTY|Device model empty|
|400|CONNECTION_LANG_PACK_INVALID|Language pack invalid|
|400|CONNECTION_NOT_INITED|Connection not initialized|
|400|CONNECTION_SYSTEM_EMPTY|Connection system empty|
|400|INPUT_LAYER_INVALID|The provided layer is invalid|
|400|INVITE_HASH_EXPIRED|The invite link has expired|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|-503|Timeout|Timeout while fetching data|


