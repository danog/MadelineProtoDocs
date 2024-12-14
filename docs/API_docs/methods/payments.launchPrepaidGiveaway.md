---
title: "payments.launchPrepaidGiveaway"
description: "Launch a [prepaid giveaway »](https://core.telegram.org/api/giveaways)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_launchPrepaidGiveaway.html
---
# Method: payments.launchPrepaidGiveaway
[Back to methods index](index.html)



Launch a [prepaid giveaway »](https://core.telegram.org/api/giveaways).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer where to launch the giveaway. | Optional|
|giveaway\_id|[long](/API_docs/types/long.html) | The prepaid giveaway ID. | Yes|
|purpose|[InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html) | Giveway parameters | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->payments->launchPrepaidGiveaway(peer: $InputPeer, giveaway_id: $long, purpose: $InputStorePaymentPurpose, );
```

