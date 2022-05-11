---
title: "payments.getBankCardData"
description: "Get info about a credit card"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getBankCardData.html
---
# Method: payments.getBankCardData
[Back to methods index](index.html)



Get info about a credit card

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|number|[string](/API_docs/types/string.html) | Credit card number | Yes|


### Return type: [payments.BankCardData](/API_docs/types/payments.BankCardData.html)

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
$payments_BankCardData = $MadelineProto->payments->getBankCardData(number: 'string', );
```

