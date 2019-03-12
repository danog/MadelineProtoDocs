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


### MadelineProto Example:


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

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.uploadWallPaper
* params - `{"file": InputFile, "mime_type": "string", "settings": WallPaperSettings, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.uploadWallPaper`

Parameters:

file - Json encoded InputFile

mime_type - Json encoded string

settings - Json encoded WallPaperSettings




Or, if you're into Lua:

```lua
WallPaper = account.uploadWallPaper({file=InputFile, mime_type='string', settings=WallPaperSettings, })
```

