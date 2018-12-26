---
title: help.getAppUpdate
description: Get info about app updates
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: help.getAppUpdate  
[Back to methods index](index.md)


Get info about app updates

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|source|[string](../types/string.md) | Source | Yes|


### Return type: [help\_AppUpdate](../types/help_AppUpdate.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_AppUpdate = $MadelineProto->help->getAppUpdate(['source' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/help.getAppUpdate`

Parameters:

source - Json encoded string




Or, if you're into Lua:

```lua
help_AppUpdate = help.getAppUpdate({source='string', })
```

