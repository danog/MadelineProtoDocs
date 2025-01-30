---
title: "payments.getStarsTransactionsByID"
description: "Obtain info about [Telegram Star transactions »](https://core.telegram.org/api/stars#balance-and-transaction-history) using specific transaction IDs."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarsTransactionsByID.html
---
# Method: payments.getStarsTransactionsByID
[Back to methods index](index.html)



Obtain info about [Telegram Star transactions »](https://core.telegram.org/api/stars#balance-and-transaction-history) using specific transaction IDs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Channel or bot. | Optional|
|id|Array of [InputStarsTransaction](/API_docs/types/InputStarsTransaction.html) | Transaction IDs. | Yes|


### Return type: [payments.StarsStatus](/API_docs/types/payments.StarsStatus.html)

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

$payments_StarsStatus = $MadelineProto->payments->getStarsTransactionsByID(peer: $InputPeer, id: [$InputStarsTransaction, $InputStarsTransaction], );
```

