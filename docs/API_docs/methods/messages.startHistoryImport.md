---
title: "messages.startHistoryImport"
description: "Complete the [history import process](https://core.telegram.org/api/import), importing all messages into the chat.  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_startHistoryImport.html
---
# Method: messages.startHistoryImport
[Back to methods index](index.html)



Complete the [history import process](https://core.telegram.org/api/import), importing all messages into the chat.  
To be called only after initializing the import with [messages.initHistoryImport](../methods/messages.initHistoryImport.html) and uploading all files using [messages.uploadImportedMedia](../methods/messages.uploadImportedMedia.html).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The Telegram chat where the messages should be [imported, click here for more info »](https://core.telegram.org/api/import) | Optional|
|import\_id|[long](/API_docs/types/long.html) | Identifier of a history import session, returned by [messages.initHistoryImport](../methods/messages.initHistoryImport.html). | Yes|


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
$Bool = $MadelineProto->messages->startHistoryImport(peer: InputPeer, import_id: long, );
```

