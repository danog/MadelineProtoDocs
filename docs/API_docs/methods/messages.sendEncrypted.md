---
title: "messages.sendEncrypted"
description: "Sends a text message to a secret chat."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendEncrypted.html
---
# Method: messages.sendEncrypted
[Back to methods index](index.html)



Sends a text message to a secret chat.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](/API_docs/types/Bool.html) | Send encrypted message without a notification | Optional|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](/API_docs/types/InputEncryptedChat.html) | Secret chat ID | Yes|
|data|[bytes](/API_docs/types/bytes.html) | TL-serialization of [DecryptedMessage](../types/DecryptedMessage.html) type, encrypted with a key that was created during chat initialization | Yes|


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
$messages_SentEncryptedMessage = $MadelineProto->messages->sendEncrypted(silent: Bool, peer: InputEncryptedChat, data: 'bytes', );
```

