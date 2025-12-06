---
title: "payments.sendStarGiftOffer"
description: "payments.sendStarGiftOffer parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_sendStarGiftOffer.html
---
# Method: payments.sendStarGiftOffer
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|slug|[string](/API_docs/types/string.html) | Optional|
|price|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|
|duration|[int](/API_docs/types/int.html) | Optional|
|allow\_paid\_stars|[long](/API_docs/types/long.html) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->payments->sendStarGiftOffer(peer: $InputPeer, slug: 'string', price: $StarsAmount, duration: $int, allow_paid_stars: $long, );
```

