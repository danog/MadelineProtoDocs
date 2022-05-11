---
title: "help.getNearestDc"
description: "Returns info on data center nearest to the user."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getNearestDc.html
---
# Method: help.getNearestDc
[Back to methods index](index.html)



Returns info on data center nearest to the user.



### Return type: [NearestDc](/API_docs/types/NearestDc.html)

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
$NearestDc = $MadelineProto->help->getNearestDc();
```

