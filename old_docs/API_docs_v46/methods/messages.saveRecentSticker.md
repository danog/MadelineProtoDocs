---
title: messages.saveRecentSticker
description: Add/remove sticker from recent stickers list
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_saveRecentSticker.html
---
# Method: messages.saveRecentSticker
[Back to methods index](index.md)



Add/remove sticker from recent stickers list

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|attached|[Bool](../types/Bool.md) | Whether to add/remove stickers recently attached to photo or video files | Optional|
|id|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | Sticker | Optional|
|unsave|[Bool](../types/Bool.md) | Whether to save or unsave the sticker | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->saveRecentSticker(['attached' => Bool, 'id' => InputDocument, 'unsave' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.saveRecentSticker({attached=Bool, id=InputDocument, unsave=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|STICKER_ID_INVALID|The provided sticker ID is invalid|


