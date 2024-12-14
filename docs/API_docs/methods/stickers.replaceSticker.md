---
title: "stickers.replaceSticker"
description: "stickers.replaceSticker parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_replaceSticker.html
---
# Method: stickers.replaceSticker
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Optional|
|new\_sticker|[InputStickerSetItem](/API_docs/types/InputStickerSetItem.html) | Yes|


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

$messages_StickerSet = $MadelineProto->stickers->replaceSticker(sticker: $InputDocument, new_sticker: $InputStickerSetItem, );
```

