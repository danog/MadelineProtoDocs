---
title: "stickers.setStickerSetThumb"
description: "Set stickerset thumbnail"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_setStickerSetThumb.html
---
# Method: stickers.setStickerSetThumb
[Back to methods index](index.html)



Set stickerset thumbnail

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Stickerset | Optional|
|thumb|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Thumbnail | Optional|


### Return type: [messages.StickerSet](/API_docs/types/messages.StickerSet.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_StickerSet = $MadelineProto->stickers->setStickerSetThumb(stickerset: InputStickerSet, thumb: InputDocument, );
```

