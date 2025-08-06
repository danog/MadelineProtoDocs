---
title: "account.resetWallPapers"
description: "Delete all installed [wallpapers](https://core.telegram.org/api/wallpapers), reverting to the default wallpaper set."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_resetWallPapers.html
---
# Method: account.resetWallPapers
[Back to methods index](index.html)



Delete all installed [wallpapers](https://core.telegram.org/api/wallpapers), reverting to the default wallpaper set.



### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->resetWallPapers();
```

