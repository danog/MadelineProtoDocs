---
title: "messages.reorderStickerSets"
description: "Reorder installed stickersets"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_reorderStickerSets.html
---
# Method: messages.reorderStickerSets
[Back to methods index](index.md)



Reorder installed stickersets

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|masks|[Bool](../types/Bool.md) | Reorder mask stickersets | Optional|
|order|Array of [long](../types/long.md) | New stickerset order by stickerset IDs | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->reorderStickerSets(['masks' => Bool, 'order' => [long, long], ]);
```

