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
|attached|[Bool](../types/Bool.md) | Get stickers attached to image? | Optional|
|id|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | The sticker | Optional|
|unsave|[Bool](../types/Bool.md) | Remove the sticker from recent stickers? | Yes|


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

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|STICKER_ID_INVALID|The provided sticker ID is invalid|


