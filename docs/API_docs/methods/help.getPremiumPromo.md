---
title: "help.getPremiumPromo"
description: "Get Telegram Premium promotion information"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getPremiumPromo.html
---
# Method: help.getPremiumPromo
[Back to methods index](index.html)



Get Telegram Premium promotion information



### Return type: [help.PremiumPromo](/API_docs/types/help.PremiumPromo.html)

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

$help_PremiumPromo = $MadelineProto->help->getPremiumPromo();
```

