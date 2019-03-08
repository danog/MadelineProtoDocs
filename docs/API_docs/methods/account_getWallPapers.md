---
title: account.getWallPapers
description: Returns a list of available wallpapers.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.getWallPapers  
[Back to methods index](index.md)


Returns a list of available wallpapers.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) |  | Optional|


### Return type: [account\_WallPapers](../types/account_WallPapers.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_WallPapers = $MadelineProto->account->getWallPapers(['hash' => [int, int], ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.getWallPapers`

Parameters:

hash - Json encoded  array of int




Or, if you're into Lua:

```lua
account_WallPapers = account.getWallPapers({hash={int}, })
```

