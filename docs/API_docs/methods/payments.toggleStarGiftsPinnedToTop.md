---
title: "payments.toggleStarGiftsPinnedToTop"
description: "Pins a received gift on top of the profile of the user or owned channels by using [payments.toggleStarGiftsPinnedToTop](../methods/payments.toggleStarGiftsPinnedToTop.html)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_toggleStarGiftsPinnedToTop.html
---
# Method: payments.toggleStarGiftsPinnedToTop
[Back to methods index](index.html)



Pins a received gift on top of the profile of the user or owned channels by using [payments.toggleStarGiftsPinnedToTop](../methods/payments.toggleStarGiftsPinnedToTop.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer where to pin the gift. | Optional|
|stargift|Array of [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | The gift to pin. | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->payments->toggleStarGiftsPinnedToTop(peer: $InputPeer, stargift: [$InputSavedStarGift, $InputSavedStarGift], );
```

