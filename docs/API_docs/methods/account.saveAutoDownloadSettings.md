---
title: "account.saveAutoDownloadSettings"
description: "Change media autodownload settings"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_saveAutoDownloadSettings.html
---
# Method: account.saveAutoDownloadSettings
[Back to methods index](index.md)



Change media autodownload settings

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|low|[Bool](../types/Bool.md) | Whether to save settings in the low data usage preset | Optional|
|high|[Bool](../types/Bool.md) | Whether to save settings in the high data usage preset | Optional|
|settings|[AutoDownloadSettings](../types/AutoDownloadSettings.md) | Media autodownload settings | Yes|


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

$Bool = $MadelineProto->account->saveAutoDownloadSettings(['low' => Bool, 'high' => Bool, 'settings' => AutoDownloadSettings, ]);
```

Or, if you're into Lua:

```lua
Bool = account.saveAutoDownloadSettings({low=Bool, high=Bool, settings=AutoDownloadSettings, })
```

