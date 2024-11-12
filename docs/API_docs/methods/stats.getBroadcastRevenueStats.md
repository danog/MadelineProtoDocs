---
title: "stats.getBroadcastRevenueStats"
description: "stats.getBroadcastRevenueStats parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getBroadcastRevenueStats.html
---
# Method: stats.getBroadcastRevenueStats
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dark|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|


### Return type: [stats.BroadcastRevenueStats](/API_docs/types/stats.BroadcastRevenueStats.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stats_BroadcastRevenueStats = $MadelineProto->stats->getBroadcastRevenueStats(dark: $Bool, peer: $InputPeer, );
```

