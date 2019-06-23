---
title: stickers.changeStickerPosition
description: Change sticker position in photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: stickers.changeStickerPosition  
[Back to methods index](index.md)


Change sticker position in photo

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|sticker|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | The sticker | Optional|
|position|[int](../types/int.md) | New position | Yes|


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

$messages_StickerSet = $MadelineProto->stickers->changeStickerPosition(['sticker' => InputDocument, 'position' => int, ]);
```

Or, if you're into Lua:

```lua
messages_StickerSet = stickers.changeStickerPosition({sticker=InputDocument, position=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|BOT_MISSING|This method can only be run by a bot|
|STICKER_INVALID|The provided sticker is invalid|


