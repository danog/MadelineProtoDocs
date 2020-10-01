---
title: account.resetWallPapers
description: Delete installed wallpapers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_resetWallPapers.html
---
# Method: account.resetWallPapers
[Back to methods index](index.md)



Delete installed wallpapers



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

$Bool = $MadelineProto->account->resetWallPapers();
```

Or, if you're into Lua:

```lua
Bool = account.resetWallPapers({})
```

