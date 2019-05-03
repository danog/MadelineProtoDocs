---
title: payments.getPaymentReceipt
description: Get payment receipt
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: payments.getPaymentReceipt  
[Back to methods index](index.md)


Get payment receipt

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|msg\_id|[int](../types/int.md) | The message ID | Yes|


### Return type: [payments\_PaymentReceipt](../types/payments_PaymentReceipt.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_PaymentReceipt = $MadelineProto->payments->getPaymentReceipt(['msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
payments_PaymentReceipt = payments.getPaymentReceipt({msg_id=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|MESSAGE_ID_INVALID|The provided message id is invalid|


