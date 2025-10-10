---
title: "payments.updateStarGiftPrice"
description: "A [collectible gift we own »](https://core.telegram.org/api/gifts#collectible-gifts) can be put up for sale on the [gift marketplace »](https://telegram.org/blog/gift-marketplace-and-more) with this method, see [here »](https://core.telegram.org/api/gifts#reselling-collectible-gifts) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_updateStarGiftPrice.html
---
# Method: payments.updateStarGiftPrice
[Back to methods index](index.html)



A [collectible gift we own »](https://core.telegram.org/api/gifts#collectible-gifts) can be put up for sale on the [gift marketplace »](https://telegram.org/blog/gift-marketplace-and-more) with this method, see [here »](https://core.telegram.org/api/gifts#reselling-collectible-gifts) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | The gift to resell. | Yes|
|resell\_amount|[StarsAmount](/API_docs/types/StarsAmount.html) | Resale price of the gift. | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->payments->updateStarGiftPrice(stargift: $InputSavedStarGift, resell_amount: $StarsAmount, );
```

