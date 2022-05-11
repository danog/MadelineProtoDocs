---
title: "messages.sendEncryptedFile"
description: "Sends a message with a file attachment to a secret chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendEncryptedFile.html
---
# Method: messages.sendEncryptedFile
[Back to methods index](index.html)



Sends a message with a file attachment to a secret chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](/API_docs/types/Bool.html) | Whether to send the file without triggering a notification | Optional|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](/API_docs/types/InputEncryptedChat.html) | Secret chat ID | Yes|
|data|[bytes](/API_docs/types/bytes.html) | TL-serialization of [DecryptedMessage](../types/DecryptedMessage.html) type, encrypted with a key generated during chat initialization | Yes|
|file|[File path or InputEncryptedFile](/API_docs/types/InputEncryptedFile.html) | File attachment for the secret chat | Optional|


### Return type: [messages.SentEncryptedMessage](/API_docs/types/messages.SentEncryptedMessage.html)

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
$messages_SentEncryptedMessage = $MadelineProto->messages->sendEncryptedFile(silent: Bool, peer: InputEncryptedChat, data: 'bytes', file: InputEncryptedFile, );
```

