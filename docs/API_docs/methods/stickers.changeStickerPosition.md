---
title: "stickers.changeStickerPosition"
description: "Changes the absolute position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_changeStickerPosition.html
---
# Method: stickers.changeStickerPosition
[Back to methods index](index.html)



Changes the absolute position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | The sticker | Optional|
|position|[int](/API_docs/types/int.html) | The new position of the sticker, zero-based | Yes|


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
$messages_StickerSet = $MadelineProto->stickers->changeStickerPosition(sticker: InputDocument, position: int, );
```

