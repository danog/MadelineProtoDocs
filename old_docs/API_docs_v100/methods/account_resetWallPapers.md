---
title: account.resetWallPapers
description: Reset wallpapers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.resetWallPapers  
[Back to methods index](index.md)


Reset wallpapers



### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


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

