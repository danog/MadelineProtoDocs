---
title: "messages.installStickerSet"
description: "Install a stickerset"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_installStickerSet.html
---
# Method: messages.installStickerSet
[Back to methods index](index.html)



Install a stickerset

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Stickerset to install | Optional|
|archived|[Bool](/API_docs/types/Bool.html) | Whether to archive stickerset | Yes|


### Return type: [messages.StickerSetInstallResult](/API_docs/types/messages.StickerSetInstallResult.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_StickerSetInstallResult = $MadelineProto->messages->installStickerSet(stickerset: InputStickerSet, archived: Bool, );
```

