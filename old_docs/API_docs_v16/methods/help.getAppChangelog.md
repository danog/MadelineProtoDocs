---
title: help.getAppChangelog
description: Get changelog of current app.  
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getAppChangelog.html
---
# Method: help.getAppChangelog
[Back to methods index](index.md)



Get changelog of current app.  
Typically, an [updates](../constructors/updates.md) constructor will be returned, containing one or more [updateServiceNotification](../constructors/updateServiceNotification.md) updates with app-specific changelogs.



### Return type: [help.AppChangelog](../types/help.AppChangelog.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help.AppChangelog = $MadelineProto->help->getAppChangelog();
```

Or, if you're into Lua:

```lua
help.AppChangelog = help.getAppChangelog({})
```

