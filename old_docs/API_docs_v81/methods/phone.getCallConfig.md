---
title: phone.getCallConfig
description: Get phone call configuration to be passed to libtgvoip's shared config
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: phone.getCallConfig  
[Back to methods index](index.md)


Get phone call configuration to be passed to libtgvoip's shared config



### Return type: [DataJSON](../types/DataJSON.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$DataJSON = $MadelineProto->phone->getCallConfig();
```

Or, if you're into Lua:

```lua
DataJSON = phone.getCallConfig({})
```

