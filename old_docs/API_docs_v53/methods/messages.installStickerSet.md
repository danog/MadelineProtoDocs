---
title: messages.installStickerSet
description: Install a stickerset
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.installStickerSet  
[Back to methods index](index.md)


Install a stickerset

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Stickerset to install | Optional|
|disabled|[Bool](../types/Bool.md) | Disable stickerset? | Yes|


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

$Bool = $MadelineProto->messages->installStickerSet(['stickerset' => InputStickerSet, 'disabled' => Bool, ]);
```

Or, if you're into Lua:

```lua
Bool = messages.installStickerSet({stickerset=InputStickerSet, disabled=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|STICKERSET_INVALID|The provided sticker set is invalid|


