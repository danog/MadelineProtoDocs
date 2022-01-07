---
title: "account.installWallPaper"
description: "Install wallpaper"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_installWallPaper.html
---
# Method: account.installWallPaper
[Back to methods index](index.md)



Install wallpaper

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|wallpaper|[InputWallPaper](../types/InputWallPaper.md) | Wallpaper to install | Yes|
|settings|[WallPaperSettings](../types/WallPaperSettings.md) | Wallpaper settings | Yes|


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

$Bool = $MadelineProto->account->installWallPaper(['wallpaper' => InputWallPaper, 'settings' => WallPaperSettings, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|WALLPAPER_INVALID|The specified wallpaper is invalid|


