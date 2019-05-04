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


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Config = $MadelineProto->help->getConfig();
```

Or, if you're into Lua:

```lua
Config = help.getConfig({})
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|Timeout|A timeout occurred while fetching data from the bot|


