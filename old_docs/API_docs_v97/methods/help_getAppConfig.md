---
title: help.getAppConfig
description: Get app config
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getAppConfig  
[Back to methods index](index.md)


Get app config



### Return type: [JSONValue](../types/JSONValue.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$JSONValue = $MadelineProto->help->getAppConfig();
```

Or, if you're into Lua:

```lua
JSONValue = help.getAppConfig({})
```

