---
title: account.getGlobalPrivacySettings
description: Get global privacy settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getGlobalPrivacySettings.html
---
# Method: account.getGlobalPrivacySettings
[Back to methods index](index.md)



Get global privacy settings



### Return type: [GlobalPrivacySettings](../types/GlobalPrivacySettings.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$GlobalPrivacySettings = $MadelineProto->account->getGlobalPrivacySettings();
```

Or, if you're into Lua:

```lua
GlobalPrivacySettings = account.getGlobalPrivacySettings({})
```

