---
title: "payments.reorderStarGiftCollections"
description: "Reorder the [star gift collections »](https://core.telegram.org/api/gifts#gift-collections) on an owned peer's profile."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_reorderStarGiftCollections.html
---
# Method: payments.reorderStarGiftCollections
[Back to methods index](index.html)



Reorder the [star gift collections »](https://core.telegram.org/api/gifts#gift-collections) on an owned peer's profile.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The owned peer. | Optional|
|order|Array of [int](/API_docs/types/int.html) | New collection order. | Yes|


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

$Bool = $MadelineProto->payments->reorderStarGiftCollections(peer: $InputPeer, order: [$int, $int], );
```

