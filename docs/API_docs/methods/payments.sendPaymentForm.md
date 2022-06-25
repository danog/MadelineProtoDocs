---
title: "payments.sendPaymentForm"
description: "Send compiled payment form"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_sendPaymentForm.html
---
# Method: payments.sendPaymentForm
[Back to methods index](index.html)



Send compiled payment form

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|form\_id|[long](/API_docs/types/long.html) | Form ID | Yes|
|invoice|[InputInvoice](/API_docs/types/InputInvoice.html) |  | Yes|
|requested\_info\_id|[string](/API_docs/types/string.html) | ID of saved and validated [order info](../constructors/payments.validatedRequestedInfo.html) | Optional|
|shipping\_option\_id|[string](/API_docs/types/string.html) | Chosen shipping option ID | Optional|
|credentials|[InputPaymentCredentials](/API_docs/types/InputPaymentCredentials.html) | Payment credentials | Yes|
|tip\_amount|[long](/API_docs/types/long.html) | Tip, in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). | Optional|


### Return type: [payments.PaymentResult](/API_docs/types/payments.PaymentResult.html)

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
$payments_PaymentResult = $MadelineProto->payments->sendPaymentForm(form_id: long, invoice: InputInvoice, requested_info_id: 'string', shipping_option_id: 'string', credentials: InputPaymentCredentials, tip_amount: long, );
```

