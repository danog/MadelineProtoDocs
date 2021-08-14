---
title: payments.validateRequestedInfo
description: Submit requested order information for validation
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_validateRequestedInfo.html
---
# Method: payments.validateRequestedInfo
[Back to methods index](index.md)



Submit requested order information for validation

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|save|[Bool](../types/Bool.md) | Save order information to re-use it for future orders | Optional|
|msg\_id|[int](../types/int.md) | Message ID of payment form | Yes|
|info|[PaymentRequestedInfo](../types/PaymentRequestedInfo.md) | Requested order information | Yes|


### Return type: [payments.ValidatedRequestedInfo](../types/payments.ValidatedRequestedInfo.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_ValidatedRequestedInfo = $MadelineProto->payments->validateRequestedInfo(['save' => Bool, 'msg_id' => int, 'info' => PaymentRequestedInfo, ]);
```

Or, if you're into Lua:

```lua
payments_ValidatedRequestedInfo = payments.validateRequestedInfo({save=Bool, msg_id=int, info=PaymentRequestedInfo, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


