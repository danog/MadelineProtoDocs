---
title: "stickers.changeStickerPosition"
description: "Changes the absolute position of a sticker in the set to which it belongs. The sticker set must have been created by the current user/bot."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_changeStickerPosition.html
---
# Method: stickers.changeStickerPosition
[Back to methods index](index.html)



Changes the absolute position of a sticker in the set to which it belongs. The sticker set must have been created by the current user/bot.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | The sticker | Optional|
|position|[int](/API_docs/types/int.html) | The new position of the sticker, zero-based | Optional|


### Return type: [messages.StickerSet](/API_docs/types/messages.StickerSet.html)

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

$messages_StickerSet = $MadelineProto->stickers->changeStickerPosition(sticker: $InputDocument, position: $int, );
```

