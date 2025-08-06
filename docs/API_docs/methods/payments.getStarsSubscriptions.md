---
title: "payments.getStarsSubscriptions"
description: "Obtain a list of active, expired or cancelled [Telegram Star subscriptions »](https://core.telegram.org/api/invites#paid-invite-links)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarsSubscriptions.html
---
# Method: payments.getStarsSubscriptions
[Back to methods index](index.html)



Obtain a list of active, expired or cancelled [Telegram Star subscriptions »](https://core.telegram.org/api/invites#paid-invite-links).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|missing\_balance|[Bool](/API_docs/types/Bool.html) | Whether to return only subscriptions expired due to an excessively low Telegram Star balance. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Always pass [inputPeerSelf](../constructors/inputPeerSelf.html). | Optional|
|offset|[string](/API_docs/types/string.html) | Offset for pagination, taken from [payments.starsStatus](../constructors/payments.starsStatus.html).`subscriptions_next_offset`. | Optional|


### Return type: [payments.StarsStatus](/API_docs/types/payments.StarsStatus.html)

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

$payments_StarsStatus = $MadelineProto->payments->getStarsSubscriptions(missing_balance: $Bool, peer: $InputPeer, offset: 'string', );
```

