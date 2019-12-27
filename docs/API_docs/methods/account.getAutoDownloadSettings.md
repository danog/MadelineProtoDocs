---
title: account.getAutoDownloadSettings
description: Get media autodownload settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getAutoDownloadSettings  
[Back to methods index](index.md)


Get media autodownload settings



### Return type: [account.AutoDownloadSettings](../types/account.AutoDownloadSettings.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account.AutoDownloadSettings = $MadelineProto->account->getAutoDownloadSettings();
```

Or, if you're into Lua:

```lua
account.AutoDownloadSettings = account.getAutoDownloadSettings({})
```

