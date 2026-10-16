---
title: "wallet.getTransactions"
description: "wallet.getTransactions parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/wallet_getTransactions.html
---
# Method: wallet.getTransactions
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|inbound|[Bool](/API_docs/types/Bool.html) | Optional|
|outbound|[Bool](/API_docs/types/Bool.html) | Optional|
|offset|[string](/API_docs/types/string.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|


### Return type: [wallet.Transactions](/API_docs/types/wallet.Transactions.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$wallet_Transactions = $MadelineProto->wallet->getTransactions(inbound: $Bool, outbound: $Bool, offset: 'string', limit: $int, );
```

