---
title: messages.saveRecentSticker
description: Add a sticker to recent stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.saveRecentSticker  
[Back to methods index](index.md)


Add a sticker to recent stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | The sticker | Optional|
|unsave|[Bool](../types/Bool.md) | Remove the sticker from recent stickers? | Yes|


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

$Bool = $MadelineProto->messages->saveRecentSticker(['id' => InputDocument, 'unsave' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.saveRecentSticker`

Parameters:

id - Json encoded InputDocument

unsave - Json encoded Bool




Or, if you're into Lua:

```
Bool = messages.saveRecentSticker({id=InputDocument, unsave=Bool, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|STICKER_ID_INVALID|The provided sticker ID is invalid|


