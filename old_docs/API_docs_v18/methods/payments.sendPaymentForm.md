---
title: payments.sendPaymentForm
description: Send compiled payment form
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_sendPaymentForm.html
---
# Method: payments.sendPaymentForm
[Back to methods index](index.md)



Send compiled payment form

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|msg\_id|[int](../types/int.md) | Message ID of form | Yes|
|requested\_info\_id|[string](../types/string.md) | ID of saved and validated [order info](../constructors/payments.validatedRequestedInfo.md) | Optional|
|shipping\_option\_id|[string](../types/string.md) | Chosen shipping option ID | Optional|
|credentials|[InputPaymentCredentials](../types/InputPaymentCredentials.md) | Payment credentials | Yes|


### Return type: [payments.PaymentResult](../types/payments.PaymentResult.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_PaymentResult = $MadelineProto->payments->sendPaymentForm(['msg_id' => int, 'requested_info_id' => 'string', 'shipping_option_id' => 'string', 'credentials' => InputPaymentCredentials, ]);
```

Or, if you're into Lua:

```lua
payments_PaymentResult = payments.sendPaymentForm({msg_id=int, requested_info_id='string', shipping_option_id='string', credentials=InputPaymentCredentials, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


