---
title: help.getProxyData
description: Get information about the current proxy
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getProxyData  
[Back to methods index](index.md)


Get information about the current proxy



### Return type: [help\_ProxyData](../types/help_ProxyData.md)

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

$help_ProxyData = $MadelineProto->help->getProxyData();
```

Or, if you're into Lua:

```lua
help_ProxyData = help.getProxyData({})
```

