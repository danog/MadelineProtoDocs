---
title: "help.getPremiumPromo"
description: "help.getPremiumPromo parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getPremiumPromo.html
---
# Method: help.getPremiumPromo
[Back to methods index](index.html)





### Return type: [help.PremiumPromo](/API_docs/types/help.PremiumPromo.html)

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
$help_PremiumPromo = $MadelineProto->help->getPremiumPromo();
```

