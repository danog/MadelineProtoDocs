---
title: account.uploadWallPaper
description: Create and upload a new wallpaper
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_uploadWallPaper.html
---
# Method: account.uploadWallPaper
[Back to methods index](index.md)



Create and upload a new wallpaper

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file|[File path or InputFile](../types/InputFile.md) | The JPG/PNG wallpaper | Yes|
|mime\_type|[string](../types/string.md) | MIME type of uploaded wallpaper | Yes|
|settings|[WallPaperSettings](../types/WallPaperSettings.md) | Wallpaper settings | Yes|


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

$WallPaper = $MadelineProto->account->uploadWallPaper(['file' => InputFile, 'mime_type' => 'string', 'settings' => WallPaperSettings, ]);
```

Or, if you're into Lua:

```lua
WallPaper = account.uploadWallPaper({file=InputFile, mime_type='string', settings=WallPaperSettings, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|WALLPAPER_FILE_INVALID|The specified wallpaper file is invalid|
|400|WALLPAPER_MIME_INVALID|The specified wallpaper MIME type is invalid|


