---
title: "messages.checkHistoryImportPeer"
description: "Check whether chat history exported from another chat app can be [imported into a specific Telegram chat, click here for more info »](https://core.telegram.org/api/import)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_checkHistoryImportPeer.html
---
# Method: messages.checkHistoryImportPeer
[Back to methods index](index.html)



Check whether chat history exported from another chat app can be [imported into a specific Telegram chat, click here for more info »](https://core.telegram.org/api/import).

If the check succeeds, and no RPC errors are returned, a [messages.CheckedHistoryImportPeer](../types/messages.CheckedHistoryImportPeer.html) constructor will be returned, with a confirmation text to be shown to the user, before actually initializing the import.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The chat where we want to [import history »](https://core.telegram.org/api/import). | Optional|


### Return type: [messages.CheckedHistoryImportPeer](/API_docs/types/messages.CheckedHistoryImportPeer.html)

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
$messages_CheckedHistoryImportPeer = $MadelineProto->messages->checkHistoryImportPeer(peer: InputPeer, );
```

