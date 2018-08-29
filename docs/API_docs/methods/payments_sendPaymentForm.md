---
title: payments.sendPaymentForm
description: Bots only: send payment form
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: payments.sendPaymentForm  
[Back to methods index](index.md)


Bots only: send payment form

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|msg\_id|[int](../types/int.md) | Message ID | Yes|
|requested\_info\_id|[string](../types/string.md) | ID of requested info | Optional|
|shipping\_option\_id|[string](../types/string.md) | Shipping option ID | Optional|
|credentials|[InputPaymentCredentials](../types/InputPaymentCredentials.md) | Payment credentials | Yes|


### Return type: [payments\_PaymentResult](../types/payments_PaymentResult.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_PaymentResult = $MadelineProto->payments->sendPaymentForm(['msg_id' => int, 'requested_info_id' => 'string', 'shipping_option_id' => 'string', 'credentials' => InputPaymentCredentials, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/payments.sendPaymentForm`

Parameters:

msg_id - Json encoded int

requested_info_id - Json encoded string

shipping_option_id - Json encoded string

credentials - Json encoded InputPaymentCredentials




Or, if you're into Lua:

```
payments_PaymentResult = payments.sendPaymentForm({msg_id=int, requested_info_id='string', shipping_option_id='string', credentials=InputPaymentCredentials, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|MESSAGE_ID_INVALID|The provided message id is invalid|


