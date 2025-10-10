---
title: "payments.deleteStarGiftCollection"
description: "Delete a [star gift collection »](https://core.telegram.org/api/gifts#gift-collections)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_deleteStarGiftCollection.html
---
# Method: payments.deleteStarGiftCollection
[Back to methods index](index.html)



Delete a [star gift collection »](https://core.telegram.org/api/gifts#gift-collections).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer that owns the collection. | Optional|
|collection\_id|[int](/API_docs/types/int.html) | ID of the collection. | Optional|


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

$Bool = $MadelineProto->payments->deleteStarGiftCollection(peer: $InputPeer, collection_id: $int, );
```

