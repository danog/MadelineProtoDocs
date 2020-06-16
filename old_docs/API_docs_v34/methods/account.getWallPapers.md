---
title: account.getWallPapers
description: Returns a list of available wallpapers.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getWallPapers.html
---
# Method: account.getWallPapers
[Back to methods index](index.md)



Returns a list of available wallpapers.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [int](../types/int.md) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [account.WallPapers](../types/account.WallPapers.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account.WallPapers = $MadelineProto->account->getWallPapers(['hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
account.WallPapers = account.getWallPapers({hash={int}, })
```

