---
title: "payments.updateStarGiftPrice"
description: "payments.updateStarGiftPrice parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_updateStarGiftPrice.html
---
# Method: payments.updateStarGiftPrice
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Yes|
|resell\_stars|[long](/API_docs/types/long.html) | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->payments->updateStarGiftPrice(stargift: $InputSavedStarGift, resell_stars: $long, );
```

