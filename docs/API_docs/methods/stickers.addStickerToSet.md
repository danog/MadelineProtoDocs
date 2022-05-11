---
title: "stickers.addStickerToSet"
description: "Add a sticker to a stickerset, bots only. The sticker set must have been created by the bot."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_addStickerToSet.html
---
# Method: stickers.addStickerToSet
[Back to methods index](index.html)



Add a sticker to a stickerset, bots only. The sticker set must have been created by the bot.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | The stickerset | Optional|
|sticker|[InputStickerSetItem](/API_docs/types/InputStickerSetItem.html) | The sticker | Yes|


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
$messages_StickerSet = $MadelineProto->stickers->addStickerToSet(stickerset: InputStickerSet, sticker: InputStickerSetItem, );
```

