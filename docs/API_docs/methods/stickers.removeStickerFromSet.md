---
title: stickers.removeStickerFromSet
description: Remove a sticker from the set where it belongs, bots only. The sticker set must have been created by the bot.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: stickers.removeStickerFromSet  
[Back to methods index](index.md)


Remove a sticker from the set where it belongs, bots only. The sticker set must have been created by the bot.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | The sticker to remove | Optional|


### Return type: [messages\_StickerSet](../types/messages_StickerSet.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StickerSet = $MadelineProto->stickers->removeStickerFromSet(['sticker' => InputDocument, ]);
```

Or, if you're into Lua:

```lua
messages_StickerSet = stickers.removeStickerFromSet({sticker=InputDocument, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BOT_MISSING|This method can only be run by a bot|
|400|STICKER_INVALID|The provided sticker is invalid|


