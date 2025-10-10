---
title: "payments.transferStarGift"
description: "Transfer a [collectible gift](https://core.telegram.org/api/gifts#collectible-gifts) to another user or channel: can only be used if transfer is free (i.e. [messageActionStarGiftUnique](../constructors/messageActionStarGiftUnique.html).`transfer_stars` is not set); see [here »](https://core.telegram.org/api/gifts#transferring-collectible-gifts) for more info on the full flow (including the different flow to use in case the transfer isn't free)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_transferStarGift.html
---
# Method: payments.transferStarGift
[Back to methods index](index.html)



Transfer a [collectible gift](https://core.telegram.org/api/gifts#collectible-gifts) to another user or channel: can only be used if transfer is free (i.e. [messageActionStarGiftUnique](../constructors/messageActionStarGiftUnique.html).`transfer_stars` is not set); see [here »](https://core.telegram.org/api/gifts#transferring-collectible-gifts) for more info on the full flow (including the different flow to use in case the transfer isn't free).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stargift|[InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | The gift to transfer. | Yes|
|to\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Destination peer. | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->payments->transferStarGift(stargift: $InputSavedStarGift, to_id: $InputPeer, );
```

