---
title: help.getConfig
description: Returns current configuration, icluding data center configuration.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getConfig.html
---
# Method: help.getConfig  
[Back to methods index](index.md)


Returns current configuration, icluding data center configuration.



### Return type: [Config](../types/Config.md)

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

Or, if you're into Lua:

```lua
Config = help.getConfig({})
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CONNECTION_DEVICE_MODEL_EMPTY|Device model empty|
|400|CONNECTION_NOT_INITED|Connection not initialized|
|400|CONNECTION_SYSTEM_EMPTY|Connection system empty|
|400|INPUT_LAYER_INVALID|The provided layer is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-503|Timeout|Timeout while fetching data|


