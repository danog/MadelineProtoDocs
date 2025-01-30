---
title: "payments.getSavedStarGift"
description: "payments.getSavedStarGift parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getSavedStarGift.html
---
# Method: payments.getSavedStarGift
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stargift|Array of [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Yes|


### Return type: [payments.SavedStarGifts](/API_docs/types/payments.SavedStarGifts.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_SavedStarGifts = $MadelineProto->payments->getSavedStarGift(stargift: [$InputSavedStarGift, $InputSavedStarGift], );
```

