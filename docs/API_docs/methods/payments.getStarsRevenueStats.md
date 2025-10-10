---
title: "payments.getStarsRevenueStats"
description: "Get [Telegram Star revenue statistics »](https://core.telegram.org/api/stars)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarsRevenueStats.html
---
# Method: payments.getStarsRevenueStats
[Back to methods index](index.html)



Get [Telegram Star revenue statistics »](https://core.telegram.org/api/stars).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|dark|[Bool](/API_docs/types/Bool.html) | Whether to enable dark theme for graph colors | Optional|
|ton|[Bool](/API_docs/types/Bool.html) | If set, fetches channel/bot ad revenue statistics in TON. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Get statistics for the specified bot, channel or ourselves ([inputPeerSelf](../constructors/inputPeerSelf.html)). | Optional|


### Return type: [payments.StarsRevenueStats](/API_docs/types/payments.StarsRevenueStats.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$payments_StarsRevenueStats = $MadelineProto->payments->getStarsRevenueStats(dark: $Bool, ton: $Bool, peer: $InputPeer, );
```

