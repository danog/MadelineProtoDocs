---
title: account.resetWallPapers
description: Reset wallpapers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.resetWallPapers  
[Back to methods index](index.md)


Reset wallpapers



### Return type: [Bool](../types/Bool.md)

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

$Bool = $MadelineProto->account->resetWallPapers();
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.resetWallPapers
* params - `{}`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.resetWallPapers`

Parameters:




Or, if you're into Lua:

```lua
Bool = account.resetWallPapers({})
```

