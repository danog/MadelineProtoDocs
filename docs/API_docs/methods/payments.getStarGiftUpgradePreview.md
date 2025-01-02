---
title: "payments.getStarGiftUpgradePreview"
description: "payments.getStarGiftUpgradePreview parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarGiftUpgradePreview.html
---
# Method: payments.getStarGiftUpgradePreview
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gift\_id|[long](/API_docs/types/long.html) | Yes|


### Return type: [payments.StarGiftUpgradePreview](/API_docs/types/payments.StarGiftUpgradePreview.html)

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

$payments_StarGiftUpgradePreview = $MadelineProto->payments->getStarGiftUpgradePreview(gift_id: $long, );
```

