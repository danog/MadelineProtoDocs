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


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$JSONValue = $MadelineProto->help->getAppConfig();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - help.getAppConfig
* params - `{}`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/help.getAppConfig`

Parameters:




Or, if you're into Lua:

```lua
JSONValue = help.getAppConfig({})
```

