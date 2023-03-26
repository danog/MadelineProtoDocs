---
title: "stickers.changeSticker"
description: "stickers.changeSticker parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_changeSticker.html
---
# Method: stickers.changeSticker
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Optional|
|emoji|[string](/API_docs/types/string.html) | Optional|
|mask\_coords|[MaskCoords](/API_docs/types/MaskCoords.html) | Optional|
|keywords|[string](/API_docs/types/string.html) | Optional|


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

$messages_StickerSet = $MadelineProto->stickers->changeSticker(sticker: InputDocument, emoji: 'string', mask_coords: MaskCoords, keywords: 'string', );
```

