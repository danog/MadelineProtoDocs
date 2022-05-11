---
title: "messages.toggleStickerSets"
description: "Apply changes to multiple stickersets"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleStickerSets.html
---
# Method: messages.toggleStickerSets
[Back to methods index](index.html)



Apply changes to multiple stickersets

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|uninstall|[Bool](/API_docs/types/Bool.html) | Uninstall the specified stickersets | Optional|
|archive|[Bool](/API_docs/types/Bool.html) | Archive the specified stickersets | Optional|
|unarchive|[Bool](/API_docs/types/Bool.html) | Unarchive the specified stickersets | Optional|
|stickersets|Array of [InputStickerSet](/API_docs/types/InputStickerSet.html) | Stickersets to act upon | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->messages->toggleStickerSets(uninstall: Bool, archive: Bool, unarchive: Bool, stickersets: [InputStickerSet, InputStickerSet], );
```

