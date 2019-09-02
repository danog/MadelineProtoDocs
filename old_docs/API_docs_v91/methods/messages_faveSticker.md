---
title: messages.faveSticker
description: Add a sticker to favorites
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.faveSticker  
[Back to methods index](index.md)


Add a sticker to favorites

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputDocument](../types/InputDocument.md) | The sticker to add to favorites | Optional|
|unfave|[Bool](../types/Bool.md) | Remove it from favorites? | Yes|


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

$Bool = $MadelineProto->messages->faveSticker(['id' => InputDocument, 'unfave' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.faveSticker({id=InputDocument, unfave=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|STICKER_ID_INVALID|The provided sticker ID is invalid|


