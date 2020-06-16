---
title: account.getWallPaper
description: Get info about a certain wallpaper
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getWallPaper.html
---
# Method: account.getWallPaper
[Back to methods index](index.md)



Get info about a certain wallpaper

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|wallpaper|[InputWallPaper](../types/InputWallPaper.md) | The wallpaper to get info about | Yes|


### Return type: [WallPaper](../types/WallPaper.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$WallPaper = $MadelineProto->account->getWallPaper(['wallpaper' => InputWallPaper, ]);
```

Or, if you're into Lua:

```lua
WallPaper = account.getWallPaper({wallpaper=InputWallPaper, })
```

