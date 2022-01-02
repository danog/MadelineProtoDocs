---
title: "messages.installStickerSet"
description: "Install a stickerset"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_installStickerSet.html
---
# Method: messages.installStickerSet
[Back to methods index](index.md)



Install a stickerset

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Stickerset to install | Optional|
|archived|[Bool](../types/Bool.md) | Whether to archive stickerset | Yes|


### Return type: [messages.StickerSetInstallResult](../types/messages.StickerSetInstallResult.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_StickerSetInstallResult = $MadelineProto->messages->installStickerSet(['stickerset' => InputStickerSet, 'archived' => Bool, ]);
```

Or, if you're into Lua:

```lua
messages_StickerSetInstallResult = messages.installStickerSet({stickerset=InputStickerSet, archived=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|STICKERSET_INVALID|The provided sticker set is invalid|


