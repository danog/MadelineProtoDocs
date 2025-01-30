---
title: "stats.getBroadcastRevenueWithdrawalUrl"
description: "Withdraw funds from a channel's [ad revenue balance »](https://core.telegram.org/api/revenue)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getBroadcastRevenueWithdrawalUrl.html
---
# Method: stats.getBroadcastRevenueWithdrawalUrl
[Back to methods index](index.html)



Withdraw funds from a channel's [ad revenue balance »](https://core.telegram.org/api/revenue).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Get ad revenue withdrawal URL for the specified channel or bot | Optional|
|password|[InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html) | 2FA password, see [here »](https://core.telegram.org/api/srp#using-the-2fa-password) for more info. | Yes|


### Return type: [stats.BroadcastRevenueWithdrawalUrl](/API_docs/types/stats.BroadcastRevenueWithdrawalUrl.html)

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

$stats_BroadcastRevenueWithdrawalUrl = $MadelineProto->stats->getBroadcastRevenueWithdrawalUrl(peer: $InputPeer, password: $InputCheckPasswordSRP, );
```

