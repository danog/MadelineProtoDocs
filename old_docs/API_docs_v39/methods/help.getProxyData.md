---
title: help.getProxyData
description: Get promotion info of the currently-used MTProxy
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getProxyData.html
---
# Method: help.getProxyData
[Back to methods index](index.md)



Get promotion info of the currently-used MTProxy



### Return type: [help.ProxyData](../types/help.ProxyData.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help.ProxyData = $MadelineProto->help->getProxyData();
```

Or, if you're into Lua:

```lua
help.ProxyData = help.getProxyData({})
```

