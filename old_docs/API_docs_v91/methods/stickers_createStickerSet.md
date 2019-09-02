---
title: stickers.createStickerSet
description: Create stickerset
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: stickers.createStickerSet  
[Back to methods index](index.md)


Create stickerset

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|masks|[Bool](../types/Bool.md) | Masks? | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user ID associated to this stickerset | Optional|
|title|[string](../types/string.md) | The stickerset title | Yes|
|short\_name|[string](../types/string.md) | The stickerset short name | Yes|
|stickers|Array of [InputStickerSetItem](../types/InputStickerSetItem.md) | The stickers to add | Yes|


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

$messages_StickerSet = $MadelineProto->stickers->createStickerSet(['masks' => Bool, 'user_id' => InputUser, 'title' => 'string', 'short_name' => 'string', 'stickers' => [InputStickerSetItem, InputStickerSetItem], ]);
```

Or, if you're into Lua:

```lua
messages_StickerSet = stickers.createStickerSet({masks=Bool, user_id=InputUser, title='string', short_name='string', stickers={InputStickerSetItem}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BOT_MISSING|This method can only be run by a bot|
|400|PACK_SHORT_NAME_INVALID|Short pack name invalid|
|400|PACK_SHORT_NAME_OCCUPIED|A stickerpack with this name already exists|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|STICKER_EMOJI_INVALID|Sticker emoji invalid|
|400|STICKER_FILE_INVALID|Sticker file invalid|
|400|STICKER_PNG_DIMENSIONS|Sticker png dimensions invalid|
|400|STICKERS_EMPTY|No sticker provided|
|400|USER_ID_INVALID|The provided user ID is invalid|


