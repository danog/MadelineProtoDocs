---
title: stickers.changeStickerPosition
description: Changes the absolute position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: stickers.changeStickerPosition  
[Back to methods index](index.md)


Changes the absolute position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | The sticker | Optional|
|position|[int](../types/int.md) | The new position of the sticker, zero-based | Yes|


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

$messages.StickerSet = $MadelineProto->stickers->changeStickerPosition(['sticker' => InputDocument, 'position' => int, ]);
```

Or, if you're into Lua:

```lua
messages.StickerSet = stickers.changeStickerPosition({sticker=InputDocument, position=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BOT_MISSING|This method can only be run by a bot|
|400|STICKER_INVALID|The provided sticker is invalid|


