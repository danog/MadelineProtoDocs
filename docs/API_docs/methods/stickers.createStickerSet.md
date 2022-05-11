---
title: "stickers.createStickerSet"
description: "Create a stickerset, bots only."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stickers_createStickerSet.html
---
# Method: stickers.createStickerSet
[Back to methods index](index.html)



Create a stickerset, bots only.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|masks|[Bool](/API_docs/types/Bool.html) | Whether this is a mask stickerset | Optional|
|animated|[Bool](/API_docs/types/Bool.html) | Whether this is an animated stickerset | Optional|
|videos|[Bool](/API_docs/types/Bool.html) | Whether this is a video stickerset | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Stickerset owner | Optional|
|title|[string](/API_docs/types/string.html) | Stickerset name, `1-64` chars | Yes|
|short\_name|[string](/API_docs/types/string.html) | Sticker set name. Can contain only English letters, digits and underscores. Must end with *"*by*<bot username="">"</bot>* (*<bot_username></bot_username>* is case insensitive); 1-64 characters | Yes|
|thumb|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Thumbnail | Optional|
|stickers|Array of [InputStickerSetItem](/API_docs/types/InputStickerSetItem.html) | Stickers | Yes|
|software|[string](/API_docs/types/string.html) | Used when [importing stickers using the sticker import SDKs](https://core.telegram.org/import-stickers), specifies the name of the software that created the stickers | Optional|


### Return type: [messages.StickerSet](/API_docs/types/messages.StickerSet.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_StickerSet = $MadelineProto->stickers->createStickerSet(masks: Bool, animated: Bool, videos: Bool, user_id: InputUser, title: 'string', short_name: 'string', thumb: InputDocument, stickers: [InputStickerSetItem, InputStickerSetItem], software: 'string', );
```

