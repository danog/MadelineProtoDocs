---
title: "payments.getResaleStarGifts"
description: "payments.getResaleStarGifts parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getResaleStarGifts.html
---
# Method: payments.getResaleStarGifts
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|sort\_by\_price|[Bool](/API_docs/types/Bool.html) | Optional|
|sort\_by\_num|[Bool](/API_docs/types/Bool.html) | Optional|
|attributes\_hash|[long](/API_docs/types/long.html) | Optional|
|gift\_id|[long](/API_docs/types/long.html) | Yes|
|attributes|Array of [StarGiftAttributeId](/API_docs/types/StarGiftAttributeId.html) | Optional|
|offset|[string](/API_docs/types/string.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|


### Return type: [payments.ResaleStarGifts](/API_docs/types/payments.ResaleStarGifts.html)

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

$payments_ResaleStarGifts = $MadelineProto->payments->getResaleStarGifts(sort_by_price: $Bool, sort_by_num: $Bool, attributes_hash: $long, gift_id: $long, attributes: [$StarGiftAttributeId, $StarGiftAttributeId], offset: 'string', limit: $int, );
```

