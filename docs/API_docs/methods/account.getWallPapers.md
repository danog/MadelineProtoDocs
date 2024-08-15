---
title: "account.getWallPapers"
description: "Returns a list of available [wallpapers](https://core.telegram.org/api/wallpapers)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getWallPapers.html
---
# Method: account.getWallPapers
[Back to methods index](index.html)



Returns a list of available [wallpapers](https://core.telegram.org/api/wallpapers).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long|string](/API_docs/types/long|string.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [account.WallPapers](/API_docs/types/account.WallPapers.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_WallPapers = $MadelineProto->account->getWallPapers(hash: [$long|string, $long|string], );
```

