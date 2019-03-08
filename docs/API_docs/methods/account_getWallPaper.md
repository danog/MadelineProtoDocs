---
title: account.getWallPaper
description: account.getWallPaper parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getWallPaper  
[Back to methods index](index.md)


### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|wallpaper|[InputWallPaper](../types/InputWallPaper.md) | Yes|


### Return type: [WallPaper](../types/WallPaper.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$WallPaper = $MadelineProto->account->getWallPaper(['wallpaper' => InputWallPaper, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.getWallPaper
* params - `{"wallpaper": InputWallPaper, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.getWallPaper`

Parameters:

wallpaper - Json encoded InputWallPaper




Or, if you're into Lua:

```lua
WallPaper = account.getWallPaper({wallpaper=InputWallPaper, })
```

