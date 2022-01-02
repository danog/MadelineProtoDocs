---
title: "stickers.setStickerSetThumb"
description: "Set stickerset thumbnail"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_setStickerSetThumb.html
---
# Method: stickers.setStickerSetThumb
[Back to methods index](index.md)



Set stickerset thumbnail

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Stickerset | Optional|
|thumb|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | Thumbnail | Optional|


### Return type: [messages.StickerSet](../types/messages.StickerSet.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StickerSet = $MadelineProto->stickers->setStickerSetThumb(['stickerset' => InputStickerSet, 'thumb' => InputDocument, ]);
```

Or, if you're into Lua:

```lua
messages_StickerSet = stickers.setStickerSetThumb({stickerset=InputStickerSet, thumb=InputDocument, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|STICKER_THUMB_PNG_NOPNG|Incorrect stickerset thumb file provided, PNG / WEBP expected.|
|400|STICKER_THUMB_TGS_NOTGS|Incorrect stickerset TGS thumb file provided.|
|400|STICKERSET_INVALID|The provided sticker set is invalid|


