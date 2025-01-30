---
title: "payments.sendStarsForm"
description: "Make a payment using [Telegram Stars, see here »](https://core.telegram.org/api/stars#using-stars) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_sendStarsForm.html
---
# Method: payments.sendStarsForm
[Back to methods index](index.html)



Make a payment using [Telegram Stars, see here »](https://core.telegram.org/api/stars#using-stars) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|form\_id|[long](/API_docs/types/long.html) | Payment form ID | Yes|
|invoice|[InputInvoice](/API_docs/types/InputInvoice.html) | Invoice | Yes|


### Return type: [payments.PaymentResult](/API_docs/types/payments.PaymentResult.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_PaymentResult = $MadelineProto->payments->sendStarsForm(form_id: $long, invoice: $InputInvoice, );
```

