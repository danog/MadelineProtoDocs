---
title: "payments.updateStarGiftCollection"
description: "payments.updateStarGiftCollection parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_updateStarGiftCollection.html
---
# Method: payments.updateStarGiftCollection
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|collection\_id|[int](/API_docs/types/int.html) | Optional|
|title|[string](/API_docs/types/string.html) | Optional|
|delete\_stargift|Array of [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Optional|
|add\_stargift|Array of [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Optional|
|order|Array of [InputSavedStarGift](/API_docs/types/InputSavedStarGift.html) | Optional|


### Return type: [StarGiftCollection](/API_docs/types/StarGiftCollection.html)

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

$StarGiftCollection = $MadelineProto->payments->updateStarGiftCollection(peer: $InputPeer, collection_id: $int, title: 'string', delete_stargift: [$InputSavedStarGift, $InputSavedStarGift], add_stargift: [$InputSavedStarGift, $InputSavedStarGift], order: [$InputSavedStarGift, $InputSavedStarGift], );
```

