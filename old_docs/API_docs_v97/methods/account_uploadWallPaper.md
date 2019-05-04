---
title: account.uploadWallPaper
description: Upload wallpaper
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.uploadWallPaper  
[Back to methods index](index.md)


Upload wallpaper

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file|[File path or InputFile](../types/InputFile.md) | Image | Yes|
|mime\_type|[string](../types/string.md) | Mime type | Yes|
|settings|[WallPaperSettings](../types/WallPaperSettings.md) | Wallpaper settings | Yes|


### Return type: [WallPaper](../types/WallPaper.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$WallPaper = $MadelineProto->account->uploadWallPaper(['file' => InputFile, 'mime_type' => 'string', 'settings' => WallPaperSettings, ]);
```

Or, if you're into Lua:

```lua
WallPaper = account.uploadWallPaper({file=InputFile, mime_type='string', settings=WallPaperSettings, })
```

