---
title: account.resetNotifySettings
description: Resets all notification settings from users and groups.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_resetNotifySettings.html
---
# Method: account.resetNotifySettings  
[Back to methods index](index.md)


Resets all notification settings from users and groups.



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->resetNotifySettings();
```

Or, if you're into Lua:

```lua
Bool = account.resetNotifySettings({})
```

