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


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_ProxyData = $MadelineProto->help->getProxyData();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - help.getProxyData
* params - `{}`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/help.getProxyData`

Parameters:




Or, if you're into Lua:

```lua
help_ProxyData = help.getProxyData({})
```

