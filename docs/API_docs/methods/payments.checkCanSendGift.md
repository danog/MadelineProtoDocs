---
title: "payments.checkCanSendGift"
description: "Check if the specified [gift »](https://core.telegram.org/api/gifts) can be sent."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_checkCanSendGift.html
---
# Method: payments.checkCanSendGift
[Back to methods index](index.html)



Check if the specified [gift »](https://core.telegram.org/api/gifts) can be sent.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|gift\_id|[long](/API_docs/types/long.html) | Gift ID. | Yes|


### Return type: [payments.CheckCanSendGiftResult](/API_docs/types/payments.CheckCanSendGiftResult.html)

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

$payments_CheckCanSendGiftResult = $MadelineProto->payments->checkCanSendGift(gift_id: $long, );
```

