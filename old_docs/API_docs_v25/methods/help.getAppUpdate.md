---
title: help.getAppUpdate
description: Returns information on update availability for the current application.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getAppUpdate.html
---
# Method: help.getAppUpdate
[Back to methods index](index.md)



Returns information on update availability for the current application.



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

$help.AppUpdate = $MadelineProto->help->getAppUpdate();
```

Or, if you're into Lua:

```lua
help.AppUpdate = help.getAppUpdate({})
```

