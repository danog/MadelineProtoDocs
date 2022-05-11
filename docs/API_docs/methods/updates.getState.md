---
title: "updates.getState"
description: "You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getState.html
---
# Method: updates.getState
[Back to methods index](index.html)



You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates



### Return type: [updates.State](/API_docs/types/updates.State.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$updates_State = $MadelineProto->updates->getState();
```

