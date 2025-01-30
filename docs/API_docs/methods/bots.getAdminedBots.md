---
title: "bots.getAdminedBots"
description: "Get a list of bots owned by the current user"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/bots_getAdminedBots.html
---
# Method: bots.getAdminedBots
[Back to methods index](index.html)



Get a list of bots owned by the current user



### Return type: [Vector\_of\_User](/API_docs/types/User.html)

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

$Vector_of_User = $MadelineProto->bots->getAdminedBots();
```

