---
title: "payments.getStarGiftCollections"
description: "Fetches all [star gift collections »](https://core.telegram.org/api/gifts#gift-collections) of a peer."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_getStarGiftCollections.html
---
# Method: payments.getStarGiftCollections
[Back to methods index](index.html)



Fetches all [star gift collections »](https://core.telegram.org/api/gifts#gift-collections) of a peer.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer. | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | Hash ([generated as specified here »](https://core.telegram.org/api/offsets#hash-generation)) using the [starGiftCollection](../constructors/starGiftCollection.html).`hash` field (**not** the `collection_id` field) of all collections returned by a previous method call, to avoid refetching the result if it hasn't changed. | Optional|


### Return type: [payments.StarGiftCollections](/API_docs/types/payments.StarGiftCollections.html)

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

$payments_StarGiftCollections = $MadelineProto->payments->getStarGiftCollections(peer: $InputPeer, hash: [$long\|string, $long\|string], );
```

