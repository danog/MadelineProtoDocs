---
title: messages.installStickerSet
description: Add a sticker set
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.installStickerSet  
[Back to methods index](index.md)


Add a sticker set

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | The sticker set to add | Optional|
|disabled|[Bool](../types/Bool.md) | Disable stickerset? | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->installStickerSet(['stickerset' => InputStickerSet, 'disabled' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.installStickerSet`

Parameters:

stickerset - Json encoded InputStickerSet

disabled - Json encoded Bool




Or, if you're into Lua:

```
Bool = messages.installStickerSet({stickerset=InputStickerSet, disabled=Bool, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|STICKERSET_INVALID|The provided sticker set is invalid|


