---
title: messages.getStickerSet
description: Get a stickerset
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getStickerSet  
[Back to methods index](index.md)


Get a stickerset

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | The stickerset to get | Optional|


### Return type: [messages\_StickerSet](../types/messages_StickerSet.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StickerSet = $MadelineProto->messages->getStickerSet(['stickerset' => InputStickerSet, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - messages.getStickerSet
* params - `{"stickerset": InputStickerSet, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.getStickerSet`

Parameters:

stickerset - Json encoded InputStickerSet




Or, if you're into Lua:

```lua
messages_StickerSet = messages.getStickerSet({stickerset=InputStickerSet, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|STICKERSET_INVALID|The provided sticker set is invalid|


