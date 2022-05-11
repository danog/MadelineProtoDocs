---
title: "messages.sendEncryptedService"
description: "Sends a service message to a secret chat."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendEncryptedService.html
---
# Method: messages.sendEncryptedService
[Back to methods index](index.html)



Sends a service message to a secret chat.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](/API_docs/types/InputEncryptedChat.html) | Secret chat ID | Yes|
|data|[bytes](/API_docs/types/bytes.html) | TL-serialization of  [DecryptedMessage](../types/DecryptedMessage.html) type, encrypted with a key generated during chat initialization | Yes|


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
$messages_SentEncryptedMessage = $MadelineProto->messages->sendEncryptedService(peer: InputEncryptedChat, data: 'bytes', );
```

