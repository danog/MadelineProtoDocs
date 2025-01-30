---
title: "stats.getBroadcastRevenueTransactions"
description: "Fetch [channel ad revenue transaction history »](https://core.telegram.org/api/revenue)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getBroadcastRevenueTransactions.html
---
# Method: stats.getBroadcastRevenueTransactions
[Back to methods index](index.html)



Fetch [channel ad revenue transaction history »](https://core.telegram.org/api/revenue).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Get ad revenue transactions for the specified channel or bot | Optional|
|offset|[int](/API_docs/types/int.html) | [Offset for pagination](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [stats.BroadcastRevenueTransactions](/API_docs/types/stats.BroadcastRevenueTransactions.html)

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

$stats_BroadcastRevenueTransactions = $MadelineProto->stats->getBroadcastRevenueTransactions(peer: $InputPeer, offset: $int, limit: $int, );
```

