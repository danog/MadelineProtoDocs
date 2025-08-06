---
title: "payments.getSuggestedStarRefBots"
description: "Obtain a list of suggested [mini apps](https://core.telegram.org/api/bots/webapps) with available [affiliate programs](https://core.telegram.org/api/bots/referrals)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getSuggestedStarRefBots.html
---
# Method: payments.getSuggestedStarRefBots
[Back to methods index](index.html)



Obtain a list of suggested [mini apps](https://core.telegram.org/api/bots/webapps) with available [affiliate programs](https://core.telegram.org/api/bots/referrals)

`order_by_revenue` and `order_by_date` are mutually exclusive: if neither is set, results are sorted by profitability.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|order\_by\_revenue|[Bool](/API_docs/types/Bool.html) | If set, orders results by the expected revenue | Optional|
|order\_by\_date|[Bool](/API_docs/types/Bool.html) | If set, orders results by the creation date of the affiliate program | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer that will become the affiliate: star commissions will be transferred to this peer's star balance. | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for pagination, taken from [payments.suggestedStarRefBots](../constructors/payments.suggestedStarRefBots.html).`next_offset`, initially empty. | Optional|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Optional|


### Return type: [payments.SuggestedStarRefBots](/API_docs/types/payments.SuggestedStarRefBots.html)

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

$payments_SuggestedStarRefBots = $MadelineProto->payments->getSuggestedStarRefBots(order_by_revenue: $Bool, order_by_date: $Bool, peer: $InputPeer, offset: 'string', limit: $int, );
```

