---
title: "account.uploadWallPaper"
description: "Create and upload a new wallpaper"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_uploadWallPaper.html
---
# Method: account.uploadWallPaper
[Back to methods index](index.html)



Create and upload a new wallpaper

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | The JPG/PNG wallpaper | Yes|
|mime\_type|[string](/API_docs/types/string.html) | MIME type of uploaded wallpaper | Yes|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.html) | Wallpaper settings | Yes|


### Return type: [WallPaper](/API_docs/types/WallPaper.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$WallPaper = $MadelineProto->account->uploadWallPaper(file: InputFile, mime_type: 'string', settings: WallPaperSettings, );
```

