---
title: help.getAppUpdate
description: Returns information on update availability for the current application.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getAppUpdate.html
---
# Method: help.getAppUpdate
[Back to methods index](index.md)



Returns information on update availability for the current application.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|device\_model|[string](../types/string.md) |  | Yes|
|system\_version|[string](../types/string.md) |  | Yes|
|app\_version|[string](../types/string.md) |  | Yes|
|lang\_code|[string](../types/string.md) |  | Yes|


### Return type: [help.AppUpdate](../types/help.AppUpdate.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_AppUpdate = $MadelineProto->help->getAppUpdate(['device_model' => 'string', 'system_version' => 'string', 'app_version' => 'string', 'lang_code' => 'string', ]);
```

Or, if you're into Lua:

```lua
help_AppUpdate = help.getAppUpdate({device_model='string', system_version='string', app_version='string', lang_code='string', })
```

