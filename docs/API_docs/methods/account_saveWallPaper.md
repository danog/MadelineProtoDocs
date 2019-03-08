---
title: account.saveWallPaper
description: Save wallpaper
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.saveWallPaper  
[Back to methods index](index.md)


Save wallpaper

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|wallpaper|[InputWallPaper](../types/InputWallPaper.md) | The wallpaper to save | Yes|
|unsave|[Bool](../types/Bool.md) | Delete saved wallpaper | Yes|
|settings|[WallPaperSettings](../types/WallPaperSettings.md) | The wallpaper to save | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->saveWallPaper(['wallpaper' => InputWallPaper, 'unsave' => Bool, 'settings' => WallPaperSettings, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.saveWallPaper
* params - `{"wallpaper": InputWallPaper, "unsave": Bool, "settings": WallPaperSettings, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.saveWallPaper`

Parameters:

wallpaper - Json encoded InputWallPaper

unsave - Json encoded Bool

settings - Json encoded WallPaperSettings




Or, if you're into Lua:

```lua
Bool = account.saveWallPaper({wallpaper=InputWallPaper, unsave=Bool, settings=WallPaperSettings, })
```

