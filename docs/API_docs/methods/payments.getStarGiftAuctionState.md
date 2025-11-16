---
title: "payments.getStarGiftAuctionState"
description: "payments.getStarGiftAuctionState parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarGiftAuctionState.html
---
# Method: payments.getStarGiftAuctionState
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|auction|[InputStarGiftAuction](/API_docs/types/InputStarGiftAuction.html) | Yes|
|version|[int](/API_docs/types/int.html) | Optional|


### Return type: [payments.StarGiftAuctionState](/API_docs/types/payments.StarGiftAuctionState.html)

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

$payments_StarGiftAuctionState = $MadelineProto->payments->getStarGiftAuctionState(auction: $InputStarGiftAuction, version: $int, );
```

