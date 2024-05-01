---
title: "stickers.changeSticker"
description: "Update the keywords, emojis or [mask coordinates](https://core.telegram.org/api/stickers#mask-stickers) of a sticker, bots only."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_changeSticker.html
---
# Method: stickers.changeSticker
[Back to methods index](index.html)



Update the keywords, emojis or [mask coordinates](https://core.telegram.org/api/stickers#mask-stickers) of a sticker, bots only.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | The sticker | Optional|
|emoji|[string](/API_docs/types/string.html) | If set, updates the emoji list associated to the sticker | Optional|
|mask\_coords|[MaskCoords](/API_docs/types/MaskCoords.html) | If set, updates the [mask coordinates](https://core.telegram.org/api/stickers#mask-stickers) | Optional|
|keywords|[string](/API_docs/types/string.html) | If set, updates the sticker keywords (separated by commas). Can't be provided for mask stickers. | Optional|


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

$messages_StickerSet = $MadelineProto->stickers->changeSticker(sticker: $InputDocument, emoji: 'string', mask_coords: $MaskCoords, keywords: 'string', );
```

