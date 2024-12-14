---
title: "payments.assignAppStoreTransaction"
description: "Informs server about a purchase made through the App Store: for official applications only."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_assignAppStoreTransaction.html
---
# Method: payments.assignAppStoreTransaction
[Back to methods index](index.html)



Informs server about a purchase made through the App Store: for official applications only.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|receipt|[bytes](/API_docs/types/bytes.html) | Receipt | Yes|
|purpose|[InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html) | Payment purpose | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->payments->assignAppStoreTransaction(receipt: 'bytes', purpose: $InputStorePaymentPurpose, );
```

