---
title: "help.getPromoData"
description: "Returns a set of useful suggestions and PSA/MTProxy sponsored peers, see [here »](https://core.telegram.org/api/config#suggestions) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/help_getPromoData.html
---
# Method: help.getPromoData
[Back to methods index](index.html)



Returns a set of useful suggestions and PSA/MTProxy sponsored peers, see [here »](https://core.telegram.org/api/config#suggestions) for more info.



### Return type: [help.PromoData](/API_docs/types/help.PromoData.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$help_PromoData = $MadelineProto->help->getPromoData();
```

