---
title: "account.getContentSettings"
description: "Get sensitive content settings"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getContentSettings.html
---
# Method: account.getContentSettings
[Back to methods index](index.md)



Get sensitive content settings



### Return type: [account.ContentSettings](../types/account.ContentSettings.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_ContentSettings = $MadelineProto->account->getContentSettings();
```

Or, if you're into Lua:

```lua
account_ContentSettings = account.getContentSettings({})
```

