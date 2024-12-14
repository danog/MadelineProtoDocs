---
title: "help.getSupportName"
description: "Get localized name of the telegram support user"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getSupportName.html
---
# Method: help.getSupportName
[Back to methods index](index.html)



Get localized name of the telegram support user



### Return type: [help.SupportName](/API_docs/types/help.SupportName.html)

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

$help_SupportName = $MadelineProto->help->getSupportName();
```

