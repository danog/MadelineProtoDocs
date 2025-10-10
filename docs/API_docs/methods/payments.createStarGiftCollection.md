---
title: "payments.createStarGiftCollection"
description: "Create a [star gift collection »](https://core.telegram.org/api/gifts#gift-collections)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_createStarGiftCollection.html
---
# Method: payments.createStarGiftCollection
[Back to methods index](index.html)



Create a [star gift collection »](https://core.telegram.org/api/gifts#gift-collections).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where to create the collection. | Optional|
|title|[string](/API_docs/types/string.html) | Title of the collection. | Optional|
|stargift|Array of [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Gifts added to the collection. | Yes|


### Return type: [StarGiftCollection](/API_docs/types/StarGiftCollection.html)

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

$StarGiftCollection = $MadelineProto->payments->createStarGiftCollection(peer: $InputPeer, title: 'string', stargift: [$InputSavedStarGift, $InputSavedStarGift], );
```

