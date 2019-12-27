---
title: messages.uninstallStickerSet
description: Uninstall a stickerset
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.uninstallStickerSet  
[Back to methods index](index.md)


Uninstall a stickerset

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | The stickerset to uninstall | Optional|


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

$Bool = $MadelineProto->messages->uninstallStickerSet(['stickerset' => InputStickerSet, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.uninstallStickerSet({stickerset=InputStickerSet, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|STICKERSET_INVALID|The provided sticker set is invalid|


