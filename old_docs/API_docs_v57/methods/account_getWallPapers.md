---
title: account.getWallPapers
description: Returns a list of available wallpapers.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getWallPapers  
[Back to methods index](index.md)


Returns a list of available wallpapers.



### Return type: [Vector\_of\_WallPaper](../types/WallPaper.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_WallPaper = $MadelineProto->account->getWallPapers();
```

Or, if you're into Lua:

```lua
Vector_of_WallPaper = account.getWallPapers({})
```

