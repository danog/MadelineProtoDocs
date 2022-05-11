---
title: "payments.getPaymentReceipt"
description: "Get payment receipt"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getPaymentReceipt.html
---
# Method: payments.getPaymentReceipt
[Back to methods index](index.html)



Get payment receipt

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer where the payment receipt was sent | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Message ID of receipt | Yes|


### Return type: [payments.PaymentReceipt](/API_docs/types/payments.PaymentReceipt.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$payments_PaymentReceipt = $MadelineProto->payments->getPaymentReceipt(peer: InputPeer, msg_id: int, );
```

