---
title: help.getConfig
description: Get server configuration
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getConfig  
[Back to methods index](index.md)


Get server configuration



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
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-503|Timeout|Timeout while fetching data|


