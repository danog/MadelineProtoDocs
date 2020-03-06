---
title: payments.getPaymentForm
description: Get a payment form
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getPaymentForm.html
---
# Method: payments.getPaymentForm  
[Back to methods index](index.md)


Get a payment form

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|msg\_id|[int](../types/int.md) | Message ID of payment form | Yes|


### Return type: [payments.PaymentForm](../types/payments.PaymentForm.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments.PaymentForm = $MadelineProto->payments->getPaymentForm(['msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
payments.PaymentForm = payments.getPaymentForm({msg_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


