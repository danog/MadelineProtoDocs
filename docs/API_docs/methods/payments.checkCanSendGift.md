---
title: "payments.checkCanSendGift"
description: "payments.checkCanSendGift parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_checkCanSendGift.html
---
# Method: payments.checkCanSendGift
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gift\_id|[long](/API_docs/types/long.html) | Yes|


### Return type: [payments.CheckCanSendGiftResult](/API_docs/types/payments.CheckCanSendGiftResult.html)

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

$payments_CheckCanSendGiftResult = $MadelineProto->payments->checkCanSendGift(gift_id: $long, );
```

