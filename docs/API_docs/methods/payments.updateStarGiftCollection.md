---
title: "payments.updateStarGiftCollection"
description: "Add or remove gifts from a [star gift collection »](https://core.telegram.org/api/gifts#gift-collections), or rename the collection."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_updateStarGiftCollection.html
---
# Method: payments.updateStarGiftCollection
[Back to methods index](index.html)



Add or remove gifts from a [star gift collection »](https://core.telegram.org/api/gifts#gift-collections), or rename the collection.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer that owns the collection. | Optional|
|collection\_id|[int](/API_docs/types/int.html) | Collection ID. | Optional|
|title|[string](/API_docs/types/string.html) | Title of the collection, to rename the collection. | Optional|
|delete\_stargift|Array of [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Can contain a list of gifts to remove from the collection. | Optional|
|add\_stargift|Array of [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Can contain a list of gifts to add to the collection. | Optional|
|order|Array of [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Can contain the new gift order. | Optional|


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

$StarGiftCollection = $MadelineProto->payments->updateStarGiftCollection(peer: $InputPeer, collection_id: $int, title: 'string', delete_stargift: [$InputSavedStarGift, $InputSavedStarGift], add_stargift: [$InputSavedStarGift, $InputSavedStarGift], order: [$InputSavedStarGift, $InputSavedStarGift], );
```

