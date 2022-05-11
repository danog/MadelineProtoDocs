---
title: "messages.faveSticker"
description: "Mark or unmark a sticker as favorite"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_faveSticker.html
---
# Method: messages.faveSticker
[Back to methods index](index.html)



Mark or unmark a sticker as favorite

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Sticker in question | Optional|
|unfave|[Bool](/API_docs/types/Bool.html) | Whether to add or remove a sticker from favorites | Yes|


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
$Bool = $MadelineProto->messages->faveSticker(id: InputDocument, unfave: Bool, );
```

