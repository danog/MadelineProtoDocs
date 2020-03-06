---
title: account.getMultiWallPapers
description: account.getMultiWallPapers parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getMultiWallPapers.html
---
# Method: account.getMultiWallPapers  
[Back to methods index](index.md)


### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|wallpapers|Array of [InputWallPaper](../types/InputWallPaper.md) | Yes|


### Return type: [Vector\_of\_WallPaper](../types/WallPaper.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_WallPaper = $MadelineProto->account->getMultiWallPapers(['wallpapers' => [InputWallPaper, InputWallPaper], ]);
```

Or, if you're into Lua:

```lua
Vector_of_WallPaper = account.getMultiWallPapers({wallpapers={InputWallPaper}, })
```

