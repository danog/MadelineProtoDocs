---
title: "payments.getPaymentReceipt"
description: "Get payment receipt"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getPaymentReceipt.html
---
# Method: payments.getPaymentReceipt
[Back to methods index](index.md)



Get payment receipt

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) |  | Optional|
|msg\_id|[int](../types/int.md) | Message ID of receipt | Yes|


### Return type: [payments.PaymentReceipt](../types/payments.PaymentReceipt.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_PaymentReceipt = $MadelineProto->payments->getPaymentReceipt(['peer' => InputPeer, 'msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
payments_PaymentReceipt = payments.getPaymentReceipt({peer=InputPeer, msg_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


