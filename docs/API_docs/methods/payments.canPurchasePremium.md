---
title: "payments.canPurchasePremium"
description: "Checks whether Telegram Premium purchase is possible. Must be called before in-store Premium purchase, official apps only."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_canPurchasePremium.html
---
# Method: payments.canPurchasePremium
[Back to methods index](index.html)



Checks whether Telegram Premium purchase is possible. Must be called before in-store Premium purchase, official apps only.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|purpose|[InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html) | Payment purpose | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->payments->canPurchasePremium(purpose: $InputStorePaymentPurpose, );
```

