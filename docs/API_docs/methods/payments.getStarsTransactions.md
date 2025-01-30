---
title: "payments.getStarsTransactions"
description: "Fetch [Telegram Stars transactions](https://core.telegram.org/api/stars#balance-and-transaction-history)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarsTransactions.html
---
# Method: payments.getStarsTransactions
[Back to methods index](index.html)



Fetch [Telegram Stars transactions](https://core.telegram.org/api/stars#balance-and-transaction-history).

The `inbound` and `outbound` flags are mutually exclusive: if none of the two are set, both incoming and outgoing transactions are fetched.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|inbound|[Bool](/API_docs/types/Bool.html) | If set, fetches only incoming transactions. | Optional|
|outbound|[Bool](/API_docs/types/Bool.html) | If set, fetches only outgoing transactions. | Optional|
|ascending|[Bool](/API_docs/types/Bool.html) | Return transactions in ascending order by date (instead of descending order by date). | Optional|
|subscription\_id|[string](/API_docs/types/string.html) | If set, fetches only transactions for the specified [Telegram Star subscription »](https://core.telegram.org/api/stars#star-subscriptions). | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Fetch the transaction history of the peer ([inputPeerSelf](../constructors/inputPeerSelf.html) or a bot we own). | Optional|
|offset|[string](/API_docs/types/string.html) | [Offset for pagination, obtained from the returned `next_offset`, initially an empty string »](https://core.telegram.org/api/offsets). | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [payments.StarsStatus](/API_docs/types/payments.StarsStatus.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_StarsStatus = $MadelineProto->payments->getStarsTransactions(inbound: $Bool, outbound: $Bool, ascending: $Bool, subscription_id: 'string', peer: $InputPeer, offset: 'string', limit: $int, );
```

