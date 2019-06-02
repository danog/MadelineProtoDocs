---
title: account.getAutoDownloadSettings
description: Get autodownload settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getAutoDownloadSettings  
[Back to methods index](index.md)


Get autodownload settings



### Return type: [account\_AutoDownloadSettings](../types/account_AutoDownloadSettings.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_AutoDownloadSettings = $MadelineProto->account->getAutoDownloadSettings();
```

Or, if you're into Lua:

```lua
account_AutoDownloadSettings = account.getAutoDownloadSettings({})
```

