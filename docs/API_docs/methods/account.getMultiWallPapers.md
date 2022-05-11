---
title: "account.getMultiWallPapers"
description: "Get info about multiple wallpapers"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getMultiWallPapers.html
---
# Method: account.getMultiWallPapers
[Back to methods index](index.html)



Get info about multiple wallpapers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|wallpapers|Array of [InputWallPaper](/API_docs/types/InputWallPaper.html) | Wallpapers to fetch info about | Yes|


### Return type: [Vector\_of\_WallPaper](/API_docs/types/WallPaper.html)

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
$Vector_of_WallPaper = $MadelineProto->account->getMultiWallPapers(wallpapers: [InputWallPaper, InputWallPaper], );
```

