---
title: account.resetNotifySettings
description: Reset all notification settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.resetNotifySettings  
[Back to methods index](index.md)


Reset all notification settings



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->resetNotifySettings();
```

Or, if you're into Lua:

```lua
Bool = account.resetNotifySettings({})
```

