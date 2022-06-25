---
title: "payments.getPaymentForm"
description: "Get a payment form"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getPaymentForm.html
---
# Method: payments.getPaymentForm
[Back to methods index](index.html)



Get a payment form

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|invoice|[InputInvoice](/API_docs/types/InputInvoice.html) |  | Yes|
|theme\_params|[DataJSON](/API_docs/types/DataJSON.html) | A JSON object with the following keys, containing color theme information (integers, RGB24) to pass to the payment provider, to apply in eventual verification pages: <br>`bg_color` \- Background color <br>`text_color` \- Text color <br>`hint_color` \- Hint text color <br>`link_color` \- Link color <br>`button_color` \- Button color <br>`button_text_color` \- Button text color | Optional|


### Return type: [payments.PaymentForm](/API_docs/types/payments.PaymentForm.html)

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
$payments_PaymentForm = $MadelineProto->payments->getPaymentForm(invoice: InputInvoice, theme_params: DataJSON, );
```

