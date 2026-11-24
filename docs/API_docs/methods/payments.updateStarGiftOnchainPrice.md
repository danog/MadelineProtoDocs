---
title: "payments.updateStarGiftOnchainPrice"
description: "payments.updateStarGiftOnchainPrice parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_updateStarGiftOnchainPrice.html
---
# Method: payments.updateStarGiftOnchainPrice
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|slug|[string](/API_docs/types/string.html) | Optional|
|amount|[long](/API_docs/types/long.html) | Yes|


### Return type: [payments.StarGiftOnchainSalePayload](/API_docs/types/payments.StarGiftOnchainSalePayload.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_StarGiftOnchainSalePayload = $MadelineProto->payments->updateStarGiftOnchainPrice(slug: 'string', amount: $long, );
```

