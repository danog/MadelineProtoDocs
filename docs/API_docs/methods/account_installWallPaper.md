---
title: account.installWallPaper
description: Install wallpaper
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
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

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->installWallPaper(['wallpaper' => InputWallPaper, 'settings' => WallPaperSettings, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.installWallPaper
* params - `{"wallpaper": InputWallPaper, "settings": WallPaperSettings, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.installWallPaper`

Parameters:

wallpaper - Json encoded InputWallPaper

settings - Json encoded WallPaperSettings




Or, if you're into Lua:

```lua
Bool = account.installWallPaper({wallpaper=InputWallPaper, settings=WallPaperSettings, })
```

