---
title: "messages.faveSticker"
description: "Mark a sticker as favorite"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_faveSticker.html
---
# Method: messages.faveSticker
[Back to methods index](index.html)



Mark a sticker as favorite

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|[MessageMedia, Update, Message or InputDocument](/API_docs/types/InputDocument.html) | Sticker to mark as favorite | Optional|
|unfave|[Bool](/API_docs/types/Bool.html) | Unfavorite | Yes|


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

$Bool = $MadelineProto->messages->faveSticker(['id' => InputDocument, 'unfave' => Bool, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|STICKER_ID_INVALID|The provided sticker ID is invalid|


