---
title: payments.getPaymentForm
description: Get payment form
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: payments.getPaymentForm  
[Back to methods index](index.md)


Get payment form

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|msg\_id|[int](../types/int.md) | Message ID | Yes|


### Return type: [payments\_PaymentForm](../types/payments_PaymentForm.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_PaymentForm = $MadelineProto->payments->getPaymentForm(['msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
payments_PaymentForm = payments.getPaymentForm({msg_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


