---
title: stickers.addStickerToSet
description: Add sticker to stickerset
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: stickers.addStickerToSet  
[Back to methods index](index.md)


Add sticker to stickerset

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | The stickerset | Optional|
|sticker|[InputStickerSetItem](../types/InputStickerSetItem.md) | The sticker | Yes|


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

$messages_StickerSet = $MadelineProto->stickers->addStickerToSet(['stickerset' => InputStickerSet, 'sticker' => InputStickerSetItem, ]);
```

Or, if you're into Lua:

```lua
messages_StickerSet = stickers.addStickerToSet({stickerset=InputStickerSet, sticker=InputStickerSetItem, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BOT_MISSING|This method can only be run by a bot|
|400|STICKERSET_INVALID|The provided sticker set is invalid|


