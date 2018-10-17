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


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->stickers->changeStickerPosition(['sticker' => InputDocument, 'position' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - stickers.changeStickerPosition
* params - `{"sticker": InputDocument, "position": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/stickers.changeStickerPosition`

Parameters:

sticker - Json encoded InputDocument

position - Json encoded int




Or, if you're into Lua:

```lua
Bool = stickers.changeStickerPosition({sticker=InputDocument, position=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|BOT_MISSING|This method can only be run by a bot|
|STICKER_INVALID|The provided sticker is invalid|


