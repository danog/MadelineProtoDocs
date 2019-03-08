---
title: help.getSupportName
description: Get support name
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getSupportName  
[Back to methods index](index.md)


Get support name



### Return type: [help\_SupportName](../types/help_SupportName.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_SupportName = $MadelineProto->help->getSupportName();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - help.getSupportName
* params - `{}`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/help.getSupportName`

Parameters:




Or, if you're into Lua:

```lua
help_SupportName = help.getSupportName({})
```

