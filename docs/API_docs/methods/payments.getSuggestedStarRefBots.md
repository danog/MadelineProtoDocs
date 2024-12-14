---
title: "payments.getSuggestedStarRefBots"
description: "payments.getSuggestedStarRefBots parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getSuggestedStarRefBots.html
---
# Method: payments.getSuggestedStarRefBots
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|order\_by\_revenue|[Bool](/API_docs/types/Bool.html) | Optional|
|order\_by\_date|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|offset|[string](/API_docs/types/string.html) | Optional|
|limit|[int](/API_docs/types/int.html) | Optional|


### Return type: [payments.SuggestedStarRefBots](/API_docs/types/payments.SuggestedStarRefBots.html)

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

$payments_SuggestedStarRefBots = $MadelineProto->payments->getSuggestedStarRefBots(order_by_revenue: $Bool, order_by_date: $Bool, peer: $InputPeer, offset: 'string', limit: $int, );
```

