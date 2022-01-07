---
title: "help.getConfig"
description: "Returns current configuration, including data center configuration."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getConfig.html
---
# Method: help.getConfig
[Back to methods index](index.html)



Returns current configuration, including data center configuration.



### Return type: [Config](/API_docs/types/Config.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Config = $MadelineProto->help->getConfig();
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CONNECTION_API_ID_INVALID|The provided API id is invalid|
|400|CONNECTION_APP_VERSION_EMPTY|App version is empty|
|400|CONNECTION_DEVICE_MODEL_EMPTY|Device model empty|
|400|CONNECTION_LANG_PACK_INVALID|Language pack invalid|
|400|CONNECTION_LAYER_INVALID|Layer invalid|
|400|CONNECTION_NOT_INITED|Connection not initialized|
|400|CONNECTION_SYSTEM_EMPTY|Connection system empty|
|400|CONNECTION_SYSTEM_LANG_CODE_EMPTY|The system_lang_code field is empty|
|400|DATA_INVALID|Encrypted data invalid|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|INPUT_LAYER_INVALID|The provided layer is invalid|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|USERNAME_INVALID|The provided username is not valid|
|-3002|All workers are busy. Active_queries = X|All workers are busy. Active_queries = X|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|USER_PRIVACY_RESTRICTED|The user's privacy settings do not allow you to do this|
|-500|No workers running|Internal error|
|-503|Timeout|Timeout while fetching data|


