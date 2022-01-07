---
title: "messages.uploadEncryptedFile"
description: "Upload encrypted file and associate it to a secret chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_uploadEncryptedFile.html
---
# Method: messages.uploadEncryptedFile
[Back to methods index](index.md)



Upload encrypted file and associate it to a secret chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Secret chat ID, Update, EncryptedMessage or InputEncryptedChat](../types/InputEncryptedChat.md) | The secret chat to associate the file to | Yes|
|file|[File path or InputEncryptedFile](../types/InputEncryptedFile.md) | The file | Optional|


### Return type: [EncryptedFile](../types/EncryptedFile.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$EncryptedFile = $MadelineProto->messages->uploadEncryptedFile(['peer' => InputEncryptedChat, 'file' => InputEncryptedFile, ]);
```

