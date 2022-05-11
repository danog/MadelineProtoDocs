---
title: "messages.initHistoryImport"
description: "Import chat history from a foreign chat app into a specific Telegram chat, [click here for more info about imported chats »](https://core.telegram.org/api/import)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_initHistoryImport.html
---
# Method: messages.initHistoryImport
[Back to methods index](index.html)



Import chat history from a foreign chat app into a specific Telegram chat, [click here for more info about imported chats »](https://core.telegram.org/api/import).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The Telegram chat where the [history should be imported](https://core.telegram.org/api/import). | Optional|
|file|[File path or InputFile](/API_docs/types/InputFile.html) | File with messages to import. | Yes|
|media\_count|[int](/API_docs/types/int.html) | Number of media files associated with the chat that will be uploaded using [messages.uploadImportedMedia](../methods/messages.uploadImportedMedia.html). | Yes|


### Return type: [messages.HistoryImport](/API_docs/types/messages.HistoryImport.html)

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
$messages_HistoryImport = $MadelineProto->messages->initHistoryImport(peer: InputPeer, file: InputFile, media_count: int, );
```

