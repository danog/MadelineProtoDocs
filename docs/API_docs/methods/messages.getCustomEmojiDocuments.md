---
title: "messages.getCustomEmojiDocuments"
description: "Fetch [custom emoji stickers »](https://core.telegram.org/api/custom-emoji)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getCustomEmojiDocuments.html
---
# Method: messages.getCustomEmojiDocuments
[Back to methods index](index.html)



Fetch [custom emoji stickers »](https://core.telegram.org/api/custom-emoji).

Returns a list of [documents](../constructors/document.html) with the animated custom emoji in TGS format, and a [documentAttributeCustomEmoji](../constructors/documentAttributeCustomEmoji.html) attribute with the original emoji and info about the emoji stickerset this custom emoji belongs to.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|document\_id|Array of [long](/API_docs/types/long.html) | [Custom emoji](https://core.telegram.org/api/custom-emoji) IDs from a [messageEntityCustomEmoji](../constructors/messageEntityCustomEmoji.html). | Yes|


### Return type: [Vector\_of\_Document](/API_docs/types/Document.html)

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
$Vector_of_Document = $MadelineProto->messages->getCustomEmojiDocuments(document_id: [long, long], );
```

