---
title: "account.uploadWallPaper"
description: "Create and upload a new [wallpaper](https://core.telegram.org/api/wallpapers)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_uploadWallPaper.html
---
# Method: account.uploadWallPaper
[Back to methods index](index.html)



Create and upload a new [wallpaper](https://core.telegram.org/api/wallpapers)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|for\_chat|[Bool](/API_docs/types/Bool.html) | Set this flag when uploading wallpapers to be passed to [messages.setChatWallPaper](../methods/messages.setChatWallPaper.html). | Optional|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | The JPG/PNG wallpaper | Yes|
|mime\_type|[string](/API_docs/types/string.html) | MIME type of uploaded wallpaper | Optional|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.html) | Wallpaper settings | Yes|


### Return type: [WallPaper](/API_docs/types/WallPaper.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$WallPaper = $MadelineProto->account->uploadWallPaper(for_chat: $Bool, file: $InputFile, mime_type: 'string', settings: $WallPaperSettings, );
```

