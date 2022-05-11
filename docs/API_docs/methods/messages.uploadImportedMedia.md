---
title: "messages.uploadImportedMedia"
description: "Upload a media file associated with an [imported chat, click here for more info »](https://core.telegram.org/api/import)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_uploadImportedMedia.html
---
# Method: messages.uploadImportedMedia
[Back to methods index](index.html)



Upload a media file associated with an [imported chat, click here for more info »](https://core.telegram.org/api/import).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The Telegram chat where the media will be imported | Optional|
|import\_id|[long](/API_docs/types/long.html) | Identifier of a [history import session](https://core.telegram.org/api/import), returned by [messages.initHistoryImport](../methods/messages.initHistoryImport.html) | Yes|
|file\_name|[string](/API_docs/types/string.html) | File name | Yes|
|media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | Media metadata | Optional|


### Return type: [MessageMedia](/API_docs/types/MessageMedia.html)

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
$MessageMedia = $MadelineProto->messages->uploadImportedMedia(peer: InputPeer, import_id: long, file_name: 'string', media: InputMedia, );
```

