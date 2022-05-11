---
title: "messages.getAttachedStickers"
description: "Get stickers attached to a photo or video"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAttachedStickers.html
---
# Method: messages.getAttachedStickers
[Back to methods index](index.html)



Get stickers attached to a photo or video

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|media|[InputStickeredMedia](/API_docs/types/InputStickeredMedia.html) | Stickered media | Yes|


### Return type: [Vector\_of\_StickerSetCovered](/API_docs/types/StickerSetCovered.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Vector_of_StickerSetCovered = $MadelineProto->messages->getAttachedStickers(media: InputStickeredMedia, );
```

